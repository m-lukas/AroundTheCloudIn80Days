import csv
from typing import List, Set


Region = str


def best_server_location(regions_to_consider: Set[Region]) -> List[Region]:
    "Calculate the region with the best available energy mix."

    ranking = []

    # calculate share of green energy for each region
    for region in regions_to_consider:
        data = data_of_region(region)
        latest_data = [to_int(b) for b in data[-1]]
        total_energy = sum(latest_data)
        green_energy = sum(
            [a for idx, a in enumerate(latest_data) if idx in GREEN_ENERGY_SOURCES]
        )

        ranking.append((region, green_energy / total_energy * 100))

    # sort the countries by the share of renewable energy
    sorted_ranking = sorted(ranking, key=lambda x: x[1], reverse=True)

    return sorted_ranking


GREEN_ENERGY_SOURCES: List[int] = [0, 8, 9, 11, 12, 13, 16, 17, 19, 20]


def data_of_region(region: Region) -> List[int]:
    data = []
    with open(f"data/{region}-2021-11-20.csv", newline="") as file:
        reader = csv.reader(file)

        # skip column names
        reader.__next__()

        for row in reader:
            if "-" in row:
                break
            data.append(row[2:])
    return data


def to_int(val: str) -> int:
    "Convert a 'str' to `int`. Returns `0` in case the conversion fails."
    try:
        return int(val)
    except ValueError:
        return 0
