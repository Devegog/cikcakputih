from django_components import component

@component.register("brand")
class brand(component.Component):
    template_name = 'feed/navbar_feed/brand/template.html'
    
    def get_context_data(self):
        
        brand = 'cicak putih'
        
        context = {
            'brand': brand
        }
        return context