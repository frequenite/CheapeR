#Crawler code
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
#making an incognito session in chrome
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
#activatin chrome driver
browser = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe', options=option)
#Here comes the target website
#I am not sure for which all websites scraping is legal with a bot...
browser.get("https://github.com/TheDancerCodes")
#We need to set up th time limit for the TimeOut error or it will go onn executing.
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class=’avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out ...Your internet might be slow or check the URL and try again")
    browser.quit()
# find_elements_by_xpath returns an array of selenium objects.
titles_content = browser.find_elements_by_xpath("//a[@class='text-bold flex-auto min-width-0']")
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_content]
# print out all the titles.
print('titles:')
print(titles, '\n')

language_element = browser.find_elements_by_xpath("//p[@class=’mb-0 f6 text-gray’]")
# same concept as for list-comprehension above.
languages = [x.text for x in language_element]
print("languages:")
print(languages, '\n')
#zipping titles to corresponding language
for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')
#    
