import matplotlib.pyplot as plt
from theme import THEME as t
from theme import pie_color as p 
def pie_chart(ser, title="bar chart"):
    max_value = max(ser.values)
    plt.figure(figsize=(7, 7),
               facecolor=t["back"])
    plt.pie(ser.values, labels=ser.index,
            autopct="%1.1f%%",
            shadow=True,
            startangle=90,
            explode=[0.1 if value == max_value else 0 for value in ser.values],
            colors= p)
    plt.title(title)
    plt.show()