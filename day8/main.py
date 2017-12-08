instructions = []

with open('input') as f:
    data = f.read().splitlines()
    for line in data:
        _line = line.split()
        instructions.append({_line[0]: {_line[1]: _line[2:]}})

_registers = list(set([list(i.keys())[0] for i in instructions]))
registers = dict(zip(_registers, [0] * len(_registers)))

max_inter = (None, 0)

for i in instructions:
    print('Instruction', i)
    for reg_name, reg_value in registers.items():
        try:
            _ = i[reg_name]
            print('Initial state of register {} -> {}'.format(reg_name, registers[reg_name]))
            print('Register instructions ', _)

            operator = list(_.keys())[0]
            print('Operator', operator)
            condition = _[str(operator)]
            print('Condition', condition)

            target_reg = condition[2]
            condition[2] = 'registers[\'{}\']'.format(target_reg)
            _to_eval = ' '.join(condition)
            to_eval = '{} else 0'.format(_to_eval)
            print(to_eval)
            x = eval(to_eval)
            if x != 0:
                if operator == 'inc':
                    registers[reg_name] += x
                if operator == 'dec':
                    registers[reg_name] -= x

            print('New state of register {} -> {}'.format(reg_name, registers[reg_name]))

            # Part 2
            if max_inter[1] < registers[reg_name]:
                max_inter = (reg_name, registers[reg_name])

            print('\n')
        except KeyError:
            pass

print('Part 1 ->', max(registers.values()))
print('Part 2 ->', max_inter)
