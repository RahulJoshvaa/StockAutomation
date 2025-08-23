CREATE TABLE IF NOT EXISTS stocks (
    id SERIAL PRIMARY KEY,
    stock_name VARCHAR(50),
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
