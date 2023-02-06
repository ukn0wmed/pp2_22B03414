def reverse(string):
    data = string.split(" ")
    n = len(data)
    result = data[n-1]
    for i in range(n-2, -1, -1):
        result = result + " " + str(data[i])
    print(result)


my_string = "We are ready"
reverse(my_string)