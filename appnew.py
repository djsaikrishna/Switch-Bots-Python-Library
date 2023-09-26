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

token = (
    app2
) = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQyMCwiaXNfYm90Ijp0cnVlLCJhY3RpdmUiOnRydWUsImlhdCI6MTY5NTM5MDE2MCwiZXhwIjoyMzI2NTQyMTYwfQ.xekH2bqj2qkPiIzqmdHrD1sscO9Q3EKe8H4ch_FpPNs"

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQxNCwiaXNfYm90Ijp0cnVlLCJhY3RpdmUiOnRydWUsImlhdCI6MTY5NTI0Njk4MSwiZXhwIjoyMzI2Mzk4OTgxfQ.KKFgLIxa6Fup793fPDsJh4ZQzhoaLacJ_NUs9v3PGqs"

bot = Client(token, auto_update_bot=False)
bot.set_bot_commands(
    [
        BotCommand("start", "Get samples", True),
    ]
)

true = True
false = False


@bot.on_callback_query(regexp(r"seeAll"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Grid")
    queryId = ctx.event.query_id
    data = {
        "height": 1200,
        "width": 1000,
        "bgColor": "#000000",
        "column": {
            "color": "#000000",
            "children": {
                "layout": {
                    "type": "grid",
                    "gridSize": 3,
                    "size": 3,
                    "children": [
                        {
#                            "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                        {
 #                           "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                        {
#                            "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                        {
#                            "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                        {
#                            "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                        {
#                            "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                        {
 #                           "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                        {
#                            "type": "grid_tile",
                            "title": "Title",
                            "subTitle": "Subtitle of media",
                            "media": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                            "icon": {
                                "type": "icon",
                                "name": "https://img.icons8.com/?size=256&id=12773&format=png",
                                "callbackData": "callback data",
                                "button": true,
                            },
                        },
                    ],
                }
            },
        },
    }
    #    data["callbackQueryId"] = queryId
    resp = await bot.bots_service.post(
        f"/v1/bots/update/app?callbackQueryId={queryId}",  data={
            "container": data,
            "type": "childrenPage",
            "callbackQueryId": ctx.event.query_id,
            "messageId": ctx.event.message.id,
            "pageId": ctx.event.callback_data
        })
    print(resp.data)


@bot.on_callback_query(regexp(r"srch"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Search")
    queryId = ctx.event.query_id
    data = {"container": {
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
                                "subTitle1": "View most popular animes...",
                                "subTitle2": "See All",
                                "subTitleAction": "seeAll",
                                "rightComponents": [
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2_8YjD9mYSgOZ-uT0XbkyU7xDUBuAmfchMQyWnrILw&s",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd89Lp7hhRqr6Vn764ZLwLHWtOcQJcE7CnXzWasDl-ul4hTYQ57xOdLufGC_mfNsRK6j4&usqp=CAU",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://i.pinimg.com/736x/47/e2/3e/47e23ef9f58145646746b7e911b79c00.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAiE4qvyp6-a2UdTM_FhoI1XamUceFm9CfVoMF36GT-C5VzeiI5xKbbiYzhgJ7kpGaFrs&usqp=CAU",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                ],
                            }
                        },
                    },
                ]
            },
        },
    }}
    #    data["callbackQueryId"] = queryId
    resp = await bot.bots_service.post(
        f"/v1/bots/update/app?callbackQueryId={queryId}", data={
            "container": data,
            "callbackQueryId": ctx.event.query_id,
            
            "type": "childrenPage",
            "messageId": ctx.event.message.id,
            "pageId": ctx.event.callback_data
        }
    )
    print(resp.data)


@bot.on_callback_query(regexp(r"openDetailed"))
async def showResponse(ctx: BotContext[CallbackQueryEvent]):
    print("Detailed")
    queryId = ctx.event.query_id
    data = {
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
                                "subTitle1": "View most popular animes...",
                                "subTitle2": "See All",
                                "subTitleAction": "seeAll",
                                "rightComponents": [
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2_8YjD9mYSgOZ-uT0XbkyU7xDUBuAmfchMQyWnrILw&s",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd89Lp7hhRqr6Vn764ZLwLHWtOcQJcE7CnXzWasDl-ul4hTYQ57xOdLufGC_mfNsRK6j4&usqp=CAU",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://i.pinimg.com/736x/47/e2/3e/47e23ef9f58145646746b7e911b79c00.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAiE4qvyp6-a2UdTM_FhoI1XamUceFm9CfVoMF36GT-C5VzeiI5xKbbiYzhgJ7kpGaFrs&usqp=CAU",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                ],
                            }
                        },
                    },
                ]
            },
        },
        # },
        # "pageBar": {
        #     "title": "One Peice",
        #     "subtitle": "",
        #     "rightIcon": {
        #         "type": "icon",
        #         "name": "https://img.icons8.com/?size=256&id=12773&format=png",
        #         "callbackData": "callback data",
        #         "size": 15,
        #         "button": true,
        #     },
        # },
    }
    #    data["callbackQueryId"] = queryId
    resp = await bot.bots_service.post(
        f"/v1/bots/update/app?callbackQueryId={queryId}",  data={
            "container": data,
            "callbackQueryId": ctx.event.query_id,
            
            "type": "childrenPage",
            "messageId": ctx.event.message.id,
            "pageId": ctx.event.callback_data
        }
    )
    print(resp.data)


@bot.on_callback_query(regexp(r"SearchButton"))
async def onSearch(ctx: BotContext[CallbackQueryEvent]):
    queryId = ctx.event.query_id
    data = {
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
                                "subTitle1": "View most popular animes...",
                                "subTitle2": "See All",
                                "subTitleAction": "seeAll",
                                "rightComponents": [
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2_8YjD9mYSgOZ-uT0XbkyU7xDUBuAmfchMQyWnrILw&s",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd89Lp7hhRqr6Vn764ZLwLHWtOcQJcE7CnXzWasDl-ul4hTYQ57xOdLufGC_mfNsRK6j4&usqp=CAU",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://i.pinimg.com/736x/47/e2/3e/47e23ef9f58145646746b7e911b79c00.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAiE4qvyp6-a2UdTM_FhoI1XamUceFm9CfVoMF36GT-C5VzeiI5xKbbiYzhgJ7kpGaFrs&usqp=CAU",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                    {
                                        "type": "image",
                                        "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                        "expandOnClick": false,
                                        "callbackData": r"openDetailed",
                                    },
                                ],
                            }
                        },
                    },
                ]
            },
        },
        # "pageBar": {
        #     "title": "One Peice",
        #     "subtitle": "",
        #     "rightIcon": {
        #         "type": "icon",
        #         "name": "https://img.icons8.com/?size=256&id=12773&format=png",
        #         "callbackData": "callback data",
        #         "size": 15,
        #         "button": true,
        #     },
        # },
    }
    #    data["callbackQueryId"] = queryId
    resp = await bot.bots_service.post(
        f"/v1/bots/update/app?callbackQueryId={queryId}", data={
            "container": data,
            "type": "childrenPage",
            "callbackQueryId": ctx.event.query_id,
            
            "messageId": ctx.event.message.id,
            "pageId": ctx.event.callback_data
        }
    )
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
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/30799/use_mask_white_man-01.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/7768/FreeVector-Digital-Circle.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
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
                                    "subTitle1": "View most popular animes...",
                                    "subTitle2": "See All",
                                    "subTitleAction": "seeAll",
                                    "rightComponents": [
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
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
                                    "subTitle1": "View most popular animes...",
                                    "subTitle2": "See All",
                                    "subTitleAction": "seeAll",
                                    "rightComponents": [
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2_8YjD9mYSgOZ-uT0XbkyU7xDUBuAmfchMQyWnrILw&s",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd89Lp7hhRqr6Vn764ZLwLHWtOcQJcE7CnXzWasDl-ul4hTYQ57xOdLufGC_mfNsRK6j4&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://i.pinimg.com/736x/47/e2/3e/47e23ef9f58145646746b7e911b79c00.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAiE4qvyp6-a2UdTM_FhoI1XamUceFm9CfVoMF36GT-C5VzeiI5xKbbiYzhgJ7kpGaFrs&usqp=CAU",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
                                        },
                                        {
                                            "type": "image",
                                            "mediaUrl": "https://www.freevector.com/uploads/vector/preview/23063/large_1x_hi.jpg",
                                            "expandOnClick": false,
                                            "callbackData": r"openDetailed",
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
                "callbackData": r"SearchButton",
                "button": true,
            },
        },
    }
    data["callbackQueryId"] = queryId
    resp = await bot.bots_service.post("/v1/bots/callback/answer", data=data)
    print(resp.data)


@bot.on_command("start")
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
