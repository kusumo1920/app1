# 1
# essay_file = open("files6/essay.txt", "r")
# essay_content = essay_file.read()
# essay_file.close()
# print(essay_content.title())

# 2
# essay_file = open("files6/essay.txt", "r")
# essay_content = essay_file.read()
# essay_file.close()
# print(len(essay_content))

# 3
# members_file = open("files6/members.txt", "r")
# members_list = members_file.readlines()
# members_file.close()
#
# new_member = input("Add a new member: ").strip()
# members_list.append(f"{new_member}\n")
# members_file = open("files6/members.txt", "w")
# members_file.writelines(members_list)
# members_file.close()

# 4
# filenames = ["one.txt", "two.txt", "three 3.txt"]
# for filename in filenames:
#     gen_file = open(f"files6/{filename}", "w")
#     gen_file.write("Hello\n")
#     gen_file.close()

# 5
# filenames = ["files6/a.txt", "files6/b.txt", "files6/c.txt"]
# for filename in filenames:
#     file = open(filename, "r")
#     print(file.read())
