

def main():
    with open('data.txt', 'r') as f:
        content = f.readlines()
        stripped = list(map(lambda x: x.replace('\n', ''), content))
        doubles = 0
        triples = 0
        for box in stripped:
            d = False
            t = False
            for letter in box:
                letter_count = box.count(letter)
                if letter_count == 2 and d == False:
                    print('DOUBLE', letter)
                    doubles += 1
                    d = True
                elif letter_count == 3 and t == False:
                    triples += 1
                    t = True
        print(doubles, triples)
        print(doubles * triples)

if __name__ == '__main__':
  main()