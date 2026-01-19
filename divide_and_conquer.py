# Divide and Conquer: Python implementations
# Algorithms: QuickSort, MergeSort, Closest Pair of Points, Standard Matrix Multiply, Strassen's Algorithm

# -------------------------------------------------
# Closest Pair of Points (Divide and Conquer, O(n log n))
# -------------------------------------------------
Point = Tuple[float, float]

def closest_pair(points: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
    """Return (distance, (p1, p2)) for closest pair among points."""
    if len(points) < 2:
        return inf, (None, None)

    pts_sorted_x = sorted(points, key=lambda p: (p[0], p[1]))
    pts_sorted_y = sorted(points, key=lambda p: (p[1], p[0]))

    def dist(p: Point, q: Point) -> float:
        return sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

    def brute_force(pts: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
        best = inf
        pair = (None, None)
        n = len(pts)
        for i in range(n):
            for j in range(i + 1, n):
                d = dist(pts[i], pts[j])
                if d < best:
                    best = d
                    pair = (pts[i], pts[j])
        return best, pair

    def strip_closest(strip: List[Point], d: float) -> Tuple[float, Tuple[Point, Point]]:
        # strip is sorted by y; check up to next ~7 points
        best = d
        best_pair = (None, None)
        n = len(strip)
        for i in range(n):
            j = i + 1
            while j < n and (strip[j][1] - strip[i][1]) < best:
                dd = dist(strip[i], strip[j])
                if dd < best:
                    best = dd
                    best_pair = (strip[i], strip[j])
                j += 1
        return best, best_pair

    def _closest(px: List[Point], py: List[Point]) -> Tuple[float, Tuple[Point, Point]]:
        n = len(px)
        if n <= 3:
            return brute_force(px)

        mid = n // 2
        mid_x = px[mid][0]
        Qx = px[:mid]
        Rx = px[mid:]

        Qy, Ry = [], []
        for p in py:
            if p[0] <= mid_x:
                Qy.append(p)
            else:
                Ry.append(p)

        dl, pair_l = _closest(Qx, Qy)
        dr, pair_r = _closest(Rx, Ry)
        d = dl if dl < dr else dr
        best_pair = pair_l if dl < dr else pair_r

        strip = [p for p in py if abs(p[0] - mid_x) < d]
        ds, pair_s = strip_closest(strip, d)
        if ds < d:
            return ds, pair_s
        return d, best_pair

    return _closest(pts_sorted_x, pts_sorted_y)


# -----------------------------------------
# Standard Matrix Multiplication (O(n^3))
# -----------------------------------------
Matrix = List[List[float]]

def matmul_standard(A: Matrix, B: Matrix) -> Matrix:
    """Standard triple-loop matrix multiplication."""
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    assert m == len(B), "Incompatible dimensions for multiplication."
    C = [[0.0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = A[i][k]
            for j in range(p):
                C[i][j] += aik * B[k][j]
    return C


# -----------------------------------------
# Strassen's Matrix Multiplication (O(n^2.81))
# -----------------------------------------
def add_matrix(A: Matrix, B: Matrix) -> Matrix:
    n = len(A); m = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

def sub_matrix(A: Matrix, B: Matrix) -> Matrix:
    n = len(A); m = len(A[0])
    return [[A[i][j] - B[i][j] for j in range(m)] for i in range(n)]

def split_quadrants(A: Matrix) -> Tuple[Matrix, Matrix, Matrix, Matrix]:
    n = len(A)
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

def combine_quadrants(C11: Matrix, C12: Matrix, C21: Matrix, C22: Matrix) -> Matrix:
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

def next_power_of_two(n: int) -> int:
    return 1 if n == 0 else 2 ** ceil(log2(n))

def pad_matrix(A: Matrix, size: int) -> Matrix:
    n = len(A); m = len(A[0])
    P = [[0.0] * size for _ in range(size)]
    for i in range(n):
        for j in range(m):
            P[i][j] = A[i][j]
    return P

def unpad_matrix(A: Matrix, rows: int, cols: int) -> Matrix:
    return [row[:cols] for row in A[:rows]]

def strassen(A: Matrix, B: Matrix, threshold: int = 64) -> Matrix:
    """
    Strassen's algorithm with padding to power-of-two and threshold for switching to standard.
    A: n x m, B: m x p
    """
    n, m = len(A), len(A[0])
    m2, p = len(B), len(B[0])
    assert m == m2, "Incompatible dimensions for multiplication."

    # Pad to square power-of-two
    s = max(n, m, p)
    S = next_power_of_two(s)
    Ap = pad_matrix(A, S)
    Bp = pad_matrix(B, S)

    Cp = _strassen_recursive(Ap, Bp, threshold)

    # Unpad to original size
    return unpad_matrix(Cp, n, p)

def _strassen_recursive(A: Matrix, B: Matrix, threshold: int) -> Matrix:
    n = len(A)
    if n <= threshold:
        return matmul_standard(A, B)
    if n % 2 != 0:
        # pad one level if needed
        A = pad_matrix(A, n + 1)
        B = pad_matrix(B, n + 1)
        n += 1

    A11, A12, A21, A22 = split_quadrants(A)
    B11, B12, B21, B22 = split_quadrants(B)

    # Strassen's seven products:
    M1 = _strassen_recursive(add_matrix(A11, A22), add_matrix(B11, B22), threshold)
    M2 = _strassen_recursive(add_matrix(A21, A22), B11, threshold)
    M3 = _strassen_recursive(A11, sub_matrix(B12, B22), threshold)
    M4 = _strassen_recursive(A22, sub_matrix(B21, B11), threshold)
    M5 = _strassen_recursive(add_matrix(A11, A12), B22, threshold)
    M6 = _strassen_recursive(sub_matrix(A21, A11), add_matrix(B11, B12), threshold)
    M7 = _strassen_recursive(sub_matrix(A12, A22), add_matrix(B21, B22), threshold)

    # Combine into C quadrants:
    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    return combine_quadrants(C11, C12, C21, C22)


# -----------------------------
# Example usage and quick tests
# -----------------------------
if __name__ == "__main__":
    # QuickSort
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("QuickSort:", quick_sort(arr))

    # MergeSort
    print("MergeSort:", merge_sort(arr))

    # Closest Pair of Points
    pts = [(2.0, 3.0), (12.0, 30.0), (40.0, 50.0), (5.0, 1.0), (12.0, 10.0), (3.0, 4.0)]
    d, pair = closest_pair(pts)
    print("Closest Pair distance:", d, "pair:", pair)

    # Standard Matrix Multiply
    A = [[2, 3],
         [1, 4]]
    B = [[1, 6],
         [4, 2]]
    print("Standard matmul:", matmul_standard(A, B))

    # Strassen (works for any rectangular sizes via padding)
    print("Strassen matmul:", strassen(A, B))
