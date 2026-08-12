# `k=17` directed-history v2: canonical propagation rows and reversal WLOG

Date: 2026-08-02  
Status: **PASS for exact construction and the current projection-level reversal symmetry.**  No v2 solver was launched or used in this audit.  No SAT or UNSAT claim is made.

## 1. Frozen inputs and output

The strengthening source is

```text
eca17a64768c35ed43f122fcf4271b4ad7fcb56837c4b083e25e84336c035bf2
  scratch/strengthen_k17_directed_history_master_20260802.cpp
```

It takes the independently audited v1 master

```text
c7bd1ac496a7f6303a334aafd1531ec086faa2fd97a30cd82686bbb1fb7050b6
  marker58_directed_history.cnf
```

and the two blocker banks

```text
9948bd6152774219b93adf7f5476929ad6e1a8a4338b9ddd38504ce47eaf3e51
  c68b.double_fusion.residence_blocks.cnf
3b218d8842b24c03f04416262700093113d764f663795fc6c185d815d6d62560
  cumulative478.blocks.cnf
```

under

```text
/home/amodo/or15/work/root_k17_directed_history_master_20260802
```

and emits

```text
8edea7e353343b420aa60c4d9fa2bb78fc9536c955af4ff0d7cb5a16718402c0
  marker58_directed_history_v2.cnf
```

with exactly

```text
variables  348,971
clauses  3,904,720.
```

## 2. Exact canonical set difference

Every nonempty line of both blocker files was parsed independently.  Each
row has only negative literals in `{-35713,...,-1}`, ends in one zero, has
no trailing token, has no repeated literal after sorting, and is unique as a
canonical literal vector.

The exact counts are

\[
 |B_{316}|=316,\qquad |B_{478}|=478.                     \tag{2.1}
\]

As canonical literal-vector sets, the old bank is a subset of the
cumulative bank:

\[
                         B_{316}\subset B_{478}.          \tag{2.2}
\]

Consequently

\[
                  |B_{478}\setminus B_{316}|=162.        \tag{2.3}
\]

Their exact arity histogram is

```text
arity 1: 12
arity 2:  5
arity 3: 73
arity 4: 72.
```

This is a canonical set difference of sorted literal vectors, not raw-text
comparison.  The v2 body contains those 162 rows in the exact lexicographic
order induced by `std::set<vector<int>>`.

The history master already implies every genuine short-run blocker.  Thus
these 162 rows are propagation strengthening only; they do not change the
intended directed-history projection.  This statement uses the blocker
semantics proved for the displayed authenticated banks.  The present audit
does not independently reconstruct all 478 occurrence certificates.

## 3. Exact header and body identity

The independent stream audit verifies:

1. clauses `1,...,3,904,557` of v2 are exactly the v1 clauses in the same
   order;
2. clauses `3,904,558,...,3,904,719` are exactly the 162 rows in (2.3);
3. the final clause is

   ```text
   204168 0
   ```

4. there is no trailing token; and
5. the variable count stays `348,971`.

Therefore

\[
        3,904,557+162+1=3,904,720                       \tag{3.1}
\]

is exact.  This is not merely a header recount.

## 4. Literal `204168` is the claimed protected direction

The independently replayed directed-history map has header

```text
type variable edge_index primary source_owner target_owner delta
     deleted inserted_target direction
```

Its first two rows are the two orientations of edge index zero, which is a
fixed protected edge (`primary=0`).  They are

```text
variable 204168  direction forward
variable 204169  direction reverse.
```

The v1 orientation clauses impose exactly one of these two literals.  Hence
the final v2 unit fixes the first fixed protected edge forward, exactly as
claimed.

## 5. Reversal is WLOG on the current v2 face

Put

\[
 F_{478}=\text{v1}\ \wedge\
          \bigwedge_{C\in B_{478}\setminus B_{316}} C.   \tag{5.1}
\]

### Theorem 5.1 — projection-level reversal normalization

The formula `F478` is satisfiable if and only if
`F478 and (204168)` is satisfiable.  The latter is the v2 formula.

### Proof

Only the reverse implication needs proof.  Let an assignment satisfy `F478`.
If `204168` is already true, stop.  Otherwise
the exact fixed-edge orientation row makes `204169` true.

Reverse every selected directed quotient component.  Equivalently, replace
each selected arc by the opposite dart of the same undirected edge.  Then:

* every primary factor variable is unchanged;
* fixed and residual facet, owner, cap, protected-edge, and inherited
  component-cut rows are unchanged because they are undirected;
* all 316 old and 162 new blocker rows are unchanged because they contain
  only primary literals;
* one incoming and one outgoing dart remain at every owner; and
* every developed coordinate trace is read in reverse, so its cyclic
  positive-run lengths are unchanged.

By the exact directed-history equivalence in
`MATH_AUDIT_AD_K17_DIRECTED_HISTORY_MASTER_20260802.md`, the reversed
resident cycle cover has a valid history assignment: at every owner simply
record the three preceding insertion labels in the reversed orientation and
the appropriate local `Z_17` frame.  Thus all history clauses can be
satisfied after reversal.  The first fixed edge is now oriented forward, so
`204168` is true.  QED.

The argument works with several quotient components; connectivity is not
needed.  It is an existential projection argument, not a claim that a fixed
literal permutation of the old history variables is a syntactic CNF
automorphism.

### Scope warning

The symmetry remains valid after adding undirected connectivity and a
**nonzero** voltage requirement, since reversal negates voltage and preserves
nonzeroness.  It must be re-audited before adding any signed unit-voltage
normalization, fixed root orientation, one-sided physical opening/collar,
directed source role, or compiler constraint which is not itself
reversal-closed.

## 6. Independent audit artifacts

The independent audit source and result are

```text
6644675f2c7c839bbcfe25579e6a1f2825983e00fd21ee92103d42089981170c
  scratch/audit_ad_k17_directed_history_v2_20260802.cpp
707175eea147b4d239524a2a9c4effc639666495e803ab007ba96ba4f2880a50
  scratch/ad_k17_directed_history_v2_independent_audit_20260802/
    directed_history_v2.independent.audit.json
8587b8f5ce9c461c2263d586fc2ae3ef00cc39879017a5dabd22a8fc991a8846
  scratch/ad_k17_directed_history_v2_independent_audit_20260802/audit.stdout
```

The replay returned

```text
PASS_AD_K17_DIRECTED_HISTORY_V2_INDEPENDENT_AUDIT
novel=162 clauses=3904720
```

The result certifies formula construction and the inputs needed by the
reversal proof.  It does not certify SAT, UNSAT, quotient connectivity,
component voltage, ranks `11+`, source placement, opening/collar semantics,
or compiler feasibility.

As with v1, the strengthening executable itself does not pin input hashes.
The PASS statement is tied to the exact hashes in Section 1.
