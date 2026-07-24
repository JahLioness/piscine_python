class calculator:
    def __init__(self):
        pass
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        if len(V1) != len(V2):
            print("Error: Vectors must be of the same length.")
            return
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors."""
        if len(V1) != len(V2):
            print("Error: Vectors must be of the same length.")
            return
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""
        if len(V1) != len(V2):
            print("Error: Vectors must be of the same length.")
            return
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")