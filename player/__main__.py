import argparse


def load(filepath):
    """Loads data from filepath database"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line.strip())
    except FileNotFoundError as e:
        print(f"{e}")


def main():

    parser = argparse.ArgumentParser(
        description="Player rewards CLI",
        epilog="Comentário/evento final"
    )

    parser.add_argument(
        "subcommand",
        type=str,
        help="Comando help do parser",
        choices=("load", "show","send")
    )

    parser.add_argument(
        "filepath",
        type=str,
        help="Comando Help do parser"
    )

    args = parser.parse_args()

    globals()[args.subcommand](args.filepath)


if __name__ == "__main__":
    main()
