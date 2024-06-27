from django_components import component
from django_components import types as t

@component.register("menuitem")
class menuitem(component.Component):
    # template_name = 'feed/sidemenu/menuitem/template.html'
    
    def get_context_data(self,link_url,link_name):
        context = {
            'link_url':link_url,
            'link_name':link_name
        }
        return context
    
    template: t.django_html = """
    <li><a href="{{ link_url }}" class="active:bg-madang-600 active:text-base-100 hover:bg-madang-600 hover:text-base-100">{{ link_name }}</a></li>
    """