import matplotlib.pyplot as plt
from load_csv import load


def draw_life_expectancy(path: str) -> None:
    """Draw a line plot of life expectancy projections for France.
    Parameters:
        path (str):
            The file path to the CSV file containing life expectancy data.
    Returns:
        None
    """
    try:
        df = load(path)
        df = df[df["country"] == "France"]
        dy = df.columns[1:].astype(int)
        plt.figure(figsize=(8, 4))
        plt.plot(dy, df.iloc[0, 1:], marker="")
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    draw_life_expectancy("life_expectancy_years.csv")


if __name__ == "__main__":
    main()
