import csv

TARGET_FILE = "target_positions.csv"


def display_targets() -> None:
    try:
        with open(TARGET_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No target position data found.")
                return

            print("\nTARGET POSITION DATA")
            print("-" * 40)

            for row in rows:
                print(" | ".join(row))

    except FileNotFoundError:
        print("Target position file not found.")
    except OSError as error:
        print(f"Error reading target position data: {error}")


if __name__ == "__main__":
    display_targets()
