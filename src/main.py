"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import sys
from textwrap import wrap

from src.recommender import MODE_CONFIGS, available_modes, get_mode_label, load_songs, recommend_songs


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

TABLE_COLUMNS = (
    ("#", 3),
    ("Song", 20),
    ("Artist", 16),
    ("Genre", 12),
    ("Score", 8),
    ("Reasons", 64),
)


def _format_profile_summary(prefs: dict) -> str:
    return (
        f"genre={prefs['favorite_genre']}, "
        f"mood={prefs['favorite_mood']}, "
        f"energy={prefs['target_energy']:.2f}, "
        f"likes_acoustic={prefs['likes_acoustic']}"
    )


def _wrap_cell(value: str, width: int) -> list[str]:
    text = "" if value is None else str(value)
    lines = []
    for raw_line in text.splitlines() or [""]:
        wrapped = wrap(raw_line, width=width) or [""]
        lines.extend(wrapped)
    return lines or [""]


def _format_table(rows: list[dict]) -> str:
    header = "| " + " | ".join(label.ljust(width) for label, width in TABLE_COLUMNS) + " |"
    separator = "+-" + "-+-".join("-" * width for _, width in TABLE_COLUMNS) + "-+"
    table_lines = [separator, header, separator]

    for row in rows:
        cell_lines = [
            _wrap_cell(str(row.get(key, "")), width)
            for key, width in (
                ("rank", TABLE_COLUMNS[0][1]),
                ("song", TABLE_COLUMNS[1][1]),
                ("artist", TABLE_COLUMNS[2][1]),
                ("genre", TABLE_COLUMNS[3][1]),
                ("score", TABLE_COLUMNS[4][1]),
                ("reasons", TABLE_COLUMNS[5][1]),
            )
        ]
        row_height = max(len(lines) for lines in cell_lines)
        for line_index in range(row_height):
            rendered_cells = []
            for lines, (_, width) in zip(cell_lines, TABLE_COLUMNS):
                rendered_cells.append(lines[line_index].ljust(width) if line_index < len(lines) else " " * width)
            table_lines.append("| " + " | ".join(rendered_cells) + " |")
        table_lines.append(separator)

    return "\n".join(table_lines)


def _build_table_rows(recommendations: list) -> list[dict]:
    rows = []
    for index, (song, score, explanation) in enumerate(recommendations, start=1):
        rows.append(
            {
                "rank": index,
                "song": song["title"],
                "artist": song["artist"],
                "genre": song["genre"],
                "score": f"{score:.2f}",
                "reasons": explanation,
            }
        )
    return rows


def _normalize_mode_input(raw_mode: str) -> str:
    normalized = (raw_mode or "balanced").strip().lower().replace("-", "_")
    return normalized if normalized in MODE_CONFIGS else "balanced"


def _parse_runtime_options(argv: list[str]) -> tuple[list[str], bool]:
    args = argv[1:]
    diversity = "--no-diversity" not in args
    filtered_args = [arg for arg in args if arg != "--no-diversity"]

    if not filtered_args:
        return ["balanced"], diversity
    if filtered_args[0].lower() == "all":
        return list(available_modes()), diversity
    return [_normalize_mode_input(filtered_args[0])], diversity


def print_profile_report(name: str, prefs: dict, recommendations: list, mode: str, diversity: bool) -> None:
    """Print one recommendation block in a readable terminal format."""
    print(f"\n=== {name} | Mode: {get_mode_label(mode)} ===")
    print(f"Profile: {_format_profile_summary(prefs)}")
    print(f"Diversity penalty: {'on' if diversity else 'off'}")
    print(_format_table(_build_table_rows(recommendations)))


def run_mode(mode: str, diversity: bool, songs: list[dict]) -> None:
    print(f"\nRecommendation runs for mode: {get_mode_label(mode)}")
    for name, prefs in EVALUATION_PROFILES.items():
        recommendations = recommend_songs(
            prefs,
            songs,
            k=5,
            mode=mode,
            diversity=diversity,
        )
        print_profile_report(name, prefs, recommendations, mode=mode, diversity=diversity)


def main() -> None:
    modes, diversity = _parse_runtime_options(sys.argv)
    songs = load_songs("data/songs.csv")
    print(f"Available modes: {', '.join(available_modes())}")
    print("Usage: python -m src.main [mode|all] [--no-diversity]")
    for mode in modes:
        run_mode(mode, diversity=diversity, songs=songs)


if __name__ == "__main__":
    main()
