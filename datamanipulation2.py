import pandas as pd

# 读取原始CSV文件
input_file = "spotify_streams_2024.csv"  # 请将此处替换为您的输入文件名
output_file = "processed_spotify_streams_2024t.csv"  # 输出文件名

# 读取CSV文件
data = pd.read_csv(input_file)

# 保留需要的列
columns_to_keep = ['Track', 'Album Name', 'Artist', 'Release Date', 'Spotify Streams']
filtered_data = data[columns_to_keep]

# 新增一列统计Track字符串长度
filtered_data['Track Length'] = filtered_data['Track'].apply(len)

# 保存为新的CSV文件
filtered_data.to_csv(output_file, index=False)

print(f"处理完成，新的CSV文件已保存为：{output_file}")
