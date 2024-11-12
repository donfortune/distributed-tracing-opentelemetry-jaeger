from fastapi import FastAPI
# from opentelemetry import trace
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.resources import Resource
# from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
# from opentelemetry.sdk.trace.export import BatchSpanProcessor

# # Set up the tracer provider with the correct resource and service name
# trace.set_tracer_provider(
#     TracerProvider(
#         resource=Resource.create(
#             {"service.name": "fastapi-SERVICE"}  # Corrected format for service name
#         )
#     )
# )

# # Get the tracer provider
# tracer_provider = trace.get_tracer_provider()

# # Configure the Jaeger exporter
# jaeger_exporter = JaegerExporter(
#     agent_host_name="host.docker.internal",  # Jaeger agent host
#     agent_port=6831,  # Jaeger agent port
# )

# # Add the Jaeger exporter to the tracer provider
# tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

# # Create FastAPI app and instrument it
app = FastAPI()

# # Instrument the FastAPI app to enable tracing
# FastAPIInstrumentor.instrument_app(app)

@app.get("/")
def home():
    return {"message": "Hello World"}
