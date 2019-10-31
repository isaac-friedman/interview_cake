def pair_movies(flight_length, movie_lengths):
    """
    Takes a flight_length and a list of movie_lengths, both in minutes, and
    returns "true" if there is a pair of movies exactly as long as the flight
    and false otherwise
    """
    ttk = 0 #Time to kill after first movie
    s = set(movie_lengths) # O(1) lookup time in the average case.
    for i in movie_lengths: # O(n)
        ttk = flight_length - i
        if ttk in s: # O(1)
            return True
    return False

flight_length = 120
movie_lengths = [120, 90, 30, 73]

print(pair_movies(flight_length, movie_lengths))
