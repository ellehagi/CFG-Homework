list1 = [1, 2, 3, 4, 5, 6, 7]
user_input = input('please enter seven numbers separated by comma(Between 1-50): ')
list2 = [int(x) for x in user_input.split(',')]


a = set(list1)
b = set(list2)


if len(a & b) == 3:
    print("you win 20")

elif len(a & b) == 4:
    print("you win 40")


elif len(a & b) == 5:
    print("you win 100")

elif len(a & b) == 6:
    print("you win 10000")

elif len(a & b) == 7:
  print("you win 1000000")

else:
    print("Sorry! you don't win anything.")