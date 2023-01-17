# Christian Znidarsic
# Computer Organization
# 2/18/22
# This program takes a list of machine code instructions, and converts them to MIPS assembly language instructions

from typing import List

# list of instructions
instructions: List[str] = ["10101111101111110000000000010100",
                           "10101111101001000000000000100000",
                           "10101111101001010000000000100100",
                           "00000011000011111100100000100001",
                           "00000011000011111100100000100001",
                           "10101111101110010000000000011000",
                           "10001111101001010000000000011000",
                           "00001100000000000001001011001100",
                           "00100100100001000000010000110000",
                           "10001111101111110000000000010100",
                           "00100111101111010000000000100000",
                           "00000011111000000000000000001000",
                           "00000001101011100101100000100100",
                           "10001101010010010000000000001000",
                           "00001000000000010010001101000101",
                           "00000010101010010101100000100010",
                           "00110101111100001011111011101111",
                           "00000010110011010101000000100000"]

# dictionary of opcode types
op_code_types = {'000000': 'R-type',
            '001001': 'I-type',
            '001100': 'I-type',
            '000010': 'J-type',
            '000011': 'J-type',
            '100011': 'I-type',
            '001101': 'I-type',
            '101011': 'I-type'}

# dictionary of opcode names
op_codes = {'001001': 'addiu',
            '001100': 'andi',
            '000010': 'j',
            '000011': 'jal',
            '100011': 'lw',
            '001101': 'ori',
            '101011': 'sw'}

# dictionary of function codes
func_codes = {'100000': 'add',
              '100001': 'addu',
              '100100': 'and',
              '001000': 'jr',
              '011000': 'mult',
              '100101': 'or',
              '100010': 'sub'}

# dictionary of registers
registers = {'00000': '$zero',
             '00001': '$at',
             '00010': '$v0',
             '00011': '$v1',
             '00100': '$a0',
             '00101': '$a1',
             '00110': '$a2',
             '00111': '$a3',
             '01000': '$t0',
             '01001': '$t1',
             '01010': '$t2',
             '01011': '$t3',
             '01100': '$t4',
             '01101': '$t5',
             '01110': '$t6',
             '01111': '$t7',
             '10000': '$s0',
             '10001': '$s1',
             '10010': '$s2',
             '10011': '$s3',
             '10100': '$s4',
             '10101': '$s5',
             '10110': '$s6',
             '10111': '$s7',
             '11000': '$t8',
             '11001': '$t9',
             '11010': '$k0',
             '11011': '$k1',
             '11100': '$gp',
             '11101': '$sp',
             '11110': '$fp',
             '11111': '$ra'}

# This function takes a single machine code instruction (word) as input, and prints the decoded MIPS assembly
# instruction as output.
def disassembler(word):
    # get the first 6 bits (opcode) of the first instruction (index 0)
    opcode = word[0:6]
    # look up the opcode in the op_code_types dictionary to determine opcode type
    opcodeType = op_code_types[opcode]

    # get the instruction format
    if (opcodeType == 'R-type'):
        # get the 6-bit function code using string slicing
        func_code = word[26:32]

        # get the 5 bit RS register
        rs = word[6:11]

        # get the 5 bit RT register
        rt = word[11:16]

        # get the 5 bit RD register
        rd = word[16:21]

        # print the instruction with the operands
        print(func_codes[func_code] + " " + registers[rd] + ", " + registers[rs] + ", " + registers[rt])

    elif (opcodeType == 'I-type'):
        # get the 5 bit RS register
        rs = word[6:11]

        # get the 5 bit RT register
        rt = word[11:16]

        # get the 5 bit RD register
        immediate = word[16:32]

        # print the instruction with the operands
        print(op_codes[opcode] + " " + registers[rt] + ", " + registers[rs] + " " + hex(int(immediate, 2)))

    elif (opcodeType == 'J-type'):
        # get the 5 bit RD register
        address = word[6:32]

        # print the instruction with the operands
        print(op_codes[opcode] + " " + hex(int(address, 2)))
        return 0

    else:
        print("error, unknown opcode type")


# iterate across all inputs in the instructions list
for x in range(0, len(instructions)):
    disassembler(instructions[x])