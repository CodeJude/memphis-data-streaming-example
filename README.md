# Memphis Data Streaming Example

This project provides an example of how to use the Memphis data streaming platform to create a producer and consumer for streaming data. It includes an example of streaming stock price data from a public API and consuming that data in real-time using the Memphis platform.

## Getting Started

To get started with this project, you will need to install the following dependencies:

Python 3.x
Memphis Python library
You can install the Memphis library by running the following command:

```
pip install memphis-py
```

Once you have installed the dependencies, you can run the producer and consumer scripts to start streaming data.

## Running the Producer

To run the producer script, use the following command:

```
python3 price_producer.py
```

This script streams stock price data from a public API and sends it to the Memphis platform for consumption.

## Running the Consumer

To run the consumer script, use the following command:

```
python3 price_consumer.py
```

This script consumes the stock price data that is being streamed by the producer and prints it to the console.

## Configuration

The price_producer.py and price_consumer.py scripts both require configuration to connect to the Memphis platform. You can configure the connection by modifying the following variables in the scripts:

MEMPHIS_HOSTNAME: The hostname of the Memphis platform

MEMPHIS_APPLICATION_USER: The username of the application connecting to the Memphis platform

MEMPHIS_CONNECTION_TOKEN: The connection token for the application connecting to the Memphis platform

STATION_NAME: The name of the Memphis station to use for streaming data

PRODUCER_NAME: The name of the producer application

CONSUMER_NAME: The name of the consumer application

CONSUMER_GROUP_NAME: The name of the consumer group

## Conclusion

The Memphis data streaming platform provides an easy and efficient way for developers and data engineers to stream data in real-time. This project provides an example of how to use the Memphis platform to stream stock price data, but the platform can be used to stream any type of data. With its ease of use and flexibility, Memphis is a great choice for any streaming data project.
