# Big Data Lab 7 Template

This project sets up a data pipeline using Docker Compose with Elasticsearch, Kibana, Logstash, and a YouTube data processor.

## Prerequisites

- Docker and Docker Compose installed
- AWS account with S3 access

## Setup

1. Copy `.env.example` to `.env` and fill in your actual values:
   - `STACK_VERSION`: Elastic Stack version (default: 9.2.1)
   - `AWS_ACCESS_KEY_ID`: Your AWS access key
   - `AWS_SECRET_ACCESS_KEY`: Your AWS secret key

2. Copy `aws-credentials.txt.example` to `aws-credentials.txt` and update with your AWS credentials.

3. Run the services:
   ```bash
   docker compose up -d
   ```

## Services

- **Elasticsearch**: Search and analytics engine at http://localhost:9200
- **Kibana**: Visualization dashboard at http://localhost:5601
- **Logstash**: Data processing pipeline that reads from S3
- **YouTube Processor**: Python script that processes YouTube data

## Configuration

- Logstash pipeline: `logstash/pipeline.conf`
- Docker Compose: `compose.yml`
- Environment variables: `.env`

## Stopping the Services

```bash
docker compose down
```

## Notes

- The project uses Elastic Stack version 9.2.1
- Data is stored in Docker volumes
- Ensure your S3 bucket and credentials are correctly configured