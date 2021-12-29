import os
from functools import reduce


def get_local_file_abs_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


def load_message(input_path: str) -> str:
    with open(input_path, "r") as file:
        return file.readline().strip()


def read_packet(binary_message: str) -> tuple[list, str]:
    packets = []
    if int(binary_message):
        version = int(binary_message[:3], base=2)
        type_id = int(binary_message[3:6], base=2)
        binary_message = binary_message[6:]
        print(f"{version=}")
        print(f"{type_id=}")
        print(f"{binary_message=}")
        match type_id:
            case 4:
                content = ""
                while True:
                    code, data, binary_message = binary_message[0], binary_message[1:5], binary_message[5:]
                    content += data
                    if code == "0":
                        break
                decoded = int(content, base=2)
                packets.append((version, type_id, decoded))
            case _:
                length_type, binary_message = int(binary_message[0], base=2), binary_message[1:]
                print(f"{length_type=}", binary_message)
                match length_type:
                    case 0:
                        subpacket_length, binary_message = int(binary_message[0:15], base=2), binary_message[15:]
                        print(f"{subpacket_length=}", binary_message)
                        packets.append((version, type_id, subpacket_length))
                        subpackets = []
                        starting_len = len(binary_message)
                        print(f"{len(binary_message)=}")
                        print(f"{starting_len=}")
                        print(f"{subpacket_length=}")
                        while len(binary_message) > (starting_len - subpacket_length):
                            if binary_message == "000":
                                breakpoint()
                            subpacket, binary_message = read_packet(binary_message)
                            packets.extend(subpacket)
                    case 1:
                        packets_to_read, binary_message = int(binary_message[0:11], base=2), binary_message[11:]
                        print(f"{packets_to_read=}", binary_message)
                        packets.append((version, type_id, packets_to_read))
                        subpackets = []
                        for _ in range(packets_to_read):
                            subpacket, binary_message = read_packet(binary_message)
                            packets.extend(subpacket)

    return packets, binary_message


def part_1(input_path: str) -> int:
    message = load_message(input_path)
    # message = "A0016C880162017C3686B18A3D4780"
    end_length = len(message) * 4
    hex_as_binary = bin(int(message, base=16))
    binary_message = hex_as_binary[2:].zfill(end_length)
    print(binary_message)
    packets, _ = read_packet(binary_message)
    print(packets)
    return reduce(lambda acc, e: e[0] + acc, packets, 0)


def part_2(input_path: str) -> int:
    return load_message(input_path)


if __name__ == "__main__":
    input_path = get_local_file_abs_path("input.txt")
    print(part_1(input_path))
    print(part_2(input_path))
