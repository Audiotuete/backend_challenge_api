webpackJsonp([1],{"/ktH":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement;return(t._self._c||e)("div",[t._t("default")],2)},s=[],o={render:a,staticRenderFns:s};e.a=o},"3GSc":function(t,e){},"DP/h":function(t,e,n){"use strict";n.d(e,"a",function(){return o});var a=n("Ju5A"),s=n("r3Od"),o=[{path:"/",components:{default:a.a,navbar:s.a}}]},EErM:function(t,e,n){"use strict";function a(t){n("srfA")}var s=n("iF1o"),o=n("/ktH"),i=n("VU/8"),r=a,c=i(s.a,o.a,!1,r,null,null);e.a=c.exports},Ju5A:function(t,e,n){"use strict";function a(t){n("KLI4")}var s=n("fkdt"),o=n("kx48"),i=n("VU/8"),r=a,c=i(s.a,o.a,!1,r,"data-v-3eaa2d22",null);e.a=c.exports},KLI4:function(t,e){},KVUS:function(t,e){},M93x:function(t,e,n){"use strict";function a(t){n("3GSc")}var s=n("xJD8"),o=n("YxyP"),i=n("VU/8"),r=a,c=i(s.a,o.a,!1,r,null,null);e.a=c.exports},NHnr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("7+uW"),s=n("/ocq"),o=n("H5Ot"),i=n.n(o),r=n("M93x"),c=n("DP/h");a.a.use(s.a),a.a.use(i.a);var u=new s.a({routes:c.a});new a.a({el:"#app",router:u,template:"<App/>",components:{App:r.a}})},YxyP:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"},on:{click:function(e){t.enterFullscreen()}}},[n("router-view",{attrs:{name:"navbar"}}),t._v(" "),n("router-view"),t._v(" "),n("router-view",{attrs:{name:"impressum"}})],1)},s=[],o={render:a,staticRenderFns:s};e.a=o},eeJE:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"navbar"},[n("div",{staticClass:"menu-container"},[n("router-link",{attrs:{to:"/"}},[n("i",{staticClass:"fa fa-cog"})]),t._v(" "),n("router-link",{attrs:{to:"/"}},[n("i",{staticClass:"fa fa-stack-exchange"})]),t._v(" "),n("router-link",{attrs:{to:"/"}},[n("i",{staticClass:"fa fa-book"})])],1)])},s=[],o={render:a,staticRenderFns:s};e.a=o},fkdt:function(t,e,n){"use strict";var a=n("Xxa5"),s=n.n(a),o=n("exGp"),i=n.n(o),r=n("EErM");e.a={name:"swiper-screen",components:{VueSwing:r.a},data:function(){return{cards:["A"],none:"none",answerValues:{NO:0,YES:1,NOTE:2},isPlaying:!1,showNotepad:!1,inputIsFocused:!1,playerVars:{listType:"playlist",list:"PLglaqunAuU1jKrln443Vi2xkwX_Oimg_G",autoplay:0,rel:0,showinfo:0,showsearch:0,controls:0,modestbranding:0,cc_load_policy:1}}},computed:{config:function(){return{allowedDirections:[r.a.Direction.RIGHT,r.a.Direction.LEFT],minThrowOutDistance:1e3,maxThrowOutDistance:5e3,throwOutConfidence:function(t,e,n){var a=Math.min(Math.abs(t)/n.offsetWidth*1.5,1),s=Math.min(Math.abs(e)/n.offsetHeight*2.5,1);return Math.max(a,s)}}}},methods:{vote:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:-1;this.saveCardAnswer(t,null),this.isPlaying=!1},goToNotepad:function(){this.$refs.youtube[0].player.pauseVideo(),this.showNotepad=!0},makeNote:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:-1,e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null;this.saveCardAnswer(t,e)},requestNewCard:function(){this.showNotepad=!1,this.inputIsFocused=!1,this.cards.push(Math.random())},saveCardAnswer:function(t,e){console.log(t,e),this.cards.shift(),this.requestNewCard()},playVideoIndex:function(t){var e=this;return i()(s.a.mark(function n(){var a;return s.a.wrap(function(n){for(;;)switch(n.prev=n.next){case 0:return a=e.$refs.youtube[0].player,n.next=3,a.getPlayerState();case 3:if(n.t0=n.sent,2!=n.t0){n.next=9;break}console.log("playing paused video"),a.playVideo(),n.next=10;break;case 9:a.playVideoAt(t);case 10:case"end":return n.stop()}},n,e)}))()},replayVideo:function(){var t=this.$refs.youtube[0].player;t.stopVideo(),t.playVideo()},playing:function(){this.isPlaying=!0}}}},iF1o:function(t,e,n){"use strict";var a=n("BO1k"),s=n.n(a),o=n("Gu7T"),i=n.n(o),r=n("J0ux");e.a={name:"vue-swing",props:["config"],data:function(){return{stack:null,cards:[],observer:null}},mounted:function(){var t=this;this.stack=r.Stack(this.config||{}),[].concat(i()(this.$el.children)).forEach(function(e){t.cards.push(t.stack.createCard(e))}),this.observer=new MutationObserver(function(e){var n=[],a=[];e.forEach(function(t){var e=t.addedNodes,s=t.removedNodes;n.push.apply(n,i()(e)),a.push.apply(a,i()(s))}),n.forEach(function(e){var n=a.indexOf(e);if(-1!==n)return void a.splice(n,1);null==t.stack.getCard(e)&&t.cards.push(t.stack.createCard(e))}),a.forEach(function(e){var n=t.stack.getCard(e);null!=n&&(t.cards.splice(t.cards.indexOf(n),1),t.stack.destroyCard(n))})}),this.observer.observe(this.$el,{childList:!0});var e=["throwout","throwoutend","throwoutdown","throwoutleft","throwoutright","throwoutup","throwin","throwinend","dragstart","dragmove","dragend","destroyCard"],n=!0,a=!1,o=void 0;try{for(var c,u=s()(e);!(n=(c=u.next()).done);n=!0){var l=c.value;!function(e){t.stack.on(e,function(n){t.$emit(e,n)})}(l)}}catch(t){a=!0,o=t}finally{try{!n&&u.return&&u.return()}finally{if(a)throw o}}},beforeDestroy:function(){this.observer.disconnect()},Card:r.Card,Direction:r.Direction,Stack:r.Stack}},kx48:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("vue-swing",{ref:"vueswing",staticClass:"swing-wrapper",attrs:{config:t.config},on:{throwoutleft:function(e){t.vote(t.answerValues.NO)},throwoutup:!0,throwoutright:function(e){t.vote(t.answerValues.YES)}}},[n("div",{staticClass:"card card-not-dragable"}),t._v(" "),t._l(t.cards,function(e){return n("div",{key:e,ref:"card",refInFor:!0,class:{card:!0,"card-not-dragable":t.showNotepad}},[n("div",{directives:[{name:"show",rawName:"v-show",value:!t.showNotepad,expression:"!showNotepad"}],staticClass:"question-container"},[n("youtube",{ref:"youtube",refInFor:!0,attrs:{id:"youtube-player","video-id":"","player-vars":t.playerVars},on:{playing:t.playing,paused:function(e){t.isPlaying=!t.isPlaying}}}),t._v(" "),n("button",{directives:[{name:"show",rawName:"v-show",value:!t.isPlaying,expression:"!isPlaying"}],staticClass:"button-play",on:{click:function(e){t.playVideoIndex(2)}}},[n("i",{staticClass:"fa fa-play"})]),t._v(" "),n("button",{staticClass:"button-replay",staticStyle:{marigin:"20px"},on:{click:function(e){t.replayVideo()}}},[n("i",{staticClass:"fa fa-undo"})])],1),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:t.showNotepad,expression:"showNotepad"}],staticClass:"note-container"},[n("div",{directives:[{name:"show",rawName:"v-show",value:!t.inputIsFocused,expression:"!inputIsFocused"}],staticClass:"note-header"},[n("button",{staticClass:"note-header-icon",on:{click:function(e){t.showNotepad=!1}}},[n("i",{staticClass:"sl-icon icon-arrow-left"})]),t._v("Anmerkungen zu:")]),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:!t.inputIsFocused,expression:"!inputIsFocused"}],staticClass:"note-question"},[t._v("Sollten in der Kantine vegetarische Speisen angeboten werden?")]),t._v(" "),n("textarea",{staticClass:"note-input",attrs:{maxlength:"250"},on:{focus:function(e){t.inputIsFocused=!0}}}),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:t.inputIsFocused,expression:"inputIsFocused"}],staticClass:"note-show-question",on:{click:function(e){t.inputIsFocused=!1}}},[n("i",{staticClass:"sl-icon icon-arrow-up note-show-question-icon"})]),t._v(" "),n("button",{staticClass:"note-button-send",on:{click:function(e){t.makeNote(t.answerValues.NOTE)}}},[t._v("Absenden")])])])})],2),t._v(" "),n("div",{directives:[{name:"show",rawName:"v-show",value:!t.showNotepad,expression:"!showNotepad"}],staticClass:"choicebar"},[n("div",{staticClass:"choice-container"},[n("button",{staticClass:"choice-button",attrs:{href:"#"},on:{click:function(e){t.vote(t.answerValues.NO)}}},[n("i",{staticClass:"sl-icon icon-close"})]),t._v(" "),n("button",{directives:[{name:"show",rawName:"v-show",value:!t.showNotepad,expression:"!showNotepad"}],staticClass:"choice-button",attrs:{href:"#"},on:{click:function(e){t.goToNotepad()}}},[n("i",{staticClass:"sl-icon icon-note"})]),t._v(" "),n("button",{staticClass:"choice-button",attrs:{href:"#"},on:{click:function(e){t.vote(t.answerValues.YES)}}},[n("i",{staticClass:"sl-icon icon-check"})])])])],1)},s=[],o={render:a,staticRenderFns:s};e.a=o},r3Od:function(t,e,n){"use strict";function a(t){n("KVUS")}var s=n("zHtI"),o=n("eeJE"),i=n("VU/8"),r=a,c=i(s.a,o.a,!1,r,null,null);e.a=c.exports},srfA:function(t,e){},xJD8:function(t,e,n){"use strict";var a=n("I95x"),s=n.n(a);e.a={name:"app",components:{},data:function(){return{}},methods:{enterFullscreen:function(){s.a.enabled&&0==s.a.isFullscreen&&s.a.request()}}}},zHtI:function(t,e,n){"use strict";var a=n("I95x");n.n(a);e.a={data:function(){return{}},methods:{}}}},["NHnr"]);
//# sourceMappingURL=app.8d99c2f2f0028a0cb519.js.map