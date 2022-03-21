def array_input():
    try:
        array = []
        rows = int(input("enter the row size:"))
        cols = int(input("enter the columns size:"))
        for i in range(rows):
            columns = []
            for j in range(cols):
                values = int(input("enter the values:"))
                columns.append(values)
            array.append(columns)

        # For printing the matrix
        for i in range(rows):
            for j in range(cols):
                print(array[i][j], end=" ")
            print()

    except ValueError:
        print("Something went wrong! Please try again ...")


if __name__ == '__main__':
    array_input()
