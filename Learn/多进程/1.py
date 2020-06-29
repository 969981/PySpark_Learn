import numpy as np

# 生成模拟数据
test_data = np.linspace(1, 100, num=100)

# 设置启动的进程数
number_kernel = 4

#  根据进程数量
# 切割输入数据
data_number = len(test_data)
slice_index = []
average_slice_step = data_number // (number_kernel + 1) + 1
for i in range(number_kernel + 1):
    current_index = i * average_slice_step

    # 保证数据都被切割
    if current_index >= data_number:
        current_index = data_number
    if i == number_kernel and current_index < (data_number):
        current_index = data_number

    slice_index.append(current_index)


# 求和函数
# 因为不清楚进程通信的情况，目前只能存下来
def calcSum(index, data):
    data_sum = 0
    for i in range(len(data)):
        data_sum = data_sum + data[i]
    # 保存计算结果
    np.save(str(index) + '.npy', data_sum)


# 开始多进程
from multiprocessing import Pool

p = Pool(number_kernel)
for i in range(number_kernel):
    start_index = slice_index[i]
    end_index = slice_index[i + 1]
    # 计算
    p.apply_async(calcSum, args=(i, test_data[start_index:end_index],))
# 等待进程计算结束
print('Waiting for all subprocesses done...')
p.close()
p.join()
print('All subprocesses done.')

# 读取进程的运算结果，并合并
total_sum = 0
for i in range(number_kernel):
    sum_tmp = np.load(str(i) + '.npy')
    total_sum = total_sum + sum_tmp

print('Result:', total_sum)
