def read_input_file(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data
