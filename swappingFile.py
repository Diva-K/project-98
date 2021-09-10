def swapFileData():
    file1=input('enter the name of the first file')
    file2=input('enter the name of the second file')
    with open (file1, 'r') as A:
        data_A=A.read()
    with open (file2, 'r') as B:
        data_B=B.read()
    with open (file1, 'w') as A:
        A.write(data_B)
    with open (file2,'w') as B:
        B.write(data_A)
swapFileData()

