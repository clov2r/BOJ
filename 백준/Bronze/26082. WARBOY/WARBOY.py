A, B, C=map(int, input().split())
'''
가격 대비 성능이 경쟁사 제품의 3배
경쟁사 제품의 가격 대비 성능 B/A
WARBOY의 가격 대비 성능 X/C
3배가 되어야 하므로 3*(B/A)=X/C
X=3*B*C//A
'''
print(3*B*C//A)