
import logging

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def process_order(order_id, amount):
    logging.debug("Processing order: %s", order_id)

    if amount <= 0:
        logging.error("Invalid order amount: %s", amount)
        return

    if amount < 500:
        logging.warning("Order amount is below 500")

    logging.info("Order %s processed successfully", order_id)


if __name__ == "__main__":
    process_order("ORD101", 1000)
    process_order("ORD102", 300)
    process_order("ORD103", -100)

    print("Order processing completed.")
    print("Check application.log for log messages.")
