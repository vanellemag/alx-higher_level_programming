CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);
INSERT INTO states (name) VALUES ("California");
INSERT INTO states (name) VALUES ("Arizona");
INSERT INTO states (name) VALUES ("Texas");
INSERT INTO states (name) VALUES ("New york");
INSERT INTO states (name) VALUES ("Navada");

CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);

INSERT INTO cities (id, state_id, name) VALUES (1, 1, "San Francisco");
INSERT INTO cities (id, state_id, name) VALUES (2, 1, "San Jose"),(3, 1, "Los Angeles"), (4, 1, "Fremont"), (5, 1, "Livermore");
INSERT INTO cities (id, state_id, name) VALUES ((6, 2, "Page"), (7, 2, "Phoenix"));
INSERT INTO cities (id, state_id, name) VALUES ((8, 3, "Dallas"), (9, 3, "Houston"), (10, 3, "Austin"));
INSERT INTO cities (id, state_id, name) VALUES ((11, 4, "New York"));
INSERT INTO cities (id, state_id, name) VALUES ((12, 5, "Las Vegas"), (13, 5, "Reno"), (14, 5, "Henderson"), (15, 5, "Carson City"));
