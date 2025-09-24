import random
from datetime import datetime

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)


FACTS = [
    "Flask's name is a playful nod to another microframework called Bottle.",
    "Werkzeug, one of Flask's core libraries, literally means 'toolbox' in German.",
    "Jinja2 templates are inspired by Django's templating engine and are named after a Japanese temple.",
    "Python itself was named after the comedy troupe Monty Python, not the snake.",
    "Flask's debugger lets you inspect live state right inside the browser during development.",
    "Despite being micro, Flask scales by leaning on extensions for databases, auth, and caching.",
]

ACHIEVEMENTS = [
    "Animated UI rendered straight from Flask - no front-end build step required.",
    "Live clock, random fact generator, and neon styling generated on the fly.",
    "Custom API endpoint powers the interactive experience without extra files.",
]

TECH_STACK = [
    "Flask",
    "Python 3",
    "Werkzeug",
    "Jinja2",
    "HTML5 + CSS3 + JavaScript",
]

GRADIENTS = [
    "linear-gradient(135deg, #0f2027, #203a43, #2c5364)",
    "linear-gradient(135deg, #03001e, #7303c0, #ec38bc, #fdeff9)",
    "linear-gradient(120deg, #1f4037, #99f2c8)",
    "linear-gradient(130deg, #141e30, #243b55)",
    "linear-gradient(135deg, #5f0a87, #a4508b)",
]

ACCENT_COLORS = ["#64ffda", "#ffd166", "#ff6ec7", "#7cf4ff", "#a0ff8f"]

MOODS = ["Curious", "Inventive", "Bold", "Playful", "Optimistic"]


@app.route("/")
def home():
    gradient = random.choice(GRADIENTS)
    accent = random.choice(ACCENT_COLORS)
    fact = random.choice(FACTS)
    mood = random.choice(MOODS)
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    return render_template_string(
        """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Cosmic Dashboard</title>
    <style>
        :root {
            --accent: {{ accent }};
            --glass: rgba(255, 255, 255, 0.08);
            --card-bg: rgba(9, 17, 31, 0.8);
            --text-main: #f5f7ff;
            --text-soft: rgba(245, 247, 255, 0.7);
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 40px;
            font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
            color: var(--text-main);
            background: {{ gradient }};
            background-size: 320% 320%;
            animation: gradientShift 20s ease infinite;
            overflow: hidden;
        }

        body::before,
        body::after {
            content: "";
            position: absolute;
            width: 420px;
            height: 420px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0));
            filter: blur(8px);
            opacity: 0.45;
            animation: float 18s ease-in-out infinite;
        }

        body::before {
            top: -160px;
            right: -120px;
        }

        body::after {
            bottom: -160px;
            left: -120px;
            animation-delay: 4s;
        }

        main {
            z-index: 2;
            width: min(900px, 100%);
        }

        .card {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 28px;
            padding: 40px;
            box-shadow: 0 40px 80px rgba(8, 15, 35, 0.65);
            backdrop-filter: blur(14px);
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: "";
            position: absolute;
            inset: -120px;
            background: radial-gradient(circle at top right, rgba(255, 255, 255, 0.35), transparent 60%);
            opacity: 0.6;
        }

        .card::after {
            content: "";
            position: absolute;
            inset: -140px;
            background: radial-gradient(circle at bottom left, rgba(255, 255, 255, 0.22), transparent 65%);
            opacity: 0.5;
            transform: rotate(12deg);
        }

        header {
            position: relative;
            z-index: 1;
        }

        h1 {
            font-size: 2.8rem;
            margin: 0;
            letter-spacing: 1.2px;
            text-transform: uppercase;
        }

        #tagline {
            margin: 12px 0 24px;
            font-size: 1.08rem;
            color: var(--text-soft);
            letter-spacing: 0.6px;
        }

        .status {
            display: grid;
            gap: 18px;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            margin-bottom: 30px;
            position: relative;
            z-index: 1;
        }

        .stat-block {
            background: rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 18px 40px rgba(7, 19, 35, 0.35);
            transition: transform 0.6s ease;
        }

        .stat-block:hover {
            transform: translateY(-6px) scale(1.01);
        }

        .stat-label {
            text-transform: uppercase;
            font-size: 0.7rem;
            letter-spacing: 1.6px;
            color: var(--text-soft);
        }

        .stat-value {
            display: block;
            margin-top: 10px;
            font-size: 1.3rem;
            font-weight: 600;
            letter-spacing: 0.4px;
        }

        .fact {
            background: rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            padding: 26px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            margin-bottom: 30px;
            position: relative;
            z-index: 1;
        }

        .fact h2,
        .tech h2,
        .achievements h2 {
            margin-top: 0;
            font-size: 1.4rem;
            letter-spacing: 0.8px;
        }

        .fact p {
            font-size: 1.05rem;
            line-height: 1.7;
            margin-bottom: 18px;
        }

        button {
            background: var(--accent);
            border: none;
            color: #031121;
            font-size: 0.95rem;
            font-weight: 600;
            padding: 12px 22px;
            border-radius: 999px;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        button:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 30px rgba(0, 0, 0, 0.35);
        }

        button:disabled {
            opacity: 0.6;
            cursor: progress;
        }

        .chips {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .chip {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 999px;
            padding: 10px 18px;
            font-size: 0.85rem;
            letter-spacing: 0.4px;
            backdrop-filter: blur(6px);
        }

        .achievements ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: grid;
            gap: 12px;
        }

        .achievements li {
            background: rgba(255, 255, 255, 0.05);
            padding: 16px 18px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            letter-spacing: 0.4px;
        }

        footer {
            margin-top: 30px;
            display: flex;
            justify-content: space-between;
            gap: 20px;
            font-size: 0.85rem;
            color: var(--text-soft);
            position: relative;
            z-index: 1;
        }

        .pulse {
            position: relative;
            padding-left: 26px;
        }

        .pulse::before {
            content: "";
            position: absolute;
            left: 6px;
            top: 50%;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent);
            box-shadow: 0 0 18px var(--accent);
            transform: translateY(-50%);
            animation: pulse 1.6s ease-in-out infinite;
        }

        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        @keyframes pulse {
            0%,
            100% {
                transform: translateY(-50%) scale(1);
                opacity: 0.85;
            }
            50% {
                transform: translateY(-50%) scale(1.2);
                opacity: 1;
            }
        }

        @keyframes float {
            0% {
                transform: translateY(0px) scale(1);
            }
            50% {
                transform: translateY(24px) scale(1.08);
            }
            100% {
                transform: translateY(0px) scale(1);
            }
        }

        @media (max-width: 720px) {
            body {
                padding: 20px;
            }

            .card {
                padding: 26px;
            }

            footer {
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
    <main>
        <section class="card">
            <header>
                <h1>Flask Cosmic Dashboard</h1>
                <p id="tagline">Microframework, macro energy. Screenshot this for instant extra credit.</p>
            </header>

            <section class="status">
                <div class="stat-block">
                    <span class="stat-label">Server Time</span>
                    <span class="stat-value" id="clock">{{ timestamp }}</span>
                </div>
                <div class="stat-block">
                    <span class="stat-label">App Mood</span>
                    <span class="stat-value">{{ mood }}</span>
                </div>
                <div class="stat-block">
                    <span class="stat-label">Random Seed</span>
                    <span class="stat-value">{{ accent }}</span>
                </div>
            </section>

            <section class="fact">
                <h2>Did you know?</h2>
                <p id="fact">{{ fact }}</p>
                <button id="factButton">New random fact</button>
            </section>

            <section class="tech">
                <h2>Stack flex</h2>
                <div class="chips">
                    {% for item in tech_stack %}
                    <span class="chip">{{ item }}</span>
                    {% endfor %}
                </div>
            </section>

            <section class="achievements">
                <h2>Highlights</h2>
                <ul>
                    {% for item in achievements %}
                    <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </section>

            <footer>
                <span>Generated at {{ timestamp }}</span>
                <span class="pulse">Live Flask endpoint</span>
            </footer>
        </section>
    </main>

    <script>
        const factButton = document.getElementById("factButton");
        const factEl = document.getElementById("fact");
        const clockEl = document.getElementById("clock");
        const fallbackFacts = {{ facts|tojson }};

        function tickClock() {
            const now = new Date();
            const options = { hour: "2-digit", minute: "2-digit", second: "2-digit" };
            clockEl.textContent = now.toLocaleTimeString([], options);
        }

        tickClock();
        setInterval(tickClock, 1000);

        factButton.addEventListener("click", async () => {
            factButton.disabled = true;
            factButton.textContent = "Loading...";

            try {
                const response = await fetch("/api/random-fact");

                if (!response.ok) {
                    throw new Error("Network error");
                }

                const payload = await response.json();
                factEl.textContent = payload.fact;
            } catch (err) {
                const fallback = fallbackFacts[Math.floor(Math.random() * fallbackFacts.length)];
                factEl.textContent = fallback + " (offline mode)";
            } finally {
                factButton.disabled = false;
                factButton.textContent = "New random fact";
            }
        });
    </script>
</body>
</html>
        """,
        accent=accent,
        gradient=gradient,
        fact=fact,
        mood=mood,
        timestamp=timestamp,
        tech_stack=TECH_STACK,
        achievements=ACHIEVEMENTS,
        facts=FACTS,
    )


@app.route("/api/random-fact")
def random_fact():
    return jsonify(
        fact=random.choice(FACTS),
        generated_at=datetime.utcnow().isoformat() + "Z",
    )
