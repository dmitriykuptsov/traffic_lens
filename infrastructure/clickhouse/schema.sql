CREATE TABLE flow_records
(
    ts DateTime64(3),

    exporter_ip String,

    src_ip IPv4,
    dst_ip IPv4,

    src_port UInt16,
    dst_port UInt16,

    protocol UInt8,

    bytes UInt64,
    packets UInt64,

    input_if UInt16,
    output_if UInt16,

    src_as UInt32,
    dst_as UInt32
)
ENGINE = MergeTree
PARTITION BY toDate(ts)
ORDER BY (ts, exporter_ip);