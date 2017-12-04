def is_passphrase_valid(pp):
    if len(pp) == len(set(pp)):
        return 1
    else:
        return 0


with open('input') as f:
    passphrases = [line.rstrip().split(' ') for line in f.readlines()]

# 1
print(sum([is_passphrase_valid(passphrase) for passphrase in passphrases]))

# 2
print(sum([is_passphrase_valid([''.join(sorted(w)) for w in passphrase]) for passphrase in passphrases]))
