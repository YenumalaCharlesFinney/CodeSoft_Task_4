# Movie dataset
movies = {
    "Comedy": [
        "Jathi Ratnalu",
        "Vivaha Bhojanambu",
        "Sreekaram",
        "Chaavu Kaburu Challaga",
        "Thimmarusu",
        "Varudu Kaavalenu",
        "F2: Fun and Frustration",
        "Pelli SandaD",
        "Most Eligible Bachelor",
        "Ek Mini Katha"
    ],
    "Drama": [
        "Vakeel Saab",
        "Uppena",
        "Love Story",
        "Tuck Jagadish",
        "Narappa",
        "Republic",
        "Rang De",
        "Konda Polam",
        "Shyam Singha Roy",
        "Akhanda"
    ],
    "Action": [
        "RRR",
        "Pushpa",
        "Sarkaru Vaari Paata",
        "Bheemla Nayak",
        "Acharya",
        "Vakeel Saab",
        "Krack",
        "Red",
        "Wild Dog",
        "Narappa"
    ],
    "Horror": [
        "Nishabdham",
        "Masooda",
        "Bhaagamathie",
        "Jessie",
        "Taxiwala",
        "Rakshasudu",
        "Raju Gari Gadhi 3",
        "Gatham",
        "Aaviri",
        "Jessie"
    ],
    "Crime": [
        "HIT: The First Case",
        "Evaru",
        "Brochevarevarura",
        "Agent Sai Srinivasa Athreya",
        "Goodachari",
        "118",
        "V",
        "Wild Dog",
        "George Reddy",
        "Red"
    ]
}

# Get user preferences
def get_user_preference():
    print("What type of movies would you like to watch?")
    print("Options: Comedy, Drama, Action, Horror, Crime")
    user_preference = input("Enter your preference: ").capitalize()
    return user_preference

# Recommendation function
def recommend_movies(movies, genre):
    if genre in movies:
        return movies[genre]
    else:
        return []

# Main function
def main():
    movies = {
        "Comedy": [
            "Jathi Ratnalu",
            "Vivaha Bhojanambu",
            "Sreekaram",
            "Chaavu Kaburu Challaga",
            "Thimmarusu",
            "Varudu Kaavalenu",
            "F2: Fun and Frustration",
            "Pelli SandaD",
            "Most Eligible Bachelor",
            "Ek Mini Katha"
        ],
        "Drama": [
            "Vakeel Saab",
            "Uppena",
            "Love Story",
            "Tuck Jagadish",
            "Narappa",
            "Republic",
            "Rang De",
            "Konda Polam",
            "Shyam Singha Roy",
            "Akhanda"
        ],
        "Action": [
            "RRR",
            "Pushpa",
            "Sarkaru Vaari Paata",
            "Bheemla Nayak",
            "Acharya",
            "Vakeel Saab",
            "Krack",
            "Red",
            "Wild Dog",
            "Narappa"
        ],
        "Horror": [
            "Nishabdham",
            "Masooda",
            "Bhaagamathie",
            "Jessie",
            "Taxiwala",
            "Rakshasudu",
            "Raju Gari Gadhi 3",
            "Gatham",
            "Aaviri",
            "Jessie"
        ],
        "Crime": [
            "HIT: The First Case",
            "Evaru",
            "Brochevarevarura",
            "Agent Sai Srinivasa Athreya",
            "Goodachari",
            "118",
            "V",
            "Wild Dog",
            "George Reddy",
            "Red"
        ]
    }

    user_preference = get_user_preference()
    recommendations = recommend_movies(movies, user_preference)

    if recommendations:
        print(f"\nTop 10 {user_preference} movies:\n")
        for idx, movie in enumerate(recommendations, 1):
            print(f"{idx}. {movie}")
    else:
        print(f"\nSorry, we don't have recommendations for the genre: {user_preference}")

# Run the main function
if __name__ == "__main__":
    main()
