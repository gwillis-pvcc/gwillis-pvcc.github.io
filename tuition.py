# Name: Gaia Willis
# Purpose: This program computes college tuition & fees
#	PVCC Fee Rates orgininate:
#	In-state tuition: $155, out-of-state tuition: $331.60
# 	capital
#
#
#

import datetime
# define tuition & fee rates
RATE_TUITION_IN=155
RATE_TUITION_OUT=331.60
RATE_CAPITAL=23.5
RATE_INSTITUTION=1.75
RATE_ACTIVITY=2.90

#define variables 
inout=1 #1 means instate 2 means out
numcredits=
scholarshipamt=0
tuituionfee=0
capitalfee=0
institutionfee=0
activityfee=0
totalowed=
balance=0

###### define program functions ###### 
def main():
	get_user_data()
	perform_calculations()
	displa_results()
def get_user_data():
	global inout, numcredits, scholarshipamt
	inout=int(input("Enter a 1 for Instat; enter a 2 for out"))
	numcredits=int(input("Number of credits registered for:"))
	scholarshipamt=float(input("Scholarship amount received:"))
	
def perform_calculations():
global tuitionfee,capitalfee,instituionfee,activityfee,totalowed,balance
	if inout==1:
		tuitionfee=numcredits * RATE_TUITION_IN
		capitalfee=0
	else:
		tuitionfee=numcredits*RATE_TUITION_OUT
		capitalfee=numcredits*RATE_CAPITAL
	institutionfee=numcredits*RATE_INSTITUTION
	activityfee=numcredits*RATE_ACTIVITY
	totalowed=tuitionfee+capitalfee+institutionfee+activityfee
	balance=totalowed-scholarshipamt
def display_result
	print('\n-------------------------------------')
	print('Number of credits:'+str(numcredits))
	print('---------------------------------------')
	print('Tuition          $'+format(tuitionfee,'10,.2f'))
	print('Capital fee      $'+str(capitalfee))
	print('Institution fee  $'+str(institutionfee))
	print('Activity fee     $'+str(activityfee))
	print('Total            $'+str(totalowed))
	print('Scholarship.     $'+str(scholarshipamt))
	print('-----------------------------------------')
	print('Balance Owed     $:'+str(balance))
	print('-----------------------------------------')
	print(str(datetime.datetime.now()))
	print("NOTE: PVCC Fee Rates: https://www.pvcc.edu/tuition-and-fees")
	main()