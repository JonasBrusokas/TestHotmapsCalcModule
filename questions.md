
- Do we have data already?
    - Can we grab data from existing data as examples to pipe to develpment?
    - A: in Local development - we do not access the database 
      - We need to download the slice from HotMaps 
        - Alternatively: generate data ourselves?
      - NOTE: we do not have access to database 
      - NOTE2: we cannot run HotMapsV1 locally, as the data itself takes 500GB
        - Jenkins pipeline checks for CMs to be updated, runs tests, tries to integrate modification to the development tool
      - GOAL: Running something locally

- Data selection
  - In Enermaps - the layers were hardcoded into the CM
  - 

- What environments are available?
  - Development server 
    - Currently not up-to-date, they played with the cloud version, ...
    - Goal: Use geoserver and database from remote, other is local
      - RUN front-end and API locally, geoserver and database is too big
        - Front-end and API will be Docker

- What Python libraries are available?
  - A: These should be put inside requirements
  - **ALWAYS** specify exact versions in requirements.txt
- How is this deployed?

### Remaining

- How do download slices from existing HotMaps?
  - This is just for local testing purposes
  - hotmaps.eu/map
    - Platform does not allow downloading huge layers
      - LAU2 or NUTS3 are available
    - Downloading the whole dataset ("download default dataset" button - cloud button)

- Unit tests/specs for making sure that our CM is ok? Works as intended?
  - Integration tests
    - Mustafa: Not really, just respect your local tests
      - You could get error messages from Jenkins
        - Jean-Marie: will use Jenkins, will use the DevSecOps pipeline
        - We should have read access for the developers
      - Common error: requirements.txt 

- Uploading our own layers?
  - For new layers, GitLab pipeline 
  - Metadata / datapackage files
  - Script for data integation (done by HESSO colleagues)
  - **INSTRUCTIONS?**
    - NOTE: might need a hosted "open source" GitLab as some EU projects do not allow US companies for hosting their stuff
      - In H2020 FEVER we had Atlassian (Australia) software: Confluence, Jira, BitBucket

- How to develop?
  - BaseCM up to date?
  - Latest version of the front-end?
  
  - Mustafa: develop local, then integrate to the V2 pipeline
    - **Communicate special needs! Special libraries, optimizers, ...**

## Notes

- Long queries (when you do optimization, etc) is not great 
  - What happens before?

- Good idea to do "mock-ups" (this is probably for the publishing part)
  - Not really a CM
  - Just "screenshots" 
  
  - Key data:
    - Input parameters: type
    - Type of layers needed for the CM
    - List of libraries that we are using
    
    - Format of raster file?
    - What time scale is needed?

  - Precalculation
    - If the calculations are too long
    - Excel, csv file?
    - Quick and dirty: inline .csv file with repository
      - We can access .tif files from GitHub (we can grab the link)
    - Better way: put into database, make it avaialble to the tool