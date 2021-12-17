def parse(data):
    version = int(data[:3],2)
    type_id = int(data[3:6],2)
    value = None
    subpackets = None

    start_len = len(data)

    data = data[6:]
    if type_id == 4:
        value_string = ""
        while True:
            value_string += data[1:5]
            if int(data[0]) == 0:
                break 
            data = data[5:]
        data = data[5:]
        value = int(value_string,2)
    else:
        if int(data[0]) == 1:
            num_subs = int(data[1:12],2)
            subpackets = []
            data = data[12:]
            for i in range(num_subs):
                data, packet = parse(data)
                subpackets.append(packet)
        else:
            sub_len = int(data[1:16],2)
            data_part = data[16:16+sub_len]
            subpackets = []
            while len(data_part) > 0 and int(data_part,2):
                data_part, packets = parse(data_part)
                subpackets.append(packets)
            data = data[16+sub_len:]
    packet = {"version": version, "type_id": type_id, "value": value, "subpackets": subpackets}
    return data, packet

def calc_packets(packet):
    if packet["type_id"] == 0:
        mysum = 0
        for subpackets in packet["subpackets"]:
            mysum += calc_packets(subpackets)
        return mysum
    elif packet["type_id"] == 1:
        product = 1
        for subpackets in packet["subpackets"]:
            product *= calc_packets(subpackets)
        return product
    elif packet["type_id"] == 2:
        blah = []
        for subpackets in packet["subpackets"]:
            blah.append(calc_packets(subpackets))
        return min(blah)
    elif packet["type_id"] == 3:
        blah = []
        for subpackets in packet["subpackets"]:
            blah.append(calc_packets(subpackets))
        return max(blah)
    elif packet["type_id"] == 4:
        return packet["value"]
    elif packet["type_id"] == 5:
        blah = []
        for subpackets in packet["subpackets"]:
            blah.append(calc_packets(subpackets))
        return 1 if blah[0] > blah[1] else 0
    elif packet["type_id"] == 6:
        blah = []
        for subpackets in packet["subpackets"]:
            blah.append(calc_packets(subpackets))
        return 1 if blah[0] < blah[1] else 0
    elif packet["type_id"] == 7:
        blah = []
        for subpackets in packet["subpackets"]:
            blah.append(calc_packets(subpackets))
        return 1 if blah[0] == blah[1] else 0

with open("input.txt","r") as myinput:
    data = myinput.readline().strip()
    intendend_len = len(data) * 4
    data = bin(int(data,16))[2:]

    data = data.zfill(intendend_len)

    packets = []
    while len(data) > 0 and int(data,2):
        data, packet = parse(data)
        packets.append(packet)

    value = 0
    for packet in packets:
        value += calc_packets(packet)
    print(value)

