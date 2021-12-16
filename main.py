import csv 
from random import choice
from datetime import timedelta
from datetime import datetime

from types import LambdaType
import re

#row_name = ['No' , 'Date' , 'Start_time' , 'End_time' , 'hall' , 'Now_show']

class Theme:
    row_name = ['No' , 'Date' , 'Start_time' , 'End_time' , 'hall' , 'Now_show']
    def __init__(self , name:str , Displayday:str , Endday:str , theme_leght:str) -> None:
        self.name = name 
        
        #Time_list = list(map(int , Displayday.split('-')))
        self.Displayday = datetime.strptime(Displayday , "%Y-%m-%d") #dt.datetime(year=Time_list[0] , month=Time_list[1] , day=Time_list[2])
        
        #Time_list = list(map(int , Endday.split('-')))
        self.Endday = datetime.strptime(Endday , "%Y-%m-%d")#dt.datetime(year=Time_list[0] , month=Time_list[1] , day=Time_list[2])
        
        Time_list = list(map(int , theme_leght.split(':')))
        self.theme_leght = timedelta(hours=Time_list[0] , minutes=Time_list[1] , seconds=Time_list[2])

        
    
    def out(self , No:int , Date , Start_time , Hall:int ):
        EndTime = str(Start_time + self.theme_leght)
        
        Date = Date.strftime("%Y-%m-%d")
       

        input = [No  , Date , str(Start_time) ,EndTime , Hall , self.name]
        return dict(zip(Theme.row_name ,input ))

    def out_debug(self):
        return [self.name , self.Displayday , self.Endday ,str(self.theme_leght)]

if __name__ == '__main__':
    file_name = str(input("output file name :"))

    theme_move = [Theme('Anabelle' , '2021-11-05' , '2021-12-28','02:10:20')
                , Theme('Frozen' , '2021-11-23' , '2021-12-15' ,'01:45:00' )
                , Theme('Ironman' , '2021-11-27' , '2021-12-27' , '02:12:05')
                , Theme('LionKing' , '2021-10-31' , '2021-11-25','02:01:02')
                , Theme('Rio' , '2021-11-01','2021-12-31','01:45:30')]

    counter = 1  

    movie_name =[x.name for x in theme_move]
    time_range = ['08:00:00' , '11:00:00' , '14:00:00' , '17:00:00' , '20:00:00' , '21:00:00']
    halls = [1 , 2]
    #for i in theme_move:
    #    print(i.out_debug())

    #print()
    base_day = datetime(year=2021 , month=10 , day=31)
    last_day = datetime(year=2021 , month=12 , day=31)
    counter_day = timedelta(1)

    diff_day = last_day - base_day
    counter_date = base_day 


    counter_no = 1 
    with open(file_name + '.csv' , mode='w') as tmp_file:
        tmp_file = csv.DictWriter(tmp_file , Theme.row_name)
        tmp_file.writeheader()

        for i in range(1 , diff_day.days+1):
            can_chioce = [x for x in theme_move if (counter_date - x.Displayday).days >= 0 and (counter_date - x.Endday).days <= 0]
            for hall in halls:
                for time_part in time_range:
                    rand_thing = choice(can_chioce)

                    t = list(map(int , time_part.split(':')))
                    tmp_file.writerow(rand_thing.out(counter_no , counter_date , timedelta(hours=t[0] , minutes=t[1] , seconds=t[2]) , hall))
                    #print(rand_thing.out(counter_no , counter_date , timedelta(hours=t[0] , minutes=t[1] , seconds=t[2]) , hall))
                    counter_no += 1  
            
            counter_date = counter_date + counter_day