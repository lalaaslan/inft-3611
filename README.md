## Task 1

httpServer_crash.go represents HTTP server that simultes an unreliable banking service.

Algorithm uses a probabilistic model to simulate failure scenrios based on random number generation:

1. **Core Dump (0.5% chance)**

Crashes the server, request restart.

2. **Internal Server error (19.5% chance)**

HTTP 500 Error

3. **Database Connection (30% chance)**

Send `error.html` file, simulate database unavailability

4. **Latency Issues (20% chance)**

Make server progressively slower

5. **Successful Responce (30% chance)**

Nomal response `index.html`

## Tsak 2
I am using gcloud, so I configure Docker authentication for Artifact Registry by `gcloud auth configure-docker me-central1-docker.pkg.dev`

The tag should has the following stucture: `HOSTNAME/PROJECT_ID/REPOSITORY/IMGE:TAG`

1. Install Docker and navigate to the repo directory in Terminal.

2. Run `docker build -t me-central1-docker.pkg.dev/inft-3611/unreliable-banking-image/unreliable-bank:lala-aslan .` to crete Docker image.

3. Push created image by using command `docker push me-central1-docker.pkg.dev/inft-3611/unreliable-banking-image/unreliable-bank:lala-aslan`.

4. The image was successfuly uploded to Artifact Registry. 

The final imge's digets are `sha256:8135324ba47fa65af809648edf864046fafb364af26f2c1b99ced0778f2afe59`.

Image path is `me-central1-docker.pkg.dev/inft-3611/unreliable-banking-image/unreliable-bank:lala-aslan`