color_dict={'black':0, 'brown':1, 'red':2, 'orange':3,
            'yellow':4, 'green':5, 'blue':6, 'violet':7,
            'grey':8, 'white':9}
res1=input()
res2=input()
res3=input()
tot=int(str(color_dict[res1])+str(color_dict[res2]))
if res3=='black':
    print(tot*1)
elif res3=='brown':
    print(tot*10)
elif res3=='red':
    print(tot*100)
elif res3=='orange':
    print(tot*1000)
elif res3=='yellow':
    print(tot*10000)
elif res3=='green':
    print(tot*100000)
elif res3=='blue':
    print(tot*1000000)
elif res3=='violet':
    print(tot*10000000)
elif res3=='grey':
    print(tot*100000000)
elif res3=='white':
    print(tot*1000000000)