############################
# Homework 2 template code #
############################
import sys

def process(zoom_audio_record_file):
    print(zoom_audio_record_file)

    fhandle = open(zoom_audio_record_file)
    
    speaker_word_cnt_dict = {}

    #TO DO: Declare other file open handles to write to the result files
    for line in fhandle:
        #Reset the is_speaker_line to False and speaker_name to None for every iteration
        is_speaker_line = False
        speaker_name = None 
        #TO DO: Add condition to check the the line is a speaker line or not. You can check if the line starts with alpha and if it has atlease one colon (:) in the line 
        #If the line is a speaker line then set the variable is_speaker_line=True 
        
        if (is_speaker_line):
            #TO DO: get the speaker name
            #speaker_name = ??

            #return all the words spoken by the speaker.
            #for ex on line 21 of the transcript it will extract following words
            # ['the','mission','of','your','hand','is','still','up.','So','just','making','sure','you','have','any','question,','or','it's','up','from','the','previous','time','that','you','put','it','up']
            
            words = line.split(":")[1].split() 
            
            #Add the words count of the speaker to its respective speaker
            speaker_word_cnt_dict[speaker_name] = speaker_word_cnt_dict.get(speaker_name, 0) + len(words)

    #By the end of the for loop now I will have all the speakers and their word count in speaker_word_cnt_dict dictionary
    
    #To do: Write a new for loop to iterate through the dictionary and build a new list to reverse key and values and 
    # add that tuple to the new list. Then sort that list and print the top 10 speakers 
    #Please refer to slide 13 in our slide deck # 10 on topic Tuples

    #TO DO: sort the dictionary based on the count
if __name__ == "__main__":
    #Takes file name as command line parameter to the script
    zoom_audio_record_file=sys.argv[1]
    process(zoom_audio_record_file)
