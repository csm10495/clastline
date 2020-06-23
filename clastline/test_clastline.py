import os
import shutil
import unittest.mock

from .clastline import cLastLine


def test_simple():
    with cLastLine() as cll:
        cll.write('hi')
        cll.write('word')
        cll.write('test', clearBeforeWrite=False)

    clearText = shutil.get_terminal_size().columns * ' '
    assert cll._writtenData == f'''hi\r{clearText}\rword\rtest\r{os.linesep}'''

def test_nothing_written_on_nothing_written():
    with cLastLine() as cll:
        pass

    assert cll._writtenData == ''

def test_one_line_with_alt_end():
    with cLastLine(lineEnd='bleh') as cll:
        cll.write('a')

    assert cll._writtenData == 'a\rbleh'
