import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# numpy 배열 만들기
data = np.array([10, 20, 30, 40, 50])

print("데이터:", data)
print("평균:", np.mean(data))
print("합계:", np.sum(data))

# pandas 데이터프레임 만들기
df = pd.DataFrame({
    "value": data
})

print("\nDataFrame:")
print(df)

# 그래프 그리기
plt.plot(data)
plt.title("Simple Data Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()