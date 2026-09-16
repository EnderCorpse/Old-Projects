import sys
import random
import ipaddress

import pygame

# Config
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BG_COLOR = (20, 20, 20)
PANEL_COLOR = (255, 255, 255)
TEXT_COLOR = (20, 20, 20)
ACCENT_COLOR = (30, 120, 180)
FONT_NAME = None # Default font
FPS = 30

# Subnetting utilities

def ip_to_int(ip_str):
    return int(ipaddress.IPv4Address(ip_str))

def int_to_ip(i):
    return str(ipaddress.IPv4Address(i))

def network_and_broadcast(ip_str, prefix_len):
    network = ipaddress.IPv4Network(f"{ip_str}/{prefix_len}", strict=False)
    usable = max(network.num_addresses - 2, 0)
    return str(network.network_address), str(network.broadcast_address), usable

def random_ipv4():
    #choose a random non-special IP address for questions (avoid 0.x.x.x, and 255.x.x.x)
    return "{}.{}.{}.{}".format(
        random.randint(1, 223),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(1, 254),
    )

def random_prefix():
    return random.choice([8, 16, 24, 25, 26, 28, 29, 30])

# Question generation

def generate_question():
    ip = random_ipv4()
    prefix = random_prefix()
    network, broadcast, total_hosts = network_and_broadcast(ip, prefix)
    qtype = random.choice(['network', 'broadcast', 'total_hosts'])
    if qtype == 'network':
        prompt = f"Given IP: {ip}/{prefix}, what is the Network Address?"
        answer = network
    elif qtype == 'broadcast':
        prompt = f"Given IP: {ip}/{prefix}, what is the Broadcast Address?"
        answer = broadcast
    else:
        prompt = f"Given IP: {ip}/{prefix}, how many Usable Hosts are in the subnet?"
        answer = str(total_hosts)  # Exclude network and broadcast addresses
    return {'prompt': prompt, 'answer': answer, 'ip': ip, 'prefix': prefix, 'type': qtype}

#Simple Text Input Box
class InputBox:
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (200, 200, 200)
        self.text = text
        self.font = font
        self.txt_surface = font.render(self.text, True, TEXT_COLOR)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (200, 200, 200)
        if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    val = self.text.strip()
                    self.text = ''
                    self.update()
                    return val
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 30:  # Limit input length
                        self.text += event.unicode
                self.update()
        return None

    def update(self):
        self.txt_surface = self.font.render(self.text, True, TEXT_COLOR)
        
    def draw(self, screen):
        pygame.draw.rect(screen, PANEL_COLOR, self.rect)
        pygame.draw.rect(screen, self.color, self.rect, 3)
        screen.blit(self.txt_surface, (self.rect.x+8, self.rect.y+8))
        
# Button Class
class Button:
    def __init__(self, x, y, w, h, text, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.txt_surface = font.render(self.text, True, (255, 255, 255))
        self.color = ACCENT_COLOR
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=6)
        tw = self.txt_surface.get_width()
        th = self.txt_surface.get_height()
        screen.blit(self.txt_surface,
                    (self.rect.centerx - tw/2, self.rect.centery - th/2))
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
# Main App
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("CSNT IPv4 Subnetting Quiz")
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(FONT_NAME, 20)
    title_font = pygame.font.Font(FONT_NAME, 30)
    small_font = pygame.font.Font(FONT_NAME, 16)
    
    score = 0
    total_asked = 0
    current = generate_question()
    feedback = ''
    feedback_timer = 0 #frames
    
    input_box = InputBox(60, 260, 620, 48, base_font)
    submit_button = Button(700, 260, 120, 48, "Submit")
    next_btn = Button(700, 330, 140, 40, "Next")
    show_answer_btn = Button(700, 390, 140, 40, "Show Answer", base_font)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            submitted = input_box.handle_event(event)
            if submitted is not None:
                total_asked += 1
                correct = check_answer(submitted, current['answer'], current['type'])
                if correct:
                    score += 1
                    feedback = "Correct!"
                    feedback_color = (20, 150, 20)
                else:
                    feedback = f"Incorrect! Correct answer: {current['answer']}"
                    feedback_color = (200, 30, 30)
                feedback_timer = FPS * 3  # Show feedback for 3 seconds
                input_box.text = ''
                input_box.update()
            elif event.type == pygame.MOUSEBUTTONDOWN and next_btn.is_clicked(event.pos):
                current = generate_question()
                input_box.text = ''
                input_box.update()
            elif event.type == pygame.MOUSEBUTTONDOWN and show_answer_btn.is_clicked(event.pos):
                feedback = f"Answer: {current['answer']}"
                feedback_color = (80, 80, 80)
                feedback_timer = FPS * 4
            
        # drawing
        screen.fill(BG_COLOR)
        
        #Header panel
        pygame.draw.rect(screen, PANEL_COLOR, (20, 20, SCREEN_WIDTH - 40, 120), border_radius=8)
        title_surf = title_font.render("CSNT IPv4 Subnetting Quiz", True, TEXT_COLOR)
        screen.blit(title_surf, (40, 32))
        subtitle = small_font.render("Test your subnetting skills! Answer the questions below.", True, (80, 80, 80))
        screen.blit(subtitle, (40, 72))
        
        #Score panel
        pygame.draw.rect(screen, PANEL_COLOR, (20, 150, SCREEN_WIDTH - 40, 380), border_radius=8)
        
        #Prompt text (warp)
        prompt_lines = wrap_text(current['prompt'], base_font, 620)
        y_offset = 40
        for line in prompt_lines:
            line_surf = base_font.render(line, True, TEXT_COLOR)
            screen.blit(line_surf, (60, 180 + y_offset))
            y_offset += 30
            
        input_box.draw(screen)
        
        submit_button.draw(screen)
        next_btn.draw(screen)
        show_answer_btn.draw(screen)
        
        score_surf = base_font.render(f"Score: {score}/{total_asked}", True, TEXT_COLOR)
        screen.blit(score_surf, (60, 370))
        
        details = small_font.render(f"IP: {current['ip']} /{current['prefix']} Type: {current['type']}", True, (90, 90, 90))
        screen.blit(details, (60, 395))
        
        # Feedback
        if feedback_timer > 0 and feedback:
            feedback_surf = base_font.render(feedback, True, feedback_color)
            screen.blit(feedback_surf, (60, 420))
            feedback_timer -= 1
            
        #instructions/help
        help_lines = [
            "Input format tips:",
            "- For IP addresses, use standard dotted-decimal notation (e.g. 192.168.1.0",
            "- For number of hosts, just enter the integer value (e.g. 254)"
        ]
        hy = 460
        for hl in help_lines:
            screen.blit(small_font.render(hl, True, (100, 100, 100)), (60, hy))
            hy += 22
        
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()

# Helpers
        
def check_answer(user, correct, qtype):
    u = user.strip().lower()
    c = str(correct).strip().lower()
    if qtype in ('network', 'broadcast'):
        try:
            u_ip = (ipaddress.IPv4Address(u))
            c_ip = (ipaddress.IPv4Address(c))
            return u_ip == c_ip
        except Exception:
            return False
    try:
        return int(u) == int(c)
    except Exception:
        return False
            
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    for word in words:
        test = current_line + (' ' if current_line else '') + word
        if font.size(test)[0] <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


if __name__ == "__main__":
    main()
    

