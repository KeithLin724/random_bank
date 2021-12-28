from datetime import timedelta
from random import choice
from Theme import Theme
from numba import jit
import pandas as pd


@jit(forceobj=True)
def find_base_end_day(input_data_arr: list[Theme]) -> tuple:
    base_day = input_data_arr[0].Displayday
    last_day = input_data_arr[0].Endday

    for x in input_data_arr:
        if x.Displayday < base_day:
            base_day = x.Displayday

        if x.Endday > last_day:
            last_day = x.Endday

    return base_day, last_day


def random_day_schedule(input_data_arr: list[Theme], file_name: str) -> None:
    re_df = pd.DataFrame()
    # input_data_arr = [Theme(x) for x in input_data_arr]

    time_range = ['08:00:00', '11:00:00', '14:00:00',
                  '17:00:00', '20:00:00', '21:00:00']

    base_day, last_day = find_base_end_day(input_data_arr)
    diff_day, counter_date, counter_no = last_day - base_day, base_day, 1

    i = diff_day.days + 1

    while i > 0:
        can_choice = [x for x in input_data_arr if (
            counter_date - x.Displayday).days >= 0 >= (counter_date - x.Endday).days]
        for hall in range(1, halls+1):
            for time_part in time_range:

                put_csv_dict: list

                if len(can_choice) > 0:
                    rand_thing = choice(can_choice)
                    t = list(map(int, time_part.split(':')))
                    put_csv_dict = rand_thing.out(counter_no, counter_date,
                                                  timedelta(hours=t[0], minutes=t[1], seconds=t[2]), hall)
                else:
                    put_csv_dict = dict(
                        zip(Theme.row_name,
                            [counter_no, time_part, 'N/A', hall, 'N/A', counter_date.strftime("%Y-%m-%d")]))

                re_df = re_df.append(put_csv_dict, ignore_index=True)
                # tmp_file.writerow(put_csv_dict)
                # print(rand_thing.out(counter_no , counter_date , timedelta(hours=t[0] , minutes=t[1] , seconds=t[2]) , hall))
                counter_no += 1
        i -= 1
        counter_date += timedelta(1)
    # return re_df
    re_df.to_csv(file_name, index=False)


if __name__ == '__main__':
    input_file_name = str(input('input your file name : '))

    file_name = str(input("output file name : "))
    halls = int(input("how many halls : "))

    need_pop_index = [3, 4, 6]
    df = pd.read_csv(input_file_name)

    df_col_name = list(df.columns)

    for i in need_pop_index:
        df.pop(df_col_name[i])

    random_day_schedule(list(Theme(x)
                        for x in df.values.tolist()), file_name=file_name + '.csv')
