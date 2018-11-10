# reference board by door
# reference board by window on far side room

import time

times_list = []
# will add 96 time slots to our list, 15 minute intervals
for i in range(24):
	for j in range(4):
		times_list.append(i)	

finalized_list = []
# used to map the times list to finalized list to make it easier
# the time in the finalized_list is the earliest possible time
for i in times_list:
	if i%4 == 0: 
		finalized_list.append(str(i) + ':00')
	if i%4 == 1:
		finalized_list.append(str(i) + ':15')
	if i%4 == 2:
		finalized_list.append(str(i) + ':30')
	if i%4 == 3:
		finalized_list.append(str(i) + ':45')

print(finalized_list)

def initialize_temp():
	

def full_day():

def morning():
	wake_up_time = input('What time do you go to sleep? ')
	wake_up_temp = input('What temperature should it be in the morning'

def leave_for_work():
	leave_for_work_time = input('What time do you leave for work in the morning? ')
	left_for_work_temp = ambient_temp

