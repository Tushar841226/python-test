A=[2,3,1,2,1]
S=0
n=len(A)

visited=[False]*n

current = S
right = True

while True:
    if visited[current]:
        print(-1)
        break

    visited[current] = True
    steps = A[current]
    if right:
        next_index = current + steps
    else:
        next_index=current - steps
    if next_index < 0 and next_index >= n:
        print(A[current])
        break
    current=next_index
    right = not left

    print("Hello Tushar")

    print("Hello Tushar")

    print("Hello Tushar")


    
