"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[6763],{3905:(e,t,n)=>{n.d(t,{Zo:()=>d,kt:()=>h});var a=n(7294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function i(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var p=a.createContext({}),s=function(e){var t=a.useContext(p),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},d=function(e){var t=s(e.components);return a.createElement(p.Provider,{value:t},e.children)},c="mdxType",u={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,p=e.parentName,d=i(e,["components","mdxType","originalType","parentName"]),c=s(n),m=r,h=c["".concat(p,".").concat(m)]||c[m]||u[m]||o;return n?a.createElement(h,l(l({ref:t},d),{},{components:n})):a.createElement(h,l({ref:t},d))}));function h(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,l=new Array(o);l[0]=m;var i={};for(var p in t)hasOwnProperty.call(t,p)&&(i[p]=t[p]);i.originalType=e,i[c]="string"==typeof e?e:r,l[1]=i;for(var s=2;s<o;s++)l[s]=n[s];return a.createElement.apply(null,l)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},4539:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>p,contentTitle:()=>l,default:()=>u,frontMatter:()=>o,metadata:()=>i,toc:()=>s});var a=n(7462),r=(n(7294),n(3905));const o={sidebar_position:4},l="Decorator Handlers",i={unversionedId:"fundamentals/decorators",id:"fundamentals/decorators",title:"Decorator Handlers",description:"If you don't want to use the add_handler method, you can use decorators to register handlers to the app.",source:"@site/docs/fundamentals/decorators.md",sourceDirName:"fundamentals",slug:"/fundamentals/decorators",permalink:"/Switch-Bots-Python-Library/docs/fundamentals/decorators",draft:!1,tags:[],version:"current",sidebarPosition:4,frontMatter:{sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Handlers",permalink:"/Switch-Bots-Python-Library/docs/fundamentals/handlers"},next:{title:"Bot Context",permalink:"/Switch-Bots-Python-Library/docs/fundamentals/context"}},p={},s=[{value:"Decorators",id:"decorators",level:2},{value:"Example",id:"example",level:3}],d={toc:s},c="wrapper";function u(e){let{components:t,...n}=e;return(0,r.kt)(c,(0,a.Z)({},d,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"decorator-handlers"},"Decorator Handlers"),(0,r.kt)("p",null,"If you don't want to use the ",(0,r.kt)("inlineCode",{parentName:"p"},"add_handler")," method, you can use decorators to register handlers to the app."),(0,r.kt)("h2",{id:"decorators"},"Decorators"),(0,r.kt)("p",null,"There are one to one matching decorators for each of the existing ",(0,r.kt)("a",{parentName:"p",href:"./handlers"},(0,r.kt)("inlineCode",{parentName:"a"},"handlers"))," methods."),(0,r.kt)("p",null,"Let's say that you have defined your app as ",(0,r.kt)("inlineCode",{parentName:"p"},"app"),", then you can use the following decorators to register handlers (change the ",(0,r.kt)("inlineCode",{parentName:"p"},"app")," variable to whatever you have defined your app as):"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_message")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_callback_query")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_command")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_channel_created")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_channel_updated")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_channel_deleted")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_group_created")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_group_updated")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_group_deleted")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_community_updated")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_member_joined")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_member_left")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_user_banned")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_unknown_command")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"@app.on_inline_query"))),(0,r.kt)("p",null,"The decorators are functions that take a function as an argument and return a function. The function that is returned is the handler that is registered to the app as a callback."),(0,r.kt)("p",null,"All of the decorators take the same arguments as the corresponding handler method. For example, the ",(0,r.kt)("inlineCode",{parentName:"p"},"@app.on_message")," decorator takes the same arguments as the ",(0,r.kt)("inlineCode",{parentName:"p"},"app.add_handler(MessageHandler(...))")," method, with the exception of the ",(0,r.kt)("inlineCode",{parentName:"p"},"callback")," argument, which is the function that is decorated."),(0,r.kt)("h3",{id:"example"},"Example"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},'from swibots import BotApp, MessageHandler\n\napp = BotApp("token", "your bot description")\n\n@app.on_message()\nasync def message_handler(ctx: BotContext[MessageEvent]):\n   await m.reply_text(f"Thank you! I received your message: {ctx.event.message.message}")\n\napp.run()\n')))}u.isMDXComponent=!0}}]);