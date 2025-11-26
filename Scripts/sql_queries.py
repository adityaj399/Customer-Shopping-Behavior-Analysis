from mysql_upload import mysql_connection

def run_sql_queries():
    print("\n📌 Running SQL Analysis...")

    conn = mysql_connection()
    if conn is None:
        return

    cursor = conn.cursor()

    queries = {
        "Revenue by Gender":
            "SELECT gender, SUM(purchase_amount_usd) FROM customer_data_cleaned GROUP BY gender;",

        "Top Rated Products":
            "SELECT item_purchased, AVG(review_rating) AS avg_rating FROM customer_data_cleaned GROUP BY item_purchased ORDER BY avg_rating DESC LIMIT 5;",

        "Shipping Type Impact":
            "SELECT shipping_type, ROUND(AVG(purchase_amount_usd),2) FROM customer_data_cleaned GROUP BY shipping_type;",

        "Subscribers vs Non-Subscribers":
            """
            SELECT subscription_status,
                   COUNT(*) AS total_customers,
                   ROUND(AVG(purchase_amount_usd),2) AS avg_spend,
                   SUM(purchase_amount_usd) AS total_revenue
            FROM customer_data_cleaned
            GROUP BY subscription_status;
            """
    }

    for title, q in queries.items():
        print(f"\n✔ {title}:")
        cursor.execute(q)
        for row in cursor.fetchall():
            print(row)

    cursor.close()
    conn.close()
