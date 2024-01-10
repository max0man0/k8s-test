
from __main__ import app

@app.get('/test')
def test():
    return 'it works!'

