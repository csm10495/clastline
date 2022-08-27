import io
import shutil

from . import cLastLine


def test_simple():
    stream = io.StringIO()

    with cLastLine(stream) as cll:
        cll.write('hi')
        cll.write('word')
        cll.write('test', clearBeforeWrite=False)

    assert stream.getvalue() == f'''hi\r  \rword\rtest\r\n'''

def test_last_line_empty():
    with cLastLine() as cll:
        pass

    assert cll._lastLine == ''

def test_one_line_with_alt_end():
    stream = io.StringIO()

    with cLastLine(stream, lineEnd='bleh') as cll:
        cll.write('a')

    assert stream.getvalue() == 'a\rbleh'
