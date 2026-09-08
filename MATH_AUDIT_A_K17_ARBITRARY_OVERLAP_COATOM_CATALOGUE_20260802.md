# Audit of the K17 arbitrary-overlap coatom catalogue and Hall obstruction

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Verdict:** PASS for the stated one-transition/native-address face.

## 1. Objects authenticated

The input is the explicit owner-labelled depth-three table

```text
scratch/k17_exact_depth3_owner_payload_table_20260802/
  k17_depth3_owner_payload.tsv
```

with SHA256

```text
029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1
```

Its independent producer-free replay is already frozen with report SHA
`bb2fc1f7eb54e0379af2797b179efdb25b7eb677a826bb0732198134b4cf001f`
and source SHA
`e198b4870f6832a5168aae596686478de38ceed525f7555eca157df0ac6a9aeb`.
The present audit does not reconstruct the Dilworth table; it consumes that
authenticated literal table and independently checks the new overlap
calculus.

The theorem under audit is

```text
MATH_THEOREM_A_K17_ARBITRARY_OVERLAP_COATOM_NORMAL_FORM_AND_FIXED_TABLE_HALL_NOGO_20260802.md
```

with SHA256

```text
fe6334cc57c89d177de8264e0a0c4a5132543f217ebb613e6feee58879a441cf
```

## 2. Proof audit

For a long head row (L_i\subset M_i\subset U_i\subset T_i), an arbitrary
overlap state (h_i=(A,B,L_i)) and a predecessor long state
(h_j=(D,A,B)) force

\[
 B=L_j,quad A\cup B=M_j,quad B\cup L_i=M_i,quad
 M_j\cup L_i=U_i.                                   \tag{2.1}
\]

The consecutive ranks make (M_j=U_i-\{x\}) for a unique (x\in L_i).
Writing (B=(M_i-L_i)\cup Y) then gives
(Y\subseteq L_i-\{x\}).  Finally

\[
 D\cup U_i=T_i,qquad D\cup M_j=U_j                 \tag{2.2}
\]

forces (U_j=(U_i-\{x\})\cup\{z_i\}), where
(z_i=T_i-U_i).  In particular, (D) cannot contain (x), since it already
contains (z_i) and (D\cup M_j) has rank eight.  These deductions are
reversible using the reduced letters

\[
 B=(M_i-L_i)\cup Y,qquad
 A=(U_i-M_i)\cup(L_i-(Y\cup\{x\})),qquad D=\{z_i\}. \tag{2.3}
\]

This proves completeness of the catalogue for arbitrary overlap at the
fixed owner/root/payload projection.  It does not simplify or certify
residence histories attached to redundant literal occurrences.

## 3. Deterministic replay

The verifier is

```text
scratch/a_k17_coatom_split_bridge_20260802/
  audit_a_k17_coatom_split_bridge_20260802.py
```

with SHA256

```text
24fbd650bae6d6e42eb517132e14791df82ca1b9a2943087f194935fc7320c77
```

It performs the following independent checks.

1. Parse all `24,310` rows and verify root uniqueness.
2. For every one of the `18,663` long heads, enumerate every
   (x\in L_i) and (Y\subseteq L_i-\{x\}).
3. Look up the forced predecessor row by its root and require all three
   identities in the coatom criterion.
4. Reconstruct both literal states and assert every suffix union, root,
   shift, and owner equality.
5. Deduplicate the resulting bipartite edge lists.
6. Compute Hopcroft--Karp maximum matchings both on all long heads and on
   the hard bank (|L_i|>1).
7. Derive the alternating-reachability Kőnig vertex cover for the hard bank,
   assert that it covers every edge, and assert that its size equals the
   matching.

The exact output is

```text
PASS
rows=24310 long_rows=18663 hard_heads=18646
coatom_edges=4739 live_suppliers=3658 covered_hard_heads=2239
long_bipartite_matching=2168 long_deficiency=16495
hard_zero_heads=16407
hard_long_matching=2167 short_rows=5647
hard_one_transition_upper=7814 hard_one_transition_defect=10832
hard_min_vertex_cover_sha256=9596de583f6fa461894e450313a1b0b4741c583804b828440425117b0563a029
edge_types=2->5:1,2->6:4,3->4:3,3->5:8,3->6:37,4->3:1,4->4:9,4->5:58,4->6:187,5->3:14,5->4:46,5->5:224,5->6:465,6->1:1,6->2:2,6->3:50,6->4:172,6->5:545,6->6:2912
```

The hard-head upper bound deliberately grants all `5,647` short rows
universal compatibility.  Hence

\[
                         18,646-(2,167+5,647)=10,832
\]

is proof-safe without enumerating a single short-row state.

The row-support lower bound is the standard matching Lipschitz argument.
If the incidence graph is changed only at `q` row identities, the changed
edge set is incident with at most `q` left and `q` right copies.  Removing
these copies from a new matching leaves an old matching, so its size can
increase by at most `2q`; for predecessor-side-only changes the increase is
at most `q`.  Applied to the `10,832` deficit, this gives the exact rounded
lower bounds `5,416` and `10,832`, respectively.

## 4. Exact scope and false extrapolations

The no-go covers all of the following simultaneously:

* the frozen K17 owner/root/payload assignment;
* one depth-three transition per row;
* native suffix addresses (1,2,3) for every long payload; and
* arbitrary coordinate overlap/repetition inside the three state letters.

It does **not** cover:

* redistributing payload targets among several owner rows;
* a larger physical macro whose contraction is not one ordinary row edge;
* rechaining the 65,535 targets or changing their owner attachment;
* a non-native address realization of a long chain; or
* another dimension.

The factor-critical conveyor is therefore not contradicted.  Rather, this
audit proves that its local modules cannot be obtained by merely grouping
these fixed rows and enriching their ordinary three-letter states.  A valid
bridge must leave this face before quotient Hall and topology become the
remaining tests.

Arbitrary-width upper shadows and common-cap/compiler compatibility were not
used and remain separate downstream gates.
