"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[9932],{3905:(e,t,r)=>{r.d(t,{Zo:()=>p,kt:()=>f});var n=r(7294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function o(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var l=n.createContext({}),d=function(e){var t=n.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):o(o({},t),e)),r},p=function(e){var t=d(e.components);return n.createElement(l.Provider,{value:t},e.children)},s="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,i=e.originalType,l=e.parentName,p=c(e,["components","mdxType","originalType","parentName"]),s=d(r),u=a,f=s["".concat(l,".").concat(u)]||s[u]||m[u]||i;return r?n.createElement(f,o(o({ref:t},p),{},{components:r})):n.createElement(f,o({ref:t},p))}));function f(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var i=r.length,o=new Array(i);o[0]=u;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c[s]="string"==typeof e?e:a,o[1]=c;for(var d=2;d<i;d++)o[d]=r[d];return n.createElement.apply(null,o)}return n.createElement.apply(null,r)}u.displayName="MDXCreateElement"},6915:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>o,default:()=>m,frontMatter:()=>i,metadata:()=>c,toc:()=>d});var n=r(7462),a=(r(7294),r(3905));const i={},o="delete_media",c={unversionedId:"api_reference/methods/delete_media",id:"api_reference/methods/delete_media",title:"delete_media",description:"Delete a Media by its ID.",source:"@site/docs/api_reference/methods/delete_media.md",sourceDirName:"api_reference/methods",slug:"/api_reference/methods/delete_media",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/delete_media",draft:!1,tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"deduct_xp",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/deduct_xp"},next:{title:"delete_message",permalink:"/Switch-Bots-Python-Library/docs/api_reference/methods/delete_message"}},l={},d=[{value:"Signature",id:"signature",level:2},{value:"Parameters",id:"parameters",level:2}],p={toc:d},s="wrapper";function m(e){let{components:t,...r}=e;return(0,a.kt)(s,(0,n.Z)({},p,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"delete_media"},"delete_media"),(0,a.kt)("p",null,"Delete a ",(0,a.kt)("a",{parentName:"p",href:"/Switch-Bots-Python-Library/docs/api_reference/types/media"},"Media")," by its ID."),(0,a.kt)("h2",{id:"signature"},"Signature"),(0,a.kt)("p",null,(0,a.kt)("inlineCode",{parentName:"p"},"async def delete_media(media_id: str)")),(0,a.kt)("h2",{id:"parameters"},"Parameters"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"media_id")," (",(0,a.kt)("inlineCode",{parentName:"li"},"str"),"): The ID of the media.")))}m.isMDXComponent=!0}}]);