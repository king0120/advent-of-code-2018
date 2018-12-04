

def main():
    with open('data.txt', 'r') as f:
        content = f.readlines()
        total = 0
        for num in content:
            total += int(num)
        print(total)
        return total

if __name__ == '__main__':
  main()