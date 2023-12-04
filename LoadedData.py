import re
import random

#Load in data
file = "postingInfo.txt"
with open(file, 'r') as file:
    elements = [line.strip() for line in file.readlines()]

def cleanData():
    """
    Cleans listing data by creating a list of lists that has when the listing was made along with the compensation
    :return: List
    """
    dataCopy = []
    for i in elements:
        if "hour" in i.split("·")[1].lower() or "hr" in i.split("·")[1].lower():
            dataCopy.append(i.split("·"))
    return dataCopy
def getMinPerListing():
    """
    Gets the first instance of a two-digit number which corresponds to the minimum possible hourly pay for each
    listing, then creates an updated list with just the date the listing was made and the minimum hourly pay
    :return: List
    """
    dataCopy = cleanData()
    digits = []
    pattern = re.compile(r'\b\d{2}\b')
    for i in dataCopy:
        match = pattern.search(i[1])
        if match:
            two_digits = match.group()
            digits.append([i[0], two_digits])
    # For testing
    #print(dataCopy)
    #print("******************************************************")
    #print(digits)
    return digits
def getMaxPerListing():
    """
    Gets each instance of two-digit numbers and gets the highest value which corresponds to the highest possible hourly
    pay for each listing, then creates an updated list with just the date the listing was made and the maximum hourly pay
    :return: List
    """
    dataCopy = cleanData()
    pattern = re.compile(r'\b\d{2}\b')

    result = []
    for item in dataCopy:
        matches = pattern.findall(item[1])
        # For testing
        #print('**********************************************')
        #print(item)
        #print(matches)
        if matches:
            # Extract the second instance if available, otherwise, extract the first one
            value_after_date = max(matches)
            result.append([item[0], value_after_date])
    return result
def avgPerDay(listingData):
    """
    Calculates the daily average o
    :param listingData: List of lists containing clean listing data
    :return: List
    """
    earningsPerDay = {}
    for post in listingData:
        date, earnings = post
        earnings = int(earnings)

        if date in earningsPerDay:
            earningsPerDay[date] += earnings
        else:
            earningsPerDay[date] = earnings



    minEarningsPerDay = (sum(earningsPerDay.values()) / 30)
    maxEarningsPerDay = sum({key: value * 8 for key, value in earningsPerDay.items()}.values()) / 30
    randomEarningsPerDay = sum({key: value * random.randint(1, 8) for key, value in earningsPerDay.items()}.values()) / 30


    avgPerDayResult = (minEarningsPerDay +
                       maxEarningsPerDay +
                       randomEarningsPerDay) / 3
    return [avgPerDayResult, [minEarningsPerDay, maxEarningsPerDay, randomEarningsPerDay]]

def main():
    maxPerHour = avgPerDay(getMaxPerListing())
    minPerHour = avgPerDay(getMinPerListing())
    dailyAvg = round((minPerHour[0] + maxPerHour[0]) / 2)
    minDailyAvg = round((minPerHour[1][0] + maxPerHour[1][0]) / 2)
    maxDailyAvg = round((minPerHour[1][1] + maxPerHour[1][1]) / 2)
    print(f"The average you can make for doing all the listings in any given day is ${dailyAvg}")
    print(f"The lowest possible average you can make daily is ${minDailyAvg}")
    print(f"The maximum possible average you can make daily is ${maxDailyAvg}")
    print(minPerHour)
    print(maxPerHour)

main()