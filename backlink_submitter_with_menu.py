import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import openpyxl

# ASCII Art for the menu
def print_ascii_menu():
    os.system('clear')
    print(r"""
     _______  _______  _______  _______  _______  ______  
    (  ____ \(  ____ \(  ___  )(       )(  ____ \(  __  \ 
    | (    \/| (    \/| (   ) || () () || (    \/| (  \  )
    | (__    | |      | |   | || || || || (__    | |   ) |
    |  __)   | |      | |   | || |(_)| ||  __)   | |   | |
    | (      | |      | |   | || |   | || (      | |   ) |
    | )      | (____/\| (___) || )   ( || (____/\| (__/  )
    |/       (_______/(_______)|/     \|(_______/(______/ 
                                                        
    Author: Saurabh aka (Ace)
    """)
    print("[1] Submit Backlinks")
    print("[2] Exit")
    print()

# Initialize Firefox WebDriver
def initialize_driver():
    options = Options()
    options.headless = False  # Set to True to run in headless mode (no browser UI)
    service = Service("/usr/local/bin/geckodriver")
    return webdriver.Firefox(service=service, options=options)

# Submit backlinks from the list
def submit_backlinks(driver, backlinks):
    submitted_urls = []
    for url in backlinks:
        try:
            print(f"Submitting to: {url}")
            driver.get(url)
            time.sleep(3)  # Adjust wait time if necessary
            
            # Example interaction: locate and fill forms (modify selectors as needed)
            if "submit.php" in url or "submit" in url.lower():
                driver.find_element(By.NAME, "url").send_keys("https://example.com")
                driver.find_element(By.NAME, "title").send_keys("Example Website")
                driver.find_element(By.NAME, "description").send_keys("This is an example description.")
                driver.find_element(By.NAME, "submit").click()
                print(f"Submitted: {url}")
                submitted_urls.append(url)
        except Exception as e:
            print(f"Failed to submit: {url} | Error: {e}")
    return submitted_urls

# Save submitted URLs to an Excel file
def save_to_excel(submitted_urls):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Submitted URLs"
    sheet.append(["Submitted Backlinks"])

    for url in submitted_urls:
        sheet.append([url])

    file_name = "submitted_backlinks.xlsx"
    workbook.save(file_name)
    print(f"\nSubmitted backlinks saved to {file_name}")

# Main menu
def main():
    print_ascii_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        # List of backlinks (Updated)
        backlinks = [
            "https://www.highrankdirectory.com/submit.php",
            "https://www.sitepromotiondirectory.com/",
            "https://www.promotebusinessdirectory.com/",
            "https://gainweb.org/submit.php?",
            "https://www.poec.info/",
            "https://poec.info/",
            "https://www.inyectronicawc.com/",
            "https://www.welcomelinks.info/",
            "https://zendirectory.com.ar/",
            "https://www.marketinginternetdirectory.com/",
            "http://www.drtest.net/",
            "https://www.pr8directory.com/",
            "https://FiveStarsAutoPawn.com",
            "https://premium.uklinks.info/",
            "https://seo.optimisationdirectory.info/",
            "https://newfreedirectory.com.ar.neobacklinks.net/",
            "https://www.submityourlink.com.ar/",
            "https://www.alexa.com.ar/",
            "https://ukdirectory.com.ar/",
            "https://www.cawausa.neobacklinks.net/",
            "https://bangalore.directorycritic.info/",
            "https://redirectplus.info/",
            "https://newfreedirectory.com.ar/",
            "https://www.moonsunfavor.com/",
            "http://www.online-websites-directory.com/",
            "https://cawausa.neobacklinks.net/",
            "https://www.optimisationdirectory.info/",
            "https://www.inyectronicawc.com/",
            "https://www.projectcollabmanila.neobacklinks.net/",
            "https://zendirectory.neobacklinks.net/",
            "https://www.exactseek.com/",
            "http://www.targetsviews.com/",
            "http://www.drtest.net/",
            "http://www.idahoindex.com/",
            "http://www.fat64.net/",
            "https://www.canadawebdir.com/",
            "https://24directory.com.ar/",
            "https://gcast.info/",
            "https://www.blpdirectory.info/",
            "https://www.blackgreendirectory.com/",
            "https://coastradar.info/",
            "https://redlavadirectory.com.ar/",
            "https://thedirectory.com.ar/",
            "http://picktu.com",
            "http://www.livepopular.com",
            "http://www.allfreethings.com",
            "http://www.freeprwebdirectory.com",
            "http://www.britainbusinessdirectory.com",
            "http://www.info-listings.com",
            "https://bidsyndicate.neobacklinks.net/",
            "https://www.besttopdir.neobacklinks.net/",
            "https://submissionwebdirectory.com/",
            "https://dizila.com/",
            "https://siteswebdirectory.com/",
        ]

        print("\nInitializing Firefox WebDriver...")
        driver = initialize_driver()

        print("\nSubmitting backlinks...")
        submitted_urls = submit_backlinks(driver, backlinks)

        print("\nClosing browser...")
        driver.quit()

        if submitted_urls:
            save_to_excel(submitted_urls)
        else:
            print("\nNo backlinks were successfully submitted.")
    elif choice == "2":
        print("\nExiting... Goodbye!")
    else:
        print("\nInvalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()
