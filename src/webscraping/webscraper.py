'''
@author: TSGGO
Created on 20 Jan 2022
'''

# Importing the necessary libraries of OS, CSV, Time, Selenium, etc.
import os, csv
import time
from selenium import webdriver

#https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python

from selenium.webdriver.firefox.service import Service

#https://exerror.com/deprecationwarning-find_element_by_-commands-are-deprecated-please-use-find_element-instead/

from selenium.webdriver.common.by import By

from word_counter import WordAnalysis #imported to run word counter

lot_names=[]
periods=[]
sell_prices=[]
links=[]

s = Service(r"C:\Users\HP\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe") #this driver could be found in the "Project Data" Folder

browser = webdriver.Firefox(service=s)

#weblinks of four group of lots, which contains the arefacts's sales data.

urls = ["https://www.christies.com/en/auction/antiquities-29064/",
        "https://www.christies.com/en/auction/antiquities-29150/",
        "https://www.christies.com/en/auction/antiquities-29063/",
        "https://www.christies.com/en/auction/antiquities-28980/"]
       
for url in urls:
    browser.get(url)
   
    if url == "https://www.christies.com/en/auction/antiquities-29064/": #this is to close the popups of cookies and membership

        browser.implicitly_wait(30)
        browser.find_element(By.XPATH, '//*[@id="onetrust-pc-btn-handler"]').click()
        browser.implicitly_wait(30)
        browser.find_element(By.XPATH, '//*[@id="onetrust-pc-sdk"]/div[3]/div[1]/button').click()
        browser.implicitly_wait(30)
        #browser.find_element(By.XPATH, '//*[@id="close_signup"]').click() #NOTE: Kindly close the membership pop-up manually!
        '''
        If you get the following error, selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: //*[@id="close_signup"]
        kindly comment out line #49: browser.find_element(By.XPATH, '//*[@id="close_signup"]').click()
        please run the code again and manually close the membership prompt pop-up as soon as it appears
        '''
   
    # These lines of codes slowly scrolls down the page, to load new entries.
   
    y = 1000
    for timer in range(0,50):
        browser.execute_script("window.scrollTo(0, "+str(y)+")")
        y += 1000  
        time.sleep(1)
   
   
    containers = browser.find_elements(By.CLASS_NAME, "chr-lot-tile__container")
    for container in containers:
       
        #Retrieves the antiquty's name.
        
        if container.find_element(By.CLASS_NAME, "chr-lot-tile__primary-title"):
            #print(container.find_element(By.CLASS_NAME, "chr-lot-tile__primary-title").text) #Commented it out since it was only for testing purpose 
            lot_names.append(container.find_element(By.CLASS_NAME, "chr-lot-tile__primary-title").text)
           
        #Retrieves the period of the object.
       
        if container.find_element(By.CLASS_NAME, "chr-lot-tile__secondary-title"):
            #print(container.find_element(By.CLASS_NAME, "chr-lot-tile__secondary-title").text) #Commented it out since it was only for testing purpose 
            periods.append(container.find_element(By.CLASS_NAME, "chr-lot-tile__secondary-title").text)
           
        #Retrieves the price that the artefact got sold for.
           
        try:
            if container.find_element(By.CLASS_NAME, "chr-lot-tile__secondary-price"):
                #print(container.find_element(By.CLASS_NAME, "chr-lot-tile__secondary-price").text) #Commented it out since it was only for testing purpose 
                sell_prices.append(container.find_element(By.CLASS_NAME, "chr-lot-tile__secondary-price").text)
           
        except:
            loc = ('No Data') # An precaution since Christies can sometimes pull off a lot's data
            #print(loc) #Commented it out since it was only for testing purpose 
            sell_prices.append(loc)
       
        #This gets the links to the object's descriptive page
       
        if container.find_element(By.TAG_NAME, "a"):
            #print(container.find_element(By.TAG_NAME, "a").get_attribute('href')) #Commented it out since it was only for testing purpose
            links.append(container.find_element(By.TAG_NAME, "a").get_attribute('href'))
    
      
    #print(lot_names) #Commented it out since it was only for testing purpose
    #print(periods) #Commented it out since it was only for testing purpose
    #print(sell_prices) #Commented it out since it was only for testing purpose
    #print(links) #Commented it out since it was only for testing purpose
    
    
#defining a variable fileOutput
fileOutput='scrape_data.csv'

pn = os.path.abspath(__file__)
pn = pn.split("src")[0]

#pathway is now the string of the directory of the csvfile.
pathway=os.path.join(pn,'data',fileOutput)

#creates 10 columns, and store them into fieldanmes.
fieldnames=['Object Name','Price', 'Period','Link']

#opens the csvfile to write data
#with open(pathway, 'w') as csvf:
with open(pathway,'w',newline='', encoding = 'utf-8-sig') as csvf:
   
    #writer is now written as dictionary type.
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)
   
    #writes the header in the csv file.
    writer.writeheader()
   
    #length of self.objectid is the same as the length of the actual number of links.
   
    for i in range(len(lot_names)):
       
        #writerow({}) inputs data as dictionary type (id - value pair). i is the counter.
       
        writer.writerow({'Object Name': lot_names[i],'Price': sell_prices[i],'Period':periods[i],'Link':links[i]})


f= open(os.path.join(pn,'data','objnames.txt'), 'w') #opens a txt file        
for word in lot_names:        
    f.write(word) #writes the data of result into the txt file
    
f= open(os.path.join(pn,'data','period.txt'), 'w') #opens a txt file        
for word in periods:        
    f.write(word) #writes the data of result into the txt file
        
runAnalysis=WordAnalysis()#calls the class wordanalysis
        
runAnalysis.word_count('objnames.txt')#This gives a preliminary inference on the most used words, which is used to determine what cultures and materials dominate to plan the excel anlaysis.   

#runAnalysis.word_count('period.txt')#runs the method wordcount, Commented it out since it was only for testing purpose. Might be effectively used if run with MWELemmetizer 
        
#print("Done") #Commented it out since it was only for testing purpose 