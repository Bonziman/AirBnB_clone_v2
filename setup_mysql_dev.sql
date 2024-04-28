--script to create db and user ang give privileges
IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'hbnb_dev_db')
  BEGIN
    CREATE DATABASE hbnb_dev_db
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

