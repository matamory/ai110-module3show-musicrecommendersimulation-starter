import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        ranked = sorted(
            self.songs,
            key=lambda song: score_song(
                user_prefs,
                {
                    "genre": song.genre,
                    "mood": song.mood,
                    "energy": song.energy,
                    "acousticness": song.acousticness,
                },
            )[0],
            reverse=True,
        )
        return ranked[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        score, reasons = score_song(
            user_prefs,
            {
                "genre": song.genre,
                "mood": song.mood,
                "energy": song.energy,
                "acousticness": song.acousticness,
            },
        )
        return f"Score {score:.2f}: {', '.join(reasons)}"

def load_songs(csv_path: str) -> List[Dict[str, object]]:
    """Load songs from a CSV file into a list of dictionaries with numeric fields parsed."""
    songs: List[Dict[str, object]] = []

    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness"}

    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song: Dict[str, object] = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a numeric score and reason list for one song given user preferences."""
    score = 0.0
    reasons: List[str] = []

    # Genre is a strong exact-match signal.
    pref_genre = str(user_prefs.get("genre", "")).strip().lower()
    song_genre = str(song.get("genre", "")).strip().lower()
    if pref_genre and song_genre == pref_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood is a smaller exact-match signal.
    pref_mood = str(user_prefs.get("mood", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()
    if pref_mood and song_mood == pref_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Reward numeric closeness to target energy, not high/low direction.
    target_energy = float(user_prefs.get("energy", 0.5))
    song_energy = float(song.get("energy", 0.0))
    energy_similarity = max(0.0, 1.0 - abs(song_energy - target_energy))
    energy_points = 2.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    # Optional: include acoustic preference if provided by the caller.
    likes_acoustic = user_prefs.get("likes_acoustic")
    if isinstance(likes_acoustic, bool):
        acousticness = float(song.get("acousticness", 0.0))
        acoustic_alignment = acousticness if likes_acoustic else (1.0 - acousticness)
        acoustic_points = 0.5 * acoustic_alignment
        score += acoustic_points
        preference_label = "acoustic" if likes_acoustic else "non-acoustic"
        reasons.append(f"{preference_label} fit (+{acoustic_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort by descending score, and return the top-k recommendations."""

    if k <= 0:
        return []

    scored_songs = [
        (song, score, reasons)
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)

    return [
        (song, score, ", ".join(reasons))
        for song, score, reasons in ranked_songs[:k]
    ]
