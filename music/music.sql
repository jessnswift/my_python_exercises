-- 1. Query all of the entries in the Genre table
SELECT Genre.label
FROM Genre

-- 2. Using the INSERT statement, add one of your favorite artists to the Artist table.
INSERT into Artist
values(null, 'Nsync', 1995)

-- 3. Using the INSERT statement, add one, or more, albums by your artist to the Album table.
insert into Album
select null, "Nsync", 1997, 567, "Ariola", artist.artistid, 7
FROM Artist
WHERE Artist.artistname = "Nsync"

-- 4. Using the INSERT statement, add some songs that are on that album to the Song table.
insert into Song
values (null, "Tearin Up My Heart", 210, 1997, 7, 28, 23);

INSERT into Song
SELECT null, "I want you back.", 210, 1997, genre.genreId, artist.ArtistId, Album.AlbumId
FROM Genre, Artist, Album
WHERE artist.artistName = "Nsync"
AND genre.label = "Pop"
AND Album.title = "Nsync"

-- 5. Write a SELECT query that provides the song titles, album title, and artist name for all
-- of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables,
-- and the WHERE keyword to filter the results to the album and artist you added.

SELECT artist.artistName, album.title as "album title", song.title as "song title"
FROM Song
LEFT JOIN Album
LEFT JOIN Artist
WHERE album.artistId = 28
AND song.AlbumId = album.albumId
AND artist.artistName = "Nsync"

-- 6. Write a SELECT statement to display how many songs exist for each album. You'll need to use
-- the COUNT() function and the GROUP BY keyword sequence.

SELECT count() as '# of songs', album.title as "Album Title"
FROM Song
JOIN Album
On Song.AlbumId = Album.AlbumId
GROUP BY song.AlbumId
ORDER BY album.title

-- 7. Write a SELECT statement to display how many songs exist for each artist. You'll need to use
-- the COUNT() function and the GROUP BY keyword sequence.

SELECT count() as '# of songs', artist.artistName as 'Artist Name'
FROM Song
JOIN Artist
ON song.ArtistId = Artist.ArtistId
GROUP BY song.artistId
ORDER BY Artist.ArtistName

-- 8. Write a SELECT statement to display how many songs exist for each genre. You'll need to use
-- the COUNT() function and the GROUP BY keyword sequence.

SELECT count() as '# of Albums', genre.genreId as 'Grene'
FROM Album
JOIN Genre
ON album.GenreId = Genre.GenreId
GROUP BY album.genreId
ORDER BY Genre.GenreId

-- 9. Using MAX() function, write a select statement to find the album with the longest duration.
-- The result should display the album title and the duration.

SELECT max(songlength) as 'Duration', album.Title as 'Album'
FROM Song
JOIN Album
ON song.AlbumId = album.AlbumId

-- 10. Using MAX() function, write a select statement to find the song with the longest duration.
-- The result should display the song title and the duration.

SELECT max(songlength) as 'Duration', song.Title as 'Title'
FROM Song

-- 11. Modify the previous query to also display the title of the album.

SELECT max(songlength) as 'Duration', song.Title as 'Title', Album.Title as 'Album'
FROM Song
JOIN Album