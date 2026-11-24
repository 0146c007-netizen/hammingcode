# hamming-code
data = input("Enter 4-bit binary data: ").strip()

if len(data) != 4 or any(bit not in "01" for bit in data):
    print("Error: Please enter exactly 4 binary bits (0 or 1).")
else:
    m = len(data)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    print("\nNumber of redundant bits:", r)

    d1, d2, d3, d4 = map(int, data)

    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4

    hamming_code = [p1, p2, d1, p4, d2, d3, d4]
    print("Original data:", data)
    print("Generated (7,4) Hamming code:", "".join(map(str, hamming_code)))

    received = hamming_code.copy()
    while True:
        try:
            err_pos = int(input("\nEnter error position to simulate (1-7, or 0 for no error): "))
            if 0 <= err_pos <= 7:
                break
            else:
                print("Invalid input. Please enter a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if err_pos != 0:
        received[err_pos - 1] ^= 1

    print("Received data:", "".join(map(str, received)))

    s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
    s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
    s4 = received[3] ^ received[4] ^ received[5] ^ received[6]

    error_location = s1 + (2 * s2) + (4 * s4)

    if error_location == 0:
        print("\nResult: No error detected.")
    else:
        print(f"\nResult: Error detected at position {error_location}!")
        received[error_location - 1] ^= 1
        print("Error corrected successfully!")

    corrected_str = "".join(map(str, received))
    print("Corrected Hamming code:", corrected_str)

    recovered_data = [received[2], received[4], received[5], received[6]]
    print("Recovered original data:", "".join(map(str, recovered_data)))
    print("\nProgram finished.")

