import csv
from F1_scraper_dictionary import return_dictionaries
from bs4 import BeautifulSoup as bs
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

def scrape_data(raceURLcode, driverCode):
    options = ChromeOptions()
    options.headless = True
    driver = Chrome(executable_path='Applications/driver/chromedriver', options=options)
    URL = "https://en.mclarenf-1.com/2022/gp/" + raceURLcode + "/lap_times/" + driverCode + "-" + driverCode + "/"
    driver.get(URL)
    soup = bs(driver.page_source, 'lxml')
    lap_element = soup.find_all('tr', role="row")
    lap = 1
    laptimes = []
    for potential_lap in lap_element:
        if len(potential_lap.contents) == 5:
            if len(potential_lap.contents[2]) > 1:
                if lap != 0 and len(potential_lap.contents[2].contents[-1]) < len(potential_lap.contents[2].contents[-2]):
                    laptimes.append([lap,potential_lap.contents[2].contents[-2],potential_lap.contents[2].contents[-1].text])
                else:
                    laptimes.append([lap,potential_lap.contents[2].contents[-1],"N/A"])
                lap += 1
    return laptimes
    
def write_to_csv(laptimes, raceYear, raceName, driverName):
    filename = "" + raceName.replace(" ","") + "_" + raceYear + "_" + driverName.replace(" ","") + ".csv"
    print(filename)
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(['Lap Number', 'Lap Time', 'Event'])

        # write data to file
        writer.writerows(laptimes)

if __name__ == "__main__":
    raceURLdict, driverDict = return_dictionaries() 

    exitKey = 1
    while exitKey != "0":
        print(
            "Options: \n0 -> exit\nanything else -> get lap times"
        )
        exitKey = input()

        while exitKey != "0":
            print(
                "\nEnter Race Year: "
            )
            raceYear = input()

            if raceYear in raceURLdict.keys():
                
                print("\nEnter Race Number:")
                for key, elem in raceURLdict[raceYear].items():
                    print(key, elem[0])
                raceNum = input()

                if raceNum in raceURLdict[raceYear].keys():
                    raceName = raceURLdict[raceYear][raceNum][0]
                    raceURLcode = raceURLdict[raceYear][raceNum][1]
                    
                    print("\nEnter Driver Number:")
                    for key, elem in driverDict.items():
                        print(key, elem[0])
                    driverNum = input()
                    if driverNum in driverDict:
                        driverName = driverDict[driverNum][0]
                        driverCode = driverDict[driverNum][1]
                        laptimes = scrape_data(raceURLcode, driverCode)
                        

                        if len(laptimes) < 1:
                            # if laptimes is empty, most likely the driver was not driving
                            print("Sorry this driver did not start this race, please try again.")
                            exitKey = "1"
                        else:
                            write_to_csv(laptimes, raceYear, raceName, driverName)
                            print(laptimes)
                            exitKey = "0"
                    else:
                        print('Driver not supported')

                else:
                    print('Race not found')
            else:
                print('Year not supported')

    exit()


