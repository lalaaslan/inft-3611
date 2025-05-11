provider "google" {
  project = "inft-3611"
  region = "me-central1"
}

resource "google_cloud_run_v2_service" "default" {
  name     = "lala-aslan"
  location = "me-central1"
  ingress = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "me-central1-docker.pkg.dev/inft-3611/unreliable-banking-image/unreliable-bank:lala-aslan-v2"
      ports {
        container_port = 8080
      }
    }
  }
}

data "google_iam_policy" "public" {
  binding {
    role = "roles/run.invoker"
    members = ["allUsers"]
  }
}
