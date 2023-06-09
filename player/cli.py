import argparse
from player.core import load

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

    print(globals()[args.subcommand](args.filepath))
