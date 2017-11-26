from jinja2 import Environment
from jinja2.loaders import DictLoader

def test_inheritance():
    """
    Render a template based on a series of
    inherited embedded and enclosing components.
    """
    print('\ntest inheritance:')
    env = Environment(loader=DictLoader({
    'a': '''[A[{% block body %}{% endblock %}]]''',
    'b': '''{% extends 'a' %}{% block body %}[B]{% endblock %}''',
    'c': '''{% extends 'b' %}{% block body %}###{{ super() }}###{% endblock %}'''
    }))
    print env.get_template('c').render()

def test_loop_filter():
    """
    Filter items in a for loop,
    print item names and indexes,
    and pass in arguments to evaluate.
    """
    print('\ntest loop filter:')
    tmpl = Environment().from_string("""\
<ul>
{%- for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if item % 2 == 0 %}
    <li>{{ loop.index }} / {{ loop.length }}: {{ item }}</li>
{%- endfor %}
</ul>
<p>if condition: {{ 1 if foo else 0 }}</p>
""")
    print(tmpl.render(foo=True))

def test_translate():
    print('\ntest translate:')
    env = Environment(extensions=['jinja2.ext.i18n'])
    env.globals['gettext'] = {
    'Hello %(user)s!': 'Hallo %(user)s!'
    }.__getitem__
    env.globals['ngettext'] = lambda s, p, n: {
    '%(count)s user': '%(count)d Benutzer',
    '%(count)s users': '%(count)d Benutzer'
    }[n == 1 and s or p]
    print env.from_string("""\
{% trans %}Hello {{ user }}!{% endtrans %}
{% trans count=users|count %}{{ count }} user{% pluralize %}{{ count }} users{% endtrans %}
""").render(user="someone", users=[1, 2, 3])

test_inheritance()
test_loop_filter()
test_translate()

exit()
