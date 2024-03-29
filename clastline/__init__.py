'''
This is the main implementation file for clastline
'''
import sys

__version__ = '2.1.0'


class cLastLine:
    '''
    cLastLine is a class that will manage the final line of terminal output
    '''
    def __init__(self, stream=sys.stdout, lineEnd='\n'):
        '''
        Initializer. This takes in the stream to write to, along with lineEnd, which is the character to add at the end of the last line upon exiting the context manager.
        '''
        self._stream = stream
        self._lineEnd = lineEnd
        self._lastLine = ''

    __enter__ = lambda self: self
    __exit__ = lambda self, *args, **kwargs: self.close()

    def close(self):
        '''
        will add a lineEnd to the stream if needed.
        Note: Will NOT close the underlying stream.
        '''
        if self._lastLine and (self._lastLine[-1] != self._lineEnd):
            self.write(self._lineEnd, clearBeforeWrite=False)

    def clearLine(self):
        '''
        If there has been data already written, writes spaces to effectively clear the line
        '''
        if self._lastLine != '':
            self.write(len(self._lastLine) * ' ', clearBeforeWrite=False)

    def write(self, txt, clearBeforeWrite=True):
        '''
        Main user facing function. Writes the given text over the text on the last line of the terminal.

        If clearBeforeWrite is set to True, will call clearLine() before writing, otherwise will not.

        The stream will be automatically flushed immediately after it is written.
        '''
        if clearBeforeWrite:
            self.clearLine()

        if self._lastLine != '':
            txt = '\r' + txt

        self._lastLine = txt

        self._stream.write(txt)
        self._stream.flush()
