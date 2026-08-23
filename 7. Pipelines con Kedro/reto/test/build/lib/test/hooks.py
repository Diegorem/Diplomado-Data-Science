from datetime import datetime
import logging
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline

# 1. Obtenemos el logger configurado para Kedro
logger = logging.getLogger(__name__)


class MiPipelineHooks:
    """Clase con hooks personalizados para monitorear el ciclo de vida del proyecto."""

    # -------------------------------------------------------------
    # Hook A: Registra la hora de inicio del pipeline
    # -------------------------------------------------------------
    @hook_impl
    def before_pipeline_run(
        self, run_params: dict, pipeline: Pipeline, catalog: DataCatalog
    ) -> None:
        """Se ejecuta justo ANTES de que el pipeline empiece a correr."""
        # Obtenemos la fecha y hora actual con formato legible
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Emitimos el mensaje solicitado en el log
        logger.info(f"El pipeline inicio ejecución justo a las {hora_actual}")

    # -------------------------------------------------------------
    # Hook B: Registra la lista del catálogo cargado
    # -------------------------------------------------------------
    @hook_impl
    def after_catalog_created(
        self, catalog: DataCatalog, conf_catalog: dict, conf_creds: dict
    ) -> None:
        """Se ejecuta justo DESPUÉS de que Kedro construye el Data Catalog."""
        # Obtenemos todos los nombres de los datasets registrados en el catalog.yml
        datasets = list(catalog.list())

        # Registramos la lista en la bitácora
        logger.info(f"Lista del catálogo cargado: {datasets}")

    @hook_impl
    def after_pipeline_run(
        self, run_params: dict, pipeline: Pipeline, catalog: DataCatalog
    ) -> None:
        """Se ejecuta justo DESPUÉS de que el pipeline termina de correr."""
        # Obtenemos la fecha y hora actual con formato legible
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Emitimos el mensaje solicitado en el log
        logger.info(f"El pipeline terminó ejecución justo a las {hora_actual}")