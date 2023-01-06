# import datetime
# from blacksheep.server import Application
# from blacksheep.server.response import text
# app = Application()
import pandas as pd
# @app.route('/')
# async def home(request):
#     return text(f'hello, worls {datetime.utcnow().isoformat()}')
df = pd.read_csv('spam.csv', encoding='ISO-8859-1')

if __name__ == "__main__":
    import uvicorn
    # import pandas as pd
    # df = pd.read_csv('spam.csv', encoding='ISO-8859-1')
    uvicorn.run("app:app", reload=True)

# run blacksheep:
#   uvicorn server:app --port 44777 --reload
