// nothing here


SET @dbname = DATABASE();
UPDATE testtable1 c
SET 
    c.is_default = 1,
    c.default_column_order = 1,
    c.is_enabled = 1,
    c.enable_contact_list = 1
WHERE
    c.column_name = 'name'
AND c.table_name = 'candidate';
UPDATE TESTTable2 c
SET
    c.is_default = 1,
    c.default_column_order = 1,
    c.is_enabled = 1,
    c.enable_contact_list = 1
WHERE
    c.column_name = 'name'
AND c.table_name = 'candidate';
