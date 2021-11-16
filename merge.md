```python
pop = population[['시도','총인구수']]

pop.head(2)

ta_agg_col = ta_agg.reset_index()

ta_agg_col.head(2)

ta_agg_col.merge(pop, left_on='발생지시도', right_on='시도')

ta_agg_col.columns = ['시도', '사망', '사망_max', '중상', '대형', '대형사고율', '사고건수']

ta_agg_col.merge(pop, left_on='시도', right_on='시도')

ta_agg_col.merge(pop, on='시도', how='outer')

pop = pop[:10]

ta_agg_col.merge(pop, on='시도', how='inner')
```