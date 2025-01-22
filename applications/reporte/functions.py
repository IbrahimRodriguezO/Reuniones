from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()

    # Establecer base_url para resolver las imágenes
    base_url = context_dict.get('base_url', 'http://localhost:8000')

    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result, encoding="utf-8", link_callback=lambda uri, rel: base_url + uri if uri.startswith('/media/') else uri)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    
    return None
