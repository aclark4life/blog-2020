from docutils import frontend
from docutils.parsers import rst
from jinja2 import Template
from uuid import uuid4
import datetime
import docutils
import os

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
entries = {}

# Gather entries
for root, dirs, files in os.walk('doc'):
    for f in files:
        if f == "index.rst":
            uuid = uuid4()
            path = os.path.join(root, f)
            path_obj = path.split('/')

            if len(path_obj) == 6:  # This is a blog article
                                    # of the form doc/YYYY/MM/DD/title/index.rst

                year = int(path_obj[1])
                month = int(path_obj[2])
                day = int(path_obj[3])
                date = datetime.datetime(year, month, day)

                fileobj = open(path)
                doc_obj = docutils.utils.new_document(fileobj.name,
                                                      parser_settings)
                parser_obj.parse(fileobj.read(), doc_obj)
                doc_obj.walk(Visitor(doc_obj))

                entry_out = entry_obj.render(date=date.isoformat(), uuid=uuid)
                entries[date] = entry_out
                fileobj.close()

# Write entries
for key in sorted(entries.keys(), reverse=True):
    atom_xml.write(entries[key])

atom_xml.write('\n</feed>\n')
atom_xml.close()
