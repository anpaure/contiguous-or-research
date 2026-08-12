# Active `k=17` directed-history `v499`: independent construction replay

Date: 2026-08-02  
Status: **PASS for the exact active-file construction and reversal WLOG.**  The active solver process was not launched, stopped, or otherwise changed by this audit.  No SAT or UNSAT claim is made.

## 1. Scope correction and frozen files

The previously audited `v2` file used `cumulative478.blocks.cnf`.  It is not
the formula currently being solved.  The active formula is instead

```text
05787aa7b9676da8f76f9523f48609127781656e5aeb455b7fd01b71ed8765ce
  /home/amodo/or15/work/root_k17_directed_history_master_20260802/
    marker58_directed_history_v499.cnf
```

built from

```text
c7bd1ac496a7f6303a334aafd1531ec086faa2fd97a30cd82686bbb1fb7050b6
  marker58_directed_history.cnf
9948bd6152774219b93adf7f5476929ad6e1a8a4338b9ddd38504ce47eaf3e51
  c68b.double_fusion.residence_blocks.cnf
5c30260ef5202100aed5b7f91d3ac9d46e8dd3b104e764b854333b9be0d63845
  cumulative499.blocks.cnf
eca17a64768c35ed43f122fcf4271b4ad7fcb56837c4b083e25e84336c035bf2
  scratch/strengthen_k17_directed_history_master_20260802.cpp.
```

The builder's own audit text has SHA-256

```text
b37c723e07d8170846939c614b1eb5068d148cef1bb7c54792996707660c4c03
  marker58_directed_history_v499.audit.txt.
```

PID `452525` was observed running the displayed `v499` file.  This replay did
not launch a second solver.

## 2. Exact canonical bank difference

Both bank files were independently parsed to canonical sorted literal
vectors.  Every row is nonempty, contains only negative primary literals in
`{-35713,...,-1}`, has no repeated literal, and has no token after its
terminating zero.  Every canonical row is unique.

The exact result is

\[
 |B_{316}|=316,\qquad |B_{499}|=499,\qquad
 B_{316}\subset B_{499}                                  \tag{2.1}
\]

as canonical literal-vector sets, and therefore

\[
                   |B_{499}\setminus B_{316}|=183.       \tag{2.2}
\]

The 183 new rows have exact arity histogram

```text
arity 1: 13
arity 2:  6
arity 3: 81
arity 4: 83.
```

This is not a raw-text subset claim: literal order in a row is irrelevant and
is normalized before comparison.

## 3. Exact active formula body

The independent stream replay proves all of the following.

1. The first `3,904,557` clauses of `v499` equal the complete v1 body,
   clause for clause and literal for literal.
2. The next 183 clauses are exactly the set difference (2.2), in canonical
   `std::set<vector<int>>` order.
3. The final clause is exactly

   ```text
   204168 0
   ```

4. There is no trailing token.
5. The header is exactly

   ```text
   p cnf 348971 3904741
   ```

Indeed,

\[
                   3,904,557+183+1=3,904,741.            \tag{3.1}
\]

The independently replayed arc map identifies `204168` as the forward dart
of fixed protected edge zero and `204169` as its reverse dart.  V1 imposes
exactly one of this pair.

## 4. The symmetry unit is WLOG on this face

Let

\[
 F_{499}=\text{v1}\ \wedge\
          \bigwedge_{C\in B_{499}\setminus B_{316}} C.   \tag{4.1}
\]

Then

\[
 F_{499}\text{ is satisfiable}
 \quad\Longleftrightarrow\quad
 F_{499}\wedge(204168)\text{ is satisfiable}.            \tag{4.2}
\]

The right-hand formula is precisely the active `v499` file.

### Proof

The reverse implication is immediate.  For the forward implication, start
with a model of `F499`.  If `204168` is true, stop.  Otherwise the fixed-edge
orientation clauses force `204169`.

Reverse every selected directed quotient component, or only the component
containing fixed edge zero.  All undirected primary variables remain fixed.
Hence the resource base, the inherited primary component cuts, and all 499
primary blocker rows remain satisfied.  Incoming and outgoing degree one are
interchanged.  Every developed cyclic coordinate trace is reversed, so all
positive-run lengths are unchanged.

By the exact history equivalence proved in
`MATH_AUDIT_AD_K17_DIRECTED_HISTORY_MASTER_20260802.md`, the reversed
resident factor admits a fresh satisfying history assignment obtained by
recording the preceding three insertion labels in the reversed chronology.
The first protected edge is now forward.  This proves (4.2).  QED.

This is an existential projection symmetry, not a claimed fixed permutation
of the old history literals.  Connectivity is unnecessary.  A later nonzero
voltage row is reversal-closed because voltage changes sign, but a signed
unit-voltage gauge, fixed directed root, one-sided collar/source role, or
non-reversal-closed compiler constraint must re-audit the unit.

## 5. Independent artifacts and exclusions

The fail-closed independent audit is

```text
6500fb38efdaed58f214f64ceaf259a83364ea38efd1e83db78a1a7d57ca991b
  scratch/audit_ad_k17_directed_history_v499_20260802.cpp
f79ac7957ba778f17f693720b173cd300e594aaf6fe0aa5ae511aa2e868b1d86
  scratch/ad_k17_directed_history_v499_independent_audit_20260802/
    directed_history_v499.independent.audit.json
23e309ec96aa376d00d5147de15fbc83d7159b6ec3fbf8a1a3cddcc69df7bd00
  scratch/ad_k17_directed_history_v499_independent_audit_20260802/
    audit.stdout.
```

It returned

```text
PASS_AD_K17_DIRECTED_HISTORY_V499_INDEPENDENT_AUDIT
novel=183 clauses=3904741.
```

The strengthening executable itself does not pin input hashes or the
expected `316/499/183` counts; the independent audit does.  A newer
`cumulative504` bank is not part of the active file and is not used in this
PASS statement, even if its rows are logically implied by the history
master.

The active formula still has the v1 scope: exact loopless cyclic positive
depth-three residence on the frozen round-one strengthened cycle-cover face,
but no complete quotient-connectivity condition, no nonzero-voltage row, no
literal opening/collar, no ranks `11+`, and no source/compiler/common-cap
gate.  The running process has no theorem status until it emits a result and
that result receives the appropriate model or proof audit.
