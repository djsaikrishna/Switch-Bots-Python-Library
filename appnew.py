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

token = app2 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQyMCwiaXNfYm90Ijp0cnVlLCJhY3RpdmUiOnRydWUsImlhdCI6MTY5NTM5MDE2MCwiZXhwIjoyMzI2NTQyMTYwfQ.xekH2bqj2qkPiIzqmdHrD1sscO9Q3EKe8H4ch_FpPNs"

#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQxNCwiaXNfYm90Ijp0cnVlLCJhY3RpdmUiOnRydWUsImlhdCI6MTY5NTI0Njk4MSwiZXhwIjoyMzI2Mzk4OTgxfQ.KKFgLIxa6Fup793fPDsJh4ZQzhoaLacJ_NUs9v3PGqs"

bot = Client(token,
             auto_update_bot=False)
bot.set_bot_commands(
    [
        BotCommand("start", "Get samples", True),
        BotCommand("sample2", "Anime", True),
        BotCommand("detailed", "Get detailed Page", True),
        BotCommand("grid", "Get Grid Page", True),
        BotCommand("search", "Get Search Page", True),
        
    ]
)
async def main():
    await bot.start()
    print(await bot.get_community(username="torrent_downloader"))
    return
    print(await bot.get_community_members("3afd3d5d-49b0-460a-839b-942a2837727d"))

bot.run(main())
exit()
true = True
false = False


@bot.on_callback_query(regexp(r"grid"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Grid")
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
                "children": {
                    "component": {
                        "type": "grid",
                        "gridSize": 3,
                        "children": [
                            {
                                "type": "grid_tile",
                                "title": "Title",
                                "subTitle": "Subtitle of media",
                                "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            }
                        ]
                        * 15,
                    }
                },
            },
        },
        "pageBar": {
            "title": "One Peice",
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


@bot.on_callback_query(regexp(r"srch"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Search")
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
                "children": {
                    "rows": [
                        {
                            "children": {
                                "component": {
                                    "type": "searchbar",
                                    "callbackData": "",
                                    "placeholder": "Search anime",
                                    "width": 100,
                                }
                            }
                        },
                        {
                            "color": "#000000",
                            "children": {
                                "layout": {
                                    "type": "list_tile",
                                    "mode": "vertical",
                                    "title": "One Peice",
                                    "subtitle": "View most popular animes...",
                                    "rightComponents": [
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2_8YjD9mYSgOZ-uT0XbkyU7xDUBuAmfchMQyWnrILw&s",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd89Lp7hhRqr6Vn764ZLwLHWtOcQJcE7CnXzWasDl-ul4hTYQ57xOdLufGC_mfNsRK6j4&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://i.pinimg.com/736x/47/e2/3e/47e23ef9f58145646746b7e911b79c00.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAiE4qvyp6-a2UdTM_FhoI1XamUceFm9CfVoMF36GT-C5VzeiI5xKbbiYzhgJ7kpGaFrs&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                    ],
                                }
                            },
                        },
                    ]
                },
            },
        },
        "pageBar": {
            "title": "One Peice",
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


@bot.on_callback_query(regexp(r"ant"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Detailed")
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
                "children": {
                    "rows": [
                        {
                            "color": "#000000",
                            "children": {
                                "component": {
                                    "type": "video_player",
                                    "title": "Godse",
                                    "subtitle": "Never ending story",
                                    "url": "https://hls012.a387e6278d8e06083d813358762e0ac63.com/dstreamhls/9e0e51329fab68c97c0e3be9381fd405/ep.1.v0.1678074211.m3u8",
                                }
                            },
                        },
                        {
                            "children": {
                                "component": {
                                    "type": "action_button",
                                    "text": {
                                        "type": "text",
                                        "text": "Play Now",
                                        "size": 30,
                                    },
                                    "callbackData": "",
                                }
                            }
                        },
                        {
                            "children": {
                                "component": {
                                    "text": {
                                        "text": "In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available"
                                    }
                                }
                            }
                        },
                        {
                            "color": "#000000",
                            "children": {
                                "layout": {
                                    "type": "list_tile",
                                    "title": "One Peice",
                                    "mode": "horizontal",
                                    "subtitle": "View most popular animes...",
                                    "rightComponents": [
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2_8YjD9mYSgOZ-uT0XbkyU7xDUBuAmfchMQyWnrILw&s",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd89Lp7hhRqr6Vn764ZLwLHWtOcQJcE7CnXzWasDl-ul4hTYQ57xOdLufGC_mfNsRK6j4&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://i.pinimg.com/736x/47/e2/3e/47e23ef9f58145646746b7e911b79c00.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAiE4qvyp6-a2UdTM_FhoI1XamUceFm9CfVoMF36GT-C5VzeiI5xKbbiYzhgJ7kpGaFrs&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                    ],
                                }
                            },
                        },
                    ]
                },
            },
        },
        "pageBar": {
            "title": "One Peice",
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


@bot.on_callback_query(regexp(r"anme"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Anime")
    queryId = ctx.event.query_id
    data = {
        "type": "appPage",
        "mode": "fullscreen",
        "container": {
            "bgColor": "#000000",
            "column": {
                "color": "#000000",
                "children": {
                    "rows": [
                        {
                            "color": "#000000",
                            "children": {
                                "layout": {
                                    "type": "carousel",
                                    "title": "text",
                                    "subTitle": "this is a subtitle",
                                    "icon": "texts",
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
                                }
                            },
                        },
                        {
                            "color": "#000000",
                            "children": {
                                "layout": {
                                    "type": "list_tile",
                                    "mode": "horizontal",
                                    "title": "Most Popular",
                                    "subtitle": "View most popular animes...",
                                    "rightComponents": [
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                    ],
                                }
                            },
                        },
                        {
                            "color": "#000000",
                            "children": {
                                "layout": {
                                    "type": "list_tile",
                                    "title": "One Peice",
                                    "mode": "horizontal",
                                    "subtitle": "View most popular animes...",
                                    "rightComponents": [
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2_8YjD9mYSgOZ-uT0XbkyU7xDUBuAmfchMQyWnrILw&s",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd89Lp7hhRqr6Vn764ZLwLHWtOcQJcE7CnXzWasDl-ul4hTYQ57xOdLufGC_mfNsRK6j4&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://i.pinimg.com/736x/47/e2/3e/47e23ef9f58145646746b7e911b79c00.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAiE4qvyp6-a2UdTM_FhoI1XamUceFm9CfVoMF36GT-C5VzeiI5xKbbiYzhgJ7kpGaFrs&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": "",
                                        },
                                    ],
                                }
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
            "bgColor": "white",
            "column": {
                "color": "black",
                "children": {
                    "rows": [
                        {
                            "color": "white",
                            "children": {
                                "component": {
                                    "type": "text",
                                    "text": "Hello User!",
                                    "color": "black",
                                    "align": "left",
                                }
                            },
                        },
                        {
                            "color": "white",
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
                            "children": {
                                "columns": [
                                    {
                                        "color": "black",
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                            },
                                        },
                                    },
                                    {
                                        "color": "black",
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
                                            },
                                        },
                                    },
                                    {
                                        "color": "black",
                                        "children": {
                                            "layout": {
                                                "type": "card",
                                                "title": "Card 1",
                                                "subTitle": "See you later",
                                                "coverImage": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                                "icon": "82ca2255-35bd-4e63-880c-087fc7e6e783",
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


@bot.on_command("detailed")
async def getSamples(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    await m.reply_text(
        "Click Below to open app!",
        inline_markup=InlineMarkup(
            [
                [InlineKeyboardButton("Launch App", callback_data=r"ant", is_app=True)],
            ]
        ),
    )


@bot.on_command("grid")
async def getSamples(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    await m.reply_text(
        "Click Below to open app!",
        inline_markup=InlineMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Launch App", callback_data=r"grid", is_app=True
                    )
                ],
            ]
        ),
    )

@bot.on_command("search")
async def getSamples(ctx: BotContext[CommandEvent]):
    m = ctx.event.message
    await m.reply_text(
        "Click Below to open app!",
        inline_markup=InlineMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Launch App", callback_data=r"srch", is_app=True
                    )
                ],
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
                        "Launch App", callback_data=r"anme", is_app=True
                    )
                ],
            ]
        ),
    )


bot.run()
