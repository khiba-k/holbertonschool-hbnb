#!/usr/bin/python3
from place import Place
from user import User
from base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user, place, comment, ratings):
        """Initialize a new Review instance."""
        super().__init__()
        self.user = User.firstName + " " + User.lastName
        self.place_name = place.name
        self.comment = comment
        self.ratings = ratings

    def save(self):
        """Save the review only if the user is not the host of the place."""
        if self.user.id == self.place.host_id:
            raise ValueError("Host cannot review their own place.")
        super().save()

    def to_dict(self):
        """Return a dictionary representation of the Review instance."""
        base_dict = super().to_dict()
        base_dict.update({
            'user': self.user,
            'place_name': self.place_name,
            'comment': self.comment,
            'ratings': self.ratings,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        })
        return base_dict

if __name__ == "__main__":
    user = User("Khiba", "Koenane")
    place = Place("cabin")
    first_review = Review(user, place, "Loved the place!", 4)
    
    print(first_review.to_dict())  # Example output
    first_review.save()
    print(first_review.to_dict())
