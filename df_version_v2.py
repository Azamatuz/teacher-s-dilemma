import pandas as pd
from random import shuffle


teachers = ['coop', 'def', 'tit1', 'tit0']*25
shuffle(teachers)
df = pd.DataFrame(columns=teachers, index=teachers)
# df = pd.DataFrame(columns=shuffle_list, index=shuffle_list)
df[:] = 'empty'
coop_status = 'C'
def_status = 'D'
tit1_status = 'C'
tit0_status = 'C'

for i in range(len(teachers)):
    for j in range(len(teachers)):

        if i == j:
            df.iloc[i][j] = '0, 0'
        else:
            # coop
            if df.columns[i] == 'coop':
                if df.index[j] == 'coop':
                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                        status_two=coop_status)
                if df.index[j] == 'def':
                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                        status_two=def_status)
                if df.index[j] == 'tit1':
                    if df.iloc[i-1][j][-1] == '0' and df.iloc[i - 2][j][0] == 'D':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                            status_two='D')
                    if df.iloc[i - 1][j][0] == 'D':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                            status_two='D')
                    else:
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                            status_two=tit1_status)
                if df.index[j] == 'tit0':
                    if i == 0 or i == 1 and df.iloc[i-1][j][0] == '0':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                            status_two='D')
                    elif df.iloc[i - 1][j][0] == '0':
                        if df.iloc[i - 2][j][0] == 'D':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                                status_two='D')
                        else:
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                                status_two=tit0_status)
                    elif df.iloc[i - 1][j][0] == 'D':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                            status_two='D')
                    else:
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=coop_status,
                                                                            status_two=tit0_status)
            # def
            if df.columns[i] == 'def':
                if df.index[j] == 'coop':
                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                        status_two=coop_status)
                if df.index[j] == 'def':
                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                        status_two=def_status)
                if df.index[j] == 'tit1':
                    if i == 0 or i == 1 and df.iloc[i-1][j][-1] == '0':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                            status_two=tit1_status)
                    else:
                        if df.iloc[i - 1][j][0] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                    status_two=tit1_status)
                        if df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                status_two='D')
                        else:
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                status_two=tit1_status)
                if df.index[j] == 'tit0':
                    if i == 0 or i == 1 and df.iloc[i-1][j][-1] == '0':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                            status_two='D')
                    else:
                        if df.iloc[i - 1][j][0] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                    status_two=tit0_status)
                        if df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                status_two='D')
                        else:
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=def_status,
                                                                                status_two=tit0_status)
            # tit1
            if df.columns[i] == 'tit1':
                if df.iloc[i][j - 1][-1] == 'D' or df.iloc[i][j - 1][0] == '0' and df.iloc[i][j - 2][-1] == 'D':
                    if df.index[j] == 'coop':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                            status_two=coop_status)
                    if df.index[j] == 'def':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                            status_two=def_status)
                    if df.index[j] == 'tit1':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                status_two=tit1_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two=not tit1_status)
                                else:
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two=tit1_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two=tit1_status)
                    if df.index[j] == 'tit0':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == 'D':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                status_two='D')
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two='D')
                                else:
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two=tit0_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two=tit0_status)
                else:
                    if df.index[j] == 'coop':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                            status_two=coop_status)
                    if df.index[j] == 'def':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                            status_two=def_status)
                    if df.index[j] == 'tit1':
                        if i == 0 or i == 1 and df.iloc[i-1][j][-1] == '0':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                status_two=tit1_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                        status_two='D')
                                else:
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                        status_two=tit1_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                    status_two=tit1_status)
                    if df.index[j] == 'tit0':
                        if i == 0 or i == 1 and df.iloc[i-1][j][-1] == '0':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                status_two='D')
                        elif df.iloc[i - 1][j][0] == '0' and df.iloc[i - 2][j][0] == 'D' or df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                status_two='D')
                        else:
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit1_status,
                                                                                status_two=tit0_status)
            # tit0
            if df.columns[i] == 'tit0':
                if j == 0 or j == 1 and df.iloc[i][j - 1][-1] == '0' \
                        or df.iloc[i][j - 1][0] == '0' and df.iloc[i][j - 2][-1] == 'D' or df.iloc[i][j - 1][-1] == 'D':
                    if df.index[j] == 'coop':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                            status_two=coop_status)
                    if df.index[j] == 'def':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                            status_two=def_status)
                    if df.index[j] == 'tit1':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                status_two=tit1_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two=not tit1_status)
                                else:
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two=tit1_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two=tit1_status)
                    if df.index[j] == 'tit0':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == 'D':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                status_two='D')
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two='D')
                                else:
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                        status_two=tit0_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one='D',
                                                                                    status_two=tit0_status)
                else:
                    if df.index[j] == 'coop':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                            status_two=coop_status)
                    if df.index[j] == 'def':
                        df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                            status_two=def_status)
                    if df.index[j] == 'tit1':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                status_two=tit1_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                        status_two='D')
                                else:
                                    df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                        status_two=tit1_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                    status_two='D')
                            else:
                                df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                    status_two=tit1_status)
                    if df.index[j] == 'tit0':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                status_two='D')
                        elif df.iloc[i - 1][j][0] == '0' and df.iloc[i - 2][j][0] == 'D' or df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                status_two='D')
                        else:
                            df.iloc[i][j] = '{status_one}, {status_two}'.format(status_one=tit0_status,
                                                                                status_two=tit0_status)


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
df_incentive = df
for i in range(len(teachers)):
    for j in range(len(teachers)):

        if df_payoff.iloc[i][j] == 3:
            df.iloc[i][j] = 3 + incent
        if df_payoff.iloc[i][j] == -3:
            df.iloc[i][j] = -3 + incent
# df_payoff.to_csv('incentive.csv')
