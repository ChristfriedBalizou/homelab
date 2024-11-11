import os
import requests

secret_domain = os.environ.get("SECRET_DOMAIN")

# All my external domain are protected with authelia
# this should be enough for authelia to authenticate
# this job.
apikey = os.environ.get("KROMGO_AUTHELIA_APIKEY")


def build_kromgo_url(tag: str, base_url: str = secret_domain):
    return f"https://kromgo.{secret_domain}/{tag}?format=badge&apikey={apikey}"


def download_svg(tag: str):
    response = requests.get(build_kromgo_url(tag))
    response.raise_for_status()

    with open(f"./kromgo/{tag}.sgv", "wb") as file_descriptor:
        for chunk in response:
            file_descriptor.write(chunk)


if __name__ == "__main__":

    for tag in [
        "cluster_age_days",
        "cluster_node_count",
        "cluster_pod_count",
        "cluster_cpu_usage",
        "cluster_memory_usage",
    ]:
        try:
            download_svg(tag)
        except:
            # fail in silent
            pass