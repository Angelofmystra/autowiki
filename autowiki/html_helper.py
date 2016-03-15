# This file does the html work for you.
# It includes test functions.
# Running this file will cause a test html to be made.
# One day it might even create a placeholder autowiki - to test the format independent of the data


def get_default_title():
    return "Dawn of War Pro Autowiki"


def get_default_body():
    return "<p> Ja ja saucisse</p>"


def get_default_content_list():
    return ""


def write_list(f, listofitems):
    f.write("<ul>")
    for e in listofitems:
        f.write("<li>"+e+"</li>")
    f.write("</ul>")


def write_image(f, url, alt, style):
    f.write("<img src="+url+" alt="+alt+" style="+style+">")


def write_url(f, url, text):
    f.write("<a href="+url+">"+text+"</a>")


def write_html(write_title_func, write_body_func):
    with open('workfile.html', 'w') as f:
        f.write("<!DOCTYPE html>")
        f.write("<html lang=\"en-US\">")
        f.write("<head>")
        f.write("<meta charset=\"UTF-8\">")
        f.write("<title>"+write_title_func()+"</title>")
        f.write("</head>")
        f.write("<body>")
        f.write(write_body_func())
        f.write("<div id=\"footer\">Copyright © Dawn of War Pro</div>")
        f.write("</body>")
        f.write("</html>")


write_html(get_default_title, get_default_body)