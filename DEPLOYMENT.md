# Deployment Guide

## Google Cloud Run (Recommended)

1. Set up Google Cloud SDK and authenticate:
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

2. Create Artifact Registry repository:
   ```bash
   gcloud artifacts repositories create tutor-repo \
     --repository-format=docker \
     --location=me-central1
   ```

3. Build and push the image:
   ```bash
   # Build the image
   docker build -t me-central1-docker.pkg.dev/YOUR_PROJECT_ID/tutor-repo/assessment:v1 .
   
   # Push to Artifact Registry
   docker push me-central1-docker.pkg.dev/YOUR_PROJECT_ID/tutor-repo/assessment:v1
   ```

4. Deploy to Cloud Run:
   ```bash
   gcloud run deploy assessment \
     --image me-central1-docker.pkg.dev/YOUR_PROJECT_ID/tutor-repo/assessment:v1 \
     --platform managed \
     --region me-central1 \
     --allow-unauthenticated
   ```

## Kubernetes

1. Build and push the image to your container registry.

2. Create a deployment:
   ```yaml
   # deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: assessment
   spec:
     replicas: 2
     selector:
       matchLabels:
         app: assessment
     template:
       metadata:
         labels:
           app: assessment
       spec:
         containers:
         - name: assessment
           image: your-registry/assessment:v1
           ports:
           - containerPort: 8000
           resources:
             requests:
               memory: "64Mi"
               cpu: "100m"
             limits:
               memory: "128Mi"
               cpu: "200m"
   ```

3. Create a service:
   ```yaml
   # service.yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: assessment
   spec:
     selector:
       app: assessment
     ports:
     - port: 80
       targetPort: 8000
     type: ClusterIP
   ```

4. Apply the configurations:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

## Docker Compose (Development)

For local development with the full stack, use the root project's docker-compose.yaml.

## Environment Variables

No environment variables are required for basic operation.

## Health Checks

The service exposes a health check endpoint at `/health` that returns:
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

Use this endpoint for container orchestration health checks. 