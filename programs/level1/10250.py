import sys

lines = sys.stdin.read().splitlines()
case_num = int(lines[0])
data_list = [{"H": int(h), "W": int(w), "N": int(n)} for h, w, n in (line.split() for line in lines[1:case_num+1])]

for case in data_list:
    if case["N"]%case["H"] == 0:
        H = case["H"]* 100
        W = case["N"]//case["H"]
    else:
        H = case["N"]%case["H"]*100
        W = case["N"]//case["H"]+1
    print(H+W)