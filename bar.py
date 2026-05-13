from theme import THEME as t
import matplotlib.pyplot as plt
def bar_chart(ser, title= "bar chart",
              xlabel="lables", ylabel= "values"):
     plt.figure(figsize=(8, 5),
               facecolor=t["back"])
     plt.bar(ser.index, ser.values, color=t["main"])
     plt.title(title,
              color=t["text"],
              fontsize=16)
     plt.xlabel(xlabel)
     plt.ylabel(ylabel)
     plt.title(title,
              color=t["text"],
              fontsize=16)
     plt.xticks(ser.index)
     plt.yticks(ser.values)
     plt.show()
