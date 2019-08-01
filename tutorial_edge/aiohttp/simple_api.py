from aiohttp import web
import json

async def handle(request):
    response_obj = {'status': "success"}
    return web.Response(text=json.dumps(response_obj), status=200)

async def new_user(request):
    try:
        # happy path where name is set
        user = request.query["name"]
        # process our new user
        print(f"Creating new user with name: {user}")
        response_obj = {"status": "success"}
        # return a success json response with status code 200 i.e. 'Ok'
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        # bath path
        response_obj = {"status": "failed", "reason": str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)

app = web.Application()
app.router.add_get("/", handle)
app.router.add_post("/user", new_user)

web.run_app(app, host="*", port=8081)
