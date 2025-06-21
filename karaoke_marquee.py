from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# បញ្ចូលវីដេអូ
video = VideoFileClip("lv_0_20250621072005.mp4")

# អត្ថបទអក្សររត់
text = "ខ្ញុំស្រលាញ់អ្នកណាស់ កុំអោយខ្ញុំឈឺចាប់តែមួយឯង..."

# កំណត់ font និងទំហំ
font_path = "LimonS4.ttf"  # ពុម្ពអក្សរខ្មែរ .ttf
fontsize = 40
speed = 100  # កំណត់ល្បឿនអក្សររត់ (ចំនួនកាន់តែធំ = លឿន)

# បង្កើត TextClip ជាពណ៌ក្រហម និងខៀវ
colors = ["red", "blue"]
text_clips = []

for i, color in enumerate(colors):
    txt_clip = TextClip(text,
                        font=font_path,
                        fontsize=fontsize,
                        color=color,
                        stroke_color="black",
                        stroke_width=1)

    txt_clip = txt_clip.set_duration(video.duration)
    txt_clip = txt_clip.set_position(lambda t: (
        video.w - (t * speed) % (video.w + txt_clip.w),
        video.h - 60 + i * 2))

    text_clips.append(txt_clip)

# បញ្ចូល text clips ទៅលើវីដេអូ
final = CompositeVideoClip([video] + text_clips)

# បញ្ចេញវីដេអូថ្មី
final.write_videofile("output_karaoke.mp4", codec="libx264", audio_codec="aac")
