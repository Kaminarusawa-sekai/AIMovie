import requests
import io
import base64
from PIL import Image
import json

def generate_pic(theme,picname):
  url = "http://127.0.0.1:7858"
  session = requests.session()
  headers={
      "accept": "application/json",
      'Content-Type': 'application/x-www-form-urlencoded'
  }

  login_json={

      'username':"admin",
      'password':"admin",

  }
  response=requests.get(url='http://localhost:7858/user/')
  response = session.post(url='http://localhost:7858/login',headers=headers,data=login_json)

  payload ={
    "enable_hr": False,
    "denoising_strength": 0,
    "firstphase_width": 0,
    "firstphase_height": 0,
    "hr_scale": 2,
    "hr_upscaler": "string",
    "hr_second_pass_steps": 0,
    "hr_resize_x": 0,
    "hr_resize_y": 0,
    "prompt": theme,
    "styles": [
      "string"
    ],
    "seed": -1,
    "subseed": -1,
    "subseed_strength": 0,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "sampler_name": "Euler",
    "batch_size": 1,
    "n_iter": 1,
    "steps": 50,
    "cfg_scale": 7,
    "width": 512,
    "height": 512,
    "restore_faces": False,
    "tiling": False,
    "do_not_save_samples": False,
    "do_not_save_grid": False,
    "negative_prompt": "nsfw,(low quality,normal quality,worst quality,jpeg artifacts),cropped,monochrome,lowres,low saturation,((watermark)),(white letters),skin spots,acnes,skin blemishes,age spot,mutated hands,mutated fingers,deformed,bad anatomy,disfigured,poorly drawn face,extra limb,ugly,poorly drawn hands,missing limb,floating limbs,disconnected limbs,out of focus,long neck,long body,extra fingers,fewer fingers,,(multi nipples),bad hands,signature,username,bad feet,blurry,bad body",
    "eta": 0,
    "s_min_uncond": 0,
    "s_churn": 0,
    "s_tmax": 0,
    "s_tmin": 0,
    "s_noise": 1,
    "override_settings": {},
    "override_settings_restore_afterwards": True,
    "script_args": [],
    "sampler_index": "Euler",
    "script_name": None,
    "send_images": True,
    "save_images": False,
    "alwayson_scripts": {}
  }
  headers1={
      "accept": "application/json",
      'Content-Type': 'application/json'
  }
  response1 = session.post(url=f'{url}/sdapi/v1/txt2img',headers=headers1, json=payload)

  r = response1.json()
  print(r)


  for i in r['images']:
      image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
      image.save(picname+'.png')
