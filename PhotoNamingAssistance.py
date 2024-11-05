#importing necessary libraries
from openai import OpenAI
import base64
from PIL import Image
from io import BytesIO
import os


#declarations
client = OpenAI()
folder_path = './photos'
files = os.listdir(folder_path)


#This function is usefull to convert image to base64
def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
    return img_str



#This function is usefull to get photo name by assistance
def getPhotoNameByAssitance(image_path):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "You are given a photo to archive, and your task is to assign a clear, descriptive name based on what you see. The name should make it easy to identify and understand the photo at a glance. Be specific—include key details like subjects, colors, actions, or any unique elements. For example, if it's a dog, include details like breed, color, and activity. What will you name this photo?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_to_base64(image_path)}",
                        }
                    },
                ],
            }
        ],
    )
    return completion;

#loop through all files in the folder and rename them
for filename in range(0,len(files)):

    old_file_path = os.path.join(folder_path, files[filename])
    if ".DS_Store" in old_file_path:
        continue
    if os.path.isfile(old_file_path):
        chatGpt_file_name = getPhotoNameByAssitance(old_file_path).choices[0].message.content
        new_filename = (chatGpt_file_name+'.' +files[filename].split('.')[1]).replace('"', '')
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_filename}')
