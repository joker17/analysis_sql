#!/usr/local/bin/python3
import re

file = open("data.sql", 'r', encoding='UTF-8')
# lines = file.readlines()
text = file.read()
text = text.upper()

#被更新的表名
#tb_name = "tstockinfo"
tb_name = "jc_tconvertmarketno"
test_word = "code"
tb_name = tb_name.upper()
test_word = test_word.upper()

#截取 from 和 where 之前的语句
index1 = text.find("FROM")
index2 = text.find("WHERE")
text1 = text[index1:index2]
print(text1)

#正则表达式匹配，获取更新表名的别名 如t、a
regular = "%s[ +](\w)[,|\s]" % (tb_name)
print(regular)
#out1 = re.findall(regular, text1)
out1 = re.findall(regular, text1)
print(out1)
str1 = out1[0]
print(str1)

#正则匹配，该表名在视图sql里所有的相关字段名
#key_word = re.findall("\w", str1)
#print(key_word[0])
#regular1 = "%s\.(\w+|\w+_\w+)" % (key_word[0])
regular1 = "%s\.(\w+|\w+_\w+)" % (str1)
#print(regular1)
out2 = re.findall(regular1, text)
print(out2)
