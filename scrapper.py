from selenium.webdriver.common.by import By

# Mengimpor XPath dari file config
from config import (
    XPATH_JOB_CARD,
    XPATH_JOB_TITLE,
    XPATH_COMPANY,
    XPATH_LOCATION,
    XPATH_TEASER,
    XPATH_DATE
)

from datetime import datetime
import time


def scrape_job_cards(driver):
    results = []  # menyimpan hasil scraping

    # mengambil semua job card di halaman
    job_cards = driver.find_elements(By.XPATH, XPATH_JOB_CARD)

    for card in job_cards:
        # mengambil informasi dari setiap job card
        title = card.find_element(By.XPATH, XPATH_JOB_TITLE).text
        company = card.find_element(By.XPATH, XPATH_COMPANY).text
        location = card.find_element(By.XPATH, XPATH_LOCATION).text

        teaser_el = card.find_element(By.XPATH, XPATH_TEASER)
        date_el = card.find_element(By.XPATH, XPATH_DATE)

        # mengambil text menggunakan javascript
        job_teaser = driver.execute_script(
            "return arguments[0].textContent;", teaser_el
        )

        job_date = driver.execute_script(
            "return arguments[0].textContent;", date_el
        )

        # menyimpan hasil scraping ke dictionary
        results.append({
            "title": title,
            "company": company,
            "location": location,
            "teaser": job_teaser,
            "date": job_date,
            "date_scraped": datetime.now()
        })

    return results


def scrape_and_click(driver, num_of_next=0):
    full_data = []

    # jika ingin scraping beberapa halaman
    if num_of_next > 0:
        full_data = scrape_job_cards(driver)

        for _ in range(num_of_next):
            # klik tombol next
            next_button = driver.find_element(By.XPATH, "//*[@title='Selanjutnya']")
            next_button.click()

            time.sleep(2)  # menunggu halaman berikutnya load

            # scraping halaman berikutnya
            full_data += scrape_job_cards(driver)

    else:
        # hanya scraping satu halaman
        full_data = scrape_job_cards(driver)

    return full_data