import heapq

# from heap.structures import BinaryMaxHeap
from day11_L215_KthLargest import BinaryMaxHeap

# 직접 구현한 힙
def test_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()  # 힙을 생성

    # for 문을 눈여겨봐두세요.
    # 힙정렬 시간복잡도 계산의 토대입니다.
    for elem in lst:
        maxheap.insert(elem)  # 넣는 족족 힙을 유지되면서 들어가
    # ^- 끝나면 리스트의 모든 요소들이 힙에 들어가 있음

    # max힙에서 값을 추출 x K번 => K번째 큰 요소
    # 앞에 리스트에 [첫번째 큰 요소, 2번째 큰요소 .. K번째 큰 요소] 들어가 있음 -> 가장 마지막에 있는 요소(k-1)
    return [maxheap.extract() for _ in range(k)][k - 1]

# 내장된 힙큐 - 문제풀때는 사용
def test_maxheap_heapq(lst, k):
    # 공식문서 https://docs.python.org/ko/3/library/heapq.html
    # 파이썬의 힙: 최소힙, 0부터 인덱싱
    # pop 메서드는 가장 큰 항목이 아닌 가장 작은 항목을 반환
    return heapq.nlargest(k, lst)[-1]  # nlargest: 주어진 리스트에서 k번째로 큰요소까지 리스트로


# 우리가 만든 힙 사용
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1

# 내장된 힙 사용
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1

# 내가 만든 힙 테스트