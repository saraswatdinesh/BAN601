############################
# Homework 2 template code #
############################
import sys

def process(input_file_name):
    print(input_file_name)

    fhandle = open(input_file_name)
    line_count = 0
    tot_base_pay = 0
    #TO DO: Declare other variable to count sum for overtime pay and benefits

    emp_master_handle = open('<[netid]_Employee_Master.csv>','w')
    #TO DO: Declare other file open handles to write to the result files
    
    for line in fhandle:
        #TO DO: Extract the each column in the line into list of elements 
        #EX: List 1 - [Id, EmployeeName, Year,  Agency] to write those contents into [netid]_Employee_Master.csv
        #EX: List 2 - [Id, BasePay, OvertimePay, OtherPay, Benefits] to write those contents into [netid]_Employee_Salaries.csv
        line_count = line_count + 1   # to count the number of lines for employee count

        #TO DO: Calculate the sum for overtime pay and benefits
        
        #TO DO: write the content of List 1 into into [netid]_Employee_Master.csv
        
        #TO DO: write the content of List 2 into into [netid]_Employee_Salaries.csv       

    #TO DO: Write the all the sum values into [netid]_Employee_Summary.csv

if __name__ == "__main__":
    input_file_name=sys.argv[1]
    process(input_file_name)
