# 
# Author            :    Dinesh Saraswat
# Email ID          :    dsaraswat2@horizon.csueastbay.edu
# Student ID        :    on5797
# Created Date      :    09/06/2023
# Topic             :    Homework1 for BAN 602
import sys

# Check if the file is available in the folder or not 


def process(input_file_name):
    print(input_file_name)
    # Ensuring the file exists with the name before processing. If not it will quit the processing
    try:
        fhandle = open(input_file_name)
    except:
        print(f"${fhandle} is not available")
        quit()
    

    line_count = 0
    tot_base_pay = 0
    tot_overtime_pay = 0
    total_benefits = 0
    #TO DO: Declare other variable to count sum for overtime pay and benefits

    emp_master_handle = open('on5797_Employee_Master.csv','w')
    #TO DO: Declare other file open handles to write to the result files
    emp_salary_handle = open('on5797_Employee_Salaries.csv','w')
    
    for line in fhandle:
        #TO DO: Extract the each column in the line into list of elements 
        # reading the file in the loop and 
        master_list = line.split(",")
        emp_master_list_index = (0,1,6,8)
        emp_salary_list_index = (0,2,3,4,5)
        emp_master_list=[]
        emp_salary_list=[]
        #print(master_list)
        emp_master_str = None
        emp_salary_str = None
        for index,item in enumerate(master_list):
            if index in emp_master_list_index:
                emp_master_list.append(item)
                if emp_master_str is None :
                    emp_salary_str = item
                else:
                    emp_master_str = emp_master_str + ',' + item
                
            if index in emp_salary_list_index:
                emp_salary_list.append(item)
                if emp_salary_str is None:
                    emp_salary_str = item
                else:
                    emp_salary_str = emp_salary_str + ',' + item
        #print(emp_master_list)
        emp_master_handle.write(emp_master_str+'\n')
        emp_salary_handle.write(emp_salary_str+'\n')
        #print(emp_salary_list)


        #EX: List 1 - [Id, EmployeeName, Year,  Agency] to write those contents into [netid]_Employee_Master.csv
        #EX: List 2 - [Id, BasePay, OvertimePay, OtherPay, Benefits] to write those contents into [netid]_Employee_Salaries.csv
        if master_list[0].strip().upper() != 'ID':
            line_count = line_count + 1   # to count the number of lines for employee count
            tot_base_pay = tot_base_pay + float(master_list[2])
            tot_overtime_pay = tot_overtime_pay + float(master_list[3])
            total_benefits = total_benefits + float(master_list[5])
        #TO DO: Calculate the sum for overtime pay and benefits
        
        #TO DO: write the content of List 1 into into [netid]_Employee_Master.csv
        
        #TO DO: write the content of List 2 into into [netid]_Employee_Salaries.csv       

    #TO DO: Write the all the sum values into [netid]_Employee_Summary.csv

if __name__ == "__main__":
    input_file_name=sys.argv[1]
    process(input_file_name)