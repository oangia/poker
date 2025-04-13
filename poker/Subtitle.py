from PIL import Image, ImageDraw, ImageFont

class Subtitle:
    def __init__(self, texts, duration):
        self.texts = texts
        self.duration = duration
        self.total_count = 0
        for text in self.texts:
            self.total_count += len(text)
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size=40)
      
    def generate(self):
        video_width = 1080
        video_height = 1920
        text_clips = []
        current_time = 0
        # Create a text clip for each entry in the array
        for text in self.texts:
            # Create transparent image for each text clip
            img = Image.new("RGBA", (video_width, video_height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            text_duration = len(text) * self.duration / self.total_count
            # Center the text
            bbox = draw.textbbox((0, 0), text, font=self.font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (video_width - text_width) // 2
            y = (video_height - text_height) // 2
    
            # Add a solid rectangle background behind the text (semi-transparent)
            background_padding = 10  # Space between text and background
            draw.rectangle(
                [x - background_padding, y - background_padding, x + text_width + background_padding, y + text_height + background_padding],
                fill=(0, 0, 0, 64)  # Semi-transparent black background (RGBA)
            )
    
            draw.text((x, y), text, font=self.font, fill="white")
    
            # Convert image to clip
            text_img = np.array(img)
            txt_clip = ImageClip(text_img, duration=text_duration - 0.1).set_start(current_time)
    
            # Add to the list of text clips
            text_clips.append(txt_clip)
            current_time += text_duration
    
        return text_clips
