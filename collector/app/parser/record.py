from dataclasses import dataclass

@dataclass
class FlowRecord:
    """Defines the flow record record format"""
    exporter_ip: str

    src_ip: str
    dst_ip: str

    src_port: int
    dst_port: int

    protocol: int
    tcp_flags: int

    packets: int
    bytes: int

    input_if: int
    output_if: int

    src_as: int
    dst_as: int

    first_seen: int
    last_seen: int