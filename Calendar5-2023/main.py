def IndexChecker(value1, value2, prevSet):
    returner = []
    seedSoil = {}
    for i in range(value1 + 1, value2):
        #print(cleaned_list[i])
        breakUp = cleaned_list[i].split(" ")
        firstSeed = int(breakUp[1])
        lastSeed = int(breakUp[1]) + int(breakUp[2]) - 1
        #print(firstSeed)
        #print(lastSeed)
        for x in range(0,int(breakUp[2])):
            seed = int(breakUp[1]) + x
            soil = int(breakUp[0]) + x
            seedSoil[seed] = soil

    for s in prevSet:
        if int(s) in seedSoil:
            value = seedSoil[int(s)]
        else:
            value = int(s)
        returner.append(value)
        print(value)
        
    return returner #returning the altered numbers that have been changed by the range alterer



if __name__ == '__main__':
    f = open("text.txt", "r")
    epic = []
    for x in f:
        epic.append(x)

    cleaned_list = [string.replace("\n", "") for string in epic]
    cleaned_list = [value for value in cleaned_list if value != ""]

    seeds = cleaned_list[0].split(" ")
    seeds.remove("seeds:") # Seeds now setup to have all integers representing seed values
    print(seeds)


    


    value = 0

    seed2soilIndex = cleaned_list.index("seed-to-soil map:")
    soil2fertilizerIndex = cleaned_list.index("soil-to-fertilizer map:")
    returner = IndexChecker(seed2soilIndex, soil2fertilizerIndex, seeds)
    print(returner)

    fertilizer2waterIndex = cleaned_list.index("fertilizer-to-water map:")
    returner = IndexChecker(soil2fertilizerIndex, fertilizer2waterIndex, returner)
    print(returner)

    water2lightIndex = cleaned_list.index("water-to-light map:")
    returner = IndexChecker(fertilizer2waterIndex, water2lightIndex, returner)
    print(returner)

    lights2tempIndex = cleaned_list.index("light-to-temperature map:")
    returner = IndexChecker(water2lightIndex, lights2tempIndex, returner)
    print(returner)

    temp2humidityIndex = cleaned_list.index("temperature-to-humidity map:")
    returner = IndexChecker(lights2tempIndex, temp2humidityIndex, returner)
    print(returner)

    humidity2locationIndex = cleaned_list.index("humidity-to-location map:")
    returner = IndexChecker(temp2humidityIndex, humidity2locationIndex, returner)
    print(returner)

    max = len(cleaned_list)
    returner = IndexChecker(humidity2locationIndex, max, returner)
    print(returner)


    print (min(returner))


