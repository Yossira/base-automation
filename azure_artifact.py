from base_automation import base


if __name__ == "__main__":
    # feeds = ["base-automation", "automation-feed"]
    feeds = ["base-automation"]
    dist_dir = base.os.path.dirname(__file__) + "/dist"
    base.upload_artifact.run_process(dist_dir, feeds)
