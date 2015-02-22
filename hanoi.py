# Simple recursive program for towers of hanoi
def towers(disks,src,spare,dest):

    if(disks == 1):
        print("Move from "+src+" to "+dest)
    else:
        towers(disks-1,src,dest,spare)
        print("Move from "+src+" to "+dest)
        towers(disks-1,spare,src,dest)

towers(3,'A','B','C')
