# -*- coding:utf-8 -*-
# copyright: GU, MANQING

# 计算beta值
# 要求：在训练期中，至少要有230天的有效交易日
# 记录基金及其对应的基金种类ETF or LOF，放置于 data/../fund_type 文件夹中
# 格式：基金代码，基金种类(2: LOF; 3: ETF)
# 处理完毕的基金及其beta值，放置于 data/../csv 文件夹中
# 格式：基金代码，基金名称，基金种类，beta

import os
import xlrd
import csv
import numpy as np
import math

# 获取目标文件夹位置
osPath = os.path.dirname(os.getcwd()) + '/data/'
# 待处理文件夹
beta_file_path = ['fund_SH_beta/', 'fund_SZ_beta/']
# 基金种类名
type_name = ['ETF_', 'LOF_']
# 待处理文件名
period = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
          '19', '20']
# 输出文件夹
output_file_path_type = 'fund_type/'
output_file_path_csv = 'csv/'
# 用来存储不同市场，各研究期间的基金代码文件名称
beta_file_name = ['fund_beta2var_SH', 'fund_beta2var_SZ']
# 两个后缀名
xls_ext_name = '.xls'
csv_ext_name = '.csv'
# 有效交易日期的设定
VALIDE_DAYS = 230


# beta计算公式
def getBeta(item_rate, hs300_rate):
    item_rate_array = np.array(item_rate)
    hs300_rate_array = np.array(hs300_rate)

    # 样本区间内所含的交易天数
    n = len(item_rate)
    # 沪深300涨跌幅 × 基金净值增长率之和
    part_a = np.sum(item_rate_array * hs300_rate_array)
    # 沪深300指数涨跌幅之和
    part_b = np.sum(hs300_rate_array)
    # 基金净值增长率之和
    part_c = np.sum(item_rate_array)
    # 沪深300指数涨跌幅平方之和
    part_d = np.sum(hs300_rate_array * hs300_rate_array)
    # 基金净值增长率之和的平方
    part_e = math.pow(np.sum(hs300_rate_array), 2)

    # 计算beta
    result = ((n * part_a) - (part_b * part_c)) / ((n * part_d) - part_e)
    return result


# 开始计算每个文件基金的beta
for k in range(len(beta_file_path)):
    sub_beta_file_path = beta_file_path[k]
    # 将每个研究期间的股票代码存储下来，用于获取var资料
    list_id = []

    for period_name in period:

        # 将当前的基金种类和研究期间存入list_id
        list_id.append([period_name])

        # 用来存储当期研究期间的所有基金的beta值
        period_list = []
        period_list.append(['item_id', 'item_name', 'item_type', 'beta'])

        # 用来储存当期研究期间的所有基金的种类
        type_list = []
        type_list.append(['item_id', 'item_type'])

        for type in type_name:

            input_file_path = osPath + sub_beta_file_path + type + period_name + xls_ext_name

            # 档案读取，如果出错，则代表已没有该文件，需要跳出循环
            try:
                open_input_file = xlrd.open_workbook(input_file_path)
            except:
                break
            table = open_input_file.sheets()[0]
            table_rows = table.nrows

            # 用来存储当前基金的日净值增长率
            now_item_rate = []
            # 用来存储当前日期的沪深300指数涨跌幅
            now_hs300_rate = []
            # 用来判断是否到达下一个基金的资料
            item_id_now = ''
            item_id_previous = ''

            for i in range(1, table_rows):
                row = table.row_values(i)
                item_id_now = str(row[0])

                # 第一条记录
                if item_id_previous == '':
                    item_id_previous = item_id_now
                    if row[3] != '':
                        now_item_rate.append(float(row[3]))
                        now_hs300_rate.append(float(row[4]))
                # 同一个商品，并且不是最后一条记录
                if item_id_previous == item_id_now and i != table_rows - 1:
                    if row[3] != '':
                        now_item_rate.append(float(row[3]))
                        now_hs300_rate.append(float(row[4]))
                # 同一个商品，并且是最后一条记录
                if item_id_previous == item_id_now and i == table_rows - 1:
                    if row[3] != '':
                        now_item_rate.append(float(row[3]))
                        now_hs300_rate.append(float(row[4]))
                    # 计算商品的有效交易天数是否满足要求
                    if len(now_item_rate) > VALIDE_DAYS:
                        # 满足，则开始计算beta值
                        beta_value = getBeta(now_item_rate, now_hs300_rate)
                        # 确认基金种类
                        if type == 'ETF_':
                            item_type = 3
                        if type == 'LOF_':
                            item_type = 2
                        # 放入period_list中
                        period_list.append([item_id_previous, row[1], item_type, beta_value])
                        # 放入type_list中
                        type_list.append([item_id_previous, item_type])
                # 这个商品全部读取完毕
                if item_id_previous != item_id_now:
                    # 计算商品的有效交易天数是否满足要求
                    if len(now_item_rate) > VALIDE_DAYS:
                        # 满足，则开始计算beta值
                        beta_value = getBeta(now_item_rate, now_hs300_rate)
                        # 确认基金种类
                        if type == 'ETF_':
                            item_type = 3
                        if type == 'LOF_':
                            item_type = 2
                        # 放入period_list中
                        period_list.append([item_id_previous, table.row_values(i - 1)[1], item_type, beta_value])
                        # 放入type_list中
                        type_list.append([item_id_previous, item_type])

                    # 开始记录下一个商品
                    now_item_rate = []
                    now_hs300_rate = []
                    item_id_previous = item_id_now
                    if row[3] != '':
                        now_item_rate.append(float(row[3]))
                        now_hs300_rate.append(float(row[4]))

        # 当期资料全部计算完毕，存入csv中
        output_file_path_period = osPath + sub_beta_file_path + output_file_path_csv + period_name + csv_ext_name
        output = open(output_file_path_period, 'w')
        writer = csv.writer(output)
        writer.writerows(period_list)

        output_file_type_path = osPath + sub_beta_file_path + output_file_path_type + period_name + csv_ext_name
        output = open(output_file_type_path, 'w')
        writer = csv.writer(output)
        writer.writerows(type_list)

        print('success：' + str(output_file_path_period))

        # 将该期的id存入list_id中
        ids = []
        for h in range(1, len(period_list)):
            ids.append(period_list[h][0])
        list_id.append(ids)

    # 将list_id存储
    output_file_path = osPath + beta_file_name[k] + csv_ext_name
    output = open(output_file_path, 'w')
    writer = csv.writer(output)
    writer.writerows(list_id)

    print('ok: ' + str(output_file_path))
