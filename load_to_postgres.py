def load_data(data, conn):
    # membuat cursor untuk menjalankan query SQL
    cursor = conn.cursor()

    create_table = """
        CREATE TABLE IF NOT EXISTS job_data (
        job_id SERIAL PRIMARY KEY,
        title TEXT,
        company TEXT,
        location TEXT,
        teaser TEXT,
        date TEXT,
        date_scraped TIMESTAMP
    );
    TRUNCATE TABLE job_data RESTART IDENTITY;
    """

    # membuat tabel jika belum ada lalu menghapus data lama
    cursor.execute(create_table)

    insert_query = """
    INSERT INTO job_data
    (title, company, location, teaser, date, date_scraped)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # memasukkan setiap data hasil scraping ke database
    for row in data:
        cursor.execute(insert_query, (
            row["title"],
            row["company"],
            row["location"],
            row["teaser"],
            row["date"],
            row["date_scraped"]
        ))

    # menyimpan perubahan ke database
    conn.commit()

    # menutup cursor
    cursor.close()