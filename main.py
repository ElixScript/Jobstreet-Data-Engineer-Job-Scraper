from driver import create_driver
from config import JOBSTREET_URL
from scrapper import scrape_and_click
from db_config import get_connection
from load_to_postgres import load_data


def main():

    # membuat browser selenium
    driver = create_driver()

    # membuka halaman jobstreet
    driver.get(JOBSTREET_URL)

    # scraping data (3 halaman berikutnya)
    data = scrape_and_click(driver, num_of_next=3)

    # membuat koneksi ke postgres
    conn = get_connection()

    # menyimpan data ke database
    load_data(data, conn)

    # menutup browser dan koneksi database
    driver.quit()
    conn.close()


# menjalankan program
if __name__ == "__main__":
    main()