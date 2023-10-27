"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[447],{3905:(e,n,r)=>{r.d(n,{Zo:()=>c,kt:()=>h});var t=r(7294);function a(e,n,r){return n in e?Object.defineProperty(e,n,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[n]=r,e}function o(e,n){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);n&&(t=t.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),r.push.apply(r,t)}return r}function l(e){for(var n=1;n<arguments.length;n++){var r=null!=arguments[n]?arguments[n]:{};n%2?o(Object(r),!0).forEach((function(n){a(e,n,r[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(r,n))}))}return e}function s(e,n){if(null==e)return{};var r,t,a=function(e,n){if(null==e)return{};var r,t,a={},o=Object.keys(e);for(t=0;t<o.length;t++)r=o[t],n.indexOf(r)>=0||(a[r]=e[r]);return a}(e,n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(t=0;t<o.length;t++)r=o[t],n.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var i=t.createContext({}),m=function(e){var n=t.useContext(i),r=n;return e&&(r="function"==typeof e?e(n):l(l({},n),e)),r},c=function(e){var n=m(e.components);return t.createElement(i.Provider,{value:n},e.children)},d="mdxType",p={inlineCode:"code",wrapper:function(e){var n=e.children;return t.createElement(t.Fragment,{},n)}},u=t.forwardRef((function(e,n){var r=e.components,a=e.mdxType,o=e.originalType,i=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),d=m(r),u=a,h=d["".concat(i,".").concat(u)]||d[u]||p[u]||o;return r?t.createElement(h,l(l({ref:n},c),{},{components:r})):t.createElement(h,l({ref:n},c))}));function h(e,n){var r=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var o=r.length,l=new Array(o);l[0]=u;var s={};for(var i in n)hasOwnProperty.call(n,i)&&(s[i]=n[i]);s.originalType=e,s[d]="string"==typeof e?e:a,l[1]=s;for(var m=2;m<o;m++)l[m]=r[m];return t.createElement.apply(null,l)}return t.createElement.apply(null,r)}u.displayName="MDXCreateElement"},3153:(e,n,r)=>{r.r(n),r.d(n,{assets:()=>i,contentTitle:()=>l,default:()=>p,frontMatter:()=>o,metadata:()=>s,toc:()=>m});var t=r(7462),a=(r(7294),r(3905));const o={},l="remove_handler",s={unversionedId:"api_reference/methods/remove_handler",id:"api_reference/methods/remove_handler",title:"remove_handler",description:"Remove a handler from the bot.",source:"@site/docs/api_reference/methods/remove_handler.md",sourceDirName:"api_reference/methods",slug:"/api_reference/methods/remove_handler",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/remove_handler",draft:!1,tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"list_restricted_users",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/list_restricted_users"},next:{title:"reply_message",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/reply_message"}},i={},m=[{value:"Signature",id:"signature",level:2},{value:"Parameters",id:"parameters",level:2},{value:"Example",id:"example",level:2}],c={toc:m},d="wrapper";function p(e){let{components:n,...r}=e;return(0,a.kt)(d,(0,t.Z)({},c,r,{components:n,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"remove_handler"},"remove_handler"),(0,a.kt)("p",null,"Remove a handler from the bot."),(0,a.kt)("h2",{id:"signature"},"Signature"),(0,a.kt)("p",null,(0,a.kt)("inlineCode",{parentName:"p"},"def remove_handler(self, handler: BaseHandler | List[BaseHandler]) -> BotApp")),(0,a.kt)("h2",{id:"parameters"},"Parameters"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"handler")," (",(0,a.kt)("inlineCode",{parentName:"li"},"BaseHandler | List[BaseHandler]"),"): The handler to remove from the bot, or a list of handlers to add to the bot (see ",(0,a.kt)("a",{parentName:"li",href:"../../fundamentals/handlers"},"Hanlders")," for more information on handlers)")),(0,a.kt)("h2",{id:"example"},"Example"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},'\n\nfrom swibots import BotApp, BotContext, CommandEvent, MessageEvent, CallbackQueryEvent, filters, InlineKeyboardButton, InlineMarkup, BotCommandInfo\n\nfrom swibots.bots.handlers import (\n    MessageHandler,\n    UnknownCommandHandler,\n    CallbackQueryHandler,\n    CommandHandler,\n)\n\n\nasync def echo(ctx: BotContext[CommandEvent]):\n    m = await ctx.bot.prepare_response_message(ctx.event.message)\n    text = ctx.event.params or "No args"\n    m.message = f"Your message: {text}"\n    await ctx.bot.send_message(m)\n\napp = BotApp()\n\n# register your handlers here\n\necho_handler = CommandHandler(\n    command="echo",\n    callback=echo,\n)\napp.add_handler(\n    echo_handler\n)\n\n# remove the handler\napp.remove_handler(\n    echo_handler\n)\n\n# now the handler won\'t be called when the user sends the /echo command\n\napp.run()\n\n')))}p.isMDXComponent=!0}}]);