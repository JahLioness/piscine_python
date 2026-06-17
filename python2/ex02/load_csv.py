import pandas


def load(path: str) -> pandas.DataFrame:
    """Load a CSV file into a pandas DataFrame.
    Parameters:
        path (str): The file path to the CSV file.
    Returns:
        pandas.DataFrame: The loaded DataFrame.
    """
    try:
        if path is None:
            raise ValueError("Path cannot be None")
        df = pandas.read_csv(path)
        print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except Exception as e:
        raise Exception(f"An error occurred while loading the CSV file: {e}")
