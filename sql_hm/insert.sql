INSERT INTO genre(genre_name)
	VALUES('Jazz'), ('Rap'), ('Chanson'), ('Pop'), ('Rock');

INSERT INTO executor(executor_name)
	VALUES('Frank Sinatra'),('Louis Armstrong'),
		('�����'),('Eminem'),('AC/DC'),
		('Linkin Park'),('Justin Timberlake'),
		('������ ����');

INSERT INTO genre_executor(genre_id, executor_id)
	VALUES(1,1), (1,2),
		(2,3), (2,4),
		(3,8), (4,7),
		(5,5), (5,6);

INSERT INTO album(album_name, year_of_release)
	VALUES('My Way',1969), ('What a Wonderful World',1967),
		('����� 40',2020), ('Music To Be Murdered By - Side B',2020),
		('Back in Black',1980), ('Living Things',2012),
		('Man of the Woods',2018), ('�����',1998);

INSERT INTO executor_album(executor_id, album_id)
	values(1,1), (2,2), (3,3), (4,4),
		(5,5), (6,6), (7,7), (8,8);

INSERT INTO track(track_name, duration, album_id)
	values('Watch What Happens', 141, 1), ('My Way', 277, 1),
		('What a Wonderful World', 140, 2), ('Hello Brother', 212, 2),
		('+100500', 348, 3), ('������ � �����', 320, 3),
		('Killer', 195, 4), ('No Regrets', 201, 4),
		('Back in Black', 256, 5), ('Rock and Rol Ain"t Noise Pollution', 256, 5),
		('Burn it Down', 230, 6), ('Powerless', 225, 6),
		('Supplies', 226, 7), ('Say Something', 279, 7),
		('������������ �������', 283, 8), ('�� ��������', 221, 8);

INSERT INTO collection_of_songs(collection_name, year_of_release)
	values('�������1', 1970), ('�������2', 2014),
		('�������3', 2018), ('�������4', 2019),
		('�������5', 2019), ('�������6', 2020),
		('�������7', 2020), ('�������8', 2011);

INSERT INTO track_collection(track_id, collection_of_songs_id)
	values(1,1), (3,1), (2,2), (4,2), (9,3), (11,3), (10,4), (12,4),
		(13,5), (15,8), (14,6), (16,8), (5,7), (7,7), (6,6), (8,6);