# Load-Balanced-URL-Shortener
Project done as a part of the course Cloud Computing (UE22CS351B) at PES University 


This project implements a URL shortener service designed with scalability, containerization, and cloud-native architecture in mind. It allows users to submit long URLs via an API and receive a shortened version, which can then be used to redirect to the original URL. The system is deployed using Docker and Kubernetes, with multiple instances running behind a load balancer with a benefit of supporting fault tolerance and horizontal scaling through Kubernetes features like replicas and autoscaling.

The system is composed of the following components:

# 1.URL Shortener API Service
A simple web API to:

Accept long URLs and return shortened ones (POST /shorten)

Redirect short URLs to the original address (GET /<short_code>)

# 2. In-Memory Store

Stores mappings between short codes and long URLs using a Redis instance running in a separate Kubernetes pod

# 3. Docker Containers
Both the API service and Redis are containerized using Docker and managed independently.

# 4. Kubernetes Deployment
Multiple replicas of the API service run as pods, connected via Kubernetes Services. Redis is deployed as a separate pod and accessed internally via ClusterIP.

# 5. Load Balancing and Autoscaling
Traffic is routed to different service instances through a Kubernetes LoadBalancer or Ingress. Horizontal Pod Autoscaler (HPA) scales instances based on CPU usage.


