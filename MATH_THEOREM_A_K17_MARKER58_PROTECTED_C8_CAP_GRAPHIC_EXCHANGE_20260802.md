# `k=17` marker58: protected `C8` cap--graphic exchange calculus

**Date:** 2026-08-02  
**Status:** exact symbolic theorem and light audit of the frozen factor.  No
`C8` catalogue was enumerated and no SAT instance was built or solved.

## 1. Frozen object and scope

Let

```text
scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv
```

be the factor of SHA-256

```text
0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e.
```

Write `O` for the rank-nine owners and `L` for the rank-eight colours.
For every `C in L`, the factor has one owner edge

\[
                    e_C=\{A_C,B_C\},\qquad A_C\cap B_C=C.       \tag{1.1}
\]

Every owner has degree two and every colour occurs once.  There are
`24,310` owner edges.  The set `P` of protected marker-path edges has
`3,944` distinct colour rows, leaving

\[
                         24,310-3,944=20,366                     \tag{1.2}
\]

mutable colour rows.

For a rank-ten cap `U`, let

\[
 \lambda_F(U)=|\{C:A_C\cup B_C=U\}|.                            \tag{1.3}
\]

The authenticated ledger has `13,307` distinct caps, `6,141` missing
caps, `11,003` repeat units, and `1,179` components.

This note concerns one atomic simple `C8` exchange in this factor.  It does
not assert that a simultaneous cap-gaining merger exists in the frozen
factor, and it makes no chronology, residence, rank-eleven-and-higher, or
compiler claim.

## 2. The protected alternating exchange

Regard the factor as the selected incidence set

\[
 I_F=\{(C,A_C),(C,B_C):C\in L\}
\]

in the rank-eight/rank-nine Boolean incidence graph.  Thus every vertex on
both shores has selected degree two.

Let `C_0,...,C_3` be the lower vertices of a simple incidence `C8`, in
cyclic order, and put

\[
 T_i=C_i\cup C_{i+1}\quad(i\bmod4).                             \tag{2.1}
\]

Fix the active phase in which `(C_i,T_i)` is selected and
`(C_i,T_{i-1})` is unselected.  Let `R_i` be the other selected owner at
`C_i`.  The atomic toggle is

\[
 (C_i,T_i)\longmapsto(C_i,T_{i-1})\qquad(0\le i<4).             \tag{2.2}
\]

Equivalently, in the owner factor it replaces

\[
 e_i^-=\{R_i,T_i\}\quad\hbox{by}\quad
 e_i^+=\{R_i,T_{i-1}\}.                                       \tag{2.3}
\]

### Lemma 2.1 (factor and protection)

The toggle (2.2) preserves every rank-eight colour and degree two at every
rank-nine owner.  It preserves all `3,944` protected marker edges if and
only if

\[
                         \{C_0,C_1,C_2,C_3\}\cap P=\varnothing. \tag{2.4}
\]

Here `P` denotes the protected colour rows.

#### Proof

At each `C_i`, one selected incidence is deleted and one is added.  At each
`T_i`, the incidence at `C_i` is deleted and the incidence at `C_{i+1}` is
added.  All other degrees are unchanged.

At a changed row, `T_i` and `T_{i-1}` are distinct and the owner pair in
(1.1) changes, so a protected edge on that row is destroyed.  Conversely,
if (2.4) holds, both selected incidences at every protected colour row are
literally unchanged.  This remains true when an endpoint owner of a changed
unprotected edge lies on a protected path.  QED.

Thus the marker paths may be contracted to fixed supervertices when
testing topology: contraction does not change component count and (2.2)
does not alter an internal protected edge.

## 3. Exact cap delta

Define the four old and new caps

\[
 U_i^-=R_i\cup T_i,
 \qquad
 U_i^+=R_i\cup T_{i-1},                                      \tag{3.1}
\]

and their multiplicities inside the packet

\[
 p_U=|\{i:U_i^-=U\}|,
 \qquad
 q_U=|\{i:U_i^+=U\}|.                                       \tag{3.2}
\]

Then the complete rank-ten multiplicity update is

\[
                      \lambda_{F'}(U)=\lambda_F(U)-p_U+q_U.   \tag{3.3}
\]

Only the at most eight named values in (3.1) must be inspected.

Put

\[
 H(Q)=|\{U:\lambda_F(U)=0, q_U>0\}|,                         \tag{3.4}
\]

\[
 L(Q)=|\{U:\lambda_F(U)>0, \lambda_F(U)-p_U+q_U=0\}|.       \tag{3.5}
\]

### Theorem 3.1 (cap min--max identity)

For an active `C8` `Q`,

\[
 |\operatorname{supp}\lambda_{F'}|-|\operatorname{supp}\lambda_F|
                              =H(Q)-L(Q).                     \tag{3.6}
\]

Consequently:

1. the number of distinct caps increases iff `H(Q)>L(Q)`;
2. every old cap remains covered iff `L(Q)=0`;
3. the exchange is a monotone strict upper improvement iff
   `L(Q)=0` and `H(Q)>0`.

#### Proof

A previously absent cap enters the support exactly in (3.4).  A previously
present cap leaves the support exactly in (3.5).  Every other support
indicator is unchanged by (3.3).  Summing the indicator differences proves
(3.6).  QED.

### Lemma 3.2 (one-marginal conservation)

Every palette-preserving owner-degree exchange, and hence every active
`C8`, preserves the point-degree vector of the rank-ten cap multiset:

\[
       \sum_U(q_U-p_U){\bf1}_U=0\quad\hbox{in }\mathbb Z^{17}.  \tag{3.7}
\]

#### Proof

For an edge of colour `C` with owner endpoints `A,B`,

\[
                  {\bf1}_{A\cup B}={\bf1}_A+{\bf1}_B-{\bf1}_C.\tag{3.8}
\]

The exchange preserves the endpoint-owner multiset and the colour
multiset.  Summing (3.8) before and after therefore gives (3.7).  QED.

In the frozen factor, every coordinate has cap-occurrence degree

\[
 2{16\choose8}-{16\choose7}=25,740-11,440=14,300.             \tag{3.9}
\]

Thus the four-old/four-new cap trade must be balanced coordinatewise.  This
is a sound early rejection row; it is not sufficient for physical `C8`
reachability.

Since `H(Q)<=4`, any route which repairs all `6,141` missing caps using
only successive `C8` exchanges needs at least

\[
                         \left\lceil{6141\over4}\right\rceil
                         =1536                                \tag{3.10}
\]

exchanges.  This is a net-gain bound, independent of how the catalogue is
regenerated between moves.

## 4. Exact component delta on eight ports

Delete the four old owner edges `e_i^-` and call the resulting graph
`F^circ`.  Treat repeated endpoint vertices as occurrence-labelled cut
ports.  The residual paths of `F^circ` pair the eight ports; denote this
fixed-point-free involution by `tau_Q`.  Define the old and new seam
matchings

\[
 \mu^-_Q=\{\{R_i,T_i\}:0\le i<4\},
 \qquad
 \mu^+_Q=\{\{R_i,T_{i-1}\}:0\le i<4\}.                       \tag{4.1}
\]

For two perfect matchings `alpha,beta` on the ports, let
`c(alpha,beta)` be the number of connected alternating cycles in their
union, counting a doubled common edge as one cycle.

### Theorem 4.1 (graphic delta)

If `kappa` denotes the number of owner-factor components, then

\[
 \kappa(F')-\kappa(F)
       =c(\tau_Q,\mu_Q^+)-c(\tau_Q,\mu_Q^-).                  \tag{4.2}
\]

In particular, `Q` merges components iff

\[
                  c(\tau_Q,\mu_Q^+)<c(\tau_Q,\mu_Q^-).       \tag{4.3}
\]

#### Proof

Every touched old cycle is cut into residual paths.  Contract each such
path.  Restoring `mu^-` gives the touched components of `F`; restoring
`mu^+` gives those of `F'`.  Their component counts are exactly the two
alternating-cycle counts in (4.2).  Untouched components cancel.  QED.

The test uses only the order of the four cut edges on their old components.
It is valid after contracting all protected marker paths.  A four-edge
exchange can reduce the component count by at most three, so reducing
`1,179` components to one by `C8`s alone requires at least

\[
                         \left\lceil{1178\over3}\right\rceil
                         =393                                 \tag{4.4}
\]

exchanges.  On the aligned `3+1` face, (4.2) is `-1`, so that restricted
face would require at least `1,178` mergers.

## 5. Simultaneous cap gain and merger

### Theorem 5.1 (necessary and sufficient local criterion)

An atomic simple `C8` produces another exact marker58 owner/rank-eight-q1
two-factor, fixes every protected path edge, increases the number of
distinct rank-ten caps, and merges owner-factor components if and only if:

1. its declared phase is active in `I_F`;
2. its four colour rows satisfy (2.4);
3. `H(Q)>L(Q)`; and
4. (4.3) holds.

If no old cap may be lost, condition 3 is replaced by
`L(Q)=0<H(Q)`.

#### Proof

Lemma 2.1 is the exact factor/protection criterion.  Theorem 3.1 is the
exact distinct-cap criterion.  Theorem 4.1 is the exact component criterion.
The three ledgers refer to the same atomic toggle and contain all changed
rows; hence their conjunction is necessary and sufficient.  QED.

There is no parity or one-marginal obstruction forcing cap gain and merger
to be disjoint.  For example, at the abstract eight-port ledger level take

\[
 \tau=\{R_0T_0,R_1R_2,T_1R_3,T_2T_3\}.                       \tag{5.1}
\]

Then `c(tau,mu^-)=2` and `c(tau,mu^+)=1`.  For a star packet with core
`S`, four distinct petals `a_i`, and four distinct private labels `b_i`,
take

\[
 R_i=S\cup\{a_i,b_i\},\qquad T_i=S\cup\{a_i,a_{i+1}\}.       \tag{5.2}
\]

The old caps are `S+a_i+a_{i+1}+b_i` and the new caps are
`S+a_i+a_{i-1}+b_i` (indices modulo four).  Both four-cap multisets have
the same point degrees,
as required by (3.7).  If the old four have exterior backup occurrences
and the new four are absent, this local ledger has `H=4,L=0` together with
a two-to-one merge.  This is a consistency witness for the exact local
conditions, not a claim that this port pattern and load pattern occur in
the frozen marker58 factor.

## 6. Exchange-space interpretation

### Proposition 6.1 (protected circuit decomposition)

Let `F_0,F_1` be two exact lower-rainbow owner-degree-two factors which
agree on every protected colour row.  Their signed incidence difference
decomposes into alternating even circuits of the rank-eight/rank-nine
Boolean incidence graph, none using a protected incidence.

#### Proof

Colour and owner degrees agree in the two factors.  Hence at every vertex
the number of `F_0-F_1` incidences equals the number of `F_1-F_0`
incidences.  Alternately following negative and positive incidences
decomposes the balanced signed graph into alternating circuits.  Agreement
on protected rows keeps every circuit disjoint from their incidences.  QED.

Thus the natural exact exchange graph is the alternating-circuit graph of
the protected bipartite `b`-factor face.  The face itself is integral by
total unimodularity.  Rank-ten support and connectedness are additional
nonlinear objectives: cap support is a thresholded multiplicity function,
while component merging is graphic rank.  They are therefore not closed by
ordinary weighted `b`-matching alone.  Theorems 3.1 and 4.1 give their exact
single-circuit augmentation oracle.

## 7. Complete marker58 simple-`C8` bound

The degree-two transition joins for star and octahedral simple `C8`s may be
rooted only at an unprotected colour row.  This sharpens the universal
active bound without enumerating a packet.

For a star, a root row has eight choices of rank-seven core and at most
`2^3` directed three-transition prefixes.  For an octahedral packet, it has
`2*binom(8,2)=56` ordered core/petal presentations and at most `2^2`
two-transition prefixes.  Every active directed circuit is counted at its
four unprotected rotations.  Therefore the complete protected-disjoint
active face satisfies

\[
\begin{array}{c|r|r}
 &\text{rooted prefixes}&\text{canonical active packets}\\ \hline
\text{star}&20,366\cdot8\cdot2^3=1,303,424&325,856\\
\text{octahedral}&20,366\cdot56\cdot2^2=4,561,984&1,140,496
\end{array}                                                   \tag{7.1}
\]

and hence

\[
              |\mathcal C_8^{\rm marker58,protected}|
                         \le \boxed{1,466,352}.                \tag{7.2}
\]

Activity closure, opposite-incidence anti-joins, repeated-row rejection,
and the simultaneous tests of Theorem 5.1 can only reduce this number.
Equation (7.2) is a complete finite upper bound, not an observed catalogue
size.

## 8. Exact boundary

The active star/octahedral transition join is therefore directly useful on
the marker58 factor: protection, cap gain, and component merging all admit
constant-size exact filters, and the complete protected-disjoint input face
has at most `1,466,352` packets.  What is not proved is that any packet in
that face passes both strict inequalities in Theorem 5.1, still less that a
sequence reaches cap completeness or connectedness.  Sequential use must
regenerate activity, cap loads, and the port involution after every toggle.

The frozen upper-aware CNF may independently decide a different global
factor.  Nothing here duplicates or constrains that solve.

## 9. Audit payload

The arithmetic and scope ledger is frozen in

```text
scratch/threadA_k17_marker58_protected_c8_exchange_20260802.audit.json.
```

Its hashes are source-relative; no search output is represented as a
theorem.
