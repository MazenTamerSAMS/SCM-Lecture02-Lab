from src.inventory import stock_is_valid


def main():
    checks = [
        (10, True, "positive stock is valid"),
        (0, True, "zero stock is valid"),
        (-1, False, "negative stock must be rejected"),
    ]
    failed = 0
    for value, expected, label in checks:
        actual = stock_is_valid(value)
        if actual == expected:
            print(f"PASS: {label}")
        else:
            print(f"FAIL: {label} (expected {expected}, got {actual})")
            failed += 1
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
