from config.celery import app

from order_manager.services.order_service import OrderService


@app.task()
def produce_order():
    OrderService.produce_order()
