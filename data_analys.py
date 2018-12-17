import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import json
import datetime
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
from get_data import get_data

data = get_data(limit = 500)#json.loads(open("data.json").read())['RECORDS'];
print('loaded')
x = [datetime.datetime.strptime(i[1], "%Y.%m.%d %H:%M:%S") for i in data]
y = [n for n, i in enumerate(data)]
names = np.array([str(i[0]) for i in data])

norm = plt.Normalize(1,4)
cmap = plt.cm.RdYlGn



fig,ax = plt.subplots()
line, = plt.plot(x,y, marker="o")
plt.style.use("seaborn-darkgrid")

annot = ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    x,y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                           " ".join([names[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = line.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)
plt.xlabel("Time")
plt.ylabel("Count")
plt.show()

