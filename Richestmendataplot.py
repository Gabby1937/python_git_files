import matplotlib.pyplot as plt

slices = [224, 144, 136, 123, 114, 103, 99.1, 98.1, 96, 95.9]
names = ['Elon Musk\n $224 Billion',
         'Jeff Bezos\n $144 Billion',
         'Bernard Arnault\n $136 Billion',
         'Bill Gates\n $123 Billion',
         'Warren Buffett\n $114 Billion',
         'Larry Page\n $103 Billion',
         'Sergey Brin\n $99.1 Billion',
         'Gautam Adani\n $98.1 Billion',
         'Mukesh Ambani\n $96 Billion',
         'Steve Ballmer\n $95.9 Billion']
cols = ['r','g','b','c','g','m','w','y','c','b']

plt.pie(slices,
        shadow=True,
        colors=cols,
        labels=names,
        startangle=90,
        explode=(0,0,0,0,0,0,0.1,0,0,0),
        autopct='%1.1f%%')

plt.title("Top 10 Richest Men")
plt.show()
