var tpj=jQuery;					
					var revapi16;
					tpj(document).ready(function() {
						if(tpj("#rev_slider_16_1").revolution == undefined){
							revslider_showDoubleJqueryError("#rev_slider_16_1");
						}else{
							revapi18 = tpj("#rev_slider_16_1").show().revolution({
								sliderType:"standard",
								jsFileLocation:"revolution/js/",
								sliderLayout:"auto",
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
									tabs: {
										style:"zeus",
										enable:true,
										width:100,
										height:30,
										min_width:100,
										wrapper_padding:0,
										wrapper_color:"transparent",
										wrapper_opacity:"0",
										tmp:'<span class="tp-tab-title">{{title}}</span>',
										visibleAmount: 3,
										hide_onmobile: true,
										hide_under:480,
										hide_onleave:false,
										hide_delay:200,
										direction:"horizontal",
										span:true,
										position:"inner",
										space:1,
										h_align:"left",
										v_align:"top",
										h_offset:30,
										v_offset:30
									}
								},
								viewPort: {
									enable:true,
									outof:"pause",
									visible_area:"80%"
								},
								responsiveLevels:[1240,1024,778,480],
								gridwidth:[1230,1024,767,480],
								gridheight:[650,650,480,360],
								lazyType:"none",
								parallax: {
									type:"scroll",
									origo:"enterpoint",
									speed:400,
									levels:[5,10,15,20,25,30,35,40,45,50],
								},
								shadow:0,
								spinner:"spinner1",
								stopLoop:"off",
								stopAfterLoops:-1,
								stopAtSlide:-1,
								shuffle:"off",
								autoHeight:"off",
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