# Execution provenance: exact21/22 suffix, range, cyclic and lift check

The complete source was reviewed by root and the induction agent before
one execution on h100, hostname `arboghast`. Both input hashes and the
source hash were checked remotely before launch. No retry occurred.

```sh
ssh h100 'timeout 150s python3 /home/amodo/exact-b-k21-k22-optimal-20260909/verify_k21_k22_optimal_suffix_and_lift.py --inputs /home/amodo/exact-b-k21-k22-optimal-20260909/inputs --out /home/amodo/exact-b-k21-k22-optimal-20260909/output > /home/amodo/exact-b-k21-k22-optimal-20260909/run.log 2>&1'
```

The output directory was fresh. Source-enforced limits were120 CPU
seconds,150 wall seconds,3 GiB address space and512 MiB per output file.
The run exited0, with final status
`PASS_EXACT_OPTIMA_CYCLIC21_AND_PERIODIC_LIFT`, CPU13.289354858 seconds
and wall13.289871970191598 seconds. The complete output was copied locally;
the report, source snapshot and both complete witness archives were hash
compared with the remote originals. The regenerated22 word has the exact
supplied raw hash recorded in the report.

```text
checker.py
cf2701d2e7e3fe95d078d472a03caead671a20a671c34bacc160c73aece9fc1f
complete_suffix_range_cyclic_lift_certificate.json
d5a6e51f5d5c14cf218b86c7e9ee1d8885f43525c87b1c58619e35d01e375706
k21_all_target_witnesses.jsonl.gz
5f7e244f8c6d0ba416e72635aa47f8a94e20cfcbfdc4344fd17afe1c0c3a537a
k22_all_target_witnesses.jsonl.gz
252bf1ef60829e326071e7a7252ba729aadf5cc94ff7f5f5d61d2c2b19d7b967
```

The report's `run_started.json` is a start marker, not the success
certificate. Success is recorded only in the final complete report and
run log. The separate forward implementation has its own provenance.
