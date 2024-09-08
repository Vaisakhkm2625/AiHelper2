from openai import OpenAI
import base64
import copykitten


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def openai_image_reponse(API_KEY,image_path):

# Path to your image
    #image_path = "./cropped_screenshot.png"

# Getting the base64 string
    base64_image = encode_image(image_path)

    client = OpenAI(api_key=API_KEY)

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "Please answer question in this image. response shouldn't be like an ai assistant, just answer is enough."},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    result = response.choices[0].message.content

    print(result)
    if result is None:
        result = "oops" 
    copykitten.copy(result)

if __name__ == "__main__":

    from settings import load_settings
    import platformdirs
    import os

    app_auther = "vaisaskh"
    app_name = "aihelper"

    config_dir = platformdirs.user_config_dir(app_name,app_auther)
    config_file = os.path.join(config_dir,"settings.ini")
    image_file_path = os.path.join(config_dir,"cropped_screenshot.png")

    settings = load_settings(config_file,app_name)
    openai_image_reponse(settings['openai_key'],image_file_path)
    
