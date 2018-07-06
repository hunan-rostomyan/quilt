import json


def read_text(path):
    with open(path) as fp:
        return fp.readlines()


def read_json(path):
    with open(path) as fp:
        return json.load(fp)


def read_jsonl(path):
    objects = []
    with open(path) as fp:
        for line in fp:
            objects.append(json.loads(line))
    return objects