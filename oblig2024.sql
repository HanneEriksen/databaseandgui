DROP SCHEMA IF EXISTS oblig2024;
CREATE SCHEMA oblig2024;
USE oblig2024;

CREATE TABLE Bilde
(
BildeID CHAR(6),
Beskrivelse CHAR(40),
OpplastetDato DATE,
Fotograf CHAR(6) NOT NULL,
CONSTRAINT BildePN PRIMARY KEY (BildeID),
CONSTRAINT FotografFN FOREIGN KEY (Fotograf) REFERENCES Bruker (BrukerID)
);

CREATE TABLE Bruker
(
BrukerID CHAR(6),
Fornavn CHAR(30),
Etternavn CHAR(20),
Epost CHAR(40),
CONSTRAINT BrukerPN PRIMARY KEY (BrukerID)
);

CREATE TABLE Likes
(
BildeID CHAR(6),
BrukerID CHAR(6),
CONSTRAINT LikesPN PRIMARY KEY (BildeID, BrukerID),
CONSTRAINT BildeIDPN FOREIGN KEY (BildeID) REFERENCES Bilde (BildeID),
CONSTRAINT BrukerIDPN FOREIGN KEY (BrukerID) REFERENCES Bruker (BrukerID)
);

CREATE TABLE Kommentar
(
BildeID CHAR(6),
BrukerID CHAR(6),
Kommentaren CHAR(40),
CONSTRAINT KommentarPN PRIMARY KEY (BildeID, BrukerID),
CONSTRAINT BildeIDPN FOREIGN KEY (BildeID) REFERENCES Bilde (BildeID),
CONSTRAINT BrukerIDPN FOREIGN KEY (BrukerID) REFERENCES Bruker (BrukerID)
);

CREATE TABLE Emneknagg
(
EmneknaggID CHAR(6),
Emneknaggen CHAR(40),
CONSTRAINT EmneknaggPN PRIMARY KEY (EmneknaggID)
);

CREATE TABLE TagForBilde
(
BildeID CHAR(6),
EmneknaggID CHAR(6),
CONSTRAINT TagForBildePN PRIMARY KEY (BildeID, EmneknaggID),
CONSTRAINT BildeIDFN FOREIGN KEY (BildeID) REFERENCES Bilde (BildeID),
CONSTRAINT EmneknaggFN FOREIGN KEY (EmneknaggID) REFERENCES Emneknagg (EmneknaggID)
);