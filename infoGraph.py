import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import matplotlib
#plotly.setCredentials(uname='email', apiKey='a;lsdkjf adfa;dkfj')

x=[1, 2, 3, 4]
y=[10, 15, 13, 17]

trace0 = go.Scatter(x=x, y=y, mode='markers')

trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9],
    mode='markers'
)
data = [trace0, trace1]

py.plot(data, filename = 'basic-line', auto_open=True)
#Matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Graph')
plt.savefig("test.png")
plt.show()



