import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
from colorama import Fore, Style, init

# Initialize Colorama for colored terminal output
init(autoreset=True)

# ASCII Art Logo
def print_logo():
    logo = """
  ██████╗  █████╗ ███████╗██████╗  █████╗ ██████╗ ██╗  ██╗
 ██╔════╝ ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝
 ██║  ███╗███████║███████╗██████╔╝███████║██████╔╝ ╚███╔╝ 
 ██║   ██║██╔══██║╚════██║██╔═══╝ ██╔══██║██╔═══╝   ██╔╝  
 ╚██████╔╝██║  ██║███████║██║     ██║  ██║██║       ██║   
  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝       ╚═╝   
    """
    print(Fore.CYAN + logo)
    print(Fore.YELLOW + "Author: SAURABH aka (Ace)")
    print(Fore.YELLOW + "-" * 60)


# Main Menu
def main_menu():
    print_logo()
    print(Fore.GREEN + "[1] Start Backlink Submission Process")
    print(Fore.RED + "[2] Exit")
    choice = input(Fore.YELLOW + "\nEnter your choice: ")
    return choice


# Backlink Submission Script
def submit_backlinks():
    # Initialize Excel Workbook
    wb = Workbook()
    ws = wb.active
    ws.append(["Submission URL", "Submitted Backlink URL", "Status"])  # Add headers to the Excel file

    # Path to your WebDriver
    driver_path = "/path/to/chromedriver"  # Replace with your WebDriver path
    driver = webdriver.Chrome(executable_path=driver_path)

    # List of backlink submission URLs
    backlink_sites = [
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
    "https://www.optimisationdirectory.info/",
    "https://www.projectcollabmanila.neobacklinks.net/",
    "https://zendirectory.neobacklinks.net/",
    "https://www.exactseek.com/",
    "http://www.targetsviews.com/",
    "http://www.idahoindex.com/",
    "http://www.fat64.net/",
    "https://gainweb.org/",
    "https://www.canadawebdir.com/",
    "https://24directory.com.ar/",
    "https://gcast.info/",
    "https://www.blpdirectory.info/",
    "https://www.blackgreendirectory.com/",
    "https://redlavadirectory.com.ar/",
    "https://thedirectory.com.ar/",
    "http://www.livepopular.com",
    "https://www.besttopdir.info/",
    "http://www.info-listings.com",
    "http://www.freeprwebdirectory.com",
    "http://www.allfreethings.com",
    "http://www.britainbusinessdirectory.com",
    "https://bidsyndicate.neobacklinks.net/",
        # Add more URLs from your list here
    ]

    # Information to be submitted
    backlink_data = {
        "name": "Your Name",
        "email": "your_email@example.com",
        "website": "https://yourwebsite.com",
        "description": "Your website description here."
    }

    try:
        print(Fore.CYAN + "Starting backlink submission process...\n")

        for index, site in enumerate(backlink_sites, start=1):
            print(Fore.YELLOW + f"[{index}/{len(backlink_sites)}] Submitting to: {site}")
            try:
                driver.get(site)
                time.sleep(3)  # Wait for the page to load

                # Example form submission (modify the selectors based on each site's form structure)
                driver.find_element(By.NAME, "name").send_keys(backlink_data["name"])
                driver.find_element(By.NAME, "email").send_keys(backlink_data["email"])
                driver.find_element(By.NAME, "website").send_keys(backlink_data["website"])
                driver.find_element(By.NAME, "description").send_keys(backlink_data["description"])
                driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Adjust the XPath as needed

                time.sleep(3)  # Wait for submission to complete

                # Get the current URL (confirmation page URL or final page URL)
                submitted_url = driver.current_url

                # Log success
                ws.append([site, submitted_url, "Success"])
                print(Fore.GREEN + f"✔ Successfully submitted to: {site}")
                print(Fore.GREEN + f"  Submitted URL: {submitted_url}\n")

            except Exception as e:
                # Log failure
                ws.append([site, "", f"Failed: {e}"])
                print(Fore.RED + f"✘ Failed to submit to: {site}")
                print(Fore.RED + f"  Error: {e}\n")

    finally:
        # Save the Excel file
        excel_path = "submitted_backlinks_with_urls.xlsx"
        wb.save(excel_path)
        print(Fore.CYAN + f"\nProcess complete. Excel file saved at: {excel_path}")

        # Close the browser
        driver.quit()
        print(Fore.CYAN + "Browser closed.")


# Main Program
if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            submit_backlinks()
        elif choice == "2":
            print(Fore.RED + "\nExiting... Goodbye!")
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again.")
