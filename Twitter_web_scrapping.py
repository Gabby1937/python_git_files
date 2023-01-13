# Opening a web page with just the text file.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.twitter.com',80))
cmd = 'GET http://www.twitter.com HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

quit()
text = "X-DSPAM-Confidence:    0.8475"
x = text.find(' ')
print(x+1)
y = text.find(str(x))
print(y)
loc = text[x+1 :]
print(float(loc))


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

quit()

names = ['Sarah', 'Caleb', 'Joshua ashawo', 'Praise', 'Gabriel','Uche', 'Mary']
for a in names:
   if a in names == 'Joshua ashawo':
      break
      print(a)






Temp = int(input("What is your body temperature: "))
if Temp > 40:
    print("Your Temp is too high")
    print('Please consult your doctor')
elif Temp < 37:
    print("Your Temp is too low")
    print('Please consult your doctor')
else:
    print("You are perfectly fine.")



normal_Temp = range(37,41)
Temp = input("what's your body temperature:  ")
if Temp == normal_Temp:
    print("You are fine.")

elif  Temp < normal_Temp:
    print("Your Temp is too low")
    print('Please consult your doctor')
elif Temp > normal_Temp:
    print("Your Temp is too high")
    print('Please consult your doctor')
    



First_name = input('Please input your first name :')
Surname = input('Please input your surname :')
Age = input('Please input your age')
print(f"""Hello {First_name} {Surname},
    Welcome to our website, please kindly confirm that you're {Age} before we continue

""")


quit()







Accesories = ['bag', 'jewelries', 'head_band', 'knukcle rings', 'glasses']
for a in Accesories:
    if a == 'head_band':
        break
    print(a)


dog = dict()
dog['name'] = 'Kitana'
dog['command'] = 'sit'
dog['Breed'] = 'Chiwawa'
dog['Gender'] = 'Female'
dog['Type'] = 'Puppy'
for a,v in dog.items():
    print(v)

    
    
    
