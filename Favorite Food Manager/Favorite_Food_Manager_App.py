favorite_food_list=[]

while True:
    print("-------Welcome-------")
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View All Foods")
    print("4. Exit")

    option=int(input("Choose an option : "))

    if option == 1:
        food=input("Enter Your Favorite Food Name : ")
        favorite_food_list.append(food)
        print(f"{food} has been added to your list.")
    elif option == 2:
         food=input("Enter the Food Name to Remove: ")
         if food in favorite_food_list :
             favorite_food_list.remove(food)
             print(f"{food} has been removed from your list.")
         else:
                print(f"{food} is not in your list.")
    elif option == 3:
            if favorite_food_list:
                print("Your Favorite Foods are:")
                for index, item in enumerate(favorite_food_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your favorite food list is empty.")           
    elif option == 4 :
         print("Thank you! Exiting the program.")
         break
    else:
        print("Invalid option! Please choose a valid option (1-4).")
