# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 15:13:53 2017
simplified Foster Friess active growth strategy, use only one period data

https://www.joinquant.com/post/3568?f=wx

2017.07.14
@author: talen
"""
import pandas as pd
import os
import numpy as np
os.chdir(os.getcwd())
# data = pd.read_excel('用于积极成长策略的财务指标.xlsx')
data = pd.read_excel('用于积极成长策略的财务指标沪深300.xlsx')
columns = data.columns
for i,u in enumerate(columns):
    if '资产负债率' in u:
        debt_index = u
    if '市盈率' in u:
        pe_index = u
    if '营业利润' in u:
        prof_index = u
    if '主营业务' in u:
        main_b_index = u

tmp_debt = np.array(data[debt_index])
debt_stock_index = []
for i,u in enumerate(tmp_debt):
    if isinstance(u,float) and u < 50:
        debt_stock_index.append(i)
del tmp_debt

tmp_pe = np.array(data[pe_index])
pe_stock_index = []
pe_threshold = 25
for i,u in enumerate(tmp_pe):
    if isinstance(u,float) and u < pe_threshold and u > 0:
        pe_stock_index.append(i)
del tmp_pe

tmp_prof = np.array(data[prof_index])
prof_stock_index = []
prof_threshold = 10
for i,u in enumerate(tmp_prof):
    if isinstance(u,float) and u > prof_threshold:
        prof_stock_index.append(i)
del tmp_prof

tmp_main_b = np.array(data[main_b_index])
main_b_stock_index = []
main_b_threshold = 80
for i,u in enumerate(tmp_main_b):
    if isinstance(u,float) and u > main_b_threshold:
        main_b_stock_index.append(i)
del tmp_main_b

selected_index = list(set(main_b_stock_index) & set(prof_stock_index) & set(pe_stock_index) & set(debt_stock_index))

stocks_selected = data.loc[selected_index]
print("Results are stored in the variable 'stocks_selected'.")
