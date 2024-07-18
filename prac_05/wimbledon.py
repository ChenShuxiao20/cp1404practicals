# Wimbledon
"""
Wimbledon
Estimate: 20 minutes
Actual:   33 minutes
"""
import csv
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    record = load_record(FILENAME)
    champion_counts = count_champions(record)
    countries = get_countries(record)
    display_details(champion_counts, countries)

def load_record(FILENAME):
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        for row in reader:
            parts = row.strip().split(",")
            records.append(parts)
        return records

def count_champions(record):
    champion_counts = {}
    for entry in record:
        champion = entry[0]
        wins = int(entry[2])
        if champion in champion_counts:
            champion_counts[champion] += wins
        else:
            champion_counts[champion] = wins
    return champion_counts

def get_countries(record):
    countries = {entry[1] for entry in record}
    return sorted(countries)

def display_details(champion_counts, countries):
    print("Wimbledon Champions:")
    for champion, wins in champion_counts.items():
        print(f"{champion} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))

main()