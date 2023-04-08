# 1
# def l_to_c_converter(liters):
#     return liters / 1000
#
#
# print(l_to_c_converter(5500))

# 2
# password = input("Enter a password: ")
#
# def check_password(password):
#     result = {}
#
#     if len(password) >= 8:
#         result["length"] = True
#     else:
#         result["length"] = False
#
#     digit = False
#     for i in password:
#         if i.isdigit():
#             digit = True
#     result["digits"]: digit
#
#     uppercase = False
#     for i in password:
#         if i.isupper():
#             uppercase = True
#     result["upper-case"] = uppercase
#     return result
#
#
# if all(check_password(password).values()):
#     print("Strong Password")
# else:
#     print("Weak Password")
