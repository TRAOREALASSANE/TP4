var tpj=jQuery;					
					var revapi6;
					tpj(document).ready(function() {
						if(tpj("#rev_slider_6_1").revolution == undefined){
							revslider_showDoubleJqueryError("#rev_slider_6_1");
						}else{
							revapi6 = tpj("#rev_slider_6_1").show().revolution({
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
									bullets: {
										enable:true,
										hide_onmobile:false,
										style:"hermes",
										hide_onleave:false,
										direction:"vertical",
										h_align:"right",
										v_align:"center",
										h_offset:30,
										v_offset:0,
										space:10,
										tmp:''
									}
									,
									thumbnails: {
										style:"gyges",
										enable:true,
										width:60,
										height:60,
										min_width:60,
										wrapper_padding:0,
										wrapper_color:"#000000",
										wrapper_opacity:"0",
										tmp:'<span class="tp-thumb-img-wrap">  <span class="tp-thumb-image"></span></span>',
										visibleAmount:10,
										hide_onmobile:false,
										hide_onleave:false,
										direction:"horizontal",
										span:false,
										position:"inner",
										space:10,
										h_align:"left",
										v_align:"bottom",
										h_offset:30,
										v_offset:30
									}
								},
								responsiveLevels:[1240,1024,778,480],
								gridwidth:[1024,850,778,480],
								gridheight:[500,400,450,400],
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