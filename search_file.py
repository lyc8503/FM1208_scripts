with open("script.cmd", "w") as f:
    f.write("hf 14a apdu -skt -d 00A40000023F00\n")
    # f.write("hf 14a apdu -skt -d 00A4000002DF03\n")

    for i in range(1, 0xFFFF + 1):
        if i == 0x3F00:
            continue
        f.write("hf 14a apdu -kt -d 00A4000002%04X\n" % i)
