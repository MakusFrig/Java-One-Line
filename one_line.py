import os, sys


file = open(f'{sys.argv[1]}', 'r')

contents = file.read().replace("\n", "").replace("\t", "")

new_path = sys.argv[1].split("/")

old_file_name = new_path[len(new_path)-1]

new_file_name = "new_" + old_file_name

new_path = new_path[:len(new_path)-1]

new_path = "/".join(new_path) + "/"

for each_letter in range(len(contents)):

	if contents [each_letter : each_letter + len(old_file_name.split(".")[0])] == old_file_name.split(".")[0]:

		contents = contents[:each_letter] + "new_" + old_file_name.split(".")[0] + contents[each_letter + len(old_file_name) - 5:]

		break

new_file = open(f'{new_path}{new_file_name}', 'w')

new_file.write(contents)


print(contents)

print(new_path, new_file_name)