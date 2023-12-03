# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):

import re


def extract_number_and_color(input_str): #function that returns number and color
    match = re.match(r'\s*(\d+)\s+(\w+)', input_str)
    if match:
        number = int(match.group(1)) #assigns the number
        color = match.group(2) #assigns the color
        return number, color #returns both as needed
    else:
        return None, None



def splitter(list):
    splitcomma = list.split(", ") #splitting by the colors now
    return splitcomma



gameindex = 1
if __name__ == '__main__':
    f = open("epicfile.txt", "r")

    count = 0 #final count which will be returned of all indexes that are valid
    gameindex = 1 #the index which starts at 1 (informs if this game index should be added to the count or not


    
    for x in f:
        j = x.split(':') #splitting the line by ":" to ensure that the Game # is removed.
        splitColon = j[1].split(";") #splitting furthermore by each time an elf draws a cube (by spltting with ;) j[1] is accessed to ensure that the Game # is ignored

        maxred = 12
        maxgreen = 13
        maxblue = 14

        found = False

        for i in splitColon:
            print(i)
            cubeReveal = splitter(i)

            for j in cubeReveal:
                #print(j)
                number, color = extract_number_and_color(j)
                if number is not None:
                    print(str(number) + " AND " + color)
                    if ((number > 12) & (color == "red")):
                        print("LARGER")
                        found = True
                        break
                    elif ((number > 13) & (color == "green")):
                        print("LARGER")
                        found = True
                        break
                    elif((number > 14) & (color == "blue")):
                        print("LARGER")
                        found = True
                        break

            if found:
                found = False
                print("THE INDEX IS "+ str(gameindex))
                count = count + gameindex
                break



        #print(splitColon[0])
        gameindex = gameindex + 1
    final = 5050 - count
    print(count)
    print(final)
