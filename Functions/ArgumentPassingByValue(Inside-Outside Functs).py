

fruits_list = ["Apple", "Grapes", "Mango", "Bananas"]

def change_list(fruits_list):
    fruits_list  = ["Kiwi", "Strawberry"]
    fruits_list.append("BlackBerry")

def sort_items_and_remove_last(my_list):
    my_list.sort()
    my_list.pop()
    my_list.append("BlackBerry")
    print("Inside the function : ", my_list)

    print("Inside the function : ", fruits_list)


change_list(fruits_list) 
print()
print("Outside the function ", fruits_list)   

sort_items_and_remove_last(fruits_list)  
