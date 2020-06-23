# cLastLine

Module to easily allow rewriting the last line in the terminal.

# Example

```
from clastline import cLastLine

with cLastLine() as c:
    # write testing to the last line
    c.write("testing")

    # write testing again to the last line (overwrites previous)
    c.write("testing again")

    # overwrite the first characters of the line (though leave rest)
    c.write("ouch!", clearBeforeWrite=False)
```

# Install
```
pip install clastline
```
