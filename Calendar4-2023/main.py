if __name__ == '__main__':
    totalcounter = 0
    f = open("text.txt", "r")
    for x in f:
        NoColon = x.split(":") # Removing everyhting before the : (since we dont need it)

        CardSplit = NoColon[1].split("|")


        winning = CardSplit[0] #first section is the winning numbers
        cardRetrun = CardSplit[1] #second section is the return (or scratched out values)

        winning = winning.split(" ")
        cardRetrun = cardRetrun.split(" ")

        winning = [item for item in winning if item != ""] # Removing every blank "" from the list (caused by single integers)
        cardRetrun = [item for item in cardRetrun if item != ""] # Removing every blank "" from the list (caused by single integers)

        cardRetrun = [s.replace('\n','') for s in cardRetrun] # Every line except for last one has a \n attached at the end, this just ensures we remove that

        counter = 0

        for i in cardRetrun: # Check for each value in our numbers we scratched off, if it is IN the winning 
            if ((i in winning) and (counter == 0)): #If its the FIRST value, we gotta set it to 1
                counter = 1
                print("BASE " + i)
            elif (i in winning): #Otherwise we continue to multiply by 2 if its not the first number
                counter = (counter * 2)
                print(i)

        print(cardRetrun) #debugging reasons
        print("COUNTER: " + str(counter)) #debugging reasons
        totalcounter = totalcounter + counter #add counter to the total counter
    print("TOTAL: " + str(totalcounter)) #print totalcounter which is every line added