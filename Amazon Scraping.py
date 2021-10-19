#%%
#import needed libraries
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#open browser
driver = webdriver.Chrome(ChromeDriverManager().install())

#%%
#go to target
driver.get('https://www.amazon.com/');
#wait 5 seconds
time.sleep(5)
#%%
#find search bar and search bar button
search = driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
searchbutton = driver.find_element_by_xpath("//*[@id='nav-search-submit-button']")
#%%
#click on search bar button
search.click()
#send value to bar
search.send_keys('xbox')
#click on search button
searchbutton.click()
#%%
#create lists to store data temporary
t = []
d = []
p = []
#%%
# Iterate from page 1-5
for i in range(6):
    #(wait for 4 seconds then start)
    time.sleep(4)
    #get each product in the page
    Products = driver.find_elements_by_xpath("//*[@class='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16']")
    #iterate through products
    for i in Products:
        #only products that has title, release date and price
        try:
            #get product title
            title = i.find_element_by_xpath(".//*[@class='a-size-medium a-color-base a-text-normal']")
            #get product release date
            date = i.find_element_by_xpath(".//*[@class='a-size-base a-color-secondary a-text-normal']")
            #get product price in dollars without fractions
            price = i.find_element_by_xpath(".//*[@class='a-price-whole']")
            #add variables to lists
            t.append(title.text)
            d.append(date.text)
            p.append(price.text)
            #any product that does not have a title or date or price will not be added
        except:
            print("")
    try:
        #move to the next page
        driver.find_element_by_xpath("//*[@class='a-last']").click()
    except:
        # Last page reached
        print("Last Page")
       

# %%
# create dataframe from lists
df = pd.DataFrame({'Product_Title': pd.Series(t), 'Date': pd.Series(d),'Price($)':pd.Series(p)})
# %%
#display data
df
# %%
