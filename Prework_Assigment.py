# Python prework assignment

#     Question 1


# def hello_name(user_name):
#     print("Hello_" + user_name)

# hello_name("Dustin")



#     Question 2


# def first_odds():
#     for number in range(1,100):
#        if number % 2 != 0:
#            print(number)
    
# first_odds()



#     Question 3


# def max_num_in_list(a_list):
#     max_num = 0
#     for number in my_list:
#         if number > max_num:
#             max_num = number
#     print(max_num)
            

# my_list=(1,3,5,6,7,2,4,89,69,77,9)

# max_num_in_list(my_list)



#     Question 4



# def is_leap_year(a_year):
#     isLeapYear = False

#     if a_year % 4 == 0:
#         isLeapYear = True

#         if a_year % 400 != 0 and a_year % 100 == 0:
#             isLeapYear = False

#     return isLeapYear

# my_year = 2023
# print(is_leap_year(my_year))



#       Question 5

# def is_consecutive(a_list):
#     previous_number = a_list[0]-1
#     for number in a_list:
#         if number == previous_number +1:
#             previous_number = number
#         else:
#             return False

#     return True

# a_list = (1,2,3,4,5,6,7)

# print(is_consecutive(a_list))