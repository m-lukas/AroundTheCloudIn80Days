import csv
from typing import List, Set, Tuple


Region = str
GreenEnergyShare = float


def best_server_location(
    regions_to_consider: Set[Region], nuclear_is_green=False
) -> Tuple[List[Tuple[Region, GreenEnergyShare]], str]:
    "Calculate the region with the best available energy mix."

    ranking: List[Tuple[Region, GreenEnergyShare]] = []

    GREEN_ENERGY_SOURCES = [0, 8, 9, 11, 12, 13, 16, 17, 19, 20]
    if nuclear_is_green:
        GREEN_ENERGY_SOURCES.append(14)

    # calculate share of green energy for each region
    for region in regions_to_consider:
        data = data_of_region(region)
        timestamp = data[-1][1]
        latest_data = [to_int(b) for b in data[-1][2:]]
        total_energy = sum(latest_data)
        green_energy = sum(
            [a for idx, a in enumerate(latest_data) if idx in GREEN_ENERGY_SOURCES]
        )

        if total_energy == 0:
            ranking.append((region, 0))
        else:
            green_energy_share = green_energy / total_energy * 100
            ranking.append((region, green_energy_share))

    # sort the countries by the share of renewable energy
    sorted_ranking = sorted(ranking, key=lambda x: x[1], reverse=True)

    return (sorted_ranking, timestamp)


def data_of_region(region: Region) -> List[str]:
    data = []
    try:
        with open(f"data/{region}.csv", newline="") as file:
            reader = csv.reader(file)

            # skip column names
            reader.__next__()

            for row in reader:
                if "-" in row:
                    break
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Region '{region}' is not available")
        return [[0]]


def to_int(val: str) -> int:
    "Convert a 'str' to `int`. Returns `0` in case the conversion fails."
    try:
        return int(val)
    except ValueError:
        return 0
