import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("New_manufacturing.xlsx")

# Convert efficiency from decimal to percentage and create new column Time Ratio
df["Efficiency %"] = df["Efficiency %"]*100
df["Time Ratio"] = df["Time Difference"]/df["Min batch time"]

# Count batches and st.deviation per Operator and Product 
df["Batch count"] = df.groupby(["Operator", "Product"])["Batch"].transform("count")
df["Deviation Time"] = df.groupby("Operator")["Time Difference"].transform("std")


# ---------------------------------------------------------
#A) First Plot Operator Time Ratio 
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(data=df, x="Operator",y="Time Ratio", palette="viridis")

plt.title("Operator Time Ratio ", fontsize=16, fontweight="bold")
plt.xlabel("Operator", fontsize=12)
plt.ylabel("Time Ratio", fontsize=12)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
#B) Second Plot Product Time Ratio 
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(data=df, x="Product", y="Time Ratio", palette="viridis")

plt.title("Time Ratio by Product", fontsize=16, fontweight="bold")
plt.xlabel("Product", fontsize=12)
plt.ylabel("Time Ratio", fontsize=12)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
#C) Third Plot Product vs Operator Efficiency % (n of Batch>1)
# ---------------------------------------------------------
df = df[df["Batch count"]>1]
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Product", y="Efficiency %", hue="Operator", palette="coolwarm")

sns.stripplot(data=df, x="Product", y="Efficiency %", hue="Operator", 
    dodge=True,color="black",alpha=0.45,
    size=4, legend=False)

plt.title("Product vs Operator Efficiency % (n of Batch>1)", fontsize=16, fontweight="bold")
plt.xlabel("Product", fontsize=12)
plt.ylabel("Efficiency %", fontsize=12)
plt.show()

print(df)
