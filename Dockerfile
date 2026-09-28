FROM python:3.13-slim

# System dependencies:
#  - libicu-dev: .NET runtime globalization (the runtime cannot start without ICU)
#  - libfontconfig1: loaded by the bundled SkiaSharp and Aspose.Slides natives;
#    presentations and export to Excel fail without it
# libgdiplus is not needed since 26.9.
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends libicu-dev libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
