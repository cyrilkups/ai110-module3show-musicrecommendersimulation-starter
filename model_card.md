# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

One weakness I found is that the recommender can be pulled too strongly by energy closeness, especially when a user has conflicting preferences. In my edge-case test, a profile asking for `classical`, `intense`, `0.95` energy, and acoustic sound still got `Gym Hero` and `Storm Runner` at the top because the model rewarded high energy and the `intense` mood even when the genre did not match. The exact-match genre rule also ignores near neighbors like `pop` and `indie pop`, so similar songs can lose points for small label differences. The catalog is also uneven, with only one rock song and one classical song, so users with niche tastes have fewer good options and may get pushed toward louder mainstream tracks. This creates a small filter bubble where certain combinations of energy and mood keep winning even when the overall vibe is not quite right.

---

## 7. Evaluation  

I tested four user profiles: `High-Energy Pop`, `Chill Lofi`, `Deep Intense Rock`, and a `Conflicted Edge Case` that mixed classical genre with intense mood and very high energy. For each one, I looked at the top 5 recommendations and checked whether the titles felt like a believable match for the vibe in plain language, not just by the numbers. The strongest results were for `Chill Lofi`, where `Library Rain`, `Midnight Coding`, and `Focus Flow` all felt consistent with a calm, acoustic, low-energy study playlist. One surprise was that `Gym Hero` ranked second for the rock profile because its energy and mood matched so well that the pop genre penalty was not enough to push it down. I also ran an experiment that doubled energy weight and halved genre weight; this moved `Rooftop Lights` above `Gym Hero` for the high-energy pop profile, which made the list feel happier but less strict about genre identity.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
