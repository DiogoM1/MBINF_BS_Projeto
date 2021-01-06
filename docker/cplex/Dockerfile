FROM python:3.7

# LABEL about the custom image
LABEL maintainer="diogodpmacedo@gmail.com"
LABEL version="1.1"
LABEL description="This is a small docker for the harmonization of bioinformatics tooling and cplex solver for the final BS project"

RUN apt update

# create cplex user
RUN useradd -ms /bin/bash cplex
USER cplex

# get files needed for cplex installation
COPY cplex_studio*.linux-x86-64.bin /home/cplex/cplex_installation/
COPY installer.properties /home/cplex/cplex_installation/

# install cplex from files
# built using CPLEX silent instalation
# https://www.ibm.com/support/knowledgecenter/SSSA5P_12.10.0/ilog.odms.studio.help/Optimization_Studio/topics/td_silent_install.html
RUN cd /home/cplex/cplex_installation/  && \
    bash cplex_studio*.linux-x86-64.bin -f "/home/cplex/cplex_installation/installer.properties"

USER root

# install cplex in your python environment, it might need a more recent version if 3.7 is too old for your usage
# remember to check compability with ME python packages
RUN cd /home/cplex/CPLEX_Studio/cplex/python/3.7/x86-64_linux/ && \
    python3 setup.py install && \
    pip install docplex

# clean up of cplex installation files
RUN rm -r /home/cplex/cplex_installation/

# install python Metabolic Engineering tooling and jupyter
RUN pip install --upgrade pip && \
    pip install jupyter && \
    pip install numpy && \
    pip install reframed && \
    pip install cobra && \
    pip install cobamp && \
    pip install escher && \
    pip install mewpy && \
    pip install biopython

# set correct non-root user
USER cplex

# document expected port for jupyter
EXPOSE 8888
# set correct terminal env
ENTRYPOINT ["bash"]