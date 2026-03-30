# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch Mini 1.0**

---

## 2. Intended Use  

This system suggests 5 songs from a small list based on user taste.
It assumes users can describe genre, mood, energy, and acoustic preference.
It is for classroom learning, not real product use.

Non-intended use: It should not be used for high-stakes decisions or real user personalization at scale.

---

## 3. How the Model Works  

Each song gets points for matching the user's genre and mood.
It also gets points for how close its energy is to the user's target energy.
It adds a small bonus for acoustic or non-acoustic fit.
I changed weights so energy matters more and genre matters less.

---

## 4. Data  

The catalog has 18 songs.
It includes genres like pop, lofi, rock, jazz, country, and others.
It includes moods like happy, chill, intense, nostalgic, and more.
The dataset is tiny, so many styles and user contexts are missing.

---

## 5. Strengths  

It works well when the user has a clear energy target.
It also works well for Chill Lofi and Deep Intense Rock profiles.
Top results often feel reasonable when mood and energy align.

---

## 6. Limitations and Bias 

The model over-prioritizes energy and can repeat similar-intensity songs.
This can create a filter bubble.
If energy input is out of range, many songs get very low energy points.
Exact label matching can miss close genre or mood matches.

---

## 7. Evaluation  

I tested High-Energy Pop, Chill Lofi, Deep Intense Rock, and adversarial profiles.
I compared top-5 lists before and after changing weights.
I also tested edge inputs like out-of-range energy.
A surprise was how often Gym Hero appeared for Happy Pop requests.

---

## 8. Future Work  

Add more features, like tempo and valence.
Clamp or normalize user energy to prevent edge-case distortions.
Add a diversity rule so top results are not all the same style.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how one weight change can shift many rankings.
AI tools helped me move faster, especially for experiments and quick comparisons.
I still had to double-check outputs to make sure the logic matched my intent.
I was surprised that a simple score formula can still feel like a real recommendation system.
If I extend this project, I would test more users, add diversity controls, and tune weights with feedback.
