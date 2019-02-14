import pandas as pd
from random import shuffle
import matplotlib.pyplot as plt

teachers = ['altruist', 'ego_centered', 'responsive', 'debatable', 'disappoint'] * 20
shuffle(teachers)
df = pd.DataFrame(columns=teachers, index=teachers)
# df = pd.DataFrame(columns=shuffle_list, index=shuffle_list)
df[:] = 'empty'
altruist_status = 'C'
ego_centered_status = 'D'
responsive_status = 'C'
debatable_status = 'C'
disappoint_status = 'C'
disappoint_status_horizon = 'C'

for i in range(len(teachers)):
    for j in range(len(teachers)):
        if i == j:
            df.iloc[i][j] = '0, 0'
        else:
            # altruist
            if df.columns[i] == 'altruist':
                if df.index[j] == 'altruist':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                      statusTwo=altruist_status)
                if df.index[j] == 'ego_centered':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                      statusTwo=ego_centered_status)
                if df.index[j] == 'responsive':
                    if df.iloc[i - 1][j][-1] == '0' and df.iloc[i - 2][j][0] == 'D':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                          statusTwo='D')
                    if df.iloc[i - 1][j][0] == 'D':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                          statusTwo='D')
                    else:
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                          statusTwo=responsive_status)
                if df.index[j] == 'debatable':
                    if i == 0 or i == 1 and df.iloc[i - 1][j][0] == '0':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                          statusTwo='D')
                    elif df.iloc[i - 1][j][0] == '0':
                        if df.iloc[i - 2][j][0] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                              statusTwo='D')
                        else:
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                              statusTwo=debatable_status)
                    elif df.iloc[i - 1][j][0] == 'D':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                          statusTwo='D')
                    else:
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                          statusTwo=debatable_status)
                if df.index[j] == 'disappoint':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=altruist_status,
                                                                      statusTwo=disappoint_status)

            # ego_centered
            if df.columns[i] == 'ego_centered':
                if df.index[j] == 'altruist':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                      statusTwo=altruist_status)
                if df.index[j] == 'ego_centered':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                      statusTwo=ego_centered_status)
                if df.index[j] == 'responsive':
                    if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                          statusTwo=responsive_status)
                    else:
                        if df.iloc[i - 1][j][0] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                                  statusTwo=responsive_status)
                        if df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                              statusTwo='D')
                        else:
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                              statusTwo=responsive_status)
                if df.index[j] == 'debatable':
                    if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                          statusTwo='D')
                    else:
                        if df.iloc[i - 1][j][0] == '0':
                            if df.iloc[i - 2][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                                  statusTwo=debatable_status)
                        if df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                              statusTwo='D')
                        else:
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                              statusTwo=debatable_status)
                if df.index[j] == 'disappoint':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=ego_centered_status,
                                                                      statusTwo=disappoint_status)
            # responsive
            if df.columns[i] == 'responsive':
                if df.iloc[i][j - 1][-1] == 'D' or df.iloc[i][j - 1][0] == '0' and df.iloc[i][j - 2][-1] == 'D':
                    if df.index[j] == 'altruist':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                          statusTwo=altruist_status)
                    if df.index[j] == 'ego_centered':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                          statusTwo=ego_centered_status)
                    if df.index[j] == 'responsive':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                              statusTwo=responsive_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo=not responsive_status)
                                else:
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo=responsive_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo=responsive_status)
                    if df.index[j] == 'debatable':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                              statusTwo='D')
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo='D')
                                else:
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo=debatable_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo=debatable_status)
                    if df.index[j] == 'disappoint':
                        if df.iloc[i - 2][j][0] == 'D' and df.iloc[i - 1][j][0] == 'D':
                            disappoint_status = 'D'
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                          statusTwo=disappoint_status)
                else:
                    if df.index[j] == 'altruist':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                          statusTwo=altruist_status)
                    if df.index[j] == 'ego_centered':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                          statusTwo=ego_centered_status)
                    if df.index[j] == 'responsive':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                              statusTwo=responsive_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                                      statusTwo='D')
                                else:
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                                      statusTwo=responsive_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                                  statusTwo=responsive_status)
                    if df.index[j] == 'debatable':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                              statusTwo='D')
                        elif df.iloc[i - 1][j][0] == '0' and df.iloc[i - 2][j][0] == 'D' or df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                              statusTwo='D')
                        else:
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                              statusTwo=debatable_status)
                    if df.index[j] == 'disappoint':
                        if df.iloc[i - 2][j][0] == 'D' and df.iloc[i - 1][j][0] == 'D':
                            disappoint_status = 'D'
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=responsive_status,
                                                                          statusTwo=disappoint_status)
            # debatable
            if df.columns[i] == 'debatable':
                if j == 0 or j == 1 and df.iloc[i][j - 1][-1] == '0' \
                        or df.iloc[i][j - 1][0] == '0' and df.iloc[i][j - 2][-1] == 'D' or df.iloc[i][j - 1][-1] == 'D':
                    if df.index[j] == 'altruist':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                          statusTwo=altruist_status)
                    if df.index[j] == 'ego_centered':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                          statusTwo=ego_centered_status)
                    if df.index[j] == 'responsive':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                              statusTwo=responsive_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo=not responsive_status)
                                else:
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo=responsive_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo=responsive_status)
                    if df.index[j] == 'debatable':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                              statusTwo='D')
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo='D')
                                else:
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                      statusTwo=debatable_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                                  statusTwo=debatable_status)
                    if df.index[j] == 'disappoint':
                        if df.iloc[i - 2][j][0] == 'D' and df.iloc[i - 1][j][0] == 'D':
                            disappoint_status = 'D'
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne='D',
                                                                          statusTwo=disappoint_status)
                else:
                    if df.index[j] == 'altruist':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                          statusTwo=altruist_status)
                    if df.index[j] == 'ego_centered':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                          statusTwo=ego_centered_status)
                    if df.index[j] == 'responsive':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                              statusTwo=responsive_status)
                        else:
                            if df.iloc[i - 1][j][0] == '0':
                                if df.iloc[i - 2][j][0] == 'D':
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                                      statusTwo='D')
                                else:
                                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                                      statusTwo=responsive_status)
                            if df.iloc[i - 1][j][0] == 'D':
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                                  statusTwo='D')
                            else:
                                df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                                  statusTwo=responsive_status)
                    if df.index[j] == 'debatable':
                        if i == 0 or i == 1 and df.iloc[i - 1][j][-1] == '0':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                              statusTwo='D')
                        elif df.iloc[i - 1][j][0] == '0' and df.iloc[i - 2][j][0] == 'D' or df.iloc[i - 1][j][0] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                              statusTwo='D')
                        else:
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                              statusTwo=debatable_status)
                    if df.index[j] == 'disappoint':
                        if df.iloc[i - 2][j][0] == 'D' and df.iloc[i - 1][j][0] == 'D':
                            disappoint_status = 'D'
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=debatable_status,
                                                                          statusTwo=disappoint_status)
            # disappoint
            if df.columns[i] == 'disappoint':
                if df.iloc[i][j - 2][-1] == 'D' and df.iloc[i][j - 1][-1] == 'D':
                    disappoint_status_horizon = 'D'
                if df.index[j] == 'altruist':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                      statusTwo=altruist_status)
                if df.index[j] == 'ego_centered':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                      statusTwo=ego_centered_status)
                if df.index[j] == 'responsive':
                    if df.iloc[i - 1][j][-1] == '0' and df.iloc[i - 2][j][0] == 'D':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                          statusTwo='D')
                    if df.iloc[i - 1][j][0] == 'D':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                          statusTwo='D')
                    else:
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                          statusTwo=responsive_status)
                if df.index[j] == 'debatable':
                    if i == 0 or i == 1 and df.iloc[i - 1][j][0] == '0':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                          statusTwo='D')
                    elif df.iloc[i - 1][j][0] == '0':
                        if df.iloc[i - 2][j][0] == 'D':
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                              statusTwo='D')
                        else:
                            df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                              statusTwo=debatable_status)
                    elif df.iloc[i - 1][j][0] == 'D':
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                          statusTwo='D')
                    else:
                        df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                          statusTwo=debatable_status)
                if df.index[j] == 'disappoint':
                    df.iloc[i][j] = '{statusOne}, {statusTwo}'.format(statusOne=disappoint_status_horizon,
                                                                      statusTwo=disappoint_status)

df.to_csv('df.csv')
df_payoff = df
for i in range(len(teachers)):
    for j in range(len(teachers)):
        if df_payoff.iloc[i][j] == '0, 0':
            df.iloc[i][j] = 0
        if df_payoff.iloc[i][j] == 'C, C':
            df.iloc[i][j] = 3
        if df_payoff.iloc[i][j] == 'C, D':
            df.iloc[i][j] = -3
        if df_payoff.iloc[i][j] == 'D, C':
            df.iloc[i][j] = 6
        if df_payoff.iloc[i][j] == 'D, D':
            df.iloc[i][j] = 0

df_payoff.to_csv('payoffs.csv')
incent = 7
df_incentive = df
for i in range(len(teachers)):
    for j in range(len(teachers)):

        if df_payoff.iloc[i][j] == 3:
            df.iloc[i][j] = 3 + incent
        if df_payoff.iloc[i][j] == -3:
            df.iloc[i][j] = -3 + incent
df_payoff.to_csv('incentive.csv')

data = df_payoff.groupby(df_payoff.index).sum()

fig1, ax1 = plt.subplots()
ax1.set_title('Strategies Comparison')
ax1.boxplot(data)
plt.show()
