import clickhouse_connect

client = clickhouse_connect.get_client(
    host="clickhouse",
    port=8123
)

def insert_batch(flows: list[dict]):

    rows = []

    for flow in flows:

        rows.append([
            flow["timestamp"],
            flow["exporter_ip"],
            flow["src_ip"],
            flow["dst_ip"],
            flow["src_port"],
            flow["dst_port"],
            flow["protocol"],
            flow["bytes"],
            flow["packets"],
            flow["input_if"],
            flow["output_if"],
            flow["first_seen"],
            flow["last_seen"]
        ])

    client.insert(
        table="flow_records",
        data=rows,
        column_names=[
            "ts",
            "exporter_ip",
            "src_ip",
            "dst_ip",
            "src_port",
            "dst_port",
            "protocol",
            "bytes",
            "packets",
            "input_if",
            "output_if",
            "first_seen",
            "last_seen"
        ]
    )