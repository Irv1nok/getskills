class RenderList:

    def __init__(self, tag):
        if tag not in ('ul', 'ol'):
            self.tag = 'ul'
        else:
            self.tag = tag

    def __call__(self, t_list, *args, **kwargs):
        ls = ''.join('<li>' + s + '</li>\n' for s in t_list)
        return f'<{self.tag}>\n{ls}</{self.tag}>'





lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
type_list = 'ul'
render = RenderList(type_list)
html = render(lst)
print(html)
# возвращается многострочная строка с соответствующей HTML-разметкой
