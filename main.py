# def my_sum(num1,num2):
#   print(num1,num2)

# print(my_sum(3,4,5))
# def a_sum (*args):

# # args are for entering
# # as many argunents as poossible
#   for num in args:
#     print(num)

# print(a_sum(1))
# print(a_sum(1,3))
# print(a_sum(1,3,4,5,6))
list = [3,4,5,6,7,8,9,10,11,12]
def sum_numbers(list):
  for num in list:
    sum = sum + num
    return sum
    print(sum(list))

# args
def a_sum(*arg):
  total = 0 
for num in args:
  total += num
  # return total
  return sum(args)

print(a_sum(3,4,5,6,7,8,9,10,11,12))