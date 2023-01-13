#name, gender, class, student number
data = dict()
List = []
def Input(student):
    student = input("New data name: ")
    data["name"] = input('Enter your name: ')
    data["gender"] = input('Gender: ')
    data["Class"] = input('Class: ')
    data["studNo"] = int(input('Student number: '))
    List.append(student)
    return student + " has been successfully added."

def show(name):
    for k,v in name.items():
        print({k:v})




def All():
    print(data)

#print(Input("temi"))
show("dgh")

#data

quit()


temi = dict()
temi["name"] = "Temilade Bamigboye"
temi["gender"] = "female"
temi["Class"] = "ss3"
temi["studNo"] = 1001
print(temi)
for k,v in temi.items():
    print({k:v})






quit()


user = input()
count = 0
a = dict()
for i in user:
    count += 1
    a[i] = count
print(a)
    




a[key] = value
a
{key:value},{key2:val2},{key3:val3}
