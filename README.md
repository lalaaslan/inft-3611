## Task 1

httpServer_crash.go represents HTTP server that simultes an unreliable banking service.

Algorithm uses a probabilistic model to simulate failure scenarios based on random number generation:

1. **Core Dump (0.5% chance)**

Crashes the server, request restart.

2. **Internal Server error (19.5% chance)**

HTTP 500 Error

3. **Database Connection (30% chance)**

Send `error.html` file, simulate database unavailability

4. **Latency Issues (20% chance)**

Make server progressively slower

5. **Successful Response (30% chance)**

Normal response `index.html`

## Task 2
I am using gcloud, so I configure Docker authentication for Artifact Registry by `gcloud auth configure-docker me-central1-docker.pkg.dev`.

The tag should has the following stucture: `HOSTNAME/PROJECT_ID/REPOSITORY/IMGE:TAG`.


Steps of creatig image & pushing one:

1. Install Docker and navigate to the repo directory in Terminal.

2. Run `docker build -t me-central1-docker.pkg.dev/inft-3611/unreliable-banking-image/unreliable-bank:lala-aslan-v2 .` to crete Docker image.

3. Push created image by using command `docker push me-central1-docker.pkg.dev/inft-3611/unreliable-banking-image/unreliable-bank:lala-aslan-v2`.

4. The image was successfuly uploded to Artifact Registry. 

The final image's digets are `sha256:116116b5bb44d1dc362cb345b15153d98e0cf36caaa15fa7b076f0d03508d858`.

Image path is `me-central1-docker.pkg.dev/inft-3611/unreliable-banking-image/unreliable-bank:lala-aslan-v2`.

## Task 3

In this task I created Terraform file and define it.

The service name is `lala-aslan` and location is `me-central1`.

I used `ingress = "INGRESS_TRAFFIC_ALL"` to allow direct access to service from the internet.

In container part I defined image which was created in Task 2 and port 8080 for matching with port in Go-file.

I also add `google_iam_policy` where I defined `roles/run.invoker` to `AllUsers` to make Cloud Function working without authentication.

I ran commands `terraform init` and `terraform apply` for creating defined service in Google Cloud.

## Task 5

The Simple Client runs endpoint `/getbalance`. I selected test count by 100 and used sleep betwwen them by 1 second to simulate steady usage. In each test code print result: success or faild.

By this we also may test our SLO systems and validate their compliance, and observe behavior of service.

## Video URL

[Assignment Video](https://youtu.be/rQSlPorgMOg)