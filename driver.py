# Mengimpor webdriver dari Selenium
# Webdriver adalah komponen yang memungkinkan Python mengontrol browser
from selenium import webdriver

# Service digunakan untuk menjalankan chromedriver sebagai service
from selenium.webdriver.chrome.service import Service

# Library untuk otomatis mendownload chromedriver sesuai versi Chrome
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    # Menginstall dan menjalankan chromedriver secara otomatis
    # Tanpa webdriver-manager biasanya kita harus download driver manual
    service = Service(ChromeDriverManager().install())

    # Membuat instance browser Chrome yang akan dikontrol Selenium
    # Browser ini nantinya akan membuka website dan melakukan scraping
    driver = webdriver.Chrome(service=service)

    # Mengembalikan object driver agar bisa digunakan di file lain
    return driver