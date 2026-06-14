import ipaddress
import struct
from parser.record import FlowRecord

FLOW_RECORD_FMT = (
    "!"
    "III"      # src,dst,nexthop
    "HH"       # input,output
    "II"       # packets,bytes
    "II"       # first,last
    "HH"       # srcport,dstport
    "B"        # pad1
    "B"        # tcp_flags
    "B"        # protocol
    "B"        # tos
    "HH"       # src_as,dst_as
    "BB"       # src_mask,dst_mask
    "H"        # pad2
)

FLOW_RECORD_SIZE = 48

def parse_flow_record(
    record_bytes: bytes,
    exporter_ip: str
) -> FlowRecord:
    
    """
    Parses the flow and outputs the record    
    """

    fields = struct.unpack(
        FLOW_RECORD_FMT,
        record_bytes
    )

    (
        srcaddr,
        dstaddr,
        nexthop,

        input_if,
        output_if,

        packets,
        octets,

        first,
        last,

        src_port,
        dst_port,

        _pad1,

        tcp_flags,
        protocol,
        tos,

        src_as,
        dst_as,

        src_mask,
        dst_mask,

        _pad2
    ) = fields

    return FlowRecord(
        exporter_ip=exporter_ip,

        src_ip=str(
            ipaddress.IPv4Address(srcaddr)
        ),

        dst_ip=str(
            ipaddress.IPv4Address(dstaddr)
        ),

        src_port=src_port,
        dst_port=dst_port,

        protocol=protocol,
        tcp_flags=tcp_flags,

        packets=packets,
        bytes=octets,

        input_if=input_if,
        output_if=output_if,

        src_as=src_as,
        dst_as=dst_as,

        first_seen=first,
        last_seen=last
    )