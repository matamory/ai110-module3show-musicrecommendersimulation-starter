"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


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

    for profile_name, user_prefs in USER_PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nProfile: {profile_name}")
        print(f"Preferences: {user_prefs}")
        print("Top Recommendations")
        print("=" * 60)
        for idx, rec in enumerate(recommendations, start=1):
            # Returned item format: (song, score, explanation)
            song, score, explanation = rec
            print(f"{idx}. {song['title']} by {song['artist']}")
            print(f"   Final Score : {score:.2f}")
            print("   Reasons:")
            for reason in explanation.split(", "):
                print(f"   - {reason}")
            print("-" * 60)


if __name__ == "__main__":
    main()
