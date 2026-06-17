from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys


def _population_to_float(value: object) -> float:
    """Convert a population value like '400k' or '3.28M' to a number."""
    text = str(value).strip()
    if text.endswith("M"):
        return float(text[:-1]) * 1_000_000
    if text.endswith("k"):
        return float(text[:-1]) * 1_000
    return float(text)


def draw_population(path: str, country: str) -> None:
    """Draw a line plot of population projections for France and a specified country.
    Parameters:
        path (str):
            The file path to the CSV file containing population data.
        country (str):
            The name of the country for which to display population projections.
    Returns:
        None
    """
    try:
        df = load(path)
        if country.capitalize() not in df["country"].values:
            print(f"Country '{country}' not found in the dataset.")
            return
        df2 = df[df["country"] == country.capitalize()]
        df = df[df["country"] == "France"]
        dy = df.columns[1:].astype(int)
        dy2 = df2.columns[1:].astype(int)
        france_population = [
            _population_to_float(value) for value in df.iloc[0, 1:]
        ]
        country_population = [
            _population_to_float(value) for value in df2.iloc[0, 1:]
        ]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(dy, france_population, label="France")
        ax.plot(dy2, country_population, label=country.capitalize())
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population (M)")
        ax.set_xlim(1800, 2050)
        ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=8))
        ax.yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda value, _: f"{value / 1_000_000:.1f}M")
        )
        ax.legend()
        fig.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    try:
        if not sys.argv or len(sys.argv) < 2:
            print("Usage: python aff_pop.py <country_name>")
            return
        country = sys.argv[1]
        if country.lower() == "france":
            print("Please specify a country other than France for comparison.")
            return
        elif country is None or country.strip() == "":
            print("Country name cannot be empty.")
            return
        draw_population("population_total.csv", country)
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    main()