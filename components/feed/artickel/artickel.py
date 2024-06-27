from django_components import component

@component.register("artickel")
class artickel(component.Component):
    template_name = 'feed/artickel/template.html'
    
    def get_context_data(self,title,simple_content,date,category):
        context = {
            'title':title,
            'simple_content':simple_content,
            'date':date,
            'category':category,
        }
        return context