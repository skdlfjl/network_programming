'''
7. 강의자료 “소켓 프로그래밍 (UDP)”에서 슬라이드 37의 “과제10: UDP 헤더 pack/unpack 
해보기” 프로그램을 작성하라. (15점)'''


import socket
import struct
import binascii

class Udphdr:
    # Source Port, Destination Port, Length, Checksum
    def __init__(self, Source_Port, Destination_Port, Length, Checksum):
        self.Source_Port = Source_Port
        self.Destination_Port = Destination_Port
        self.Length = Length
        self.Checksum = Checksum
    
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!4H', self.Source_Port, self.Destination_Port, self.Length, self.Checksum)
        return packed



def unpack_Uphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked


udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_Uphdr = udp.pack_Udphdr()
#print(packed_Uphdr)
print(binascii.b2a_hex(packed_Uphdr))

unpacked_Uphdr = unpack_Uphdr(packed_Uphdr)
print(unpacked_Uphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(unpacked_Uphdr[0], unpacked_Uphdr[1], unpacked_Uphdr[2], unpacked_Uphdr[3]))
