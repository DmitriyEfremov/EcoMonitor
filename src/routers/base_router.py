from fastapi import APIRouter

from core.config import Settings
from src.routers.v1.router_eco_problems import router_eco_problems
from src.routers.v1.router_files_eco import router_files_eco
from src.routers.v1.router_files_report import router_files_report
from src.routers.v1.router_report import router_report
from src.routers.v1.router_report_status import router_report_status
from src.routers.v1.router_statuses import router_statuses
from src.routers.v1.router_type_incidents import router_type_incidents

base_router = APIRouter(prefix=Settings.API_VERSION)

base_router.include_router(router_statuses)
base_router.include_router(router_files_eco)
base_router.include_router(router_type_incidents)
base_router.include_router(router_eco_problems)
base_router.include_router(router_report)
base_router.include_router(router_report_status)
base_router.include_router(router_files_report)
