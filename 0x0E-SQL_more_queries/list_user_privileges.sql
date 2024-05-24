-- Script to list all privileges of MySQL users user_0d_1 and user_0d_2

-- Query to list global privileges from mysql.user table
SELECT 
    user AS User, 
    host AS Host, 
    CONCAT(
        'Global Privileges: ', 
        IF(Super_priv = 'Y', 'SUPER, ', ''),
        IF(Select_priv = 'Y', 'SELECT, ', ''),
        IF(Insert_priv = 'Y', 'INSERT, ', ''),
        IF(Update_priv = 'Y', 'UPDATE, ', ''),
        IF(Delete_priv = 'Y', 'DELETE, ', ''),
        IF(Create_priv = 'Y', 'CREATE, ', ''),
        IF(Drop_priv = 'Y', 'DROP, ', ''),
        IF(Grant_priv = 'Y', 'GRANT, ', ''),
        IF(Index_priv = 'Y', 'INDEX, ', ''),
        IF(Alter_priv = 'Y', 'ALTER, ', ''),
        IF(Show_db_priv = 'Y', 'SHOW DATABASES, ', ''),
        IF(Execute_priv = 'Y', 'EXECUTE, ', ''),
        IF(Trigger_priv = 'Y', 'TRIGGER, ', ''),
        IF(Create_view_priv = 'Y', 'CREATE VIEW, ', ''),
        IF(Show_view_priv = 'Y', 'SHOW VIEW, ', ''),
        IF(Create_routine_priv = 'Y', 'CREATE ROUTINE, ', ''),
        IF(Alter_routine_priv = 'Y', 'ALTER ROUTINE, ', ''),
        IF(Create_user_priv = 'Y', 'CREATE USER, ', ''),
        IF(Event_priv = 'Y', 'EVENT, ', ''),
        IF(Create_tablespace_priv = 'Y', 'CREATE TABLESPACE, ', '')
    ) AS Privileges
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2');

-- Query to list database-level privileges from mysql.db table
SELECT 
    user AS User, 
    host AS Host, 
    CONCAT(
        'Global Privileges: ', 
        IF(Select_priv = 'Y', 'SELECT, ', ''),
        IF(Insert_priv = 'Y', 'INSERT, ', ''),
        IF(Update_priv = 'Y', 'UPDATE, ', ''),
        IF(Delete_priv = 'Y', 'DELETE, ', ''),
        IF(Create_priv = 'Y', 'CREATE, ', ''),
        IF(Drop_priv = 'Y', 'DROP, ', ''),
        IF(Grant_priv = 'Y', 'GRANT, ', ''),
        IF(Index_priv = 'Y', 'INDEX, ', ''),
        IF(Alter_priv = 'Y', 'ALTER, ', ''),
        IF(Create_tmp_table_priv = 'Y', 'CREATE TEMPORARY TABLES, ', ''),
        IF(Lock_tables_priv = 'Y', 'LOCK TABLES, ', ''),
        IF(Execute_priv = 'Y', 'EXECUTE, ', ''),
        IF(Trigger_priv = 'Y', 'TRIGGER, ', ''),
        IF(Create_view_priv = 'Y', 'CREATE VIEW, ', ''),
        IF(Show_view_priv = 'Y', 'SHOW VIEW, ', ''),
        IF(Create_routine_priv = 'Y', 'CREATE ROUTINE, ', ''),
        IF(Alter_routine_priv = 'Y', 'ALTER ROUTINE, ', ''),
        IF(Event_priv = 'Y', 'EVENT, ', '')
    ) AS Privileges
FROM mysql.db
WHERE user IN ('user_0d_1', 'user_0d_2');
