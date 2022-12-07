from utils.api import get_input


def create_dir(root_dir, parent_dir, name):
    return {"name": name, "..": parent_dir, "/": root_dir}


def find_directory_size_recursive(dir: dict):
    directory_sizes = []
    size_of_this_dir = 0
    for entry_name in set(dir.keys()) - set(["..", "/", "name"]):
        if type(dir[entry_name]) is dict:
            sizes_from_sub_directory = find_directory_size_recursive(dir[entry_name])
            size_of_this_dir += sizes_from_sub_directory[0]
            directory_sizes.extend(sizes_from_sub_directory)
        else:
            size_of_this_dir += dir[entry_name]

    directory_sizes.insert(0, size_of_this_dir)
    return directory_sizes


def print_directory_structure(dir: dict, padding: str):
    for entry_name in set(dir.keys()) - set(["..", "/", "name"]):
        if type(dir[entry_name]) is dict:
            print(f'{padding}|{dir[entry_name]["name"]}')
            print(f"{padding}---|")
            print_directory_structure(dir[entry_name], f"{padding}|  ")
        else:
            print(f"{padding}|{entry_name}: {dir[entry_name]}")


input_str = get_input(7)

root_dir = {"name": "/"}
root_dir[".."] = root_dir
root_dir["/"] = root_dir
current_dir = root_dir
for line in input_str.rstrip().split("\n"):
    components = line.strip().split(" ")

    if components[0] == "$":
        if components[1] == "cd":
            current_dir = current_dir[components[2]]
    else:
        if components[0] == "dir":
            current_dir[components[1]] = create_dir(
                root_dir, current_dir, components[1]
            )
        else:
            current_dir[components[1]] = int(components[0])


directory_sizes = find_directory_size_recursive(root_dir)

sum_of_dirs_part_1 = sum(filter(lambda size: size <= 100000, directory_sizes))

print(f"Solution part 1: {sum_of_dirs_part_1}")

needed_size_to_delete = 30000000 - (70000000 - directory_sizes[0])

size_of_file_to_delete = min(
    filter(lambda size: size >= needed_size_to_delete, directory_sizes)
)

print(f"Solution part 2: {size_of_file_to_delete}")
