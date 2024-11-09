#!/usr/bin/env python
# coding: utf-8

# In[20]:


# from flask import Flask, request, jsonify, render_template
# from google.cloud import texttospeech
# import os
# import uuid
# from ibm_watsonx_ai.foundation_models import ModelInference
# from ibm_watsonx_ai.client import APIClient

# # Initialize Flask app
# app = Flask(__name__)

# # Load configuration from config.py
# app.config.from_object('config')  # Ensure config.py is in the same directory as app.py

# # Initialize Google TTS client
# tts_client = texttospeech.TextToSpeechClient()

# # Initialize IBM Watson Model client with settings from config
# credentials = {
#     "apikey": app.config["API_KEY"],
#     "url": app.config["SERVICE_URL"]
# }
# api_client = APIClient(credentials)

# # Add project_id or space_id as needed
# model = ModelInference(
#     api_client=api_client,
#     model_id=app.config["MODEL_ID"],
#     project_id=app.config.get("PROJECT_ID"),  # Use project_id if available
# )

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process_data():
#     data = request.json
#     question = data.get("question")
#     response_text = generate_response(question)
   
#     # Generate audio from response using Google TTS
#     audio_path = generate_tts(response_text)
#     return jsonify(response=response_text, audio=audio_path)

# def generate_response(user_input):
#     # Construct a prompt to guide model response
#     prompt = f"""
    
# المهمة الرئيسية:
# تعليم اللغة العربية من خلال إجراء حوار مع المستخدم

# التعليمات:
# اسأل المتسخدم عن اسمه
# مثال:
# اهلا وسهلا بك اسمي علام أنا هنا لمساعدتك في تعلم اللغة العربية ما اسمك؟

# ثم

# اعرض على المستخدم مواضيع الحوارات

# مثال:
#  اهلا يا .......... اختر واحداً من هذه المواضيع لنقوم أنا وأنت بإجراء حوار حول هذا الموضوع 
# 1. في المطار
# 2. في الجامعة
# 3. في السوق
# 4. في في المنزل 
# 5. حوار عن الجو..
# 6. شراء هاتف جوال 
  
# ثم انشأ حوار مبسط لمستوى مبتدئ مع المستخدم




#  ثم

#  اعد الحوار مع المستخدم بحيث تقوم أنت بتأدية أحد الأدوار والمستخدم يقوم بالدور الآخر
# مثال:
# يؤدي المستخدم دوره :

# بعد أن كتب المستخدم دوره  تقوم أنت بدورك :

# يؤدي المستخدم دوره :

# بعد أن كتب المستخدم دوره  تقوم أنت بدورك:


# يؤدي المستخدم دوره :

# بعد أن كتب المستخدم دوره  تقوم أنت بدورك:



#     <</SYS>>

#     User: {user_input}
#     Bot:
#     """

#     # Generate response from the model using only the prompt
#     response = model.generate_text(prompt=prompt)
#     return response.strip()

# def generate_tts(text):
#     # Configure TTS request for Google Cloud
#     synthesis_input = texttospeech.SynthesisInput(text=text)
#     voice = texttospeech.VoiceSelectionParams(language_code="ar-SA", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
#     audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

#     # Perform the text-to-speech request
#     response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

#     # Save audio to a temporary file
#     audio_filename = f"{uuid.uuid4()}.mp3"
#     audio_path = os.path.join("static", audio_filename)
#     with open(audio_path, "wb") as out:
#         out.write(response.audio_content)
#         print(f'Audio content written to file "{audio_path}"')
   
#     return audio_path

# if __name__ == '__main__':
#     app.run(debug=True)


# In[21]:


# from flask import Flask, request, jsonify, render_template
# from google.cloud import texttospeech
# import os
# import uuid
# from ibm_watsonx_ai.foundation_models import ModelInference
# from ibm_watsonx_ai.client import APIClient

# # Initialize Flask app
# app = Flask(__name__)

# # Load configuration from config.py
# app.config.from_object('config')

# # Initialize Google TTS client
# tts_client = texttospeech.TextToSpeechClient()

# # Initialize IBM Watson Model client with settings from config
# credentials = {
#     "apikey": app.config["API_KEY"],
#     "url": app.config["SERVICE_URL"]
# }
# api_client = APIClient(credentials)

# # Add project_id or space_id as needed
# model = ModelInference(
#     api_client=api_client,
#     model_id=app.config["MODEL_ID"],
#     project_id=app.config.get("PROJECT_ID")
# )

# # Memory to store conversation context
# conversation_memory = []

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process_data():
#     data = request.json
#     question = data.get("question")
#     response_text = generate_response(question)
   
#     # Generate audio from response using Google TTS
#     audio_path = generate_tts(response_text)
#     return jsonify(response=response_text, audio=audio_path)

# def generate_response(user_input):
#     # Append user input to conversation memory
#     conversation_memory.append(f"المستخدم: {user_input}")
    
#     # Structure prompts in segments to reduce truncation
#     segmented_prompts = [
#         "علام: مرحبًا بك في جلسة تعلم اللغة العربية! ما هو اسمك؟",
#         "علام: من فضلك اختر موضوعًا من القائمة التالية:",
#         "علام: هل ترغب في دور الزبون أم البائع؟",
#         "علام: لنبدأ الحوار. كيف يمكنني مساعدتك؟",
#         "علام: شكرًا لك! هل ترغب في تجربة موضوع آخر؟"
#     ]

#     response = ""
#     for prompt in segmented_prompts:
#         # Generate each response segment and store it in conversation memory
#         full_prompt = "\n".join(conversation_memory) + "\n" + prompt
#         segment_response = model.generate_text(prompt=full_prompt).strip()

#         # Continue until a complete response is generated for each segment
#         if segment_response.endswith("...") or len(segment_response) < 30:
#             segment_response += model.generate_text(prompt=prompt + " اكمل الجواب:").strip()
        
#         # Append each segment response to the conversation memory and main response
#         conversation_memory.append(f"علام: {segment_response}")
#         response += "\n" + segment_response
    
#     return response

# def generate_tts(text):
#     synthesis_input = texttospeech.SynthesisInput(text=text)
#     voice = texttospeech.VoiceSelectionParams(language_code="ar-SA", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
#     audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

#     response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

#     audio_filename = f"{uuid.uuid4()}.mp3"
#     audio_path = os.path.join("static", audio_filename)
#     with open(audio_path, "wb") as out:
#         out.write(response.audio_content)
#         print(f'Audio content written to file "{audio_path}"')
   
#     return audio_path

# if __name__ == '__main__':
#     app.run(debug=True)


# In[23]:


# from flask import Flask, request, jsonify, render_template
# from google.cloud import texttospeech
# import os
# import uuid
# from ibm_watsonx_ai.foundation_models import ModelInference
# from ibm_watsonx_ai.client import APIClient

# # Initialize Flask app
# app = Flask(__name__)

# # Load configuration from config.py
# app.config.from_object('config')

# # Initialize Google TTS client
# tts_client = texttospeech.TextToSpeechClient()

# # Initialize IBM Watson Model client with settings from config
# credentials = {
#     "apikey": app.config["API_KEY"],
#     "url": app.config["SERVICE_URL"]
# }
# api_client = APIClient(credentials)

# # Add project_id or space_id as needed
# model = ModelInference(
#     api_client=api_client,
#     model_id=app.config["MODEL_ID"],
#     project_id=app.config.get("PROJECT_ID")
# )

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process_data():
#     data = request.json
#     question = data.get("question")
#     response_text = generate_response(question)
   
#     # Generate audio from response using Google TTS
#     audio_path = generate_tts(response_text)
#     return jsonify(response=response_text, audio=audio_path)

# def generate_response(user_input):
#     # Base system prompt to guide Allam in a structured, beginner-friendly conversation
#     system_prompt = """
#     <<SYS>>
#     أنت "علام"، مساعد لتعليم اللغة العربية من خلال حوارات بسيطة. الهدف هو الحفاظ على حوار باللغة العربية فقط، باستخدام جمل قصيرة وبسيطة.
    
#     التعليمات:
#     1. قدم نفسك واسأل عن اسم المستخدم.
#     2. عند معرفة اسم المستخدم، اعرض عليه المواضيع للاختيار.
#     3. بناءً على الموضوع الذي يختاره، اسأله عن الدور الذي يريد تأديته.
#     4. في الحوار، تأكد من أن كل سؤال منطقي ومباشر، مع تقديم إجابات قصيرة وسهلة الفهم.
#     5. عند انتهاء الحوار، اسأل المستخدم إذا كان يريد تجربة موضوع آخر.

#     تذكر، اجعل إجاباتك موجزة وبسيطة، وابقَ ضمن موضوع الحوار دون الخروج عنه.
#     <<SYS>>
#     """

#     # Conversation steps to ensure logical responses
#     steps = [
#         {"prompt": "علام: مرحبًا! أنا علام، مساعدك في تعلم اللغة العربية. ما اسمك؟", "expect": "الاسم"},
#         {"prompt": "علام: سررت بمعرفتك! اختر موضوعًا لبدء الحوار:\n1. في السوق\n2. في المطعم\n3. في المطار\n4. في المستشفى", "expect": "الموضوع"},
#         {"prompt": "علام: رائع! هل ترغب في أن تكون الزبون أم البائع؟", "expect": "الدور"},
#         {"prompt": "علام: لنبدأ الحوار! كيف يمكنني مساعدتك اليوم؟", "expect": "الحوار"},
#         {"prompt": "علام: شكرًا لك على هذا الحوار! هل ترغب في تجربة موضوع آخر؟", "expect": "نهاية"}
#     ]

#     # Determine the conversation step based on previous memory or new input
#     conversation_memory = []

#     for step in steps:
#         # Build the prompt with the context from the system and current step
#         full_prompt = system_prompt + "\n" + "\n".join(conversation_memory) + "\n" + step["prompt"]

#         # Generate response for each step
#         response = model.generate_text(prompt=full_prompt).strip()
        
#         # Ensure response is logical and relevant to the prompt
#         if response.endswith("...") or len(response) < 30:
#             response += model.generate_text(prompt=step["prompt"] + " اكمل الجواب:").strip()
        
#         # Store response in conversation memory
#         conversation_memory.append(f"علام: {response}")
        
#         # If response meets the expectation, continue to the next step
#         if step["expect"] in ["الاسم", "الموضوع", "الدور", "الحوار", "نهاية"]:
#             conversation_memory.append(f"المستخدم: {user_input}")

#     return "\n".join(conversation_memory)

# def generate_tts(text):
#     # Configure TTS request for Google Cloud
#     synthesis_input = texttospeech.SynthesisInput(text=text)
#     voice = texttospeech.VoiceSelectionParams(language_code="ar-SA", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
#     audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

#     # Perform the text-to-speech request
#     response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

#     # Save audio to a temporary file
#     audio_filename = f"{uuid.uuid4()}.mp3"
#     audio_path = os.path.join("static", audio_filename)
#     with open(audio_path, "wb") as out:
#         out.write(response.audio_content)
#         print(f'Audio content written to file "{audio_path}"')
   
#     return audio_path

# if __name__ == '__main__':
#     app.run(debug=True)


# In[24]:


from flask import Flask, request, jsonify, render_template
from google.cloud import texttospeech
import os
import uuid
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.client import APIClient

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config')  # Ensure config.py is in the same directory as app.py

# Initialize Google TTS client
tts_client = texttospeech.TextToSpeechClient()

# Initialize IBM Watson Model client with settings from config
credentials = {
    "apikey": app.config["API_KEY"],
    "url": app.config["SERVICE_URL"]
}
api_client = APIClient(credentials)

# Add project_id or space_id as needed
model = ModelInference(
    api_client=api_client,
    model_id=app.config["MODEL_ID"],
    project_id=app.config.get("PROJECT_ID"),  # Use project_id if available
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    question = data.get("question")
    response_text = generate_response(question)
   
    # Generate audio from response using Google TTS
    audio_path = generate_tts(response_text)
    return jsonify(response=response_text, audio=audio_path)

def generate_response(user_input):
    # Construct a prompt to guide model response
    prompt = f"""
    
المهمة الرئيسية:
تعليم اللغة العربية من خلال إجراء حوار مع المستخدم

التعليمات:
اسأل المتسخدم عن اسمه
مثال:
اهلا وسهلا بك اسمي علام أنا هنا لمساعدتك في تعلم اللغة العربية ما اسمك؟

ثم

اعرض على المستخدم مواضيع الحوارات

مثال:
 اهلا يا .......... اختر واحداً من هذه المواضيع لنقوم أنا وأنت بإجراء حوار حول هذا الموضوع 
1. في المطار
2. في الجامعة
3. في السوق
4. في في المنزل 
5. حوار عن الجو..
6. شراء هاتف جوال 
  
ثم انشأ حوار مبسط لمستوى مبتدئ مع المستخدم




 ثم

 اعد الحوار مع المستخدم بحيث تقوم أنت بتأدية أحد الأدوار والمستخدم يقوم بالدور الآخر
مثال:
يؤدي المستخدم دوره :

بعد أن كتب المستخدم دوره  تقوم أنت بدورك :

يؤدي المستخدم دوره :

بعد أن كتب المستخدم دوره  تقوم أنت بدورك:


يؤدي المستخدم دوره :

بعد أن كتب المستخدم دوره  تقوم أنت بدورك:



    <</SYS>>

    User: {user_input}
    Bot:
    """

    # Generate response from the model using only the prompt
    response = model.generate_text(prompt=prompt)
    return response.strip()

def generate_tts(text):
    # Configure TTS request for Google Cloud
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="ar-SA", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the text-to-speech request
    response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # Save audio to a temporary file
    audio_filename = f"{uuid.uuid4()}.mp3"
    audio_path = os.path.join("static", audio_filename)
    with open(audio_path, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{audio_path}"')
   
    return audio_path

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




