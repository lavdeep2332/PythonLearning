# pascal triangle.

#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1
x=""
for i in range(5):
    print((5-i)*" ", end="")
    x=str(11**i)
    for j in x:
        print(j, end=" ")
    print()