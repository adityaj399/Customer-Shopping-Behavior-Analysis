import pandas as pd

def clean_dataset(df):
    print("\n📌 Cleaning Dataset...")

    # Standardizing column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df.rename(columns={"purchase_amount_(usd)": "purchase_amount_usd"}, inplace=True)

    # Handling missing values for Review Rating
    if "review_rating" in df.columns:
        df["review_rating"] = df.groupby("category")["review_rating"].transform(
            lambda x: x.fillna(x.median())
        )

    # Feature Engineering – Age Group
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 25, 40, 60, 100],
        labels=["Young Adult", "Adult", "Middle-aged", "Senior"],
        right=False
    )

    # Purchase frequency (days)
    if "previous_purchases" in df.columns:
        df["purchase_frequency_days"] = 365 / (df["previous_purchases"] + 1)

    # Drop redundant column
    if "promo_code_used" in df.columns:
        df.drop("promo_code_used", axis=1, inplace=True)

    print("Cleaning Completed!")
    print(df.info())

    return df
