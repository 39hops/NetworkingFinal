from random import getrandbits
from socket import inet_ntop, AF_INET6
from struct import pack
import ipaddress


def random_ipv6():
    return inet_ntop(AF_INET6, pack(">QQ", getrandbits(64), getrandbits(64)))


with open("ipv6_compressed.txt", "w") as file:
    for i in range(400):
        print(f"{i} :  {ipaddress.IPv6Address(random_ipv6()).exploded}")
        file.write(f"{i} : {ipaddress.IPv6Address(random_ipv6()).compressed}\n")
