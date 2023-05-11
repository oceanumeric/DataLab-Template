FROM mcr.microsoft.com/devcontainers/universal:2

# Install additional packages
FROM mcr.microsoft.com/devcontainers/universal:2

# Install R and R packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends r-base && \
    echo "install.packages(c('tidyverse', 'ggplot2', 'dplyr', 'readr', 'data.table', 'knitr', 'magrittr', 'curl', 'ISLR', 'stringr', 'devtools', 'IRkernel'), repos='https://cran.rstudio.com/')" | R --no-save && \
    Rscript -e "IRkernel::installspec()"

# Install Python packages
RUN pip3 install --no-cache-dir \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    jupyterlab 
