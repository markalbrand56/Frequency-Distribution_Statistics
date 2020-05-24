import collections


def simple_frequencies(list):
    import time
    counter = collections.Counter(list) #Counts each appearence of each number. This returns it in the format {(value, count), (value, count)}

    print("\nValue ==> Frequency ==> Accumulated") 
    accumulated = 0 #Accumulated frequency
    for key, value in counter.items():
        accumulated += value
        time.sleep(0.05)
        print("{}   |   {}   |   {}".format(key, value, accumulated)) 


if __name__ == "__main__":
    lst = [10.0, 12.0, 12.0, 12.0, 1300.0, 144.0, 15.0, 15.0, 15.0, 16.0, 17.0, 17.0, 18.0, 21.0, 23.0, 24.0, 24.0, 25.0, 25.0, 26.0, 26.0, 32.0, 32.0]
    lst = sorted(lst)
    print(len(lst))
    simple_frequencies(lst)