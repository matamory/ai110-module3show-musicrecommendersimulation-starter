# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommendation systems (like Spotify or YouTube) usually combine behavior signals from similar users with content signals from each song, then rank items by how well they match a listener's taste and current context. In this simulation, we prioritize a transparent content-based approach: each song is scored by how closely its attributes match a user's stated preferences, then the top-scoring songs are recommended.

### Features Used In This Simulation

Song features (`Song` object):

- `id`
- `title`
- `artist`
- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

User preference features (`UserProfile` object):

- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `likes_acoustic`

### Algorithm Plan (Data Flow)

1. Input (User Preferences)
- Accept a user profile with target taste values (genre, mood, energy preference, and acoustic preference).

2. Process (Scoring Loop)
- Load all songs from `data/songs.csv`.
- Loop through each song and compute a total score using weighted feature rules.
- Categorical scoring:
   - Genre match adds points.
   - Mood match adds points.
- Numeric scoring:
   - Reward closeness to the user's target energy using a distance-based rule.
   - Example: `energy_score = 1 - abs(song_energy - target_energy)` (clipped to `[0, 1]`).
- Optional acoustic preference:
   - If user likes acoustic songs, reward higher acousticness.
   - If not, reward lower acousticness.
- Save `(song, score, explanation)` for each song.

3. Output (Ranking)
- Sort all scored songs from highest to lowest score.
- Return the Top K songs as recommendations.
- Provide short explanations showing why each top song matched.

### Suggested Starting Weights

- Mood match: `0.30`
- Genre match: `0.20`
- Energy closeness: `0.25`
- Acoustic preference alignment: `0.25`

These weights are a starting point and can be tuned after testing with different user profiles.

### Potential Biases To Watch

- This system may over-prioritize exact genre or mood labels and miss songs that are a strong numeric match but tagged differently.
- A single target energy value can bias recommendations toward one listening context (for example study mode) and under-serve other contexts (for example workouts).
- The small song catalog can make results feel repetitive and may not represent diverse musical tastes.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

### Terminal Output Screenshot

This is the formatted terminal output from running:

```bash
python -m src.main
```

![Terminal Output](terminal_output_screenshot.png)

### Screenshots 1-6

| Screenshot 1 | Screenshot 2 |
|---|---|
| ![Screenshot 1](screenshot1.png) | ![Screenshot 2](screenshot2.png) |

| Screenshot 3 | Screenshot 4 |
|---|---|
| ![Screenshot 3](screenshot3.png) | ![Screenshot 4](screenshot4.png) |

| Screenshot 5 | Screenshot 6 |
|---|---|
| ![Screenshot 5](screenshot5.png) | ![Screenshot 6](screenshot6.png) |

Sample output:

```text
Loaded songs: 18

Top Recommendations
============================================================
1. Sunrise City by Neon Echo
   Final Score : 9.90
   Reasons:
   - genre match (+2.0)
   - mood match (+3.0)
   - energy closeness (+4.90)
------------------------------------------------------------
2. Rooftop Lights by Indigo Parade
   Final Score : 7.80
   Reasons:
   - mood match (+3.0)
   - energy closeness (+4.80)
------------------------------------------------------------
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

