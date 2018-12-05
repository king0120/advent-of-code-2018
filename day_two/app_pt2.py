def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def main():
    with open('data.txt', 'r') as f:
        content = f.readlines()
        stripped = list(map(lambda x: x.replace('\n', ''), content))
        pair = ()
        # Holy shit this is inefficient
        for i, current in enumerate(stripped):
            print(f'checking {i} of {len(stripped)}')
            for other in stripped:
                score = levenshtein(current, other)
                if score == 1:
                    print("ONE", current, other)
                    pair = (current, other)
                    break

        answer = ''
        for i, letter in enumerate(pair[0]):
            print(letter, pair[1][i])
            if letter == pair[1][i]:
                answer+= letter

        print(answer)
if __name__ == '__main__':
  main()