CREATE TABLE data_records (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    data_value JSONB,
    category VARCHAR(255)
) PARTITION BY RANGE (created_at);

CREATE INDEX idx_category ON data_records (category);
CREATE INDEX idx_created_at ON data_records (created_at);
