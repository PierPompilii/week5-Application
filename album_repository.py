from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection
        
    def all (self):
        rows = self.connection.execute ("SELECT * FROM albums")
        albums = []
        for row in rows:
            album = Album (row ["title"], row ["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    def find (self, album_id):
        rows = self.connection.execute("SELECT * FROM albums WHERE id = %s" , [album_id])
        row = rows [0]
        return Album(row ["title"], row["release_year"], row["artist_id"])
    
    def create (self, album):
        self.connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", (album.title, album.release_year, album.artist_id))
        return None
    
    def delete (self, album_id):
        self.connection.execute("DELETE FROM albums WHERE id =%s" , [album_id])
        return None