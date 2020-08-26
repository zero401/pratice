import sys
def Hours(minute):
    if minute < 0:
        print("It is wrong number.")
    else:
        print("{} H, {} M".format(int(minute / 60), minute % 60))
try:
    Hours(int(sys.argv[1]))
except:
     print("ValueError")
