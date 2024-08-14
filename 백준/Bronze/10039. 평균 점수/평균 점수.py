X_list=[]
for i in range(5):
    X_list.append(int(input()))
    if X_list[i]<40:
        X_list[i]=40
print(sum(X_list)//len(X_list))
