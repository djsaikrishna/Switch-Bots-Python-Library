import logging

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
bot.set_bot_commands([BotCommand("start", "Get samples", True)])
true = True
false = False


@bot.on_callback_query(regexp(r"toast"))
async def showNudge(ctx: BotContext[CallbackQueryEvent]):
    queryId = ctx.event.query_id
    data = {
        "callbackQueryId": queryId,
        "type": "toast",
        "icon": {
            "type": "icon",
            "name": "82ca2255-35bd-4e63-880c-087fc7e6e783",
            "callbackData": "",
            "size": 20,
            "button": False,
        },
        "title": "Hello user",
        "description": "GO that way",
        "duration": 10,
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"cardnudge"))
async def showNudge(ctx: BotContext[CallbackQueryEvent]):
    print("CardNudge")
    queryId = ctx.event.query_id
    data = {
        "callbackQueryId": queryId,
        "type": "card_nudge",
        "icon": {
            "type": "icon",
            "name": "82ca2255-35bd-4e63-880c-087fc7e6e783",
            "callbackData": "",
            "size": 20,
            "button": False,
        },
        "title": "Hello user",
        "subTitle": "GO that way",
        "tag": "construction",
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"banner"))
async def showNudge(ctx: BotContext[CallbackQueryEvent]):
    queryId = ctx.event.query_id
    print("Banner")
    data = {
        "callbackQueryId": queryId,
        "type": "banner",
        "text": {
            "type": "text",
            "text": "Hello this is banner",
            "size": 30,
            "color": "black",
            "align": "center",
        },
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"dynamic"))
async def showNudge(ctx: BotContext[CallbackQueryEvent]):
    queryId = ctx.event.query_id
    print("dynamic callback")
    data = {
        "callbackQueryId": queryId,
        "type": "answer_callback",
        "text": {
            "type": "text",
            "text": "Hello this is header",
            "size": 30,
            "color": "black",
            "align": "center",
        },
        "container": {
            "height": 800,
            "width": 400,
            "bgColour": "white",
            "column": {
                "color": "black",
                "scrollable": True,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "rows": [
                    {
                        "type": "row",
                        "color": "white",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "center",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                        "children": {
                            "component": {
                                "type": "image",
                                "mediaUrl": "https://www.freevector.com/uploads/vector/preview/30799/use_mask_white_man-01.jpg",
                                "expandOnClick": false,
                                "callbackData": "",
                            },
                        },
                    },
                    {
                        "type": "row",
                        "color": "white",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "center",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                        "children": {
                            "component": {
                                "type": "image",
                                "mediaUrl": "https://www.freevector.com/uploads/vector/preview/30799/use_mask_white_man-01.jpg",
                                "expandOnClick": false,
                                "callbackData": "",
                            },
                        },
                    },
                    {
                        "type": "row",
                        "color": "white",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "center",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                        "children": {
                            "component": {
                                "type": "image",
                                "mediaUrl": "https://www.freevector.com/uploads/vector/preview/30799/use_mask_white_man-01.jpg",
                                "expandOnClick": false,
                                "callbackData": "",
                            },
                        },
                    },
                ],
            },
        },
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"app"))
async def showApp(ctx: BotContext[CommandEvent]):
    queryId = ctx.event.query_id
    print("Clicked App")
    data = {
        "type": "appPage",
        "callbackQueryId": queryId,
        "mode": "fullscreen",
        "container": {
            "height": "20",
            "width": "20",
            "bgColor": "white",
            "row": {
                "color": "white",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "component": {
                        "type": "text",
                        "text": "text",
                        "size": 5,
                        "color": "black",
                        "opacity": 0.5,
                        "align": "right",
                    },
                    "layout": {
                        "type": "card",
                        "title": "text",
                        "subTitle": "texts",
                        "coverImage": "text",
                        "icon": "texts",
                        "iconAlignment": "right",
                        "size": 5.6,
                        "components": [
                            {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            }
                        ],
                    },
                },
                "columns": [
                    {
                        "color": "black",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "center",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                        "children": {
                            "component": {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            },
                            "layout": {
                                "type": "card",
                                "title": "text",
                                "subTitle": "texts",
                                "coverImage": "text",
                                "icon": "texts",
                                "iconAlignment": "right",
                                "size": 5.6,
                                "components": [
                                    {
                                        "type": "text",
                                        "text": "text",
                                        "size": 5,
                                        "color": "black",
                                        "opacity": 0.5,
                                        "align": "right",
                                    }
                                ],
                            },
                        },
                        "rows": [],
                    }
                ],
            },
            "column": {
                "color": "black",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "component": {
                        "type": "text",
                        "text": "text",
                        "size": 5,
                        "color": "black",
                        "opacity": 0.5,
                        "align": "right",
                    },
                    "layout": {
                        "type": "card",
                        "title": "text",
                        "subTitle": "texts",
                        "coverImage": "text",
                        "icon": "texts",
                        "iconAlignment": "right",
                        "size": 5.6,
                        "components": [
                            {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            }
                        ],
                    },
                },
                "rows": [],
            },
        },
        "pageBar": {
            "title": "text",
            "subtitle": "texts",
            "leftIcon": {
                "type": "icon",
                "name": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                "callbackData": "callback data",
                "size": "6",
                "button": True,
            },
        },
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"capp"))
async def showApp(ctx: BotContext[CommandEvent]):
    queryId = ctx.event.query_id
    print("capp")
    data = {
        "type": "appPage",
        "callbackQueryId": queryId,
        "mode": "fullscreen",
        "container": {
            "height": "20",
            "width": "20",
            "bgColor": "white",
            "row": {
                "color": "white",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "component": {
                        "type": "text",
                        "text": "text",
                        "size": 5,
                        "color": "black",
                        "opacity": 0.5,
                        "align": "right",
                    },
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
                            },
                            {
                                "type": "image",
                                "mediaUrl": "https://www.freevector.com/uploads/vector/preview/30799/use_mask_white_man-01.jpg",
                                "expandOnClick": false,
                                "callbackData": "",
                            },
                            {
                                "type": "image",
                                "mediaUrl": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                "expandOnClick": false,
                                "callbackData": "",
                            },
                        ],
                    },
                },
                "columns": [
                    {
                        "color": "black",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "center",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                        "children": {
                            "component": {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            },
                            "layout": {
                                "type": "card",
                                "title": "text",
                                "subTitle": "texts",
                                "coverImage": "text",
                                "icon": "texts",
                                "iconAlignment": "right",
                                "size": 5.6,
                                "components": [
                                    {
                                        "type": "text",
                                        "text": "text",
                                        "size": 5,
                                        "color": "black",
                                        "opacity": 0.5,
                                        "align": "right",
                                    }
                                ],
                            },
                        },
                        "rows": [],
                    }
                ],
            },
            "column": {
                "color": "black",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "component": {
                        "type": "text",
                        "text": "text",
                        "size": 5,
                        "color": "black",
                        "opacity": 0.5,
                        "align": "right",
                    },
                    "layout": {
                        "type": "card",
                        "title": "text",
                        "subTitle": "texts",
                        "coverImage": "text",
                        "icon": "texts",
                        "iconAlignment": "right",
                        "size": 5.6,
                        "components": [
                            {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            }
                        ],
                    },
                },
                "rows": [],
            },
        },
        "pageBar": {
            "title": "text",
            "subtitle": "texts",
            "leftIcon": {
                "type": "icon",
                "name": "left icon name",
                "callbackData": "callback data",
                "size": "6",
                "button": True,
            },
        },
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"example"))
async def ___e(ctx: BotContext[CallbackQueryEvent]):
    print(ctx.event.query_id, "Example")
    data = {
        "type": "appPage",
        "callbackQueryId": ctx.event.query_id,
        "mode": "fullscreen",
        "container": {
            "height": "20",
            "width": "20",
            "bgColor": "white",
            "row": {
                "color": "white",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "component": {
                        "type": "text",
                        "text": "text",
                        "size": 5,
                        "color": "black",
                        "opacity": 0.5,
                        "align": "right",
                    },
                    "layout": {
                        "type": "card",
                        "title": "text",
                        "subTitle": "texts",
                        "coverImage": "text",
                        "icon": "texts",
                        "iconAlignment": "right",
                        "size": 5.6,
                        "components": [
                            {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            }
                        ],
                    },
                },
                "columns": [
                    {
                        "color": "black",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "center",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                        "children": {
                            "component": {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            },
                            "layout": {
                                "type": "card",
                                "title": "text",
                                "subTitle": "texts",
                                "coverImage": "text",
                                "icon": "texts",
                                "iconAlignment": "right",
                                "size": 5.6,
                                "components": [
                                    {
                                        "type": "text",
                                        "text": "text",
                                        "size": 5,
                                        "color": "black",
                                        "opacity": 0.5,
                                        "align": "right",
                                    }
                                ],
                            },
                        },
                        "rows": [],
                    }
                ],
            },
            "column": {
                "color": "black",
                "scrollable": true,
                "mainAxisSize": "max",
                "mainAxisAlignment": "center",
                "crossAxisAlignment": "center",
                "expansion": "default_expansion",
                "padding": {"r": 5, "l": 5, "u": 5, "d": 5},
                "children": {
                    "component": {
                        "type": "text",
                        "text": "text",
                        "size": 5,
                        "color": "black",
                        "opacity": 0.5,
                        "align": "right",
                    },
                    "layout": {
                        "type": "card",
                        "title": "text",
                        "subTitle": "texts",
                        "coverImage": "text",
                        "icon": "texts",
                        "iconAlignment": "right",
                        "size": 5.6,
                        "components": [
                            {
                                "type": "text",
                                "text": "text",
                                "size": 5,
                                "color": "black",
                                "opacity": 0.5,
                                "align": "right",
                            }
                        ],
                    },
                },
                "rows": [],
            },
        },
        "pageBar": {
            "title": "text",
            "subtitle": "texts",
            "leftIcon": {
                "type": "icon",
                "name": "left icon name",
                "callbackData": "callback data",
                "size": "6",
                "button": true,
            },
        },
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_callback_query(regexp(r"Complete"))
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
                "children": None,
                "rows": [
                    {
                        "type": "row",
                        "color": "white",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "left",
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
                            },
                        },
                    },
                    {
                        "type": "row",
                        "color": "white",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "left",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 0, "l": 5, "u": 0, "d": 10},
                        "children": {
                            "component": {
                                "type": "image",
                                "mediaUrl": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                "expandOnClick": false,
                                "callbackData": "",
                            },
                        },
                    },
                    {
                        "type": "row",
                        "color": "white",
                        "scrollable": true,
                        "mainAxisSize": "max",
                        "mainAxisAlignment": "start",
                        "crossAxisAlignment": "center",
                        "expansion": "default_expansion",
                        "padding": {"r": 0, "l": 5, "u": 0, "d": 10},
                        "columns": [
                            {
                                "type": "column",
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
                                },
                                "rows": [],
                            },
                            {
                                "type": "column",
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
                                },
                                "rows": [],
                            },
                            {
                                "type": "column",
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
                                },
                                "rows": [],
                            },
                        ],
                    },
                ],
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
                "button": True,
            },
        },
    }
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_command("start")
async def getSamples(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    await m.reply_text(
        "List of Samples",
        inline_markup=InlineMarkup(
            [
                [InlineKeyboardButton("Card Nudge", callback_data="cardnudge")],
                [InlineKeyboardButton("Toast", callback_data=r"toast")],
                [InlineKeyboardButton("Dynamic Callback", callback_data=r"dynamic")],
                [InlineKeyboardButton("Banner", callback_data=r"banner")],
                [InlineKeyboardButton("App", callback_data=r"app")],
                [
                    InlineKeyboardButton(
                        "Carousel App", callback_data=r"capp", is_app=True
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Example App", callback_data=r"example", is_app=True
                    )
                ],
                [
                    InlineKeyboardButton(
                        "App II", callback_data=r"Complete", is_app=True
                    )
                ],
            ]
        ),
    )


bot.run()
