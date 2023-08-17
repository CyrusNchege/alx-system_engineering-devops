# Task: Web Server Debugging

## Introduction
In this web stack debugging task, we are testing the performance of our NGINX web server setup under pressure. It appears that our server is experiencing a significant number of failed requests.

For benchmarking, we are using ApacheBench, a popular tool in the industry. ApacheBench allows us to simulate HTTP requests to the web server. In this case, we are making 2000 requests to the server with 100 requests being processed concurrently. Our goal is to eliminate the failed requests and improve the performance of our stack.

## Initial Benchmarking Results
