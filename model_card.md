# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

**Goal / Task:**  
This model suggests songs from a small catalog. It tries to find songs that match a user's genre, mood, energy, and acoustic preference.

**Intended Use:**  
This project is for classroom learning and simple demos. It is meant to show how a content-based recommender works.

**Non-Intended Use:**  
It should not be used for real music products. It should not be used to judge a person's full taste, mood, or identity.

---

## 3. How the Model Works

The model looks at each song one at a time. It checks whether the genre matches, whether the mood matches, and how close the song's energy is to the user's target. It also gives a small bonus if the song matches the user's acoustic preference. After that, it sorts all songs by score and returns the top results.

---

## 4. Data

The dataset has 18 songs. Each song has a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. I started with the 10-song starter file and added 8 more songs to make the catalog more varied. The data is still small, hand-written, and incomplete, so it misses a lot of real musical variety.

---

## 5. Strengths

The model works best for clear profiles like `Chill Lofi` and `Deep Intense Rock`. In those cases, the top songs usually feel close to the target vibe. The scoring is also easy to explain because every point comes from a simple rule.

---

## 6. Limitations and Bias

One problem is that energy can sometimes matter too much. In my edge-case test, a user asking for `classical` and `intense` still got loud songs like `Gym Hero` because the energy score was so strong. The model also treats genre labels as exact matches, so `pop` and `indie pop` do not help each other. The dataset is uneven too, so users with niche tastes have fewer good matches.

---

## 7. Evaluation

I tested four user profiles: `High-Energy Pop`, `Chill Lofi`, `Deep Intense Rock`, and a `Conflicted Edge Case`. I looked at the top 5 songs for each profile and asked whether the list felt right in plain language. I also ran one experiment where I doubled the energy weight and cut the genre weight in half. That experiment changed the rankings in a believable way, but it also made the system less strict about genre.

---

## 8. Future Work

- Add more songs and more balanced genre coverage.
- Use softer genre matching so similar labels can still help each other.
- Add more user preferences, like target valence or danceability.

---

## 9. Personal Reflection

My biggest learning moment was seeing how one song could rise for very different users just because a few numbers matched well. `Gym Hero` kept showing up because high energy and low acousticness gave it a strong score, even when the genre was not a perfect fit. That made the recommender feel smart at first, but it also showed me how easy it is for a simple rule to miss the bigger vibe.

AI tools helped me move faster when I was writing code, planning test profiles, and drafting explanations. They were most useful for giving me a starting point. I still had to double-check the imports, the math, and the actual rankings, because a suggestion can sound right while still producing a bad result.

What surprised me most is that a simple scoring system can still feel personal. Even without lyrics, history, or real user behavior, the top songs often looked like real recommendations. If I kept going, I would try fuzzy genre matching, more song data, and a way to reward variety so the same kind of track does not always win.
