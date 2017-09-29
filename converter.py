
def load_input_sentences(file_path: str) -> list:
    result = []
    with open(file_path) as file:
        for line in file.readlines():
            result.append(line[:-1])
    return result


def save_output(file_path: str, output: list) -> None:
    with open(file_path, 'w') as file:
        for item in output:
            file.write('{}\n'.format(item))


s = load_input_sentences('output.txt')

r = []
for x in s:
    r.append('{}\t1.0'.format(x))

save_output('output.txt', r)
