from datetime import datetime
import calendar
from datetime import date
from datetime import timedelta




def find_date(input1, input2):
 start_month = int(datetime.strptime(input1, '%Y%m%d').strftime('%m'))
 start_year = int(datetime.strptime(input1, '%Y%m%d').strftime('%Y'))
 start_date = int(datetime.strptime(input1, '%Y%m%d').strftime('%d'))

 end_month = int(datetime.strptime(input2, '%Y%m%d').strftime('%m'))
 end_year = int(datetime.strptime(input2, '%Y%m%d').strftime('%Y'))
 end_date = int(datetime.strptime(input2, '%Y%m%d').strftime('%d'))

 end_date_obj = date(end_year, end_month, end_date)

 def all_saturdays(start_year, start_month, start_date):
 d = date(start_year, start_month, start_date)

 d += timedelta(days=5 - d.weekday())
 while d <= end_date_obj: # d.year <= int(end_year)
 yield d
 d += timedelta(days=7)

 all_saturdays = all_saturdays(start_year, start_month, start_date)

 for each_sat in all_saturdays:
 flag1 = False
 flag2 = False
 cal = calendar.monthcalendar(each_sat.year, each_sat.month)
 first_week = cal[0]
 second_week = cal[1]
 third_week = cal[2]
 fourth_week = cal[3]
 fifth_week = cal[4]
 if each_sat.day % 5 == 0:
 flag2 = True
 if first_week[calendar.SATURDAY]:
 fourth_saturday = date(each_sat.year, each_sat.month, fourth_week[calendar.SATURDAY])
 if each_sat == fourth_saturday:
 flag1 = True
 else:
 fourth_saturday = date(each_sat.year, each_sat.month, fifth_week[calendar.SATURDAY])
 if each_sat == fourth_saturday:
 flag1 = True

 if flag1:
 if not flag2:
 print(datetime.strptime(str(each_sat), '%Y-%m-%d').strftime('%Y%m%d'))
 else:
 if flag2:
 print(datetime.strptime(str(each_sat), '%Y-%m-%d').strftime('%Y%m%d'))


if __name__ == '__main__':
 input1 = '20180728'
 input2 = '20180927'
 find_date(input1,input2)
