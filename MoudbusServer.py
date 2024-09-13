import logging
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext, ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification
from threading import Thread
import time

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# 初始值 X
X = 100

# 创建初始值列表，初始时第一个保持寄存器为 X
initial_values = [X] + [2]*4

# 创建 ModbusSequentialDataBlock
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [15]*5),  # 离散输入寄存器
    co=ModbusSequentialDataBlock(0, [16]*5),  # 线圈寄存器
    hr=ModbusSequentialDataBlock(0, initial_values),  # 保持寄存器，使用包含 X 的初始值
    ir=ModbusSequentialDataBlock(0, [19]*5)  # 输入寄存器
)

context = ModbusServerContext(slaves=store, single=True)

# 设备信息
identity = ModbusDeviceIdentification()
identity.VendorName = 'PythonModbusServer'
identity.ProductCode = 'PMBS'
identity.VendorUrl = 'http://github.com'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'Modbus Server Example'
identity.MajorMinorRevision = '1.0'

# 动态更新 X 的线程函数
def update_X():
    global X
    while True:
        time.sleep(5)  # 每隔 5 秒更新一次 X
        X += 10  # 动态修改 X 的值
        log.debug(f"Updated X to {X}")

        # 更新保持寄存器的第一个寄存器（地址 0）值
        context[0].setValues(3, 0, [X])
        log.debug("Updated holding register 0 with new X value")


# 启动 Modbus TCP 服务器
if __name__ == "__main__":
    # 启动一个线程，用于动态更新 X 的值
    thread = Thread(target=update_X)
    thread.daemon = True  # 设置为守护线程，确保程序退出时终止
    thread.start()

    # 启动 Modbus TCP 服务器
    StartTcpServer(context=context, identity=identity, address=("192.168.2.235", 502))
