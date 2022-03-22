def file_to_list(filepath):
    with open(filepath, "r") as f:
        data = [int(line.strip("\n")) for line in f.readlines()]

    return data
