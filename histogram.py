def histogram(list):
    n = len(list)
    for i in range(0, n):
        result = ""
        for j in range(0, list[i]):
            result = result + "*"
        print(result)



histogram([2, 3, 4])
