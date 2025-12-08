export type Matrix<T> = T[][];
export function transposeMatrix<T>(matrix: Matrix<T>): Matrix<T> {
  if (matrix.length === 0) return [];

  const transposed: T[][] = [];
  const rows = matrix.length;
  const cols = matrix[0].length;

  for (let col = 0; col < cols; col++) {
    const newRow: T[] = [];
    for (let row = 0; row < rows; row++) {
      newRow.push(matrix[row][col]);
    }
    transposed.push(newRow);
  }

  return transposed;
}
