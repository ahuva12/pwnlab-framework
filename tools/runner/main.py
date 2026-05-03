from lab import Lab


if __name__ == "__main__":
    lab = Lab()

    result = lab.run_challenge("overflow", "AAAAAAA\n")

    print("=== STDOUT ===")
    print(result.get("stdout"))

    print("=== STDERR ===")
    print(result.get("stderr"))