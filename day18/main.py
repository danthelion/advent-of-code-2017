LAST_FREQ = None
i = 0

with open('input') as f:
    instructions = [line.strip() for line in f.readlines()]

_registers = set([x.split(' ')[1] for x in instructions if x.split(' ')[1] != '1'])
registers = {x: 0 for x in _registers}

while True:
    print(registers)
    _ = instructions[i].split(' ')
    operation = _[0]
    target = _[1]
    print('Operation:', operation)
    try:
        target = int(target)
    except ValueError:
        pass
    print('Target:', target)
    if len(_) == 3:
        try:
            value = int(_[2])
        except ValueError:
            value = _[2]
        print('Value:', value)

    print('\n')

    if operation == 'set':
        if type(value) == int:
            registers[target] = value
        elif type(value) == str:
            registers[target] = registers[value]
        i += 1
    if operation == 'snd':
        LAST_FREQ = registers[target]
        print('PLAYING NOTE:', LAST_FREQ)
        i += 1
    if operation == 'add':
        if type(value) == int:
            registers[target] += value
        elif type(value) == str:
            registers[target] += registers[value]
        i += 1
    if operation == 'mul':
        registers[target] *= value
        i += 1
    if operation == 'mod':
        if type(value) == int:
            rem = registers[target] % value
        elif type(value) == str:
            rem = registers[target] % registers[value]
        registers[target] = rem
        i += 1
    if operation == 'rcv':
        if LAST_FREQ != 0:
            print('LAST PLAYED FREQ', LAST_FREQ)
        i += 1
    if operation == 'jgz':
        print(type(target), type(value))
        if type(target) == int:
            if target > 0:
                i += value
            else:
                i += 1
        elif type(target) == str:
            if registers[target] > 0:
                i += value
            else:
                i += 1
