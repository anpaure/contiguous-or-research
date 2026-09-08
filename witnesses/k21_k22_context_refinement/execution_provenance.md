# Execution provenance

One fixed paired run on h100/arboghast, 2026-09-09. Root and induction
read the complete source before execution. No optimizer or schedule replay.

Command:

```sh
ssh h100 'python3 /home/amodo/exact-b-k21-k22-context-refinement-20260909/verify_k21_k22_context_refinement_suffix_and_lift.py --inputs /home/amodo/exact-b-k21-k22-context-refinement-20260909/inputs --out /home/amodo/exact-b-k21-k22-context-refinement-20260909/suffix_and_lift > /home/amodo/exact-b-k21-k22-context-refinement-20260909/suffix_and_lift.run.log 2>&1'
```

The source enforces120 CPU seconds,150 wall seconds,3GiB address space
and512MiB per file. Exit0; actual13.289791308 CPU seconds and
13.290546125732362 wall seconds. Both complete cubes and every saved
witness passed; the22 lift matched byte for byte.

The output directory was copied intact by rsync. Remote sha256sum and local
shasum agreed for these principal artifacts:

|Artifact|SHA256|
|---|---|
|checker.py|197d30ce52b14f085fbf1ba457da11b614afbf7485ccaf4538b86154a55b740a|
|complete_suffix_range_lift_certificate.json|1e01464fd535dd1d20edc850e07d2b83406fcd460830accc56a7afab8714fddf|
|k21_all_target_witnesses.jsonl.gz|3983b987a9a51ab97d6d2172dfd0665daef0e97dd3cdb3580916bc375151da47|
|k22_all_target_witnesses.jsonl.gz|8e74a7648f92bb00cf4a01ec9d75c25fb3f601d1fecec6261e9190b59f45af05|
|k22_regenerated_from_k21.word|aef0f78939dec65f60ffffe3c1ce77999fdacdd3034964684884b7e5352d5a59|

The local source outside the bundle has the identical checker hash. The
raw21 hash isf404c9f1e00bf40b24b1996ba31ee87c26cadfa70c2ca6140b04891685cb7392;
the raw22 hash is the regenerated-word hash above. Both were pinned inside
the executed checker before enumeration. The complete run log is retained
at ../k21_k22_context_refinement.run.log.
