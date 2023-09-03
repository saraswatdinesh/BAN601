while True:
    inp = input("Enter the number 1, 2,3 or 4 or Done to break out of the program")
    if inp.upper() == 'DONE':
        break
    value = int(inp)

    try:
        file = open("exercise1.txt")
    except:
        print("File does not exist")
        quit()
    count = 0
    if int(inp) == 1:
        for lines in file:
            count = count +1
            if count%2 != 0:
                #print the odd lines
                print(lines.rstrip())
                
    elif int(inp) == 2:
        for lines in file:
            count = count + 1 
            if count%2 ==0:
                #print the even lines
                print(lines.rstrip())
    elif int(inp) == 3:
        length=0
        for item in file: 
            length = length + 1
        max_lines = length
        #print(f"Maximum number of lines in file {max_lines}")
        line_num = int(input(f"Enter the line number you want to print {max_lines}: ").strip())
        print(line_num)
        count = 0
        for item in file:
            count = count+1
            print(f"current_count is :{count}")
            if count == line_num:
                print(item.rstrip())
    elif int(inp) == 4:
        for line in file:
            print(line.strip())
    

