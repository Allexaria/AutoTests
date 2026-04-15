import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from qa_project.framework.core.config import Config


class APIClient:
    def __init__(self, base_url=None, timeout=None):
        self.base_url = (base_url or Config.API_BASE_URL).rstrip("/")
        self.timeout = timeout or Config.DEFAULT_TIMEOUT
        self.session = requests.Session()

        retry = Retry(
            total=3,
            backoff_factor=0.3,
            status_forcelist=[500, 502, 503],
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
        )

        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.get(self._url(path), **kwargs)

    def post(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.post(self._url(path), **kwargs)

    def put(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.put(self._url(path), **kwargs)

    def delete(self, path, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.delete(self._url(path), **kwargs)
