

with open('targets.txt', 'r') as f:
    for line in f:
        item1, item2, *everything_else = line.split('-')
        print(item1, item2, '-'.join(everything_else))
