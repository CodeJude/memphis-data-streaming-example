import asyncio
import random
from memphis import Memphis, Headers, MemphisError, MemphisConnectError, MemphisHeaderError, MemphisSchemaError

async def main():
    try:
        # Create a Memphis instance and connects to the Memphis server
        memphis = Memphis()
        await memphis.connect(host="localhost", username="stock_feed", connection_token="memphis")

        # Create a producer for the stock_prices station and set headers
        producer = await memphis.producer(station_name="stock_prices", producer_name="stock_price_producer")
        headers = Headers()

        while True:
            # Continously sends the prices to the Memphis server
            company = random.choice(["META", "MSFT", "AAPL", "GOOG", "FB", "AMZN", "TSLA"])
            price = round(random.uniform(100, 500), 2)
            headers.add("company", company)

            print(f"Producing: {company} - ${price}")
            await producer.produce(bytearray(f"{price}", 'utf-8'), headers=headers)
            await asyncio.sleep(1)

    except (MemphisError, MemphisConnectError, MemphisHeaderError, MemphisSchemaError) as e:
        print(e)

    finally:
        await memphis.close()

if __name__ == '__main__':
    asyncio.run(main())

