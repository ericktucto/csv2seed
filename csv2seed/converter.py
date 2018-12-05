from os.path import splitext, basename, abspath, dirname
import csv

template = """{model}::create([
{attributes}
]);
"""


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def getAbsolutePath(file):
    return dirname(abspath(file))


def generateContent(indented, attributes, data):
    return "\n".join([
        '%s"%s" => "%s",' %
        (indented, attribute, tuple(data)[index])
        for index, attribute in enumerate(attributes)
    ])


def run(csv_file, indented=" " * 4, delimiter=";", model=None,
        attributes=None, has_header=False):
    with open(csv_file, newline='') as csvfile:
        seeder = ""
        file_name = getFileName(csvfile.name)
        model = model or file_name.capitalize()
        include_header = attributes and not has_header
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for data in reader:
            content = ""
            attributes = attributes or tuple(data)
            if include_header:
                content = generateContent(indented, attributes, data.keys())
                seeder += template.format(model=model, attributes=content[:-1])
                include_header = False
                content = ""
            content = generateContent(indented, attributes, data.values())
            seeder += template.format(model=model, attributes=content[:-1])
        seeder_file = "%s/%s.txt" % (getAbsolutePath(csv_file), file_name)
        f = open(seeder_file, "w")
        f.write(seeder)
        f.close()
