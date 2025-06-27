import matplotlib.pyplot as plt
import pandas as pd
import scienceplots
from adjustText import adjust_text
from cycler import cycler

plt.rcParams.update(
    {
        "font.size": 13,
        "font.weight": "normal",
        "axes.labelsize": 14,
        "axes.labelweight": "normal",
    }
)
plt.style.use(
    [
        "science",
        "ieee",
    ]
)
plt.rcParams.update({"figure.dpi": "400"})
plt.rcParams.update(
    {
        "axes.prop_cycle": (
            cycler("color", ["k", "r", "b", "g", "darkorange", "steelblue"])
            + cycler("ls", ["-", "--", ":", "-.", (0, (5, 1)), (0, (3, 1, 1, 1))])
        )
    }
)

# Read the combined CSV file
df = pd.read_csv("../data/model_tracker.csv")

# Define the date format (assuming format is consistent)
date_format = "%d/%m/%Y"  # Adjust this based on the actual date format in the file

# Convert 'Date' column to datetime with specified format and error handling
df["Date"] = pd.to_datetime(df["Date"], format=date_format, errors="coerce")

# Drop rows with invalid dates
df = df.dropna(subset=["Date"])
print(df)

# Filter out non-positive values and rows with NaN
df = df[df["#Params"] > 0]

# Plotting Params vs Year for CV, NLP, and OTHER with color matching the Type column
fig = plt.figure(figsize=(10, 6))

# Scatter plot with color coding based on Model Type
colors = {"NLP": "blue", "CV": "red", "Other": "green"}
print(df["Model Type"].unique())
for model_type in df["Model Type"].unique():
    subset = df[df["Model Type"] == model_type]
    plt.scatter(
        subset["Date"],
        subset["#Params"] / 1e3,
        color=colors[model_type],
        label=model_type,
    )

# Adding labels for the points with dynamic adjustment to avoid overlap
texts = [
    plt.text(
        df["Date"].iloc[i],
        df["#Params"].iloc[i] / 1e3,
        df["Model"].iloc[i],
        fontsize=13,
        ha='center',
        va='center',
        rotation=40,
    )
    for i in range(len(df))
]

# adjust_text(
#     texts,
#     # only_move={"points": "y", "text": "y"},
#     arrowprops=dict(arrowstyle="-", color="r", lw=0.5),
# )

plt.yscale("log")
plt.xlabel("Date")
plt.ylabel("Params (Billions)")
plt.title("Model Parameters Over Time by Type", fontsize=14)
plt.legend()
plt.grid(True, which="both", ls="--")
fig.savefig("./fig_size_vs_date_adjusted.pdf")
# fig.savefig("./fig_size_vs_date_adjusted.png")
