import socket
from parser.netflow_v5 import parse_netflow_v5_packet
from parser.record import FlowRecord
from datetime import datetime, UTC
from kafka.producer import send

def collector_v5(collector_ip = "0.0.0.0", port = 2055, max_buffer = 65535):
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    sock.bind((collector_ip, port))

    while True:
        data, addr = sock.recvfrom(max_buffer)

        exporter_ip = addr[0]

        record: FlowRecord

        records = parse_netflow_v5_packet(
            data,
            exporter_ip
        )

        for record in records:
            timestamp = datetime.now(UTC).isoformat()

            json_bytes = {
                "timestamp": timestamp,
                "src_ip": record.src_ip,
                "dst_ip": record.dst_ip,
                "src_port": record.src_port,
                "dst_port": record.dst_port,
                "protocol": record.protocol,
                "bytes": record.bytes,
                "packets": record.packets,
                "device_ip": record.exporter_ip,
                "input_if": record.input_if,
                "output_if": record.output_if,
                "first_seen": record.first_seen,
                "last_seen": record.last_seen
            }

            send(json_bytes)

