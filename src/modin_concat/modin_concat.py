import modin.pandas as mpd
import pandas as pd
import pytest
empty = pd.Series([])
nonempty = pd.Series([1,2])

concatted_pandas = pd.concat([empty,nonempty])
assert concatted_pandas.tolist() == [1,2]

with pytest.raises(ValueError):
    concatted_modin = mpd.concat([mpd.Series(empty), mpd.Series(nonempty)])

