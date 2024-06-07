FROM python:3.9-slim
WORKDIR /HDBC
COPY requirements.txt .
RUN python -m venv venv && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["sh", "-c", ". venv/bin/activate && streamlit run hdbc_streamlit.py --server.port 8080"]