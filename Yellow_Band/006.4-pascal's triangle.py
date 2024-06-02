def print_pascals_triangle(n):

    triangle = [[1]]


    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # The last element of each row is always 1
        triangle.append(row)


    for row in triangle:
        print(' '.join(map(str, row)))


n = int(input("Enter the number of rows for Pascal's Triangle: "))


print_pascals_triangle(n)
