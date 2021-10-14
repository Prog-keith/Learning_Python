

num_list = [1,5,6,7,9,34,56,77,100]

filter(lambda x : x > 10, num_list)

greater_than_10_list = list(filter(lambda x : x > 10, num_list))
print(greater_than_10_list)

less_than_50_list = list(filter(lambda y: y < 50, num_list))
print(less_than_50_list)

even_list = list(filter(lambda z: z % 2 == 0, num_list))
print(even_list)

greater_than_10_less_50_list = list(filter(lambda x : x > 10 and x < 50, num_list))
print(greater_than_10_less_50_list)
