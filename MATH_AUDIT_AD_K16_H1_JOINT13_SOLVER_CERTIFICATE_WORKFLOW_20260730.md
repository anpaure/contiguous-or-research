# Audit of the K16 H1 joint13 solver/certificate workflow

Date: 2026-07-30  
Lane: AD independent workflow audit  
Status: **workflow audited; no solve performed and no remote artifact written**

## 1. Frozen formula and decoder

The formula to be solved is the composed proxy/supply-code formula, not any
of the earlier explicit-witness or occupancy formulas.

```text
scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.cnf
SHA-256 f03c8c3e38caf4d4f47bb7ae4569e07526afdd7689acc2c1b32b8dfd71ab488e

scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.map.json
SHA-256 f5f50ec0563adb1175500ef1426144f753dd72ed37f360f787ebb840feeb5ed8
payload SHA-256 7ff2f7a17a45b40360b7e29a004365b7f7031b169188cb58e85ddf2d1e6c8698

scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a

scratch/decode_verify_ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730.py
SHA-256 cbb9e235d8e71b144caf3e69f659f40f3f3651b107366f652a342d35ef88ffe4
```

The map declares exactly 469 variables, 28,233 clauses and 174,662
literals.  Its 275 code variables choose one retained chart for each of the
55 residual targets; its 194 supply variables certify the proxy generators.
There are 1,579 retained actions.  The frozen support is

```text
0,1,4486,4487,4488,4489,6438,6439,6440,12869,12870,12871,12872.
```

The independent ordered-clause reconstruction is

```text
scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.independent_audit.json
SHA-256 331f1d7d56c18c6c639c8abf27b9e177c692a012b9a20e6878b4397efb025c76
payload SHA-256 72be9126c4233d3d18c3008a2751774c52db46410c9ba2aa599d2a6658b774f1
status PASS_UNSOLVED_UNKNOWN.
```

I independently recomputed the map payload and the four displayed file
hashes.  They agree with the composition theorem and audit.

## 2. SAT decoding is fail-closed at the semantic gates

The correct invocation is of the form

```text
python3 scratch/decode_verify_ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730.py \
  --source scratch/k16_h2_to_h1_p0.h1.word \
  --cnf scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.cnf \
  --map scratch/ad_k16_h1_fourportal_joint13_proxy_supplycode_20260730/model.map.json \
  --assignment SOLVE.OUT \
  --word answers/k16_upper12873.word \
  --audit scratch/ad_k16_h1_joint13_proxy_supplycode_12873.decode.audit.json
```

Kissat must not be given `-n` or `--partial`.  Its default is a complete
assignment.  The decoder requires an explicit SAT status, exactly one truth
value for every variable 1 through 469, and rejects contradictory or
out-of-range literals.  It then checks every CNF clause itself.  Thus a
solver exit code or status line alone is not accepted as a witness.

The semantic decoding has three further independent gates:

1. It decodes a valid chart code for every target and checks the proxy supply
   and every forbidden supply.
2. It forms each physical cell as the intersection of all targets crossing
   it and checks every selected chart's **original need**, not merely the
   reduced proxy generator.
3. It substitutes the thirteen values into the hash-frozen source and uses a
   suffix-state contiguous-OR replay.  It explicitly rejects unless all
   65,535 nonempty masks occur.

For a second implementation, run, without Python optimization,

```text
python3 verify_word.py --k 16 answers/k16_upper12873.word
```

`verify_word.py` has SHA-256
`7beea259577d243b8952634a39baef2c38d3dd5adb33649de1314b9975163b79`.
It is a start-by-start replay and also checks the exact counting-bound delay.
The stdout and resource log must be retained and hashed.  A SAT result is
publishable only after both replays pass.  The canonical answer name is
`answers/k16_upper12873.word`; this file does not currently exist.

There is one output-transaction caveat in the decoder.  Its two calls to
`atomic_text` occur sequentially: it writes the word before attempting the
audit.  It does not first check that both output paths are distinct and
absent.  Therefore the caller must preflight that both paths are distinct and
neither exists.  Otherwise a pre-existing audit path can leave a newly
written word without its audit.  This does not affect semantic soundness of a
successful decode, but it is a fail-closed bundle-hygiene requirement.

## 3. Solver-output and proof-format rules

The authenticated H100 tools under `/home`, checked read-only in this audit,
are

```text
/home/amodo/or15/kissat/build/kissat
version 4.0.4
SHA-256 3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d

/home/amodo/or15/drat-trim/drat-trim
SHA-256 92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a

/home/amodo/or15/drat-trim/lrat-check
SHA-256 e9e71c96b68dc9ed22db35d7581e613e6b161ffbc82c20cba5699f8320a065b8
```

Kissat 4.0.4 accepts `kissat [options] CNF PROOF`.  The proof path must be a
new path; do not use `-f` to overwrite an old trace.  Exit 10 plus
`s SATISFIABLE` selects the SAT branch.  Exit 20 plus `s UNSATISFIABLE`
selects the proof-checking branch.  A proof file left by a SAT, UNKNOWN,
timeout or killed run is an incomplete by-product, never a certificate.

For UNSAT, independently convert and check the exact frozen CNF by

```text
drat-trim model.cnf proof.drat -c core.cnf -L core.lrat
lrat-check model.cnf core.lrat
```

The first command must exit zero and print `s VERIFIED`; the second must exit
zero and print its verified marker.  The LRAT is checked against the **full
original 28,233-clause CNF**, not the extracted and renumbered diagnostic
core.  Hash the CNF, map, independent audit, solver binary, solver stdout and
stderr, DRAT, core, LRAT, both checker binaries and both checker logs.

Kissat emits ordinary DRAT for a plain `.drat` proof path.  If CaDiCaL is
substituted, its binary/ASCII proof option must be recorded and matched by
the corresponding `drat-trim` parse mode; using Kissat avoids this extra
format ambiguity.

## 4. Resource and status protocol

The solve and proof checks must use a new directory below
`/home/amodo/or15/work/`, never `/dev/shm`, with explicit wall-time and
address-space caps.  The input hashes must be recorded before solving.  A
timeout, signal, exit other than 10 or 20, ENOSPC, malformed/partial model,
missing proof, failed DRAT check or failed LRAT check is **UNKNOWN**.  A
nonempty partial DRAT does not improve that status.

If SAT passes both literal replays, it proves a universal length-12,873 word
and closes the current gap.  If checked UNSAT passes DRAT and LRAT, the exact
conclusion is only:

> No universal word is obtainable by arbitrary nonzero substitution on the
> frozen joint13 support of the authenticated source.

It is not a global length-12,873 impossibility and not WLOG outside that
fibre.

