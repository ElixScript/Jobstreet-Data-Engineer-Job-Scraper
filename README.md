# Jobstreet Data Engineer Job Scraper

## Overview

This project is a **web scraping pipeline** built with **Python and Selenium** to collect job listings for **Data Engineer positions** from Jobstreet.
The scraper extracts relevant job information and stores it in a **PostgreSQL database** for further analysis.

The project demonstrates a simple **data pipeline workflow**:

Website → Data Extraction → Data Processing → Database Storage

---

## Features

* Automated job scraping using **Selenium**
* Extraction of key job information:

  * Job title
  * Company name
  * Job location
  * Job teaser / short description
  * Posting date
* Pagination support to scrape multiple pages
* Automatic storage of scraped data into **PostgreSQL**
* Modular and maintainable project structure

---

## Project Structure

```
jobstreet_scraper/
│
├── config.py              # Configuration variables (URL and XPath selectors)
├── driver.py              # Selenium WebDriver setup
├── scrapper.py            # Scraping logic for job cards and pagination
├── db_config.py           # PostgreSQL connection configuration
├── load_to_postgres.py    # Function to insert scraped data into PostgreSQL
├── main.py                # Main pipeline orchestrator
|── README.md              # Project documentation
```

---

## Tech Stack

* **Python**
* **Selenium**
* **PostgreSQL**
* **psycopg2**
* **webdriver-manager**

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/jobstreet-scraper.git
cd jobstreet-scraper
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

Example `requirements.txt`:

```
selenium
webdriver-manager
psycopg2
```

---

## Database Setup

Create a PostgreSQL database before running the project.

Example:

```
CREATE DATABASE test_db;
```

Update the database credentials inside:

```
db_config.py
```

```
host="localhost"
port=5432
database="test_db"
user="postgres"
password="postgres"
```

---

## How to Run

Execute the main pipeline:

```
python main.py
```

The program will:

1. Launch a Selenium Chrome browser
2. Open the Jobstreet Data Engineer jobs page
3. Scrape job listings from multiple pages
4. Collect job details
5. Store the results in a PostgreSQL table

---

## Database Output

The scraper stores data in the table:

```
job_data
```

Table structure:

| Column       | Description                         |
| ------------ | ----------------------------------- |
| job_id       | Primary key                         |
| title        | Job title                           |
| company      | Company name                        |
| location     | Job location                        |
| teaser       | Short job description               |
| date         | Posting date                        |
| date_scraped | Timestamp when the data was scraped |

---

## Example Query

You can view the collected data with:

```
SELECT * FROM job_data;
```

