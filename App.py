def load(path):
    input_file = open(path, mode="r", encoding="utf-8")
    lines = input_file.read().splitlines()
    parsed_input = {
        'lon': float(lines[0].replace(',', '.')),
        'lat': float(lines[1].replace(',', '.')),
        'n': int(lines[2])
    }
    for index, line in enumerate(lines[3:]):
        parsed_input[index+1] = line
    input_file.close()
    return parsed_input
