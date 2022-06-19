from comtypes.client import CreateObject
import os.path
import getopt
import sys


n = 1
f = "data/group.xlsx"

# get option from cmd
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# parsing opts value
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# path to file
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

# start Exel generator
xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
# generate groups name
for i in range(n):
    xl.Range[f"A{i+1}"].Value[()] = f"group {i}"
wb.SaveAs(file)
xl.Quit()