# Consider the following set of bytes that represent the header of a packet
# IPv4. Using the package format as a reference in
# https://en.wikipedia.org/wiki/Internet_Protocol_version_4 (and considering that the
# grouped data is big-endian), answer indicating the code snippet in Python
# which was used to obtain each response.
# IpPacket = b"\x45\x00\x00\x38\x04\x88\x40\x00\x80\x11\x69\
# x34\xc0\xa8\x01\x69\xac\xd9\x1e\x0e"
# #If you prefer, create a package using struct
# • What is the TTL of this datagram?
# • What are the origin and destination addresses of this datagram?
# • What is the size of the header and the total size of this datagram?
# • Indicate the value in each of the (three) flags related to the datagram.

import struct

IpPacket = b"\x45\x00\x00\x38\x04\x88\x40\x00\x80\x11\x69\x34\xc0\xa8\x01\x69\xac\xd9\x1e\x0e"

# Extract the TTL (Time To Live) of the datagram
ttl = struct.unpack('!B', IpPacket[8:9])[0]
print(f"The TTL of this datagram is: {ttl}")

# Extract source and destination addresses
source_ip = '.'.join(map(str, struct.unpack('!BBBB', IpPacket[12:16])))
dest_ip = '.'.join(map(str, struct.unpack('!BBBB', IpPacket[16:20])))
print(f"The source address is: {source_ip}")
print(f"The destination address is: {dest_ip}")

# Extract header size and total datagram size
header_length = (IpPacket[0] & 0x0F) * 4 # Header length is in the lowest 4 bits of the first byte
total_length = struct.unpack('!H', IpPacket[2:4])[0] # The next 2 bytes represent the total size
print(f"Header size is: {header_length} bytes")
print(f"The total size of the datagram is: {total_length} bytes")

# Extract the values ​​of the three flags related to the datagram
flags = struct.unpack('!H', IpPacket[6:8])[0]
reserved_flag = (flags >> 15) & 1
dont_fragment_flag = (flags >> 14) & 1
more_fragment_flag = (flags >> 13) & 1
print(f"The value of the reserved bit is: {reserved_flag}")
print(f"The value of the 'Don't Fragment' bit is: {dont_fragment_flag}")
print(f"The value of the 'More Fragments' bit is: {more_fragment_flag}")
