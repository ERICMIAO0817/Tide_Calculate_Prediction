import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 显示所有列


# cols = ['time', 'longitude', 'latitude', 'stationID', 'Water_Level', 'Water_Level_ODM']

# condition = 'Achill_Island_MODELLED'


# df_first_day = df.loc[df['time_UTC'].str.match('2017-11-02T')]
#
# highest = df_first_day['Water_Level_metres'].max()
# lowest = df_first_day['Water_Level_metres'].min()
#
# df_high = df_first_day.loc[df_first_day['Water_Level_metres'] == highest]
# df_low = df_first_day.loc[df_first_day['Water_Level_metres'] == lowest]

# print(df_high)
# print(df_low)
from datetime import date, timedelta

from tqdm import tqdm


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# for year in ['2017', '2018', '2019', '2020']:
#     for index, row in df.loc[df['time_UTC'].str.match(year)].iterrows():
#         x.append(row['time_UTC'])
#         y.append(row['Water_Level_metres'])
#
# print(len(x))
# print(len(y))

# plt.style.use("seaborn-darkgrid")
# # create a Figure object
# plt.figure(figsize=(12, 6))
# # create the line plot
# plt.plot(df["Date"], df["Price"])
# plt.show()

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)

    df = pd.read_csv('Tide_Prediction.csv', header=[0, 1])
    df.columns = df.columns.map('_'.join)
    # csv.rename_axis('Date').reset_index()

    print(df.count())

    print(df.columns)

    df = df.loc[df['stationID_Unnamed: 3_level_1'] == 'Achill_Island_MODELLED']

    start_date = date(2017, 1, 1)
    end_date = date(2020, 1, 1)
    x = []
    y_low = []
    y_high = []

    for single_date in tqdm(daterange(start_date, end_date)):
        df_first_day = df.loc[df['time_UTC'].str.match(str(single_date))]
        highest = df_first_day['Water_Level_metres'].max()
        lowest = df_first_day['Water_Level_metres'].min()
        x.append(single_date)
        y_low.append(lowest)
        y_high.append(highest)
        # print(lowest, highest)
    # fig = plt.figure()
    #
    # ax = fig.add_subplot(111)
    # l1 = ax.plot(x, y_low, 'r--', label='low')
    # l2 = ax.plot(x, y_high, 'g--', label='high')
    #
    # ax.plot(x, y_low, 'ro-', x, y_high, 'g+-')
    # ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    # plt.title('The Lasers in Three Conditions')
    # plt.xlabel('row')
    # plt.ylabel('column')
    #
    # plt.legend()
    # plt.ion()
    # ...
    # plt.pause(15)  # 显示秒数
    # plt.close()
    plt.plot(x, y_low, label="low", linestyle="-.")
    plt.plot(x, y_high, label="high", linestyle=":")
    plt.legend()
    plt.show()
