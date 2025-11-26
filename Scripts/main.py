import pandas as pd
from datacleaning import clean_dataset
from mysql_upload import upload_dataframe
from sql_queries import run_sql_queries
from visualization import visualize



'''def load_dataset(path):
    print("\n📌 Loading dataset...")
    df = pd.read_csv(path)
    print("Dataset Loaded Successfully!")
    print(df.head())
    return df'''
def main():
    # Load dataset
    df = pd.read_csv("data/customer.csv")

    # Clean
    df = clean_dataset(df)

    # Upload to MySQL
    upload_dataframe(df)

    # Run SQL insights
    run_sql_queries()

    # Visualizations
    visualize(df)

# -------- 6. CREATE TABLE + INSERT DATA INTO MYSQL -------- #


# -------- 7. RUN SQL ANALYTICS -------- #

# -------- 8. VISUALIZATIONS -------- #



# -------- 9. MAIN FUNCTION -------- #



# -------- 10. ENTRY POINT -------- #
if __name__ == "__main__":
    main()