# backend/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel backend after removing example directory!</h1>
            <p>The current time is { now }.</p>
            <h1> Big test </h1>
        </body>
    </html>
    '''
    return HttpResponse(html)
