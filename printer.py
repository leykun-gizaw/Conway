def prntr(mat):
    for row in mat:
        for elem in mat[0]:
            print(elem.get(), end=" ")
        print()
