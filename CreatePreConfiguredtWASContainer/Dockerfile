FROM ibmcom/websphere-traditional:latest

USER root

RUN mkdir /demo && chown was /demo

USER was

RUN mkdir /demo/mysqldrivers

COPY mysqldrivers/mysql-connector-java-8.0.21.jar /demo/mysqldrivers

COPY wsadmin.py /demo/
COPY cargotracker-1.0.war /demo/

COPY transformationadvisor-Linux_cargotracker_monolith_collection2.tgz.part* /demo/

WORKDIR "/demo"
RUN cat transformationadvisor-Linux_cargotracker_monolith_collection2.tgz.part? > transformationadvisor-Linux_cargotracker_monolith_collection2.tgz
RUN tar xvfz transformationadvisor-Linux_cargotracker_monolith_collection2.tgz
COPY customCmd.properties /demo/transformationadvisor-2.2.0/conf/

COPY PASSWORD /tmp/PASSWORD
ENV pwd=passw0rd
RUN echo $pwd

RUN wsadmin.sh -lang jython -f /demo/wsadmin.py -conntype NONE -username wsadmin -password passw0rd
