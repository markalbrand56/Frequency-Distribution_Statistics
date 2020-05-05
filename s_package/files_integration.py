def custom_file(name):
    file = name + ".txt"
    file = open(file, 'rt')
    file = file.readlines()
    #file = file.remove('\n')
    #file = file.replace(',', ' ')
    raw_data = []
    for data in file:
        raw_data.append(data)
    print(raw_data)
    

    

custom_file("data_fd") 