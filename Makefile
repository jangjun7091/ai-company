# Optional convenience targets. Requires GNU Make; on Windows just run the
# python commands directly (see README).
.PHONY: doctor start test

doctor:
	python scripts/doctor.py

start:
	python scripts/session_start.py --json

test:
	python -m unittest discover -s tests -p 'test_*.py'
