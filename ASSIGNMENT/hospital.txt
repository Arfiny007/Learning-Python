CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    DoctorName VARCHAR(100) NOT NULL,
    DoctorSpecialization VARCHAR(255) NOT NULL,
    DoctorPhone VARCHAR(11) NOT NULL
);
INSERT INTO Doctors (DoctorName, DoctorSpecialization, DoctorPhone) VALUES
    ('Arfin', 'Neurologist', '01632121707'),
    ('Rony', 'Dermatologist', '01786991542'),
    ('Pritom', 'Orthopedic Surgeon', '01945778426'),
    ('Rafi', 'Pediatrician', '01889475260'),
    ('Yeasin', 'Cardiologist', '01678542685');


CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    PatienName VARCHAR(100) NOT NULL,
    PatienAge INT NOT NULL,
    PatienGender CHAR(1) NOT NULL,
    PatienPhone VARCHAR(11) NOT NULL
);
INSERT INTO Patients (PatienName, PatienAge, PatienGender, PatienPhone) VALUES
    ('Rakib', 25, 'F', '01678554963'),
    ('Shimanto', 40, 'M', '01758423658'),
    ('Efty', 60, 'M', '01784884257'),
    ('sonia', 35, 'F', '01975362485'),
    ('Robin', 50, 'M', '01348526792');


CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL
);
INSERT INTO Departments (DepartmentName, Location) VALUES
    ('Cardiology', 'Building A, Room-101'),
    ('Pediatrics', 'Building A, Room-102'),
    ('Orthopedics', 'Building A, Room-103'),
    ('Dermatology', 'Building A, Room-104'),
    ('Neurology', 'Building A, Room-105');


CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    DoctorID INT,
    PatientID INT,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO Appointments (DoctorID, PatientID, Date, Time, Status) VALUES
    (1, 1, '2024-12-19', '10:00:00', 'Booked'), 
    (2, 2, '2024-12-20', '11:30:00', 'Booked'), 
    (3, 3, '2024-12-19', '14:00:00', 'Booked'), 
    (4, 4, '2024-12-21', '09:00:00', 'Booked'), 
    (5, 5, '2024-12-22', '15:30:00', 'Booked'); 


CREATE TABLE Doctor_Departments (
    DoctorID INT,
    DepartmentID INT,
    PRIMARY KEY (DoctorID, DepartmentID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID) ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO Doctor_Departments (DoctorID, DepartmentID) VALUES
    (1, 1), 
    (2, 2), 
    (3, 3), 
    (4, 4), 
    (5, 5); 