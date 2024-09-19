import pandas as pd
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 读取CSV文件，跳过前几行
url = "https://data.weather.gov.hk/cis/csvfile/SC/2024/daily_SC_WSPD_2024.csv"
data = pd.read_csv(url, sep=',', encoding='utf-8', on_bad_lines='skip', skiprows=3)

# 查看数据的前几行
print(data.head())

# 只选择需要的列
data = data.iloc[:, [0, 1, 2, 3]]  # 选择前四列
data.columns = ['Year', 'Month', 'Day', 'Value']  # 重命名列

# 将Year, Month, Day列转换为数值，无法转换的值将变为NaN
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
data['Month'] = pd.to_numeric(data['Month'], errors='coerce')
data['Day'] = pd.to_numeric(data['Day'], errors='coerce')
data['Value'] = pd.to_numeric(data['Value'], errors='coerce')  # 转换风速值

# 删除包含NaN的行
data.dropna(subset=['Year', 'Month', 'Day', 'Value'], inplace=True)

# 创建一个日期列
data['Date'] = pd.to_datetime(data[['Year', 'Month', 'Day']], errors='coerce')

# 绘制风速随时间变化的折线图
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Value'], marker='o', linestyle='-')
plt.title('Daily Wind Speed in 2024')
plt.xlabel('Date')
plt.ylabel('Wind Speed (m/s)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
