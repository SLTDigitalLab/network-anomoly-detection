CREATE TABLE IF NOT EXISTS data_ont (
    id serial primary key, 
    rx FLOAT, 
    tx FLOAT, 
    ymd TIMESTAMP, 
    rx_score INTEGER,
    tx_score INTEGER,
    anomoly INTEGER,
    user TEXT
);