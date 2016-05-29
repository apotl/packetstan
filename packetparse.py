#!/usr/bin/env python

import csv
import pyshark


def breakdown_to_csv(pcapfile):
    cap = pyshark.FileCapture(pcapfile)
    fwrite = csv.writer(open('full_breakdown.csv', 'wb'))
    fwrite.writerow(['frame_number', 'frame_time', 'eth_src', 'eth_dsst',
                     'ip_src', 'ip_dst', 'ip_proto', 'frame_len'])
    for i in cap:
        fwrite.writerow([i.number, i.sniff_time.isoformat(' '), i.eth.src,
                         i.eth.dst, i.ip.src, i.ip.dst, i.ip.proto, i.length])


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
