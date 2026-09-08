# K17 common-basis outer oracle and the typed-socket column gate

**Date:** 2026-08-02  
**Status:** exact static counts, exact oracle reduction, and exact
one-column extension criterion.  No joint `1S-ROTS(17)` solution is claimed.

## 1. Exact direct size

Put

\[
 L=\binom{[17]}1\cup\cdots\cup\binom{[17]}6,
 \qquad M=\binom{[17]}7,
 \qquad R=\binom{[17]}8.
\]

Then

\[
              (|L|,|M|,|R|)=(21777,19448,24310).
\]

The strict-containment edge counts are

\[
\begin{aligned}
 |E(L,M)|
   &=\sum_{t=1}^6\binom{17}{t}\binom{17-t}{7-t}
     =19448(2^7-2)=2\,450\,448,\\
 |E(L,R)|
   &=\sum_{t=1}^6\binom{17}{t}\binom{17-t}{8-t}
     =24310\sum_{t=1}^6\binom8t=5\,980\,260,\\
 |E(M,R)|&=19448(17-7)=194\,480.
\end{aligned}
\]

Thus a literal static edge formulation has

\[
             8\,430\,708+194\,480=8\,625\,188             \tag{1.1}
\]

primary matching variables before any address, occurrence, supplier, or
chronology variable.

For calibration, encode each low-target row, rank-eight receiver row, and
rank-seven-target row as exactly one and each rank-seven low-receiver row as
at most one, using a separate Sinz chain for every row.  The four row
families contain `17,250,376` incidences and `84,983` rows.  Therefore this
standard encoding has exactly

\[
\begin{aligned}
 17\,250\,376-84\,983&=17\,165\,393
       &&\text{sequential auxiliaries},\\
 25\,790\,581&&&\text{static variables in total},\\
 51\,411\,196+65\,535&=51\,476\,731
       &&\text{static clauses}.                         \tag{1.2}
\end{aligned}
\]

These counts do not prove that every carefully engineered flat encoding
exceeds 8 GiB.  They do show that a flat launch has no audited budget for
the much larger occurrence-DNF, flag, supplier, and chronology layers.  The
proof-safe implementation should therefore retain matching oracles rather
than expand (1.1).

The independent counter and fixture replay are

```text
scratch/audit_k17_common_basis_outer_edge_counts_20260802.cpp
  fb7958841b93de769ecbd43f39d994a1ee2a480df5c20cb89d0da4ddabf9b176

scratch/k17_phase0_retained_witness_private_basis_20260802/
  common_basis_outer_size.audit.json
  06a3e8da8f4c50f3c2c539cd2c527076b0eee5fa4ec469797a3fe08af72c192f
```

It also replays the protected private-H table as `4862` direct low chains,
`2533` direct rank-seven chains, and `16915` long chains.

## 2. The static oracle

Let `M_L` be the transversal matroid on ground set `M dotcup R` presented by
the low-containment graph.  Let `M_7` be the transversal matroid on `R`
presented by the `M--R` containment graph, and put

\[
                  N=M_7^*\oplus U_{16915,M}.          \tag{2.1}
\]

Both matroids have rank `21777`.  By the common-basis theorem, a receiver
set `C` supports an exact no-singleton three-level table if and only if it
is a common basis of `M_L` and `N`.

The two independence oracles are literal matching oracles:

* `X` is independent in `M_L` iff the receiver vertices in `X` can be
  matched to distinct low targets;
* `X` is independent in `N` iff
  `|X cap M|<=16915` and

  \[
       r_{M_7}(R-(X\cap R))=19448,                    \tag{2.2}
  \]

  which is again one containment matching.

Consequently ordinary weighted matroid intersection is an exact outer
algorithm for an additive receiver cost

\[
                         w(C)=\sum_{v\in C}w_v.        \tag{2.3}
\]

Protected receiver elements can be handled by deletion and contraction.
The returned basis must be decoded with two matching witnesses: one low
matching into `C`, and one rank-seven matching into
`R-(C cap R)`.

### Corollary 2.1 (specialized one-flow implementation)

For this presented K17 pair, generic weighted matroid intersection is not
needed for the static receiver objective.  In the augmented matching graph
of Section 4, put cost `w(m)` on every low edge `l->m`, cost `w(r)` on
every direct low edge `l->r`, and cost zero on every `m->r` and
dummy-bank edge.  A minimum-cost perfect matching then has cost exactly

\[
       \sum_{m\in C\cap M}w(m)+\sum_{r\in C\cap R}w(r)=w(C), \tag{2.4}
\]

and returns the low and rank-seven matching witnesses at the same time.
The `2533` symmetric dummies are one capacity-`2533` bank with one
unit-capacity zero-cost arc to every middle receiver; their complete
bipartite expansion is unnecessary.

If the desired cost is instead on complement roots `B=R-(C cap R)`, put
that cost on the `m->r` edges.  Since every root is used exactly once, a
mixed `C_R/B` root objective differs from an equivalent one-shore objective
only by the corresponding fixed root-cost constant.

Thus the preferred static implementation is a single min-cost flow.  The
matroid statement remains useful for deletion/contraction language and for
abstract receiver-basis exchange.  Both implementations have exactly the
same receiver-only scope.

### Scope of the weights

Equation (2.3) is proof-safe only for data determined by the receiver
element itself.  It does **not** price any of the following:

* which low target is matched to a receiver;
* which rank-seven target is matched to a root;
* a predecessor/successor occurrence;
* an address or long flag;
* a supplier identity; or
* a common-state socket DNF.

Those are properties of the two matching representatives, not of `C`.
Replacing them by a minimum or union price on `C` is only a relaxation.

## 3. Exact representative-level branch flows

Let `x` denote the rank-seven matching and `y` the low matching.

### Fix `x`

Let `R_0` be the roots unused by `x`.  Delete every forbidden direct
`L--R` occurrence.  If the selected edge out of `m` has no admissible
middle-short ticket, require `m` to receive a low predecessor.  The residual
`y` problem is exactly a bipartite matching saturating

1. every low target;
2. every root of `R_0`; and
3. every mandatory middle receiver.

This is one lower-bounded max flow.  Failure returns an exact Hall shore.

### Fix `y`

Let `C_R` be the roots used by `y`, and let `S_M` be the middle vertices not
used by `y`.  The residual `x` problem is a perfect matching

\[
                  M\longrightarrow R-C_R,             \tag{3.1}
\]

with edges out of `S_M` restricted to those admitting a middle-short
ticket.  Both shores in (3.1) have size `19448`; saturating only the left
shore without checking this root identity is not a sufficient audit.

This yields the proof-safe outer loop:

1. weighted common-basis exchange for receiver-only prices;
2. fixed-`x` low flow;
3. fixed-`y` rank-seven flow;
4. occurrence-DNF and shared-flag branching; and
5. residual long--long and selected-state supplier Hall separation.

Every learned cut must cite the selected representation edges on which its
neighborhood depends.  A Hall cut from one fixed table is not automatically
a cut on the whole common-basis fibre.

## 4. Exact typed-socket column oracle

There is a particularly small exact oracle for a proposed literal socket
column.

Construct the augmented bipartite graph

\[
 \mathcal G^+=
 (L\dot\cup M\dot\cup\Delta, M\dot\cup R),          \tag{4.1}
\]

where `|Delta|=2533`.  Use all strict `L--M`, `L--R`, and `M--R`
containment edges, and join every dummy to every middle receiver.  The dummy
edges should be implemented by one capacity-`2533` bank, not materialized.

### Lemma 4.1 (perfect matching equivalence)

Perfect matchings of `G+` are in bijection with labelled-dummy versions of
exact no-singleton three-level tables.

#### Proof

Every real left target is used once.  Every root on the right is used once.
A middle receiver is used either by a low target, producing a long chain,
or by one dummy, producing a direct middle--root chain.  Since there are

\[
        (|M|+|R|)-(|L|+|M|)=|R|-|L|=2533
\]

more right vertices than real left vertices, exactly all dummy supplies are
used.  Forgetting dummy labels gives an exact table.  The reverse
construction is immediate. \(\square\)

A literal ticket `g` carries a finite static footprint `P(g)`:

* a long chain `l-m-r` contributes `l->m` and `m->r`;
* a direct low chain `l-r` contributes `l->r`;
* a direct middle chain `m-r` contributes `m->r` and one dummy-bank unit at
  receiver `m`.

The predecessor, short, and successor roles of a common-state socket give
the union of their footprints.  The address, flag, and five-cell witness
remain labels on the same ticket; they are not inferred from the static
edges.

For a partial matching `P` in `G+`, define

\[
 p_P(X)=|V_{\rm left}(P)\cap X|,
 \qquad q_P(Y)=|V_{\rm right}(P)\cap Y|.             \tag{4.2}
\]

### Theorem 4.2 (protected one-ticket extension)

Let `P_0` be a protected bank of already selected literal chain footprints.
A proposed ticket `g` has a static extension to an exact three-level table
if and only if

1. `P_0 union P(g)` is a partial matching in `G+`; and
2. after deleting all its left and right endpoints, the residual augmented
   graph has a perfect matching.

Equivalently, for every left set `X`,

\[
 q_{P_0\cup P(g)}(N(X))-p_{P_0\cup P(g)}(X)
       \le |N(X)|-|X|.                                \tag{4.3}
\]

#### Proof

The first condition is necessary for the prescribed edges to coexist.
Conditional on it, an extension is exactly a perfect matching of the
residual graph.  Hall's theorem gives condition 2 and, after expanding the
deleted endpoints, (4.3). \(\square\)

The theorem is prospective: the matching oracle chooses the rest of the
table around `g`.  It is not a fixed-table test.  It is therefore the exact
column-validity oracle for one occurrence-labelled socket in a
branch-and-Benders implementation.

It is also strictly stronger than contracting only the receiver element in
`M_L` and `N`.  A literal chain ticket fixes its representing edge.  In the
two-presentation language one must delete the fixed low witness and/or
rank-seven source together with the used receiver/root, then test the
resulting common-basis minors.  This presentation-minor formulation and the
residual perfect-matching test above are equivalent descriptions of the
same operation.  The independent derivation is
`MATH_AUDIT_K_K17_COMMON_BASIS_BRANCH_FLOW_AND_LITERAL_ONE_TICKET_EXTENSION_20260802.md`
(SHA-256
`2f0c0ad2661a3cf564e9a26c1823b0de2df6af64a293855b91312f38eefa9bfa`).

For several selected tickets the same theorem applies to the union of their
footprints.  Selecting the tickets jointly is not a matching problem: each
ticket is a bundle of static edges, endpoint ports, and state literals.  The
natural triangle submatrix has determinant two.  Thus the correct
implementation branches on ticket columns and calls the residual matching
oracle; it does not append marginal socket rows to the common-basis LP and
claim total unimodularity.

## 5. Protected private-H baseline and exact live gate

The independent materializer

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  materialize_k17_phase0_private_h_bank_20260802.cpp
  d23b09929ce5ed98c0261b295b4553c75b6c333104509cd5ec4a67f7a7fb5191
```

emits a table byte-for-byte identical to the authoritative protected table,
SHA-256

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
```

Its selected-state projection is

\[
 P=16796/16898,qquad Z=4708,qquad\Omega=3878,       \tag{5.1}
\]

with Hall shore `109 -> 7` and zero split

\[
                  3187\ ({\rm fixed/P2})+1521\ (F)+0\ (H).
\]

Thus the protected bank closes the `1748` H-short ticket rows but not the
remaining fixed/free rows.  No complete post-role-move catalogue of those
`3899+1748=5647` common-state DNFs currently exists.

The exact live finite gate is therefore:

> choose a common basis and its two matching representatives, retain the
> protected H tickets, choose one occurrence-labelled DNF for every one of
> the remaining 5647 short roles with common endpoint flags, complete the
> 9520 residual long--long arcs, and satisfy the selected-state supplier
> Hall family.

Receiver-only common-basis weights cannot replace this gate.  Socket
columns must be regenerated after a representative edge or role changes.

## 6. Marker scope

The determinant-two face does have one exact local repair: one odd physical
bridge plus its complementary even configuration.  The bridge must also
have zero reset curvature and satisfy (4.3).  This is the minimal
one-marker lemma proved in
`MATH_THEOREM_K_ROTS_MINIMAL_PARITY_MARKER_RESET_CURVATURE_AND_HALL_20260802.md`.

It does **not** imply a dimension-uniform `O(1)` marker bank.  A direct sum
of `t` parity cells has quotient `(Z/2)^t`, and bounded-support marker modes
need at least the corresponding two-primary rank (or the covering lower
bound).  The global master must therefore track literal odd-ticket residue;
an abstract marker label or receiver weight is insufficient.

## 7. Resource and scope ledger

The successful H100 preflight snapshot before this audit reported `205 GiB`
available RAM and `23 GiB` free under `/home/amodo/or15/work`.  No heavy
common-basis or socket solve was launched.  This note deliberately replaces
the unbudgeted flat master by matching oracles.

Still outside scope are one chronology/connectivity, literal cyclic-cell
replay, residence, arbitrary upper shadows, common-cap/compiler feasibility,
and the final word.
