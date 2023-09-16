
import sys

def check_if_speaker_line(word):
    
    try:
        int(word)
        return False
    except ValueError:
        return True

def sort_dict(dict1):
    
    sorted_list= sorted([(v,k) for k,v in dict1.items()], reverse=True)[:5]
    print(sorted_list)
    for item in sorted_list:
        print(item[1])
    


    


def process_file(file_name):
    fhandle = open(file_name,'r')
    speaker_name_and_count = {}
    prev_speaker=""
    for line in fhandle:
        word = line.split(":")[0]
        if check_if_speaker_line(word):
            #get the name 
            #Check if there is no Speaker Name
            if ":" in line:
                speaker_name = line.split(":")[0]
                word_count = len(line.split(":")[1].split())
                speaker_name_and_count[speaker_name] = speaker_name_and_count.get(speaker_name,0)+ word_count
                prev_speaker = speaker_name
            else : # add to the previous speaker inputs, so that it 
                if prev_speaker == "":
                    # No speaker Identified, Continuing to count next loop
                    continue
                else:
                    word_count = len(line.split(":")[0].split())
                    speaker_name_and_count[prev_speaker] = speaker_name_and_count.get(prev_speaker,0) + word_count
            

        else:
            continue
    sort_dict(speaker_name_and_count)



def check_if_file(file_name):
    try:
        open(file_name)
        return True
    except:
        print(f" The {file_name} does not exists. Pleae verify and run the program again!!")
        exit(-1)

def main():
    #zoom_audio_record_file=sys.argv[1]
    zoom_audio_record_file="/Users/dineshsaraswat/Desktop/BAN601/homework3/zoom_class_audio_transcript.txt"
    if check_if_file(zoom_audio_record_file):
        process_file(zoom_audio_record_file)
    else:
        exit(-1)





if __name__ == "__main__":
    #Takes file name as command line parameter to the script
    
    main()