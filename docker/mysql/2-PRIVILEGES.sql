#-----------------------------------#
#       USER RIGHTS MANAGEMENT      #
#-----------------------------------#
CREATE USER 'userIterator'@'%' IDENTIFIED BY 'qwerty1234';

GRANT ALL PRIVILEGES ON `iterator-db`.* TO 'userIterator'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
