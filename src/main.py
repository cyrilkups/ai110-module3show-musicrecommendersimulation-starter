"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import DEFAULT_SCORING_WEIGHTS, load_songs, recommend_songs


EVALUATION_PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.85,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "likes_acoustic": False,
    },
    "Conflicted Edge Case": {
        "favorite_genre": "classical",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "likes_acoustic": True,
    },
}

ENERGY_HEAVY_EXPERIMENT = {
    **DEFAULT_SCORING_WEIGHTS,
    "genre": 1.0,
    "energy": 4.0,
}


def print_profile_report(name: str, prefs: dict, recommendations: list) -> None:
    """Print one recommendation block in a readable terminal format."""
    print(f"\n=== {name} ===")
    print(
        "Profile:"
        f" genre={prefs['favorite_genre']},"
        f" mood={prefs['favorite_mood']},"
        f" energy={prefs['target_energy']:.2f},"
        f" likes_acoustic={prefs['likes_acoustic']}"
    )
    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Why:   {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print("\nBaseline recommendation runs:")

    for name, prefs in EVALUATION_PROFILES.items():
        recommendations = recommend_songs(prefs, songs, k=5)
        print_profile_report(name, prefs, recommendations)

    experiment_profile_name = "High-Energy Pop"
    experiment_prefs = EVALUATION_PROFILES[experiment_profile_name]
    experiment_recommendations = recommend_songs(
        experiment_prefs,
        songs,
        k=5,
        weights=ENERGY_HEAVY_EXPERIMENT,
    )
    print("\nExperiment: double energy weight and halve genre weight.")
    print_profile_report(
        f"{experiment_profile_name} (Energy-Heavy Experiment)",
        experiment_prefs,
        experiment_recommendations,
    )


if __name__ == "__main__":
    main()
