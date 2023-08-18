#Getting base image
FROM openjdk:11

#working directory where all code will be kept
WORKDIR app/

#copy the app to current directory of container
COPY Hello.java .

#Compile code
RUN javac Hello.java

#run java complied code
CMD ["java","Hello"]

