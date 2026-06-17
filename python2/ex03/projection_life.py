import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def format_thousands(value, _position):
    if value >= 1000:
        return f"{value / 1000:g}k"
    return f"{value:g}"


def draw_gnp_life_projection(path_life: str, path_gnp: str) -> None:
    """Draw points plot of GNP per capita and life expectancy projections for all countries register for the year 1900.
    Parameters:
        path_life (str):
            The file path to the CSV file containing life expectancy data.
        path_gnp (str):
            The file path to the CSV file containing GNP data.
    Returns:
        None
    """
    try:
        df_life = load(path_life)
        df_gnp = load(path_gnp)
        life_expectancy = df_life["1900"].tolist()
        gnp_per_capita = df_gnp["1900"].tolist()
        plt.figure(figsize=(10, 6))
        plt.scatter(gnp_per_capita, life_expectancy)
        plt.xscale("log")
        plt.gca().xaxis.set_major_formatter(FuncFormatter(format_thousands))
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy (years)")
        plt.title("GNP per Capita vs Life Expectancy (1900)")
        # plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    try:
        draw_gnp_life_projection("life_expectancy_years.csv", "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()
