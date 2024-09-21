def task11(A,B):
    if len(A) != 3 or len(B) != 3:
        raise ValueError("У каждого вектора должно быть 3 координаты")
    
    x = A[1]*B[2] - A[2]*B[1]
    y = A[2]*B[0] - A[0]*B[2]
    z = A[0]*B[1] - A[1]*B[0]

    return (x,y,z)

vector_a = (1,2,3)
vector_b = (4,5,6)
answer = task11(vector_a,vector_b)

print(f"Векторное произведение = {answer}")