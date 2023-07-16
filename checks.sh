echo "----------- Running checks -----------"

echo "----------- Running black --check ."
black --check .

echo "----------- Running mypy --strict ."
mypy --strict .

echo "----------- Running flake8 ."
flake8p .

echo "----------- Running pytest tests/unit"
pytest tests/unit

echo "----------- Running pytest tests/integration"
pytest tests/integration

echo "----------- Running pytest tests/e2e"
pytest tests/e2e

echo "----------- End checks -----------"
