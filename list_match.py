import pandas as pd
import numpy as pn


teachers = ['coop', 'defect', 'tit1', 'tit0', 'saspic']

result_list = []
for index, t1 in enumerate(teachers):
    temp_list = []
    teachers_local = []
    teachers_local= list(teachers)
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

            if t2 == 'saspic':
                if index <= 1:
                    temp_list.append('C, D')
                else:
                    if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                        temp_list.append('C, C')
                    else:
                        temp_list.append('C, D')
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
            if t2 == 'saspic':
                if index <= 1:
                    temp_list.append('D, D')
                else:
                    if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                        temp_list.append('D, C')
                    else:
                        temp_list.append('D, D')
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
                        temp_list.append('C, C')
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
                            temp_list.append('D, C')
                        else:
                            temp_list.append('C, D')
            if index2 > 0:
                # print(index2-1)
                # print(temp_list[index2 - 1])
                # print(index2)
                # print(temp_list[index2 - 1][-1])
                if temp_list[index2-1][-1] == 'C':
                    print(temp_list[index2 - 1][-1])
                    print(t1, t2)
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
                    if t2 == 'saspic':
                        if index <= 1:
                            temp_list.append('C, D')
                        else:
                            if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                                temp_list.append('C, C')
                            else:
                                temp_list.append('C, D')
                if temp_list[index2 - 1][-1] == 'D':
                    print(temp_list[index2 - 1][-1])
                    print(t1, t2)
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
                    if t2 == 'saspic':
                        if index <= 1:
                            temp_list.append('D, D')
                        else:
                            if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                                temp_list.append('D, C')
                            else:
                                temp_list.append('D, D')
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
                if t2 == 'saspic':
                    if index <= 1:
                        temp_list.append('D, D')
                    else:
                        if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                            temp_list.append('D, C')
                        else:
                            temp_list.append('D, D')
            if index2 > 0:
                # print(index2-1)
                # print(temp_list[index2 - 1])
                # print(index2)
                # print(temp_list[index2 - 1][-1])
                if temp_list[index2-1][-1] == 'C':
                    print(temp_list[index2 - 1][-1])
                    print(t1, t2)
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
                    if t2 == 'saspic':
                        if index <= 1:
                            temp_list.append('C, D')
                        else:
                            if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                                temp_list.append('C, C')
                            else:
                                temp_list.append('C, D')
                if temp_list[index2 - 1][-1] == 'D':
                    print(temp_list[index2 - 1][-1])
                    print(t1, t2)
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
                    if t2 == 'saspic':
                        if index <= 1:
                            temp_list.append('D, D')
                        else:
                            if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                                temp_list.append('D, C')
                            else:
                                temp_list.append('D, D')
        if t1 == 'saspic':
            if index <= 1:
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
                if t2 == 'saspic':
                    if index <= 1:
                        temp_list.append('D, D')
                    else:
                        if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                            temp_list.append('D, C')
                        else:
                            temp_list.append('D, D')
            else:
                if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
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
                else:
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
                    if t2 == 'saspic':
                        if index <= 1:
                            temp_list.append('D, D')
                        else:
                            if result_list[index - 1][index2][0] == 'C' and result_list[index - 2][index2][0] == 'C':
                                temp_list.append('D, C')
                            else:
                                temp_list.append('D, D')
    result_list.append(temp_list)

