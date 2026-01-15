# stage3/S3_DICT_06.py


def group_by(items, key):
    groups = {}
    for item in items:
        val = item.get(key)
        if val not in groups:
            groups[val] = []
        groups[val].append(item)
    return groups


users = [{
    "name": "A",
    "city": "IST"
}, {
    "name": "B",
    "city": "ANK"
}, {
    "name": "C",
    "city": "IST"
}]
print(f"Grouped by city: {group_by(users, 'city')}")
