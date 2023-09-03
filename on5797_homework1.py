# 
# Author            :    Dinesh Saraswat
# Email ID          :    dsaraswat2@horizon.csueastbay.edu
# Student ID        :    on5797
# Created Date      :    08/30/2023
# Revision Date     :    09/03/2023
# Revision          :    Changed the rules for non-overtime eligible students to calculate the pay for only 40 hours or less
# Topic             :    Homework1 for BAN 601
# 
# Description       :  Python code to calculate the pay for an employee based on the input from the user at the prompt 
#
# Input             :  At the prompt provide the input for Employee First Name, Employee Last Name, Number 
#                   :  of hours, Employee Grade and Employee Level
#                   :   
# 
# Execution Command : python on5797_homework1.py
# 
# Scope of the Progam  : This program does not expect negative number of hours
#    and Assumptions   : This prgram does not expect spaces for a name, it will continue to prompt you for valid name
#                      : This program can be terminated  by ctrl +C or ctrl +D at any time or entering Done at any prompt
#                      : This program accepts only valid values in the range provided at the prompt for Employee Grade, Employee Level
#                      : This program is run once only for an employee. If you need to get pay calculation for multiple employees 
#                        you have to call the program multiple times separately for each employee with prompted information
#
# Description of the Program : 
#                   This program prompts the user to provide the values for Employee First Name, 
#                   employee Last Name, Employee Pay Grade, Employee number of Hours and Employee Level.
#                   Based on the provided input and the logical rule for the calculation of the pay rate
#                   the actual pay is calculated. The overtime is applicable for only APRT employee Grade employees
#                   and rest of the employees are paid as per hourly wages. 
#

def if_number(string):
    #Function to determine if the provided value is a numerical value or not. 
    #It will return False if the value provided cannot be converted to a valid number.
    # This function is called in the get_input function to ensure if the number of hours are numerial or not

    try:
        float(string)
        return True
    except ValueError:
        return False

def print_done_quit():
    # A function to quit and prompt the quitting message when user enters done while entering the inputs to the program
    print("We are quiting ! See you on next execution.")
    quit()

def get_input():
    # This function is called from the main function to get the input and validate the input from the user at the prompt
    # If the input is not as per the valid values and in within the rules it will keep prompting the user to correct 
    # mistaken value and try providing the value once again for the prompt
    # This will return the formatted and type converted values to the calling variable    
    cond = True
    while cond :
        emp_fname = input("Enter the Employee's First Name or  Done to exit: ")
        
        if len(emp_fname.strip()) == 0:
            print(" The employee name cannot be empty. Kindly enter the name on next prompt!")
        
        elif emp_fname.strip().upper() == 'DONE':
            print_done_quit()
        
        else:
            cond = False         
   
    cond = True
    while cond:
        emp_lname = input("Enter the Employee's Last Name or Done to exit: ")
        if len(emp_lname.strip()) == 0 :
            print("The employee last name should not be empty. Kindly enter the name on the next prompt !")
        elif emp_lname.strip().upper() == 'DONE':
            print_done_quit()
        else :
            cond = False
    
    cond = True
    while cond:
        num_of_hours = input("Enter the number of hours in whole or Done to exit: ")

        if num_of_hours.strip().upper() == 'DONE':
            print_done_quit()
        elif if_number(num_of_hours.strip()):
            cond = False
        else:
            print("The number of hours has to be a float value. Kindly enter the correct value on next prompt !")

    cond = True
    while cond:
        emp_grade = input("Enter the grade of the Employee (IC, MGR or APRT) or Done to exit: ")
        if emp_grade.strip().upper() == 'DONE':
            print_done_quit()

        elif emp_grade.strip().upper() in ('IC', 'MGR', 'APRT'):
            cond = False
        else:
            print("Kindly enter the Employee Grade as IC , MGR or APRT only")
    
    cond = True
    while cond:        
        emp_level = input("Enter the employee level as (1, 2 or 3) for IC or MGR and (1,2)for APRT employee grade or Done to quit: ")
        if emp_level.strip().upper() =='DONE':
            print_done_quit()
        elif emp_level.strip() in ('1','2','3') and emp_grade.strip().upper() in ('IC','MGR') or emp_level.strip() in ('1','2') and emp_grade.strip().upper()== 'APRT':
            cond = False
        else:
            print("The Employee grade has to be either 1 , 2 or 3 for IC and MGR employee Grade or 1 and 2 for APRT. Kindly enter valid employee grade at next prompt !")

    # values are returned in the formatted and typed manner t
    return emp_fname.strip(), emp_lname.strip() , float(num_of_hours.strip()), emp_grade.strip().upper() , emp_level.strip()

def define_hourly_pay_rate_overtime_flag (num_of_hours, emp_grade, emp_level):
    # This function defines the hourly rate and the overtime flag for the employee Grade, and employee level 
    # and number of hours worked. This will be used to calculate the actual pay eventually 
    
    #define the hourly rate and overtime_flag
    if emp_grade == 'APRT' and emp_level == '1':
        hourly_rate = 30
        overtime_flag = 'YES'
        return hourly_rate, overtime_flag
    elif emp_grade == 'APRT' and emp_level == '2':
        hourly_rate = 40
        overtime_flag = 'YES'
        return hourly_rate, overtime_flag
    elif emp_grade == 'IC' and emp_level == '1':
        hourly_rate = 60
        overtime_flag = 'NO'
        return hourly_rate, overtime_flag
    elif emp_grade == 'IC' and emp_level == '2':
        hourly_rate = 70
        overtime_flag = 'NO'
        return hourly_rate, overtime_flag
    elif emp_grade == 'IC' and emp_level == '3':
        hourly_rate = 90
        overtime_flag = 'NO'
        return hourly_rate, overtime_flag
    elif emp_grade == 'MGR' and emp_level == '1':
        hourly_rate = 70
        overtime_flag = 'NO'
        return hourly_rate, overtime_flag
    elif emp_grade == 'MGR' and emp_level == '2':
        hourly_rate = 90
        overtime_flag = 'NO'
        return hourly_rate, overtime_flag
    elif emp_grade == 'MGR' and emp_level == '3':
        hourly_rate = 110
        overtime_flag = 'NO'
        return hourly_rate, overtime_flag

def net_pay(num_of_hours, hourly_rate, overtime_flag):
    # This function calculates the net pay of the employee based on the numbers of hours, hourly rate and overtime flag
    
    if overtime_flag =='YES':
        if num_of_hours >40:
            hour_pay = (40 * hourly_rate )+((num_of_hours - 40) * hourly_rate * 1.5)
            return hour_pay
        else:
            hour_pay = num_of_hours * hourly_rate
            return hour_pay
    else :
        if num_of_hours > 40 :
            hour_pay = 40 * hourly_rate
            return hour_pay
        else:
            hour_pay = num_of_hours * hourly_rate
            return hour_pay

def main():
    # The main program to control the execution flow of the functions to calculate the total pay for the week 

    print("Enter Done at any time of the prompt to exit of the program")

    # Below command calls teh get_input function and assigns the returned values to the variables to left of the assignment variable

    emp_fname , emp_lname , num_of_hours , emp_grade , emp_level = get_input()

    # Below command calls the define_hourly_pay_rate_overtime_flag function to get the hourly rate and overtime flag based on set of rules
    hourly_rate , overtime_flag = define_hourly_pay_rate_overtime_flag(num_of_hours,emp_grade,emp_level)
    
    # Below command calls the net_pay function to get the pay and format the same to the 2 decimal precision 
    total_pay = format(net_pay(num_of_hours, hourly_rate,overtime_flag),".2f")
    
    # This command is to print the information on the command propt as per the provided inputs and the calculated information
    print(f"The total pay for {emp_fname} {emp_lname} is ${total_pay} ")

if __name__ == "__main__":
    # execution manner of the program to invoke the main function
    main()