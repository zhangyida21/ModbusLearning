# from pymodbus.client import ModbusTcpClient
#
# # 初始化Modbus客户端（TCP模式）
# server_ip = '192.168.2.235'  # Server IP
# server_port = 502            # Modbus port
#
# client = ModbusTcpClient(server_ip, port=server_port)
# client.connect()
#
# # 读取保持寄存器
# address = 0  # 起始地址
# register_count = 4  # 读取1个寄存器
#
# response = client.read_holding_registers(address, register_count, slave=1)
#
# # 检查读取是否成功
# if not response.isError():
#     print("保持寄存器中的值 (X):", response.registers)
# else:
#     print("读取保持寄存器时出错:", response)
#
# client.close()
from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient('192.168.2.235')
client.connect()


# 循环读取保持寄存器的第一个值
for _ in range(10):
    response = client.read_holding_registers(0, 1)
    print(f"X = {response.registers[0]}")
    time.sleep(5)  # 每隔 5 秒读取一次

client.close()
