from random import *
import pygame # 파이게임 불러오기(이거 지우는 얘는 없겠지)

pygame.init() # 초기화(이거 지우는 얘는 없겠지)

screen_w = 150 # 화면 넓이
screen_h = 300  # 화면 높이
screen = pygame.display.set_mode((screen_w, screen_h)) # 화면 생성

pygame.display.set_caption("일조") # 타이틀 제목

clock = pygame.time.Clock() 


background = pygame.image.load("C:/PythonWorkspace/flema/back.png") # 배경 그림 불러오기


notes_x=[20,50,80,110] 
note = pygame.image.load("C:/PythonWorkspace/flema/note.png") # 메뉴 그림 불러오기
note_size = note.get_rect().size # 메뉴 이미지의 크기를 구해옴
note_w = note_size[0] # 메뉴의 가로 크기
note_h = note_size[1] # 메뉴의 세로 크기
note_x_pos = 0 # 메뉴 x 좌표
note_y_pos = 0 # 메뉴 y 좌표

note = pygame.image.load("C:/PythonWorkspace/flema/note.png") # 배경 그림 불러오기
pygame.mixer.music.load("C:/PythonWorkspace/flema/music1.mp3")
note_speed = 10
running = True # 게임이 진행중인지
while running: # True 시 진행 False 시 종료
    dt = clock.tick(60)

    for event in pygame.event.get(): # 이거해야 이벤트 할수있어(이거 지우는 얘는 없겠지)
        if event.type == pygame.QUIT: # 타이틀 제목 오른쪽 x누르면 종료 

            running = False # 게임 끌게
        pygame.mixer.music.play(0)

    

    note_y_pos += note_speed
    if note_y_pos > screen_h:
        shuffle(notes_x)
        note_xx_pos = sample(notes_x ,2)
        note_x_pos = note_xx_pos[0]
        note_y_pos = -10



        

    
    screen.blit(background, (0, 0)) # 0, 0 좌표에 배경 불러오기
    screen.blit(note,(note_x_pos, note_y_pos))
    pygame.display.update() # 이거 해야 화면이 유지된다(이거 지우는 얘는 없겠지)


pygame.quit() # 위 와일 문 탈출 시 이놈이 게임 끈다(이거 지우는 얘는 없겠지)