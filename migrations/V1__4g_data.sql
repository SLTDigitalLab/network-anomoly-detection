CREATE TABLE IF NOT EXISTS data_4g (
    id serial primary key, 
    rsrq FLOAT, 
    rsrp FLOAT, 
    ymd TIMESTAMP, 
    rsrp_score FLOAT,
    rsrq_score FLOAT,
    anomoly BOOLEAN,
    user VARCHAR(11)
);