from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection


class Application():
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/music_library.sql")
        
    def run (self):
        print("Welcome to the music library manager!")
        
        while True:
            print("What would you like to do?")
            print("1 - List all albums")
            print("2 - List all artist")
            print ("3 - Exit")
            
            choice = input("Enter your choice (1, 2, 3): ")
            if choice == "1":
                album_repository = AlbumRepository(self.connection)
                albums = album_repository.all()
                for album in albums:
                    print(f"{album.title}, {album.release_year} ({album.artist_id})")
                
                    
            elif choice == "2":
                artist_repository = ArtistRepository(self.connection)
                artists = artist_repository.all()
                for artist in artists:
                    print(f"{artist.id}: {artist.name} ({artist.genre})")
            
                    
            elif choice == "3":
                print ("Good bye")
                break
            
            
if __name__ == '__main__':
    app = Application()
    app.run