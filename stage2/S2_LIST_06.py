# stage2/S2_LIST_06.py

def get_active_user_names(users):
    # if user active take the name and make it upper case and 
    # sort the list

    active_names = [user["name"].upper() for user in users if user["active"]]

    return sorted(active_names)

def main():
    users = [
        {"id": 1, "name": "alice", "active": True},
        {"id": 2, "name": "bob", "active": False},
        {"id": 3, "name": "charlie", "active": True},
        {"id": 4, "name": "david", "active": True},
        {"id": 5, "name": "eve", "active": False}
    ]

    result = get_active_user_names(users)

    print(f"Original User Records: {users}")
    print(f"Active User Names (Upper & Sorted): {result}")

if __name__ == "__main__":
    main()