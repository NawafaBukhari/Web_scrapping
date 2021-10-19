#%%
# Import libraries
import pandas as pd
import requests 
from bs4 import BeautifulSoup
#%%
# Assign a target
URL = "https://realpython.github.io/fake-jobs/"
# get page as html
page = requests.get(URL)

# Print HTML Page code
print(page.text)
#%%
# Assign Page to BS to to extract data
soup = BeautifulSoup(page.content, "html.parser")
#Find data that is going to be extracted
results = soup.find(id="ResultsContainer")
#find specific content
job_elements = results.find_all("div", class_="card-content")
#%%
# lists to store data we want to get
job = []
company = []
location = []

#%%
#Iterate through all elements 
for job_element in job_elements:
    #find title job's name
    title_element = job_element.find("h2", class_="title")
    #find company's name
    company_element = job_element.find("h3", class_="company")
    #find company's location
    location_element = job_element.find("p", class_="location")
    #store all data into list
    job.append(title_element.text.strip())
    company.append(company_element.text.strip())
    location.append(location_element.text.strip())
    
# %%
#create dataframe using lists
df = pd.DataFrame(list(zip(job, company,location)),
               columns =['Job_Title', 'Company_Name','Location'])
#%%
df

# %%
