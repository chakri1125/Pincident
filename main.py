import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home():
    return RedirectResponse(url="/launch_screen")


@app.get("/launch_screen")
async def launch_screen(request: Request):
    return templates.TemplateResponse(request, "pages/auth/launch_screen.html")

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(request, "pages/auth/login.html")

@app.get('/sso')
async def sso(request: Request):
    return templates.TemplateResponse(request, "pages/auth/sso.html")

@app.get('/sso_prev')
async def sso_prev(request: Request):
    return templates.TemplateResponse(request, "pages/auth/sso_prev.html")

@app.get('/forget_password')
async def forget_password(request: Request):
    return templates.TemplateResponse(request, "pages/auth/forget_password.html")

@app.get('/update_password')
async def update_password(request: Request):
    return templates.TemplateResponse(request, "pages/auth/update_password.html")

@app.get('/forget_done')
async def forget_done(request: Request):
    return templates.TemplateResponse(request, "pages/auth/forget_done.html")

@app.get('/change_password')
async def change_password(request: Request):
    return templates.TemplateResponse(request, "pages/auth/change_password.html")

@app.get('/email_verify')
async def email_verify(request: Request):
    return templates.TemplateResponse(request, "pages/auth/email_verify.html")

@app.get('/phone_verify')
async def phone_verify(request: Request):
    return templates.TemplateResponse(request, "pages/auth/phone_verify.html")

@app.get('/signup')
async def signup(request: Request):
    return templates.TemplateResponse(request, "pages/auth/signup.html")

@app.get('/welcome_screen_first')
async def welcome_screen_first(request: Request):
    return templates.TemplateResponse(request, "pages/auth/welcome_screen_first.html")

@app.get('/welcome_screen_second')
async def welcome_screen_second(request: Request):
    return templates.TemplateResponse(request, "pages/auth/welcome_screen_second.html")

@app.get('/commenting')
async def commenting(request: Request):
    return templates.TemplateResponse(request, "pages/dashboard/commenting.html")

@app.get('/notifications')
async def notifications(request: Request):
    return templates.TemplateResponse(request, "pages/dashboard/notifications.html")

@app.get('/filters')
async def filters(request: Request):
    return templates.TemplateResponse(request, "pages/dashboard/filters.html")

@app.get('/global_search')
async def global_search(request: Request):
    return templates.TemplateResponse(request, "pages/dashboard/global_search.html")

@app.get('/myzones')
async def myzones(request: Request):
    return templates.TemplateResponse(request, "pages/dashboard/myzones.html")

@app.get('/settings')
async def settings(request: Request):
    return templates.TemplateResponse(request, "pages/settings.html")

@app.get('/familyandfriends')
async def familyandfriends(request: Request):
    return templates.TemplateResponse(request, "pages/invitation/familyandfriends.html")

@app.get('/invitesearch')
async def invitesearch(request: Request):
    return templates.TemplateResponse(request, "pages/invitation/invitesearch.html")

@app.get('/inviteuser')
async def inviteuser(request: Request):
    return templates.TemplateResponse(request, "pages/invitation/inviteuser.html")

@app.get('/invitesent')
async def invitesent(request: Request):
    return templates.TemplateResponse(request, "pages/invitation/invitesent.html")

@app.get('/profile_view')
async def invitesearch(request: Request):
    return templates.TemplateResponse(request, "pages/profile/profile_view.html")

@app.get('/profile_edit')
async def profile_edit(request: Request):
    return templates.TemplateResponse(request, "pages/profile/profile_edit.html")

@app.get('/user_details')
async def user_details(request: Request):
    return templates.TemplateResponse(request, "pages/profile/user_details.html")

@app.get('/dent_search')
async def dent_search(request: Request):
    return templates.TemplateResponse(request, "pages/map/dent_search.html")

@app.get('/dent_detail')
async def dent_detail(request: Request):
    return templates.TemplateResponse(request, "pages/map/dent_detail.html")

@app.get('/zone_creation')
async def zone_creation(request: Request):
    return templates.TemplateResponse(request, "pages/map/zone_creation.html")

@app.get('/zone_detail')
async def zone_detail(request: Request):
    return templates.TemplateResponse(request, "pages/map/zone_detail.html")

uvicorn.run(app=app, host="127.0.0.1", port=8000)
