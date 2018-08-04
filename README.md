# Problem
See [here](https://github.com/InsightDataScience/pharmacy_counting)

# Run
- Go to the directory `./insight_testsuite` and run: `sh run_tests.sh` (This is for test)
- Or write the input file in the directory `./input` and change corespondingly in `run.sh` then run: `sh run.sh`

# The idea
- While reading the input file, use dictionary `drug_list` to record drug cost and prescribers. Use dictionary `drug_prescriber` to prevent duplicate input. For example, in the input file there might be duplicate lines.
- Then restore the dictionary `drug_list` in an list `result` and sort it by the `cost`. 
- Then iterate the list, write the each item into the output file.
