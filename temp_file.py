
if t1 == 'defect' and t2 == 'coop':
    temp_list.append('D, C')
if t1 == 'defect' and t2 == 'defect':
    temp_list.append('D, D')
if t1 == 'defect' and t2 == 'tit1':
    if index != 0:
        if result_list[index - 1][index2][0] == 'D':
            temp_list.append('D, D')
        else:
            temp_list.append('D, C')
if t1 == 'defect' and t2 == 'tit0':
    if index != 0:
        if result_list[index - 1][index2][0] == 'D':
            temp_list.append('D, D')
        else:
            temp_list.append('D, C')
if t1 == 'defect' and t2 == 'saspic':
    if index >= 1:
        if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
            temp_list.append('D, D')
        else:
            temp_list.append('D, C')

if t1 == 'tit1' and index2 == 0:
    if t1 == 'tit1' and t2 == 'coop':
        temp_list.append('C, C')
    if t1 == 'tit1' and t2 == 'defect':
        temp_list.append('C, D')
    if t1 == 'tit1' and t2 == 'tit1':
        if index != 0:
            if result_list[index - 1][index2][0] == 'D':
                temp_list.append('C, D')
            else:
                temp_list.append('C, C')
    if t1 == 'tit1' and t2 == 'tit0':
        if index != 0:
            if result_list[index - 1][index2][0] == 'D':
                temp_list.append('C, D')
            else:
                temp_list.append('C, C')
    if t1 == 'tit1' and t2 == 'saspic':
        if index >= 1:
            if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                temp_list.append('C, D')
            else:
                temp_list.append('C, C')
elif t1 == 'tit1' and index2 >= 1:
    print(index2)
    print(temp_list[index2 - 1])
    print(index2)
    print(temp_list[index2 - 1][-1])
    if temp_list[index2 - 1][-1] == 'D':
        print(temp_list[index2 - 1][-1])
        print(t1, t2)
        if t1 == 'tit1' and t2 == 'coop':
            temp_list.append('D, C')
        if t1 == 'tit1' and t2 == 'defect':
            temp_list.append('D, D')
        if t1 == 'tit1' and t2 == 'tit1':
            if index != 0:
                if result_list[index - 1][index2][0] == 'D':
                    temp_list.append('D, D')
                else:
                    temp_list.append('D, C')
        if t1 == 'tit1' and t2 == 'tit0':
            if index != 0:
                if result_list[index - 1][index2][0] == 'D':
                    temp_list.append('D, D')
                else:
                    temp_list.append('D, C')
        if t1 == 'tit1' and t2 == 'saspic':
            if index >= 1:
                if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                    temp_list.append('D, D')
                else:
                    temp_list.append('D, C')
    elif temp_list[index2 - 1][-1] == 'C':
        if t1 == 'tit1' and t2 == 'coop':
            temp_list.append('C, C')
        if t1 == 'tit1' and t2 == 'defect':
            temp_list.append('C, D')
        if t1 == 'tit1' and t2 == 'tit1':
            if index != 0:
                if result_list[index - 1][index2][0] == 'D':
                    temp_list.append('C, D')
                else:
                    temp_list.append('C, C')
        if t1 == 'tit1' and t2 == 'tit0':
            if index != 0:
                if result_list[index - 1][index2][0] == 'D':
                    temp_list.append('C, D')
                else:
                    temp_list.append('C, C')
        if t1 == 'tit1' and t2 == 'saspic':
            if index >= 1:
                if result_list[index - 1][index2][0] == 'D' and result_list[index - 2][index2][0] == 'D':
                    temp_list.append('C, D')
                else:
                    temp_list.append('C, C')

# print(result_list[index])
