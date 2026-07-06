# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder Mini 1.0**

## 2. Goal / Task

This recommender suggests songs that match a user's taste profile.
It tries to rank songs the user will like next.

## 3. Data Used

The dataset has 28 songs.
Each song has genre, mood, energy, tempo, valence, danceability, and acousticness.
The data is small, so it does not cover every style or taste.

## 4. Algorithm Summary

The system gives points for genre matches and mood matches.
It also gives points for songs whose energy is close to the user's target energy.
Songs are ranked from highest score to lowest score.

## 5. Observed Behavior / Biases

The system can over-focus on energy.
That can create a filter bubble where similar-intensity songs keep showing up.
It can also miss good songs if their genre or mood label does not match exactly.

## 6. Evaluation Process

I tested a normal pop/happy profile, an adversarial sad-but-hyper profile, and an edge-case profile with out-of-range energy.
I also compared how rankings changed when I shifted the weights.
The surprise was that energy could overpower mood when the profile was unusual.

### High-Energy Pop

```text
High-Energy Pop
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9, 'likes_acoustic': False}
Top Recommendations
============================================================
1. Dynamite by BTS
	Final Score: 5.37
	Reasons:
	- genre match (+2.0)
	- mood match (+1.0)
	- energy closeness (+1.92)
	- non-acoustic fit (+0.45)
------------------------------------------------------------
2. Sunrise City by Neon Echo
	Final Score: 5.25
	Reasons:
	- genre match (+2.0)
	- mood match (+1.0)
	- energy closeness (+1.84)
	- non-acoustic fit (+0.41)
------------------------------------------------------------
3. Gym Hero by Max Pulse
	Final Score: 4.42
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.94)
	- non-acoustic fit (+0.47)
------------------------------------------------------------
4. Permission to Dance by BTS
	Final Score: 4.38
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.94)
	- non-acoustic fit (+0.45)
------------------------------------------------------------
5. Butter by BTS
	Final Score: 4.34
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.88)
	- non-acoustic fit (+0.46)
------------------------------------------------------------
```

### Adversarial: Sad But Hyper

```text
Adversarial: Sad But Hyper
Preferences: {'genre': 'pop', 'mood': 'sad', 'energy': 0.9, 'likes_acoustic': True}
Top Recommendations
============================================================
1. Permission to Dance by BTS
	Final Score: 4.00
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.94)
	- acoustic fit (+0.06)
------------------------------------------------------------
2. Dynamite by BTS
	Final Score: 3.97
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.92)
	- acoustic fit (+0.05)
------------------------------------------------------------
3. Gym Hero by Max Pulse
	Final Score: 3.96
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.94)
	- acoustic fit (+0.03)
------------------------------------------------------------
4. Sunrise City by Neon Echo
	Final Score: 3.93
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.84)
	- acoustic fit (+0.09)
------------------------------------------------------------
5. Butter by BTS
	Final Score: 3.92
	Reasons:
	- genre match (+2.0)
	- energy closeness (+1.88)
	- acoustic fit (+0.04)
------------------------------------------------------------
```

### Edge Case: Energy Out Of Range

```text
Edge Case: Energy Out Of Range
Preferences: {'genre': 'edm', 'mood': 'happy', 'energy': 1.5, 'likes_acoustic': False}
Top Recommendations
============================================================
1. Dynamite by BTS
	Final Score: 2.17
	Reasons:
	- mood match (+1.0)
	- energy closeness (+0.72)
	- non-acoustic fit (+0.45)
------------------------------------------------------------
2. Sunrise City by Neon Echo
	Final Score: 2.05
	Reasons:
	- mood match (+1.0)
	- energy closeness (+0.64)
	- non-acoustic fit (+0.41)
------------------------------------------------------------
3. Rooftop Lights by Indigo Parade
	Final Score: 1.84
	Reasons:
	- mood match (+1.0)
	- energy closeness (+0.52)
	- non-acoustic fit (+0.33)
------------------------------------------------------------
4. Idol by BTS
	Final Score: 1.38
	Reasons:
	- energy closeness (+0.90)
	- non-acoustic fit (+0.47)
------------------------------------------------------------
5. Steel Horizon by Iron Vale
	Final Score: 1.37
	Reasons:
	- energy closeness (+0.90)
	- non-acoustic fit (+0.47)
------------------------------------------------------------
```

The normal profile looked the most balanced.
The adversarial and edge-case profiles showed that energy can push the ranking hard.

## 7. Intended Use and Non-Intended Use

This system is meant for learning and small demos.
It is not meant for real product personalization or high-stakes decisions.

## 8. Ideas for Improvement

I would add more features like tempo and valence.
I would make the score less sensitive to extreme energy values.
I would add a diversity rule so the top results are less repetitive.

## 9. Personal Reflection

My biggest learning moment was seeing how a small weight change can change the whole ranking.
AI tools helped me move faster, but I still had to check the outputs carefully.
I was surprised that a simple score formula can still feel like a real recommender.
If I kept going, I would test more profiles and tune the weights with feedback.
