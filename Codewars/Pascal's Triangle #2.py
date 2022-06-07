def get_next_row(row):
    if len(row) == 0:
        return [1]

    result = [1]
    for i in range(len(row) - 1):
        result.append(row[i] + row[i + 1])
    result.append(1)

    return result

def pascal(p):
    result = []
    current_row = []
    for i in range(p):
        current_row = get_next_row(current_row)
        result.append(current_row)
    return result

