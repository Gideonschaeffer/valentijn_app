import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Valentijnsverzoek 💘",
    page_icon="💌",
    layout="centered"
)

st.title("💘 Een belangrijke vraag...")
st.subheader("Wil je mijn Valentijn zijn? 🌹")
st.markdown("*(Nee zeggen is optioneel 😏)*")

# Echte JA-knop (Streamlit)
if st.button("Ja 💕"):
    st.balloons()
    st.success("YES!! 💖🥰 Beste Valentijn ooit!")
    st.write("Dit wordt iconisch 🍫✨")

st.write("")  # spacing

# Evil knop met JS (werkt op mobiel & desktop)
components.html(
    """
    <div id="container"
         style="
            height:180px;
            position:relative;
            width:100%;
            max-width:350px;
            margin:auto;
            border-radius:16px;
         ">

        <button id="trickBtn"
            style="
                position:absolute;
                left:35%;
                top:40%;
                padding:14px 28px;
                font-size:18px;
                border-radius:16px;
                border:none;
                background-color:#ff4b4b;
                color:white;
                cursor:pointer;
                transition: 0.15s;
            ">
            Nee 🙈
        </button>
    </div>

    <script>
        let count = 0;
        const btn = document.getElementById("trickBtn");
        const container = document.getElementById("container");

        function moveButton() {
            count++;

            if (count >= 5) {
                btn.innerText = "Ja 💕";
                btn.style.backgroundColor = "#ff69b4";
                btn.onclick = () => {
                    alert("🎉 Goede keuzes 
                😌💖");
                };
                return;
            }

            const maxX = container.clientWidth - btn.clientWidth;
            const maxY = container.clientHeight - btn.clientHeight;

            const randX = Math.random() * maxX;
            const randY = Math.random() * maxY;

            btn.style.left = randX + "px";
            btn.style.top = randY + "px";
        }

        // Desktop
        btn.addEventListener("mouseover", moveButton);

        // Mobiel
        btn.addEventListener("touchstart", moveButton);
    </script>
    """,
    height=220
)