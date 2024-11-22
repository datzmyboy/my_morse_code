import time
import  pygame
import sys
from playsound import  playsound
morse_code_dict = { 'A':'.-', 'B':'-...',  'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.', " ": "/"}




class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.font_1 = pygame.font.Font(None, 35)
        self.text_title_font = pygame.font.Font(None, 80)
        self.play_text_font = pygame.font.Font(None, 50)
        self.font_char = pygame.font.Font(None,70)
        pygame.display.set_caption("My Morse Code")
        self.user_text = ""
        self.input_text_box = pygame.Rect(180, 250, 250, 40)
        self.button_rect_box = pygame.Rect(230, 310, 150, 40)
        self.temp_text = ""
        self.is_pressed_button = False
        self.is_pressed_box = False
        self.is_done_playing = False
        self.exit__game = False
        self.converted_message_list = []
    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.text_logic(event)
                    if event.key == pygame.K_BACKSPACE:
                        self.counter_for_backspace()
                    if event.key == pygame.K_ESCAPE:
                        self.exit__game = True
                    else:
                        self.temp_text += event.unicode
                        self.user_text += event.unicode
                        self.user_text = self.user_text.upper()
                        print(self.temp_text)

            self.screen.fill((255, 255, 255))  # Clear the screen to white
            self.activate_button()  # Check for button hover and draw it
            self.check_ispressed_box(event)

            self.blit_render_text()

            self.play_the_code()
          
            # Draw the text and input box
            pygame.display.update()  # Update the display

    def blit_render_text(self):
        pygame.draw.rect(self.screen, (255, 0, 10), self.input_text_box, 3)  # Draw input box border
        text_surface = self.font_1.render(self.user_text, True, (0, 0, 0))  # Render user text
        self.screen.blit(text_surface, (185, 255))  # Position user text
        text_title_surface = self.text_title_font.render("My Morse Code", True, (0, 255, 0))  # Render title
        play_text_surface = self.play_text_font.render("Play", True, (255, 255, 255))  # Render button text
        self.screen.blit(text_title_surface, (80, 140))  # Position title
        self.screen.blit(play_text_surface, (265, 312))  # Position button text

    def text_logic(self, event):
        if len(self.user_text) > 13:
            self.user_text = self.user_text[-13:]  # Keep only the last 13 characters

    def counter_for_backspace(self):
        if self.temp_text:  # Ensure there's text to remove
            self.temp_text = self.temp_text[:-1]
            self.user_text = self.temp_text.upper()
            if len(self.temp_text) > 13:
                self.user_text = self.user_text[-13:].upper()
            else:
                    self.user_text =self.temp_text.upper()

    def activate_button(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
        # Check if the mouse is within the button's bounds
        if (self.button_rect_box.x <= mouse_x <= self.button_rect_box.x + self.button_rect_box.w and
                self.button_rect_box.y <= mouse_y <= self.button_rect_box.y + self.button_rect_box.h):
            pygame.draw.rect(self.screen, (192, 192, 192), self.button_rect_box)  # Hover color
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect_box)  # Default color

    def check_ispressed_box(self,event):
        # a,b,c,d = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect_box.collidepoint(event.pos):
                self.is_pressed_button = True
    def play_the_code(self):
        if self.is_pressed_button:
            code = self.convert_message(self.user_text)
            if self.is_done_playing == False:
                self.play_code()



    def convert_message(self,text):
        # converted_message_list = []
        if self.is_done_playing == False:
            for m in text.upper():
                if m in morse_code_dict:
                    converted_value = morse_code_dict[m]
                    self.converted_message_list.append(converted_value)
                    # print(converted_value)
                    # print("proff")
            print(f" this the value of the converted {self.converted_message_list}")
            # print("this is it")
            print(len(self.converted_message_list))
            morse_code = " ".join(self.converted_message_list)
            return morse_code

    def play_code(self):
        for i, v in enumerate(self.converted_message_list):
            pygame.draw.rect(self.screen, (255, 255, 255), (200, 400, 100, 50))  # Clear area for Morse code symbol
            pygame.draw.rect(self.screen, (255, 255, 255), (450, 400, 100, 50))
            # Render Morse code symbol (from `converted_message_list`)
            symbol_text = self.font_1.render(v, True, (0, 0, 0))
            self.screen.blit(symbol_text, (200, 400))

            # Render user input text at a different position
            symbol_text2 = self.font_1.render(self.user_text[i], True, (0, 0, 0))
            self.screen.blit(symbol_text2, (450, 400))

            pygame.display.flip()  # Update the display with both texts

            for j in v:  # Iterate through each symbol in the Morse code string
                if j == ".":
                    playsound("short beep.mp3")
                    time.sleep(0.3)
                elif j == "-":
                    playsound("long beep.mp3")
                    time.sleep(0.3)
                elif j == "/" or j == " ":
                    time.sleep(0.5)  # Pause for space or slash symbols
                else:
                    print("invalid char")  # Print if an invalid character is encountered

        self.is_done_playing = True
        self.reset_all()

    def reset_all(self):
        self.is_pressed_button = False
        self.is_done_playing = False
        self.user_text = ""
        self.temp_text = ""
        self.converted_message_list = []







# Start the game
game = Main()
game.main_loop()








