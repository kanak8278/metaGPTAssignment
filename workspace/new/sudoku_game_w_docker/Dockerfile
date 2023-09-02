FROM python:3.9.5-slim-buster
WORKDIR /app
COPY sudoku_game /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]