from docutils import frontend
from docutils.parsers import rst
from jinja2 import Template
import datetime
import docutils
import os

template_in = """
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>Example Feed</title>
  <link href="http://example.org/"/>
  <updated>{{ date }}</updated>
  <author>
    <name>{{ name }}</name>
  </author>
  <id>urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6</id>

  <entry>
    <title>Atom-Powered Robots Run Amok</title>
    <link href="http://example.org/2003/12/13/atom03"/>
    <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
    <updated>2003-12-13T18:30:02Z</updated>
    <summary>Some text.</summary>
  </entry>

</feed>
"""

class Visitor(docutils.nodes.GenericNodeVisitor):
    """
    """
    def default_visit(self, node):
        # Pass all other nodes through.
        pass

fileobj = open(os.path.join('doc', 'index.rst'))

# https://eli.thegreenplace.net/2017/a-brief-tutorial-on-parsing-restructuredtext-rest/
default_settings = frontend.OptionParser(
    components=(rst.Parser,)).get_default_values()
document = docutils.utils.new_document(fileobj.name, default_settings)
parser = rst.Parser()
parser.parse(fileobj.read(), document)


visitor = Visitor(document)
document.walk(visitor)


template_obj = Template(template_in)
date = datetime.datetime.now().isoformat()
template_out = template_obj.render(name='Alex Clark', date=date)
print(template_out)
