# stage3/S3_PIPE_04.py

def stream_pipeline(data):
    def clean_step(items):
        for item in items:
            try:
                yield float(str(item).strip())
            except (ValueError, TypeError):
                continue

    def double_step(nums):
        for n in nums:
            yield n * 2

    cleaned = clean_step(data)
    doubled = double_step(cleaned)

    return sum(doubled)

raw_data = [" 1.5 ", "junk", "2", " 3 "]
print(f"Total: {stream_pipeline(raw_data)}")