# 历史模拟法

import numpy as np
import math


def getVaR(item_list, simulation_days, item_origin_price, CONFIDENCE_LIMIT):

    his_days = len(item_list)  # 历史期间
    select_position = int(his_days * (1 - CONFIDENCE_LIMIT))  # 确定临界损益分布位置，向下取整

    # 转换为array，并降序排序
    item_array = np.array(item_list)
    item_array.sort()

    # 确定临界损益分布
    rate = float(item_array[select_position])

    result = round(math.sqrt(simulation_days) * item_origin_price * rate, 2)

    return result
