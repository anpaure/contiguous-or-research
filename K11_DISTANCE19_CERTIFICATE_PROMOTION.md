# Promotion of the corrected `k=11` distance-19 certificate

## Verdict

The pending theorem in `K11_DISTANCE19_AUDIT.md` is now **proved**.
The independent `drat-trim` run terminated with

```text
s VERIFIED
EXIT:0
```

after 9848.830 seconds.  Its complete local log has SHA-256

```text
da9fddf68f57aefbdf4e61941c925ee91b086f5d7b116aa43862dd34a32e2bfd
```

The exact proof-critical hashes are

```text
b2c247d22105cfa963d4e6871e03397c5948a4447d2cedf5e5c7f7f09ccb90ef  corrected_allinc19.cnf
e55401bf90ed645f032f8769db262646ed661519d753aa441b05198b4a30fa78  corrected_allinc19_proof.drat
1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2  recombine_paths_sat.cpp
71dfa5b4c33c86dee070b46fb991d9c8a0ef2c9d49a09825fc96d8e8c398552f  k11_allbase_r7full.txt
f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477  k11_lower956_upper549.txt
ae0cd43d8e780c8c682a63fac37f41d242b07ca5fd16e0f6ccca326e44f08be6  producer log
```

The proof file has 4,723,026,902 bytes.  The CNF, source, inputs, producer
log, and independent checker log are frozen under
`scratch/certificates/k11_distance19/`; the proof itself remains on the
proof-producing RunPod under the recorded hash because of its size.

## Exact certified theorem

Let `E0` be the 461 consecutive Johnson edges of
`k11_lower956_upper549.txt`.  There is no 461-edge real subgraph of
`J(11,6)` satisfying all of:

1. exactly two real vertices have degree one and all others have degree two,
   with disconnected cycles permitted;
2. at most nineteen edges of `E0` are absent;
3. the 461 selected rank-five intersection colours are distinct;
4. all 330 rank-seven union colours occur; and
5. the unique omitted rank-five colour is contained in an endpoint vertex.

Therefore every qualifying connected Hamilton path drops at least twenty
seed edges.  Since both edge sets have size 461, its real-edge symmetric
difference from `E0` is at least forty.

This remains a local central-colour theorem.  It does not rule out a candidate
at distance twenty or more, impose connectivity or factorability, or decide
the unrestricted length-465 OR-array problem.

An independent promotion audit re-parsed the CNF, checked every local hash and
terminal checker condition, remotely re-hashed the existing proof, and
re-derived the distance semantics.  It passed; see
`K11_DISTANCE19_PROMOTION_INDEPENDENT_AUDIT.md`, SHA-256
`8f11ae6244eff2007585aa931cabd4523d41f20517d3430677a6c6e06e2ae520`.
