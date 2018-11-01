
import utils
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

    # act
    actual = utils.compile_instructions(instructions)

    # assert
    expected = ['100', '101', '102', '103', '104', '105', '106', '107', '108', '109']
    assert actual == expected


def test_givenUnknownOpcodes_whenCompiling_thenFunctionShouldRaise():
    # arrange
    instructions = ['NOPe R0, R1']

    # act & assert
    with pytest.raises(utils.CompilationException) as ce:
        utils.compile_instructions(instructions)


def test_givenLowerCaseCode_whenCompiling_thenFunctionShouldStillProduceCorrectOutput():
    # arrange
    instructions = ['NoP r0, R1']

    # act
    actual = utils.compile_instructions(instructions)

    # assert
    expected = ['100']
    assert actual == expected


def test_givenRegisterPC_whenCompiling_thenFunctionShouldTranslateToR0():
    # arrange
    instructions = ['NOP PC, R1']

    # act
    actual = utils.compile_instructions(instructions)

    # assert
    expected = ['100']
    assert actual == expected

def test_givenPCAsSecondRegister_whenCompiling_thenCompilerShouldTruncateImmValue():
    # arange
    instruction = ['LD R1, PC #0']

    # act
    actual = utils.compile_instructions(instruction)

    # assert
    expected = ['408']
    assert actual == expected