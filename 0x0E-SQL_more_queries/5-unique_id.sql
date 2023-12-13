-- Create the unique_id table if it does not exist

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE, -- Column for ID with integer data type, default value 1, and must be unique
    name VARCHAR(256)         -- Column for name with VARCHAR data type
);
