from os.path import splitext, basename, dirname
import csv

template = """{model}::create([
{attributes}
]);
"""


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def run(csv_file, indented=" " * 4, delimiter=";", model=None):
    with open(csv_file, newline='') as csvfile:
        seeder = ""
        for data in csv.DictReader(csvfile, delimiter=delimiter):
            model = getFileName(csvfile.name).capitalize() if not model else model
            attributes = ""
            for attribute in list(data.keys()):
                attributes += f'{indented}"{attribute}" => "{data[attribute]}",\n'
            attributes = attributes[:-2]
            seeder += template.format(model=model, attributes=attributes)
        seeder_file = f"{dirname(csvfile.name)}/{getFileName(csvfile.name)}.txt"
        f  = open(seeder_file, "w")
        f.write(seeder)
        f.close()
