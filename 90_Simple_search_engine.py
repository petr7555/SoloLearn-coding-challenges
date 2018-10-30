import json


def nice_print(document):
    print(json.dumps(document, sort_keys=True, indent=4))


with open("people.json") as file:
    text = file.read()

collection = json.loads(text)
max_id = 0
for document in collection:
    if document["id"] > max_id:
        max_id = document["id"]
print("Fields are: ")
for key in collection[0]:
    print("   " + key)
print("Query options are: GET, POST, PUT, DELETE.")
while True:
    query = input("Enter query: \n")
    if query.lower() == "break":
        break
    elif query.upper() == "POST":
        max_id += 1
        collection.append(
            {'id': max_id, 'first_name': input('first_name: '), 'last_name': input('last_name: '),
             'email': input('email: '), 'gender': input('gender: ')})
        nice_print(collection)
    elif query[:3].upper() == "PUT":
        command, doc_id, q = query.split()
        field, value = q.split("=")
        for document in collection:
            if document["id"] == int(doc_id):
                document[field.lower()] = value
                nice_print(document)
    else:
        command, q = query.split()
        command = command.upper()
        q = q.lower()
        if q == "all":
            nice_print(collection)
            continue
        field, value = q.split("=")
        if command == "GET":
            if field == "id":
                for document in collection:
                    if document[field] == int(value):
                        nice_print(document)
            else:
                for document in collection:
                    if document[field].lower() == value:
                        nice_print(document)
        elif command == "DELETE":
            collection = [document for document in collection if not document[field].lower() == value]
            nice_print(collection)
