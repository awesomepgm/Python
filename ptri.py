def main(nx,r = 0):
    import math
    if type(r)==str:
        r=r.lower()
    fout=()
    out=set()
    out12=[]
    out3=[]
    for x in range(1,nx+1):
        for y in range(1,nx+1):
            out12=[x,y]
            out3 =math.sqrt((out12[0] ** 2) + (out12[1] ** 2))
            if out3.is_integer() == True:
                if r in ['yes', 1, '1']:
                    if x and y and out3 not in out:
                        out.add(x)
                        out.add(y)
                        out.add(out3)
                        fout=fout+((out12[0], out12[1], int(out3)),)
                else:
                    fout=fout+((out12[0], out12[1], int(out3)),)
    return(fout)