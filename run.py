import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as CM
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TIMEOUT = 15
USERNAME = os.getenv('USERNAME')
dirname = os.path.dirname(__file__)

def scrape():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")   # Uncomment this option to run it headless
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)
    instagram = 'https://www.instagram.com/'
    url = instagram + str(USERNAME)

    bot.get(url)

    time.sleep(3.5)

    print('[Info] - Scraping Followers...')
    followers_span = bot.find_element(By.CSS_SELECTOR,
    "span[title]")

    total_followers = followers_span.get_attribute('title')

    print('[Info] - Saving...')
    print('[Info] - Total of ' + total_followers + ' followers')
    print('[DONE] - Your total followers are saved in followers.txt file!')

    with open(os.path.join(dirname, 'followers.txt'), 'r+') as file:
        file.seek(0, 0)  
        file.write(total_followers) 


if __name__ == '__main__':
    scrape()
