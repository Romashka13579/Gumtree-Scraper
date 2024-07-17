import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
import json
import os.path



def item_scraping(item_id, link):
    driverForLinks.get(link)
    name = driverForLinks.find_element(By.CSS_SELECTOR, "[data-q='vip-title']")
    price = driverForLinks.find_element(By.CSS_SELECTOR, "[data-q='ad-price']")
    description = driverForLinks.find_element(By.CSS_SELECTOR, "[itemprop='description']")
        
    print(name.text, price.text)
    data[str(item_id)] = {"name" : name.text, "price": price.text, "description": description.text, "link": link}
    writeToJSONFile('./','savedData', data)
    print("__________%s____________"% i)


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)



options = uc.ChromeOptions() 
options.headless = False
options.headless = False

driver = uc.Chrome(options=options) 
driverForLinks = uc.Chrome(headless=False) 

item_id = 0
i = 100 
cookies = 1

linksChecked = []
data = {}

if os.path.exists('./savedData.json'):
    with open('./savedData.json', 'r') as file:
        data = json.load(file)
    for item in data:
        linksChecked.append(data[""+item+""]["link"])
        item_id = int(item)

while i!=0:
    pages = 0

    with driver:
        driver.get("https://www.gumtree.com/search?featured_filter=false&q=&search_location=uk&search_category=for-sale&urgent_filter=false&sort=date&search_scope=false&photos_filter=false&min_price=0&max_price=1")
    time.sleep(2)

    while pages!=2 and driver.find_elements(By.CSS_SELECTOR, "[data-q='pagination-forward-page']"):
        if cookies == 1:
            driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
            cookies = 0
        time.sleep(2)
        for item in driver.find_elements(By.CSS_SELECTOR, "[data-q='search-result-anchor']"):
            if item.get_attribute("href") not in linksChecked:
                linksChecked.append(item.get_attribute("href"))
                item_scraping(item_id, item.get_attribute("href"))
                item_id = item_id+1
        pages=pages+1
        driver.find_element(By.CSS_SELECTOR, "[data-q='pagination-forward-page']").click()
        time.sleep(2)
    i = i-1

driver.quit()
driverForLinks.quit()
