import logging, json

logging.basicConfig(level=logging.INFO)

from swibots import (
    Client,
    InlineKeyboardButton,
    BotCommand,
    BotContext,
    CommandEvent,
    InlineMarkup,
    regexp,
    CallbackQueryEvent,
)

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQxNCwiaXNfYm90Ijp0cnVlLCJhY3RpdmUiOnRydWUsImlhdCI6MTY5NTI0Njk4MSwiZXhwIjoyMzI2Mzk4OTgxfQ.KKFgLIxa6Fup793fPDsJh4ZQzhoaLacJ_NUs9v3PGqs"

bot = Client(token)
bot.set_bot_commands(
    [BotCommand("start", "Get samples", True), BotCommand("sample2", "Anime", True)]
)
true = True
false = False


@bot.on_callback_query(regexp(r"anime"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Anime")
    queryId = ctx.event.query_id
    data = {
        "type": "appPage",
        "mode": "fullscreen",
        "container": {
            "height": 1200,
            "width": 1000,
            "bgColor": "#000000",
            "column": {
                "color": "#000000",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "start",
                "crossAxisAlignment": "start",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "rows": [
                        {
                            "color": "#000000",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "start",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 0, "u": 0, "d": 0},
                            "children": {
                                "layout": {
                                    "type": "carousel",
                                    "title": "text",
                                    "subTitle": "texts",
                                    "icon": "texts",
                                    "iconAlignment": "right",
                                    "size": 5.6,
                                    "components": [
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                            "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/30799/use_mask_white_man-01.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                            "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                            "padding": {"r": 0, "l": 0, "u": 0, "d": 0},
                                        },
                                    ],
                                }
                            },
                        },
                        {
                            "color": "#000000",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "start",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 0, "u": 10, "d": 0},
                            "children": {
                                "component": {
                                    "type": "text",
                                    "text": "Most Popular now",
                                    "size": 30,
                                    "color": "#ffffff",
                                    "opacity": 0.5,
                                    "align": "left",
                                }
                            },
                        },
                        {
                            "color": "#000000",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "start",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 5, "u": 0, "d": 10},
                            "children": {
                                "columns": [
                                    {
                                        "color": "#ffffff",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "start",
                                        "crossAxisAlignment": "start",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqsJnASaZ7NkA0mGQpQ8L3K0aRqzk8VA69pQ&usqp=CAU",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                    {
                                        "color": "#ffffff",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "start",
                                        "crossAxisAlignment": "start",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Anime 2",
                                                "subTitle": "see me Later",
                                                "coverImage": "https://img.freepik.com/free-vector/hand-drawn-vintage-comic-illustration_52683-97130.jpg?w=360",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                    {
                                        "color": "#ffffff",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "start",
                                        "crossAxisAlignment": "start",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 3",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                ]
                            },
                        },
                        {
                            "color": "#000000",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "start",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 0, "u": 10, "d": 0},
                            "children": {
                                "component": {
                                    "type": "text",
                                    "text": "One Peice",
                                    "size": 30,
                                    "color": "#ffffff",
                                    "opacity": 0.5,
                                    "align": "left",
                                }
                            },
                        },
                        {
                            "color": "#000000",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "start",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 5, "u": 0, "d": 10},
                            "children": {
                                "columns": [
                                    {
                                        "color": "#ffffff",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "start",
                                        "crossAxisAlignment": "start",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqsJnASaZ7NkA0mGQpQ8L3K0aRqzk8VA69pQ&usqp=CAU",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                    {
                                        "color": "#ffffff",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "start",
                                        "crossAxisAlignment": "start",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Anime 2",
                                                "subTitle": "see me Later",
                                                "coverImage": "https://img.freepik.com/free-vector/hand-drawn-vintage-comic-illustration_52683-97130.jpg?w=360",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                    {
                                        "color": "#ffffff",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "start",
                                        "crossAxisAlignment": "start",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 3",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                    {
                                        "color": "#000000",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "start",
                                        "crossAxisAlignment": "start",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 0, "u": 10, "d": 0},
                                        "children": {
                                            "component": {
                                                "type": "text",
                                                "text": "One Peice",
                                                "size": 30,
                                                "color": "#ffffff",
                                                "opacity": 0.5,
                                                "align": "left",
                                            }
                                        },
                                    },
                                ]
                            },
                        },
                    ]
                },
            },
        },
        "pageBar": {
            "title": "AniWatch",
            "subtitle": "",
            "rightIcon": {
                "type": "icon",
                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                "callbackData": "callback data",
                "size": 15,
                "button": true,
            },
        },
    }
    data["callbackQueryId"] = queryId
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"app"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    queryId = ctx.event.query_id

    print("Clicked Complete")
    data = {
        "callbackQueryId": queryId,
        "type": "appPage",
        "mode": "fullscreen",
        "container": {
            "height": 600,
            "width": 400,
            "bgColor": "white",
            "column": {
                "color": "black",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "rows": [
                        {
                            "color": "white",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "center",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 0, "u": 0, "d": 0},
                            "children": {
                                "component": {
                                    "type": "text",
                                    "text": "Hello User!",
                                    "size": 10,
                                    "color": "black",
                                    "opacity": 0.5,
                                    "align": "left",
                                }
                            },
                        },
                        {
                            "color": "white",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "center",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 5, "u": 0, "d": 10},
                            "children": {
                                "component": {
                                    "type": "image",
                                    "mediaUrl": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                    "expandOnClick": false,
                                    "callbackData": "",
                                }
                            },
                        },
                        {
                            "color": "white",
                            "scrollable": true,
                            "mainAxisSize": "max",
                            "mainAxisAlignment": "start",
                            "crossAxisAlignment": "center",
                            "expansion": "default_expansion",
                            "padding": {"r": 0, "l": 5, "u": 0, "d": 10},
                            "children": {
                                "columns": [
                                    {
                                        "color": "black",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "center",
                                        "crossAxisAlignment": "center",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                    {
                                        "color": "black",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "center",
                                        "crossAxisAlignment": "center",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                    {
                                        "color": "black",
                                        "scrollable": true,
                                        "mainAxisSize": "max",
                                        "mainAxisAlignment": "center",
                                        "crossAxisAlignment": "center",
                                        "expansion": "default_expansion",
                                        "padding": {"r": 0, "l": 5, "u": 0, "d": 0},
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                                "iconAlignment": "",
                                                "size": 255,
                                                "components": [],
                                            },
                                            "rows": [],
                                        },
                                    },
                                ]
                            },
                        },
                    ]
                },
            },
        },
        "pageBar": {
            "title": "text",
            "subtitle": "texts",
            "leftIcon": {
                "type": "icon",
                "name": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                "callbackData": "callback data",
                "size": 15,
                "button": true,
            },
        },
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_command("start")
async def getSamples(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    await m.reply_text(
        "Click Below to open app!",
        inline_markup=InlineMarkup(
            [
                [InlineKeyboardButton("Launch App", callback_data=r"app", is_app=True)],
            ]
        ),
    )


@bot.on_command("sample2")
async def getSamples(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    await m.reply_text(
        "Click Below to open app!",
        inline_markup=InlineMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Launch App", callback_data=r"anime", is_app=True
                    )
                ],
            ]
        ),
    )


bot.run()
