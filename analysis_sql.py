#!/usr/local/bin/python3

file = open("data.sql", 'r', encoding='UTF-8')
# lines = file.readlines()
text = file.read()

tb_name = "tstockinfo"

# print(lines)
print(text.findall(r"tstock(.+?)test", str2))
print(text.find(tb_name))