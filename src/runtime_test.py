import time
import subprocess


def get_lengths(filename):
    # Open input file
    file = open(filename, "r")

    # Store cleaned lines
    lines = []
    for line in file:
        stripped = line.strip()
        if stripped != "":
            lines.append(stripped)

    # Close input file
    file.close()

    k = int(lines[0])
    a = lines[k + 1]
    b = lines[k + 2]

    return len(a), len(b)


def main():
    # List test files
    files = [
        "test1.in",
        "test2.in",
        "test3.in",
        "test4.in",
        "test5.in",
        "test6.in",
        "test7.in",
        "test8.in",
        "test9.in",
        "test10.in",
    ]

    runs = 1000

    # Open output file
    output_file = open("data/runtime_results.csv", "w")
    output_file.write("file,len_a,len_b,time_seconds\n")

    for file_name in files:
        full_path = "tests/" + file_name
        len_a, len_b = get_lengths(full_path)

        # Start timer
        start = time.time()

        for _ in range(runs):
            subprocess.run(
                ["python3", "src/hvlcs.py", full_path],
                stdout=subprocess.DEVNULL,
            )

        # Stop timer
        end = time.time()
        total_time = end - start

        output_file.write(
            file_name
            + ","
            + str(len_a)
            + ","
            + str(len_b)
            + ","
            + str(total_time)
            + "\n"
        )

        print(file_name, len_a, len_b, total_time)

    # Close output file
    output_file.close()


if __name__ == "__main__":
    main()
