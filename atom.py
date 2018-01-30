from docutils import frontend
from docutils.parsers import rst
from jinja2 import Template
from uuid import uuid4
import datetime
import docutils
import os

# https://eli.thegreenplace.net/2017/a-brief-tutorial-on-parsing-restructuredtext-rest/

feed = """
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>Alex Clark's Blog</title>
  <link href="https://blog.aclark.net"/>
  <updated>{{ date }}</updated>
  <author>
    <name>Alex Clark</name>
  </author>
  <id>urn:uuid:{{ uuid }}</id>
"""

entry = """
  <entry>
    <title>Atom-Powered Robots Run Amok</title>
    <link href="http://example.org/2003/12/13/atom03"/>
    <id>urn:uuid:{{ uuid }}</id>
    <updated>{{ date }}</updated>
    <summary>Some text.</summary>
  </entry>
"""


class Visitor(docutils.nodes.GenericNodeVisitor):
    """
    """

    def default_visit(self, node):
        """
        """


date = datetime.datetime.now().isoformat()
uuid = uuid4()

parser_settings = frontend.OptionParser(
    components=(rst.Parser, )).get_default_values()
parser_obj = rst.Parser()

feed_obj = Template(feed)
feed_out = feed_obj.render(date=date, uuid=uuid)

atom_xml = open('atom.xml', 'w')
atom_xml.write(feed_out)

entry_obj = Template(entry)

for root, dirs, files in os.walk('doc'):
    for f in files:
        if f.endswith(".rst"):
            article = open(os.path.join(root, f))
            document = docutils.utils.new_document(article.name,
                                                   parser_settings)
            parser_obj.parse(article.read(), document)
            visitor = Visitor(document)
            document.walk(visitor)
            uuid = uuid4()
            entry_out = entry_obj.render(date=date, uuid=uuid)
            article.close()
            atom_xml.write(entry_out)
atom_xml.write('\n</feed>\n')
atom_xml.close()
