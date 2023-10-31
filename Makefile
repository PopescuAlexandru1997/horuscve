include makefile.pkg

clean:
	for i in $(OUTPUT_FILES); do \
		if [ -f $$i ] ; \
		then \
			rm $$i ; \
		fi; \
		done

horuscve:
	$(PYTHON_ENV_VAR) horuscve.py $(LOGGING) $(START_DATE) $(END_DATE) $(FINAL_PACKAGES_DIRS)

mydebug:
	$(info DATE:                  $(shell date +"%FT%H:%M:%S") )
	$(info EXAMPLE:               $(wildcard example/*/*/) )
	$(info START DATE:            $(START_DATE))
	$(info END DATE:              $(END_DATE))
	$(info LOGGING:               $(LOGGING))
	$(info PACKAGES_DIRS:         $(PACKAGES_DIRS))
	$(info EXCLUDE_PACKAGES_DIRS: $(EXCLUDE_PACKAGES_DIRS))
	$(info FINAL_PACKAGES_DIRS:   $(FINAL_PACKAGES_DIRS))