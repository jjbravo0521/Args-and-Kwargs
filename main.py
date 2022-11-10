def my_sum(num1,num2):
  print(num1,num2)

print(my_sum(3,4,5))
def a_sum (*args):

# args are for entering
# as many argunents as poossible
  for num in args:
    print(num)

print(a_sum(1))
print(a_sum(1,3))
print(a_sum(1,3,4,5,6))