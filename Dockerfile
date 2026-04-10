FROM node:18-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    curl unzip xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Typst
RUN curl -fsSL https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-musl.tar.xz \
    | tar -xJ --strip-components=1 -C /usr/local/bin/

# Install Python dependencies
RUN python3 -m pip install --break-system-packages feedgen pyyaml

# Install MyST Markdown
RUN npm install -g mystmd

# Download fonts
RUN mkdir -p /fonts \
    && curl -sL "https://github.com/adobe-fonts/source-sans-pro/releases/download/3.006R/source-sans-pro-3.006R.zip" -o /tmp/ssp.zip \
    && unzip -o /tmp/ssp.zip -d /tmp/ssp \
    && cp /tmp/ssp/source-sans-pro-3.006R/OTF/*.otf /fonts/ \
    && curl -sL "https://use.fontawesome.com/releases/v6.7.2/fontawesome-free-6.7.2-desktop.zip" -o /tmp/fa.zip \
    && unzip -o /tmp/fa.zip -d /tmp/fa \
    && cp /tmp/fa/fontawesome-free-6.7.2-desktop/otfs/*.otf /fonts/ \
    && rm -rf /tmp/ssp /tmp/fa /tmp/ssp.zip /tmp/fa.zip

WORKDIR /app
COPY . .

# Build CV PDF
RUN python3 generate_cv.py \
    && typst compile cv.typ cv.pdf --font-path /fonts --ignore-system-fonts

# Build site content
RUN myst build --site

# Generate RSS/Atom feeds (into repo root; copied later if HTML build exists)
RUN python3 generate_rss.py || true

EXPOSE 3000 3100

# Bind to 0.0.0.0 so the site is accessible outside the container
ENV HOST=0.0.0.0
CMD ["myst", "start", "--keep-host"]
