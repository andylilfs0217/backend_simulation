from parse_flatfile import parse_flatfile


def main():
    input = [
        ["data/testformat7_2015-06-28.txt", "specs/testformat7.csv"],
    ]
    for idx, files in enumerate(input):
        try:
            print(f'Testing Case {idx}')
            output = parse_flatfile(files[0], files[1])
            print(output)
        except BaseException as err:
            print(err)


if __name__ == '__main__':
    main()
