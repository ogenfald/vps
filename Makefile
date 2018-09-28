DESTDIR = /usr/bin

.DEFAULT_GOAL := help

help:
	@echo "Makefile Usage"
	@echo ""
	@echo "install			Install to $(DESTDIR)/vps"

install:
	@echo "Installing vps to $(DESTDIR)/vps"
	@cp $$(pwd)/vps.py $(DESTDIR)/vps
	@chmod +x $(DESTDIR)/vps
