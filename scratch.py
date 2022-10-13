import numpy as np
import pandas as pd
idx = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
cols = ['2017','2018','2019','2020','2021','2022','2023','2024','2025']
df = pd.DataFrame(np.arange(108).reshape(12, 9),
                  index=idx,
                  columns=cols)
print(df)