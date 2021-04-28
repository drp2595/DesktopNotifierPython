import datetime
from plyer import notification #for getting notification on your PC
import pandas as pd
import xlrd
import pause


wb = xlrd.open_workbook('Sample.xlsx') #Load xl file
sheet = wb.sheet_by_index(0) #Reading details from first Sheet
counter=1  #raw counter
while (True):
	
	#Try block for index errors
	try:
		row=sheet.row_values(counter) #Skipping title row, starting from second row
		Title=row[0]                  #Column 1
		Detail=row[1]                 #Column 2
		Hour=int(row[2])              #Column 3
		Min=int(row[3])               #Column 4
		Sec=int(row[4])               #Column 5
		untilTime=datetime.datetime(2021, 4, 28, Hour,Min,Sec) #Converting hour,minute,second to milisecond.
		print(untilTime)
		print('\n')
		pause.until(untilTime)  #this function will pause the execution till 'untilTime' miliseconds from starting.
		#below is notification function.
		notification.notify(
        title = Title ,
        message = Detail + '\n' + str(Hour)+':'+str(Min)+':'+str(Sec),
        timeout  = 20 # the notification stays for 'timeout' sec
    	)
	except:
		print("Finished")
		break
	counter=counter+1
