from similarity import similarity


def get_similarity(sentence1: str, sentence2: str) -> float:
    return similarity(sentence1, sentence2, True)


def load_input_sentences(file_path: str) -> list:
    result = []
    with open(file_path) as file:
        for line in file.readlines():
            result.append(line.split('\t'))
    return result


def save_output(file_path: str, output: list) -> None:
    with open(file_path, 'w') as file:
        for item in output:
            file.write('{}\t1.0\n'.format(item))


def normalize(number: float) -> float:
    return number * 5


def main() -> None:
    similarities = []
    input_sentences = load_input_sentences('data/STS.input.headlines.txt')
    length = len(input_sentences)
    for index, sentences in enumerate(input_sentences, 1):
        print('[{}/{}] Calc similarity for: {} ----- {}'.format(index, length, sentences[0], sentences[1], flush=True))
        sim = normalize(get_similarity(sentences[0], sentences[1]))
        print('Similarity: {:06.4f}'.format(sim))
        similarities.append('{:06.4f}'.format(sim))
    save_output('output.txt', similarities)


if __name__ == '__main__':
    main()
