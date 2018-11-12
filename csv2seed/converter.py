from os.path import splitext, basename, dirname
import csv


def getFileName(file):
    base = basename(file)
    return splitext(base)[0]


def run(csv_file, indented=" " * 4, delimiter=";", model=None):
    with open(csv_file, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=delimiter)
        seeder = ""
        for data in spamreader:
            attributes = list(data.keys())
            model = getFileName(csvfile.name).capitalize() if not model else model
            content = f"{model}::create([\n"
            for attribute in attributes:
                content += f'{indented}"{attribute}" => "{data[attribute]}",\n'
            content = f"{content[:-2]}\n]);"
            seeder += f"{content}\n"
        seeder_file = f"{dirname(csvfile.name)}/{getFileName(csvfile.name)}.txt"
        f  = open(seeder_file, "w")
        f.write(seeder)
        f.close()