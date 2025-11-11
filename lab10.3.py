import matplotlib.pyplot as plt
import numpy as np

magazines = {
    "Наука і Техніка": {"price": 50, "copies": 8000},
    "Мандрівник": {"price": 45, "copies": 12000},
    "IT-Світ": {"price": 60, "copies": 9000},
    "Здоров’я": {"price": 40, "copies": 15000},
    "Історик": {"price": 55, "copies": 7000}
}
labels = list(magazines.keys())
copies = [magazines[m]["copies"] for m in labels]
def func(pct, allvals):
    absolute = int(np.round(pct/100. * np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute} прим.)"
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(
    copies,
    autopct=lambda pct: func(pct, copies),
    textprops=dict(color="white"),
    startangle=140
)
ax.legend(
    wedges,
    labels,
    title="Журнали",
    loc="center left",
    bbox_to_anchor=(1, 0.5, 0.3, 1)
)
plt.setp(autotexts, size=11, weight="bold")
ax.set_title("Розподіл тиражу журналів за рік", fontsize=15)
plt.show()