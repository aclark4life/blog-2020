from jinja2 import Template
atom_xml = open('atom.xml').read()
template = Template(atom_xml)
print(template.render(name='Alex Clark'))
