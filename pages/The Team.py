import streamlit as st
import streamlit.components.v1 as components
import base64

# Function to encode images as base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"

# Team members and their images
team_members = [
    {"name": "Priyanka M", "image": "images/team/Priyanka M.jpg", "github": "https://github.com/Priyankagithub2004"},
    {"name": "Prajwal M", "image": "images/team/Prajwal.jpg", "github": "https://github.com/Prajwal590"},
    {"name": "Raju S B", "image": "images/team/Raju S B.jpg", "github": "https://github.com/RAJUS248"},
    {"name": "Kartik G", "image": "images/team/Kartik G.jpg", "github": "https://github.com/Kartik-Galgali"},
]

# Generate HTML for slides
slides_html = ""
for member in team_members:
    base64_img = get_base64_image(member["image"])
    slides_html += f"""
    <div class="swiper-slide">
        <div class="card">
            <img src="{base64_img}" />
            <div class="overlay">
                <h4>{member['name']}</h4>
                <a href="{member['github']}" target="_blank">GitHub</a>
            </div>
        </div>
    </div>
    """

# Final HTML with Swiper
swiper_html = f"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

<style>
.swiper {{
  width: 100%;
  padding-top: 50px;
  padding-bottom: 50px;
}}

.swiper-slide {{
  width: 160px;
  height: 260px;
  background: #000;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
}}

.card {{
  width: 100%;
  height: 100%;
  position: relative;
  border-radius: 10px;
  overflow: hidden;
}}

.card img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}}

.overlay {{
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 10px 5px;
  background: rgba(0, 0, 0, 0.6);
  color: #fff;
  text-align: center;
}}

.overlay h4 {{
  margin: 5px 0;
  font-size: 14px;
}}

.overlay a {{
  color: #00acee;
  font-size: 12px;
  text-decoration: none;
  font-weight: bold;
}}
</style>

<div class="swiper mySwiper">
  <div class="swiper-wrapper">
    {slides_html}
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  new Swiper(".mySwiper", {{
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    loop: true,
    spaceBetween: -100,
    coverflowEffect: {{
      rotate: 30,
      stretch: 0,
      depth: 300,
      modifier: 2,
      slideShadows: true,
    }},
  }});
</script>
"""

# Display in Streamlit
st.markdown("## 🌟 Meet Our Team :) ")
components.html(swiper_html, height=550)
