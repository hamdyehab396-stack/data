import matplotlib.pyplot as plt
from theme import THEME as t
def line_chart(ser, title="line chart",
               xlabel="X", ylabel="Y"):
    plt.figure(figsize=(8, 5),
               facecolor=t["back"])
    plt.plot(ser.index, ser.values, color=t["main2"],
             marker="o",
             linewidth=3,
             markersize=10,
             markerfacecolor=t["main"],
             markeredgecolor=t["main"])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(color=t["grid"],
             linestyle="--",
             alpha=0.7)
    plt.title(title,
              color=t["text"],
              fontsize=16)
    plt.xticks(ser.index)
    plt.yticks(ser.values)
    plt.show()