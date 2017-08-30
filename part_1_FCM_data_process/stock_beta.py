# -*- coding:utf-8 -*-
# copyright: GU, MANQING

# 剔除建筑业类、金融业类的股票 'E' 'J'
# 将本期与下一期的股票代码比较，删去下一期没有的股票代码 -> 保证股票在整个研究期间内都有数据
# 记录股票及其对应的股票门类，放置于 data/../stock_type 文件夹中
# 格式：股票代码，门类代码
# 处理完毕的股票及其beta值，放置于 data/../csv 文件夹中
# 格式：股票代码，股票名称，门类代码，beta

import os
import xlrd
import csv

# 获取目标文件夹位置
osPath = os.path.dirname(os.getcwd()) + '/data/'
# 待处理文件夹
beta_file_path = ['stock_SH_beta/', 'stock_SZ_beta/']
# 待处理文件名
period = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
          '19', '20', '21']
# 输出文件夹
output_file_path_type = 'stock_type/'
output_file_path_csv = 'csv/'
# 用来存储不同市场，各研究期间的股票代码文件名称
beta_file_name = ['stock_beta2var_SH', 'stock_beta2var_SZ']
# 两个后缀名
xls_ext_name = '.xls'
csv_ext_name = '.csv'

for k in range(len(beta_file_path)):
    sub_beta_file_path = beta_file_path[k]
    # 将每个研究期间的股票代码存储下来，用于获取var资料
    list_id = []
    for i in range(len(period) - 1):
        period_name_now = period[i]  # 目前要处理的研究期间名称
        period_name_next = period[i + 1]  # 需要进行相互比较的研究期间名称

        input_file_name_now = osPath + sub_beta_file_path + period_name_now + xls_ext_name
        input_file_name_next = osPath + sub_beta_file_path + period_name_next + xls_ext_name

        list_id.append([period_name_now]) # 存储当前的研究期间

        # 先处理目前的研究期间，剔除2类股票
        open_file_now = xlrd.open_workbook(input_file_name_now)
        table_now = open_file_now.sheets()[0]
        table_now_rows = table_now.nrows
        list_now = []  # 用于存储目前研究期间的数据
        for i in range(table_now_rows):
            row_now = table_now.row_values(i)
            if i != 0:
                if row_now[2] == 'E' or row_now[2] == 'J':
                    continue
            list_now.append([row_now[0], row_now[1], row_now[2], row_now[4]])

        # 打开要互相比较的研究期间
        open_file_next = xlrd.open_workbook(input_file_name_next)
        table_next = open_file_next.sheets()[0]
        table_next_rows = table_next.nrows
        list_next = []  # 用于存储下一个研究期间的数据
        for i in range(table_next_rows):
            row_next = table_next.row_values(i)
            list_next.append(row_next)

        # 两者比较，得出最终结果
        final_list = []
        final_list.append(list_now[0])
        for i in range(1, len(list_now)):
            for j in range(1, len(list_next)):
                if list_now[i][0] in list_next[j]:
                    final_list.append(list_now[i])
                    break

        # 将最终结果final_list存储
        output_file_path = osPath + sub_beta_file_path + output_file_path_csv + period_name_now + csv_ext_name
        output = open(output_file_path, 'w')
        writer = csv.writer(output)
        writer.writerows(final_list)

        # 提炼出 股票编号，股票门类 并存储
        list_type = []
        sub_list_id = []
        for i in range(len(final_list)):
            list_type.append([final_list[i][0], final_list[i][2]])
            if i != 0:
                sub_list_id.append(final_list[i][0])
        list_id.append(sub_list_id) # 存储当前研究期间的股票代码

        # 将最终结果list_type存储
        output_file_path = osPath + sub_beta_file_path + output_file_path_type + period_name_now + csv_ext_name
        output = open(output_file_path, 'w')
        writer = csv.writer(output)
        writer.writerows(list_type)

        print('success：' + str(output_file_path))

    # 将list_id 存储
    output_file_path = osPath + beta_file_name[k] + csv_ext_name
    output = open(output_file_path, 'w')
    writer = csv.writer(output)
    writer.writerows(list_id)

    print('ok:' + str(output_file_path))
