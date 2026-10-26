#!/usr/bin/env python3
"""Independent exact audit of the all-index characterization of A195608."""
from pathlib import Path

LIMIT = 1_000_000


def member(n):
    if n < 1:
        return False
    k = n // 2
    return (k.bit_count() % 2 == 0 and
            (n % 2 == 1 or (k - 1).bit_count() % 2 == 0))


def main():
    # Direct definition: neither the evil-number formula nor the membership
    # criterion is used to build this list or the summatory identity.
    evil = [x for x in range(2 * LIMIT + 2) if x.bit_count() % 2 == 0]
    assert len(evil) >= LIMIT + 1
    selected = []
    total = 0
    for n in range(1, LIMIT + 1):
        total += evil[n - 1]
        original = 4 * total == evil[n - 1] * evil[n]
        assert member(n) == original, (n, original)
        if original:
            selected.append(n)
    print(f"PASS original summatory identity and criterion for n=1..{LIMIT}")

    # Independent construction of the Thue-Morse word by its substitution.
    word = bytearray([0])
    while len(word) <= LIMIT // 2:
        word = bytearray(bit for b in word for bit in (b, 1 - b))
    via_word = [n for n in range(1, LIMIT + 1)
                if word[n // 2] == 0 and (n % 2 or word[n // 2 - 1] == 0)]
    assert via_word == selected
    print("PASS independent binary substitution generates the same full set")

    published_path = Path(__file__).with_name("b195608-published.txt")
    published = []
    for line in published_path.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            j, value = map(int, line.split())
            assert j == len(published) + 1
            published.append(value)
    assert len(published) == 10_000
    assert selected[:len(published)] == published
    print(f"PASS all {len(published)} saved published b-file terms")

    gaps = {y - x for x, y in zip(selected, selected[1:])}
    assert gaps == {1, 4, 6}
    blocks = []
    for n in selected:
        if blocks and n == blocks[-1][-1] + 1:
            blocks[-1].append(n)
        else:
            blocks.append([n])
    for block in blocks:
        if block[-1] == LIMIT:  # a final truncated block is not complete
            continue
        assert len(block) in (1, 3), block
        m = block[0]
        if m > 1:
            assert evil[m] - evil[m - 2] == 5, (m, block)
    assert blocks[0] == [1]
    print("PASS gaps {1,4,6}, complete blocks of size 1 or 3, and all defined block-start identities")
    print(f"PASS {len(selected)} members found; first terms: {selected[:20]}")


if __name__ == "__main__":
    main()
