CREATE TABLE IF NOT EXISTS 'nodes' (
	'to' varchar(255) NOT NULL,
	'from' varchar(255) NOT NULL,
	'date' varchar(255) NOT NULL,
	PRIMARY KEY ('to', 'from')
)