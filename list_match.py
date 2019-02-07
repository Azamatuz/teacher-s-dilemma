import pandas as pd
import numpy as pn
from random import shuffle


teachers = ['coop', 'defect', 'tit1', 'tit0', 'disap']*20
shuffle_list = teachers[:]
shuffle(shuffle_list)
print(shuffle_list)

result_list = []
for index, t1 in enumerate(shuffle_list):
    temp_list = []
    teachers_local = []
    teachers_local = list(teachers)
    teachers_local.remove(t1)
    for index2, t2 in enumerate(teachers_local):
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

            if t2 == 'disap':
                if index <= 1:
                    temp_list.append('C, C')
                else:
                    if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                        temp_list.append('C, D')
                    else:
                        temp_list.append('C, C')
        if t1 == 'defect':
            if t2 == 'coop':
                temp_list.append('D, C')
            if t2 == 'defect':
                temp_list.append('D, D')
            if t2 == 'tit1':
                if index == 0:
                    temp_list.append('D, C')
                else:
                    if result_list[index - 1][index2][0] == 'D':
                        temp_list.append('D, D')
                    else:
                        temp_list.append('D, C')
            if t2 == 'tit0':
                if index == 0:
                    temp_list.append('D, D')
                else:
                    if result_list[index - 1][index2][0] == 'D':
                        temp_list.append('D, D')
                    else:
                        temp_list.append('D, C')
            if t2 == 'disap':
                if index <= 1:
                    temp_list.append('D, C')
                else:
                    if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                        temp_list.append('D, D')
                    else:
                        temp_list.append('D, C')

        if t1 == 'tit1':
            if index2 == 0:
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
                if t2 == 'disap':
                    if index <= 1:
                        temp_list.append('C, C')
                    else:
                        if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':

                            temp_list.append('C, D')
                        else:
                            temp_list.append('C, C')

            if index2 > 0:
                if temp_list[index2-1][-1] == 'C':
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
                        if index > 0:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('C, D')
                            else:
                                temp_list.append('C, C')
                    if t2 == 'disap':
                        if index <= 1:
                            temp_list.append('C, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':

                                temp_list.append('C, D')
                            else:
                                temp_list.append('C, C')

                if temp_list[index2 - 1][-1] == 'D':
                    if t2 == 'coop':
                        temp_list.append('D, C')
                    if t2 == 'defect':
                        temp_list.append('D, D')
                    if t2 == 'tit1':
                        if index == 0:
                            temp_list.append('D, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
                    if t2 == 'tit0':
                        if index == 0:
                            temp_list.append('D, D')
                        else:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
                    if t2 == 'disap':
                        if index <= 1:
                            temp_list.append('D, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
        if t1 == 'tit0':
            if index2 == 0:
                if t2 == 'coop':
                    temp_list.append('D, C')
                if t2 == 'defect':
                    temp_list.append('D, D')
                if t2 == 'tit1':
                    if index == 0:
                        temp_list.append('D, C')
                    else:
                        if result_list[index - 1][index2][0] == 'D':
                            temp_list.append('D, D')
                        else:
                            temp_list.append('D, C')
                if t2 == 'tit0':
                    if index == 0:
                        temp_list.append('D, D')
                    else:
                        if result_list[index - 1][index2][0] == 'D':
                            temp_list.append('D, D')
                        else:
                            temp_list.append('D, C')
                if t2 == 'disap':
                    if index <= 1:
                        temp_list.append('D, C')
                    else:
                        if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                            temp_list.append('D, D')
                        else:
                            temp_list.append('D, C')
            if index2 > 0:
                if temp_list[index2-1][-1] == 'C':
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
                        if index > 0:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('C, D')
                            else:
                                temp_list.append('C, C')
                    if t2 == 'disap':
                        if index <= 1:
                            temp_list.append('C, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                                temp_list.append('C, D')
                            else:
                                temp_list.append('C, C')
                if temp_list[index2 - 1][-1] == 'D':
                    if t2 == 'coop':
                        temp_list.append('D, C')
                    if t2 == 'defect':
                        temp_list.append('D, D')
                    if t2 == 'tit1':
                        if index == 0:
                            temp_list.append('D, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
                    if t2 == 'tit0':
                        if index == 0:
                            temp_list.append('D, D')
                        else:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
                    if t2 == 'disap':
                        if index <= 1:
                            temp_list.append('D, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
        if t1 == 'disap':
            if index < 2:
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
                if t2 == 'disap':
                    if index <= 1:
                        temp_list.append('C, C')
                    else:
                        if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                            temp_list.append('C, D')
                        else:
                            temp_list.append('C, C')
            else:
                if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                    if t2 == 'coop':
                        temp_list.append('D, C')
                    if t2 == 'defect':
                        temp_list.append('D, D')
                    if t2 == 'tit1':
                        if index == 0:
                            temp_list.append('D, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
                    if t2 == 'tit0':
                        if index == 0:
                            temp_list.append('D, D')
                        else:
                            if result_list[index - 1][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')

                    if t2 == 'disap':
                        if index <= 1:
                            temp_list.append('C, D')
                        else:
                            if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                                temp_list.append('D, D')
                            else:
                                temp_list.append('D, C')
                else:
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
                    if t2 == 'disap':
                        if index <= 1:
                            temp_list.append('C, C')
                        else:
                            if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                                temp_list.append('C, D')
                            else:
                                temp_list.append('C, C')
    result_list.append(temp_list)

print(len(result_list))
for i in range(99):
    print('###########')
    for j in range(99):
        if i == j:
            print('0')
        else:
            print(result_list[i][j])