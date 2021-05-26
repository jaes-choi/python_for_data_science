# 데이터 과학을 위한 Python
### @DataSolution_Learning_Center
- 실습에 필요한 파일들이 저장되어 있습니다.


## Notebook 사용할 때 편리한 Shortcut들 정리


### cell 실행
- [ctrl]-[enter]
- [shift]-[enter]
- [alt]-[enter]

### command / edit 모드 전환 
- [esc] / [enter]

### cell 추가
- a 
- b

### copy & paste, delete, undo
- c
- v
- x dd
- z

### cell 나누고 합치기
- [ctrl]-[shift]-[-]
- [shift]-[m]

### code / markdown 전환
- y / m

### save
- [ctrl]-[s]

### interrupt & restart kernel
- ii
- 00

### output 표시 선택
- o

### help
- h
- p

## 곰세마리
> 곰세마리가 한집에 있어 <br> 
> 아빠곰 엄마곰 애기곰  <br>
> 아빠곰은 뚱뚱해  <br>
> 엄마곰은 날씬해  <br>
> 애기곰은 너무 귀여워  <br>
> 히쭉히쭉 잘한다 <br>

## backpack_list

backpack_list = ['paper', 'orange', 'book', 'paper', 'paper', 'apple', 'paper',
       'paper', 'orange', 'tumbler', 'tumbler', 'paper', 'book', 'pencil',
       'paper', 'tumbler']

## plot에서 한글 문제있을 때
```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
```

```python

# 데이터 만들기 
np.random.seed(19961213)
N = 200
x = np.random.randn(N)
y1 = 10*x + 5*np.random.randn(N)
y2 = -5*x + 3*np.random.randn(N)+10

# pie chart
plt.pie(a, 
        autopct='%1.1f%%', 
        explode=[0,0,0,0,0.1],
        startangle=90, 
        shadow=True
       )
plt.show()

plt.scatter(x, y1)
plt.scatter(x, y2)
plt.show()

y = pd.DataFrame([y1, y2]).T

# Legend와 Stacked, color
colors=['red','blue']
plt.hist(y, color=colors, label=colors, stacked=True)
plt.legend()
plt.show()

# 하나에 4개 subplot 그려보기
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8,6))
axes[0,0].hist(y)
axes[0,1].hist(y, 20, color=colors, label=colors, stacked=True)
axes[0,1].legend()
axes[1,0].scatter(x,y1)
axes[1,0].scatter(x,y2)
axes[1,1].boxplot(y, labels=colors)
plt.show()

```


