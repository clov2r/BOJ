T=int(input()) #전체 테스트 케이스의 수
for i in range(T):
   A, B=map(int, input().split()) #A=수강생의 수 B=제출한 수
   A_list=set(range(1, A+1)) #수강생의 수 리스트
   B_list=set(map(int, input().split())) #제출한 학생들의 숫자
   C_list=A_list-B_list
   print('#%d'%(i+1), *C_list)