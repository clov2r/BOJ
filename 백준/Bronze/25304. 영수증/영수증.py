num=int(input()) #총 금액
count=int(input()) #구매한 종류의 수
total=0
for i in range(count):
    article, cnt=input().split()
    article =int(article)
    cnt =int(cnt)
    result = int(article*cnt)
    total+=result
if num == total:
    print("Yes")
else:
    print("No")
