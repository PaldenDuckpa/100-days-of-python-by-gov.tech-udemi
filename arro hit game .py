import pygame
import sys
import random
import math

# --- Initialization ---
pygame.init()

# --- Screen Settings ---
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Archery Master")

# --- Colors ---
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
WOOD_BROWN = (139, 69, 19)
STRING_COLOR = (40, 40, 40)
ARROW_COLOR = (60, 60, 60)
FLETCHING_COLOR = (210, 180, 140)
TARGET_COLORS = [(255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (255, 255, 0)]
SCORE_COLOR = (255, 215, 0)
POWER_BAR_COLOR = (220, 20, 60)
TRAJECTORY_COLOR = (0, 0, 0, 100) # Semi-transparent black

# --- Game Constants ---
# Bow settings
BOW_POSITION = (150, HEIGHT // 2)
BOW_HEIGHT = 120
MAX_PULL_STRENGTH = 100
MIN_PULL_STRENGTH = 10
PULL_SPEED_FACTOR = 0.2

# Arrow settings
ARROW_LENGTH = 70
ARROW_WEIGHT = 5
GRAVITY = 0.15

# Target settings
TARGET_X_POS = WIDTH - 150
TARGET_RADIUS = 50
TARGET_THICKNESS = 10

# --- Font ---
try:
    # Use a more thematic font if available
    title_font = pygame.font.Font("freesansbold.ttf", 48)
    score_font = pygame.font.Font("freesansbold.ttf", 32)
    message_font = pygame.font.Font("freesansbold.ttf", 40)
except FileNotFoundError:
    # Fallback to default font
    title_font = pygame.font.SysFont(None, 60)
    score_font = pygame.font.SysFont(None, 45)
    message_font = pygame.font.SysFont(None, 50)

# --- Game State Variables ---
score = 0
arrow_in_flight = False
pulling_bow = False
pull_strength = 0
pull_angle = 0

# --- Classes ---

class Bow:
    """Represents the player's bow, handling aiming and drawing."""
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        self.limb_thickness = 8
        self.grip_height = 40

    def draw(self, surface, pull_dist, angle):
        """Draws the bow, making it bend based on pull strength."""
        # Calculate tip positions
        top_tip = (self.pos[0], self.pos[1] - self.height // 2)
        bottom_tip = (self.pos[0], self.pos[1] + self.height // 2)
        
        # Calculate the string's pull-back point
        pull_x = self.pos[0] - pull_dist * math.cos(angle)
        pull_y = self.pos[1] - pull_dist * math.sin(angle)
        pull_point = (pull_x, pull_y)

        # Draw the bending limbs of the bow
        bend_factor = pull_dist / 2
        top_control_point = (self.pos[0] + bend_factor, self.pos[1] - self.height // 4)
        bottom_control_point = (self.pos[0] + bend_factor, self.pos[1] + self.height // 4)

        pygame.draw.line(surface, WOOD_BROWN, top_tip, top_control_point, self.limb_thickness)
        pygame.draw.line(surface, WOOD_BROWN, top_control_point, bottom_control_point, self.limb_thickness)
        pygame.draw.line(surface, WOOD_BROWN, bottom_control_point, bottom_tip, self.limb_thickness)

        # Draw the bowstring
        pygame.draw.line(surface, STRING_COLOR, top_tip, pull_point, 2)
        pygame.draw.line(surface, STRING_COLOR, bottom_tip, pull_point, 2)
        
        # Draw the grip
        pygame.draw.rect(surface, WOOD_BROWN, (self.pos[0] - 5, self.pos[1] - self.grip_height // 2, 10, self.grip_height), border_radius=3)


class Arrow:
    """Represents the arrow, handling its flight and drawing."""
    def __init__(self, pos):
        self.start_pos = list(pos)
        self.pos = list(pos)
        self.vel = [0, 0]
        self.angle = 0
        self.is_flying = False

    def launch(self, speed, angle):
        """Launches the arrow with a given speed and angle."""
        self.vel = [speed * math.cos(angle), speed * math.sin(angle)]
        self.is_flying = True

    def update(self):
        """Updates the arrow's position and angle during flight."""
        if self.is_flying:
            self.vel[1] += GRAVITY
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]
            self.angle = math.atan2(self.vel[1], self.vel[0])

    def draw(self, surface, angle_override=None):
        """Draws the arrow on the screen."""
        draw_angle = self.angle if angle_override is None else angle_override
        
        # Calculate end of arrow shaft
        end_x = self.pos[0] + ARROW_LENGTH * math.cos(draw_angle)
        end_y = self.pos[1] + ARROW_LENGTH * math.sin(draw_angle)

        # Draw shaft
        pygame.draw.line(surface, ARROW_COLOR, self.pos, (end_x, end_y), ARROW_WEIGHT)

        # Draw arrowhead
        self.draw_polygon_rotated(surface, ARROW_COLOR, 3, 12, (end_x, end_y), draw_angle)

        # Draw fletching (feathers)
        fletching_pos_x = self.pos[0] + 10 * math.cos(draw_angle)
        fletching_pos_y = self.pos[1] + 10 * math.sin(draw_angle)
        self.draw_polygon_rotated(surface, FLETCHING_COLOR, 4, 10, (fletching_pos_x, fletching_pos_y), draw_angle)
    
    def draw_polygon_rotated(self, surface, color, sides, radius, pos, angle):
        """Helper function to draw rotated polygons for arrowhead and fletching."""
        points = []
        for i in range(sides):
            theta = angle + (2 * math.pi * i / sides)
            x = pos[0] + radius * math.cos(theta)
            y = pos[1] + radius * math.sin(theta)
            points.append((x, y))
        pygame.draw.polygon(surface, color, points)

    def reset(self):
        """Resets the arrow to its starting position."""
        self.pos = list(self.start_pos)
        self.vel = [0, 0]
        self.is_flying = False

class Target:
    """Represents the archery target."""
    def __init__(self, x, min_y, max_y, radius):
        self.x = x
        self.min_y = min_y
        self.max_y = max_y
        self.radius = radius
        self.y = self.get_new_y()
        self.stand_height = 100

    def get_new_y(self):
        return random.randint(self.min_y, self.max_y)

    def draw(self, surface):
        """Draws the target with its stand."""
        # Stand
        stand_top = (self.x, self.y + self.radius)
        leg1 = (self.x - 30, self.y + self.radius + self.stand_height)
        leg2 = (self.x + 30, self.y + self.radius + self.stand_height)
        pygame.draw.line(surface, WOOD_BROWN, stand_top, leg1, 6)
        pygame.draw.line(surface, WOOD_BROWN, stand_top, leg2, 6)

        # Rings
        for i, color in enumerate(TARGET_COLORS):
            pygame.draw.circle(surface, color, (self.x, self.y), self.radius - i * TARGET_THICKNESS)

    def check_hit(self, pos):
        """Checks if an arrow hit the target and returns the score."""
        dist = math.hypot(pos[0] - self.x, pos[1] - self.y)
        if dist <= self.radius:
            if dist <= self.radius - 4 * TARGET_THICKNESS: return 50 # Bullseye
            if dist <= self.radius - 3 * TARGET_THICKNESS: return 40
            if dist <= self.radius - 2 * TARGET_THICKNESS: return 30
            if dist <= self.radius - 1 * TARGET_THICKNESS: return 20
            return 10
        return 0

    def reset_pos(self):
        self.y = self.get_new_y()

# --- Helper Functions ---

def draw_background(surface):
    """Draws a simple sky and grass background."""
    surface.fill(SKY_BLUE)
    pygame.draw.rect(surface, GRASS_GREEN, (0, HEIGHT * 0.7, WIDTH, HEIGHT * 0.3))

def draw_ui(surface):
    """Draws the score, title, and power bar."""
    # Title
    title_text = title_font.render("Archery Master", True, (0, 0, 0))
    surface.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))
    
    # Score
    score_text = score_font.render(f"Score: {score}", True, SCORE_COLOR)
    pygame.draw.rect(surface, (0,0,0,128), (18, 18, score_text.get_width() + 24, score_text.get_height() + 4), border_radius=5)
    surface.blit(score_text, (30, 20))

    # Power bar
    if pulling_bow:
        bar_height = (pull_strength / MAX_PULL_STRENGTH) * (HEIGHT * 0.4)
        pygame.draw.rect(surface, (0,0,0), (30, HEIGHT*0.3 - 5, 30, HEIGHT*0.4 + 10), 4, border_radius=5)
        pygame.draw.rect(surface, POWER_BAR_COLOR, (35, HEIGHT*0.7 - bar_height, 20, bar_height), border_radius=5)

def draw_aim_guide(surface, start_pos, speed, angle):
    """Draws a dotted line showing the arrow's predicted trajectory."""
    pos = list(start_pos)
    vel = [speed * math.cos(angle), speed * math.sin(angle)]
    for _ in range(20): # Draw 20 segments of the trajectory
        vel[1] += GRAVITY
        pos[0] += vel[0]
        pos[1] += vel[1]
        pygame.draw.circle(surface, TRAJECTORY_COLOR, pos, 2)


# --- Game Setup ---
bow = Bow(BOW_POSITION, BOW_HEIGHT)
arrow = Arrow(BOW_POSITION)
target = Target(TARGET_X_POS, 100, HEIGHT - 150, TARGET_RADIUS)
clock = pygame.time.Clock()
hit_message = ""
hit_message_timer = 0

# --- Main Game Loop ---
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not arrow.is_flying:
            if event.button == 1:
                pulling_bow = True
        
        if event.type == pygame.MOUSEBUTTONUP and pulling_bow:
            pulling_bow = False
            if pull_strength > MIN_PULL_STRENGTH:
                arrow.launch(pull_strength * PULL_SPEED_FACTOR, pull_angle)
            pull_strength = 0

    # --- Game Logic ---
    if pulling_bow:
        # Calculate pull strength and angle based on mouse position
        dx = BOW_POSITION[0] - mouse_pos[0]
        dy = BOW_POSITION[1] - mouse_pos[1]
        pull_angle = math.atan2(dy, dx)
        pull_strength = min(math.hypot(dx, dy), MAX_PULL_STRENGTH)
    
    if arrow.is_flying:
        arrow.update()
        
        # Check for hit
        points_scored = target.check_hit(arrow.pos)
        if points_scored > 0:
            score += points_scored
            hit_message = f"+{points_scored}!"
            hit_message_timer = current_time + 1000 # Show for 1 second
            arrow.reset()
            target.reset_pos()
            
        # Check for out of bounds
        if not (0 < arrow.pos[0] < WIDTH and 0 < arrow.pos[1] < HEIGHT):
            hit_message = "Miss!"
            hit_message_timer = current_time + 1000
            arrow.reset()
            
    # --- Drawing ---
    draw_background(screen)
    target.draw(screen)

    # Draw Bow and Arrow
    if pulling_bow:
        # The "pull distance" is how far back the string is drawn visually
        visual_pull_dist = pull_strength / 2
        bow.draw(screen, visual_pull_dist, pull_angle)
        
        # Draw the arrow nocked on the string
        nock_x = BOW_POSITION[0] - visual_pull_dist * math.cos(pull_angle)
        nock_y = BOW_POSITION[1] - visual_pull_dist * math.sin(pull_angle)
        arrow.pos = [nock_x, nock_y]
        arrow.draw(screen, angle_override=pull_angle)

        # Draw trajectory guide
        draw_aim_guide(screen, arrow.pos, pull_strength * PULL_SPEED_FACTOR, pull_angle)

    elif arrow.is_flying:
        arrow.draw(screen)
    else: # Resting state
        bow.draw(screen, 0, 0)
        arrow.draw(screen, angle_override=0)

    draw_ui(screen)

    # Display hit/miss message
    if current_time < hit_message_timer:
        msg_color = SCORE_COLOR if "+" in hit_message else (255, 0, 0)
        msg_text = message_font.render(hit_message, True, msg_color)
        screen.blit(msg_text, (target.x - msg_text.get_width()//2, target.y - 80))

    pygame.display.flip()
    clock.tick(60)

# --- Exit ---
pygame.quit()
sys.exit()