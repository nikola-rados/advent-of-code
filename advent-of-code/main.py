import click
from day1 import day1_challenge


@click.command()
@click.option("-d", "--day", type=int, required=True, help="Day target")
@click.option("-f", "--filepath", type=str, help="Data path target")
def main(day, filepath):
    print(f"Day entry: {day}")
    print(f"Filepath entry: {filepath}")

    if day == 1:
        day1_challenge(filepath)


if __name__ == "__main__":
    main()
