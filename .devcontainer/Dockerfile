# set base image (host OS)
FROM python:3.9

# install dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get -y install --no-install-recommends zsh

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && chsh -s /bin/zsh $USERNAME

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY . .

RUN pip install -r requirements.txt
