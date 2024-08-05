num: int = int(input("Enter number: "))
def base_n_repr(number:int) -> dict[str, str, str]:
    d = {}
    d["bin"] = bin(number)
    d["oct"] = oct(number)
    d["hex"] = hex(number)
    return d
print(base_n_repr(num))