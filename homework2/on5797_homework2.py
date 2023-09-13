# 
# Author            :    Dinesh Saraswat
# Email ID          :    dsaraswat2@horizon.csueastbay.edu
# Student ID        :    on5797
# Created Date      :    09/06/2023
# Topic             :    Homework1 for BAN 601


import sys


def process(input_file_name):
    #print(input_file_name)
    # Ensuring the file exists with the name before processing. If not it will quit the processing.
    # If incorrect file name provided and if it exists it may still process the code however the results might be
    # inconsistent
    try:
        fhandle = open(input_file_name)
    except:
        print(f"${fhandle} is not available")
        quit()
    
    #Key variables to store the sum of the employee count, base pay, overtime_pay and total benefits
    line_count = 0
    tot_base_pay = 0
    #TO DO: Declare other variable to count sum for overtime pay and benefits
    tot_overtime_pay = 0
    total_benefits = 0
   
    emp_master_handle = open('on5797_Employee_Master.csv','w')
    #TO DO: Declare other file open handles to write to the result files
    emp_salary_handle = open('on5797_Employee_Salaries.csv','w')
    

    # Open the fhandle file and iterate it to process the data .
    for line in fhandle:
        #TO DO: Extract the each column in the line into list of elements 
        # reading the file in the loop and 
        master_list = line.split(",")  # spliting the read line with ',' delimiter as its csv
        emp_master_list_index = (0,1,6,8)   # defining the index values for the master list data set
        emp_salary_list_index = (0,2,3,4,5)  # Defining the index value for salary list
        emp_master_str = None    # Declaring and initiating variable to store employee_master String
        emp_salary_str = None   # Declaring and initiating variable to store employee_Salary String
        #Iterate over the master_list and have the index values checked. If it matches the index values
        #in the index tuples employee_master_list_index and em_salary_list_index then create
        # creating the write strings to each file. 
        for index,item in enumerate(master_list):
            if index in emp_master_list_index:
                if emp_master_str is None :
                    emp_master_str = item
                    
                else:
                    emp_master_str = emp_master_str + ',' + item
            
                
            if index in emp_salary_list_index:
                if emp_salary_str is None:
                    emp_salary_str = item
                else:
                    emp_salary_str = emp_salary_str + ',' + item
        #After iteration of the list the created variables are written to the file using the write method

        emp_master_handle.write(emp_master_str+'\n')
        emp_salary_handle.write(emp_salary_str+ '\n')


        #EX: List 1 - [Id, EmployeeName, Year,  Agency] to write those contents into [netid]_Employee_Master.csv
        #EX: List 2 - [Id, BasePay, OvertimePay, OtherPay, Benefits] to write those contents into [netid]_Employee_Salaries.csv
        # My Comment --> I do not need to create the list and iterate it over once again to write to a file. 
        #I chose the string method and have it writen directly to the file as it will be faster.
        
        # Below Program code to calculate the information for the summary file.
        # For the first line we do not want it to be included in calculation hence the logic to disregard the line 
        # from calculation and skip the loop to continue.

        if master_list[0].strip().upper() != 'ID':
            line_count = line_count + 1   # to count the number of lines for employee count
            tot_base_pay = tot_base_pay + float(master_list[2])
            tot_overtime_pay = tot_overtime_pay + float(master_list[3])
            total_benefits = total_benefits + float(master_list[5])
        else:
            continue
 # The Below line creates the handles for summary write file, Input string  for first line  
 # and summary line to be inserted to the csv file. Used the round method to summarize at the 2 decimal places
 # as per the professors input
    summary_fhandle = open("on5797_Employee_Summary.csv",'w')
    summ_first_line = "total_num_employees,total_base_pay, total_overtime_pay, total_benefits"
    summ_write_str = str(line_count) + "," + str(round(tot_base_pay,2)) + "," \
                     + str(round(tot_overtime_pay,2)) + ", " \
                        + str(round(total_benefits,2))
    summary_fhandle.write(summ_first_line + "\n")
    summary_fhandle.write(summ_write_str+ "\n")
    #print(line_count, tot_base_pay, tot_overtime_pay, total_benefits)
    #TO DO: Write the all the sum values into [netid]_Employee_Summary.csv
    # Closing all the files that were opened to release the memory. 

    summary_fhandle.close()
    fhandle.close()
    emp_master_handle.close()
    emp_salary_handle.close()


if __name__ == "__main__":
    input_file_name=sys.argv[1]
    process(input_file_name)