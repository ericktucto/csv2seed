from os.path import splitext, basename, dirname
import csv

template = """{model}::create([
{attributes}
]);
"""


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def run(csv_file, indented=" " * 4, delimiter=";", model=None,
        attributes=None):
    with open(csv_file, newline='') as csvfile:
        seeder = ""
        file_name = getFileName(csvfile.name)
        model = file_name.capitalize() if not model else model
        if attributes:
            for data in csv.reader(csvfile, delimiter=delimiter):
                content = ""
                for i, attribute in enumerate(attributes):
                    value = data[i]
                    content += f'{indented}"{attribute}" => "{value}",\n'
                seeder += template.format(model=model, attributes=content[:-2])
        else:
            for data in csv.DictReader(csvfile, delimiter=delimiter):
                content = ""
                for attribute in list(data.keys()):
                    value = data[attribute]
                    content += f'{indented}"{attribute}" => "{value}",\n'
                seeder += template.format(model=model, attributes=content[:-2])
        seeder_file = f"{dirname(csvfile.name)}/{file_name}.txt"
        f = open(seeder_file, "w")
        f.write(seeder)
        f.close()
