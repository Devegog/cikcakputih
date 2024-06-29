from django_components import component
from django_components import types as t

@component.register("ui_daisy")
class ui_daisy(component.Component):
    
    template:t.django_html = """
  <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.2/dist/full.min.css" rel="stylesheet" type="text/css" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            'fm': {
              50: '#f0fdfa',
              100: '#d5fbf4',      
              200: '#9bf4e6',      
              300: '#60e8d6',      
              400: '#30d1c2',      
              500: '#17b5a9',      
              600: '#0f928a',      
              700: '#117470',      
              800: '#125d5a',      
              900: '#144d4b',      
              950: '#052e2e',
            },
          'fc': {
            50: '#f6f6f6',    
            100: '#e7e7e7',
            200: '#d1d1d1',
            300: '#b0b0b0',
            400: '#888888',
            500: '#6d6d6d',
            600: '#5d5d5d',
            700: '#4f4f4f',
            800: '#454545',
            900: '#3d3d3d',   
            950: '#262626',
          },
          'madang': {
            50: '#eeffef',
            100: '#d8ffdd',
            200: '#c2ffca',
            300: '#78fd8b',    
            400: '#36f252',
            500: '#0cdb2b',
            600: '#03b61e',
            700: '#078e1b',
            800: '#0b701b',
            900: '#0c5b1a',    
            950: '#00330a',
          },
          }
        }
      }
    }
  </script>
    """