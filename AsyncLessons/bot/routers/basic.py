from datetime import datetime
from aiogram import F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.utils.formatting import Bold, HashTag, as_key_value, as_list, as_marked_section

r = Router()


@r.message(Command("start"))
async def start_message(message: Message):
    await message.answer("Привет! Чем могу помочь?")


@r.message(Command("format"), F.text)
async def any_message(message: Message):
    await message.answer(text="Hello <b>world</b>", parse_mode=ParseMode.HTML)

    await message.answer(text="Hello *world*", parse_mode=ParseMode.MARKDOWN_V2)

    await message.answer(text="Hello `world`", parse_mode=ParseMode.MARKDOWN_V2)

    await message.answer(
        text="Hello <blockquote>world</blockquote>",
    )

    await message.answer(
        text="Hello <u>world</u>",
    )

    await message.answer(text="Hello <s>world</s> without formatting", parse_mode=None)


@r.message(Command("hello"), F.text)
async def hello(message: Message):
    await message.answer(
        text=f"Hello, {html.bold(html.quote(message.from_user.full_name))}"
    )

@r.message(Command("advanced_example"))
async def cmd_advanced_example(message: Message):
    content = as_list(
        as_marked_section(
            Bold("Success:"),
            "Test 1",
            "Test 3",
            "Test 4",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Failed:"),
            "Test 2",
            marker="❌ ",
        ),
        as_marked_section(
            Bold("Summary:"),
            as_key_value("Total", 4),
            as_key_value("Success", 3),
            as_key_value("Failed", 1),
            marker="  ",
        ),
        HashTag("#test"),
        sep="\n\n",
    )
    await message.answer(**content.as_kwargs())


@r.message(Command('settimer'))
async def cmd_settimer(
    message: Message, 
    command: CommandObject
    ):
    if command.args is None:
        await message.answer(
            'Ошибка: не переданы аргументы'
        )
        return
    print(f'Аргументы комманды будут переданны вот в таком виде "{command.args}"')
    try:
        delay_time, text_to_send = command.args.split(' ', maxsplit=1)
    except ValueError:
        await message.answer(
            "Ошибка: Неправильный формат команды. Пример:\n"
            "/settime <time> <message>"
        )
        return
    
    await message.answer(
        'Таймер добавлен!\n'
        f"Время: {delay_time}\n"
        f"Сообщение: {text_to_send}\n"
    )


@r.message(Command('custom1', prefix='%'))
async def cmd_custom(message: Message):
    await message.answer(
        "Вижу комманду!"
    )
    
@r.message(Command('custom2', prefix='/!'))
async def cmd_custom2(message: Message):
    await message.answer(
        "И это комманду тоже вижу!"
    )

@r.message(F.text)
async def extract_data(message: Message):
    data = {
        'url': '<N/A>',
        'email': '<N/A>',
        'code': '<N/A>'
    }
    
    entities = message.entities or []
    
    for item in entities:
        if item.type in data.keys():
            # Неправильно
            # data[item.type] = message.text[item.offset : item.offset+item.length]
            # Правильно
            data[item.type] = item.extract_from(message.text)
    
    await message.reply(
        'Вот что я нашёл\n'
        f'URL: {html.quote(data["url"])}\n'
        f'E-mail: {html.quote(data["email"])}\n'
        f'Пароль: {html.quote(data["code"])}'
    )


# @r.message(F.text)
# async def  echo_with_time(message: Message):
#     time_now = datetime.now().strftime('%H:%M')
#     added_text = html.underline(f'Создано в {time_now}')
#     # print(message.html_text)
#     await message.answer(
#         text = f'{message.html_text}\n\n{added_text}'
#     )
