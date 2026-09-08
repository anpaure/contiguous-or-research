# The coatom Pluecker lattice is not a positive or physical Markov theorem

Date: 2026-08-01  
Lane: H2, independent audit / physical-lift boundary  
Status: the authoritative integral lattice theorem is independently replayed;
the implication from signed generation to nonnegative packet reachability is
refuted by the smallest packet-admissible occurrence table.  Realizability of
that small table by a global safe carrier is not asserted.

## 0. Outcome

The authoritative theorem
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`
is correct in its stated algebraic scope.  At lower depth two, a canonical
mixed coatom packet changes the complete occurrence-count vector by exactly
one short Pluecker relation, every short relation has a literal packet
labelling when the four spare coordinates exist, and those relations generate
the full integer kernel of the point-degree map.

This is **not** a Markov-basis statement.  In the first physically admissible
parameter row,

\[
                         D=2,\qquad r=6,\qquad s=r-2=4,
\]

there is a mass-two nonnegative degree fibre with at least two points, but
both displayed points are isolated under all short Pluecker moves.  The
smallest extra datum needed even before chronology is therefore the occupied
`(s-2)`-overlap graph.  A packet move needs an occupied edge of this graph.

A safe-carrier move has still stronger prerequisites: the two negative
targets must occur in the two prescribed windows of one complete planted
packet, with its owner word, ordered halo, boundary attachments and residence
state.  Thus the algebraic lattice theorem cannot by itself imply a path in
one safe-carrier component.

## 1. Independent replay of the depth-two action

Use residence depth `D>=2`, owner rank `r>=D+4`, and lower target rank

\[
                              s=r-2.
\]

For the canonical upper-screen set `{1,3,5,7}`, the only multiplicity changes
among intersections of three consecutive owners are

\[
\begin{split}
 -1 &: H\cup\{b,f_1\},\quad H\cup\{a,f_D\},\\
 +1 &: H\cup\{a,f_1\},\quad H\cup\{b,f_D\},
\end{split}                                                     \tag{1.1}
\]

where

\[
 H=K\cup\{\mathord\infty,c\}
       \cup\{f_2,\ldots,f_{D-1}\},\qquad |H|=r-4=s-2.          \tag{1.2}
\]

This is an equality of **occurrence counters**, not only of support
differences: there are exactly four nonzero coordinates, each with coefficient
`+1` or `-1`.

Given any abstract square core `H` and four labels `a,b,x,y` outside it,
partition `H` into

```text
K, {infinity,c}, {f2,...,f_(D-1)}
```

and put `(f1,fD)=(x,y)`.  The part sizes are respectively

\[
                      r-D-4,\quad2,\quad D-2.                  \tag{1.3}
\]

They sum to `r-4`.  The packet still needs the four labels
`e,d_active,f0,f_(D+1)` outside the square support.  Hence

\[
                           |\Omega|-r\ge4                      \tag{1.4}
\]

is exactly sufficient for this labelling argument.  Reversing the packet and
permuting the four displayed labels gives either orientation and every choice
of the two pairings.

The independent replay checks (1.1) as a full multiplicity identity for
`2<=D<=16` and four owner ranks at every depth, and exhausts the partition
counts for the first four admissible rows.

## 2. Integral lattice audit

Let

\[
 \partial_s:\mathbb Z^{\binom\Omega s}\longrightarrow\mathbb Z^\Omega,
 \qquad [S]\longmapsto\sum_{i\in S}e_i.                        \tag{2.1}
\]

The quotient proof in the authoritative theorem can equivalently be phrased
as follows.  Modulo core-square relations, for distinct `i,j` the difference

\[
                  [A\cup\{i\}]-[A\cup\{j\}]                   \tag{2.2}

is independent of the `(s-1)`-set `A` disjoint from `i,j`: adjacent choices
of `A` differ by one core square, and the relevant Johnson graph is connected.
The resulting differences obey the cocycle identity.  Choosing one reference
coordinate therefore puts every class in the form

\[
                              c+\sum_{i\in S}y_i.               \tag{2.3}

If `x` has zero point degrees, summing (2.3) against `x` gives zero; also
`s sum_S x_S=0`, hence `sum_S x_S=0` over the integers.  This proves

\[
       \langle\hbox{short core squares}\rangle_{\mathbb Z}
                       =\ker\partial_s                         \tag{2.4}

without a rational-to-integral gap.

As an independent finite check, the H2 audit constructs every square column
for `4<=|Omega|<=8`, verifies point-degree neutrality literally, and obtains
rank `binom(|Omega|,s)-|Omega|` over each of `F_2,F_3,F_5,F_7` in every
nontrivial layer.  This corroborates but does not replace (2.2)--(2.4).

## 3. Smallest nonnegative obstruction

Take `Omega={0,...,9}`, `s=4`, and the two nonnegative occurrence tables

\[
\begin{aligned}
 \mu &= [0123]+[4567],\\
 \nu &= [0145]+[2367].                                      \tag{3.1}
\end{aligned}
\]

Both have degree one on coordinates `0,...,7` and degree zero on `8,9`.
Thus

\[
                            \partial_4\mu=\partial_4\nu.       \tag{3.2}
\]

They are distinct, so (2.4) says that `nu-mu` is an integer signed sum of
packet square vectors.

Nevertheless no first nonnegative square move is available at either table.
A short rank-four square has two negative sets with a common core of size
`s-2=2`.  The only two occupied sets in each table are disjoint.  Therefore
the occupied overlap graph

\[
 \mathcal O_{s-2}(\mu):
 S\sim T\quad\Longleftrightarrow\quad
 \mu(S),\mu(T)>0\ \hbox{ and }\ |S\cap T|=s-2                 \tag{3.3}
\]

has no edge, and similarly for `nu`.  Both points are isolated in the
nonnegative short-square graph.

This obstruction is minimal in the two relevant senses.

1. A mass-one point is uniquely determined by its point-degree vector, so a
   nontrivial fixed-degree fibre needs mass at least two.
2. The mixed packet has `D>=2` and `r>=D+4`; hence its depth-two target rank
   satisfies `s>=4`.  The row `(D,r,|Omega|)=(2,6,10)` in (3.1) is the first
   row which also has the four spare packet coordinates required by (1.4).

The example is deliberately an occurrence-table theorem.  It does not claim
that the two sparse tables in (3.1) are complete depth-two decks of global
safe carriers.  It proves the logically prior point that signed lattice
generation plus nonnegativity cannot be used as a physical reachability
theorem.

## 4. Exact hierarchy of lift conditions

For a signed square decomposition to become a safe-carrier path, three
strictly stronger conditions are needed.

### 4.1 Positive shelling

There must be an ordering `g_1,...,g_m` of signed square generators such that

\[
                    \mu+\sum_{j\le i}g_j\ge0                   \tag{4.1}
\]

coordinatewise for every prefix.  Section 3 shows that an integer
decomposition need not admit such an ordering.

### 4.2 Witness pairing

For each negative pair at step `i`, the current chronology must realize its
two targets in the paired prefix/suffix windows of one common flag signature.
Occurrence counts do not record this pairing.

### 4.3 Planted physical halo

Those windows must extend to the complete length-`12D+35` old phase with the
exact ordered owner word, four spare labels, endpoint owners, exterior
attachments and clipped residence state.  Only then is the edge present in
the safe-move graph of the serial theorem.

These conditions are also a proof-safe sufficient interface: an ordered list
of packet embeddings satisfying them in the carrier obtained after each
previous replacement is literally a walk in the safe-carrier graph.  In the
stronger static case of pairwise disjoint packet halos, the replacements
commute and all Boolean phase choices form an embedded cube of safe carriers.
No claim is made that the current Pascal construction supplies either
interface.

Finally, even a physical depth-two walk carries the coupled higher-depth flag
actions and preserves the reflected pair-degree invariants of the
authoritative theorem.  Positive/physical lift and the coupled-depth terminal
compiler condition are therefore separate gates.

## 5. Audit and provenance

Authoritative theorem independently replayed:

```text
MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md
  SHA-256 616709fc50029593ca29bbf1e4459005a33a752fb4ff2e6f3aa617f0639c5e64
scratch/audit_coatom_flag_signature_lattice_20260801.py
  SHA-256 bd50dbd863c84b6e6bcbec546d0811af785e9c88bbe5e6790d865a2af65146e1
scratch/coatom_flag_signature_lattice_20260801.audit.json
  SHA-256 0f45fa17bf2a3cc2048e8b508f472846224fccccc1d1295752745de9f39e0071
payload
  8f30a09f7c260a91f0666b427f7bef2592a964d316bf7e94d2d59ef4e3d8aa90
```

Independent packet/lattice/positive-fibre audit:

```text
scratch/audit_h2_coatom_q2_plucker_occurrence_lattice_20260801.py
scratch/h2_coatom_q2_plucker_occurrence_lattice_20260801.audit.json
```

It reports

```text
PASS_Q2_PACKET_PLUCKER_OCCURRENCE_LATTICE
```

with canonical payload SHA-256

```text
25b560db4a86d7bffc3e37d24f7dd4913351e4af6e0373f404101af599e09063
```

No compiler reachability, global safe-component connectivity, or additive
constant conclusion is claimed.
