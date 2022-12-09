from utils.api import get_input


def find_visibility_on_row_of_trees(row: list):
    highest_tree = row[0]
    tree_visibility = []
    for tree in row[1: -1]:
        tree_visibility.append((tree - highest_tree) > 0)
        highest_tree = max(tree, highest_tree)

    highest_tree = row[-1]
    tree_visibility_reversed = []
    for tree in row[::-1][1: -1]:
        tree_visibility_reversed.append((tree - highest_tree) > 0)
        highest_tree = max(tree, highest_tree)

    return [
        forwards or backwards
        for (forwards, backwards)
        in zip(tree_visibility, tree_visibility_reversed[::-1])
    ]


def find_amount_of_visible_trees_for_each_tree_in_row(row: list):
    highest_tree_index = {row[0]: 0}
    tree_score = []
    for tree, index in zip(row[1: -1], range(1, len(row)-1)):
        tree_score.append(
            index - max([
                value
                for _, value
                in filter(
                    lambda entry: entry[0] >= tree,
                    highest_tree_index.items()
                )
            ], default=0)
        )
        highest_tree_index[tree] = index

    highest_tree_index = {row[-1]: 0}
    tree_score_reversed = []
    for tree, index in zip(row[1: -1][::-1], range(1, len(row)-1)):
        tree_score_reversed.append(
            index - max([
                value
                for _, value
                in filter(
                    lambda entry: entry[0] >= tree,
                    highest_tree_index.items()
                )
            ], default=0)
        )
        highest_tree_index[tree] = index

    return [forwards * backwards for forwards, backwards in zip(tree_score, tree_score_reversed[::-1])]


input_str = get_input(8)

tree_grid = [
    [int(height) for height in row.rstrip()]
    for row
    in input_str.rstrip().split()
]

visibility_rows = [
    find_visibility_on_row_of_trees(row)
    for row
    in tree_grid[1: -1]
]
visibility_columns = [
    find_visibility_on_row_of_trees(column)
    for column
    in list(zip(*tree_grid))[1: -1]
]

visible_trees = len(list(filter(
    lambda row_and_column: row_and_column[0] or row_and_column[1],
    zip(
        [tree for row in visibility_rows for tree in row],
        [tree for column in zip(*visibility_columns) for tree in column]
    )
)))

visible_trees += len(tree_grid) * 4 - 4

print(f'Solution part 1: {visible_trees}')

visibility_amount_rows = [
    find_amount_of_visible_trees_for_each_tree_in_row(row)
    for row
    in tree_grid[1: -1]
]

visibility_amount_columns = [
    find_amount_of_visible_trees_for_each_tree_in_row(column)
    for column
    in list(zip(*tree_grid))[1: -1]
]

tree_with_best_visibility = max([
    row * column
    for row, column
    in zip(
        [tree for row in visibility_amount_rows for tree in row],
        [tree for column in zip(*visibility_amount_columns) for tree in column]
    )
])

print(f'Solution part 2: {tree_with_best_visibility}')
