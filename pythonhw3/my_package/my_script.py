import pickle


def do_the_thing():
    filename = input("введите имя файла: ")
    with open(filename + '.txt', 'w') as f:
        data = list(iter(input, 'quit'))
        count = 0
        for line in data:
            f.write(line+"\n")
            count = count+1

    metadata = {'filename': filename,
                'count': count}
    with open('metadata.pkl', 'wb') as f:
        pickle.dump(metadata, f)

    with open('metadata.pkl', 'rb') as f:
        loaded_info = pickle.load(f)
    print(loaded_info)

    name_of_file = metadata['filename']
    with open(name_of_file+'.txt') as f:
        for line in f:
            print(line)