# RF495 three-chain separator Hall theorem and forced two-chain coupling

Date: 2026-07-30  
Status: unconditional for the three one-chain faces of the authenticated
seed-5/self RF495 lead.  The later companion
`MATH_THEOREM_K_K16_RF495_ORIENTED_ANCHOR_HALL_FIBRE_NOGO_20260730.md`
strengthens the same endpoint idea and closes the entire fixed fibre.

## 1. Exact setting

The eighteen editable cells split into three disjoint chains

\[
C_L=[0,3],\qquad C_M=[4,12],\qquad C_R=[13,17]
\]

of lengths (4,9,5).  The seventy editable supports are exactly their
nonempty intervals:

\[
\binom52+\binom{10}2+\binom62=10+45+15=70.
\]

A physical provider is a triple ((T,F,I)): (T\subseteq[16]) is its target,
(F\subseteq T) is the fixed-body OR, and (I) is a nonempty interval in
one chain.  Cell masks (X_p\ne\varnothing) realize the provider when

\[
X_p\subseteq T\quad(p\in I),
\qquad
F\cup\bigcup_{p\in I}X_p=T.                         \tag{1.1}
\]

The authenticated atlas contains 6,089 potential literal physical intervals.
Eight duplicate intervals collapse to identical semantic triples
`(target,fixed OR,free positions)`, leaving 6,081 semantic provider rows.
Sections 2, 4, and 5 may use the semantic table.  The endpoint theorem in
Section 6 is checked against the complete 6,089-row literal table, so no
physical endpoint is silently discarded.

In a one-chain face, the other two chains retain their authenticated lead
values.  A residual target not delivered by either frozen chain is called
mandatory for the free chain.  Exact replay gives

\[
|R_L|=17,\qquad |R_M|=40,\qquad |R_R|=19.            \tag{1.2}
\]

## 2. The correct Hall dual: labelled blocker covers

### Theorem 2.1 (maximal intersections)

Fix one provider (a=(T_a,F_a,I_a)) for each selected target and put

\[
U_p=\bigcap_{a:p\in I_a}T_a,
\qquad
D_a=T_a\setminus F_a,                                \tag{2.1}
\]

with (U_p=[16]) if no selected interval contains (p).  The selected
providers have a common nonzero integral realization if and only if

\[
U_p\ne\varnothing\quad\hbox{for every }p,             \tag{2.2}
\]

and

\[
D_a\subseteq\bigcup_{p\in I_a}U_p
\quad\hbox{for every }a.                              \tag{2.3}
\]

When these conditions hold, the componentwise maximal assignment
(X_p=U_p) is a realization.

#### Proof

Every realization satisfies (X_p\subseteq U_p), proving necessity of
(2.2).  Equation (1.1) gives
(D_a\subseteq\bigcup_{p\in I_a}X_p\), proving (2.3).  Conversely,
(U_p\subseteq T_a) for (p\in I_a), while (2.3) supplies all of
(T_a\setminus F_a).  Hence

\[
F_a\cup\bigcup_{p\in I_a}U_p=T_a,
\]

so (X_p=U_p) works.  ∎

For a coordinate (b), define its blocked and permitted positions by

\[
B_b=\bigcup_{a:b\notin T_a}I_a,
\qquad P_b=C\setminus B_b.                            \tag{2.4}
\]

Then (b\in U_p) exactly when (p\in P_b).  Thus (2.2)--(2.3) are
equivalent to

\[
\forall p\ \exists b:\ p\in P_b,                    \tag{2.5}
\]

and, for every demanded pair (b\in D_a),

\[
I_a\cap P_b\ne\varnothing.                           \tag{2.6}
\]

This is the exact Hall analogue for OR cells.  A failure of (2.6) has an
interval cover of (I_a) by (b)-omitting blockers; a greedy minimal cover
uses at most (|I_a|) rows.  A dead cell in (2.5) has at most sixteen
coordinate-labelled blocker witnesses.  Support-only Hall or consecutive-
ones total unimodularity is not enough, because cells are shareable and the
target intersections in (2.1) retain coordinate labels.

## 3. Two one-dimensional obstruction lemmas

### Lemma 3.1 (antichain endpoint Hall)

Let (mathcal A) be an antichain of targets, and let (E(T)) be the set of
right endpoints of all physical providers available to (T) in one chain.
Every realization induces a matching of (mathcal A) into the endpoint
sets.  Consequently

\[
|mathcal X|\le
\left|\bigcup_{T\in\mathcal X}E(T)\right|
\quad(\mathcal X\subseteq\mathcal A).                 \tag{3.1}
\]

#### Proof

Two literal intervals with the same right endpoint are nested.  Their ORs
are therefore comparable by inclusion.  Two distinct members of an
antichain cannot use that same endpoint.  The selected endpoints are an SDR,
and ordinary Hall gives (3.1).  ∎

Distinct sets of one rank are automatically an antichain.  Notice that the
endpoint quotient is essential: ordinary target-to-provider Hall may be
perfect even when (3.1) fails.

### Lemma 3.2 (blocked separator and endpoint equality)

Consider an (n)-cell chain with physical outputs

\[
F\cup\bigcup_{p\in I}X_p
\]

over nonempty intervals (I).  Let (L\cup\{Z\}) be distinct mandatory
targets.  Suppose:

1. every nonzero fixed OR contains a coordinate (b);
2. every target in (L\cup\{Z\}) omits (b);
3. (Z) contains a coordinate (z) omitted by every target in (L).

If one common assignment of the (n) cells simultaneously realizes every
target in (L\cup\{Z\}), then

\[
|L|\le\binom n2.                                      \tag{3.2}
\]

If equality holds, (L) must have a greatest element under inclusion.

#### Proof

Condition 1 and omission of (b) force every one of these targets to use
(F=0).  Choose a cell (p) which supplies (z) to the interval realizing
(Z).  Every interval realizing a member of (L) avoids (p).  With
zero-based (p), the number of intervals avoiding it is

\[
\binom{p+1}{2}+\binom{n-p}{2}\le\binom n2.            \tag{3.3}
\]

Distinct outputs require distinct intervals, proving (3.2).  Equality in
(3.3) forces (p) to be an endpoint and uses every interval of the remaining
((n-1))-cell chain.  Its full interval has OR containing the OR of every
other interval, so the corresponding target is a greatest element of (L).
∎

## 4. Left chain: a sharp separator obstruction

Every nonzero fixed OR on the left chain is one of

```text
3104, 318c, 319c, 339c, 739c, 739d, 73bd,
```

and hence contains blocker bit `0x2000`.  The seven mandatory targets

\[
L_L=\{1846,18e6,18e7,1986,19c6,19e6\},
\qquad Z_L=9e20                                      \tag{4.1}
\]

all omit `0x2000`.  Target (Z_L) contains separator bit `0x8000`, while
every member of (L_L) omits it.  Here

\[
|L_L|=6=\binom42,
\]

but

\[
\bigcup L_L=19e7\notin L_L.                          \tag{4.2}
\]

Lemma 3.2 proves the left-only face impossible.

There is also an independent certificate which does not use interval
geometry.  Plain OR service by (m) cells gives a Boolean rectangle cover
of the target-by-coordinate incidence matrix with at most (m) rectangles.
The five diagonal entries

\[
(18e7,0),\ (9e20,15),\ (1846,6),\ (1986,8),\ (18e6,5) \tag{4.3}
\]

form a fooling set: each is a 1-entry and, for every pair, at least one cross
entry is zero.  No rectangle covers two of them.  Hence at least five cells
are needed, independently confirming that four left cells cannot suffice.

## 5. Right chain: the same theorem at the next scale

Every nonzero right-chain fixed OR is one of

```text
8a4a, 8a6a, 8a6b, aa6b,
```

so all contain blocker bit `0x0008`.  Put

\[
\begin{split}
L_R=\{&18e7,1e20,1e64,1e74,8b42,9b00,9b52,\\
      &9b54,9b56,9e20\},
\qquad Z_R=3de7.                                      \tag{5.1}
\end{split}
\]

All eleven targets are mandatory and omit `0x0008`; (Z_R) contains
separator `0x2000`, omitted by every member of (L_R).  Now

\[
|L_R|=10=\binom52,
\qquad
\bigcup L_R=9ff7\notin L_R.                          \tag{5.2}
\]

Lemma 3.2 closes the right-only face.

## 6. Middle chain: a deficiency-one endpoint Hall core

The following ten mandatory targets are distinct rank-eight sets:

```text
18e7, 1c67, 1f54, 9867, 98e6,
99c6, 9c63, 9e54, 9e64, b986.
```

The ten targets have exactly 812 rows in both the semantic and complete
literal tables: none of the eight global duplicate collapses meets this core.
Of these, 558 are middle-chain provider rows.  Every such literal interval
ends at one of exactly nine
physical positions

\[
E=\{6434,6435,\ldots,6442\}.                          \tag{6.1}
\]

Their 254 providers on the other two chains all fail under the frozen lead,
which is precisely why the ten targets are middle-mandatory.  Lemma 3.1 now
gives the Hall inequality

\[
10\le |E|=9,                                          \tag{6.2}
\]

a contradiction.  Thus the middle-only face is impossible.  The core has
literal endpoint deficiency one; it is not a count of (Q)-classes.

## 7. Coupling conclusion and boundary

Combining Sections 4--6 proves:

> **Three-chain coupling theorem.**  No word obtained from the authenticated
> seed-5/self RF495 lead by changing cells in only one of its three collar
> chains covers all seventy residual targets.  Every completion of this lead
> must change at least two chains together.

This is stronger than the previous 810,000-state left closure census and
requires no SAT solve.  Standing alone, Sections 4--6 only force a two-chain
move.  The companion oriented-anchor theorem closes all two-chain faces and
the unrestricted exact-one formula for this fixed fibre.  Neither theorem
decides another parent pair, another layout, or global K16 equality.  The
acceptance gate for any different candidate remains literal coverage of all
65,535 nonzero masks at length 12,873.  Exactness of the diagnostic
(D^3) middle row is neither assumed nor required.

The old seed-4 root proof and the corrected sharp-root Q-only cut are not used
anywhere in this argument.  The unrestricted seed-5 exact-one run has separate
execution ownership and is not duplicated here.

## 8. Audit artifacts

The light independent replay is

```text
scratch/audit_k16_rf495_three_chain_separator_hall_20260730.py
scratch/k16_rf495_three_chain_separator_hall_20260730.audit.json
```

It reconstructs the three mandatory families from the frozen lead, checks
all raw fixed-OR families, verifies both separator applications, verifies the
five-entry Boolean fooling set, and compares all 812 semantic core rows with
all 812 literal core intervals and their physical endpoints.  It pins the
authenticated input hashes, verifies that the qmask family is exactly the 70
nonempty intervals of the three chains, performs no Cartesian cell search,
and launches no solver.

## 9. Exact mandatory families

For reproducibility, the full one-chain mandatory sets reconstructed by the
audit are:

```text
left4 (17):
1846 18e6 18e7 1986 19c6 19e6 3186 318e 319e
339e 3986 398e 39c6 39e6 3bde 3de7 9e20

middle9 (40):
1866 1867 18e7 1c63 1c67 1e40 1e54 1f54 3de7 8000
9846 9866 9867 98e6 98e7 9986 99c6 99e6 9c63 9c67
9e20 9e40 9e54 9e64 9e74 9f54 b104 b186 b18e b19c
b19e b39c b39e b986 b98e b9c6 b9e6 bbde bde7 f3bd

right5 (19):
18e7 1e20 1e64 1e74 3de7 8b42 8b4a 8b6a 8b6b 9b00
9b4a 9b52 9b54 9b56 9b5a 9b6a 9b7b 9e20 ab6b
```

These are target masks, not quotient labels.  The smaller sets in Sections
4--6 are the literal obstruction cores.

## 10. Frozen hashes and scope summary

```text
semantic incidence  a3ca5b14a5e6286cbcb96e6ca3c827979a525f697eabf6f0704c4fcde982113c
literal intervals   c8f7381486c0412f9f3d34a724d6bbfdc60c210fbf1a2bb2aaa647fad3f0e6dc
lead cells          6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
primary audit       bb798d4fcc361811b09798f225f15d4b974bebdbcaf0111be3c5c28adfa2e059
primary audit JSON  b08d43b2e54079fb30612b0c71be5f0494d23248e556315eb7dc03225dd47bd4
independent audit   9b536f6a4ac7ff852de7c1e7947919ffa807a9951b2f4075651615b90dc69351
independent JSON    b1c1698fa5909babfadec63f4c031fca8b139ba100d3a3fd92c843f70c825b58
```

The theorem in Sections 4--7 is the requested standalone closure of all
three one-chain faces.  The independent audit also verifies the later
oriented-anchor strengthening, but that broader conclusion and its exact
scope are stated in the companion theorem rather than silently imported
here.
