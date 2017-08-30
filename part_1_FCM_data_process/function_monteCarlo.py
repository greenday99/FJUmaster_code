# -*- coding:utf-8 -*-
# copyright: GU, MANQING

# 蒙地卡罗模拟法

import numpy as np
import math
import random


def getVaR(item_list, simulation_days, item_origin_price, CONFIDENCE_LIMIT, SIMULATE_TIMES):
    # 确定临界损益分布位置，向下取整
    select_position = int(SIMULATE_TIMES * (1 - CONFIDENCE_LIMIT))
    # 历史期间数
    his_days = len(item_list)
    item_array = np.array(item_list)
    item_mean = np.mean(item_array)  # 平均值
    item_std = np.std(item_array)  # 标准差

    # 存储模拟的数值
    sim_list = []

    for i in range(SIMULATE_TIMES + 1):
        value = item_origin_price * math.exp(
            ((item_mean - (math.pow(item_std, 2) / 2)) * math.exp(random.gauss(0, 1))) + item_std * random.gauss(0,1))
        sim_list.append(value)

    # 计算模拟后的损益分布
    sim_rate = []
    for i in range(len(sim_list) - 1):
        sub_rate = (sim_list[i + 1] - sim_list[i]) / sim_list[i]
        sim_rate.append(sub_rate)

    # 转换为array，并降序排序
    sim_rate_array = np.array(sim_rate)
    sim_rate_array.sort()

    # 确定临界损益分布
    rate = float(sim_rate_array[select_position])

    result = round(math.sqrt(simulation_days) * item_origin_price * rate, 2)

    return result
