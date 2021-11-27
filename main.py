from parse_flatfile import parse_flatfile


def main():
    input = [
        ["data/testformat1_2015-06-28.txt", "specs/testformat1.csv"],
        ["not_exists_file", "specs/testformat1.csv"],
        ["data/testformat1_2015-06-28.txt", "not_exists_file"],
        ["not_exists_file", "another_not_exists_file"],
        ["data/testformat2_2015-06-28.txt", "specs/testformat2.csv"],
        ["data/testformat3_2015-06-28.txt", "specs/testformat3.csv"],
        ["data/testformat4_2015-06-28.txt", "specs/testformat4.csv"],
        ["data/testformat5_2015-06-28.txt", "specs/testformat5.csv"],
        ["data/testformat6_2015-06-28.txt", "specs/testformat6.csv"],
        ["data/testformat7_2015-06-28.txt", "specs/testformat7.csv"],
        ["data/testformat8_2015-06-28.txt", "specs/testformat8.csv"],
        ["data/testformat9_2015-06-28.txt", "specs/testformat9.csv"],
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
