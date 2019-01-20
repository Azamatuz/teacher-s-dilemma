import pandas as pd
import numpy as pn


teachers = ['coop', 'defect', 'tit1', 'tit0', 'saspic']

result_list = []
for index, t1 in enumerate(teachers):
    temp_list = []
    for index2, t2 in enumerate(teachers):
        if t1 == 'coop':
            if t2 == 'coop':
                temp_list.append('C, C')
            if t2 == 'defect':
                temp_list.append('C, D')
            if t2 == 'tit1':
                if index == 0:
                    temp_list.append('C, C')
                else:
                    if result_list[index - 1][index2][0] == 'D':
                        temp_list.append('C, D')
                    else:
                        temp_list.append('C, C')
            if t2 == 'tit0':
                if index == 0:
                    temp_list.append('C, D')
                else:
                    if result_list[index - 1][index2][0] == 'D':
                        temp_list.append('C, D')
                    else:
                        temp_list.append('C, C')

            if t2 == 'saspic':
                if index <= 1:
                    temp_list.append('C, D')
                else:
                    if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                        temp_list.append('C, C')
                    else:
                        temp_list.append('C, D')

    result_list.append(temp_list)

