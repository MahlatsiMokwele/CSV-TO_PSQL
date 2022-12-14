# CSV-TO_PSQL
This python project enables the ability to upload csv files to PSQL Databases

## Prerequisits
*   Python 
*   VirtualEnvironment
*   .env file

#### Create .env File
    POSTGRES_DATA=/path/to/data/mount/
    POSTGRES_PASSWORD=<password>
    POSTGRES_USER=<postgres_user>
    POSTGRES_DB=<name_of_database>
    POSTGRES_EXT_PORT=55432 # Or preferred external port for POSTGRES
    POSTGRES_HOST=postgis # Keep The Same
    SCHEMA_LOCATION=/path/to/schema/<file>.sql
    CSV_LOCATION=/path/to/csv/location/<file>.csv
Change the variables to suit your set-up.

### How To Use CSV-TO_PSQL
1. In the root folder of your project, run the following to create your database:
```markdown
docker-compose up -d
```
2. Create your VirtualEnvironment & activate it
```markdown
virtualenv <virtualenv_name> --python=python3
source <virtualenv_name>/bin/activate
```
3. Install Required Dependencies
```markdown
pip install -r requirements.txt
```    
4. Once All Of The Above Has Been Done Successfully, Run:
```markdown
python main.py
```
    
