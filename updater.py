import csv
from itertools import cycle
from time import sleep

REGIONS = [
    "AT",
    "BE",
    "CH",
    "DE",
    "DK",
    "ES",
    "FI",
    "FR",
    "IE",
    "IT",
    "NL",
    "NO",
    "PL",
    "SE",
    "UK",
]

if __name__ == "__main__":
    # simulate the 24 hours of the day
    for step in cycle(range(1, 25)):

        print(step)

        # update each region
        for region in REGIONS:
            with open(f"data/full/{region}.csv", newline="") as file:
                reader = csv.reader(file)

                # skip column names
                headline = reader.__next__()

                full_data = list(reader)

                # calculate number of rows
                step_size = len(full_data) / 24
                number_of_rows = int(step * step_size)

                data = full_data[:number_of_rows]

                # write data to file
                with open(f"data/{region}.csv", "w", newline="") as write_file:
                    writer = csv.writer(write_file)
                    writer.writerow(headline)
                    writer.writerows(data)

        # sleep for one conceptual hour
        sleep(2)
