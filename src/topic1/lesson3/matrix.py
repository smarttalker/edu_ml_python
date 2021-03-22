if __name__ == '__main__':

    M1 = [[1, 2, 3, 4, 11],
          [5, -6, 7, 8, 11],
          [5, 2, -42, 8, 11],
          [1, 6, 7, 11, 100]]

    # TODO print ALL elements of matrix
    final_str = ""
    for i in range(len(M1)):
        my_str = "Строка " + str(i) + ": "
        #тут берем размерность строки
        for j in range(len(M1[i])):
            my_str += str(M1[i][j]) + "   "
        final_str += my_str + "\n"
    print(final_str)


    M2 = [[1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
    # TODO print diagonal - 1,-6,5,11
    print(M2)
    final_str = ""
    for i in range(len(M2)):
        final_str += "Элемент " + str(i) + ": " + str(M2[i][i]) + "\n"
    print(final_str)



    """
    так как два следующих задания с квадратной матрицей, то размер по вертикали и горизонтали одинаковый, 
    потому не будем узнавать размер строк
    """


    M3 = [[1, 2, 3, 4],
          [5, 2, 7, 8],
          [5, 6, 3, 8],
          [1, 6, 7, 4]]
    # TODO print diagonal in oposite order  4, 3, 2, 1
    print(M3)
    final_str = "Спава сверху налево вниз\n"
    for i in range(len(M3)):
        final_str += "Элемент " + str(i) + ": " + str(M3[i][len(M3)-i-1]) + "\n"
    print(final_str)

    final_str = "Справа снизу налево вверх\n"
    for i in range(len(M3)):
        final_str += "Элемент: " + str(M3[len(M3)-i-1][len(M3)-i-1]) + "\n"
    print(final_str)