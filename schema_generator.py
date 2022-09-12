import json

def  data_type(value):
    dictionary = {
        type(''): 'string',
        type(54.0): 'number',
        type({}): 'object',
        type(54): 'integer',
        type([]): 'array',
        type(None): 'null',
        type(True): 'boolean'
    }

    return dictionary[type(value)]

def generate(
    obj: dict,
    list_type=False,
    first=False
):
    dictionary = {}

    if first:
        dictionary['$schema'] = 'https://json-schema.org/draft/2020-12/schema'
        dictionary['type'] = 'object'
        dictionary['properties'] = generate(obj)
        dictionary['required'] = [k for k in obj.keys()]
        return dictionary

    if list_type:
        dictionary['type'] = 'object'
        for item in obj:
            if data_type(item) != 'object':
                continue
            dictionary['properties'] = generate(item)
            dictionary['required'] = [k for k in item.keys()]
        return dictionary

    for key in obj.keys():
        dic2 = {}

        if data_type(obj[key]) == 'object':
            dic2['type'] = 'object'
            dic2['properties'] = generate(obj[key])
            dic2['required'] = [k for k in obj.keys()]
        elif data_type(obj[key]) == 'array':
            dic2['type'] = 'array'
            dic2['itens'] = generate(obj[key], True)
        else:
            dic2['type'] = data_type(obj[key])
        dictionary[key] = dic2
    return dictionary

file = open("schema.json", "r")

schema_json = json.load(file)
file.close()

result = generate(schema_json, first=True)

file = open("schema_result.json", "w")
json.dump(result, file, indent=4)
file.close()