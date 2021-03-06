from typing import Dict, List, Tuple
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from energy_calculator import best_server_location

app = FastAPI()


class Body(BaseModel):
    countries: List[str]
    cloud_provider: str
    nuclear_is_green = False


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)

    response.headers["Cache-Control"] = "no-store"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers[
        "Content-Security-Policy"
    ] = "default-src 'self'; script-src 'self' https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui-bundle.js 'sha256-R2r7jpC1j6BEeer9P/YDRn6ufsaSnnARhKTdfrSKStk='; style-src 'self' https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui.css; frame-ancestors 'none'"

    # HTML-related (future-proof)
    response.headers["Feature-Policy"] = "'none'"
    response.headers["Referrer-Policy"] = "no-referrer"

    return response

@app.post("/ranking")
async def root(body: Body):
    ranking, timestamp = best_server_location(
        body.countries, nuclear_is_green=body.nuclear_is_green
    )
    response = construct_response(ranking, body.cloud_provider, timestamp)
    return response


def construct_response(
    ranking: List[Tuple[str, float]], selected_cloud_provider: str, timestamp: str
):
    CLOUD_REGIONS: Dict[str, List[Tuple[str, str]]] = {
        "AT": [
            ("Azure", "Austria East"),
        ],
        "BE": [("GCP", "europe-west1")],
        "CH": [("Azure", "Switzerland North"), ("GCP", "europe-west6")],
        "DE": [
            ("AWS", "eu-central-1"),
            ("Azure", "Germany West Central"),
            ("GCP", "europe-west3"),
        ],
        "DK": [
            ("Azure", "Denmark East"),
        ],
        "ES": [
            ("Azure", "Spain Central"),
        ],
        "FI": [("GCP", "europe-north1")],
        "FR": [
            ("AWS", "eu-west-3"),
            ("Azure", "France Central"),
        ],
        "GR": [
            ("Azure", "Greece Central"),
        ],
        "IE": [
            ("AWS", "eu-west-1"),
            ("Azure", "North Europe"),
        ],
        "IT": [
            ("AWS", "eu-south-1"),
            ("Azure", "Italy North"),
        ],
        "NL": [("Azure", "West Europe"), ("GCP", "europe-west4")],
        "NO": [("Azure", "Norway East")],
        "PL": [("Azure", "Poland Central"), ("GCP", "europe-central2")],
        "SE": [
            ("AWS", "eu-north-1"),
            ("Azure", "Sweden Central"),
        ],
        "UK": [
            ("AWS", "eu-west-2"),
            ("Azure", "UK South"),
            ("Azure", "UK West"),
            ("GCP", "europe-west2"),
        ],
    }

    response = {"timestamp": timestamp, "data": []}

    for country, percentage in ranking:
        cloud_regions = CLOUD_REGIONS[country]
        for cloud_provider, region in cloud_regions:
            if cloud_provider == selected_cloud_provider:
                response["data"].append(
                    {
                        "country": country,
                        "percentage": percentage,
                        "cloud_provider": cloud_provider,
                        "region": region,
                    }
                )

    return response
