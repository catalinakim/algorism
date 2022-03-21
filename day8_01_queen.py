def nqueen(n):  # 혼자서 다시 직접 구현! 손에 익히기! -> 발상, 구현력
    """
    visited 의 인덱스는 행, 값은 열을 나타낸다.
    (1, 3)에 놓은 경우, visited[1] = 3 으로 표현하겠다는 것.

    예시) n=4 이고 visited = [1, 3, 0, 2] 인 경우,
    체스판을 그려보면 아래와 같다. (1이 퀸)
    0 1 0 0
    0 0 0 1
    1 0 0 0
    0 0 1 0
    """
    visited = [-1] * n  # tip! 시간복잡도 n^2 -> n
    cnt = 0             # print용
    answers = []

    def is_ok_on(nth_row): #n번째 row에 지금 queen을 놓을 수 있는 상태야?
        """
        n번째(nth) 행에 퀸을 놓았을 때, 올바른 수인지 검사한다.
        nth 행의 퀸 위치와, 0번째 행부터 n-1번째 행까지 놓여진 퀸의 위치를 비교한다.
        nth 행에 놓여진 퀸이 규칙을 깼다면 False 를 반환한다.
        """
        # 0번째 행 ~ nth_row-1번째 행의 퀸 위치를 차례대로 꺼내온다.(지금까지 둔 수를 한번 검사)
        # 영상에서 n-1이라고 말하는데 오류입니다. nth_row-1까지 살펴봅니다.
        for row in range(nth_row):
            # 방금 놓여진 nth 퀸은 (nth_row, visited[nth_row]) 에 놓여져있다.
            # 각 행에 차례대로 단 한 번만 두기 때문에 행이 겹치는 것은 검사하지 않아도 된다.
            # 1) 열 번호가 (이전에 뒀던 열과) 겹치지는 않는지? visited[nth_row] == visited[row]:
            # 2) 또는 대각선으로 존재하지는 않는지? nth_row - row == abs(visited[nth_row] - visited[row]) 살펴본다.
            #                                 행의 거리수와 열의 거리수가 같은지, nth_row>row이므로 왼쪽은 절대값 안함
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False
        return True

    def dfs(row): # row번째 행에 퀸을 두는 동작
        """
        row 는 퀸을 놓을 행번호를 의미한다.
        dfs(0) 은 0번째 행에서 퀸의 위치를 고르는 것이고,
        dfs(1) 은 1번째 행에서 퀸의 위치를 고르는 것이고,
        ...
        dfs(n-1) 은 n-1번째 행에서 퀸의 위치를 고르는 것이다.
        따라서 row 는 n-1까지 가능하며, n이 되었다는 것은 n개의 퀸을 모두 올바른 위치에 두었다는 의미이다.
        """

        # 0 ~ n-1 행에 퀸을 모두 하나씩 두었을 때 경우의 수를 1 증가시키고 재귀탐색을 종료한다.
        if row >= n:  # ==도 가능 but 재귀적 코드 안전하게 >= 사용함
            # nonlocal 은 지역변수가 아님을 의미한다. 밖에있는거 갖다쓴거야
            nonlocal cnt 
            cnt += 1  # 경우의 수 1증가
            print('count:', cnt)
            print("*" * 80)
            print(f"{cnt}번째 답 - visited: {visited}")
            # 그림으로 그리는 작업 .이 4개 있는 배열 만들고, n번 반복해라
            grid = [['.'] * n for _ in range(n)]  # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
            for idx, value in enumerate(visited):
                   grid[idx][value] = 'Q'  # 각 좌표값에 Q찍어줘
            result = [] # 결과 하나
            for row in grid:
                print(row)  # 인쇄
                result.append(''.join(row)) # 정답에 추가, Join: 배열에 있는 요소를 합친 문자열 반환
            answers.append(result)
            return

        # visited[row] 의 값을 결정한다.
        # n*n 의 체스판이므로 가능한 열의 범위는 0 ~ n-1 이다.
        for col in range(n):   # 행번호는 정해졌으니까, 열번호만 정하면 되, 열범위를 0부터 n-1까지 전부실험해보기
            # (row, col) 위치에 퀸을 두었다고 가정하고, 규칙을 깨지 않는다면 row+1 행에 다시 퀸을 둔다.
            # row = 0
            # col = 0
            visited[row] = col # row번째에 0부터 n-1까지 쫙 둬봐,
            # visited[0] = 0
            print('row:', row, 'col:', col)
            if is_ok_on(row):
                print('before recur')
                dfs(row + 1)   # 괜찮으면 다음번(다음줄)째 수를 둬
        print(' __close')
    # 0번째 행에 퀸을 둔다.
    dfs(0)
    return answers


assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
# assert myqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]