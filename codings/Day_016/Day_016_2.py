# creating a code which provides table in a ascii format
# using prettytable package

# pretty table package is downloaded from the extension in pycharm

from prettytable import PrettyTable

table = PrettyTable()    # table as object, PrettyTable() as class
# print(table)   # printing an empty table

'''output:
    ++
    ||
    ++
    ++
'''

# refer the documentation of the package before using it from pypi website

table.add_column("Name",["hritick","aswin","karthi"])
table.add_column("Reg_no",["21BAD203","21BAD204","21BAD207"])

print(table)


'''
output:
    +---------+----------+
    |   Name  |  Reg_no  |
    +---------+----------+
    | hritick | 21BAD203 |
    |  aswin  | 21BAD204 |
    |  karthi | 21BAD207 |
    +---------+----------+
'''