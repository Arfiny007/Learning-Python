print("----Basic Calculator----")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

option = int(input("Select Your Operation : "))

if(option == 1 ) :
    first_number = int(input("Enter Your First Number : "))
    second_number = int(input("Enter Your Second Number : "))
    result = first_number+second_number
    print("Addition Result : "+ str(result))
elif option == 2 :
    first_number = int(input("Enter Your First Number : "))
    second_number = int(input("Enter Your Second Number : "))
    result = first_number-second_number
    print("Substraction Result : "+ str(result))
elif option == 3 :
    first_number = int(input("Enter Your First Number : "))
    second_number = int(input("Enter Your Second Number : "))
    result = first_number*second_number
    print("MultiplicationResult : "+ str(result))
elif option == 4 :
    first_number = int(input("Enter Your First Number : "))
    second_number = int(input("Enter Your Second Number : "))
    result = first_number/second_number
    print("Division Result : "+ str(result))
elif option == 5 :
        print("Exiting Calculator. Goodbye!")
else:
        print("Invalid option. Please select a number between 1 and 5.")