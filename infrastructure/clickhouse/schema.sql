CREATE TABLE metrics_raw (
 ts DateTime64(3),
 device_id String,
 metric String,
 value Float64
) ENGINE=MergeTree
ORDER BY (device_id, metric, ts);
