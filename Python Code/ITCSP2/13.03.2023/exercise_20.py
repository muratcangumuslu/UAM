def cube(x):
    return x ** 3

my_list = [1, 2, 3, 4, 5]
cubed_list = list(map(cube, my_list))
print(cubed_list)
