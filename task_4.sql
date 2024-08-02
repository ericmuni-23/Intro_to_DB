-- Query to get the table structure from INFORMATION_SCHEMA
SELECT 
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_DEFAULT AS 'Default Value',
    EXTRA AS 'Extra Info'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'Books'
ORDER BY 
    ORDINAL_POSITION;
    