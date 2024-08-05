all_record={}
for i in range(8):
    rec, T=input().split()
    M,SS,SSS=rec.split(':')
    res=float(str(int(M)*60+int(SS)) +'.'+SSS)
    all_record[res]=T
all_record=sorted(all_record.items())
point=[10,8,6,5,4,3,2,1]
R,B=0,0
for i in range(8):
    if all_record[i][1]=='R':
        R+=point[i]
    else:
        B+=point[i]
if R>B:
    print('Red')
else:
    print('Blue')