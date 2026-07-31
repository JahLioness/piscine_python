def NULL_not_found(object: any) -> int:
    if (object is None):
        print(f"Nothing: None {type(object)}")
        return 0
    elif (type(object) is float and object is not object):  # NaN check
        print(f"Garlic: nan {type(object)}")
        return 0
    elif (type(object) is int and object == 0):
        print(f"Zero: 0 {type(object)}")
        return 0
    elif (type(object) is str and object == ""):
        print(f"Empty: {type(object)}")
        return 0
    elif (type(object) is bool and object is False):
        print(f"Fake: False {type(object)}")
        return 0
    else:
        print("Type not found")
        return 1

# def main():
#     Nothing = None
#     Garlic = float("NaN")
#     Zero = 0
#     Empty = ""
#     Fake = False
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))

# if __name__ == "__main__":
#     main()
