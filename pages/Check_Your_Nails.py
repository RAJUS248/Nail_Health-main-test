# import streamlit as st
# from yolo_predictions import YOLO_Pred
# from PIL import Image
# import numpy as np

# st.set_page_config(page_title="YOLO Object Detection",
#                    layout='wide',
#                    page_icon='./images/nail.png')

# st.header('Welcome to Nail Health Portal')
# # st.write('Please Upload Image to get detections')

# with st.spinner('Please wait while your model is loading'):
#     yolo = YOLO_Pred(onnx_model=r'C:/Users/ripud/Desktop/OneDrive - UTS/UTS/Sem 3/DEEP_LEARNING/GUI/Ripu/Nail_Health/models/nail_yolo/best.onnx',
#                     data_yaml=r'C:/Users/ripud/Desktop/OneDrive - UTS/UTS/Sem 3/DEEP_LEARNING/GUI/Ripu/Nail_Health/models/nail_yolo/data.yaml')
                    



# col1, col2 = st.columns(2)
# with col1:
#     # Upload Image
#     image_file = st.file_uploader(label='Upload Image')
#     def upload_image():
#         if image_file is not None:
#             size_mb = image_file.size/(1024**2)
#             file_details = {"filename":image_file.name,
#                             "filetype":image_file.type,
#                             "filesize": "{:,.2f} MB".format(size_mb)}
#             #st.json(file_details)
#             # validate file
#             if file_details['filetype'] in ('image/png','image/jpeg'):
#                 st.success('VALID IMAGE file type (png or jpeg)')
#                 return {"file":image_file,
#                         "details":file_details}
            
#             else:
#                 st.error('INVALID Image file type')
#                 st.error('Upload only png,jpg, jpeg')
#                 return None

# with col2:
#     st.markdown("##### Take Picture #####")
#     buttonVal = st.button('Do you want to take picture from Camera?')
#     def camera_input():
#         if buttonVal:
#             picture = st.camera_input("Take a picture")
#             if picture:
#                 st.image(picture)
                
        
# def main():
#     object = upload_image()
#     object1 = camera_input()
#     if object:
#         prediction = False
#         image_obj = Image.open(object['file'])       
        
#         col1 , col2 = st.columns(2)
        
#         with col1:
#             st.info('Preview of Image')
#             st.image(image_obj)
            
#         with col2:
#             st.subheader('Check below for file details')
#             st.json(object['details'])
#             button = st.button('Get Detection from YOLO')
#             if button:
#                 with st.spinner("""
#                 Geting Objects from image. please wait
#                                 """):
#                     # below command will convert
#                     # obj to array
#                     image_array = np.array(image_obj)
#                     pred_img = yolo.predictions(image_array)
#                     pred_img_obj = Image.fromarray(pred_img)
#                     prediction = True
                
#         if prediction:
#             st.subheader("Predicted Image")
#             st.caption("Object detection from YOLO V5 model")
#             st.image(pred_img_obj)
    
#     # elif object1:
#     #     st.image(object1['Picture'])
#         # prediction = False
#         # image_obj = Image.open(object['file'])       
        
#         # col1 , col2 = st.columns(2)
        
#         # with col1:
#         #     st.info('Preview of Image')
#         #     st.image(image_obj)
            
#         # with col2:
#         #     st.subheader('Check below for file details')
#         #     st.json(object['details'])
#         #     button = st.button('Get Detection from YOLO')
#         #     if button:
#         #         with st.spinner("""
#         #         Geting Objets from image. please wait
#         #                         """):
#         #             # below command will convert
#         #             # obj to array
#         #             image_array = np.array(image_obj)
#         #             pred_img = yolo.predictions(image_array)
#         #             pred_img_obj = Image.fromarray(pred_img)
#         #             prediction = True
                
#         # if prediction:
#         #     st.subheader("Predicted Image")
#         #     st.caption("Object detection from YOLO V5 model")
#         #     st.image(pred_img_obj)
    
    
    
# if __name__ == "__main__":
#     main()






# import streamlit as st
# from yolo_predictions import YOLO_Pred
# from PIL import Image
# import numpy as np

# st.set_page_config(page_title="YOLO Object Detection",
#                    layout='wide',
#                    page_icon='./images/nail.png')

# st.header('Get Object Detection for any Image')
# st.write('*Please Upload Image to get detections*')

# with st.spinner('Please wait while your model is loading'):
#     yolo = YOLO_Pred(onnx_model=r'./models/nail_yolo/yolov5_200.onnx',
#                     data_yaml=r'./models/nail_yolo/data_final.yml')
#     #st.balloons()

# def upload_image():
#     # Upload Image
#     image_file = st.file_uploader(label='Upload Image')
#     if image_file is not None:
#         size_mb = image_file.size/(1024**2)
#         file_details = {"filename":image_file.name,
#                         "filetype":image_file.type,
#                         "filesize": "{:,.2f} MB".format(size_mb)}
#         #st.json(file_details)
#         # validate file
#         if file_details['filetype'] in ('image/png','image/jpeg'):
#             st.success('VALID IMAGE file type (png or jpeg')
#             return {"file":image_file,
#                     "details":file_details}
        
#         else:
#             st.error('INVALID Image file type')
#             st.error('Upload only png,jpg, jpeg')
#             return None
        
# def main():
#     object = upload_image()
    
#     if object:
#         prediction = False
#         image_obj = Image.open(object['file'])       
        
#         col1 , col2 = st.columns(2)
        
#         with col1:
#             st.info('Preview of Image')
#             st.image(image_obj)
            
#         with col2:
#             st.subheader('Check below for file details')
#             st.json(object['details'])
#             button = st.button('Get Detection from YOLO')
            
#             if button:
#                 with st.spinner("""
#                 Geting Objets from image. please wait
#                                 """):
#                     # below command will convert
#                     # obj to array
#                     image_array = np.array(image_obj)
#                     pred_img = yolo.predictions(image_array)
#                     pred_img_obj = Image.fromarray(pred_img)
#                     prediction = True
                
#         if prediction:
#             st.subheader("Predicted Image")
#             st.caption("Object detection from YOLO V5 model")
#             st.image(pred_img_obj)
    
    
    
# if __name__ == "__main__":
#     main()

# import streamlit as st
# from PIL import Image
# import numpy as np
# import torch
# from io import *
# import glob
# from datetime import datetime
# import os
# import wget

# st.set_page_config(page_title="YOLO Object Detection",
#                    layout='wide',
#                    page_icon='./images/nail.png')

# st.header('Get Object Detection for Nail Image')
# st.write('*Please Upload Image to get detections*')

# st.header('Get Object Detection for Nail Image')


# CFG_MODEL_PATH = "models/yolo_nail200.pt"
# deviceoption = "CPU"

# @st.cache_resource
# def loadmodel():
#     with st.spinner('Please wait while your model is loading'):
#         model = torch.hub.load('ultralytics/yolov5', 'custom', path=CFG_MODEL_PATH, force_reload=True, device=deviceoption)
#     return model
    
    

# def upload_image():
#     # Upload Image
#     image_file = st.file_uploader(label='Upload Image')
#     if image_file is not None:
#         size_mb = image_file.size/(1024**2)
#         file_details = {"filename":image_file.name,
#                         "filetype":image_file.type,
#                         "filesize": "{:,.2f} MB".format(size_mb)}
#         #st.json(file_details)
#         # validate file
#         if file_details['filetype'] in ('image/png','image/jpeg'):
#             st.success('VALID IMAGE file type (png or jpeg')
#             return {"file":image_file,
#                     "details":file_details}
        
#         else:
#             st.error('INVALID Image file type')
#             st.error('Upload only png,jpg, jpeg')
#             return None
        
# def main():
#     model = loadmodel()
#     object = upload_image()
    
    
#     if object:
#         prediction = False
#         image_obj = Image.open(object['file'])
#         img_details = object['details']       
#         # print("img_details :",img_details)
#         col1 , col2 = st.columns(2)
        
#         with col1:
#             st.info('Preview of Image')
#             st.image(image_obj,width=300)
        
#         ts = datetime.timestamp(datetime.now())
#         imgpath = os.path.join('data/uploads', str(ts)+img_details['filename'])  
#         outputpath = os.path.join('data/outputs', os.path.basename(imgpath))
        
#         with open(imgpath, mode="wb") as f:
#             image_obj.save(f)
#             st.success("File saved successfully")

#         with col2:
#             st.subheader('Check below for file details')
#             st.json(object['details'])
#             button = st.button('Get Detection from YOLO')
            
#             if button:
#                 with st.spinner(""" Getting Objects from image. please wait """):
#                     pred = model(imgpath)
#                     # pred.dtype()
#                     # print(type(pred))
#                     # print("Pred-------------", pred)
#                     # names = pred.split(" ")
#                     # print("names",names)
#                     pred.render()
#                         # save output to file
#                     for im in pred.ims:
#                         im_base64 = Image.fromarray(im)
#                         im_base64.save(outputpath)
#                     prediction = True
                
#         if prediction:
#             # Predictions
#             img_ = Image.open(outputpath)
#             st.image(img_, caption='Model Prediction(s)', width=300)
            
    
    
# if __name__ == "__main__":
#     main()

import streamlit as st 
from PIL import Image
import numpy as np
import torch
from datetime import datetime
import os

st.set_page_config(page_title="YOLO Object Detection",
                   layout='wide',
                   page_icon='./images/nail.png')

st.header('Get Object Detection for Nail Image')
st.text("Please refer the sample images below for taking a photo (only raw unmanicured nails):")

col1, col2, col3 = st.columns(3)
with col1:
    st.image('./images/VALIDPITCURE/pic3.jpg', width=200)
with col2:
    st.image('./images/VALIDPITCURE/pic1.jpg', width=200)
with col3:
    st.image('./images/VALIDPITCURE/pic2.jpg', width=100)

st.warning("Please note that this detection is not a medical advice. For any further medical help please consult your doctor.")

CFG_MODEL_PATH = "models/yolo_nail200.pt"
deviceoption = "CPU"

@st.cache_resource
def loadmodel():
    with st.spinner('Please wait while your model is loading'):
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=CFG_MODEL_PATH, force_reload=True, device=deviceoption)
    return model

def upload_image():
    image_file = st.file_uploader(label='Please Upload Image to get detections')
    if image_file is not None:
        size_mb = image_file.size / (1024**2)
        file_details = {"filename": image_file.name,
                        "filetype": image_file.type,
                        "filesize": "{:.2f} MB".format(size_mb)}
        if file_details['filetype'] in ('image/png', 'image/jpeg'):
            st.success('VALID IMAGE file type (png or jpeg)')
            return {"file": image_file, "details": file_details}
        else:
            st.error('INVALID Image file type')
            st.error('Upload only png, jpg, jpeg')
    return None

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
        "Beaus Line": {
            "description": "Indented lines or grooves across the nail, often due to illness, injury, or malnutrition.",
            "precautions": [
                "Ensure good nutrition",
                "Address underlying health conditions",
                "Avoid trauma to nails"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/22906-beaus-lines"
        },
        "Blue Finger": {
            "description": "Discoloration often due to poor circulation or oxygen deficiency.",
            "precautions": [
                "Check for underlying heart or lung issues",
                "Warm your hands in cold weather",
                "Consult a doctor if persistent"
            ],
            "link": "https://www.medicoverhospitals.in/diseases/blue-nails/"
        },
        "Clubbing": {
            "description": "Nails curve downward and fingertips enlarge — often related to heart or lung disease.",
            "precautions": [
                "Get a respiratory or cardiac check-up",
                "Quit smoking",
                "Follow-up on chronic diseases"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/24474-nail-clubbing"
        },
        "Koilonychia": {
            "description": "Spoon-shaped nails that may indicate iron-deficiency anemia.",
            "precautions": [
                "Take iron-rich foods or supplements",
                "Consult your doctor for blood tests"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/22140-koilonychia-spoon-nails"
        },
        "Lindsay-s Nail": {
            "description": "Also known as half-and-half nails; often linked to kidney disease.",
            "precautions": [
                "Check kidney function",
                "Stay hydrated",
                "Follow doctor's dietary advice"
            ],
            "link": "https://www.medicoverhospitals.in/diseases/lindsays-nails/"
        },
        "Muehrckes Lines": {
            "description": "White lines that run across the nails, usually caused by low protein levels.",
            "precautions": [
                "Improve protein intake",
                "Treat underlying medical conditions"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/muehrcke-lines"
        },
        "Onychogryphosis": {
            "description": "Thickened, curved nails — commonly seen in the elderly or with trauma.",
            "precautions": [
                "Proper nail trimming",
                "Podiatry care",
                "Avoid tight shoes"
            ],
            "link": "https://www.healthline.com/health/onychogryphosis"
        },
        "Pitting": {
            "description": "Small depressions in the nails — can be a sign of psoriasis or alopecia areata.",
            "precautions": [
                "See a dermatologist",
                "Manage autoimmune conditions",
                "Use medicated nail creams"
            ],
            "link": "https://www.healthline.com/health/skin-disorders/nail-pitting"
        },
        "Terry-s Nail": {
            "description": "White nails with a reddish-brown strip — often linked with liver disease or diabetes.",
            "precautions": [
                "Check liver function and blood sugar",
                "Regular medical check-ups"
            ],
            "link": "https://my.clevelandclinic.org/health/symptoms/22890-terrys-nails"
        }
    }
    return info.get(label, {
        "description": "No specific details found for this condition.",
        "precautions": ["Consult a healthcare provider for further analysis."],
        "link": "https://www.webmd.com/skin-problems-and-treatments/default.htm"
    })

def main():
    model = loadmodel()
    object = upload_image()

    if object:
        prediction = False
        image_obj = Image.open(object['file'])
        img_details = object['details']

        col1, col2 = st.columns(2)
        with col1:
            st.info('Preview of Image')
            st.image(image_obj, width=300)

        ts = datetime.timestamp(datetime.now())
        imgpath = os.path.join('data/uploads', str(ts) + img_details['filename'])
        outputpath = os.path.join('data/outputs', os.path.basename(imgpath))

        with open(imgpath, mode="wb") as f:
            image_obj.save(f)
            st.success("File saved successfully")

        with col2:
            st.subheader('Check below for file details')
            st.json(object['details'])
            button = st.button('Get Detection from YOLO')

            if button:
                with st.spinner("Getting objects from image. Please wait..."):
                    pred = model(imgpath)
                    pred.render()

                    for im in pred.ims:
                        im_base64 = Image.fromarray(im)
                        im_base64.save(outputpath)
                    prediction = True

                    if len(pred.pred[0]) > 0:
                        detected_labels = [pred.names[int(box[-1])] for box in pred.pred[0]]
                        detected_labels = list(set(detected_labels))  # remove duplicates
                    else:
                        detected_labels = ["Unknown"]

        if prediction:
            st.image(Image.open(outputpath), caption='Model Prediction(s)', width=500)
            st.text(pred)

            for label in detected_labels:
                nail_info = get_nail_info(label)
                st.markdown(f"### 🩺 Diagnosis: {label}")
                st.write(nail_info["description"])
                st.markdown("### 🛡️ Precautions:")
                for item in nail_info["precautions"]:
                    st.write(f"- {item}")
                st.markdown(f"📖 [Click here to read more]({nail_info['link']})")
                st.markdown("---")

if __name__ == "__main__":
    main()

