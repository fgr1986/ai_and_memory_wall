import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scienceplots
from cycler import cycler

plt.rcParams.update(
    {
        "font.size": 11,
        "font.weight": "normal",
        "axes.labelsize": 12,
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

# mpl.rcParams['text.usetex'] = True
# mpl.rcParams['font.family'] = 'serif'
# mpl.rcParams['font.serif'] = ['Computer Modern Roman']

# Read the combined CSV file
df = pd.read_csv("../data/model_tracker.csv")

# Load memory price data
memory_df = pd.read_csv("../data/historical-cost-of-computer-memory-and-storage.csv")
memory_df = memory_df[["Year", "Historical price of memory"]].dropna()
memory_df["Year"] = pd.to_datetime(memory_df["Year"], format="%Y")

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
# fig, ax1 = plt.figure(figsize=(10, 6))
fig, ax1 = plt.subplots(figsize=(10, 5))
# ax2 = ax1.twinx()
#
# memory_df = memory_df[memory_df["Year"] > pd.to_datetime("2010-01-01")]
# ax2.plot(
#     memory_df["Year"],
#     memory_df["Historical price of memory"],
#     color="orange",
#     label="Memory Price",
# )
# ax2.set_ylabel("Memory Price (\$ per GB)")

# Scatter plot with color coding based on Model Type
colors = {"NLP": "blue", "CV": "red", "Other": "green"}
print(df["Model Type"].unique())
for model_type in df["Model Type"].unique():
    if model_type == "Other":
        continue
    subset = df[df["Model Type"] == model_type]
    ax1.scatter(
        subset["Date"],
        subset["#Params"] / 1e3,
        color=colors[model_type],
        label=model_type,
    )

# Adding labels for the points with varied alignment to avoid overlap
alignments = [
    ("right", "top"),
    ("left", "bottom"),
    ("center", "center"),
    ("right", "bottom"),
    ("left", "top"),
]
for i in range(len(df)):
    if df.iloc[i]["Model Type"] == "Other":
        continue
    ha, va = alignments[i % len(alignments)]
    ax1.text(
        df["Date"].iloc[i],
        df["#Params"].iloc[i] / 1e3,
        df["Model"].iloc[i],
        fontsize=12,
        ha=ha,
        va=va,
    )

ax1.set_yscale("log")
# ax2.set_yscale("log")
ax1.set_xlabel("Date")
ax1.set_ylabel("Params (Billions)")
# plt.title("Model Parameters Over Time by Type", fontsize=14)
ax1.legend()
# plt.grid(True, which="both", ls="--")
plt.grid(True, ls="--")
fig.savefig("fig_size_vs_date.pdf")
fig.savefig("fig_size_vs_date.png")
# plt.show()
