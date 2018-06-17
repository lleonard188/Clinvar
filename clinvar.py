import xml.etree.ElementTree as et

path = "ClinVarFullRelease_2018-05.xml"

context = et.iterparse(path, events=("start", "end"))

context = iter(context)

ev, root = next(context)

f= open("NewClinvar.vcf","w+")

for ev, el in context:
    if ev == 'end' and el.tag == 'SequenceLocation':
        if el.attrib['Assembly'] == 'GRCh38':
            f.write(el.attrib['Chr'])

    root.clear()

f.close()
