import main
from main import blockify
import themes.theme_manager as theme_manager


health = 3
class Blocks:
    def __init__(self):
        self.num_rows = None
        self.num_blocks = None
        self.block_gap = None
        

        self.SCREEN_WIDTH = main.config.get('display_size')[0]
        self.SCREEN_HEIGHT = main.config.get('display_size')[1]
        self.active_blocks = []

        self.calculate_rect()

    
    
    def calculate_rect(self):
        self.num_rows = 5
        self.num_blocks = 10
        self.block_gap = 10
        
        
        block_image_paths = [
            f'resources/images/themes/{theme_manager.get_name(theme_manager.current_theme)}/blocks/block{i}.png'
            for i in range(1, self.num_blocks + 1)
        ]

        for row_num in range(self.num_rows):
            for block_num in range(self.num_blocks):
                image_path = block_image_paths[row_num]
                image = blockify.image.load(image_path)

                rect = image.get_rect()
                rect.x = self.block_gap + (rect.width + self.block_gap) * block_num
                rect.y = self.block_gap + (rect.height + self.block_gap) * row_num

                self.active_blocks.append([image, rect, health])

    def draw_blocks(self, surface):
        for image, rect, health in self.active_blocks:
            surface.blit(image, rect)

    def get_blocks(self):
        return self.active_blocks
    
    def get_health(self, active_block):
            return active_block[2]
        
    
    def set_health(self, active_block):
        if active_block[2] > 0:
            active_block[2] = active_block[2] - 1
        
