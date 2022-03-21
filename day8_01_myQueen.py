def myqueen(n):
    answer = []
    count = 0
    visited = [-1]*n

    def check(row):
        for r in range(row):
            # 같은 열에 있거나 대각선
            if visited[r] == visited[row] or row - r == abs(visited[row] - visited[r]):
                return False
            # print(1) # row가 0일때 for를 안돌아서 여긴 실행조차 안됨
        return True

    def dfs(row):
        # count 언제?
        if n == row: # if문 먼저(순서)
            nonlocal count
            count+=1
            print('count:',count)
            grid = [['.'] * n for _ in range(n)]  # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

            for idx, val in enumerate(visited):
                grid[idx][val] = 'Q'

            temp = []
            for row in grid:
                temp.append(''.join(row))
            answer.append(temp)
            print('answer:',answer)
            return
        for col in range(n):
            visited[row] = col # 에러 row = 4 <- 답하나 찾고 return안해줘서
            print('row:',row,'col:',col)
            if check(row): # col
                # Q 놓기 ----- 여기서 넣고싶은데 later
                # grid[row][col] = 'Q'
                print('before recur')
                dfs(row+1)
        return

    dfs(0)
    return answer # [[".Q..","...Q","Q...","..Q."],

# assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
# assert myqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
print(myqueen(4))