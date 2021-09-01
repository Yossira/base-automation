import os

from base_automation import upload_artifact

if __name__ == "__main__":
    # feeds = ["base-automation", "automation-feed"]
    azure_feeds = ["base-automation"]
    dist_dir = os.path.dirname(__file__) + "/dist"
    upload_artifact.run_process(dist_dir=dist_dir, azure_feeds=azure_feeds, azure_artifact=False,
                                pypi_artifact=True)
