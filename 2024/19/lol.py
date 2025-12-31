d=[
(1, 'Tommy', 'London', 'UK', 95, '2023-11-15'),
(2, 'Sarah', 'London', 'UK', 88, '2023-11-14'),
(3, 'James', 'London', 'UK', 92, '2023-11-16'),
(4, 'Emma', 'London', 'UK', 85, '2023-11-15'),
(5, 'Louis', 'London', 'UK', 90, '2023-11-17'),
(6, 'Oliver', 'London', 'UK', 87, '2023-11-18'),

(7, 'Harry', 'Manchester', 'UK', 91, '2023-11-15'),
(8, 'Sophie', 'Manchester', 'UK', 89, '2023-11-14'),
(9, 'William', 'Manchester', 'UK', 94, '2023-11-16'),
(10, 'Lucy', 'Manchester', 'UK', 86, '2023-11-15'),
(11, 'George', 'Manchester', 'UK', 93, '2023-11-17'),

(12, 'Charlie', 'Birmingham', 'UK', 84, '2023-11-15'),
(13, 'Emily', 'Birmingham', 'UK', 88, '2023-11-14'),
(14, 'Jack', 'Birmingham', 'UK', 92, '2023-11-16'),
(15, 'Lily', 'Birmingham', 'UK', 87, '2023-11-15'),
(16, 'Oscar', 'Birmingham', 'UK', 89, '2023-11-17'),

(17, 'Lucas', 'Paris', 'France', 88, '2023-11-15'),
(18, 'Emma', 'Paris', 'France', 91, '2023-11-14'),
(19, 'Louis', 'Paris', 'France', 87, '2023-11-16'),
(20, 'Chloe', 'Paris', 'France', 92, '2023-11-15'),
(21, 'Hugo', 'Paris', 'France', 89, '2023-11-17'),
(22, 'Lea', 'Paris', 'France', 90, '2023-11-18'),

(23, 'Thomas', 'Lyon', 'France', 93, '2023-11-15'),
(24, 'Alice', 'Lyon', 'France', 88, '2023-11-14'),
(25, 'Jules', 'Lyon', 'France', 91, '2023-11-16'),
(26, 'Louise', 'Lyon', 'France', 89, '2023-11-15'),
(27, 'Gabriel', 'Lyon', 'France', 92, '2023-11-17'),

(28, 'Max', 'Berlin', 'Germany', 94, '2023-11-15'),
(29, 'Sophie', 'Berlin', 'Germany', 89, '2023-11-14'),
(30, 'Leon', 'Berlin', 'Germany', 92, '2023-11-16'),
(31, 'Emma', 'Berlin', 'Germany', 91, '2023-11-15'),
(32, 'Paul', 'Berlin', 'Germany', 88, '2023-11-17'),
(33, 'Marie', 'Berlin', 'Germany', 93, '2023-11-18'),

(34, 'Felix', 'Munich', 'Germany', 90, '2023-11-15'),
(35, 'Anna', 'Munich', 'Germany', 87, '2023-11-14'),
(36, 'Lukas', 'Munich', 'Germany', 91, '2023-11-16'),
(37, 'Laura', 'Munich', 'Germany', 88, '2023-11-15'),
(38, 'David', 'Munich', 'Germany', 89, '2023-11-17'),

(39, 'Marco', 'Rome', 'Italy', 95, '2023-11-15'),
(40, 'Sofia', 'Rome', 'Italy', 92, '2023-11-14'),
(41, 'Leonardo', 'Rome', 'Italy', 88, '2023-11-16'),
(42, 'Giulia', 'Rome', 'Italy', 91, '2023-11-15'),
(43, 'Alessandro', 'Rome', 'Italy', 89, '2023-11-17'),
(44, 'Valentina', 'Rome', 'Italy', 93, '2023-11-18'),

(45, 'Francesco', 'Milan', 'Italy', 90, '2023-11-15'),
(46, 'Aurora', 'Milan', 'Italy', 87, '2023-11-14'),
(47, 'Lorenzo', 'Milan', 'Italy', 91, '2023-11-16'),
(48, 'Martina', 'Milan', 'Italy', 89, '2023-11-15'),
(49, 'Matteo', 'Milan', 'Italy', 88, '2023-11-17'),

(50, 'Pablo', 'Madrid', 'Spain', 93, '2023-11-15'),
(51, 'Lucia', 'Madrid', 'Spain', 90, '2023-11-14'),
(52, 'Daniel', 'Madrid', 'Spain', 88, '2023-11-16'),
(53, 'Sara', 'Madrid', 'Spain', 91, '2023-11-15'),
(54, 'Diego', 'Madrid', 'Spain', 89, '2023-11-17'),
(55, 'Carmen', 'Madrid', 'Spain', 92, '2023-11-18'),
(56, 'Javier', 'Madrid', 'Spain', 90, '2023-11-19'),

(57, 'Marc', 'Barcelona', 'Spain', 91, '2023-11-15'),
(58, 'Ana', 'Barcelona', 'Spain', 88, '2023-11-14'),
(59, 'Carlos', 'Barcelona', 'Spain', 92, '2023-11-16'),
(60, 'Marina', 'Barcelona', 'Spain', 89, '2023-11-15'),
(61, 'Alex', 'Barcelona', 'Spain', 90, '2023-11-17'),
(62, 'Elena', 'Barcelona', 'Spain', 87, '2023-11-18'),

(63, 'Lars', 'Amsterdam', 'Netherlands', 94, '2023-11-15'),
(64, 'Eva', 'Amsterdam', 'Netherlands', 91, '2023-11-14'),
(65, 'Jan', 'Amsterdam', 'Netherlands', 89, '2023-11-16'),
(66, 'Lisa', 'Amsterdam', 'Netherlands', 92, '2023-11-15'),
(67, 'Tim', 'Amsterdam', 'Netherlands', 90, '2023-11-17'),

(68, 'Daan', 'Rotterdam', 'Netherlands', 28, '2023-11-15'),
(69, 'Sophie', 'Rotterdam', 'Netherlands', 41, '2023-11-14'),
(70, 'Thomas', 'Rotterdam', 'Netherlands', 59, '2023-11-16'),
(71, 'Anna', 'Rotterdam', 'Netherlands', 17, '2023-11-15'),
(72, 'Max', 'Rotterdam', 'Netherlands', 50, '2023-11-17')]

from collections import defaultdict
cities=defaultdict(int)
citychildcount=defaultdict(int)

for t in d:
    child_id, name, city, country, naughty_nice_score, letter_sent_date = t
    city+=f', {country}'
    cities[city]+=naughty_nice_score
    citychildcount[city]+=1

for city in cities.keys():
    cities[city]//=citychildcount[city]
    pass

cities=list(cities.items())

cities.sort(lambda c:c[1], reverse=1)

print(citychildcount)

for city in cities:
    print(city)
