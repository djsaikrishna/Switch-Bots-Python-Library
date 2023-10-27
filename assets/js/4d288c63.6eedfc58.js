"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[3713],{3905:(e,t,r)=>{r.d(t,{Zo:()=>l,kt:()=>f});var n=r(7294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var m=n.createContext({}),u=function(e){var t=n.useContext(m),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},l=function(e){var t=u(e.components);return n.createElement(m.Provider,{value:t},e.children)},p="mdxType",s={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},y=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,i=e.originalType,m=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),p=u(r),y=o,f=p["".concat(m,".").concat(y)]||p[y]||s[y]||i;return r?n.createElement(f,a(a({ref:t},l),{},{components:r})):n.createElement(f,a({ref:t},l))}));function f(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=r.length,a=new Array(i);a[0]=y;var c={};for(var m in t)hasOwnProperty.call(t,m)&&(c[m]=t[m]);c.originalType=e,c[p]="string"==typeof e?e:o,a[1]=c;for(var u=2;u<i;u++)a[u]=r[u];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}y.displayName="MDXCreateElement"},634:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>m,contentTitle:()=>a,default:()=>s,frontMatter:()=>i,metadata:()=>c,toc:()=>u});var n=r(7462),o=(r(7294),r(3905));const i={},a="get_community",c={unversionedId:"api_reference/methods/get_community",id:"api_reference/methods/get_community",title:"get_community",description:"Gets a Community by its ID.",source:"@site/docs/api_reference/methods/get_community.md",sourceDirName:"api_reference/methods",slug:"/api_reference/methods/get_community",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/get_community",draft:!1,tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"get_channel_chat_history",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/get_channel_chat_history"},next:{title:"get_community_member",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/get_community_member"}},m={},u=[{value:"Signature",id:"signature",level:2},{value:"Parameters",id:"parameters",level:2}],l={toc:u},p="wrapper";function s(e){let{components:t,...r}=e;return(0,o.kt)(p,(0,n.Z)({},l,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"get_community"},"get_community"),(0,o.kt)("p",null,"Gets a ",(0,o.kt)("a",{parentName:"p",href:"../types/community"},"Community")," by its ID."),(0,o.kt)("h2",{id:"signature"},"Signature"),(0,o.kt)("p",null,(0,o.kt)("inlineCode",{parentName:"p"},"async def get_community(community_id: str) -> Community")),(0,o.kt)("h2",{id:"parameters"},"Parameters"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("inlineCode",{parentName:"li"},"community_id")," (",(0,o.kt)("inlineCode",{parentName:"li"},"str"),"): The ID of the community")))}s.isMDXComponent=!0}}]);