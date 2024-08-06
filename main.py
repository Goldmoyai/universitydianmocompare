import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import scipy.stats as st

idw1 = pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=2,header=0)
idw2 = pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=3,header=0)
idw3 = pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=4,header=0)
idm1 = pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=5,header=0)
idm2 = pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=6,header=0)
idm3 = pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=7,header=0)
ilbilm2 =pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=8,header=0)
ilbilm3 =pd.read_excel('/Users/user/Downloads/Динамометрия 1985-2024 Сравнение (2).xlsx', sheet_name=9,header=0)

df = pd.DataFrame(columns=['университет 1', 'университет 2', 'т критерий по правой', 'т критерий по левой'])
def univer(data1, name1, data2, name2):
    alpha = 0.05
    t_kriteri1 = st.ttest_ind(data1['прав рука'], data2['прав рука'])
    t_kriteri2 = st.ttest_ind(data1[' левая рука'], data2[' левая рука'])
    p_value1 = round(t_kriteri1.pvalue, 2)
    p_value2 = round(t_kriteri2.pvalue, 2)

    if p_value1 < alpha and p_value2 < alpha:
        new_row = [name1, name2, f'p(0.05)={p_value1}, есть значимые различия',
                   f'p(0.05)={p_value2}, есть значимые различия']
    elif p_value1 < alpha and p_value2 > alpha:
        new_row = [name1, name2, f'p(0.05)={p_value1}, есть значимые различия',
                   f'p(0.05)={p_value2}, нет значимых различий']
    elif p_value1 > alpha and p_value2 < alpha:
        new_row = [name1, name2, f'p(0.05)={p_value1}, нет значимых различий',
                   f'p(0.05)={p_value2}, есть значимые различия']
    elif p_value1 >= alpha and p_value2 >= alpha:
        new_row = [name1, name2, f'p(0.05)={p_value1}, нет значимых различий',
                   f'p(0.05)={p_value2}, нет значимых различий']

    df.loc[len(df)] = new_row


# Example usage


# Example usage
univer(idw1, 'idw1', idw2, 'idw2')
univer(idw2, 'idw2', idw3, 'idw3')
univer(idw1, 'idw1', idw3, 'idw3')
univer(idm1, 'idm1', idm2, 'idm2')
univer(idm2, 'idm2', idm3, 'idm3')
univer(idm1, 'idm1', idm3, 'idm3')
univer(idm2,'idm2',ilbilm2, 'ilbilm2')
univer(idm3,'idm3',ilbilm3, 'ilbilm3')



output_file = '/Users/user/Downloads/trythat2.xlsx'
df.to_excel(output_file, index=False)
