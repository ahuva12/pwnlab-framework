from lab import Lab

if __name__ == "__main__":
    lab = Lab()
    
    tests = [
        ("overflow", "AAAAAAA\n"),
        ("uaf", "bob\n"),
        ("fmt", "hi!\n"),
    ]

    results = {}

    for name, input_data in tests:
        results[name+" without ASLR"] = lab.run_challenge(name, input_data, False)
        results[name +" with ASLR"] = lab.run_challenge(name, input_data, True)

    for name, result in results.items():
        print(f"\n=== {name.upper()} ===")
        print("STDOUT:")
        print(result.get("stdout"))
        print("STDERR:")
        print(result.get("stderr"))