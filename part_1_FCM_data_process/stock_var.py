# -*- coding:utf-8 -*-

# 计算历史模拟法和蒙地卡罗模拟法的VaR值
# 要求：在训练期中，至少要有230天的有效交易日
# 存储于 data/../csv 文件夹中
# 格式：股票代码，历史模拟法VaR，蒙地卡罗模拟法VaR

import os
import xlrd
import csv
from myThesis_new.part_1_FCM_data_process import function_hissimulation as simulation_his
from myThesis_new.part_1_FCM_data_process import function_monteCarlo as simulation_mont

# 获取目标文件夹位置
osPath = os.path.dirname(os.getcwd()) + '/data/'
# 待处理文件夹
var_file_path = ['stock_SH_var/', 'stock_SZ_var/']
# 商品初始价格存储文件夹
origin_price_file_name = 'var_original_price/'
# 待处理文件名
period = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
          '19', '20']
sub_period = ['_0', '_1', '_2', '_3', '_4', '_5']
page = ['_0', '_1']
# 输出文件夹
output_file_path_csv = 'csv/'
# 两个后缀名
xls_ext_name = '.xls'
csv_ext_name = '.csv'
# 有效交易日期的设定
VALIDE_DAYS = 230
# 模拟置信区间
CONFIDENCE_LIMIT = 0.95
# 蒙地卡罗模拟次数
SIMULATE_TIMES = 10000

# 获取所有研究期间的估算期间
sim_days = {}
sim_file_path = osPath + 'simulation_days.csv'
sim_file = open(sim_file_path, 'r')
reader = csv.reader(sim_file)
for row in reader:
    sim_days[row[0]] = int(row[1])

for sub_var_file_path in var_file_path:
    for period_name in period:
        # 获取当期的估算期间
        now_sim_days = sim_days[period_name]

        # 获取当期所有商品的初始资产价格
        origin_price = {}
        origin_price_file_path = osPath + sub_var_file_path + origin_price_file_name + period_name + xls_ext_name
        origin_price_file = xlrd.open_workbook(origin_price_file_path)
        price_table = origin_price_file.sheets()[0]
        price_table_rows = price_table.nrows
        for i in range(1, price_table_rows):
            row = price_table.row_values(i)
            origin_price[row[0]] = float(row[1])

        # 用来存储当期研究期间的所有股票的var值
        period_list = []
        period_list.append(['item_id', 'unadjusted_var', 'adjusted_var'])

        for sub_period_name in sub_period:

            # 用来存储当前股票的资料
            now_item = []
            # 用来判断是否到达下一个股票的资料
            item_id_now = ''
            item_id_previous = ''

            # 输入的文件地址
            input_file_path_0 = osPath + sub_var_file_path + period_name + sub_period_name + page[0] + xls_ext_name
            input_file_path_1 = osPath + sub_var_file_path + period_name + sub_period_name + page[1] + xls_ext_name

            # 打开相应的文件，若无，则跳出该循环
            try:
                open_input_file_0 = xlrd.open_workbook(input_file_path_0)
            except:
                break

            table_0 = open_input_file_0.sheets()[0]
            table_rows_0 = table_0.nrows

            # period为02、03、04的要单独处理
            if period_name == '02' or period_name == '03' or period_name == '04':
                special_item_list = {}  # 存储第二个page中的各股票资料
                open_input_file_1 = xlrd.open_workbook(input_file_path_1)
                table_1 = open_input_file_1.sheets()[0]
                table_rows_1 = table_1.nrows

                for k in range(1, table_rows_1):
                    row_1 = table_1.row_values(k)
                    if row_1[0] in special_item_list.keys():
                        if row_1[2] != '':
                            special_item_list[row_1[0]].append(row_1[2])
                    else:
                        special_item_list[row_1[0]] = []
                        if row_1[2] != '':
                            special_item_list[row_1[0]].append(row_1[2])

            for i in range(1, table_rows_0):
                row = table_0.row_values(i)
                item_id_now = str(row[0])

                # 第一条记录
                if item_id_previous == '':
                    item_id_previous = item_id_now
                    if row[2] != '':
                        now_item.append(float(row[2]))
                # 同一个商品，并且不是最后一条记录
                if item_id_previous == item_id_now and i != table_rows_0 - 1:
                    if row[2] != '':
                        now_item.append(float(row[2]))
                # 同一个商品，并且是最后一条记录
                if item_id_previous == item_id_now and i == table_rows_0 - 1:
                    if row[2] != '':
                        now_item.append(float(row[2]))
                    # period为02、03、04时需要将page2加入
                    if period_name == '02' or period_name == '03' or period_name == '04':
                        now_item += special_item_list[item_id_now]
                    # 计算商品的有效交易天数是否满足要求
                    if len(now_item) > VALIDE_DAYS:
                        # 满足，则开始计算VaR值
                        # 获取这个商品的初始资产价格
                        item_origin_price = origin_price[item_id_now]
                        unadjuested_var = simulation_his.getVaR(now_item, now_sim_days, item_origin_price,
                                                                CONFIDENCE_LIMIT)
                        adjuested_var = simulation_mont.getVaR(now_item, now_sim_days, item_origin_price,
                                                               CONFIDENCE_LIMIT, SIMULATE_TIMES)
                        # 将结果放入period_list中
                        period_list.append([item_id_now, unadjuested_var, adjuested_var])
                # 这个商品全部读取完毕
                if item_id_previous != item_id_now:
                    # period为02、03、04时需要将page2加入
                    if period_name == '02' or period_name == '03' or period_name == '04':
                        now_item += special_item_list[item_id_previous]
                    # 计算商品的有效交易天数是否满足要求
                    if len(now_item) < VALIDE_DAYS:
                        # 不满足，则这个商品不计算，开始记录下一个商品
                        item_id_previous = item_id_now
                        now_item = []
                        if row[2] != '':
                            now_item.append(float(row[2]))
                    else:
                        # 获取这个商品的初始资产价格
                        try:
                            item_origin_price = origin_price[item_id_previous]
                            unadjuested_var = simulation_his.getVaR(now_item, now_sim_days, item_origin_price,
                                                                    CONFIDENCE_LIMIT)
                            adjuested_var = simulation_mont.getVaR(now_item, now_sim_days, item_origin_price,
                                                                   CONFIDENCE_LIMIT, SIMULATE_TIMES)
                        except:
                            print(input_file_path_0)
                            print(item_id_previous)
                            print(now_item)
                            exit(1)
                        # 将结果放入period_list中
                        period_list.append([item_id_now, unadjuested_var, adjuested_var])
                        # 开始记录下一个商品
                        now_item = []
                        item_id_previous = item_id_now
                        if row[2] != '':
                            now_item.append(float(row[2]))

        # 当期资料全部计算完毕，存入csv中
        output_file_path = osPath + sub_var_file_path + output_file_path_csv + period_name + csv_ext_name
        output = open(output_file_path, 'w')
        writer = csv.writer(output)
        writer.writerows(period_list)

        print('success: ' + str(output_file_path))
