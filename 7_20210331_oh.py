import pygame # 파이게임 불러오기(이거 지우는 얘는 없겠지)
import time # sleep(몇초 쉬었다 실행하는거) 쓰기 위해서 
from random import * # 랜덤함수 사용 가능

pygame.init() # 초기화(이거 지우는 얘는 없겠지)

screen_w = 1280 # 화면 넓이
screen_h = 720  # 화면 높이
screen = pygame.display.set_mode((screen_w, screen_h)) # 화면 생성

pygame.display.set_caption("일조") # 타이틀 제목

clock = pygame.time.Clock() #프레임 설정 *이거 나중에 필요함

background = pygame.image.load("C:/PythonWorkspace/flema/배경1.jpg") # 배경 그림 불러오기

menu = pygame.image.load("C:/PythonWorkspace/flema/배경2.jpg") # 메뉴 그림 불러오기
menu_size = menu.get_rect().size # 메뉴 이미지의 크기를 구해옴
menu_w = menu_size[0] # 메뉴의 가로 크기
menu_h = menu_size[1] # 메뉴의 세로 크기
menu_x_pos = 0 # 메뉴 x 좌표
menu_y_pos = 180 # 메뉴 y 좌표

setting = pygame.image.load("C:/PythonWorkspace/flema/배경3.jpg") # 설정 그림 불러오기
setting_size = setting.get_rect().size # 설정 이미지의 크기를 구해옴
setting_w = setting_size[0] # 설정 가로 크기
setting_h = setting_size[1] # 설정 세로 크기

setscreen = pygame.image.load("C:/PythonWorkspace/flema/설정화면.png") #설정화면 그림 불러오기
setscreen_size = setscreen.get_rect().size # 설정 이미지의 크기를 구해옴
setscreen_w = setscreen_size[0] # 설정화면 가로 크기
setscreen_h = setscreen_size[1] # 설정화면 세로 크기


arrowr = pygame.image.load("C:/PythonWorkspace/flema/배경5.jpg") # 오른쪽 화살표 그림 불러오기
aroowr_size = arrowr.get_rect().size # 오른쪽 화살표 이미지의 크기를 구해옴
arrowr_w = aroowr_size[0] # 오른쪽 화살표 가로 크기
arrowr_h = aroowr_size[1] # 오른쪽 화살표 세로 크기

arrowl = pygame.image.load("C:/PythonWorkspace/flema/배경6.jpg") # 왼쪽 화살표 그림 불러오기
aroowl_size = arrowl.get_rect().size # 왼쪽 화살표 이미지의 크기를 구해옴
arrowl_w = aroowl_size[0] # 왼쪽 화살표 가로 크기
arrowl_h = aroowl_size[1] # 왼쪽 화살표 세로 크기

yes_button = pygame.image.load("C:/PythonWorkspace/flema/예.png") # 예쓰버튼 그림 불러오기
yes_button_size = yes_button.get_rect().size # 설정 이미지의 크기를 구해옴
yes_button_w = yes_button_size[0] # 설정 가로 크기
yes_button_h = yes_button_size[1] # 설정 세로 크기

no_button = pygame.image.load("C:/PythonWorkspace/flema/아니오.png") # 노버튼 그림 불러오기
no_button_size = no_button.get_rect().size # 설정 이미지의 크기를 구해옴
no_button_w = no_button_size[0] # 설정 가로 크기
no_button_h = no_button_size[1] # 설정 세로 크기

game_background = pygame.image.load("C:/PythonWorkspace/flema/게임1.jpg") # 게임 배경화면 그림 불러오기
game_background_size = game_background.get_rect().size # 게임 배경화면 이미지의 크기를 구해옴
game_background_w = game_background_size[0] # 게임 배경화면 가로 크기
game_background_h = game_background_size[1] # 게임 배경화면 세로 크기

game_screen = pygame.image.load("C:/PythonWorkspace/flema/게임2.jpg") # 게임 스크린 그림 불러오기
game_screen_size = game_screen.get_rect().size # 게임 스크린 이미지의 크기를 구해옴
game_screen_w = game_screen_size[0] # 게임 스크린 가로 크기
game_screen_h = game_screen_size[1] # 게임 스크린 세로 크기

game_bar = pygame.image.load("C:/PythonWorkspace/flema/게임3.jpg") # 바 그림 불러오기
game_bar_size = game_bar.get_rect().size # 바 이미지의 크기를 구해옴
game_bar_w = game_bar_size[0] # 바 가로 크기
game_bar_h = game_bar_size[1] # 바 세로 

back_button = pygame.image.load("C:/PythonWorkspace/flema/이전.jpg") # 바 그림 불러오기
back_button_size = back_button.get_rect().size # 바 이미지의 크기를 구해옴
back_button_w = back_button_size[0] # 바 가로 크기
back_button_h = back_button_size[1] # 바 세로

game_down = pygame.image.load("C:/PythonWorkspace/flema/게임4.jpg") # 떨어지는 바 그림 불러오기
game_down_size = game_down.get_rect().size # 떨어지는 바 이미지의 크기를 구해옴[]
game_down_w = game_down_size[0] # 떨어지는 바 가로 크기
game_down_h = game_down_size[1] # 떨어지는 바 세로 크기
game_down_y_pos = -100 # 떨어지는 바 y 값
game_down_speed = 10 # 떨어지는 바 속도

album_num = 1 # 앨범 순서 정하기
LEFT = 1 #마우스 왼쪽클릭
RIGHT = 3 #마우스 오른쪽 클릭

back_button_screen = 0
yes_no = 0 # yes no 버튼 불러오기 위한 변수
setting_screen = 0 # 설정화면을 불러오기 위한 변수
game = 0 # 게임 화면을 불러오기 위한 변수


running = True # 게임이 진행중인지
while running: # True 시 진행 False 시 종료
    dt = clock.tick(60) #게임 진행하는동안 60프레임으로 고정 *이거 나중에 필요함
    
    
    album = pygame.image.load("C:/PythonWorkspace/flema/앨범{0}.jpg".format(album_num)) # 앨범 그림 불러오기
    album_size = album.get_rect().size # 앨범 이미지의 크기를 구해옴
    album_w = album_size[0] # 앨범 가로 크기
    album_h = album_size[1] # 앨범 세로 크기

    if yes_no >= 1:
        yn_album_h = album_h / 2    #예스 or 노 가 떴을때 앨범 움직이지 않게 하기위한것
        yn_no_button_h = no_button_h # 이하 동문
        yn_no_button_w = no_button_w # 이하 동문
        yn_album_w = album_w # 이하 동문
        yn_yes_button_h = yes_button_h # 이하 동문
        yn_yes_button_w = yes_button_w # 이하 동문
    else:
        yn_album_h = 0 # 이하 동문
        yn_no_button_h = 0 # 이하 동문
        yn_no_button_w = 0 # 이하 동문
        yn_album_w = 0 # 이하 동문
        yn_yes_button_h = 0 # 이하 동문
        yn_yes_button_w = 0 # 이하 동문

    
    
    for event in pygame.event.get(): # 이거해야 이벤트 할수있어(이거 지우는 얘는 없겠지)

        if event.type == pygame.QUIT: # 타이틀 제목 오른쪽 x누르면 종료 
            running = False # 게임 끌게
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT: # 마우스  왼쪽 클릭 이벤트 발생하면
            mousepos = pygame.mouse.get_pos() #마우스 위치를 받고
            if yes_no == 0:
                if 1030 <= mousepos[0] <= 1230 and 350 <= mousepos[1] <= 550: #마우스의 위치가 오른쪽 화살표의 위치 면
                    if album_num <=2: #앨범 순서가 2보다 작거나 같을때
                        album_num += 1 #앨범 순서를 다음으로 넘김
                if 50 <= mousepos[0] <= 250 and 350 <= mousepos[1] <= 550: #마우스의 위치가 왼쪽 화살표의 위치 면
                    if album_num >=2: #앨범 순서가 2보다 크거나 같을떄
                        album_num -= 1 #앨범 순서를 이전으로 넘김
                if 435  <= mousepos[0] <= 435 + album_w and 247.5 <= mousepos[1] <= 247.5 + album_w: # 엘범을 클릭 했을때
                    yes_no += 1 # 변수에 1을 더함
            if 435 + (yn_album_h) + ( yn_no_button_h /2) <= mousepos[0] <= 435 + (yn_album_h) + ( yn_no_button_h /2) + yn_no_button_w \
            and yn_album_w <=mousepos[1] <= yn_album_w + yn_no_button_h: # 아니오 버튼 클릭 좌표 
                    yes_no = 0
            if 435 + (yn_album_h) - ( yn_yes_button_h *2.5) <= mousepos[0] <= 435 + (yn_album_h) - ( yn_yes_button_h *2.5) + yn_yes_button_w \
            and yn_album_w <=mousepos[1] <= yn_album_w + yn_yes_button_h: # 예 버튼 클릭 좌 
                    yes_no = 0
                    game += 1                  
            if 1110 <= mousepos[0] <= 1110 + setscreen_w and 50 <= mousepos[1] <= 50 + setting_h: #설정 클릭 했을때
                setting_screen += 1 #setting_screen 변수에 1을 저장
                back_button_screen += 1 #back_button_screen 변수에 1을 저장
                yes_no = -1 # 설정 눌렀을때 yes no 가 안뜨게하기위해서 -1로 지정
            if screen_w / 2 +(setscreen_w/2) - back_button_w <= mousepos[0] <=screen_w / 2 +(setscreen_w/2) \
                and screen_h/2 - (setscreen_h/2) <=mousepos[1] <= screen_h/2 - (setscreen_h/2) + back_button_w: # 뒤로가기 버튼 클릭했을때
                    setting_screen = 0  # 세팅스크린 0으로 저장
                    back_button_screen = 0 # 버튼 0으로저장
                    yes_no = 0 # -1로 돼어있던것을 0으로 저장

    

   
    screen.blit(background, (0, 0)) # 0, 0 좌표에 배경 불러오기
    screen.blit(menu, (menu_x_pos, menu_y_pos)) # 좌표에 메뉴 불러오기
    screen.blit(setting, (1110, 50)) # 좌표에 설정 불러오기
    screen.blit(album,(435,247.5)) #앨범 불러오기
    screen.blit(arrowr, (1030, 350)) # 좌표에 오른쪽 화살표 불러오기
    screen.blit(arrowl, (50, 350)) # 좌표에 왼쪽 화살표 불러오기
    if yes_no >= 1: # 변수가 1이상 일 때
        screen.blit(yes_button, ( 435 + (album_h / 2) - ( yes_button_h *2.5)    , album_w )) # 예 버튼 불러오기
        screen.blit(no_button, ( 435 + (album_h / 2) + ( yes_button_h /2)    , album_w )) # 아니오 버튼 불러오기
    if setting_screen >=1: # 변수가 1이상 일 때
        screen.blit(setscreen, (screen_w / 2 -(setscreen_w/2), screen_h/2 - (setscreen_h/2))) # 설정 화면 불러오기
    if back_button_screen >=1:
        screen.blit(back_button, (screen_w / 2 +(setscreen_w/2) - back_button_w , screen_h/2 - (setscreen_h/2)))
    if game >=1: # 변수가 1이상 일 때
        screen.blit(game_background, (0, 0)) # 게임 배경화면 불러오기
        screen.blit(game_screen, (290, 0)) # 게임 스크린 불러오기
        screen.blit(game_screen, (430, 0)) # 게임 스크린 불러오기
        screen.blit(game_screen, (570, 0)) # 게임 스크린 불러오기
        screen.blit(game_screen, (710, 0)) # 게임 스크린 불러오기
        screen.blit(game_screen, (850, 0)) # 게임 스크린 불러오기
        screen.blit(game_bar, (305, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (445, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (585, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (725, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (865, 605)) # 게임 바 불러오기


        

    pygame.display.update() # 이거 해야 화면이 유지된다(이거 지우는 얘는 없겠지)

pygame.quit() # 위 와일 문 탈출 시 이놈이 게임 끈다(이거 지우는 얘는 없겠지)