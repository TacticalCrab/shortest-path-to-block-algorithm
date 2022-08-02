from random import choice

def generate_sample_data(amount: int, places: list):
    result = []
    for _ in range(amount):
        result.append({name: choice([True, False]) for name in places})
    return result

# Sample data
_template = {
    "office": True,
    "gym": True,
    "store": True
}

if __name__ == '__main__':
    print(*generate_sample_data(5, ["office", "gym", "store"]), sep="\n")