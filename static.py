from typing import Dict, List


CLOUD_REGIONS: Dict[str, Dict[str, List[str]]] = {
    "AT": {"AWS": [], "Azure": ["Austria East"], "GCP": []},
    "BE": {"AWS": [], "Azure": [], "GCP": ["europe-west1"]},
    "CH": {"AWS": [], "Azure": ["Switzerland North"], "GCP": ["europe-west6"]},
    "DE": {
        "AWS": ["eu-central-1"],
        "Azure": ["Germany West Central"],
        "GCP": ["europe-west3"],
    },
    "DK": {"AWS": [], "Azure": ["Denmark East"], "GCP": []},
    "ES": {"AWS": [], "Azure": ["Spain Central"], "GCP": []},
    "FI": {"AWS": [], "Azure": [], "GCP": ["europe-north1"]},
    "FR": {"AWS": ["eu-west-3"], "Azure": ["France Central"], "GCP": []},
    "GR": {"AWS": [], "Azure": ["Greece Central"], "GCP": []},
    "IE": {"AWS": ["eu-west-1"], "Azure": ["North Europe"], "GCP": []},
    "IT": {"AWS": ["eu-south-1"], "Azure": ["Italy North"], "GCP": []},
    "NL": {"AWS": [], "Azure": ["West Europe"], "GCP": ["europe-west4"]},
    "NO": {"AWS": [], "Azure": ["Norway East"], "GCP": []},
    "PL": {"AWS": [], "Azure": ["Poland Central"], "GCP": ["europe-central2"]},
    "SE": {"AWS": ["eu-north-1"], "Azure": ["Sweden Central"], "GCP": []},
    "UK": {
        "AWS": ["eu-west-2"],
        "Azure": ["UK South", "UK West"],
        "GCP": ["europe-west2"],
    },
}
