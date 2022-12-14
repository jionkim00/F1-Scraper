# F1-Scraper

## Description

This is a tool that scrapes lap times for a selected year, race, and driver then compiles them into a CSV formatted into lap #, lap time, and events. Events include things like pit stops and crashes.

The F1 Scraper is only functional with data from the 2016-2022 Formula One seasons and works with every driver that has started a race in those seasons.

## Instructions + Dependencies

You will need MacOS, Chrome, Python, BeautifulSoup, and Selenium.

1. Pull BOTH files into directory you wish to save your laptime csv's in
2. Run the F1_scraper.py script
3. Answer requested inputs prompted on the terminal
4. Find your csv in the format Race_Year_FirstnameLastname.csv in the same directory

## Next Steps
More features coming soon!

TODO: 
* Remove Selenium for functionality with request for faster pull and less dependencies
* Check if driver raced in race before data pull to reduce unnecessary requests
* Make compatible with Windows, test Linux compatibility
* Add tire details (Tire hardness and degredation)
* Clear air percentage
* More events (Yellow or Red Flags)
