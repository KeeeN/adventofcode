import os
from functools import reduce
from math import prod


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_message(input_path: str) -> str:
    with open(input_path, "r") as file:
        return file.readline().strip()


def read_packet(binary_message: str) -> tuple[tuple, str]:
    if int(binary_message):
        version = int(binary_message[:3], base=2)
        type_id = int(binary_message[3:6], base=2)
        binary_message = binary_message[6:]
        match type_id:
            case 4:
                content = ""
                while True:
                    code, data, binary_message = binary_message[0], binary_message[1:5], binary_message[5:]
                    content += data
                    if code == "0":
                        break
                decoded = int(content, base=2)
                return (version, type_id, decoded), binary_message
            case _:
                length_type, binary_message = int(binary_message[0], base=2), binary_message[1:]
                match length_type:
                    case 0:
                        subpacket_length, binary_message = int(binary_message[0:15], base=2), binary_message[15:]
                        subpackets = []
                        starting_len = len(binary_message)
                        while len(binary_message) > (starting_len - subpacket_length):
                            if binary_message == "000":
                                breakpoint()
                            subpacket, binary_message = read_packet(binary_message)
                            subpackets.append(subpacket)
                        return (version, type_id, subpackets), binary_message
                    case 1:
                        packets_to_read, binary_message = int(binary_message[0:11], base=2), binary_message[11:]
                        subpackets = []
                        for _ in range(packets_to_read):
                            subpacket, binary_message = read_packet(binary_message)
                            subpackets.append(subpacket)
                        return (version, type_id, subpackets), binary_message


def flatten(packet: tuple) -> list:
    output = []
    if type(packet[2]) is list:
        output.append((packet[0], packet[1], "list"))
        for subpacket in packet[2]:
            output.extend(flatten(subpacket))
    else:
        output.append(packet)
    return output


def process(packet: list) -> int:
    match packet[1]:
        case 4:
            return packet[2]
        case 0:
            return sum(process(sub) for sub in packet[2])
        case 1:
            return prod(process(sub) for sub in packet[2])
        case 2:
            return min(process(sub) for sub in packet[2])
        case 3:
            return max(process(sub) for sub in packet[2])
        case 5:
            return 1 if process(packet[2][0]) > process(packet[2][1]) else 0
        case 6:
            return 1 if process(packet[2][0]) < process(packet[2][1]) else 0
        case 7:
            return 1 if process(packet[2][0]) == process(packet[2][1]) else 0
    return 0


def part_1(input_path: str) -> int:
    message = load_message(input_path)
    end_length = len(message) * 4
    hex_as_binary = bin(int(message, base=16))
    binary_message = hex_as_binary[2:].zfill(end_length)
    packets, _ = read_packet(binary_message)
    return reduce(lambda acc, e: e[0] + acc, flatten(packets), 0)


def part_2(input_path: str) -> int:
    message = load_message(input_path)
    end_length = len(message) * 4
    hex_as_binary = bin(int(message, base=16))
    binary_message = hex_as_binary[2:].zfill(end_length)
    packets, _ = read_packet(binary_message)
    return process(packets)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
