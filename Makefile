PLUGINS = plugin.video.ctuplinkrss\
	  plugin.video.ctuplink\
	  plugin.audio.ctuplinkaudio\
	  plugin.audio.ctuplinkaudio_basic\
	  plugin.video.heiseonline\
	  plugin.video.heiseshow
ZIPS = $(addsuffix .zip,$(PLUGINS))

ALL: $(ZIPS)
$(ZIPS) : %.zip : | %
	zip $@ $*/*.*

