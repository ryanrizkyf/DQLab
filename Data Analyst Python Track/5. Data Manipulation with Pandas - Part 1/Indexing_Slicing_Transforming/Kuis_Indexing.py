import pandas as pd
df_week = pd.DataFrame({'day_number': [1, 2, 3, 4, 5, 6, 7],
                        'week_type': ['weekday' for i in range(5)] + ['weekend' for i in range(2)]
                        })
df_week_ix = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
df_week.index = [df_week_ix, df_week['day_number'].to_list()]
df_week.index.names = ['name', 'num']
