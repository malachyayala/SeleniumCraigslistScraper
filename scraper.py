from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class CraiglistScraper():
    """
    A Class to web scrape the cragistlist gigs section using selenium

    This class initializing scraping, collects compensation data on each craigslist gig, and goes to each page to get the listing data
    """
    def __init__(self, url: str):
        """
        Constructor to begin scraping
        :param url: String containing Craigslist paid gig URL
        """
        self.url = url
        self.driver = webdriver.Chrome()
        self.listingCompensation = []

    def startscrape(self) -> None:
        """
        Initializes scraping by going to the URL
        :return: None
        """
        self.driver.get(self.url)

    def getListings(self) -> None:
        """
        Get listings and the corresponding compensation data
        :return: None
        """
        listings = self.driver.find_elements(By.CLASS_NAME, "result-info")
        for listing in listings:
            #listingPay = listing.find_element(By.CLASS_NAME, "meta").text.split("·")[1]
            listingPay = listing.find_element(By.CLASS_NAME, "meta").text
            if "hour" in listingPay or "hr" in listingPay:
                self.listingCompensation.append(listingPay)
    def clickNextPage(self) -> None:
        """

        :return:
        """
        nextPageButton = self.driver.find_element(By.CSS_SELECTOR, ".bd-button.cl-next-page.icon-only").find_element(By.CSS_SELECTOR, ".icon.icom-")
        nextPageButton.click()

    def savePostingInfo(self) -> None:
        file = "postingInfo.txt"
        with open(file, 'w') as file:
            for listing in self.listingCompensation:
                file.write(f"{listing}\n")

def main():
    scraper = CraiglistScraper("https://boston.craigslist.org/search/ggg?is_paid=yes#search=1~thumb~0~0")
    scraper.startscrape()
    for i in range(6):
        scraper.getListings()
        scraper.clickNextPage()
    scraper.savePostingInfo()
    #time.sleep(10)
    print(scraper.listingCompensation)

main()


"""
This was going to be a process so I knew I had to break it down. First I decided which listings I was specifically going to look at. I decided on listings that had the pay clearly stated in the listing as "compensation."

Next I had to figure out how to get this payment data from each listing. First I figured out a way to get each listing as an element in a list so I could access the title, date posted, and compensation. I did this by finding all instances of classes that contained a 
listing, which in this case was a "result-info" class. Next I had to figure out how to extract only the just the compensation part of each listing. To do so I did a similar process and found the class containing all the compensation info. The issue I had here was
that I also got how long ago the posting was made as part of my result. However, this was very easy to work around and I just split the string and selected which part I wanted. 
"""

