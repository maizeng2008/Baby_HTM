import numpy as np
import math
# from .base import Base
# import Encoder.utils as utils
from bitarray import bitarray
from .ascii_converter import create_encrypted_code
import Encoder.ascii_converter
import utils

'''
Data need to be a string and contain different fields
fields (dictionary) need to be in a specific order to be trained
Every character will be convert to binary (7 bits) because in 
ASCII code the max number for representing a char is 127 which can be 
represented by 7 bits in binary
'''


class encoder:

    def __init__(self, num_bits):
        self.nbits = num_bits

    def encode(self, data):
        ascii_codes = create_encrypted_code()
        c_encoded = bitarray()
        for key in data:
            v_encoded = bitarray()
            v_encoded.encode(ascii_codes, data[key])
            # print(v_encoded)
            c_encoded.extend(v_encoded)
        if v_encoded.length() > self.nbits:
            print("Fields are oversize")
        else:
            extended_code = (self.nbits - v_encoded.length()) * bitarray([False])
            c_encoded.extend(extended_code)
        return c_encoded

    def decode(self, data):
        raise NotImplementedError

    # override this method if you can, better provide directly BMap1D output
    def np_encode(self, data):
        return utils.bits2np(self.encode(data))

    def np_decode(self, data):
        return utils.bits2np(self.decode(data))

    def batch_encode(self, data):
        if isinstance(data, list): data = np.array(data)
        rv = np.zeros((data.size, self.nbits))
        for i in np.arange(data.size):
            rv[i] = self.encode(data[i])
        return rv

    def batch_decode(self, data):
        if isinstance(data, list): data = np.array(data)
        rv = np.zeros((data.size, self.nbits))
        for i in np.arange(data.size):
            rv[i] = self.decode(data[i])
        return rv


if __name__ == "__main__":
    Encoder = encoder(80)
    print(Encoder.encode({'instruction1': 'Set A 1', 'Time': '5:02', 'instruction type': 'SET'
                    , 'Key': 'A', 'Value': '1'}))
