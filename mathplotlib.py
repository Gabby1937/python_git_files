import matplotlib.pyplot as plt

slices = [2,2,7,7]
Nclass = ['ss3','ss2','jss1','jss2']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=Nclass,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('Classes of Student')
plt.show()
