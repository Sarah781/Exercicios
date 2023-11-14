code, quantity = [int(x) for x in input().split()]

if code == 1:
    print(f"Total: R$ {4.00 * quantity:.2f}")
elif code == 2:
    print(f"Total: R$ {4.50 * quantity:.2f}")
elif code == 3:
    print(f"Total: R$ {5.00 * quantity:.2f}")
elif code == 4:
    print(f"Total: R$ {2.00 * quantity:.2f}")
elif code == 5:
    print(f"Total: R$ {1.50 * quantity:.2f}")


