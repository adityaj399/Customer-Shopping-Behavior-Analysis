import mysql.connector
from mysql.connector import Error

host="localhost"
database="customer_db"
user="root"
password="@#Adi123"
 


def mysql_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="customer_db",
            user="root",
            password="@#Adi123"
 
            )
        return conn
    except Error as e:
        print("❌ MySQL Connection Error:", e)
        return None


def upload_dataframe(df):
    print("\n📌 Uploading data to MySQL...")

    conn = mysql_connection()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS customer_data_cleaned")

    create_query = """
        CREATE TABLE customer_data_cleaned (
            customer_id INT,
            age INT,
            gender VARCHAR(20),
            item_purchased VARCHAR(100),
            category VARCHAR(50),
            purchase_amount_usd FLOAT,
            location VARCHAR(50),
            size VARCHAR(10),
            color VARCHAR(20),
            season VARCHAR(20),
            review_rating FLOAT,
            subscription_status VARCHAR(20),
            shipping_type VARCHAR(30),
            discount_applied VARCHAR(10),
            previous_purchases INT,
            payment_method VARCHAR(30),
            frequency_of_purchases VARCHAR(30),
            age_group VARCHAR(20),
            purchase_frequency_days FLOAT
        );
    """
    cursor.execute(create_query)

    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql_insert = f"INSERT INTO customer_data_cleaned ({columns}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

    print("✔ Data Upload Successful!")
