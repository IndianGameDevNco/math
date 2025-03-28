def kaprekar(k):
    # Ensure k is a 4-digit number by padding with leading zeros if necessary
    k = f"{k:04d}"
    a = int(''.join(sorted(k, reverse=True)))
    b = int(''.join(sorted(k)))
    return a - b

for i in range(1111, 10000):
    # Skip numbers with all identical digits
    if len(set(str(i))) < 2:
        continue

    count = 0
    while i != 6174:
        i = kaprekar(i)
        count += 1

    print(f"Reached 6174 for starting number {i} in {count} iterations.")