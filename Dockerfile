FROM python AS bbkbasebx

EXPOSE 9818

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt update && apt install graphviz -y
RUN apt update && apt install wget -y
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
# RUN apt install ./wkhtmltox_0.12.6.1-3.bookworm_amd64.deb -y

# RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb \
#     && dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb


RUN pip3 install pyvis
RUN pip3 install jupyterlab
RUN pip3 install ipykernel
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install google-generativeai
RUN pip3 install tqdm
RUN pip3 install unstructured
RUN pip3 install geopy
RUN pip3 install reportlab
RUN pip3 install pdfminer.six
RUN pip3 install langchain
RUN pip3 install langchain-openai
RUN pip3 install langchain_experimental
RUN pip3 install openai
RUN pip3 install networkx
RUN pip3 install pydot
RUN pip3 install scipy
RUN pip3 install dask
RUN pip3 install neo4j
RUN pip3 install wikipedia-api 
RUN pip3 install requests 
RUN pip3 install beautifulsoup4
RUN pip3 install python-dotenv


WORKDIR /code

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

ENTRYPOINT [ "jupyter", "lab", "--ip=0.0.0.0", "--port=9818" ]
