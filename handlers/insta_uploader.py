from loader import dp
from aiogram import types

video_path = "/home/pi/telegram-bots/tg-bots/tulzbot/video.mp4"
caption = """Прояви актив! Поставь свой царский лайк ❤️ и подпишись @vidos.mem4ik 🔥🤝
• ~~~~~ •
🔹 Всем хорошего и приятного дня! 👌
🔹 Спасибо за поддержку! 🤝
• ~~~~~ •
🔸 Подпишись на новые видосы ➡️ @vidos.mem4ik 🔔
🔸 Отмечай друзей 👫
🔸 Оставляй комментарии ⌨️
🔸 Новые посты каждый день 📆
• ~~~~~ •
#смехота #смех😂 #смехдослёз #хахачкала #смешнодослез #смешныевидеоприколы #чёрныйюмор #юмормастеров #угарно #угарныевидео #видеожара #хахаха #hahaha #взаимныелайки #видеоприколы2022 #приколы2022 #прикольноевидео #прикольное #кино🎥🍿 #кино🎥 #киномания #ржачь😂 #пранки #ржака😂
"""


@dp.channel_post(lambda post: post.chat.id == -1001614366263)
async def channel_post_h(post: types.Message):
    print(post)
    if post.video:
        if post.text: text = post.text + "\n•\n•\n•\n•\n•\n" + caption
        else: text = caption
        # video = await bot.download(post.video, video_path)
        # ig_client.video_upload(video_path, text)
        await post.reply("Done!")
