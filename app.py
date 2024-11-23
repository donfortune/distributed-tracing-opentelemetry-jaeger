from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
import time
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
#from opentelemetry.exporter.jaeger import JaegerExporter

#set up jaeger exporter
# jaeger_exporter = JaegerExporter(
#     agent_address="jaeger-agent:5775", 
#     agent_port=5775
# )

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Change to "localhost" for local Docker 
    agent_port=6831               # Standard OpenTelemetry port for Jaeger
)

resource = Resource(attributes={"service.name": "Don-fortune-Macbook-Pro", "os-version": 1234.5, "cluster": "A", "datacenter":"NG"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)

console_exporter = ConsoleSpanExporter()
processor.add_span_processor(BatchSpanProcessor(console_exporter))



 # events are not a full span, they happen within a span
# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("my.tracer.name")

@tracer.start_as_current_span("add")
def add(first, second):
    current_span = trace.get_current_span() # get status of span
    current_span.set_status(trace.StatusCode.OK) # set status of span

    current_span.set_attributes(attributes={
        "first-value": first,
        "second-value": second
    })

    # add an event
    time.sleep(1)
    current_span.add_event(name="myEvent", attributes={"foo4": 222, "addition_process": "completed"}, timestamp=time.time_ns())
    time.sleep(1)

    return first + second

if __name__ == "__main__":
    return_value = add(11, 3)
    print(f"Return value: {return_value}")
