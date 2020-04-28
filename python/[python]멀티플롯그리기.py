# [pyrhon] matplotlib.pyplot 여러개의 플롯 그리기

import matplotlib.pyplot as plt
x=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
y=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
for i in range(len(x)):
    plt.figure()
    plt.plot(x[i],y[i])
