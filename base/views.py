from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
    <head>
        <title>Heshwan's Homepage</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial, sans-serif; background-color: #f9f9f9; text-align: center; margin: 0; padding: 0; }
            header { background-color: #0073e6; color: white; padding: 20px; font-size: 24px; }
            section { margin: 20px; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
            footer { background-color: #333; color: white; padding: 10px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <header>Hi ! I Am Heshwan Adnan</header>
        <section>
            <h2>About Me</h2>
            <p>I Am Computer Science Student and I Study At University Of Sulaimani .</p>
        </section>
        <section>
            <h3>My Interests</h3>
            <ul style="list-style: none; padding: 0;">
                <li> Programming</li>
                <li> Graphic Design</li>
                <li> Learning Language </li>
            </ul>
        </section>
        
    </body>
    </html>
    """
    return HttpResponse(html_content)