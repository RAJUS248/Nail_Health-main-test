import streamlit as st 
import torch
from PIL import Image
import cv2
import numpy as np

# ========== PAGE CONFIG ==========
st.set_page_config(page_title="Nail Health Detection", layout="centered")

# ========== CONFIG ==========
CFG_MODEL_PATH = "models/yolo_nail200.pt"
DEVICE_OPTION = "cpu"  # or 'cuda' if GPU is available

# ========== LOAD MODEL ==========
@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=CFG_MODEL_PATH, force_reload=True, device=DEVICE_OPTION)
    return model

model = load_model()

# ========== GET NAIL INFO ==========
def get_nail_info(label):
    info = {
        "Healthy Nail": {
            "description": "Your nail appears healthy. It shows a smooth texture, consistent color, and no signs of damage or infection.",
            "precautions": [
                "Keep your nails trimmed and clean",
                "Moisturize nails and cuticles regularly",
                "Avoid using nails as tools",
                "Wear gloves when doing chores involving water or chemicals"
            ],
            "link": "https://www.healthline.com/health/beauty-skin-care/healthy-nails"
        },
        "Acral Lentiginous Melanoma": {
            "description": "A serious form of skin cancer that appears under the nails, on palms or soles. Look out for dark stripes.",
            "precautions": [
                "Seek immediate dermatological advice",
                "Don't ignore dark streaks or spots",
                "Protect affected area from sun"
            ],
            "link": "https://dermnetnz.org/topics/melanoma-of-the-nail-unit"
        },
        "Koilonychia": {
            "description": "Koilonychia, also known as spoon nails, is usually a sign of iron-deficiency anemia or other health conditions.",
            "precautions": [
                "Consult a doctor for iron level testing",
                "Improve dietary intake of iron-rich foods",
                "Take iron supplements if prescribed"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/22140-koilonychia-spoon-nails"
        },
        "Beaus Line": {
            "description": "Beau's lines are horizontal indentations on the nails. Often related to trauma or severe illness.",
            "precautions": [
                "Consult your physician if you notice deep lines",
                "Check for underlying illnesses or deficiencies"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/22906-beaus-lines"
        },
        "Blue Finger": {
            "description": "Blue discoloration may indicate poor oxygen levels or circulatory issues.",
            "precautions": [
                "Seek urgent medical attention if persistent",
                "Avoid cold exposure and improve circulation"
            ],
            "link": "https://www.medicoverhospitals.in/diseases/blue-nails/"
        },
        "Clubbing": {
            "description": "Nail clubbing may signal lung disease, heart problems, or gastrointestinal disorders.",
            "precautions": [
                "Schedule a check-up to identify root cause",
                "Monitor respiratory health"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/24474-nail-clubbing"
        },
        "Lindsay-s Nail": {
            "description": "Also known as half-and-half nails, often related to kidney disease.",
            "precautions": [
                "Get evaluated for kidney function",
                "Manage existing chronic illnesses carefully"
            ],
            "link": "https://www.medicoverhospitals.in/diseases/lindsays-nails/"
        },
        "Muehrckes Lines": {
            "description": "White lines that may appear with low protein levels or liver/kidney problems.",
            "precautions": [
                "Get blood work done to assess albumin levels",
                "Consult with a hepatologist or nephrologist"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/muehrcke-lines"
        },
        "Onychogryphosis": {
            "description": "Thickened, curved nails resembling claws, often due to neglect, trauma, or aging.",
            "precautions": [
                "Maintain nail hygiene and trimming",
                "Visit a podiatrist for proper treatment"
            ],
            "link": "https://www.healthline.com/health/onychogryphosis"
        },
        "Pitting": {
            "description": "Tiny dents in the nails may indicate psoriasis or alopecia areata.",
            "precautions": [
                "Consult a dermatologist",
                "Manage any underlying skin or autoimmune condition"
            ],
            "link": "https://www.healthline.com/health/skin-disorders/nail-pitting"
        },
        "Terry-s Nail": {
            "description": "White nails with a pink or brown band. May indicate liver disease, diabetes, or aging.",
            "precautions": [
                "Get liver function tests",
                "Evaluate for chronic diseases"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/22890-terrys-nails"
        }
    }
    return info.get(label, {
        "description": "No detailed information available for this condition.",
        "precautions": ["Please consult a medical professional."],
        "link": "https://www.webmd.com/skin-problems-and-treatments/nail-problems"
    })

# ========== DETECTION FUNCTION ==========
def run_object_detection(image):
    results = model(image)
    return results

# ========== MAIN ==========
def main():
    st.title("🖐️ Nail Health Detection")
    st.write("This app detects nail conditions using a YOLOv5 model.")

    option = st.radio("Choose Input Method:", ["📸 Camera Snapshot (Mobile Friendly)", "🎥 Real-time Webcam (Desktop Only)"])

    if option == "📸 Camera Snapshot (Mobile Friendly)":
        st.info("Use your phone or computer to take a picture of your nails.")
        picture = st.camera_input("Take a picture")

        if picture:
            image = Image.open(picture).convert("RGB")
            st.image(image, caption="Captured Image", use_column_width=True)

            with st.spinner("🔍 Analyzing your nail..."):
                results = run_object_detection(image)
                pred_df = results.pandas().xyxy[0]

                if not pred_df.empty:
                    results.render()
                    for im in results.ims:
                        st.image(im, caption="Detection Result", use_column_width=True)

                    shown_labels = set()

                    for _, row in pred_df.iterrows():
                        label = row['name']
                        confidence = row['confidence']

                        if label not in shown_labels:
                            st.markdown(f"### 🩺 Detected: **{label}** ({confidence:.2f})")
                            info = get_nail_info(label)
                            st.write(info['description'])
                            st.markdown("### 🛡️ Precautions:")
                            for step in info['precautions']:
                                st.write(f"- {step}")
                            st.markdown(f"📖 [Click here to read more]({info['link']})")
                            shown_labels.add(label)

                else:
                    st.warning("❌ No condition detected. Try again with better lighting or a different angle.")

    elif option == "🎥 Real-time Webcam (Desktop Only)":
        st.warning("This feature only works on desktops/laptops with a connected webcam.")
        run = st.button("Start Webcam Detection")

        if run:
            video_capture = cv2.VideoCapture(0)
            placeholder = st.empty()
            st.info("Press **Stop** or refresh the app to end detection.")

            while True:
                ret, frame = video_capture.read()
                if not ret:
                    st.error("Webcam not accessible.")
                    break

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame_rgb)
                results = run_object_detection(image)
                pred_df = results.pandas().xyxy[0]

                for _, row in pred_df.iterrows():
                    x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                    label = f"{row['name']} {row['confidence']:.2f}"
                    frame_rgb = cv2.rectangle(frame_rgb, (x1, y1), (x2, y2), (255, 0, 255), 2)
                    frame_rgb = cv2.putText(frame_rgb, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

                placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

            video_capture.release()

# ========== LAUNCH ==========
if __name__ == '__main__':
    main()
