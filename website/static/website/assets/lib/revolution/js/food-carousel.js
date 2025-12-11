var tpj=jQuery;						
			var revapi108;
			tpj(document).ready(function() {
				if(tpj("#rev_slider_108_1").revolution == undefined){
					revslider_showDoubleJqueryError("#rev_slider_108_1");
				}else{
					revapi108 = tpj("#rev_slider_108_1").show().revolution({
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
							arrows: {
								style:"metis",
								enable:true,
								hide_onmobile:true,
								hide_under:768,
								hide_onleave:false,
								tmp:'',
								left: {
									h_align:"left",
									v_align:"center",
									h_offset:0,
									v_offset:0
								},
								right: {
									h_align:"right",
									v_align:"center",
									h_offset:0,
									v_offset:0
								}
							}
							,
							thumbnails: {
								style:"erinyen",
								enable:true,
								width:150,
								height:100,
								min_width:150,
								wrapper_padding:20,
								wrapper_color:"#000000",
								wrapper_opacity:"0.05",
								tmp:'<span class="tp-thumb-over"></span><span class="tp-thumb-image"></span><span class="tp-thumb-title">{{title}}</span><span class="tp-thumb-more"></span>',
								visibleAmount:9,
								hide_onmobile:false,
								hide_onleave:false,
								direction:"horizontal",
								span:true,
								position:"outer-bottom",
								space:10,
								h_align:"center",
								v_align:"bottom",
								h_offset:0,
								v_offset:0
							}
						},
						carousel: {
							maxRotation: 65,
							vary_rotation: "on",
							minScale: 55,
							vary_scale: "off",
							horizontal_align: "center",
							vertical_align: "center",
							fadeout: "on",
							vary_fade: "on",
							maxVisibleItems: 5,
							infinity: "on",
							space: -150,
							stretch: "off"
						},
						gridwidth:600,
						gridheight:600,
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