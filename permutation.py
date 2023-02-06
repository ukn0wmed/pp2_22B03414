def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            # Swap the ith and jth character
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            # Swap back the ith and jth character to generate other permutations
            data[i], data[j] = data[j], data[i]


def all_permutations(string):
    n = len(string)
    data = list(string)
    permute(data, 0, n)


string = "abc"
all_permutations(string)
