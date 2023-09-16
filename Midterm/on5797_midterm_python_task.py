# Code to count the word occurence  in a file 
# Output file will be created at the same filepath.
# File path is not expected to have the absolute filepath + filename

def process(inp_file_name, output_file_name):
    try:
        fhandle = open(inp_file_name,'r') # Handle to open the file
        counts ={}  # empty dictionary to hold the information
        
        for line in fhandle: # opening the file line by line and assigning the words to the line_list
            line_list = line.split()
            for item in line_list: # iterating the list and checking if we have the word in teh dictionary if yes then increase else make an entry
                if item not in counts:
                    counts[item] = 1
                else:
                    counts[item] = counts[item] + 1
        #print(counts)
    
    #writing to a file now
    
        
        whandle = open(output_file_name,'w') # Writing file Handle
        for word in counts: # iterating over the dictionary and making a write in the file
            write_str=word + " : " +str(counts[word])+"\n"
            whandle.write(write_str)
        
        fhandle.close() # Closing the files
        whandle.close()



    except:
        print(f"{file_name} File Does not exists. Exiting !!!")
        quit()
        #TO DO: Give an error message to the user if the filename is incorrect 


if __name__ == "__main__":
    file_path = input("Please enter the file path : ")
    file_name = input("Please enter the file name : ")
    absolute_file_name = file_path + "/" + file_name
    
    outfile_path = file_path
    outfile_name = 'on5797_midterm_python_task_output.txt'
    absolute_out_file_name= outfile_path +"/"+outfile_name
    process(absolute_file_name,absolute_out_file_name)
