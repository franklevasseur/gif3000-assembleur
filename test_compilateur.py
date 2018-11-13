from utils.Program import Program
from utils.CompilationException import CompilationException
import pytest


def test_givenStandardOpcodes_whenCompiling_thenOpcodesAreCorrectlyTranslated():
    # arrange
    instructions = ['NOP R0, R1',
                    'ADD R0, R1',
                    'SUB R0, R1',
                    'MUL R0, R1',
                    'AND R0, R1',
                    'MOV R0, R1',
                    'SHR R0, R1',
                    'SHL R0, R1',
                    'LD R0, R1',
                    'SD R0, R1']
    program = Program(instructions)

    # act
    actual = program.compile()

    # assert
    expected = ['100', '101', '102', '103', '104', '105', '106', '107', '108', '109']
    assert actual == expected


def test_givenUnknownOpcodes_whenCompiling_thenFunctionShouldThrow():
    # arrange
    instructions = ['NOPe R0, R1']
    program = Program(instructions)

    # act & assert
    with pytest.raises(CompilationException) as ce:
        program.compile()


def test_givenLowerCaseCode_whenCompiling_thenFunctionShouldStillProduceCorrectOutput():
    # arrange
    instructions = ['NoP r0, R1']
    program = Program(instructions)

    # act
    actual = program.compile()

    # assert
    expected = ['100']
    assert actual == expected


def test_givenRegisterPC_whenCompiling_thenFunctionShouldTranslateToR0():
    # arrange
    instructions = ['NOP PC, R1']
    program = Program(instructions)

    # act
    actual = program.compile()

    # assert
    expected = ['100']
    assert actual == expected

def test_givenPCAsSecondRegister_whenCompiling_thenCompilerShouldTruncateImmValue():
    # arange
    instruction = ['LD R1, PC #0']
    program = Program(instruction)

    # act
    actual = program.compile()

    # assert
    expected = ['408']
    assert actual == expected


def test_givenEmptyLines_whenCreatingProgram_thenShouldRemoveEmptyLines():
    # arange
    instruction = ['NOP R1, R1',
                   '',
                   'NOP R1, R1']

    # act
    program = Program(instruction)
    actual = program.compile()

    # assert
    expected = ['500', '500']
    assert actual == expected


def test_givenComments_whenCompiling_thenCommentsShouldBeRemoved():
    # arange
    instructions = ['SD R1, R2 #2 // this is a in-line comment',
                   '// this is full line comment',
                   'NOP R1, R1',
                    '// this in another comment']

    # act
    program = Program(instructions)
    actual = program.compile()

    # assert
    expected = ['629', '500']
    assert actual == expected


def test_givenFlagUpdateInstruction_whenCompiling_thenCorrespondingBitShouldBeSet():
    # arange
    instruction = ['ADD R1, R2 -f']

    # act
    program = Program(instruction)
    actual = program.compile()

    # assert
    expected = ['681']
    assert actual == expected


def test_givenConditionnalInstruction_whenCompiling_thenCorrespondingBitsShouldBeSet():
    # arange
    instruction = ['ADDZ R1, R2',
                   'MOVNZ R1, R2',
                   'SUBC R1, R2',
                   'MULNC R1, R2']

    # act
    program = Program(instruction)
    actual = program.compile()

    # assert
    expected = ['641', '655', '662', '673']
    assert actual == expected


def test_givenImmediateValueAndOpcodeIsNotLdOrSd_whenCompiling_thenShouldThrow():
    # arrange
    instructions = ['ADD R1, R1 #15']
    program = Program(instructions)

    # act & assert
    with pytest.raises(CompilationException) as ce:
        program.compile()


def test_givenFlagUpdateAndOpcodeIsLdOrSd_whenCompiling_thenShouldThrow():
    # arrange
    instructions = ['LD R1, R1 #15 -f']
    program = Program(instructions)

    # act & assert
    with pytest.raises(CompilationException) as ce:
        program.compile()


def test_givenConditionAndOpcodeIsLdOrSd_whenCompiling_thenShouldThrow():
    # arrange
    instructions = ['ADD R1, R1 #15']
    program = Program(instructions)

    # act & assert
    with pytest.raises(CompilationException) as ce:
        program.compile()


def test_givenConditionAndUpdateFlag_whenCompiling_thenMiddleNibbleShouldBeExpectedOne():
    # arange
    instruction = ['ADDZ R1, R2 -f',
                   'MOVNZ R1, R2 -f',
                   'SUBC R1, R2 -f',
                   'MULNC R1, R2 -f']

    # act
    program = Program(instruction)
    actual = program.compile()

    # assert
    expected = ['6C1', '6D5', '6E2', '6F3']
    assert actual == expected
