# Exact certificate for `nu(16)=12873`

## Result

The retained word

```text
answers/k16.word
```

has length `12873`, SHA-256

```text
890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

and its contiguous-subarray ORs contain all `65535` nonzero 16-bit masks.
The general monotone-deadline theorem gives

```text
nu(16) >= B(16) = binom(16,8) + 3 = 12873.
```

Therefore

\[
                         \boxed{\nu(16)=12873}.
\]

## Construction lineage

The construction starts from the authenticated four-filter `k=15` seed

```text
scratch/K15_FOURFILTER_SEED_20260731.word
SHA-256 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4
```

and its natural `k=16` carrier.  Reversing the inclusive prefix `[0..6388]`
and inclusive suffix `[12826..12869]` gives the endpoint-rerooted middle
carrier

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

with exact middle ownership and complete upper coverage.  The depth-three
schedule is

```text
omitted starts X = {12870,12871,12872}
omitted deadlines Y = {0,1,6388}
selected area       = 32224
physical short cells = 32230
```

and reserves the one-cell interval at physical position `6389` for the
singleton `0x8000`.  Removing that already-fixed target and cell leaves
`26331` lower targets, `32229` available physical cells, and `347677`
target-cell incidences.  The residual Hall graph has a perfect matching.

The remaining issue was simultaneous realization: choices for overlapping
short intervals must come from one common assignment of physical letters.
The exact direct CNF encodes that coupling.  Its variables are:

- one incidence selector for each of the `347677` residual Hall edges;
- one bit variable `a_(p,b)` for every bit allowed by the maximal envelope at
  physical position `p`;
- sequential at-most-one auxiliaries.

It enforces exactly one physical cell for every residual lower target, at
most one target per cell, the equivalence between physical bits and all
selected incidences that block them, nonempty letters, complete middle rows,
and literal realization of every selected lower target.  Thus any satisfying
assignment decodes to one physical word, not merely to a marginal matching.

## Exact model provenance

The complete generated bundle is retained locally under

```text
scratch/k16_trueff_commoncap_direct_cnf_20260731/
```

and on the H100 under

```text
/home/amodo/or15/work/trueff_commoncap_direct_cnf_20260731/
```

The large generated CNF and solver trace are deliberately not Git artifacts;
the following hashes freeze them:

| artifact | SHA-256 |
|---|---|
| `build_k16_trueff_commoncap_matching_cnf_20260731.cpp` | `1cc95858620183305e5b58bf158795ea5174cf22ca0fc9fb2a0cd555aeb2aa7e` |
| `model.cnf` | `7fc512869e0c525183c4796b746da87a1eb4f7652eebfc6465b839218b7e6e0c` |
| `model.map.tsv` | `abd76cf89a1b80123e46be3067de8fffa7173710dee2bcc3e39cccd8c398849d` |
| `model.meta.json` | `8f67b41a1ac7ee2c582e3927624489351b7289add665d1a1837d68ad7700aab2` |
| `solver.out` | `2efa5c7b3a73f53d913127e4c6620c56e7828f02fa04a87ae5e5e59242796165` |
| `proof.drat` | `dae871c459d179d9cbb1f92fd1b9ecfc94b825a6a58323090a6d1823e2976653` |

The table names the byte-exact generator retained inside the frozen bundle.
The repository also retains a fail-closed mirror at
`scratch/build_k16_trueff_commoncap_matching_cnf_20260731.cpp`, SHA-256
`09347eae587b482b4b0a8581c91257cae559c6b5ec1897ecadbb2691747e5b7d`.
It adds input-SHA and dimension regression checks without changing the CNF
semantics.

The CNF has `1,055,230` variables and `4,513,893` clauses.  Kissat 4.0.4,
invoked with `--no-binary --seed=1`, returned SAT (`exit 10`) after parsing
and propagation, with zero conflicts and zero decisions.  The positive
certificate is the decoded word; the retained `proof.drat` is a solver trace,
not an UNSAT proof and is not needed to trust the result.

## Independent verification

The result has four independent positive replay paths.

1. The model decoder reconstructs the selected matching, recomputes every
   maximal common cap rather than trusting the model's `a` variables, checks
   every middle and selected lower target, then directly enumerates all
   interval ORs.  It reports `PASS_LITERAL_UNIVERSAL_WORD` and `65535/65535`.
   Its source SHA is
   `6395121fca6bbd7a9466ef9e035db5258f4ead7a419ebade011b89a07898a94b`;
   its audit SHA is
   `a7fdc56461c1d25d496853740143badf9a88f06fba0b064d1de2185325c3a700`.
2. A separately implemented direct audit ignores all selector metadata and
   replays the decoded word against the schedule, target carrier, all short
   lower targets, and all `65535` masks.  Its audit SHA is
   `bf4052620e822dbdbb35ea7535c3e5a7f01641a3218ac4b9e8f0945f1393c063`.
3. A second independently implemented model audit produces a byte-identical
   word and the same full literal replay.  Its audit SHA is
   `65387456186adf7c196baf3a1fc2bc7a198a3c865d0fcaad7dbab3c311482df7`.
4. The repository's generic verifier, independent of the construction,
   reports

   ```text
   PASS k=16 length=12873 covered=65535/65535
   counting lower bound: d=3, B(16)=12870+3=12873
   ```

A minimal independent C++ interval enumerator is also retained as
`scratch/verify_k16_optimal_12873_independent.cpp`; it reports
`PASS length=12873 covered=65535/65535`.

The retained fail-closed lineage audit
`scratch/audit_lane_k16_c7be_commonq_chain_20260731.py` (SHA-256
`8892cae1ab199eada719b9f993698145ce798d34cd4979c6fb404bdba807cca8`)
independently hashes the input chronology before model replay, checks all
`4,513,893` clauses and `418,436` map rows, reconstructs the byte-identical
word, and performs the full mask replay.  The retained result is
`scratch/k16_c7be_commonq_chain_independent_20260731.audit.json`; its
SHA-256 is
`d451c9b3ef40d62c54cec9139b1a969d21c1952283ba82f037f122b58d42735d`
and its normalized payload SHA-256 is
`80a94b84551c6c04a6c9a44d29e9615553ef721bb1409e700f65a933a9c030d2`.

## Why the simple even splice did not settle this case

The closed-form splice

```text
X, 0x8000, (X without its last letter) | 0x8000
```

is a valid general construction of length `2*nu(15)=12876`.  It proves a
small additive upper bound but is three positions longer than `B(16)`.  The
previous `12874` certificate removed two of those positions but still paid
one extra unit.  The exact `12873` construction uses a different mechanism:
an endpoint-rerooted genuine four-filter carrier and one simultaneous
common-cap matching.  Consequently the splice theorem is valuable general
structure, but it does not automatically imply the exact `k=16` value.
