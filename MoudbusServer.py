import logging
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext, ModbusSequentialDataBlock
from pymodbus.device import ModbusDeviceIdentification
from threading import Thread
import time

# Configure logging to display debug messages
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Initial value for X
X = 100

# Create a list of initial values for the holding registers.
# The first value is X, and the rest are initialized to 2.
initial_values = [X] + [2]*4

# Create a ModbusSlaveContext to define the data store for the Modbus server.
# Define the data blocks for various types of registers:
# - Discrete Inputs (di): initialized with 15 in the first 5 addresses
# - Coils (co): initialized with 16 in the first 5 addresses
# - Holding Registers (hr): initialized with the `initial_values` list, where the first value is X
# - Input Registers (ir): initialized with 19 in the first 5 addresses
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [15]*5),  # Discrete Input Registers
    co=ModbusSequentialDataBlock(0, [16]*5),  # Coil Registers
    hr=ModbusSequentialDataBlock(0, initial_values),  # Holding Registers, first value is X
    ir=ModbusSequentialDataBlock(0, [19]*5)  # Input Registers
)

# Create a ModbusServerContext with the defined store. This context is used to manage Modbus requests.
context = ModbusServerContext(slaves=store, single=True)

# Create and configure the device identification information for the Modbus server.
identity = ModbusDeviceIdentification()
identity.VendorName = 'PythonModbusServer'
identity.ProductCode = 'PMBS'
identity.VendorUrl = 'http://github.com'
identity.ProductName = 'Modbus Server'
identity.ModelName = 'Modbus Server Example'
identity.MajorMinorRevision = '1.0'

# Define a function to dynamically update the value of X every 5 seconds.
def update_X():
    global X
    while True:
        time.sleep(5)  # Wait for 5 seconds before updating X
        X += 10  # Increment the value of X by 10
        log.debug(f"Updated X to {X}")  # Log the new value of X

        # Update the holding register at address 0 with the new value of X
        context[0].setValues(3, 0, [X])
        log.debug("Updated holding register 0 with new X value")

# Main execution block
if __name__ == "__main__":
    # Start a new thread that runs the update_X function to update X in the background
    thread = Thread(target=update_X)
    thread.daemon = True  # Set the thread as a daemon thread so it exits when the main program exits
    thread.start()

    # Start the Modbus TCP server with the specified context and device identity, listening on the given IP address and port
    StartTcpServer(context=context, identity=identity, address=("192.168.2.235", 502))
