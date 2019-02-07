import pandas as pd
from random import shuffle


teachers = ['coop', 'def', 'tit1', 'tit0', 'tit1', 'def', 'tit0', 'coop', 'tit0', 'def', 'tit1', 'coop']
# this order works: teachers = ['coop', 'def', 'tit1', 'tit0', 'tit1', 'def', 'tit0', 'coop', 'tit0', 'def', 'tit1', 'coop']
# teachers = ['tit1', 'def', 'tit0', 'coop']

shuffle_list = teachers[:]
shuffle(shuffle_list)
teachers = teachers + shuffle_list * 3
df = pd.DataFrame(columns=teachers, index=teachers)
# df = pd.DataFrame(columns=shuffle_list, index=shuffle_list)


for i in range(len(teachers)):
    for j in range(len(teachers)):

        if i == j:
            df.iloc[i][j] = '0,0'
        else:
            if df.columns[i] == 'coop':
                if df.index[j] == 'coop':
                    df.iloc[i][j] = 'C, C'
                if df.index[j] == 'def':
                    df.iloc[i][j] = 'C, D'
                if df.index[j] == 'tit1':
                    if i == 0:
                        df.iloc[i][j] = 'C, C'
                    else:
                        if df.iloc[i-1][j][-1] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = 'C, D'
                            if df.iloc[i - 2][j][0] == 'C':
                                df.iloc[i][j] = 'C, C'
                        else:
                            if df.iloc[i-1][j][0] == 'D':
                                df.iloc[i][j] = 'C, D'
                            if df.iloc[i-1][j][0] == 'C':
                                df.iloc[i][j] = 'C, C'

                if df.index[j] == 'tit0':
                    if i == 0:
                        df.iloc[i][j] = 'C, D'
                    else:
                        if df.iloc[i-1][j][-1] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = 'C, D'
                            if df.iloc[i - 2][j][0] == 'C':
                                df.iloc[i][j] = 'C, C'
                        else:
                            if df.iloc[i-1][j][0] == 'D':
                                df.iloc[i][j] = 'C, D'
                            if df.iloc[i-1][j][0] == 'C':
                                df.iloc[i][j] = 'C, C'

# Defencer case
            if df.columns[i] == 'def':
                if df.index[j] == 'coop':
                    df.iloc[i][j] = 'D, C'
                if df.index[j] == 'def':
                    df.iloc[i][j] = 'D, D'
                if df.index[j] == 'tit1':
                    if i == 0 or (i == 1 and df.iloc[i-1][j][0] == '0'):
                        df.iloc[i][j] = 'D, C'
                    else:
                        if df.iloc[i-1][j][0] == 'D':
                            df.iloc[i][j] = 'D, D'
                        if df.iloc[i-1][j][0] == 'C':
                            df.iloc[i][j] = 'D, C'
                        if df.iloc[i-1][j][0] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = 'D, D'
                            if df.iloc[i - 2][j][0] == 'C':
                                df.iloc[i][j] = 'D, C'
                if df.index[j] == 'tit0':
                    if j == 0 or (i == 1 and df.iloc[i-1][j][0] == '0'):
                        df.iloc[i][j] = 'D, D'
                    if j >= 1:
                        if df.iloc[i-1][j][0] == 'D':
                            df.iloc[i][j] = 'D, D'
                        if df.iloc[i-1][j][0] == 'C':
                            df.iloc[i][j] = 'D, C'
                        if df.iloc[i-1][j][0] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = 'D, D'
                            if df.iloc[i - 2][j][0] == 'C':
                                df.iloc[i][j] = 'D, C'

# Tit1 case
            if df.columns[i] == 'tit1':
                if j == 0 or (j == 1 and df.iloc[i][j - 1][0] == '0'):
                    if df.index[j] == 'coop':
                        df.iloc[i][j] = 'C, C'
                    if df.index[j] == 'def':
                        df.iloc[i][j] = 'C, D'
                    if df.index[j] == 'tit1':
                        if i == 0:
                            df.iloc[i][j] = 'C, C'
                        else:
                            if df.iloc[i-1][j][-1] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i - 2][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'
                            else:
                                if df.iloc[i-1][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i-1][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'

                    if df.index[j] == 'tit0':
                        if i == 0 or (i == 1 and df.iloc[i-1][j][0] == '0'):
                            df.iloc[i][j] = 'C, D'
                        else:
                            if df.iloc[i-1][j][-1] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i - 2][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'
                            else:
                                if df.iloc[i-1][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i-1][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'
                else:
                    if df.iloc[i][j - 1][-1] == 'D':

                        if df.index[j] == 'coop':
                            df.iloc[i][j] = 'D, C'
                        if df.index[j] == 'def':
                            df.iloc[i][j] = 'D, D'
                        if df.index[j] == 'tit1':
                            if i == 0:
                                df.iloc[i][j] = 'D, C'
                            if i == 1:
                                if df.iloc[i - 1][j][0] == '0':
                                    df.iloc[i][j] = 'D, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'
                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'

                        if df.index[j] == 'tit0':

                            if i == 0:

                                df.iloc[i][j] = 'D, D'
                            if i >= 1:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i][j - 2][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i][j - 2][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'D, C'

                    if df.iloc[i][j - 1][-1] == 'C':

                        if df.index[j] == 'coop':
                            df.iloc[i][j] = 'C, C'
                        if df.index[j] == 'def':
                            df.iloc[i][j] = 'C, D'
                        if df.index[j] == 'tit1':
                            if i == 0 or (i == 1 and df.iloc[i - 1][j][0] == '0'):
                                df.iloc[i][j] = 'C, C'

                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'

                        if df.index[j] == 'tit0':
                            if i == 0 or (i == 1 and df.iloc[i-1][j][0] == '0'):
                                df.iloc[i][j] = 'C, D'
                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i][j - 2][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i][j - 2][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                    if df.iloc[i][j - 1][0] == '0':
                        if df.iloc[i][j - 2][-1] == 'D':
                            if df.index[j] == 'coop':
                                df.iloc[i][j] = 'D, C'
                            if df.index[j] == 'def':
                                df.iloc[i][j] = 'D, D'
                            if df.index[j] == 'tit1':
                                if i == 0:
                                    df.iloc[i][j] = 'D, C'
                                else:
                                    if df.iloc[i - 1][j][0] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'

                            if df.index[j] == 'tit0':
                                if i == 0:
                                    df.iloc[i][j] = 'D, D'
                                else:
                                    if df.iloc[i - 1][j][0] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'
                        if df.iloc[i][j - 2][-1] == 'C':
                            if df.index[j] == 'coop':
                                df.iloc[i][j] = 'C, C'
                            if df.index[j] == 'def':
                                df.iloc[i][j] = 'C, D'
                            if df.index[j] == 'tit1':
                                if i == 0:
                                    df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][-1] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'

                            if df.columns[i] == 'tit1' and df.index[j] == 'tit0':
                                if i == 0:
                                    df.iloc[i][j] = 'C, D'
                                else:
                                    if df.iloc[i - 1][j][-1] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'
                    else:
                        if df.columns[i] == 'tit1' and df.index[j] == 'coop':
                            df.iloc[i][j] = 'C, C'
                        if df.columns[i] == 'tit1' and df.index[j] == 'def':
                            df.iloc[i][j] = 'C, D'
                        if df.columns[i] == 'tit1' and df.index[j] == 'tit1':
                            if i == 0:
                                df.iloc[i][j] = 'C, C'
                            else:
                                if df.iloc[i - 1][j][-1] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'

                        if df.columns[i] == 'tit1' and df.index[j] == 'tit0':
                            if i == 0:
                                df.iloc[i][j] = 'C, D'
                            else:
                                if df.iloc[i - 1][j][-1] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'

# Tit0 case
            if df.columns[i] == 'tit0':
                if j == 0 or (j == 1 and df.iloc[i][j - 1][0] == '0'):
                    if df.index[j] == 'coop':
                        df.iloc[i][j] = 'D, C'
                    if df.index[j] == 'def':
                        df.iloc[i][j] = 'D, D'
                    if df.index[j] == 'tit1':
                        if i == 0:
                            df.iloc[i][j] = 'D, C'
                        else:
                            if df.iloc[i-1][j][-1] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 2][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'
                            else:
                                if df.iloc[i-1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i-1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'

                    if df.index[j] == 'tit0':
                        if i == 0:
                            df.iloc[i][j] = 'D, D'
                        else:
                            if df.iloc[i-1][j][-1] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 2][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'
                            else:
                                if df.iloc[i-1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i-1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'
                else:
                    if df.iloc[i][j - 1][-1] == 'D':
                        if df.index[j] == 'coop':
                            df.iloc[i][j] = 'D, C'
                        if df.index[j] == 'def':
                            df.iloc[i][j] = 'D, D'
                        if df.index[j] == 'tit1':
                            if i == 0:
                                df.iloc[i][j] = 'D, C'
                            if i == 1:
                                if df.iloc[i - 1][j][0] == '0':
                                    df.iloc[i][j] = 'D, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'
                            if i > 1:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'

                        if df.columns[i] == 'tit1' and df.index[j] == 'tit0':
                            if i == 0:
                                df.iloc[i][j] = 'D, D'
                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i][j - 2][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i][j - 2][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                    if df.iloc[i][j - 1][-1] == 'C':
                        if df.index[j] == 'coop':
                            df.iloc[i][j] = 'C, C'
                        if df.index[j] == 'def':
                            df.iloc[i][j] = 'C, D'
                        if df.index[j] == 'tit1':
                            if i == 0:
                                df.iloc[i][j] = 'C, C'
                            if i == 1:
                                if df.iloc[i - 1][j][0] == '0':
                                    df.iloc[i][j] = 'C, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'
                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'


                        if df.columns[i] == 'tit1' and df.index[j] == 'tit0':
                            if i == 0:
                                df.iloc[i][j] = 'C, D'
                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i][j - 2][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i][j - 2][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                    if df.iloc[i][j - 1][0] == '0':
                        if df.iloc[i][j - 2][-1] == 'D':
                            if df.index[j] == 'coop':
                                df.iloc[i][j] = 'D, C'
                            if df.index[j] == 'def':
                                df.iloc[i][j] = 'D, D'
                            if df.index[j] == 'tit1':
                                if i == 0:
                                    df.iloc[i][j] = 'D, C'
                                else:
                                    if df.iloc[i - 1][j][0] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'

                            if df.index[j] == 'tit0':
                                if i == 0:
                                    df.iloc[i][j] = 'D, D'
                                else:
                                    if df.iloc[i - 1][j][0] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'D, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'D, C'
                        if df.iloc[i][j - 2][-1] == 'C':
                            if df.index[j] == 'coop':
                                df.iloc[i][j] = 'C, C'
                            if df.index[j] == 'def':
                                df.iloc[i][j] = 'C, D'
                            if df.index[j] == 'tit1':
                                if i == 0:
                                    df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][-1] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'

                            if df.columns[i] == 'tit1' and df.index[j] == 'tit0':
                                if i == 0:
                                    df.iloc[i][j] = 'C, D'
                                else:
                                    if df.iloc[i - 1][j][-1] == '0':
                                        if df.iloc[i - 2][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 2][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'
                                    else:
                                        if df.iloc[i - 1][j][0] == 'D':
                                            df.iloc[i][j] = 'C, D'
                                        if df.iloc[i - 1][j][0] == 'C':
                                            df.iloc[i][j] = 'C, C'
                    else:
                        if df.columns[i] == 'tit1' and df.index[j] == 'coop':
                            df.iloc[i][j] = 'C, C'
                        if df.columns[i] == 'tit1' and df.index[j] == 'def':
                            df.iloc[i][j] = 'C, D'
                        if df.columns[i] == 'tit1' and df.index[j] == 'tit1':
                            if i == 0:
                                df.iloc[i][j] = 'C, C'
                            else:
                                if df.iloc[i - 1][j][-1] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'

                        if df.columns[i] == 'tit1' and df.index[j] == 'tit0':
                            if i == 0:
                                df.iloc[i][j] = 'C, D'
                            else:
                                if df.iloc[i - 1][j][-1] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'C, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'C, C'

# Dis case
            if df.columns[i] == 'dis':
                if j > 2:
                    if df.iloc[i][j - 1][-1] == 'D' and df.iloc[i][j - 2][-1] == 'D':
                        if df.index[j] == 'coop':
                            df.iloc[i][j] = 'D, C'
                        if df.index[j] == 'def':
                            df.iloc[i][j] = 'D, D'
                        if df.index[j] == 'tit1':
                            if i == 0:
                                df.iloc[i][j] = 'D, C'
                            if i == 1:
                                if df.iloc[i - 1][j][0] == '0':
                                    df.iloc[i][j] = 'D, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'
                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i - 2][j][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i - 2][j][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                                if df.iloc[i - 1][j][0] == 'D':
                                    df.iloc[i][j] = 'D, D'
                                if df.iloc[i - 1][j][0] == 'C':
                                    df.iloc[i][j] = 'D, C'

                        if df.index[j] == 'tit0':
                            if i == 0:
                                df.iloc[i][j] = 'D, D'
                            else:
                                if df.iloc[i - 1][j][0] == '0':
                                    if df.iloc[i][j - 2][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i][j - 2][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                                else:
                                    if df.iloc[i - 1][j][0] == 'D':
                                        df.iloc[i][j] = 'D, D'
                                    if df.iloc[i - 1][j][0] == 'C':
                                        df.iloc[i][j] = 'D, C'
                else:
                    if df.index[j] == 'coop':
                        df.iloc[i][j] = 'C, C'
                    if df.index[j] == 'def':
                        df.iloc[i][j] = 'C, D'
                    if df.index[j] == 'tit1':
                        if i == 0:
                            df.iloc[i][j] = 'C, C'
                        else:
                            if df.iloc[i-1][j][-1] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i - 2][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'
                            else:
                                if df.iloc[i-1][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i-1][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'

                    if df.index[j] == 'tit0':
                        if i == 0:
                            df.iloc[i][j] = 'C, D'
                        else:
                            if df.iloc[i-1][j][-1] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i - 2][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'
                            else:
                                if df.iloc[i-1][j][0] == 'D':
                                    df.iloc[i][j] = 'C, D'
                                if df.iloc[i-1][j][0] == 'C':
                                    df.iloc[i][j] = 'C, C'
df['Total_C'] = 0
for i in range(len(teachers)):
    c_counter = 0
    for j in range(len(teachers)):
        if df.iloc[i][j][0] == 'C':
            c_counter += 1
    df['Total_C'][i] = c_counter
print(df)

# df.to_csv('df.csv')
df_payoff = df
for i in range(len(teachers)):
    for j in range(len(teachers)):
        if df_payoff.iloc[i][j] == '0,0':
            df.iloc[i][j] = 0
        if df_payoff.iloc[i][j] == 'C, C':
            df.iloc[i][j] = 3
        if df_payoff.iloc[i][j] == 'C, D':
            df.iloc[i][j] = -3
        if df_payoff.iloc[i][j] == 'D, C':
            df.iloc[i][j] = 6
        if df_payoff.iloc[i][j] == 'D, D':
            df.iloc[i][j] = 0



# df_payoff.to_csv('payoffs.csv')
incent = 7
df_incentive  = df
for i in range(len(teachers)):
    for j in range(len(teachers)):

        if df_payoff.iloc[i][j] == 3:
            df.iloc[i][j] = 3 + incent
        if df_payoff.iloc[i][j] == -3:
            df.iloc[i][j] = -3 + incent




# df_payoff.to_csv('incentive.csv')
