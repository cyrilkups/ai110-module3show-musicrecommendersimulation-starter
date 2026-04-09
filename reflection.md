# Reflection Notes

## Pairwise Profile Comparisons

- `High-Energy Pop` vs `Chill Lofi`: the pop profile pushed bright, upbeat songs like `Sunrise City` and `Gym Hero` to the top, while the lofi profile switched hard toward softer tracks like `Library Rain` and `Midnight Coding`. That makes sense because the energy target drops from `0.85` to `0.35`, and the acoustic preference flips from `False` to `True`.

- `High-Energy Pop` vs `Deep Intense Rock`: both profiles liked energetic songs, so tracks like `Gym Hero` stayed high in both lists. The difference is that the rock profile rewarded the `intense` mood enough for `Storm Runner` to take first place, while the pop profile kept `Sunrise City` at the top because it matched both `pop` and `happy`.

- `Chill Lofi` vs `Deep Intense Rock`: these profiles produced the clearest contrast in the whole project. The lofi profile favored quiet, acoustic songs with study vibes, while the rock profile preferred loud, low-acoustic tracks with near-maximum energy. In plain language, one profile is asking for background focus music and the other is asking for adrenaline.

## Edge-Case Note

- The `Conflicted Edge Case` profile showed the system's biggest weakness. Even though it asked for `classical`, the top results were `Gym Hero` and `Storm Runner` because the scoring rule cared more about `intense` mood and high energy than about finding a truly classical track. This is a good reminder that a recommender can look reasonable in simple cases but still behave oddly when the user wants a rare combination.
