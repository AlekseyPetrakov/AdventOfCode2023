# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def firstvalue(list):
    for i in list:
        if (i.isdigit()):
            return int(i)

def lastvalue(list):
    reversedlist = list.copy()
    reversedlist.reverse()
    for i in reversedlist:
        if (i.isdigit()):
            return int(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("input.txt", "r")

    count = 0
    for x in f:
        j = list(x)
        firstNumber = firstvalue(j)
        lastNumber = lastvalue(j)

        combined = str(firstNumber) + str(lastNumber)
        combined = int(combined)

        #print(combined)
        count = count + combined
    print(count)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
