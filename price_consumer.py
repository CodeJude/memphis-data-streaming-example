import asyncio
from memphis import Memphis, MemphisError, MemphisConnectError, MemphisHeaderError

# Define the asynchronous main function for the price consumer
async def main():
    async def msg_handler(msgs, error, context):
        try:
            for msg in msgs:
                company = msg.get_headers().get("company", "UNKNOWN")
                price = msg.get_data().decode('utf-8')
                print(f"Received: {company} - ${price}")
                await msg.ack()
                
                if error:
                    print(error)
                    
        except (MemphisError, MemphisConnectError, MemphisHeaderError) as e:
            print(e)
            return

    try:
        # Create a Memphis instance and connect to the Memphis server
        memphis = Memphis()
        await memphis.connect(host="localhost", username="stock_feed", connection_token="memphis")

        # Create a consumer for the "stock prices" station 
        consumer = await memphis.consumer(station_name="stock_prices", consumer_name="stock_price_consumer", consumer_group="stock_price_group")
        consumer.set_context({"key": "value"})
        consumer.consume(msg_handler)
        
        # Keep your main thread alive so the consumer will keep receiving data
        await asyncio.Event().wait()

    except (MemphisError, MemphisConnectError) as e:
        print(e)

    finally:
        await memphis.close()

if __name__ == '__main__':
    asyncio.run(main())

