# Selenium Craigslist Scraper Web Scraper
<h4> This was going to be a process so, I knew I had to break it down. First I decided which listings I was specifically 
going to look at. I decided on listings that had the pay clearly stated in the listing as "compensation." I went with this
design choice because these seemed like the most reliable listing that would most likely lead to receiving pay. A lot of
listings that did not have compensation immediately available were often unpaid or questionable gigs, like just filling
and submitting surveys.</h4>

<h4> Next I had to figure out how to get this payment data from each listing. First I figured out a way to get each listing 
as an element in a list so that I could access the date posted, and compensation. I did this by finding all instances 
of classes that contained a listing, which in this case was a "result-info" class. Next I had to figure out how to extract
the compensation and date each listing for later use. To do so I did a similar process and found the class containing the information.
This gave me an issue since when I scraped this data, the time posted and compensation were connected together in a string.
However, this was very easy to work around and I just split the string and selected which part I wanted. Once I this working,
I saved the data to a text file so that I could load it into another program and avoid getting banned by Craigslist since I
would be running this test code a lot</h4>

<h4> Honestly, the hardest part of this challenge was decided exactly how I was going to calculate income per day. 
The reason for this was mainly because while most listing at minimum posted their hourly compensation, most of them did 
not include how long the jobs would take. In order to work around this, I tried to create an average. First, I
would get the first occurrence of a two-digit which corresponded to the minimum hourly possible pay for each listing. 
Next, I essentially did the same thing to get the maximum possible pay per hour. Except for this I collected all instances 
of two-digit numbers and selected the highest one. At this point I averaged out how much I could make on each day hourly and saved that
to a dictionary with the date as the key and average on that day as the value. Once I had this, I then calculated how much
I could make daily if each job was one hour, eight hours, and a random number of hours between 1 and 8.</h4>