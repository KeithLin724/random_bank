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

    def __init__(self, input_list: list) -> None:  # for panda
        self.name = input_list[0]

        self.Displayday = datetime.strptime(input_list[1], "%Y/%m/%d")

        self.Endday = datetime.strptime(input_list[2], "%Y/%m/%d")

        Time_list = list(map(int, input_list[3].split(':')))
        self.theme_length = timedelta(
            hours=Time_list[0], minutes=Time_list[1], seconds=Time_list[2])

 #   def __init__(self, input_dict: dict) -> None:
#        self.name = input_dict['Name']

 #       self.Displayday = datetime.strptime(
 #           input_dict['DisplayTime'], "%Y-%m-%d")

 #       self.Endday = datetime.strptime(input_dict['EndTime'], "%Y-%m-%d")

#        Time_list = list(map(int, input_dict['HowLong'].split(':')))
 #       self.theme_length = timedelta(
#            hours=Time_list[0], minutes=Time_list[1], seconds=Time_list[2])

    def out(self, No: int, Date: datetime, Start_time: timedelta, Hall: int) -> dict:
        EndTime = str(Start_time + self.theme_length)

        Date = Date.strftime("%Y/%m/%d")

        input_list = [No, str(Start_time), EndTime, Hall, self.name, Date]
        return dict(zip(Theme.row_name, input_list))

    def out_list(self, No: int, Date: datetime, Start_time: timedelta, Hall: int) -> list:
        EndTime = str(Start_time + self.theme_length)

        Date = Date.strftime("%Y/%m/%d")

        return [No, str(Start_time), EndTime, Hall, self.name, Date]

    def out_debug(self) -> list:
        return [self.name, self.Displayday, self.Endday, str(self.theme_length)]
