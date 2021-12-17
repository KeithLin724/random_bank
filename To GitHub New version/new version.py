import csv
from random import choice
from datetime import timedelta
from datetime import datetime


class Theme:
    row_name = ['No', 'Start_time', 'End_time', 'hall', 'Now_show', 'Date']

    def __init__(self, name: str, Displayday: str, Endday: str, Theme_length: str) -> None:
        self.name = name

        self.Displayday = datetime.strptime(Displayday, "%Y-%m-%d")

        self.Endday = datetime.strptime(Endday, "%Y-%m-%d")

        Time_list = list(map(int, Theme_length.split(':')))
        self.theme_length = timedelta(
            hours=Time_list[0], minutes=Time_list[1], seconds=Time_list[2])

    def __init__(self, input_dict: dict) -> None:
        self.name = input_dict['Name']

        self.Displayday = datetime.strptime(
            input_dict['DisplayTime'], "%Y-%m-%d")

        self.Endday = datetime.strptime(input_dict['EndTime'], "%Y-%m-%d")

        Time_list = list(map(int, input_dict['HowLong'].split(':')))
        self.theme_length = timedelta(
            hours=Time_list[0], minutes=Time_list[1], seconds=Time_list[2])

    def out(self, No: int, Date: datetime, Start_time, Hall: int) -> dict:
        EndTime = str(Start_time + self.theme_length)

        Date = Date.strftime("%Y-%m-%d")

        input_list = [No, str(Start_time), EndTime, Hall, self.name, Date]
        return dict(zip(Theme.row_name, input_list))

    def out_debug(self) -> list:
        return [self.name, self.Displayday, self.Endday, str(self.theme_length)]


if __name__ == '__main__':
    input_file_name = str(input('input your file name : '))

    file_name = str(input("output file name : "))
    halls = int(input("how many halls : "))

    need_pop_index = [3, 4, 6]
    input_data_arr = []
    with open(input_file_name, mode='r', newline='') as readcsv:
        rows_scanner = csv.reader(readcsv, delimiter=',')
        header = next(rows_scanner)
        header[0] = 'Name'

        for row in rows_scanner:
            put = dict(zip(header, row))
            for P in need_pop_index:
                put.pop(header[P])
            input_data_arr.append(put)

    theme_move = [Theme(x) for x in input_data_arr]

    time_range = ['08:00:00', '11:00:00', '14:00:00',
                  '17:00:00', '20:00:00', '21:00:00']
    halls = list(range(1, halls+1))

    base_day = datetime(year=2021, month=10, day=31)
    last_day = datetime(year=2021, month=12, day=31)
    counter_day = timedelta(1)

    diff_day = last_day - base_day
    counter_date = base_day

    counter_no = 1
    with open(file_name + '.csv', mode='w') as tmp_file:
        tmp_file = csv.DictWriter(tmp_file, Theme.row_name)
        tmp_file.writeheader()

        for i in range(1, diff_day.days+1):
            can_choice = [x for x in theme_move if (counter_date - x.Displayday).days >= 0
                          and (counter_date - x.Endday).days <= 0]
            for hall in halls:
                for time_part in time_range:

                    put_csv_dict: dict

                    if len(can_choice) > 0:
                        rand_thing = choice(can_choice)
                        t = list(map(int, time_part.split(':')))
                        put_csv_dict = rand_thing.out(counter_no, counter_date,
                                                      timedelta(hours=t[0], minutes=t[1], seconds=t[2]), hall)
                    else:
                        put_csv_dict = dict(
                            zip(Theme.row_name,
                                [counter_no, time_part, 'N/A', hall, 'N/A', counter_date.strftime("%Y-%m-%d")]))
                    # list have thing

                    tmp_file.writerow(put_csv_dict)
                    #print(rand_thing.out(counter_no , counter_date , timedelta(hours=t[0] , minutes=t[1] , seconds=t[2]) , hall))
                    counter_no += 1

            counter_date = counter_date + counter_day
