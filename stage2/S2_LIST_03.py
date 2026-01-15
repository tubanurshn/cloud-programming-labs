# stage2/S2_LIST_03.py


def chunk(lst, size):

    if size <= 0:
        return None

    chunks = []

    for i in range(0, len(lst), size):
        chunks.append(lst[i:i + size])

    return chunks


def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f"Chunk size 3: {chunk(my_list, 3)}")

    print(f"Chunk size 5: {chunk(my_list, 5)}")

    print(f"Chunk size 0: {chunk(my_list, 0)}")


if __name__ == "__main__":
    main()
