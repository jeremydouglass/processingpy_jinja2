from jinja2 import Environment
from jinja2.loaders import DictLoader

def inheritance_test():
    """Render a template """
    env = Environment(loader=DictLoader({
    'a': '''[A[{% block body %}{% endblock %}]]''',
    'b': '''{% extends 'a' %}{% block body %}[B]{% endblock %}''',
    'c': '''{% extends 'b' %}{% block body %}###{{ super() }}###{% endblock %}'''
    }))
    print env.get_template('c').render()

def test_loop_filter():
    tmpl = Environment().from_string("""\
<ul>
{%- for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if item % 2 == 0 %}
    <li>{{ loop.index }} / {{ loop.length }}: {{ item }}</li>
{%- endfor %}
</ul>
<p>if condition: {{ 1 if foo else 0 }}</p>
""")
    print(tmpl.render(foo=True))

print('\ntest inheritance:')
inheritance_test()

print('\ntest loop:')
test_loop_filter()

exit()
