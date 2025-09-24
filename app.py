import random
from datetime import datetime

from flask import Flask, render_template_string

app = Flask(__name__)


RICK_GIFS = [
    "https://media.giphy.com/media/Vuw9m5wXviFIQ/giphy.gif",
    "https://media.giphy.com/media/GR2bO75ZtH2wI/giphy.gif",
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    "https://media.giphy.com/media/LHZyixOnHwDDy/giphy.gif",
    "https://media.giphy.com/media/fqTuThV8cqqNa/giphy.gif",
]

BACKDROPS = [
    "linear-gradient(135deg, #091236, #1E215D, #5D2F90)",
    "linear-gradient(140deg, #1b2735, #090a0f, #1f4037)",
    "linear-gradient(135deg, #0f0c29, #302b63, #24243e)",
    "linear-gradient(135deg, #360033, #0b8793)",
    "linear-gradient(120deg, #3a1c71, #d76d77, #ffaf7b)",
]

NEON_COLORS = ["#ff4ecd", "#48e0ff", "#ffe066", "#7cf57d", "#ff9671"]

STAGE_TITLES = [
    "Neon Roller Rink",
    "Infinite Rick Loop",
    "Retro Wave Lounge",
    "Pixel Disco Dome",
    "Turbo Groove Atrium",
]

LYRIC_SNIPPETS = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around",
    "Never gonna desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
]

CLONE_COUNT = 15


def build_clones(count):
    clones = []
    for index in range(count):
        clones.append(
            {
                "gif": random.choice(RICK_GIFS),
                "delay": round(index * 0.12, 2),
                "scale": round(random.uniform(0.75, 1.25), 2),
                "hue": random.randint(-30, 30),
                "offset": random.randint(-18, 18),
            }
        )
    return clones


@app.route("/")
def dance_floor():
    gradient = random.choice(BACKDROPS)
    accent = random.choice(NEON_COLORS)
    stage_name = random.choice(STAGE_TITLES)
    clones = build_clones(CLONE_COUNT)
    lyric_choices = random.sample(LYRIC_SNIPPETS, k=min(4, len(LYRIC_SNIPPETS)))

    return render_template_string(
        """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ultimate Rick Roll Stage</title>
    <style>
        :root {
            --accent: {{ accent }};
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
            color: #fdfdfd;
            background: {{ gradient }};
            background-size: 280% 280%;
            animation: gradient-shift 18s ease infinite;
            overflow: hidden;
        }

        body::before,
        body::after {
            content: "";
            position: absolute;
            width: 520px;
            height: 520px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0));
            filter: blur(12px);
            opacity: 0.35;
            animation: float 22s ease-in-out infinite;
        }

        body::before {
            top: -200px;
            right: -160px;
        }

        body::after {
            bottom: -220px;
            left: -140px;
            animation-delay: 5s;
        }

        main {
            position: relative;
            z-index: 2;
            width: min(1100px, 100%);
            display: flex;
            flex-direction: column;
            gap: 34px;
        }

        .hero {
            background: rgba(4, 12, 28, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 32px;
            padding: 32px;
            backdrop-filter: blur(18px);
            box-shadow: 0 45px 85px rgba(7, 10, 30, 0.7);
        }

        h1 {
            margin: 0;
            font-size: 3rem;
            letter-spacing: 1px;
            text-transform: uppercase;
            text-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        }

        #tagline {
            margin: 16px 0 24px;
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.75);
            letter-spacing: 0.6px;
        }

        .ticker {
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            margin-bottom: 24px;
        }

        .ticker span {
            padding: 10px 18px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.25);
            font-size: 0.95rem;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            animation: pop 2.4s ease-in-out infinite;
        }

        .ticker span:nth-child(odd) {
            animation-delay: 0.6s;
        }

        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            align-items: center;
        }

        .badge {
            padding: 10px 16px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.16);
            letter-spacing: 0.4px;
            font-weight: 600;
        }

        button {
            background: var(--accent);
            color: #050505;
            border: none;
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: 0.6px;
            padding: 12px 26px;
            border-radius: 999px;
            cursor: pointer;
            box-shadow: 0 18px 30px rgba(0, 0, 0, 0.35);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        button:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 24px 38px rgba(0, 0, 0, 0.4);
        }

        button:disabled {
            opacity: 0.7;
            cursor: progress;
        }

        .timestamp {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.68);
            letter-spacing: 0.4px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 24px;
        }

        .clone {
            position: relative;
            height: 260px;
            border-radius: 22px;
            overflow: hidden;
            border: 2px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 28px 60px rgba(3, 6, 20, 0.65);
            background-size: cover;
            background-position: center;
            animation: bounce 1.9s ease-in-out infinite;
            animation-delay: var(--delay);
            transform: translateX(var(--offset)) scale(var(--scale));
            filter: hue-rotate(var(--hue));
        }

        .clone::before {
            content: "";
            position: absolute;
            inset: -40% -30%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.35), transparent 70%);
            opacity: 0.6;
            animation: shimmer 2.8s linear infinite;
        }

        .clone::after {
            content: "Rick Roll";
            position: absolute;
            left: 16px;
            bottom: 16px;
            padding: 6px 12px;
            border-radius: 999px;
            background: rgba(0, 0, 0, 0.55);
            font-size: 0.82rem;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        .video {
            background: rgba(4, 12, 28, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 28px;
            padding: 24px;
            backdrop-filter: blur(18px);
            box-shadow: 0 38px 70px rgba(6, 10, 26, 0.6);
        }

        .video p {
            margin: 0 0 18px;
            color: rgba(255, 255, 255, 0.76);
            letter-spacing: 0.4px;
        }

        iframe {
            width: 100%;
            aspect-ratio: 16 / 9;
            border: none;
            border-radius: 20px;
            background: rgba(0, 0, 0, 0.4);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
        }

        @keyframes gradient-shift {
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

        @keyframes float {
            0%,
            100% {
                transform: translateY(0px) scale(1);
            }
            50% {
                transform: translateY(26px) scale(1.06);
            }
        }

        @keyframes pop {
            0%,
            100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-6px);
            }
        }

        @keyframes bounce {
            0%,
            100% {
                transform: translateX(var(--offset)) scale(var(--scale));
            }
            50% {
                transform: translateX(calc(var(--offset) * -1)) scale(calc(var(--scale) + 0.08));
            }
        }

        @keyframes shimmer {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }

        @media (max-width: 780px) {
            body {
                padding: 24px;
            }

            h1 {
                font-size: 2.2rem;
            }

            .clone {
                height: 220px;
            }
        }
    </style>
</head>
<body>
    <main>
        <section class="hero">
            <h1>Rick Roll Arena</h1>
            <p id="tagline">{{ stage }} is live. The clones are never gonna give you up.</p>
            <div class="ticker">
                {% for line in lyrics %}
                <span>{{ line }}</span>
                {% endfor %}
            </div>
            <div class="controls">
                <div class="badge">Stage: {{ stage }}</div>
                <button id="anthemButton">Launch the anthem</button>
                <span class="timestamp">Synced at {{ timestamp }}</span>
            </div>
        </section>

        <section class="grid">
            {% for clone in clones %}
            <div
                class="clone"
                style="--delay: {{ clone.delay }}s; --scale: {{ clone.scale }}; --hue: {{ clone.hue }}deg; --offset: {{ clone.offset }}px; background-image: url('{{ clone.gif }}');"
            ></div>
            {% endfor %}
        </section>

        <section class="video">
            <p>Optional bonus: fire up the original track and let the squad dance in sync.</p>
            <iframe
                id="anthemFrame"
                data-base="{{ video_base }}"
                src="about:blank"
                title="Rick Astley - Never Gonna Give You Up"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
            ></iframe>
        </section>
    </main>

    <script>
        const button = document.getElementById("anthemButton");
        const frame = document.getElementById("anthemFrame");

        button.addEventListener("click", () => {
            frame.src = frame.dataset.base + "&autoplay=1";
            button.disabled = true;
            button.textContent = "Anthem playing...";
        });
    </script>
</body>
</html>
        """,
        accent=accent,
        gradient=gradient,
        stage=stage_name,
        lyrics=lyric_choices,
        clones=clones,
        timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        video_base="https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ?rel=0&modestbranding=1&start=8",
    )


if __name__ == "__main__":
    app.run(debug=True)
