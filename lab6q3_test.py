import lab6q3
from io import StringIO
from sys import stderr

def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('1\n3\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'1') != -1
    assert captured_stdout.strip().find(f'2') != -1
    assert captured_stdout.strip().find(f'3') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab6q3.py") as tf:
    head = [next(tf) for _ in range(68)]
    s = tf.read()
    assert(s.find("for") != -1 )
    assert(s.find("range") != -1 )

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('4\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f"I don't understand") != -1

    
def test_case4(monkeypatch, capsys):
    number_inputs = StringIO('dddd\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f"Enter valid input") != -1


def test_case5(monkeypatch, capsys):
    number_inputs = StringIO('2\n14\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f"14") != -1
    assert captured_stdout.strip().find(f"20") != -1

def test_case6(monkeypatch, capsys):
    number_inputs = StringIO('2\ndddd\n14')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f"14") != -1
    assert captured_stdout.strip().find(f"20") != -1