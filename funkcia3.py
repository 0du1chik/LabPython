def funkcia2(p: int) -> int:
    a, b = 0, 1
    while b <= p:
        a, b = b, a + b
    return b