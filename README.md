# InterviewTask
This repository contains the code to scrape the first 500 ads for flats for sale from sreality.cz, save them to a postgreSQl database and then display them on a simple Flask webpage. For each ad are displayed the title, location and price and 3 images.


You can simply run the code by using the (sudo) docker compose up command and then visit 127.0.0.1:8080 to see the ads on a simple web page.

Make sure you have containerd installed before running, otherwise you might get errors when starting the docker containers.
