# stage3/S3_PIPE_05.py


def parse_logs(lines):
    user_ids = []
    for line in lines:
        if not line.startswith("INFO:"):
            continue

        try:

            parts = line.split()
            user_part = [p for p in parts if p.startswith("user=")][0]
            user_id = int(user_part.split("=")[1])
            user_ids.append(user_id)
        except (IndexError, ValueError):
            continue

    return user_ids


log_data = [
    "INFO: user=42 action=login", "ERROR: user=99 action=fail",
    "INFO: user=10 action=logout"
]
print(f"Extracted User IDs: {parse_logs(log_data)}")
