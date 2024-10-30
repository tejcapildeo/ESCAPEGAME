import pygame

def show_paper_display():
    # Define a square popup size and properties
    popup_rect = pygame.Rect(300, 150, 300, 300)  # Adjusted to be square (300x300)
    font = pygame.font.Font(None, 36)  # Slightly smaller font for better fit
    active = True

    # Dot pattern text and emphasis text
    emphasis_text = "a SQUARE page."
    dot_pattern = [
        "....",
        "....",
        ".",
        "."
    ]

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not popup_rect.collidepoint(mouse_pos):
                    active = False  # Close popup if clicked outside

        # Draw the popup background and border
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Display the emphasis text at the top of the popup
        text_surface = font.render(emphasis_text, True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 20))

        # Display the dot pattern below the emphasis text
        y_offset = 80  # Start below the emphasis text
        for line in dot_pattern:
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (popup_rect.x + 110, popup_rect.y + y_offset))  # Centered horizontally
            y_offset += 40  # Move down for the next line of dots

        pygame.display.flip()


def show_riddle_popup():
    # Define popup properties
    popup_rect = pygame.Rect(200, 150, 500, 200)
    font = pygame.font.Font(None, 28)
    active = True

    # Riddle text
    riddle_text = [
        "I want to play a game. Here is a riddle for you:",
        "I am not alive, yet I can grow;",
        "I don't have lungs, yet I need air.",
        "What am I?"
    ]

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not popup_rect.collidepoint(mouse_pos):
                    active = False  # Close popup if clicked outside

        # Draw the popup background and border
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Display the riddle text
        y_offset = 20
        for line in riddle_text:
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + y_offset))
            y_offset += 30  # Move down for the next line of text

        pygame.display.flip()


letter_to_number = {
    'a': 4, 'b': 6, 'c': 6, 'd': 7, 'e': 8, 'f': 4, 'g': 3, 'h': 8, 'i': 5,
    'j': 2, 'k': 1, 'l': 0, 'm': 7, 'n': 2, 'o': 3, 'p': 5, 'q': 6, 'r': 6,
    's': 1, 't': 8, 'u': 7, 'v': 4, 'w': 3, 'x': 5, 'y': 2, 'z': 9
}

def show_translation_hint():
    # Define popup properties
    popup_rect = pygame.Rect(200, 150, 400, 300)
    font = pygame.font.Font(None, 28)
    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not popup_rect.collidepoint(mouse_pos):
                    active = False  # Close popup if clicked outside

        # Draw the popup background and border
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Display the hint text
        y_offset = 30
        for index, (letter, number) in enumerate(letter_to_number.items()):
            text_surface = font.render(f"{letter.upper()}{number}", True, (255, 255, 255))
            x_position = popup_rect.x + 20 + (index % 5) * 70  # Adjusts position horizontally
            y_position = popup_rect.y + y_offset + (index // 5) * 30  # Moves to the next row after 5 letters
            screen.blit(text_surface, (x_position, y_position))

        text_surface = font.render("I feeling to nap. I also feeling to shit.", True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 210))
        text_surface = font.render("Anyway, I see this written on the wall.", True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 240))

        pygame.display.flip()


def open_lock1_minigame():
    show_popup1(screen, "4568")

def show_speaker_popup_true():
    # Define popup properties
    popup_rect = pygame.Rect(300, 150, 900, 150)  # Adjusted to fit the text comfortably
    font = pygame.font.Font(None, 36)
    active = True

    # Message to display
    message = "The root of all your problems can be solved with the piece of paper."

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not popup_rect.collidepoint(mouse_pos):
                    active = False  # Close popup if clicked outside

        # Draw the popup background and border
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Display the message
        text_surface = font.render(message, True, (255, 255, 255))
        # Center the message horizontally in the popup
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 60))

        pygame.display.flip()

def show_speaker_popup_false():
    popup_rect = pygame.Rect(300, 200, 400, 200)
    font = pygame.font.Font(None, 36)
    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not popup_rect.collidepoint(mouse_pos):
                    active = False  # Close popup if clicked outside

        # Draw popup background
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Render popup message
        text_surface = font.render("Speaker low on charge", True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 40, popup_rect.y + 80))

        pygame.display.flip()
    



def show_popup1(screen, correct_answer):
    # Define popup properties
    global locked_flag
    global speaker_accessible
    popup_rect = pygame.Rect(200, 150, 400, 300)
    font = pygame.font.Font(None, 36)
    
    # Input box settings
    input_box = pygame.Rect(popup_rect.x + 50, popup_rect.y + 150, 300, 40)
    user_text = ''
    active = True
    feedback = ''

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get the mouse position
                if not popup_rect.collidepoint(mouse_pos):
                    active=False
            # Handle text input for the answer box
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check if the input is correct
                    if user_text.lower() == correct_answer.lower():
                        feedback = "Correct!"
                        locked_flag = 0
                        speaker_accessible = True
                        active = False  # Close popup if the answer is correct
                    else:
                        feedback = "Incorrect, try again."
                        user_text = ''  # Clear input box
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # Remove last character
                else:
                    user_text += event.unicode  # Add character to input

        # Draw popup background
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Render popup text
        text_surface = font.render("Input the code to unlock", True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 20))
        text_surface = font.render("Press enter to submit it.", True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 50))
        text_surface = font.render("Click away to leave popup", True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 80))
        text_surface = font.render("Behind this is a cord", True, (255, 255, 255))
        screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + 110))

        # Draw the input box
        pygame.draw.rect(screen, (255, 255, 255), input_box)
        text_surface = font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # Render feedback message (correct/incorrect)
        feedback_surface = font.render(feedback, True, (255, 0, 0) if feedback == "Incorrect, try again." else (0, 255, 0))
        screen.blit(feedback_surface, (popup_rect.x + 20, popup_rect.y + 230))

        # Update display
        pygame.display.flip()

def show_popup2(screen, correct_answer):
    # Define popup properties
    global second_lock_flag
    popup_rect = pygame.Rect(200, 150, 400, 300)
    font = pygame.font.Font(None, 36)
    
    # Input box settings
    input_box = pygame.Rect(popup_rect.x + 50, popup_rect.y + 150, 300, 40)
    user_text = ''
    active = True
    feedback = ''

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not popup_rect.collidepoint(mouse_pos):
                    active = False  # Close popup if clicked outside
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check if the input is correct
                    if user_text.lower() == correct_answer.lower():
                        feedback = "Correct!"
                        second_lock_flag = 0  # Unlock the second lock
                        active = False  # Close popup if the answer is correct
                    else:
                        feedback = "Incorrect, try again."
                        user_text = ''  # Clear input box for retry
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # Remove last character
                else:
                    user_text += event.unicode  # Add character to input

        # Draw the popup background and border
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Render instructions text
        instructions = [
            "Input the code to unlock",
            "Press enter to submit it.",
            "Click away to leave popup"
        ]
        y_offset = 20
        for line in instructions:
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + y_offset))
            y_offset += 30  # Move down for each instruction line

        # Draw the input box and user text
        pygame.draw.rect(screen, (255, 255, 255), input_box)
        text_surface = font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # Render feedback message (correct/incorrect)
        feedback_surface = font.render(feedback, True, (255, 0, 0) if feedback == "Incorrect, try again." else (0, 255, 0))
        screen.blit(feedback_surface, (popup_rect.x + 20, popup_rect.y + 230))

        # Update the display
        pygame.display.flip()

def show_popup3(screen, correct_answer):
    # Define popup properties
    global final_lock_flag
    popup_rect = pygame.Rect(200, 150, 400, 300)
    font = pygame.font.Font(None, 36)
    
    # Input box settings
    input_box = pygame.Rect(popup_rect.x + 50, popup_rect.y + 150, 300, 40)
    user_text = ''
    active = True
    feedback = ''

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not popup_rect.collidepoint(mouse_pos):
                    active = False  # Close popup if clicked outside
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check if the input is correct
                    if user_text.lower() == correct_answer.lower():
                        feedback = "Correct!"
                        final_lock_flag = 0  # Unlock the final lock
                        active = False  # Close popup if the answer is correct
                    else:
                        feedback = "Incorrect, try again."
                        user_text = ''  # Clear input box for retry
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # Remove last character
                else:
                    user_text += event.unicode  # Add character to input

        # Draw the popup background and border
        pygame.draw.rect(screen, (30, 30, 30), popup_rect)
        pygame.draw.rect(screen, (255, 255, 255), popup_rect, 2)

        # Render instructions text
        instructions = [
            "What you discovered in the past",
            "Will help you to escape",
            "Combine what you already know"
        ]
        y_offset = 20
        for line in instructions:
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (popup_rect.x + 20, popup_rect.y + y_offset))
            y_offset += 30  # Move down for each instruction line

        # Draw the input box and user text
        pygame.draw.rect(screen, (255, 255, 255), input_box)
        text_surface = font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # Render feedback message (correct/incorrect)
        feedback_surface = font.render(feedback, True, (255, 0, 0) if feedback == "Incorrect, try again." else (0, 255, 0))
        screen.blit(feedback_surface, (popup_rect.x + 20, popup_rect.y + 230))

        # Update the display
        pygame.display.flip()

def display_win_message(screen):
    # Define font and message color
    font = pygame.font.Font(None, 100)  # Large font size
    win_message = "YOU WIN!"
    color = (0, 255, 0)  # Green color

    # Render the message
    text_surface = font.render(win_message, True, color)

    # Center the message on the screen
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)

##############################################################################################################################################33
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
locked_flag = 1
final_lock_flag = 1
second_lock_flag = 1
speaker_accessible = False

page = pygame.image.load("sprites/SinglePage.png")
page = pygame.transform.scale(page, (50, 50))
page_rect = page.get_rect(topleft=(200, 250))

vinayak = pygame.image.load("sprites/vinayak.jpeg")
vinayak = pygame.transform.scale(vinayak, (100, 200))
vinayak_rect = vinayak.get_rect(topleft=(1150, 50))


jigsaw = pygame.image.load("sprites/jigsaw.png")
jigsaw = pygame.transform.scale(jigsaw, (100, 100))
jigsaw_rect = jigsaw.get_rect(topleft=(900, 350))

questionmark = pygame.image.load("sprites/unidentified.png")
questionmark = pygame.transform.scale(questionmark, (40, 700))
questionmark_rect = questionmark.get_rect(topleft=(900, 160))

speaker = pygame.image.load("sprites/speaker.png")
speaker = pygame.transform.scale(speaker, (100, 100))
speaker_rect = speaker.get_rect(topleft=(500, 560))

locked = pygame.image.load("sprites/locked.png")
locked = pygame.transform.scale(locked, (90, 90))
lock_rect = locked.get_rect(topleft=(400, 150))

unlocked = pygame.image.load("sprites/unlocked.png")
unlocked = pygame.transform.scale(unlocked, (90, 90))
unlock_rect = unlocked.get_rect(topleft=(400, 150))

finallock = pygame.image.load("sprites/locked.png")
finallock = pygame.transform.scale(finallock, (90, 90))
finallock_rect = finallock.get_rect(topleft=(1000, 150))

finalunlock = pygame.image.load("sprites/unlocked.png")
finalunlock = pygame.transform.scale(finalunlock, (90, 90))
finalunlock_rect = finalunlock.get_rect(topleft=(1000, 150))

secondlock = pygame.image.load("sprites/locked.png")
secondlock = pygame.transform.scale(secondlock, (90, 90))
secondlock_rect = secondlock.get_rect(topleft=(1000, 600))

secondunlock = pygame.image.load("sprites/unlocked.png")
secondunlock = pygame.transform.scale(secondunlock, (90, 90))
secondunlock_rect = secondunlock.get_rect(topleft=(1000, 600))

sack = pygame.image.load("sprites/sack.png")
sack_rect = sack.get_rect(topleft=(300, 150))

player_pos = pygame.Vector2(100, 100)
background = pygame.image.load("sprites/dungeon10.png")
background = pygame.transform.scale(background, (1750, 1200))

player_image = pygame.image.load("sprites/cowboygun.png")
player_image = pygame.transform.scale(player_image, (150, 150))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # Get the mouse position

            # Check if the lock was clicked
            if lock_rect.collidepoint(mouse_pos) and locked_flag == 1:
                # Call a function to open the lock minigame
                open_lock1_minigame()
            if secondlock_rect.collidepoint(mouse_pos) and second_lock_flag == 1:
                show_popup2(screen, "2211")
            if finallock_rect.collidepoint(mouse_pos) and final_lock_flag == 1:
                show_popup3(screen, "6779")

            # Check if the speaker was clicked
            if speaker_rect.collidepoint(mouse_pos) and speaker_accessible == False:
                # Speaker low on charge popup
                show_speaker_popup_false()
            if speaker_rect.collidepoint(mouse_pos) and speaker_accessible == True:
                show_speaker_popup_true()

            if vinayak_rect.collidepoint(mouse_pos):
                show_translation_hint()

            if jigsaw_rect.collidepoint(mouse_pos):
                show_riddle_popup()
            if page_rect.collidepoint(mouse_pos):
                show_paper_display()
                
                
                


    # fill the screen with a color to wipe away anything from last frame
    
    screen.blit(background, (-220, -130))
    screen.blit(player_image, player_pos)
    screen.blit(vinayak, vinayak_rect)
    screen.blit(jigsaw, jigsaw_rect)
    screen.blit(page, page_rect)
    # screen.blit(questionmark, questionmark_rect)
    if locked_flag == 1:
        screen.blit(locked, lock_rect)
    else:
        screen.blit(unlocked, unlock_rect)

    if second_lock_flag == 1:
        screen.blit(secondlock, secondlock_rect)
    else:
        screen.blit(secondunlock, secondlock_rect)    

    if final_lock_flag == 1:
        screen.blit(finallock, finallock_rect)
    else:
        screen.blit(finalunlock, finallock_rect)
   

    screen.blit(speaker, speaker_rect)

    if final_lock_flag == 0:
        display_win_message(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000









pygame.quit()