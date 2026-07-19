.PHONY: doctor start test

doctor:
	python scripts/doctor.py

start:
	python scripts/session_start.py

test:
	python -m unittest discover -s tests -p 'test_*.py'
