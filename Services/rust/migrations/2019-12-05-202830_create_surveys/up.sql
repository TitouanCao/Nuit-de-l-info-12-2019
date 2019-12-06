-- Your SQL goes here
CREATE TABLE Survey (
	id INTEGER NOT NULL AUTO_INCREMENT,
	user_nickname VARCHAR(20),
	type_etudiant CHAR(3),
	handicap BOOLEAN,
	type_logement CHAR(3),
	ressource_bourses int,
	ressource_job_etudiant int,
	ressource_parents int,
	PRIMARY KEY (id)
);
