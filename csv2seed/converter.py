from os.path import splitext, basename, dirname
import csv

template = """{model}::create([
{attributes}
]);
"""


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def rowCSVFile(csvfile, delimiter=";", attributes=None):
    if attributes:
        for row in csv.reader(csvfile, delimiter=delimiter):
            yield row
    else:
        for row in csv.DictReader(csvfile, delimiter=delimiter):
            yield row


def run(csv_file, indented=" " * 4, delimiter=";", model=None,
        attributes=None, has_header=True):
    with open(csv_file, newline='') as csvfile:
        seeder = ""
        file_name = getFileName(csvfile.name)
        model = model or file_name.capitalize()
        if attributes:
            first = True
            for data in rowCSVFile(csvfile, delimiter=delimiter, attributes=attributes):
                content = ""
                if has_header and first:
                    first = False
                    pass
                else:
                    for i, attribute in enumerate(attributes):
                        value = data[i]
                        content += f'{indented}"{attribute}" => "{value}",\n'
                    seeder += template.format(model=model, attributes=content[:-2])
                first = False
        else:
            for data in rowCSVFile(csvfile, delimiter=delimiter, attributes=attributes):
                content = ""
                for attribute in list(data.keys()):
                    value = data[attribute]
                    content += f'{indented}"{attribute}" => "{value}",\n'
                seeder += template.format(model=model, attributes=content[:-2])
        seeder_file = f"{dirname(csvfile.name)}/{file_name}.txt"
        f = open(seeder_file, "w")
        f.write(seeder)
        f.close()
