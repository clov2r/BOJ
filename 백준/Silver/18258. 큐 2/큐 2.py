import sys
from sys import stdin

from collections import deque
queue=deque()

def push(x) :
    queue.append(x)


# print(queue)
# # pop(x)는 리스트의 x번째 요소를 리턴하고 그 요소는 삭제
def pop():
    if(len(queue) == 0):
        print(-1)   
    else:
        print(queue.popleft()) # 가장 왼쪽 요소 반환 및 삭제

def size():
    print(len(queue))

def empty():
    if(len(queue) == 0):
        print(1)
    else:
        print(0)

def front(): ## 가장 앞에 있는 정수(먼저 들어온)
    if(len(queue)==0):
        print(-1)
    else:
        print(queue[0])

def back(): ## 가장 뒤에 있는 정수
    if(len(queue)==0):
        print(-1)
    else:
        print(queue[-1])

N = int(stdin.readline())
for i in range(N): #0~ 14까지 for(i = 0; i<15 ; i++)
    k = stdin.readline().split()
    if(k[0] == 'push'):
        push(int(k[1]))
    elif(k[0]=='pop'):
        pop()
    elif(k[0]=='size'):
        size()
    elif(k[0]=='empty'):
        empty()
    elif(k[0]=='front'):
        front()
    elif(k[0]=='back'):
        back()
