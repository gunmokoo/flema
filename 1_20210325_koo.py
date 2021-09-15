import pygame # 파이게임 불러오기(이거 지우는 얘는 없겠지)

pygame.init() # 초기화(이거 지우는 얘는 없겠지)

screen_w = 1280 # 화면 넓이
screen_h = 720  # 화면 높이
screen = pygame.display.set_mode((screen_w, screen_h)) # 화면 생성

pygame.display.set_caption("일조") # 타이틀 제목

background = pygame.image.load("C:/Users/owner/Desktop/PythonWorkspace/flema/배경1.jpg") # 배경 그림 불러오기

menu = pygame.image.load("C:/Users/owner/Desktop/PythonWorkspace/flema/배경2.jpg") # 메뉴 그림 불러오기
menu_size = menu.get_rect().size # 메뉴 이미지의 크기를 구해옴
menu_w = menu_size[0] # 메뉴의 가로 크기
menu_h = menu_size[1] # 메뉴의 세로 크기
menu_x_pos = 0 # 메뉴 x 좌표
menu_y_pos = 180 # 메뉴 y 좌표

setting = pygame.image.load("C:/Users/owner/Desktop/PythonWorkspace/flema/배경3.jpg") # 설정 그림 불러오기
setting_size = setting.get_rect().size # 설정 이미지의 크기를 구해옴
setting_w = setting_size[0] # 설정 가로 크기
setting_h = setting_size[1] # 설정 세로 크기

album = pygame.image.load("C:/Users/owner/Desktop/PythonWorkspace/flema/배경4.jpg") # 앨범 그림 불러오기
album_size = album.get_rect().size # 앨범 이미지의 크기를 구해옴
album_w = album_size[0] # 앨범 가로 크기
album_h = album_size[1] # 앨범 세로 크기

arrowr = pygame.image.load("C:/Users/owner/Desktop/PythonWorkspace/flema/배경5.jpg") # 오른쪽 화살표 그림 불러오기
aroowr_size = arrowr.get_rect().size # 오른쪽 화살표 이미지의 크기를 구해옴
arrowr_w = aroowr_size[0] # 오른쪽 화살표 가로 크기
arrowr_h = aroowr_size[1] # 오른쪽 화살표 세로 크기

arrowl = pygame.image.load("C:/Users/owner/Desktop/PythonWorkspace/flema/배경6.jpg") # 왼쪽 화살표 그림 불러오기
aroowl_size = arrowl.get_rect().size # 왼쪽 화살표 이미지의 크기를 구해옴
arrowl_w = aroowl_size[0] # 왼쪽 화살표 가로 크기
arrowl_h = aroowl_size[1] # 왼쪽 화살표 세로 크기

running = True # 게임이 진행중인지
while running: # True 시 진행 False 시 종료
    for event in pygame.event.get(): # 이거해야 이벤트 할수있어(이거 지우는 얘는 없겠지)
        if event.type == pygame.QUIT: # 타이틀 제목 오른쪽 x누르면 종료 
            running = False # 게임 끌게



    screen.blit(background, (0, 0)) # 0, 0 좌표에 배경 불러오기
    screen.blit(menu, (menu_x_pos, menu_y_pos)) # 좌표에 메뉴 불러오기
    screen.blit(setting, (1110, 50)) # 좌표에 설정 불러오기
    screen.blit(album, (435, 247.5)) # 좌표에 앨범 불러오기
    screen.blit(arrowr, (1030, 350)) # 좌표에 오른쪽 화살표 불러오기   
    screen.blit(arrowl, (50, 350)) # 좌표에 왼쪽 화살표 불러오기

    pygame.display.update() # 이거 해야 화면이 유지된다(이거 지우는 얘는 없겠지)

pygame.quit() # 위 와일 문 탈출 시 이놈이 게임 끈다(이거 지우는 얘는 없겠지)