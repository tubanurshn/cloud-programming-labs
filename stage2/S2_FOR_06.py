# stage2/S2_FOR_06.py


def sum_nested(matrix):
  if not isinstance(matrix, list):
    return None

  total = 0

  for row in matrix:
    if not isinstance(row, list):
      return None

    for value in row:
      if isinstance(value, (int, float)):
        total += value
      else:

        continue

  return total


def main():
  matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  matrix2 = [[1, 2], "geçersiz satır", [3, 4]]

  print(f"Sum of Matrix 1: {sum_nested(matrix1)}")
  print(f"Sum of Matrix 2: {sum_nested(matrix2)}")


if __name__ == "__main__":
  main()
