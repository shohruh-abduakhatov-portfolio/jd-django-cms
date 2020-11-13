from io import BytesIO

import imgkit
import requests
from PIL import Image
from django.http import HttpResponseServerError, HttpResponse
from django.shortcuts import render
import os
import json

from cms_panel.settings import MIDDLEWARE_URL


url = 'cms_panel/static/styles/pdf_images/'
template = "cms_panel/templates/pdf_app/index.html"
html_file = "cms_panel/templates/pdf_app/ticket.html"
img_file = url + "ticket.jpg"
pdf_file = url + "ticket.pdf"

def from_html(request):
    """
    :param request:
    :return: pdf of ticket
    """

    """read ticket data from server"""
    data = requests.get(MIDDLEWARE_URL + "orders/byid/ed4bc189-f072-48be-bda4-a882eab066c0")
    if data.status_code != 200: return HttpResponseServerError()
    content = json.loads(data.content.decode('utf-8'))[0]
    body = render(request, "pdf_app/index.html", {"data":content})
    #   html._container[0].decode()
    # return body


    """first save file"""
    with open(html_file, "w") as html:
        html.write(body._container[0].decode())

    """read saved HTML and save as IMG"""
    try:
        imgkit.from_file(html_file, img_file)
    except:
        pass

    """read saved IMG and save as PDF"""
    try:
        im = Image.open(img_file)
        if im.mode == 'RGBA': im = im.conver('RGB')
        im.save(pdf_file, "PDF", resolution=100.0)
    except:
        pass

    # os.remove(html_file)

    """convert to byte"""
    import base64
    with open(pdf_file, "rb") as pdf:
        str = base64.b64encode(pdf.read()) # v1
        b = bytearray(pdf.read()) # v2

    return HttpResponse("ok")
