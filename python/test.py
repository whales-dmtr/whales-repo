import os

name_new_file = input('>>>')
with open('1.py', mode='r', encoding='UTF-8') as myfile, open(name_new_file, mode='w', encoding='UTF-8') as newfile:
    r = myfile.readlines()
    newfile.writelines(r)
os.system(f"mv {name_new_file} tasks/mytasks")
