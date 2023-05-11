FROM mcr.microsoft.com/devcontainers/universal:2

# Install Python packages
RUN pip3 install --no-cache-dir \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    jupyterlab 

# Install required packages for R
RUN apt-get update && \
    apt-get install -y --no-install-recommends r-base && \
    apt-get install -y libzmq3-dev libharfbuzz-dev libfribidi-dev

RUN apt-get install -y libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev && \
    apt-get install -y build-essential libcurl4-openssl-dev libxml2-dev && \
    apt-get install -y libssl-dev libfontconfig1-dev

# Install R packages
RUN echo "install.packages(c('languageserver', 'ggplot2', 'dplyr','data.table', 'knitr', 'magrittr', 'curl', 'ISLR', 'stringr','devtools'), repos='https://cran.rstudio.com/')" | R --no-save 

# Install R kernel for Jupyter
RUN echo "devtools::install_github('IRkernel/IRkernel')" | R --no-save 
RUN echo "IRkernel::installspec()" | R --no-save


# install Latex
RUN apt-get update && \
    apt-get install --no-install-recommends -y texlive-full

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install google chrome and chromium

# Chrome instalation 
RUN apt-get update && apt-get install -y gnupg2 wget curl
RUN apt-get install -y libu2f-udev unzip fonts-liberation 
    
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
&& apt-get update && apt-get install -y google-chrome-stable \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
&& echo "Chrome version: " && apt-cache policy google-chrome-stable | grep "Installed:" | awk '{print $2}'


# Check chrome version
RUN echo "Chrome: " && google-chrome --version

# Chromium instalation
RUN apt-get update && \
    apt-get install -y chromium-browser && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


