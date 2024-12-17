import pandas as pd
import re

# 读取原始CSV文件
input_file = "spotify_streams_2024.csv"  # 请将此处替换为您的输入文件名
output_file = "processed_spotify_streams_2024t.csv"  # 输出文件名

# 读取CSV文件
data = pd.read_csv(input_file)

# 保留需要的列
columns_to_keep = ['Track', 'Album Name', 'Artist', 'Release Date', 'Spotify Streams']
filtered_data = data[columns_to_keep]

# 定义一个函数统计仅包含英文字母和数字的字符数量
def count_alphanumeric_chars(track_name):
    return len(re.findall(r'[A-Za-z0-9]', track_name))

# 新增一列统计仅包含英文字母和数字的字符数量
filtered_data['Alphanumeric Count'] = filtered_data['Track'].apply(count_alphanumeric_chars)

# 保存为新的CSV文件
filtered_data.to_csv(output_file, index=False)

print(f"处理完成，新的CSV文件已保存为：{output_file}")
