import collections


def frequency(list):
    counter = collections.Counter(list)
    #keys = counter.keys()
    #print(keys)

    print("\nValue ==> Frequency ==> Accumulated")
    accumulated = 0
    for key, value in counter.items():
        accumulated += value
        print("{}   |   {}   |   {}".format(key, value, accumulated))


#lst = [10.0, 12.0, 12.0, 12.0, 1300.0, 144.0, 15.0, 15.0, 15.0, 16.0, 17.0, 17.0, 18.0, 21.0, 23.0, 24.0, 24.0, 25.0, 25.0, 26.0, 26.0, 32.0, 32.0]
#frequency(lst)