from fastapi import FastAPI
import gradio as gr
from fastapi.responses import RedirectResponse

from gradio_ui import demo
import t2speech
import t2text
import chatbot
import dashboard
import t2speechmuit
app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200
@app.get("/redirect")
async def redirect_to_site():
    # إعادة التوجيه إلى موقع معين
    return RedirectResponse(url="http://lahja.runasp.net/services")
app = gr.mount_gradio_app(app, demo, path='/studio-t2speech')
app = gr.mount_gradio_app(app, t2speech.demo, path='/t2speech')

app = gr.mount_gradio_app(app, t2text.demo, path='/studio-t2text')

app = gr.mount_gradio_app(app, demo, path='/vbot')

app = gr.mount_gradio_app(app, chatbot.demo, path='/chatbot')
app = gr.mount_gradio_app(app, dashboard.dashboard, path='/dashboard')
app = gr.mount_gradio_app(app, t2speechmuit.demo, path='/t2speechmuit')
