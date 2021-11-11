from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/Users/Shahar Reuven/Documents/שחר/Job/DevOps Expert/Lesson 4 - Testing/chromedriver.exe")
website_url = "https://www.kan.org.il/"
my_driver.get(website_url)
