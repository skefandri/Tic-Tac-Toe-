
# # x = 4

# # if x == 3:
# #     print("hello world")
# # else:
# #     print("hadchi mrid")

# # for x in range(1,6, 2):
# #     print(x) 
# # name = input("enter your name: ")

# # print("Hello " + name)

# # name = input("enter the first number: ")
# # name1 = input("enter the second number: ")

# # result =  float(name) + float(name1)

# # print(result)

# # def fun(name):
# #     print( "Hello " + name)

# # fun(input()) 
# # def functions():
# number=[4,2,4,6,7,8,4,3,1,1,3,5,6,7,8,9,53,2,7]
# print(set(number))


worker_file = open("text", "r")

print(worker_file.readlines())


worker_file.close()