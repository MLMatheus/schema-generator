import json

def generate(obj: dict, list_type=False):
    dictionary = {}

    if list_type:
        dictionary['type'] = 'object'
        for item in obj:
            dictionary['properties'] = generate(item)
        return dictionary

    for key in obj.keys():
        data_type = {
            type(''): 'string',
            type(54.0): 'number',
            type({}): 'object',
            type(54): 'integer',
            type([]): 'array'
        }

        dic2 = {}

        if data_type[type(obj[key])] == 'object':
            dic2['type'] = 'object'
            dic2['properties'] = generate(obj[key])
        elif data_type[type(obj[key])] == "array":
            dic2['type'] = 'array'
            dic2['itens'] = generate(obj[key], True)
        else:
            dic2['type'] = data_type[type(obj[key])]
        dictionary[key] = dic2
    dictionary['required'] = [k for k in obj.keys()]
    return dictionary

file = open("schema.json", "r")

schema_json = json.load(file)
file.close()

result = generate(schema_json)

file = open("schema_result.json", "w")
json.dump(result, file, indent=4)
file.close()