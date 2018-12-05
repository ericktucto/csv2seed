from os.path import splitext, basename, abspath, dirname
import csv

template = """{model}::create([
{attributes}
]);
"""


def run(csv_file, indented=" " * 4, delimiter=";", model=None,
        attributes=None, has_header=False):

    def generateContent(indented, attributes, data):
        content = "\n".join([
            '%s"%s" => "%s",' %
            (indented, attribute, tuple(data)[index])
            for index, attribute in enumerate(attributes)
        ])
        return content[:-1]  # Delete , end

    def getFileName(file):
        base = basename(file)
        return splitext(base)[0]

    def getAbsolutePath(file):
        return dirname(abspath(file))

    with open(csv_file, newline='') as csvfile:
        seeder = ""
        file_name = getFileName(csvfile.name)
        model = model or file_name.capitalize()
        include_header = attributes and not has_header
        for data in csv.DictReader(csvfile, delimiter=delimiter):
            content = ""
            attributes = attributes or tuple(data)
            if include_header:
                values = data.keys()
                content = generateContent(indented, attributes, values)
                seeder += template.format(model=model, attributes=content)
                include_header = False
                content = ""
            values = data.values()
            content = generateContent(indented, attributes, values)
            seeder += template.format(model=model, attributes=content)
        seeder_file = "%s/%s.txt" % (getAbsolutePath(csv_file), file_name)
        f = open(seeder_file, "w")
        f.write(seeder)
        f.close()
