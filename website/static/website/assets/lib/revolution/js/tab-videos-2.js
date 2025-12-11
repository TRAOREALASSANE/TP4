var tpj=jQuery;
			
			var revapi30;
			tpj(document).ready(function() {
				if(tpj("#rev_slider_30_1").revolution == undefined){
					revslider_showDoubleJqueryError("#rev_slider_30_1");
				}else{
					revapi30 = tpj("#rev_slider_30_1").show().revolution({
						sliderType:"carousel",
						jsFileLocation:"revolution/js/",
						sliderLayout:"fullwidth",
						dottedOverlay:"none",
						delay:9000,
						navigation: {
							keyboardNavigation:"off",
							keyboard_direction: "horizontal",
							mouseScrollNavigation:"off",
							onHoverStop:"off",
							touch:{
								touchenabled:"on",
								swipe_threshold: 75,
								swipe_min_touches: 1,
								swipe_direction: "horizontal",
								drag_block_vertical: false
							}
							,
							arrows: {
								style:"gyges",
								enable:true,
								hide_onmobile:false,
								hide_onleave:false,
								tmp:'',
								left: {
									h_align:"left",
									v_align:"center",
									h_offset:20,
									v_offset:0
								},
								right: {
									h_align:"right",
									v_align:"center",
									h_offset:20,
									v_offset:0
								}
							}
							,
							tabs: {
								style:"gyges",
								enable:true,
								width:250,
								height:80,
								min_width:250,
								wrapper_padding:30,
								wrapper_color:"#26292b",
								wrapper_opacity:"1",
								tmp:'<div class="tp-tab-content">  <span class="tp-tab-date">{{param1}}</span>  <span class="tp-tab-title">{{title}}</span></div><div class="tp-tab-image"></div>',
								visibleAmount: 5,
								hide_onmobile: false,
								hide_onleave:false,
								hide_delay:200,
								direction:"horizontal",
								span:true,
								position:"outer-bottom",
								space:0,
								h_align:"center",
								v_align:"bottom",
								h_offset:0,
								v_offset:0
							}
						},
						carousel: {
							horizontal_align: "center",
							vertical_align: "center",
							fadeout: "on",
							vary_fade: "on",
							maxVisibleItems: 3,
							infinity: "on",
							space: 0,
							stretch: "off"
						},
						gridwidth:720,
						gridheight:405,
						lazyType:"none",
						shadow:0,
						spinner:"spinner1",
						stopLoop:"on",
						stopAfterLoops:0,
						stopAtSlide:1,
						shuffle:"off",
						autoHeight:"off",
						disableProgressBar:"on",
						hideThumbsOnMobile:"off",
						hideSliderAtLimit:0,
						hideCaptionAtLimit:0,
						hideAllCaptionAtLilmit:0,
						debugMode:false,
						fallbacks: {
							simplifyAll:"off",
							nextSlideOnWindowFocus:"off",
							disableFocusListener:false,
						}
					});
				}
			});	/*ready*/