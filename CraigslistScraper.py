from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class CraigslistScraper:
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

    def startScrape(self) -> None:
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
            self.listingCompensation.append(listingPay)

    def clickNextPage(self) -> None:
        """
        Finds and clicks the next page button
        :return: None
        """
        nextPageButton = self.driver.find_element(By.CSS_SELECTOR, ".bd-button.cl-next-page.icon-only").find_element(By.CSS_SELECTOR, ".icon.icom-")
        nextPageButton.click()

    def savePostingInfo(self) -> None:
        """
        Saves date listing was made and compensation for each listing to text file
        :return: None
        """
        file = "postingInfo.txt"
        with open(file, 'w') as file:
            for listing in self.listingCompensation:
                file.write(f"{listing}\n")

def main():
    # Initialize Craigslist scraper
    scraper = CraigslistScraper("https://boston.craigslist.org/search/ggg?is_paid=yes#search=1~thumb~0~0")

    # Get URL and start scraping
    scraper.startScrape()

    # Loop through each page and
    for i in range(6):
        scraper.getListings()
        scraper.clickNextPage()

    # save posting data to text file
    scraper.savePostingInfo()

    # For testing
    #time.sleep(10)
    #print(scraper.listingCompensation)

main()

