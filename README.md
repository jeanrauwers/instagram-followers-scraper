# instagram-get-follower-scraper

This script uses Selenium and the ChromeDriver to scrape the number of followers for a given Instagram account. It saves the number of followers to a text file called "followers.txt" in the same directory as the script.

# How to use:

Required to have Python 3 installed -> https://www.python.org

1. Install Python on your system if it's not already installed.
2. Rename .env.example to .env and add ig username in example file.
3. Install the required packages using the command pip install -r requirements.txt.
4. Open the command prompt or terminal and navigate to the directory where the script is saved.
5. Run the script using the command `python run.py`.
6. The script will look for an environment variable called USERNAME and use its value as the account name.
7. Wait for the script to complete execution. Once it's done, the total number of followers for the given Instagram account will be saved in a file called followers.txt in the same directory where the script is saved.

p.s. Optionally If you want to scrape followers of a specific Instagram account using an argument, you can pass the account name as a command-line argument. For example, `python run.py account_name`.
