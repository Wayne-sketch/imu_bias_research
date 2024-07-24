import matplotlib.pyplot as plt

# 文件名
filename1 = 'imu_bias_a0.0_0.0_MH01.txt'
filename2 = 'imu_bias_a0.15_0.0_MH01.txt'


# 读取数据
timestamps1 = []
ax_values1 = []
ay_values1 = []
az_values1 = []
gx_values1 = []
gy_values1 = []
gz_values1 = []

with open(filename1, 'r') as file1:
    # 跳过第一行（假设第一行是标题）
    # next(file)
    for line1 in file1:
        data1 = line1.strip().split(',')
        timestamps1.append(float(data1[0]))
        ax_values1.append(float(data1[1]))
        ay_values1.append(float(data1[2]))
        az_values1.append(float(data1[3]))
        gx_values1.append(float(data1[4]))
        gy_values1.append(float(data1[5]))
        gz_values1.append(float(data1[6]))

# 选择你想绘制的列（例如：ax_values）
y_values11 = ax_values1
y_values12 = ay_values1
y_values13 = az_values1
y_values14 = gx_values1
y_values15 = gy_values1
y_values16 = gz_values1


# 创建图表
plt.plot(timestamps1, y_values11, label = 'acc_bias_x_0.05')
plt.plot(timestamps1, y_values12, label = 'acc_bias_y_0.05')
plt.plot(timestamps1, y_values13, label = 'acc_bias_z_0.05')
# plt.plot(timestamps1, y_values14, label = 'gyro_bias_x_0.05')
# plt.plot(timestamps1, y_values15, label = 'gyro_bias_y_0.05')
# plt.plot(timestamps1, y_values16, label = 'gyro_bias_z_0.05')

# 读取数据
timestamps2 = []
ax_values2 = []
ay_values2 = []
az_values2 = []
gx_values2 = []
gy_values2 = []
gz_values2 = []

with open(filename2, 'r') as file2:
    # 跳过第一行（假设第一行是标题）
    # next(file)
    for line2 in file2:
        data2 = line2.strip().split(',')
        timestamps2.append(float(data2[0]))
        ax_values2.append(float(data2[1]))
        ay_values2.append(float(data2[2]))
        az_values2.append(float(data2[3]))
        gx_values2.append(float(data2[4]))
        gy_values2.append(float(data2[5]))
        gz_values2.append(float(data2[6]))

# 选择你想绘制的列（例如：ax_values）
y_values21 = ax_values2
y_values22 = ay_values2
y_values23 = az_values2
y_values24 = gx_values2
y_values25 = gy_values2
y_values26 = gz_values2


# 创建图表
# plt.plot(timestamps2, y_values21, label = 'acc_bias_x_0.15')
# plt.plot(timestamps2, y_values22, label = 'acc_bias_y_0.15')
# plt.plot(timestamps2, y_values23, label = 'acc_bias_z_0.15')
# plt.plot(timestamps2, y_values24, label = 'gyro_bias_x_0.15')
# plt.plot(timestamps2, y_values25, label = 'gyro_bias_y_0.15')
# plt.plot(timestamps2, y_values26, label = 'gyro_bias_z_0.15')

# 读取数据
# y_values31 = [a - b for a, b in
# zip(y_values21, y_values11)]
# y_values32 = [a - b for a, b in
# zip(y_values22, y_values12)]
# y_values33 = [a - b for a, b in
# zip(y_values23, y_values13)]
# y_values34 = [a - b for a, b in
# zip(y_values24, y_values14)]
# y_values35 = [a - b for a, b in
# zip(y_values25, y_values15)]
# y_values36 = [a - b for a, b in
# zip(y_values26, y_values16)]
# plt.plot(timestamps2, y_values31, label = 'acc_bias_x')
# plt.plot(timestamps2, y_values32, label = 'acc_bias_y')
# plt.plot(timestamps2, y_values33, label = 'acc_bias_z')
# plt.plot(timestamps2, y_values34, label = 'gyro_bias_x')
# plt.plot(timestamps2, y_values35, label = 'gyro_bias_y')
# plt.plot(timestamps2, y_values36, label = 'gyro_bias_z')




# 添加标题和标签
plt.legend()
plt.title('Accelerometer Bias X over Time')
plt.xlabel('Timestamp')
plt.ylabel('Accelerometer Bias X')

# 显示图表
plt.show()
