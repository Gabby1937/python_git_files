import matplotlib.pyplot as plt

slices = [6, 8, 4, 8, 6, 6, 6, 8, 12, 4]
phone_ram = ['iPhone 13 Pro Max\n 6GB',
         'Samsung Galaxy S22 Ultra\n 8GB',
         'iPhone 13\n 4GB',
         'Google Pixel 6\n 8GB',
         'Google Pixel 5a\n 6GB',
         ' Samsung Galaxy A53\n 6GB',
         'iPhone 13 Pro\n 6GB',
         'OnePlus 10 Pro\n 8GB',
         'Google Pixel 6 Pro\n 12GB',
         'iPhone SE (2022)\n 4GB']
cols = ['r','g','b','c','g','m','w','y','c','b']

plt.pie(slices,
        shadow=True,
        colors=cols,
        labels=phone_ram,
        startangle=0,
        explode=(0,0,0,0,0,0,0.1,0,0,0),
        autopct='%1.1f%%')

plt.title("Top 10 phones and their RAM size ")
plt.show()
