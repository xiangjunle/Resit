class Movie:
    def __init__(self, title, runtime, year_released, genre):
        """Initialize the Movie object with title, runtime, year released, and genre."""
        self.title = title
        self.runtime = runtime
        self.year_released = year_released
        self.genre = genre

    def print_details(self):
        """Print the details of the movie in a single line."""
        print(f"{self.title} ({self.year_released}), Runtime: {self.runtime} minutes, Genre: {self.genre}")

# Example of using the Movie class
if __name__ == "__main__":
    # Create instances of the Movie class
    godfather = Movie("The Godfather", 175, 1972, "Crime, Drama")
    shawshank = Movie("The Shawshank Redemption", 142, 1994, "Crime, Drama")
    godfather.print_details()
    shawshank.print_details()