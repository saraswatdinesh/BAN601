
# Author : Dinesh Saraswat
# Date   : 09/16/2023
#This script expects that you provide the input file as the second parameter to the python execution
# Execution command is 

# > python on5797_homework3.py <filenamewithpath>
import sys

def check_if_speaker_line(word):
    # Function to check if we have a word generated as a speaker or a timestamp/number. It will return False
    #if its a integer. Basically to identify speaker name lines
    
    try:
        int(word)
        return False
    except ValueError:
        return True

def sort_dict(dict1):
    # Function to sort the dictionary based on the values and generate a list of tuples with value and key
    
    sorted_list= sorted([(v,k) for k,v in dict1.items()], reverse=True)
    return sorted_list
    #print(sorted_list)
    for item in sorted_list:
        print(item[1], item[0])
    

def process_file(file_name):
    # Generate the dictionary of the speakers and disregard all the noise from the data file.
    fhandle = open(file_name,'r')
    speaker_name_and_count = {} # This list will have the list of all the attendees
    prev_speaker=""
    for line in fhandle:
        word = line.split(":")[0] # Get the first word of the line
        if check_if_speaker_line(word): # If the word is speaker and not a time stamp or a number it skips
            #get the name 
            #Check if there is no Speaker Name
            if ":" in line: 
                # If there is  : in the word it means it has speaker name details we split the records
                #get the speaker name and teh words separately and use the len function to calculate the number of word
                speaker_name = line.split(":")[0]
                word_count = len(line.split(":")[1].split())
                speaker_name_and_count[speaker_name] = speaker_name_and_count.get(speaker_name,0)+ word_count
                prev_speaker = speaker_name
            else : # add to the previous speaker name as it is a continuation of his speaking
                if prev_speaker == "":
                    # No speaker Identified, Continuing to count next loop 
                    # This is to remove the first 2-3 lines of garbage in the file.
                    continue
                else: # Logic to add to the previous speaker word counts when speaker name is missing
                    word_count = len(line.split(":")[0].split())
                    speaker_name_and_count[prev_speaker] = speaker_name_and_count.get(prev_speaker,0) + word_count
        else:
            # Continue in order to skip the non speaker lines
            continue
    sorted_list = sort_dict(speaker_name_and_count)[:5]  # Here we will sort and just take the first 5 records
    for item in sorted_list:  # Printing the list with the name and the count
        print(item[1], item[0])
    fhandle.close()


def check_if_file(file_name):
    # Function to check if the file exists or not. If it does not exist it prompts the user and exists
    try:
        open(file_name)
        return True
    except:
        print(f" The {file_name} does not exists. Pleae verify and run the program again!!")
        exit(-1)

def main():  
    #Main function to have the flow of the execution of the program
    zoom_audio_record_file=sys.argv[1]
    #print(" Enter the filename with path for the zoom audio transcript file:  ")
    #zoom_audio_record_file="/Users/dineshsaraswat/Desktop/BAN601/homework3/zoom_class_audio_transcript.txt"
    
    if check_if_file(zoom_audio_record_file): # Check if the file exists if yes then process  
        process_file(zoom_audio_record_file)  #  Process the audio file to get the names of top 5 speakers on the call
    else:
        exit(-1)


if __name__ == "__main__":
    #Takes file name as command line parameter to the script
    main()