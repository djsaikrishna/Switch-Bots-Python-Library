"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[9679],{3905:(e,t,r)=>{r.d(t,{Zo:()=>m,kt:()=>y});var n=r(7294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function s(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?s(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function o(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},s=Object.keys(e);for(n=0;n<s.length;n++)r=s[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(n=0;n<s.length;n++)r=s[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var p=n.createContext({}),l=function(e){var t=n.useContext(p),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},m=function(e){var t=l(e.components);return n.createElement(p.Provider,{value:t},e.children)},c="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,s=e.originalType,p=e.parentName,m=o(e,["components","mdxType","originalType","parentName"]),c=l(r),u=a,y=c["".concat(p,".").concat(u)]||c[u]||d[u]||s;return r?n.createElement(y,i(i({ref:t},m),{},{components:r})):n.createElement(y,i({ref:t},m))}));function y(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var s=r.length,i=new Array(s);i[0]=u;var o={};for(var p in t)hasOwnProperty.call(t,p)&&(o[p]=t[p]);o.originalType=e,o[c]="string"==typeof e?e:a,i[1]=o;for(var l=2;l<s;l++)i[l]=r[l];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}u.displayName="MDXCreateElement"},5061:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>p,contentTitle:()=>i,default:()=>d,frontMatter:()=>s,metadata:()=>o,toc:()=>l});var n=r(7462),a=(r(7294),r(3905));const s={},i="reply_message",o={unversionedId:"api_reference/methods/reply_message",id:"api_reference/methods/reply_message",title:"reply_message",description:"Replies to a message.",source:"@site/docs/api_reference/methods/reply_message.md",sourceDirName:"api_reference/methods",slug:"/api_reference/methods/reply_message",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/reply_message",draft:!1,tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"remove_handler",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/remove_handler"},next:{title:"reply_message_text",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/reply_message_text"}},p={},l=[{value:"Signature",id:"signature",level:2},{value:"Parameters",id:"parameters",level:2}],m={toc:l},c="wrapper";function d(e){let{components:t,...r}=e;return(0,a.kt)(c,(0,n.Z)({},m,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"reply_message"},"reply_message"),(0,a.kt)("p",null,"Replies to a message."),(0,a.kt)("h2",{id:"signature"},"Signature"),(0,a.kt)("p",null,(0,a.kt)("inlineCode",{parentName:"p"},"async def reply_message_text(message: int | Message, reply: Message, embed_message:media: EmbeddedMedia = None) -> Message:")),(0,a.kt)("h2",{id:"parameters"},"Parameters"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"message")," (int | ",(0,a.kt)("a",{parentName:"li",href:"../types/message"},"Message"),"): The ID of the message to reply to or the message itself"),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"reply")," (",(0,a.kt)("a",{parentName:"li",href:"../types/message"},"Message"),"): The message to reply with"),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"inline_markup")," (",(0,a.kt)("a",{parentName:"li",href:"../types/inline_markup"},"InlineMarkup"),"): The inline markup of the message"),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"embedded_message")," (",(0,a.kt)("a",{parentName:"li",href:"/Switch-Bots-Python-Library/docs/api_reference/types/embedded_media"},"EmbeddedMedia"),"): The media to send with the message")),(0,a.kt)("admonition",{type:"tip"},(0,a.kt)("p",{parentName:"admonition"},"This method does the same thing as the ",(0,a.kt)("inlineCode",{parentName:"p"},"reply")," method of the ",(0,a.kt)("a",{parentName:"p",href:"../types/message"},"Message")," class.")))}d.isMDXComponent=!0}}]);