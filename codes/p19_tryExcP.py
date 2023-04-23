# # Ex.
# try:
#     1 / 0
# except ZeroDivisionError:
#     print('Divided by zero')

# print('Ex.: Should reach here')

# # Ex2.
# try:
#     open("fantasy.txt")
# except:
#     print('Something went wrong')
# print('Ex2.: Should reach here')

# # Ex3.
# try:
#     x = input("Enter number: ")
#     x = x + 1
#     print(x)
# except:
#     print("Ex3.: Invalid input")

# # Ex4.


# def fail():
#     1 / 0


# try:
#     fail()
# except:
#     print('Exception occured')
# print('Program continues')

# # Ex5.
# try:
#     f = open("test.txt")
# except:
#     print('Could not open file')
# finally:
#     f.close()
# print('Program continue')

# # Ex6.
# try:
#     x = 1
# except:
#     print('Failed to set x')
# else:
#     print('No exception occured')
# finally:
#     print('We always do this')

# # Ex7.
# raise MemoryError("Out of memory")

# # Ex8.
# raise ValueError("Wrong value")

# # Ex9.
# class LunchError(Exception):
#  pass
# raise LunchError("Programmer went to lunch")

# # Ex10.
# class NoMoneyException(Exception):
#     pass


# class OutOfBudget(Exception):
#     pass


# balance = int(input("Enter a balance: "))
# if balance < 1000:
#     raise NoMoneyException
# elif balance > 10000:
#     raise OutOfBudget