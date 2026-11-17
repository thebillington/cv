.PHONY: build pdf site check preview og og-check clean

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

og:
	.venv/bin/python og/render.py

og-check:
	.venv/bin/python og/render.py --check

clean:
	rm -rf output
