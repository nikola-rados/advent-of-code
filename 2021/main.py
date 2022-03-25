import click
from day1.day1 import run_challenges as run_day1
from day2.day2 import run_challenges as run_day2


@click.command()
@click.option("-d", "--day", type=int, required=True, help="Day to run")
@click.option("-f", "--datapath", type=str, help="Path to data")
def main(day: int, datapath: str):
    print(f"Day {day}")
    print(f"Data used: {datapath}\n")

    if day == 1:
        run_day1(datapath)

    elif day == 2:
        run_day2(datapath)

    elif day == 3:
        print("Coming soon!")


if __name__ == "__main__":
    main()
