from django_components import component

@component.register("sidemenu")
class sidemenu(component.Component):
    template_name = 'feed/sidemenu/template.html'

    def get_context_data(self):
        link_data = {
            'Fiksi': '#',
            'Buku': '#',
            'Art': '#',
            'Teknology': '#',
            'Human': '#',
            'Animal': '#',
            'Ghost': '#',
            
        }
        context = {
            'link_data': link_data  # Pass link_data to the context
        }
        return context
