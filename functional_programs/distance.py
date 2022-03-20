'''
Take the input from the user 
Find the distance between two points x,y
using the formula to find the distance math.sqrt((x ** 2) + (y ** 2))
'''


def find_distance():
    try:
        x = int(input("Enter the value of X : "))  # taking the input from the user
        y = int(input("Enter the value of y : "))  # taking the input from the user

        distance = (x ** 2) + (y ** 2) ** (1 / 2)
        print("The distance between", (x, y), "is:", distance)

    except ValueError:
        print("No valid integer! Please try again ...")


if __name__ == "__main__":
    find_distance()
