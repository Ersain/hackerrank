from PythonEvaluation import eval_statement


def test_eval_statement_1():
    assert eval_statement("9 + 5") == 14


def test_eval_statement_2():
    assert eval_statement("abs(complex(6, 8))") == 10


def test_eval_statement_3():
    assert eval_statement("1024>>9") == 2
