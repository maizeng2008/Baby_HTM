import configparser
import string
from bitarray import bitarray

BASE_CONFIGURATION = '../base_configuration.ini'
BASE_CONFIG_SECTION = 'Configuration.Name'
ENCODER_CONTENT = 'Encoder.Content'
ENCODER_SECTION = 'EncoderSection'
ENCODER_CONFIG_NAME = 'EncoderConfig'
FORMAT = 'Format'


def create_encrypted_code():
    ascii_codes = {}
    config = configparser.ConfigParser()
    config.read(BASE_CONFIGURATION)
    for c in string.printable:
        ascii_codes[c] = bitarray(format(ord(c), '07b'))
    return ascii_codes


if __name__ == "__main__":
    ascii_code = create_encrypted_code()
    a = bitarray()
    a.encode(ascii_code, 'Set A 7')
    print(a)
