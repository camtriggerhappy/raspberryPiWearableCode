from smbus2 import SMBus


class MCP9808():
    addressBit = 0x18  # default for this sensor

    def __init__(self, addressBit: hex):
        addressBit = addressBit



    def readTemp(self, bus: SMBus):
        """

        :param bus: the i2c bus object
        :return: temperatures in farenheit > 0deg celsius need to learn more about bits to make it better
        """
        temp = format(bus.read_word_data(self.addressBit, 0x05), '016b')
        temp = int(temp[12:16] + temp[0:8])  # why must low level stuff be like this
        temp = float(temp) * (9 / 5) + 32  # now in celsius but im American
        return temp