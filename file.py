with open('test_file.txt', 'w') as f: #file will be closed automatically after this block of code
    f.write('meow')
    f.write('\n')
    f.seek(0)
    f.write('ME')
    # f.tell() - returns the number of symbols we have already read
    # f.seek(a) - sets the number of symbols read as a
    # while len(file) > 0:
    #     print(file, end='$')
    #     file = f.read(size_to_read)
    # f.read() - #whole file as it is
    # f.readlines() - #list of lines
    # f.readline() - 1st line
    # f.read(size_to_read)
    # for i in f: # prints whole file
    #     print(i, end='')

