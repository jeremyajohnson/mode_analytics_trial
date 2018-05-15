# # SQL output is imported as a pandas dataframe variable called "df"
# import pandas as pd
# import numpy as np
# import time
# from inspect import currentframe

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

# def print_time_elapsed(line):
#   now = time.time()
#   print('Line {}: {}'.format(line, now - start))

# start = time.time()
# print_time_elapsed(get_linenumber())


def z_score(x, n):
  if n < 5 or x < 100:
    return (x + 1.92) / (n + 3.84)
  elif n:
    return x / n
  else:
    return None
  
def confidence_interval(sum_filtered, sum_all, p_adjusted, n):
    if not n:
        return None
    limit =  1.64 * np.sqrt(p_adjusted * (1 - p_adjusted) / n)
    if p_adjusted - limit < sum_all < p_adjusted + limit:
        return None
    else:
        return (sum_filtered - sum_all)/sum_all

# # Transpose data, rename Issue column and sort
# df = df.set_index('dimension').T.reset_index() \
# .rename(index=str, columns={'index':'issue'}) \
# .sort_values(by=['sum_filtered'], ascending=False)

# print_time_elapsed(get_linenumber())

# # Remove rows where filtered population is 100%
# df = df.drop(df[df['sum_filtered'] >= 1].index)

# print_time_elapsed(get_linenumber())

# # Calculations
# calc_z_score = np.vectorize(z_score)
# df['p_adjusted'] = calc_z_score(df['x'], df['n'])

# print_time_elapsed(get_linenumber())

# calc_confidence_interval = np.vectorize(confidence_interval)
# df['relative_difference'] = calc_confidence_interval(df['sum_filtered'], df['sum_all'], df['p_adjusted'], df['n'])

# print_time_elapsed(get_linenumber())
  
# # Column selection and renaming
# def rename_cols(key):
#   column_labels = {
#     'issue': 'issue',
#     'sum_all': 'group',
#     'sum_filtered': 'all ctl',
#     'relative_difference': 'rel. difference'
#   }
#   try:
#       return column_labels[key]
#   except KeyError:
#     return key
  
# df = df.drop(columns=['n','x','p_adjusted']) \
# .rename(rename_cols, axis='columns')

# print_time_elapsed(get_linenumber())

# periscope.output(df)
