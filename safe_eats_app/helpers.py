from django.template import loader, RequestContext


def render_to_string(template_name, context=None, request=None):
  context_instance = RequestContext(request) if request else None
  return loader.render_to_string(template_name, context, context_instance)
