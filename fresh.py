#Define hourly wages/deductions
wages_hourly = (16.50, 15.75, 15.75, 19.50)
taxes = (.12, .03, .062, .0145)

#define global variables
pay_rate = 0
gross_pay = 0
fed_tax = 0
state_tax = 0
ss_tax = 0
med_tax = 0
total_taxes = 0
net_pay = 0
job_cat = ""
job_title = ""
hours_worked = 0

def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input('Do you need to calculate another employees weekly pay? (y/n):')
        if yesno.upper() != "Y" :
            another_employee = False

def get_user_data():
    global job_cat, job_title, hours_worked, pay_rate
    
    print('\nJob Category Codes: ', 'C: Cashier', 'S: Stocker', 'J: Janitor', 'M: Maintenance\n')
    
    job_cat = input("Please input your job category code (C, S, J, M): ")
    hours_worked = int(input("How many hours did you work this week?: "))
    
    if job_cat.upper() == 'C':
        pay_rate = wages_hourly[0]
        job_title = 'Cashier'
    if job_cat.upper() =='S':
        pay_rate = wages_hourly[1]
        job_title = 'Stocker'
    if job_cat.upper() =='J':
        pay_rate = wages_hourly[2]
        job_title = 'Janitor'
    if job_cat.upper() == 'M':
        pay_rate = wages_hourly[3]
        job_title = 'Maintenance'


def perform_calculations():
    global gross_pay, pay_rate, fed_tax, state_tax, ss_tax, med_tax, total_taxes, net_pay
    gross_pay = pay_rate * hours_worked
    fed_tax = gross_pay * taxes[0]
    state_tax = gross_pay * taxes[1]
    ss_tax = gross_pay * taxes[2]
    med_tax = gross_pay * taxes[3]
    total_taxes = fed_tax + state_tax + ss_tax + med_tax
    net_pay = gross_pay - total_taxes

def display_results():
    print('\n--------------------------------------------------')
    print('          ***** FRESH FOOD MARKETPLACE *****')
    print('          ****** EMPLOYEE WEEKLY PAY *******')
    print('----------------------------------------------------')
    print('         Job Category:        ', job_title)
    print('         Hourly Wage:            $', format(pay_rate,'8,.2f'))
    print('         Hours Worked:        $', format(hours_worked, '8,.2f'))
    print('----------------------------------------------------')
    print('         Gross Pay:           $', format(gross_pay, '8,.2f'))
    print('         Federal Income Tax:  $', format(fed_tax, '8,.2f'))
    print('         State Income Tax:    $', format(state_tax, '8,.2f'))
    print('         Social Security Tax: $', format(ss_tax, '8,.2f'))
    print('         Medicare Tax:        $', format(med_tax, '8,.2f'))
    print('         Total Taxes:   $', format(total_taxes, '8,.2f'))
    print('----------------------------------------------------')
    print('         Net Pay:             $', format(net_pay, '8,.2f'))
    print('----------------------------------------------------')
main()