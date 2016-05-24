#!/usr/bin/env python

import pyshark

def bps(pcapfile):
    cap = pyshark.FileCapture(pcapfile)

    #print((cap[0]).__dict__)
    #print(dir(cap[0]))

    bw = {}
    for i in cap:
        epoch = int(float(i.sniff_timestamp))
        if epoch in bw.keys():
            bw[epoch] += int(i.captured_length)
        else:
            bw[epoch] = int(i.captured_length)
    return bw
