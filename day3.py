with open('day3.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]


def count_trees(right, down):
    tree_count = 0
    i = 0
    for line in input[down::down]:
        i += right
        if line[i % len(line)] == '#':
            tree_count += 1
    return tree_count


print("\n# Part 1")
print("Number of trees: {}".format(count_trees(3, 1)))

print("\n# Part 2")
print("Number of trees for 'Right 1, down 1': {}".format(count_trees(1, 1)))
print("Number of trees for 'Right 3, down 1': {}".format(count_trees(3, 1)))
print("Number of trees for 'Right 5, down 1': {}".format(count_trees(5, 1)))
print("Number of trees for 'Right 7, down 1': {}".format(count_trees(7, 1)))
print("Number of trees for 'Right 1, down 2': {}".format(count_trees(1, 2)))
print("Multiplied: {}".format(
    count_trees(1, 1) *
    count_trees(3, 1) *
    count_trees(5, 1) *
    count_trees(7, 1) *
    count_trees(1, 2)
))
