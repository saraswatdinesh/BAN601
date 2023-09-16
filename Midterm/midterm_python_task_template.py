##############################################################################################################################
# Mid Term Exam Python Task
# Write a program which will read the text file and print the count of times each word appear in the file
# The text file (poems.txt) is attached here in the exam task
# You will write at least one function in your python program
# You should ask for the file path and name input from the user
# If the user enters incorrect file name or path then show a meaningful message to the user and exit
# If the user enters correct file name then read all the words in the file and
# Write the word and its count into another output file
# The new output file should contain word and count separated by colon “:” character
# Following is an example of output
# >>cat output.txt
# feathers : 1
# - : 15
# That : 3
##############################################################################################################################

def process(file_name):
    try:
        fhandle = open(file_name)
        word_count_dict = dict()
        for line in fhandle:
            words = line.split() #Extract the words from the line

            #TO DO: write a for loop to go through the words and:
                #TO DO: use word_count_dict dictionary to store the word as key and its count as value

        #TO DO: write a for loop to go through the word_count_dict dictionary
            #TO DO: write the word and count into the new file

    except:
        pass
        #TO DO: Give an error message to the user if the filename is incorrect 

if __name__ == "__main__":
    file_name = input("Please enter the file name: ")
    process(file_name)
