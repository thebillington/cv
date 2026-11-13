.PHONY: build pdf site check preview clean

build:
	.venv/bin/python scripts/build.py

pdf:
	.venv/bin/python scripts/build.py --pdf

site:
	.venv/bin/python scripts/build.py --website

check:
	.venv/bin/python scripts/check_pdf.py output/Billy-Rebecchi-CV.pdf

preview:
	.venv/bin/python scripts/preview.py output/Billy-Rebecchi-CV.pdf
	.venv/bin/python scripts/screenshot_site.py

clean:
	rm -rf output
