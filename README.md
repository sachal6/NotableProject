# NotableProject

## Setup
Using python, run 'pip install -r requirements.txt' and then 'python api.py' to launch the server

## Usage
Please see 'instructions.ipynb' for a full demonstration

## Known Errors
The API as implemented does not check to make sure that only 3 appointments can overlap at a time. This is a fairly trivial fix with the overlapping-interval algorithm (https://www.geeksforgeeks.org/merging-intervals/) but due to time constraints, this was left out. 


The API assumes that all inputs (especially dates/times) are well-formatted and does not check for adverserial inputs (though this can, again, be trivially implemented).


Due to time constraints, the API was unable to be thoroughly commented/documented. This would not be the case for a proper launch or code review. 