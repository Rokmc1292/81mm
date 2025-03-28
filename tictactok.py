# 2022041018 김태욱
# 틱택톡 게임 만들기
import pygame
import sys
import math

# 초기 설정
pygame.init()
# 화면크기
WIDTH, HEIGHT = 300, 300
# 각 칸을 구분하는 선의 색깔 - 검정색
LINE_COLOR = (0, 0, 0)
# 배경색 - 흰색
BACKGROUND_COLOR = (255, 255, 255)
# 플레이어의 o 색깔 - 파란색
CIRCLE_COLOR = (0, 0, 255)
# AI의 x 색깔 - 빨간색색
CROSS_COLOR = (255, 0, 0)
# 선의 두께
LINE_WIDTH = 5
# 보드의 크기 
BOARD_ROWS, BOARD_COLS = 3, 3
# 한칸의 크기
CELL_SIZE = WIDTH // BOARD_COLS

# 보드 생성 - 각 칸은 None으로 비어있다
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# 피그마를 이용하여 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 창 상단에 표시할 이름
pygame.display.set_caption("Tic-Tac-Toe AI")
# 화면을 흰색으로 채운다
screen.fill(BACKGROUND_COLOR)

# 화면 그리는 함수
def draw_lines():
    for i in range(1, BOARD_ROWS):
        # 가로선 그리기
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        # 세로선 그리기
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)

# O,X 그리는 함수
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3, LINE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + 20, row * CELL_SIZE + 20), (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + CELL_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + 20, row * CELL_SIZE + CELL_SIZE - 20), (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + 20), LINE_WIDTH)

# 남은칸 찾는 함수
def available_moves():
    return [(r, c) for r in range(BOARD_ROWS) for c in range(BOARD_COLS) if board[r][c] is None]

# 누가 이겼는지 찾는 함수
def check_winner(player):
    # 가로로 빙고 완성했을때
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            return True
    # 세로로 빙고 완성했을때 
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True
    # 두경우의 대각선중 하나 완성했을때
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_ROWS - 1 - i] == player for i in range(BOARD_ROWS)):
        return True
    return False

def minimax(player):
    opponent = 'O' if player == 'X' else 'X'
    if check_winner('X'):
        return 1
    elif check_winner('O'):
        return -1
    elif not available_moves():
        return 0

    moves = []
    for r, c in available_moves():
        board[r][c] = player
        score = minimax(opponent)
        board[r][c] = None
        moves.append((score, (r, c)))
    
    return max(moves)[0] if player == 'X' else min(moves)[0]

def best_move():
    best_score = -math.inf
    move = None
    for r, c in available_moves():
        board[r][c] = 'X'
        score = minimax('O')
        board[r][c] = None
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

running = True
player_turn = True  # 플레이어가 먼저 시작

draw_lines()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if player_turn and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] is None:
                board[row][col] = 'O'
                player_turn = False
                if check_winner('O'):
                    print("Player wins!")
                    running = False
                elif not available_moves():
                    print("Draw!")
                    running = False
    
    if not player_turn and running:
        move = best_move()
        if move:
            board[move[0]][move[1]] = 'X'
            if check_winner('X'):
                print("AI wins!")
                running = False
            elif not available_moves():
                print("Draw!")
                running = False
        player_turn = True

    screen.fill(BACKGROUND_COLOR)
    draw_lines()
    draw_figures()
    pygame.display.update()

pygame.quit()
