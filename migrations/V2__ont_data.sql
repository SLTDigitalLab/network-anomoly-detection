CREATE TABLE IF NOT EXISTS data_ont (
    id serial primary key, 
    rx FLOAT, 
    tx FLOAT, 
    ymd TIMESTAMP, 
    rx_score FLOAT,
    tx_score FLOAT,
    anomoly BOOLEAN,
    user VARCHAR(11)
);