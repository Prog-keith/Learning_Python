my_list = ['FizzBuzz' if(i % 3 == 0 and i % 5 == 0)
else 'Fizz' if(i % 3 == 0)
else 'Buzz' if(i % 5 == 0)
else str(i) for i in range(1, 100)]
print(my_list)
# string = " ".join(my_list)
# print(string)
# for i in my_list:
#     print(i)
