from config.celery import app

from order_manager.services.order_service import OrderService


@app.task()
def task_produce_order():
    OrderService.produce_order()
