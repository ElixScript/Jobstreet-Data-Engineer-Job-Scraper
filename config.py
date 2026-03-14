# URL halaman Jobstreet yang berisi daftar lowongan Data Engineer
# Selenium akan membuka halaman ini sebagai target scraping
JOBSTREET_URL = "https://id.jobstreet.com/id/data-engineer-jobs"


# XPath untuk mengambil semua container job card
# //*  -> cari semua tag HTML
# [@data-card-type='JobCard'] -> filter elemen yang memiliki attribute tersebut
# Setiap job posting berada dalam container ini
XPATH_JOB_CARD = "//*[@data-card-type='JobCard']"


# XPath untuk tombol pagination "Selanjutnya"
# Digunakan untuk berpindah ke halaman berikutnya saat scraping
# Selenium nanti akan menemukan elemen ini lalu menjalankan .click()
XPATH_NEXT_BUTTON = "//*[@title='Selanjutnya']"


# XPath untuk judul pekerjaan di dalam job card
# Titik (.) berarti pencarian dilakukan relatif terhadap job card
# bukan seluruh halaman
XPATH_JOB_TITLE = ".//*[@data-testid='job-card-title']"


# XPath untuk nama perusahaan di dalam job card
# Mengambil elemen yang memiliki attribute data-type='company'
XPATH_COMPANY = ".//*[@data-type='company']"


# XPath untuk lokasi pekerjaan
# Biasanya berisi kota atau informasi remote/hybrid
XPATH_LOCATION = ".//*[@data-type='location']"


# XPath untuk deskripsi singkat pekerjaan (job teaser)
# span dipilih karena elemen ini berupa teks pendek
XPATH_TEASER = ".//span[@data-testid='job-card-teaser']"


# XPath untuk tanggal posting lowongan
# Contoh output: "2 days ago", "1 week ago"
XPATH_DATE = ".//span[@data-automation='jobListingDate']"