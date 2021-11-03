import pygame # 파이게임 불러오기(이거 지우는 얘는 없겠지)
from random import * # 랜덤함수 사용 가능

pygame.init() # 초기화(이거 지우는 얘는 없겠지)

screen_w = 1280 # 화면 넓이
screen_h = 720  # 화면 높이
screen = pygame.display.set_mode((screen_w, screen_h)) # 화면 생성

pygame.display.set_caption("일조") # 타이틀 제목

clock = pygame.time.Clock() #프레임 설정 *이거 나중에 필요함

background = pygame.image.load("C:/PythonWorkspace/flema/img/display.jpg") # 배경 그림 불러오기
background_opa = pygame.image.load("C:/PythonWorkspace/flema/img/display2.png") # 배경 그림 불러오기

arrowr = pygame.image.load("C:/PythonWorkspace/flema/img/cursor_r.png") # 오른쪽 화살표 그림 불러오기
aroowr_size = arrowr.get_rect().size # 오른쪽 화살표 이미지의 크기를 구해옴
arrowr_w = aroowr_size[0] # 오른쪽 화살표 가로 크기
arrowr_h = aroowr_size[1] # 오른쪽 화살표 세로 크기

arrowl = pygame.image.load("C:/PythonWorkspace/flema/img/cursor_l.png") # 왼쪽 화살표 그림 불러오기
aroowl_size = arrowl.get_rect().size # 왼쪽 화살표 이미지의 크기를 구해옴
arrowl_w = aroowl_size[0] # 왼쪽 화살표 가로 크기
arrowl_h = aroowl_size[1] # 왼쪽 화살표 세로 크기

yesno = pygame.image.load("C:/PythonWorkspace/flema/img/yesno.jpg") # 예쓰버튼 그림 불러오기
yesno_size = yesno.get_rect().size # 설정 이미지의 크기를 구해옴
yesno_w = yesno_size[0] # 설정 가로 크기
yesno_h = yesno_size[1] # 설정 세로 크기

yes_button = pygame.image.load("C:/PythonWorkspace/flema/img/예.png") # 예쓰버튼 그림 불러오기
yes_button_size = yes_button.get_rect().size # 설정 이미지의 크기를 구해옴
yes_button_w = yes_button_size[0] # 설정 가로 크기
yes_button_h = yes_button_size[1] # 설정 세로 크기

no_button = pygame.image.load("C:/PythonWorkspace/flema/img/아니오.png") # 노버튼 그림 불러오기
no_button_size = no_button.get_rect().size # 설정 이미지의 크기를 구해옴
no_button_w = no_button_size[0] # 설정 가로 크기
no_button_h = no_button_size[1] # 설정 세로 크기

game_bar = pygame.image.load("C:/PythonWorkspace/flema/img/bar.png") # 바 그림 불러오기
game_bar_size = game_bar.get_rect().size # 바 이미지의 크기를 구해옴
game_bar_w = game_bar_size[0] # 바 가로 크기
game_bar_h = game_bar_size[1] # 바 세로 

back_button = pygame.image.load("C:/PythonWorkspace/flema/img/이전.png") # 뒤로가기 그림 불러오기
back_button_size = back_button.get_rect().size # 뒤로가기 이미지의 크기를 구해옴
back_button_w = back_button_size[0] # 뒤로가기 가로 크기
back_button_h = back_button_size[1] # 뒤로가기 세로

game_down = pygame.image.load("C:/PythonWorkspace/flema/img/note.png") # 떨어지는 바 그림 불러오기
game_down_size = game_down.get_rect().size # 떨어지는 바 이미지의 크기를 구해옴[]
game_down_w = game_down_size[0] # 떨어지는 바 가로 크기
game_down_h = game_down_size[1] # 떨어지는 바 세로 크기
game_downs = [] # 떨어지는 바 n개를 불러오기 위해서
game_down_x =[310, 450, 590, 730, 870] # 떨어지는 바 x 값 집합
game_down_x_pos = sample(game_down_x, 1) # 랜덤의 x 값
game_down_y_pos = -100 # 떨어지는 바 y 값
game_down_speed = 10 # 떨어지는 바 속도

album_num = 1 # 앨범 순서 정하기
album_opacity = 0
LEFT = 1 #마우스 왼쪽클릭
RIGHT = 3 #마우스 오른쪽 클릭

back_button_screen = 0 # 뒤로가기 버튼
yes_no = 0 # yes no 버튼 불러오기 위한 변수
game = 0 # 게임 화면을 불러오기 위한 변수

start_ticks = pygame.time.get_ticks() # 게임 시작 시간 정보
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성

no_pull = 0
note_one = 1
yes_controll = 1
fairy_condition = 0

crash_square = pygame.image.load("C:\\Pythonworkspace\\flema\\img\\line.png") 
crash_square_size = crash_square.get_rect().size
crash_square_w = crash_square_size[0]
crash_square_h = crash_square_size[1]

fairy = pygame.image.load("C:/PythonWorkspace/flema/img/fairy.png") # 요정 그림 불러오기

game_down_remove = -1 # 떨어지는 바 사라지게 하기위한 변수

game_score = 0
game_play = 0

running = True # 게임이 진행중인지
while running: # True 시 진행 False 시 종료

    dt = clock.tick(60) #게임 진행하는동안 60프레임으로 고정 *이거 나중에 필요함

    album = pygame.image.load("C:/PythonWorkspace/flema/img/앨범{0}.png".format(album_num)) # 앨범 그림 불러오기
    album_size = album.get_rect().size # 앨범 이미지의 크기를 구해옴
    album_w = album_size[0] # 앨범 가로 크기
    album_h = album_size[1] # 앨범 세로 크기

    if album_num == 1:
        game_down_speed = 10 # 떨어지는 바 속도
    elif album_num == 2:
        game_down_speed = 15 # 떨어지는 바 속도
    elif album_num == 3:
        game_down_speed = 20 # 떨어지는 바 속도

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

    if game == 1:
        yes_controll = 0
    else:
        yes_controll = 1

    for event in pygame.event.get(): # 이거해야 이벤트 할수있어(이거 지우는 얘는 없겠지)

        if event.type == pygame.QUIT: # 타이틀 제목 오른쪽 x누르면 종료 
            running = False # 게임 끌게

        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT: # 마우스  왼쪽 클릭 이벤트 발생하면
            mousepos = pygame.mouse.get_pos() #마우스 위치를 받고
            if yes_no == 0:
                if game == 0:
                    if 1030 <= mousepos[0] <= 1230 and 250 <= mousepos[1] <= 450: #마우스의 위치가 오른쪽 화살표의 위치 면
                        if album_num <=2: #앨범 순서가 2보다 작거나 같을때
                            album_num += 1 #앨범 순서를 다음으로 넘김
                    if 50 <= mousepos[0] <= 250 and 250 <= mousepos[1] <= 450: #마우스의 위치가 왼쪽 화살표의 위치 면
                        if album_num >=2: #앨범 순서가 2보다 크거나 같을떄
                            album_num -= 1 #앨범 순서를 이전으로 넘김
                if 515.5  <= mousepos[0] <= 515.5 + album_w and 277.5 <= mousepos[1] <= 277.5 + album_w: # 엘범을 클릭 했을때
                    yes_no += 1 # 변수에 1을 더함
            if 515.5 + yn_album_h + ( yn_no_button_h /2) <= mousepos[0] <= 515.5 + (yn_album_h) + ( yn_no_button_h /2) + yn_no_button_w \
            and 277.5 + (yn_album_w/3) <=mousepos[1] <=  277.5+(yn_album_w/3) + yn_no_button_h: # 아니오 버튼 클릭 좌표 
                    yes_no = 0 # 변수를 0으로
                    fairy_condition += 1
            if 515.5 + yn_album_h - ( yn_yes_button_h *2) <= mousepos[0] <= 515.5 + yn_album_h - ( yn_yes_button_h *2) + yn_yes_button_w \
            and 277.5 + (yn_album_w/3) <=mousepos[1] <=  277.5+(yn_album_w/3) + yn_yes_button_h: # 예 버튼 클릭 좌 
                    yes_no = 0 # 변수를 0으로
                    fairy_condition = 0
                    game += 1 # 변수에 1을 더함
                    album_opacity = 1
                    start_ticks = pygame.time.get_ticks() # 게임 시작 시간 정보
                    pygame.mixer.music.load("C:/PythonWorkspace/flema/music{0}.mp3".format(album_num)) #음악 불러오기
                    pygame.mixer.music.play(0) #음악 재생
                    pygame.mixer.music.set_volume(0.1)

                
                    
        if event.type == pygame.KEYDOWN: # 키보드 입력 이벤트 발생하려면 필요
            if event.key == pygame.K_LEFT: # 키보드 왼쪽버튼이 눌릴시에
                if game >=1 : # 게임 변수가 1이상일떄
                    no_pull = 1  # no_pull가 1일때에만 나오게하기위해 변수 지정
                    crash_square_rect = crash_square.get_rect() # put바 사각형으로 정의
                    crash_square_rect.left = 305 # put바 활성화 x값 가로크기
                    crash_square_rect.top = 600 # put바 활성화 y값 세로크기
                    for game_down_idx, game_down_val in enumerate(game_downs):
                        game_down_x_pos = game_down_val[0]
                        game_down_y_pos = game_down_val[1]
                        game_down_rect = game_down.get_rect() # 떨어지는 바를 사각형으로 정의
                        game_down_rect.left = game_down_x_pos[0]
                        game_down_rect.top = game_down_y_pos
                        if game_down_rect.colliderect(crash_square_rect): # 충돌처리 조건
                            game_down_remove = game_down_idx
                            if 555 <= game_down_y_pos <= 605:
                                game_score += 100
                            elif 505 <= game_down_y_pos < 555 or 605 < game_down_y_pos <= 655:
                                game_score += 50
                        else:
                            pass
            
            if event.key == pygame.K_UP: # 키보드 위버튼이 눌릴시에
                if game >=1 : # 게임 변수가 1이상일떄
                    no_pull = 2  # no_pull가 2일때에만 나오게하기위해 변수 지정
                    crash_square_rect = crash_square.get_rect() # put바 사각형으로 정의
                    crash_square_rect.left = 445 # put바 활성화 x값 가로크기
                    crash_square_rect.top = 600 # put바 활성화 y값 세로크기
                    for game_down_idx, game_down_val in enumerate(game_downs):
                        game_down_x_pos = game_down_val[0]
                        game_down_y_pos = game_down_val[1]
                        game_down_rect = game_down.get_rect() # 떨어지는 바를 사각형으로 정의
                        game_down_rect.left = game_down_x_pos[0]
                        game_down_rect.top = game_down_y_pos
                        if game_down_rect.colliderect(crash_square_rect): # 충돌처리 조건
                            game_down_remove = game_down_idx
                            if 555 <= game_down_y_pos <= 605:
                                game_score += 100
                            elif 505 <= game_down_y_pos < 555 or 605 < game_down_y_pos <= 655:
                                game_score += 50
                        else:
                            pass
            
            if event.key == pygame.K_SPACE: # 키보드 스페이스바버튼이 눌릴시에
                if game >=1 : # 게임 변수가 1이상일떄
                    no_pull = 3  # no_pull가 3일때에만 나오게하기위해 변수 지정
                    crash_square_rect = crash_square.get_rect() # put바 사각형으로 정의
                    crash_square_rect.left = 585 # put바 활성화 x값 가로크기
                    crash_square_rect.top = 600 # put바 활성화 y값 세로크기
                    for game_down_idx, game_down_val in enumerate(game_downs):
                        game_down_x_pos = game_down_val[0]
                        game_down_y_pos = game_down_val[1]
                        game_down_rect = game_down.get_rect() # 떨어지는 바를 사각형으로 정의
                        game_down_rect.left = game_down_x_pos[0]
                        game_down_rect.top = game_down_y_pos
                        if game_down_rect.colliderect(crash_square_rect): # 충돌처리 조건
                            game_down_remove = game_down_idx
                            if 555 <= game_down_y_pos <= 605:
                                game_score += 100
                            elif 505 <= game_down_y_pos < 555 or 605 < game_down_y_pos <= 655:
                                game_score += 50
                        else:
                            pass

            if event.key == pygame.K_DOWN: # 키보드 아래버튼이 눌릴시에
                if game >=1 : # 게임 변수가 1이상일떄
                    no_pull = 4  # no_pull가 4일때에만 나오게하기위해 변수 지정
                    crash_square_rect = crash_square.get_rect() # put바 사각형으로 정의
                    crash_square_rect.left = 725 # put바 활성화 x값 가로크기
                    crash_square_rect.top = 600 # put바 활성화 y값 세로크기
                    for game_down_idx, game_down_val in enumerate(game_downs):
                        game_down_x_pos = game_down_val[0]
                        game_down_y_pos = game_down_val[1]
                        game_down_rect = game_down.get_rect() # 떨어지는 바를 사각형으로 정의
                        game_down_rect.left = game_down_x_pos[0]
                        game_down_rect.top = game_down_y_pos
                        if game_down_rect.colliderect(crash_square_rect): # 충돌처리 조건
                            game_down_remove = game_down_idx
                            if 555 <= game_down_y_pos <= 605:
                                game_score += 100
                            elif 505 <= game_down_y_pos < 555 or 605 < game_down_y_pos <= 655:
                                game_score += 50
                        else:
                            pass

            if event.key == pygame.K_RIGHT: # 키보드 오른쪽버튼이 눌릴시에
                if game >=1 : # 게임 변수가 1이상일떄
                    no_pull = 5  # no_pull가 5일때에만 나오게하기위해 변수 지정
                    crash_square_rect = crash_square.get_rect() # put바 사각형으로 정의
                    crash_square_rect.left = 865 # put바 활성화 x값 가로크기
                    crash_square_rect.top = 600 # put바 활성화 y값 세로크기
                    for game_down_idx, game_down_val in enumerate(game_downs):
                        game_down_x_pos = game_down_val[0]
                        game_down_y_pos = game_down_val[1]
                        game_down_rect = game_down.get_rect() # 떨어지는 바를 사각형으로 정의
                        game_down_rect.left = game_down_x_pos[0]
                        game_down_rect.top = game_down_y_pos
                        if game_down_rect.colliderect(crash_square_rect): # 충돌처리 조건
                            game_down_remove = game_down_idx
                            if 555 <= game_down_y_pos <= 605:
                                game_score += 100
                            elif 505 <= game_down_y_pos < 555 or 605 < game_down_y_pos <= 655:
                                game_score += 50
                        else:
                            pass

        if event.type == pygame.KEYUP:  # 키보드를 땠을 때
            no_pull = 0 # 그림을 지우기위해 다시 0으로 지정

    game_downs = [ [g[0], g[1] + game_down_speed] for g in game_downs] # x, y 값 갱신
    game_downs = [ [g[0], g[1]] for g in game_downs if g[1] < 703] # y 값이 바닥에 닿으면 사라짐

    def real_game_down(event): # 묻지마 나도 헷갈려
        if event == int(elapsed_time): # real_game_down(숫자) 숫자가 시간과 같을시 나오게
            game_down_x_pos = sample(game_down_x, 1) # x 값 랜덤
            game_down_y_pos = -100 # 떨어지는 바 y 값
            game_downs.append([game_down_x_pos, game_down_y_pos]) # x, y 값 갱신
        if int(elapsed_time) == 79:
            game = 0;
            game_score = 0
            pygame.mixer.music.stop() #노래 끄기
            yes_no = 0
            album_opacity = 0
            game_play = 0

    if game_down_remove > -1:
        del game_downs[game_down_remove]
        game_down_remove = -1

    screen.blit(background, (0, 0)) # 0, 0 좌표에 배경 불러오기
    screen.blit(album,(515.5,277.5)) #앨범 불러오기
    if album_num != 3 and album_opacity ==0:
        screen.blit(arrowr, (1030, 250)) # 좌표에 오른쪽 화살표 불러오기
    if album_num != 1 and album_opacity ==0:
        screen.blit(arrowl, (50, 250)) # 좌표에 왼쪽 화살표 불러오기
    if yes_no >= 1: # 변수가 1이상 일 때
        screen.blit(yesno, (277.5, 208.5)) # 예 버튼 불러오기
        screen.blit(yes_button, (537, 358.5)) # 예 버튼 불러오기
        screen.blit(no_button, (662, 358.5)) # 아니오 버튼 불러오기
    if fairy_condition >=5:
        screen.blit(fairy, (800, 400)) # 요정 불러오기
    if game >=1: # 변수가 1이상 일 때
        screen.blit(background_opa, (0, 0)) # 0, 0 좌표에 배경 불러오기
        screen.blit(game_bar, (305, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (445, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (585, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (725, 605)) # 게임 바 불러오기
        screen.blit(game_bar, (865, 605)) # 게임 바 불러오기
        screen.blit(back_button, (screen_w - back_button_w, 0)) # 게임 뒤로가기 버튼

        if no_pull == 1:  # 버튼을 눌러 no_pull가 1일떄에 
            screen.blit(crash_square, (300,0)) # 좌표에 그림 출력
        if no_pull == 2:  # 버튼을 눌러 no_pull가 2일떄에
            screen.blit(crash_square, (440,0))  # 좌표에 그림 출력
        if no_pull == 3:  # 버튼을 눌러 no_pull가 3일떄에
            screen.blit(crash_square, (580,0))  # 좌표에 그림 출력
        if no_pull == 4:  # 버튼을 눌러 no_pull가 4일떄에
            screen.blit(crash_square, (720,0))  # 좌표에 그림 출력
        if no_pull == 5:  # 버튼을 눌러 no_pull가 5일떄에
            screen.blit(crash_square, (860,0))  # 좌표에 그림 출력

        score = game_font.render(str("score : "+ str(game_score)), True, (255, 255, 255))
        screen.blit(score, (985, 0))
        if game_down_speed == 10:
            elapsed_time = elapsed_time1
        if game_down_speed == 15:
            elapsed_time = elapsed_time2
        if game_down_speed == 20:
            elapsed_time = elapsed_time3
        if int(elapsed_time) == 8:
            game_play = 1
        if game_play == 1:
            if note_one == 1:                       
                for i in range(78):
                    real_game_down(i)
                current_time = int(elapsed_time)
                note_one = 0
            if int(elapsed_time) == current_time:
                pass
            else:
                note_one = 1

        if screen_w - back_button_w <= mousepos[0] <= screen_w and 0 <=mousepos[1] <= back_button_h: #뒤로가기 버튼 클릭했을때
            game = 0 # 게임 변수를 0으로 정의
            game_score = 0
            pygame.mixer.music.stop() #노래 끄기
            yes_no = 0
            album_opacity = 0
            game_play = 0

        for game_down_x_pos, game_down_y_pos in game_downs:
            screen.blit(game_down, (game_down_x_pos[0], game_down_y_pos)) # 떨어지는 바 불러오기

    elapsed_time1 = (pygame.time.get_ticks() - start_ticks) / 1150 # 경과 시간 계산 단위는 1초
    elapsed_time2 = (pygame.time.get_ticks() - start_ticks) / 500
    elapsed_time3 = (pygame.time.get_ticks() - start_ticks) / 250

    pygame.display.update() # 이거 해야 화면이 유지된다(이거 지우는 얘는 없겠지)

pygame.quit() # 위 와일 문 탈출 시 이놈이 게임 끈다(이거 지우는 얘는 없겠지)