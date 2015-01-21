""" Status Out, In, Maintenance """

CREATE TABLE key (
    id INT AUTO_INCREMENT,
    code TEXT,
    assignee TEXT,
    location INT,
    unit INT,
    status TEXT,
    primary key (id)
);


CREATE TABLE location (
    id INT AUTO_INCREMENT,
    name TEXT,
    address TEXT,
    manager TEXT,
    primary key (id)
);

CREATE TABLE unit (
    id INT AUTO_INCREMENT,
    number INT
    primary key (id)
);

