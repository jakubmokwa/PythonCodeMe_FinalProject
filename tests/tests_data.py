test_values_int = [
    [3, 2, 1, 5, 7, 1, 2, 3, 5, 5],
    [100, 200, 12353, 53, 324, 32423, 432, 2346],
    [213, 213, 5, 525, 525, 6, 25, 25, 112, 52, 785]

]
test_correct_values_int = [
    [1, 1, 2, 2, 3, 3, 5, 5, 5, 7],
    [53, 100, 200, 324, 432, 2346, 12353, 32423],
    [5, 6, 25, 25, 52, 112, 213, 213, 525, 525, 785]
]
test_values_float = [
    [5.0, 4.2, 4.21, 5.01, 6.2],
    [6.7, 8.4, 6.2, 3.5, 7.45, 7.5, 0.01, 0.003, 4.32, 5.67]
]
test_correct_values_float = [
    [4.2, 4.21, 5.0, 5.01, 6.2],
    [0.003, 0.01, 3.5, 4.32, 5.67, 6.2, 6.7, 7.45, 7.5, 8.4]
]
test_negatives = [
    [1, -5, 3],
    [6, 8, 9, 7, 2, 3, 4, -2, -7, -5],
    [-5, -6, -1, -2222, -7, -21421, -10]

]
test_correct_negative_values = [
    [-5, 1, 3],
    [-7, -5, -2, 2, 3, 4, 6, 7, 8, 9],
    [-21421, -2222, -10, -7, -6, -5, -1]

]
test_errors = [
    [1, 'abc'],
    5,
    ['a', 'b', 'c', 's', 'e'],
    [[1, 2], [3, 4], [8, 8], 1],
    [(1, 2), [6, 4], (3, 5)],
    (2, 5, 7, 3, 4, 5, 6, 2)
]

