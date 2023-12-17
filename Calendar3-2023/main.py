# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
def is_symbol(char):
    Symbols = ["!","@","#","$","%","^","&","*","(",")","/","+","-","=","_"]
    return char in Symbols



def has_symbol_around(megaList, x, y):
    # Define the 8 possible directions around the current position
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        # Check if the new position is within bounds
        if 0 <= new_x < len(megaList[0]) and 0 <= new_y < len(megaList):
            # Check if the character at the new position is a symbol
            if is_symbol(megaList[new_y][new_x]):
                return True  # Symbol found around the digit

    return False  # No symbol found around the digit



def LeftMost(x, y): #gets the left most number to get returned
    leftInt = x-1 #checks 
    if ((megaList[y][leftInt]).isdigit()):
        secondleftInt = leftInt - 1
        if((megaList[y][secondleftInt]).isdigit()):
            leftInt = leftInt - 1
            return (secondleftInt, y) #was third most (and values are max of 4)

        else:
            return (leftInt, y) #was second most


    else: #already left most
        return (x,y)





coords = []
newcoord = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("input.txt", "r")
    megaList = []

    
    for read in f:
        innerList = list(read.strip())
        megaList.append(innerList)
    #print(megaList[0])


    for y in range(len(megaList)):

        smallerList = megaList[y]

        for x in range(len(smallerList)): #(for each character in each row) j symbolizes character

            if (megaList[y][x].isdigit() & (has_symbol_around(megaList, x, y))):
                coords.append((x,y))
                

    for ko in coords:
        (x,y) = LeftMost(ko[0],ko[1])
        new_coordinate = (x,y)


        if new_coordinate not in newcoord:
            newcoord.append(new_coordinate)
        #newcoord.append((x,y))
        #print(ko)
        #print("co ord: " + megaList[ko[1]][ko[0]])
    
    
    #print(newcoord)

    total = 0
    # Prints for every vlaue in newcord, the actual number (from megalist)
    for x, y in newcoord:
        full_number = megaList[y][x]  # Initialize with the digit at the current coordinate

        # Move left and append digits to the full number until a non-digit character is encountered
        leftInt = x - 1
        while leftInt >= 0 and megaList[y][leftInt].isdigit():
            full_number = megaList[y][leftInt] + full_number
            leftInt -= 1

        # Move right and append digits to the full number until a non-digit character is encountered
        rightInt = x + 1
        while rightInt < len(megaList[y]) and megaList[y][rightInt].isdigit():
            full_number += megaList[y][rightInt]
            rightInt += 1

        total += int(full_number)
        print(f"Number at ({x}, {y}): {full_number}")
    
    print("the total (not part numbers) is: " + str(total)) #printing the final sum
        
    #print(megaList[0][25])
