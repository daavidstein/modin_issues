import modin.pandas as mpd
import pandas as pd

empty = pd.Series([])
nonempty = pd.Series([1,2])

concatted_pandas = pd.concat([empty,nonempty])
assert concatted_pandas.tolist() == [1,2]

# throws ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 1 dimension(s) and the array at index 1 has 2 dimension(s)
concatted_modin = mpd.concat([mpd.Series(empty), mpd.Series(nonempty)])

