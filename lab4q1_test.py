import lab4q1
from io import StringIO
from sys import stderr

def generate_value(a=0, b=0):
  return 5

def test_matching(monkeypatch, capsys):
  monkeypatch.setattr("random.randint", generate_value)
  number_inputs = StringIO("10\n5\nn\n")

  monkeypatch.setattr('sys.stdin', number_inputs)
  lab4q1.main()
  captured_stdout, captured_stderr = capsys.readouterr()  

  assert captured_stdout.strip().find(f'too high') != -1
  assert captured_stdout.strip().find(f'2') != -1

def test_matching2(monkeypatch, capsys):
  monkeypatch.setattr("random.randint", generate_value)
  number_inputs = StringIO("3\n5\nn\n")

  monkeypatch.setattr('sys.stdin', number_inputs)
  lab4q1.main()
  captured_stdout, captured_stderr = capsys.readouterr()  

  assert captured_stdout.strip().find(f'too low') != -1
  assert captured_stdout.strip().find(f'2') != -1

def test_matching3(monkeypatch, capsys):
  monkeypatch.setattr("random.randint", generate_value)
  number_inputs = StringIO("3\n5\ny\n6\n5\nn\n")

  monkeypatch.setattr('sys.stdin', number_inputs)
  lab4q1.main()
  captured_stdout, captured_stderr = capsys.readouterr()  

  assert captured_stdout.strip().find(f'too low') != -1
  assert captured_stdout.strip().find(f'too high') != -1
  assert captured_stdout.strip().find(f'2') != -1

def test_matching4(monkeypatch, capsys):
  monkeypatch.setattr("random.randint", generate_value)
  number_inputs = StringIO("3\n5\nr\nn\n")

  monkeypatch.setattr('sys.stdin', number_inputs)
  lab4q1.main()
  captured_stdout, captured_stderr = capsys.readouterr()  

  assert captured_stdout.strip().find(f'too low') != -1
  assert captured_stdout.strip().find(f'2') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab4q1.py") as tf:
    head = [next(tf) for _ in range(13)]
    s = tf.read()
    assert(s.find("while") != -1 )

