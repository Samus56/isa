FROM python

WORKDIR home/isa

COPY dist/isa-0.0.1-py3-none-any.whl .

RUN ["python", "-m", "pip", "install", "isa-0.0.1-py3-none-any.whl"]

ENTRYPOINT ["isa"]
