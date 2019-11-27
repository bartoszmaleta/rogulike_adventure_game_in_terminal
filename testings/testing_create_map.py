def create_map(file_name):
    # board = []
    # # -------------------------------------    CSV
    # file_name2 = "map2.csv"
    # crimefile = open(file_name2, 'r')
    # reader = csv.reader(crimefile)
    # allRows = [row for row in reader]
    # print(allRows)
    # print('-------------------------------------')
    # for elem in allRows:
        # print(elem)
    print('------------------------------------- should print file_obj')
    print()
    myFile = open(file_name, "r+")
    myLines = list(myFile)
    myFile.close()
    # print(len(myLines))
    # print(myLines)
    
    board2 = []
    small_list = []
    counter = 0

    for line in myLines:
        board2.append(line)

    list_of_map = []
    list_of_map.append(board2)
    print('-------=====================')
    print(board2)  # wrong, lists with lines
    print('-------=====================')
    print(list_of_map)      # list with lists with lines
    print('-------=====================')
    for row in board2:
    # this one could be one line!!!!! :
    # print(''.join(row))
        for element in row:
            print(element, end="")
    print()

    print('-------=====================')
    # with open(file_name) as file_obj:
    #     list_of_file = file_obj.readlines()

    #     print(type(list_of_file))
    #     print(list_of_file)

    #     for line in list_of_file:
    #         print(len(line))
    #         for row_index in range(len(line)):
    #             board = []
    #             for col_index in range(len(line)):
    #                 board.append(line[col_index])
    #                 # board[row_index][col_index] = line[col_index]

    # print(board)        

    # print()
        # for row_index in range(len(file_obj)):
            # board = []
            # for character in line:
                # board.append(character)
            # print(line, end='')
    # print('-------------------------------------')
    # -------------------------------------    
    # with open(file_name) as file_obj:
        # for line in file_obj:
            # for character in line:
                # board.append(character)
            # print(line, end='')
    # print('-------------------------------------')
    # print(type(board))
    
    # for elem in board:
        # print(elem, end='')
    # # print(board)