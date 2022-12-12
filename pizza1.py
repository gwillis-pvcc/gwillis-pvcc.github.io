# Name: Gaia Willis
# Purpose: Pizza calc

import datetime 

############## define global variables ################
# define tax rate and prices 
SALES_TAX_RATE = .055
s_cost = 9.99
m_cost = 12.99
l_cost = 14.99
xl_cost = 17.99

# define global variables
piz_size = ""

s_piz_amount = 0
m_piz_amount = 0
l_piz_amount = 0
xl_piz_amount = 0

s_piz_cost = 0
m_piz_cost = 0
l_piz_cost = 0
xl_piz_cost = 0

subtotal = 0
sales_tax = 0
total = 0

################# define program functions ##################
def main():
 another_piz = True
 while another_piz:
  get_user_data()
  perform_calculations()
  yesno = input("\nWould you like another pizza; y/n?")
  if yesno.upper() == "y" or "Y":
   another_piz = True
  if yesno.upper() == "n" or "N":
   another_piz = False
   display_results() 
   
	

def get_user_data():
	global piz_size, s_piz_amount, m_piz_amount, l_piz_amount, xl_piz_amount
	piz_size = input("What size pizza do you want; s,m,l, or xl?")
	if piz_size.upper() == 's' or 'S':
		s_piz_amount += 1
	if piz_size.upper() == 'm' or 'M':
		m_piz_amount += 1
	if piz_size.upper() == 'l' or 'L':
		l_piz_amount += 1
	if piz_size.upper() == 'xl' or 'Xl' or 'XL':
		xl_piz_amount += 1
def perform_calculations():
	global s_piz_cost, m_piz_cost, l_piz_cost, xl_piz_cost, subtotal, salestax, total
	s_piz_cost = s_piz_amount * s_cost
	m_piz_cost = m_piz_amount * m_cost
	l_piz_cost = l_piz_amount * l_cost
	xl_piz_cost = xl_piz_amount * xl_cost
	subtotal = s_piz_cost + m_piz_cost + l_piz_cost + xl_piz_cost
	salestax = subtotal * SALES_TAX_RATE
	total = subtotal + salestax
	
def display_results():
	print('------------------------------')
	print('****** Gaias Pizzeria ******')
	print('Your delicious local pizza place')
	print('-------------------------------')
	print('Pizzas       $'+format(subtotal,'8,.2f'))
	print('Sales Tax     $'+format(sales_tax, '8,.2f'))
	print('Total         $'+format(total, '8,.2f'))
	print('-------------------------------')
	print(str(datetime.datetime.now()))
	
	####### call on main program to exe #######
main()