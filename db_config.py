# library untuk koneksi Python ke PostgreSQL
import psycopg2


def get_connection():
    # membuat koneksi ke database
    conn = psycopg2.connect(
        host="localhost",      # alamat server database
        port=5432,             # port PostgreSQL
        database="test_db",    # nama database
        user="postgres",       # username PostgreSQL
        password=""   # password PostgreSQL
    )
    
    return conn  # mengembalikan object koneksi