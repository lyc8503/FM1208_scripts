with open("script.cmd", "w") as f:
    for i in range(1, 0xFF + 1):
        f.write("hf 14a apdu -kt -d 00B2%02X0400\n" % i)
