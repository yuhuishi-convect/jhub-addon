import sh
import yaml

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
    def test_jupyterhub_addon(self):
        microk8s_enable("jupyterhub")
        wait_for_pod_state("", "jhub", "running", label="app=jupyterhub,component=hub")
        status = yaml.safe_load(sh.microk8s.status(format="yaml").stdout)
        expected = {"jupyterhub": "enabled"}
        microk8s_disable("jupyterhub")
