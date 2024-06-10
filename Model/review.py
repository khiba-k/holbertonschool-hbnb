#!/usr/bin/python3
from place import Place
from user import User

class Review:
    def __init__(self, user, place, comment, ratings):
        self.user = User.firstName + " " + User.lastName
        self.placeName = Place.placeName
        self.comment = comment
        self.ratings = ratings
        

if __name__ == "__main__":
    user = User("Khiba", "Koenane")
    place = Place("Cabin")
    firstReview = Review(user, place, "Loved the place!", 4)
    print(firstReview.user)
    print(firstReview.placeName)
    print(firstReview.comment)
    print(firstReview.ratings)
