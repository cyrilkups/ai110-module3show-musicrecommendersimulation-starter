import csv
from typing import List, Dict, Tuple
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
        """Return the top-k songs sorted by match score for one user."""
        scored_songs = []
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        for song in self.songs:
            score, _ = score_song(user_prefs, _song_to_dict(song))
            scored_songs.append((score, song))

        scored_songs.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Summarize why one song matches the user's profile."""
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_prefs, _song_to_dict(song))
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and convert numeric fields to usable types."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song and explain the feature matches behind the score."""
    prefs = _normalize_user_prefs(user_prefs)
    score = 0.0
    reasons = []

    if song["genre"] == prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == prefs["favorite_mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_score = max(0.0, 2.0 * (1 - abs(song["energy"] - prefs["target_energy"])))
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    acousticness = song["acousticness"]
    if prefs["likes_acoustic"]:
        acoustic_score = 0.5 * acousticness
        reasons.append(f"acoustic preference (+{acoustic_score:.2f})")
    else:
        acoustic_score = 0.5 * (1 - acousticness)
        reasons.append(f"less-acoustic preference (+{acoustic_score:.2f})")
    score += acoustic_score

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score the catalog, rank it, and return the top-k recommendations."""
    scored_recommendations = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_recommendations.append((song, score, explanation))

    ranked_recommendations = sorted(
        scored_recommendations,
        key=lambda item: item[1],
        reverse=True,
    )
    return ranked_recommendations[:k]


def _normalize_user_prefs(user_prefs: Dict) -> Dict:
    """Support both starter keys and expanded profile keys for preferences."""
    return {
        "favorite_genre": user_prefs.get("favorite_genre", user_prefs.get("genre", "")),
        "favorite_mood": user_prefs.get("favorite_mood", user_prefs.get("mood", "")),
        "target_energy": float(user_prefs.get("target_energy", user_prefs.get("energy", 0.5))),
        "likes_acoustic": bool(user_prefs.get("likes_acoustic", user_prefs.get("acousticness", True))),
    }


def _song_to_dict(song: Song) -> Dict:
    """Convert a Song object into the dict format used by the functional API."""
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }
