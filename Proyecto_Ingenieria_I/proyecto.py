from pzem import PZEM
import machine

# define hardware uart
uart = machine.UART(1, baudrate=9600,timeout=500);
print('paso')

# define PZEM device [UART, ADDR = 0xF8 (default)]
for address in range(0xf7, 0xf8+1):
    print('address:', address)
    try:
        dev = PZEM(uart=uart,addr=address)
    except Exception as e:
        print(e)
        
# Get the PZEM real device address (e.g 0x10 = 16)
    #print(dev.getAddress())

"""
sleep = 60 * 1000

while(True):

  # Read the new values
  if(dev.read()):

    # print the reading value (public filed)
    print(dev.toString())
    print(dev.getCurrent())
    print(dev.getActivePower())

    # wait for the next reading
    machine.time.sleep_ms(sleep - dev.getReadingTime())
"""