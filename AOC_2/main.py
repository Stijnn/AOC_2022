def main(input):
    print(input)
    return 0


if __name__ == '__main__':
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('./input.txt', 'r') as input_file:
        exit(main(input=[l.strip() for l in input_file.readlines()]))