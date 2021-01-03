import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/python-study/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/python-study/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지 크기 구하기
character_width = character_size[0]  # 캐릭터 가로 크기
character_heigth = character_size[1]  # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 캐릭터 가로 위치
character_y_pos = screen_height - character_heigth  # 캐릭터 세로 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 이벤트 발생했는지 체크
        if event.type == pygame.QUIT:  # 창닫기
            running = False  # 게임 실행종료

        if event.type == pygame.KEYDOWN:  # 키보드 방향키 입력
            if event.key == pygame.K_LEFT:  # 왼쪽으로
                to_x -= 1
            elif event.key == pygame.K_RIGHT:  # 오른쪽으로
                to_x += 1
            elif event.key == pygame.K_UP:  # 위쪽으로
                to_y -= 1
            elif event.key == pygame.K_DOWN:  # 아래쪽으로
                to_y += 1

        if event.type == pygame.KEYUP:  # 키보드 방향키 입력종료
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_heigth:
        character_y_pos = screen_height - character_heigth

    # screen.fill((0,0,0))
    screen.blit(background, (0, 0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()
