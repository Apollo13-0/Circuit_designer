class Ordenamiento:
    """
    Es la clase que almacena los algoritmos de ordenamiento
    """

    def shellSort(array):
        """
        Este realiza el ordenamiento de una lista ordenada atraves del algoritmo shellShort
        :return: La lista ordenada
        """
        n = len(array)
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval

                array[j] = temp
            interval //= 2

    def insertionSort(nlist):
        """
        Este realiza el ordenamiento de una lista atraves del algoritmo insertionSort
        :return: La lista ordenada
        """
        for index in range(1,len(nlist)):

            currentvalue = nlist[index]
            position = index

            while position>0 and nlist[position-1]>currentvalue:
                nlist[position]=nlist[position-1]
                position = position-1

            nlist[position]=currentvalue

