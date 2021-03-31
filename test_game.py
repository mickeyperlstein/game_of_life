import pytest
import main as game

expected_board = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0]]

board = [

    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]


@pytest.mark.parametrize(
    'board, expecteed_board', [
        (board, expected_board)]

)
def test_game(board, expecteed_board):
    actual = game.next_state(board)

    for r in range(len(actual)):
        for c in range(len(actual[0])):
            assert actual[r][c] == expected_board[r][c]

