"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from src.recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    from recommender import load_songs, recommend_songs


TASTE_PROFILE = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.86,
    "likes_acoustic": False,
}


USER_PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.25,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.85,
        "likes_acoustic": False,
    },
    # Adversarial profile: contradictory mood/energy can expose weighting artifacts.
    "Adversarial: Sad But Hyper": {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.9,
        "likes_acoustic": True,
    },
    # Edge profile: out-of-range energy tests score clipping behavior.
    "Edge Case: Energy Out Of Range": {
        "genre": "edm",
        "mood": "happy",
        "energy": 1.5,
        "likes_acoustic": False,
    },
    # Adversarial profile: unknown labels and non-boolean acoustic pref test robustness.
    "Adversarial: Unknown Labels": {
        "genre": "micro-genre-that-does-not-exist",
        "mood": "nostalgic",
        "energy": 0.5,
        "likes_acoustic": "sometimes",
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")
    print(f"Target taste profile: {TASTE_PROFILE}")
    print(
        "This profile is specific enough to separate intense rock from chill lofi "
        "because it combines genre, mood, energy, and acoustic preference."
    )

    for profile_name, user_prefs in USER_PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print_recommendations(profile_name, user_prefs, recommendations)


def print_recommendations(profile_name: str, user_prefs: dict, recommendations: list) -> None:
    print(f"\n{profile_name}")
    print(f"Preferences: {user_prefs}")
    print("Top Recommendations")
    print("=" * 60)

    for idx, rec in enumerate(recommendations, start=1):
        # Returned item format: (song, score, explanation)
        song, score, explanation = rec
        print(f"{idx}. {song['title']} by {song['artist']}")
        print(f"   Final Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split(", "):
            print(f"   - {reason}")
        print("-" * 60)


if __name__ == "__main__":
    main()
