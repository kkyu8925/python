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

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 이벤트 발생했는지 체크
        if event.type == pygame.QUIT:  # 창닫기
            running = False  # 게임 실행종료

    # screen.fill((0,0,0))
    screen.blit(background, (0, 0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 게임화면을 다시 그리기


# pygame 종료
pygame.quit()
