import random

name = input('Enter your name: ')
print("Hello", name, "what would you like to decide on?")

print("""Select any of the following:
1. Food
2. Movies
3. Songs
4. Books
""")
def selection():
    select = input('Enter your choice: ')
    
    if select == 'food':
            print('What would you like to eat')
            print("""Select any of the following:
            1. Breakfast
            2. Lunch
            3. Dinner
            """)
            a_select = input('Enter your choice: ')
            if a_select == 'breakfast':
                breakfast = ["Instant Oatmeal with Cranberries and Pecans", "Roasted Potato and Chorizo Hash", "PB Chocolate Sheet Pancake", "Sausage and Egg Sandwiches"]
                b = random.choice(breakfast)
                print("I think you should eat", b, "for breakfast")

                answer = input("Would you like to get any other suggestion?: ")
                if answer == "yes":
                    print("""Select any of the following:
                    1. Food
                    2. Movies
                    3. Songs
                    4. Books
                    """)
                    selection()
                else:
                    print("Bye:)...")
                    exit()

            if a_select == 'lunch':
                lunch = ["Rice and stew", "Beans and Dodo", "Jollof rice and chicken", "Fried potato and tomato egg stew"]
                c =  random.choice(lunch)
                print("I think you should eat", c, "for breakfast")

                answer = input("Would you like to get any other suggestion?: ")
                if answer == "yes":
                    print("""Select any of the following:
                    1. Food
                    2. Movies
                    3. Songs
                    4. Books
                     """)
                    selection()
                else:
                    print("Bye:)...")
                    exit()

            if a_select == 'Dinner':
                dinner = ["Plantain porridge", "Semovita/Eba with Okra Soup", "Spaghetti with beef stew", "Rice stew garnished with vegetables"]
                d =  random.choices(dinner)
                print("I think you should eat", d, "for breakfast")

                answer = input("Would you like to get any other suggestion?: ")
                if answer == "yes":
                    print("""Select any of the following:
                    1. Food
                    2. Movies
                    3. Songs
                    4. Books
                     """)
                    selection()
                else:
                    print("Bye:)...")
                    exit()
selection()


    
