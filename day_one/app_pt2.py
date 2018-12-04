def main(hist={}, total=0):
    print(hist)
    with open('data.txt', 'r') as f:
        content = f.readlines()
        for num in content:
            total += int(num)
            if str(total) in hist:
                print("HIT")
                print(total)
                return total
            else:
                hist[str(total)] = True
        print("LET'S GO AGAIN")
        main(hist, total)

if __name__ == '__main__':
  main()