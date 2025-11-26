import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df):
    print("\n📌 Generating Visualizations...")

    sns.countplot(x="gender", data=df)
    plt.title("Customer Count by Gender")
    plt.show()

    sns.barplot(x="age_group", y="purchase_amount", data=df, estimator=np.mean)
    plt.title("Average Purchase Amount by Age Group")
    plt.show()

    sns.barplot(x="shipping_type", y="purchase_amount", data=df)
    plt.title("Purchase Amount by Shipping Type")
    plt.show()

    print("✔ Charts Created!")