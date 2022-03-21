'''
Print the roots quadratic equation ax2+bx+c=0
where the values of a,b,c
Two roots to find the equation
'''
import math


def quadratic():
    try:
        a = int(input("Enter the coefficients of X square: "))  # taking the input from the user
        b = int(input("Enter the coefficients of X : "))  # taking the input from the user
        c = int(input("Enter the constants: "))  # taking the input from the user

        # calculating discriminant
        discriminant = b * b - 4 * a * c
        print("Discriminant = ", discriminant)

        # checking the condition  discriminant is 0
        if discriminant == 0:
            print("Roots are real and equal")
            # finding the root values and the discriminant is 0 so that no need to use sqrt
            root1 = (-b) / (2 * a)
            root2 = (-b) / (2 * a)
            print("First roots are {}: ".format(root1))
            print("Second roots are{}: ".format(root2))
        # checking the condition  discriminant is greater than 0
        elif discriminant > 0:
            print("Roots are real and unequal")
            # finding the root values
            root1 = ((-b) + (math.sqrt(discriminant))) / (2 * a)
            root2 = ((-b) - (math.sqrt(discriminant))) / (2 * a)
            print("First roots are : {} ".format(root1))
            print("Second roots are: {}".format(root2))
        else:
            print("Roots are imaginary")

    except ValueError:
        print("Something went wrong!please enter again")


if __name__ == "__main__":
    quadratic()
