from telethon import events, Button, TelegramClient
from sqlite3 import connect
import config
from telethon.errors import TimedOutError


bot = TelegramClient("robot", config.api_id, config.api_hash, proxy=None if config.proxy is False else config.proxy_address)
print("connecting...")
bot.start(bot_token=config.bot_token)
print("connected!")
db = connect('bot.db')
cur = db.cursor()
bot_text = config.bot_text


@bot.on(events.NewMessage())
async def handler(event):
    text = event.raw_text
    user_id = event.sender_id
    if text == "/start":
        find_user = cur.execute(f"SELECT * FROM users WHERE user_id = {user_id}").fetchone()
        if find_user is None:
            cur.execute(f"INSERT INTO users VALUES ({user_id}, {0}, '{'آزمون نداده'}')")
            db.commit()
            buttons = [
                Button.inline(bot_text["start_test"], b'start_test')
            ]
            await event.reply(bot_text["no_score_start"], buttons=buttons)
        else:
            score = find_user[1]
            if score == 0:
                buttons = [
                    Button.inline(bot_text["start_test"], b'start_test')
                ]
                await event.reply(bot_text["no_score_start"], buttons=buttons)
            else:
                buttons = [
                    [Button.inline(bot_text["re_test"], b'start_test')],
                    [Button.inline(bot_text["information"], b'information')]
                ]
                await event.reply(bot_text["start"], buttons=buttons)
    # elif text == bot_text["start_test"]:
@bot.on(events.CallbackQuery(data=b'information'))
async def information(event):
    user_id = event.sender_id
    find_user = cur.execute(f"SELECT * FROM users WHERE user_id = {user_id}").fetchone()
    text = f"اطلاعات شما:\nامتیاز: {find_user[1]}\nنتیجه آزمون شما:{find_user[2]}"
    await event.reply(text)
@bot.on(events.CallbackQuery(data=b'start_test'))
async def start_test(event):
    user_id = event.sender_id

    await event.reply(bot_text["start_test_text"])
    async with bot.conversation(user_id) as conv:
        q1_scores = {
            "a": 10,
            "b": 5,
            "c": 2,
        }
        q1_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_1"], buttons=q1_buttons)
        q1_score = 0
        q1_response = await conv.wait_event(events.CallbackQuery())
        q1_response = q1_response.data
        if q1_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q1_score = q1_scores[q1_response.decode()]
        q2_scores = {
            "a": 10,
            "b": 5,
            "c": 2,
        }
        q2_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_2"], buttons=q2_buttons)
        q2_score = 0
        q2_response = await conv.wait_event(events.CallbackQuery())
        q2_response = q2_response.data
        if q2_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q2_score = q2_scores[q2_response.decode()]
        q3_scores = {
            "a": 10,
            "b": 2,
            "c": 5,
        }
        q3_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_3"], buttons=q1_buttons)
        q3_score = 0
        q3_response = await conv.wait_event(events.CallbackQuery())
        q3_response = q3_response.data
        if q3_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q3_score = q3_scores[q3_response.decode()]
        q4_scores = {
            "a": 10,
            "b": 5,
            "c": 2,
        }
        q4_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_4"], buttons=q4_buttons)
        q4_score = 0
        q4_response = await conv.wait_event(events.CallbackQuery())
        q4_response = q4_response.data
        if q4_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q4_score = q4_scores[q4_response.decode()]
        q5_scores = {
            "a": 10,
            "b": 3,
            "c": 2,
        }
        q5_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_5"], buttons=q5_buttons)
        q5_score = 0
        q5_response = await conv.wait_event(events.CallbackQuery())
        q5_response = q5_response.data
        if q5_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q5_score = q5_scores[q5_response.decode()]
        q6_scores = {
            "a": 10,
            "b": 2,
            "c": 10,
            "d": 5,
        }
        q6_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["d"], b'd'),
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_6"], buttons=q6_buttons)
        q6_score = 0
        q6_response = await conv.wait_event(events.CallbackQuery())
        q6_response = q6_response.data
        if q6_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q6_score = q6_scores[q6_response.decode()]
        q7_scores = {
            "a": 2,
            "b": 5,
            "c": 10,
        }
        q7_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_7"], buttons=q7_buttons)
        q7_score = 0
        q7_response = await conv.wait_event(events.CallbackQuery())
        q7_response = q7_response.data
        if q7_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q7_score = q7_scores[q7_response.decode()]
        q8_scores = {
            "a": 10,
            "b": 2,
        }
        q8_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_8"], buttons=q8_buttons)
        q8_score = 0
        q8_response = await conv.wait_event(events.CallbackQuery())
        q8_response = q8_response.data
        if q8_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q8_score = q8_scores[q8_response.decode()]
        await event.reply(bot_text["next_questions"])
        q9_scores = {
            "a": 4,
            "b": 4,
            "c": 4,
            "d": 4,
            "e": 4,
            "f": 4,
            "g": 4,
            "h": 4,
            "i": 1,
        }
        q9_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["d"], b'd')
            ],
            [
                Button.inline(bot_text["e"], b'e')
            ],
            [
                Button.inline(bot_text["f"], b'f')
            ],
            [
                Button.inline(bot_text["g"], b'g')
            ],
            [
                Button.inline(bot_text["h"], b'h')
            ],
            [
                Button.inline(bot_text["i"], b'i')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_9"], buttons=q9_buttons)
        q9_score = 0
        q9_response = await conv.wait_event(events.CallbackQuery())
        q9_response = q9_response.data
        if q9_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q9_score = q9_scores[q9_response.decode()]
        q10_scores = {
            "a": 4,
            "b": 4,
            "c": 4,
            "d": 4,
            "e": 4,
            "f": 4,
            "g": 4,
            "h": 4,
            "i": 1,
        }
        q10_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["d"], b'd')
            ],
            [
                Button.inline(bot_text["e"], b'e')
            ],
            [
                Button.inline(bot_text["f"], b'f')
            ],
            [
                Button.inline(bot_text["g"], b'g')
            ],
            [
                Button.inline(bot_text["h"], b'h')
            ],
            [
                Button.inline(bot_text["i"], b'i')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_10"], buttons=q10_buttons)
        q10_score = 0
        q10_response = await conv.wait_event(events.CallbackQuery())
        q10_response = q10_response.data
        if q10_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q10_score = q10_scores[q10_response.decode()]
        q11_scores = {
            "a": 4,
            "b": 4,
            "c": 4,
            "d": 4,
            "e": 4,
            "f": 4,
            "g": 4,
            "h": 4,
            "i": 1,
        }
        q11_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["d"], b'd')
            ],
            [
                Button.inline(bot_text["e"], b'e')
            ],
            [
                Button.inline(bot_text["f"], b'f')
            ],
            [
                Button.inline(bot_text["g"], b'g')
            ],
            [
                Button.inline(bot_text["h"], b'h')
            ],
            [
                Button.inline(bot_text["i"], b'i')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_11"], buttons=q11_buttons)
        q11_score = 0
        q11_response = await conv.wait_event(events.CallbackQuery())
        q11_response = q11_response.data
        if q11_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q11_score = q11_scores[q11_response.decode()]
        q12_scores = {
            "a": 4,
            "b": 4,
            "c": 4,
            "d": 4,
            "e": 4,
            "f": 4,
            "g": 4,
            "h": 4,
            "i": 1,
        }
        q12_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["d"], b'd')
            ],
            [
                Button.inline(bot_text["e"], b'e')
            ],
            [
                Button.inline(bot_text["f"], b'f')
            ],
            [
                Button.inline(bot_text["g"], b'g')
            ],
            [
                Button.inline(bot_text["h"], b'h')
            ],
            [
                Button.inline(bot_text["i"], b'i')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_12"], buttons=q12_buttons)
        q12_score = 0
        q12_response = await conv.wait_event(events.CallbackQuery())
        q12_response = q12_response.data
        if q12_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q12_score = q12_scores[q12_response.decode()]
        q13_scores = {
            "a": 4,
            "b": 4,
            "c": 4,
            "d": 4,
            "e": 4,
            "f": 4,
            "g": 4,
            "h": 4,
            "i": 1,
        }
        q13_buttons = [
            [
                Button.inline(bot_text["a"], b'a')
            ],
            [
                Button.inline(bot_text["b"], b'b')
            ],
            [
                Button.inline(bot_text["c"], b'c')
            ],
            [
                Button.inline(bot_text["d"], b'd')
            ],
            [
                Button.inline(bot_text["e"], b'e')
            ],
            [
                Button.inline(bot_text["f"], b'f')
            ],
            [
                Button.inline(bot_text["g"], b'g')
            ],
            [
                Button.inline(bot_text["h"], b'h')
            ],
            [
                Button.inline(bot_text["i"], b'i')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_13"], buttons=q13_buttons)
        q13_score = 0
        q13_response = await conv.wait_event(events.CallbackQuery())
        q13_response = q13_response.data
        if q13_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q13_score = q13_scores[q13_response.decode()]
        q14_scores = {
            "a": 2,
            "b": 10,
        }
        q14_buttons = [
            [
                Button.inline(bot_text["yes"], b'a')
            ],
            [
                Button.inline(bot_text["no"], b'b')
            ],
            [
                Button.inline(bot_text["cancel"], b'cancel')
            ]
        ]
        r = await conv.send_message(bot_text["question_14"], buttons=q14_buttons)
        q14_score = 0
        q14_response = await conv.wait_event(events.CallbackQuery())
        q14_response = q14_response.data
        if q4_response == b'cancel':
            await conv.send_message(bot_text["canceled"])
            await bot.delete_messages(user_id, r.id)
            return
        else:
            await bot.delete_messages(user_id, r.id)
            q14_score = q14_scores[q14_response.decode()]
    score = q1_score + q2_score + q3_score + q4_score + q5_score + q6_score + q7_score + q8_score + q9_score + q10_score + q11_score + q12_score + q13_score + q14_score
    test_result = None
    if score < 40:
        test_result = "خیلی بد حتما پاکسازی عمیق و فنگشویی انجام شود"
    elif score >= 40 and score < 70:
        test_result = "معمولی و احتیاج به مشاوره"
    else:
        test_result = "عالی، احتیاج به فنگشویی و درمانگری ندارید، فقط تقویت المان ها"
    print(cur.execute(f"SELECT * FROM users WHERE user_id={user_id}").fetchone())
    cur.execute(f"UPDATE users SET score = {score},level='{test_result}' WHERE user_id={user_id}")
    db.commit()
    print(cur.execute(f"SELECT * FROM users WHERE user_id={user_id}").fetchone())
    await event.reply(bot_text["result"].format(score=score, test_result=test_result))
if __name__ == "__main__":
    bot.run_until_disconnected()
