# 
# Author            :    Dinesh Saraswat
# Email ID          :    dsaraswat2@horizon.csueastbay.edu
# Student ID        :    on5797
# Created Date      :    08/30/2023
# Revision Date     :    08/30/2023
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
#                      : This program can be terminated  by ctrl +C or ctrl +D at any time
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


def get_input():
    # This function is called from the main function to get the input and validate the input from the user at the prompt
    # If the input is not as per the valid values and in within the rules it will keep prompting the user to correct 
    # mistaken value and try providing the value once again for the prompt
    # This will return the formatted and type converted values to the calling variable    
    cond = True
    while cond :
        emp_fname = input("Enter the Employee's First Name : ")
        if len(emp_fname.strip()) == 0 :
            print(" The employee name cannot be empty. Kindly enter the name on next prompt!")
        else:
            cond = False         
   
    cond = True
    while cond:
        emp_lname = input("Enter the Employee's Last Name : ")
        if len(emp_lname.strip()) == 0 :
            print("The employee last name should not be empty. Kindly enter the name on the next prompt !")
        else :
            cond = False
    
    cond = True
    while cond:
        num_of_hours = input("Enter the number of hours in whole : ")
        if if_number(num_of_hours.strip()):
            cond = False
        else:
            print("The number of hours has to be a float value. Kindly enter the correct value on next prompt !")

    cond = True
    while cond:
        emp_grade = input("Enter the grade of the Employee (IC, MGR or APRT) : ")
        if emp_grade.strip().upper() in ('IC', 'MGR', 'APRT'):
            cond = False
        else:
            print("Kindly enter the Employee Grade as IC , MGR or APRT only")
    cond = True
    while cond:        
        emp_level = input("Enter the employee level as (1, 2 or 3) for IC or MGR and (1,2)for APRT employee grade: ")
        if emp_level.strip() in ('1','2','3') and emp_grade.strip().upper() in ('IC','MGR') or emp_level.strip() in ('1','2') and emp_grade.strip().upper()== 'APRT':
            cond = False
        else:
            print("The Employee grade has to be either 1 , 2 or 3 for IC and MGR employee Grade or 1 and 2 for APRT. Kindly enter valid employee grade at next prompt !")

    # values are returned in the formatted and typed manner t
    return emp_fname.strip(), emp_lname.strip() , float(num_of_hours.strip()), emp_grade.strip().upper() , emp_level.strip()





def pay_claculate(num_of_hours, emp_grade, emp_level):
    
    # The function to caluclate the actual pay of the employee baased on the num of hours,
    # emp_grade and employee level. It will return the actual pay for the provided information
    
    

    if emp_grade == 'APRT' and emp_level == '1' :
        # For Grade "APRT" and level 1 Employees pay calculation

        if num_of_hours >40 :
            # Since APRT is eligible for overtime, hence if hours are >40 then calculation is different else
            # if hours are less then 40 then different calculation
            pay = ((40* 30) + ((num_of_hours - 40) * 30 * 1.5))
            return pay
        else:
            pay = num_of_hours * 30
            return pay
    
    elif emp_grade == 'APRT' and emp_level == '2' :
        # For Grade "APRT" and level 2 employee pay calculation. As its eligible for overtime hence different calculation
        # for hours greater then 40 otherwise different calculation if hours less then 40
        if num_of_hours >40 :
            pay = ((40* 40) + ((num_of_hours - 40) * 40 * 1.5))
            return pay
        else:
            pay = num_of_hours * 40
            return pay

    
    elif emp_grade == 'IC' and emp_level == '1' :
        #Pay calculation for IC and Employee 1 level
        pay = num_of_hours * 60
        return pay
    
    
    elif emp_grade == 'IC' and emp_level == '2' :
        # Pay calculation for "IC" and level 2 employee
        pay = num_of_hours * 70
        return pay
    
    elif emp_grade == 'IC' and emp_level == '3' :
        # Pay calculation for "IC" and level 3 employee
        pay = num_of_hours * 90
        return pay
    
    elif emp_grade == 'MGR' and emp_level == '1' :
        # Pay calculation for "MGR" and level 1 employee
        pay = num_of_hours * 70
        return pay
    
    elif emp_grade == 'MGR' and emp_level == '2' :
        # Pay calculation for "MGR" and level 2 employee
        pay = num_of_hours * 90
        return pay
    
    elif emp_grade == 'MGR' and emp_level == '3' :
        # Pay calculation for "MGR" and level 3 employee
        pay = num_of_hours * 110
        return  pay    


def main():
    # Main program to call the get_input to get the input from the user and validate the input 
    
    print("Enter ctrl +c or ctrl + d at any time of the prompt to exit of the program")
    
    emp_fname , emp_lname , num_of_hours , emp_grade , emp_level = get_input()   
    
    #Calling the pay calculation function below and formating the output to 2 decimal places
    pay = format(pay_claculate(num_of_hours, emp_grade, emp_level),".2f")
    
    # print the values in the formmated manner
    print(f"The total pay for {emp_fname} {emp_lname} is ${pay} ")

if __name__ == "__main__":
    # execution manner of the program to invoke the main function
    main()