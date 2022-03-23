def file_to_list(datapath):
    with open(datapath, "r") as f:
        data = [int(line.strip("\n")) for line in f.readlines()]

    return data
