class AssemblerInterpreter:
    def __init__(self, program):
        self.program = program
        self.result = {}

    def mov(self, variable, value):
        if value.isdigit():
            real_value = int(value)
        else:
            real_value = self.result[value]

        self.result[variable] = real_value

    def inc(self, variable):
        self.result[variable] += 1

    def dec(self, variable):
        self.result[variable] -= 1

    @staticmethod
    def get_args(command_line):
        args = command_line.split()[1:]
        if len(args) == 2:
            return args
        return args[0], None

    def run_command_line(self, command_index, variable, value=None):
        command = self.program[command_index].split()[0]

        if command == 'mov':
            self.mov(variable, value)
        elif command == 'inc':
            self.inc(variable)
        elif command == 'dec':
            self.dec(variable)
        elif command == 'jnz':
            if self.result[variable] != 0:
                new_command_index = command_index + int(value)
                print('JNZ:',self.program[new_command_index].split()[0], variable, value)
                self.run_command_line(new_command_index, variable, value)

        print(self.result)

    def run_commands(self):
        self.result = {}

        for index in range(len(self.program)):
            variable, value = self.get_args(self.program[index])
            self.run_command_line(command_index=index, variable=variable, value=value)

        return self.result



code = '''mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''

program = ['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']
assembler_interpreter = AssemblerInterpreter(code.splitlines())
print(assembler_interpreter.run_commands())
