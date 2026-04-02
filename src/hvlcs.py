import sys


def read_input(filename):
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

    # Read alphabet size
    k = int(lines[0])
    values = {}

    # Read character values
    index = 1
    for _ in range(k):
        parts = lines[index].split()
        char = parts[0]
        value = parts[1]
        values[char] = int(value)
        index += 1

    # Read both strings
    a = lines[index]
    b = lines[index + 1]

    return values, a, b


def compute_max_value(values, a, b):
    n = len(a)
    m = len(b)

    # Build DP table
    dp = []
    for _ in range(n + 1):
        row = []
        for _ in range(m + 1):
            row.append(0)
        dp.append(row)

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                take = dp[i - 1][j - 1] + values[a[i - 1]]
                skip_a = dp[i - 1][j]
                skip_b = dp[i][j - 1]
                dp[i][j] = max(take, skip_a, skip_b)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return DP table
    return dp


def reconstruct_subsequence(dp, values, a, b):
    # Start from end
    i = len(a)
    j = len(b)
    result = []

    # Backtrack solution path
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            match_value = dp[i - 1][j - 1] + values[a[i - 1]]
            if dp[i][j] == match_value:
                result.append(a[i - 1])
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    # Reverse answer list
    result.reverse()
    return "".join(result)


def main():
    # Check input arguments
    if len(sys.argv) != 2:
        print("Usage: python3 src/hvlcs.py <input_file>")
        return

    input_file = sys.argv[1]
    values, a, b = read_input(input_file)

    dp = compute_max_value(values, a, b)
    subsequence = reconstruct_subsequence(dp, values, a, b)

    # Print final answer
    print(dp[len(a)][len(b)])
    print(subsequence)


if __name__ == "__main__":
    main()
