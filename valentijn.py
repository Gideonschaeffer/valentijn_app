import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Valentijnsverzoek 💘",
    page_icon="💌",
    layout="centered"
)

# Alle tekst roze maken
st.markdown(
    """
    <style>
        html, body, [class*="css"]  {
            color: #ff69b4 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("hihi ik heb een vraagje")
st.subheader("Wil je mijn Valentijn zijn? 🌹")

components.html(
    """
    <div style="text-align:center; color:#ff69b4;">

        <div id="container"
            style="
                position: relative;
                width: 100%;
                max-width: 360px;
                height: 200px;
                margin: 20px auto;
                overflow: hidden;
                border-radius: 20px;
            ">

            <!-- JA KNOP -->
            <button id="jaBtn"
                style="
                    position: absolute;
                    left: 25%;
                    top: 50%;
                    transform: translate(-50%, -50%) scale(1);
                    padding: 14px 30px;
                    font-size: 18px;
                    border-radius: 18px;
                    border: none;
                    background-color: #ff69b4;
                    color: white;
                    cursor: pointer;
                    transition: transform 0.2s ease;
                ">
                Ja 💕
            </button>

            <!-- NEE KNOP -->
            <button id="neeBtn"
                style="
                    position: absolute;
                    left: 75%;
                    top: 50%;
                    transform: translate(-50%, -50%);
                    padding: 14px 30px;
                    font-size: 18px;
                    border-radius: 18px;
                    border: none;
                    background-color: #ff4b4b;
                    color: white;
                    cursor: pointer;
                    user-select: none;
                ">
                Nee
            </button>
        </div>

        <h3 id="result" style="color:#ff69b4;"></h3>
    </div>

    <script>
        let count = 0;
        const neeBtn = document.getElementById("neeBtn");
        const jaBtn = document.getElementById("jaBtn");
        const result = document.getElementById("result");
        const container = document.getElementById("container");

        function moveNee() {
            count++;

            // Ja knop groter maken
            jaBtn.style.transform = "translate(-50%, -50%) scale(" + (1 + count * 0.15) + ")";

            // Na 5 keer verdwijnt Nee knop
            if (count >= 5) {
                neeBtn.style.display = "none";
                return;
            }

            const maxX = container.clientWidth - neeBtn.offsetWidth;
            const maxY = container.clientHeight - neeBtn.offsetHeight;

            neeBtn.style.left = Math.random() * maxX + "px";
            neeBtn.style.top = Math.random() * maxY + "px";
            neeBtn.style.transform = "none";
        }

        function sayYes() {
            result.innerHTML = "💖 OMGG jaaaa nu ben ik happyyyy.💖";
            confetti();
        }

        function confetti() {
            for (let i = 0; i < 30; i++) {
                const heart = document.createElement("div");
                heart.innerHTML = "💖";
                heart.style.position = "fixed";
                heart.style.left = Math.random() * 100 + "vw";
                heart.style.top = "-20px";
                heart.style.fontSize = "24px";
                heart.style.animation = "fall 3s linear";
                document.body.appendChild(heart);

                setTimeout(() => heart.remove(), 3000);
            }
        }

        neeBtn.addEventListener("pointerenter", moveNee);
        neeBtn.addEventListener("pointerdown", moveNee);
        jaBtn.onclick = sayYes;
    </script>

    <style>
        @keyframes fall {
            to {
                transform: translateY(110vh);
                opacity: 0;
            }
        }
    </style>
    """,
    height=320
)
