# Domino-twin inverse stability: the exact star-to-top deferred-mate charge

Date: 2026-07-27

## 0. Verdict

Let (F,G) be two simple domino-twin packets, each of size
(K=4m), and put

\[
 s=|F\setminus G|=|G\setminus F|.
\]

The star-to-top ambiguity in the four-target normal form does **not**
cost merely a phase bit pointwise.  A two-target top edge determines the
top union and one element of each endpoint domino, but it does not
determine the two mates.  Thus the line

\[
       k=2\quad\Longrightarrow\quad0\text{ free letters}
\]

in the current paired-window zipper proof is not literally justified.

There is nevertheless an exact repair for this branch.  Conditional on
the abstract cell-incidence record, every genuinely undetermined mate
created by a star-to-top shared edge is assigned injectively to a lower
cell of (G) containing exactly one common target.  Such a cell contains
three targets of (G\setminus F).  Consequently, if (f_{\rm st}) is
the number of free mate labels arising from all star-to-top edges, then

\[
 \boxed{3f_{\rm st}\le s.}                              \tag{0.1}
\]

Hence the genuine top-only star-to-top branch contributes at most

\[
 \boxed{n^{f_{\rm st}}\le n^{s/3}}                     \tag{0.2}
\]

completions after the finite incidence record is fixed.  In particular,
genuine top-only coincidences cannot by themselves cause the critical
(n^{s/2}) list size.  Shore/mate hinges are excluded from this sentence;
they are the critical residual classified in the companion counteraudit.

This note does **not** validate the whole claimed inverse-stability
theorem.  In fact the subsequent independent audit
`MATH_AUDIT_DOMINO_DOUBLE_SEGMENT_HALF_EXPONENT_AND_COLLAR_OVERLAP_20260727.md`
shows that the uniform exponent below (1/2) is false: two segments at
displacement (r) reuse the same remote charge front.  Section 4 below
records the exact four-missing-target charge available for an owner-fixed
dark reconnection; the obstruction is precisely that the local three-
and four-charges cannot be made globally disjoint.

## 1. Exact alternating cell normal form

Write the paired cyclic word of (G) as

\[
 (C_0,C_1,\ldots,C_{m-1}),\qquad |C_j|=2,
\]

and put

\[
 W_j=C_j\cup C_{j+1}\cup\cdots\cup C_{j+r-1},
 \qquad R=2r+1.
\]

The lower star cell at (j) is

\[
 \mathcal L_j=
 \{W_j\cup\{z\}:z\in C_{j-1}\cup C_{j+r}\}.          \tag{1.1}
\]

Put

\[
 U_j=W_j\cup C_{j+r}.
\]

The upper top cell between \(\mathcal L_j\) and
\(\mathcal L_{j+1}\) is

\[
 \mathcal T_j=
 \{U_j\setminus\{z\}:z\in C_j\cup C_{j+r}\}.         \tag{1.2}
\]

Its two shores are

\[
 \mathcal T_j\cap\mathcal L_j
 =\{U_j\setminus\{z\}:z\in C_{j+r}\},                 \tag{1.3}
\]

\[
 \mathcal T_j\cap\mathcal L_{j+1}
 =\{U_j\setminus\{z\}:z\in C_j\}.                     \tag{1.4}
\]

Thus the lower and upper cells form an alternating cyclic chain, and
each consecutive pair shares a two-target shore.

The exact clique census proves that this is not merely a subgraph of the
distance-one graph induced by (G).  The canonical lower and upper
quartets contain (10m) Johnson edges and are (5)-regular on the
(4m) targets.  The exact pair census also gives (5n=10m) distance-one
edges in total.  Hence every Johnson edge induced by (G) is contained
in a canonical lower star or canonical upper top (and a shore edge is
contained in both).  This justifies the star/top dichotomy for a
two-target intersection.

## 2. What a top-only shared edge determines

Let (X,Y\in F\cap G) be a top-only edge of (G), contained in
\(\mathcal T_j\), with one endpoint on each shore.  Write

\[
 X=U_j\setminus\{x\},\qquad
 Y=U_j\setminus\{y\},                                  \tag{2.1}
\]

where, after interchanging the shores if necessary,

\[
 C_{j+r}=\{x,x'\},\qquad C_j=\{y,y'\}.                 \tag{2.2}
\]

The pair (X,Y) determines

\[
 U_j=X\cup Y,
 \qquad x=U_j\setminus X,
 \qquad y=U_j\setminus Y.                              \tag{2.3}
\]

It does not determine (x') or (y').  Indeed, before neighbouring
cell equations are used, (x') and (y') can be arbitrary distinct
members of (U_j\setminus\{x,y\}), subject to completing the two
endpoint dominoes and the interior domino partition.  A star/top bit
therefore cannot, by itself, pay these labels.

This is the precise defect in the pointwise (k=2\mapsto0) row of the
uncorrected zipper table.  The next theorem supplies the correct
amortized statement.

## 3. Deferred-mate injection

### Theorem 3.1 (one free mate costs three missing targets)

In the notation of (2.1)--(2.2), the mate (x') is determined as soon
as the adjacent lower cell \(\mathcal L_j\) contains a second target of
(F\cap G).  If it is not so determined, then

\[
 |\mathcal L_j\cap F|=1
 \quad\text{and}\quad
 |\mathcal L_j\setminus F|=3.                          \tag{3.1}
\]

The analogous assertion holds for (y') and
\(\mathcal L_{j+1}\).

#### Proof

By (1.3), (X\in\mathcal L_j).  Suppose that
(Z\in(\mathcal L_j\cap F)\setminus\{X\}).  Any two distinct members
of one lower star have intersection equal to its common lower core.
Therefore

\[
 W_j=X\cap Z.                                           \tag{3.2}
\]

Since

\[
 X=U_j\setminus\{x\}=W_j\cup\{x'\},
\]

we recover

\[
 x'=X\setminus W_j=X\setminus(X\cap Z).                \tag{3.3}
\]

Thus (x') is determined by the second common target.  If no such
target exists, (X) is the unique member of \(\mathcal L_j\cap F\).
The lower cell has four targets, proving (3.1).  The proof for (y')
is identical using (1.4).  \(\square\)

### Theorem 3.2 (injective global charge)

Fix the abstract record specifying which common targets lie in each
canonical lower and upper cell of (G), and expose every mate which is
determined by Theorem 3.1.  Let (f_{\rm st}) be the number of remaining
mate labels associated with top-only shared edges.  Then

\[
 3f_{\rm st}\le |G\setminus F|.                         \tag{3.4}
\]

Consequently their total number of label assignments is at most

\[
 n^{f_{\rm st}}\le n^{s/3}.                            \tag{3.5}
\]

#### Proof

Assign the undetermined mate (x') in Theorem 3.1 to
\(\mathcal L_j\).  By (3.1), this cell has the unique common target
(X).  That target lies on exactly one of the two shores of
\(\mathcal L_j\), hence in exactly one of its two adjacent upper cells.
Therefore the same weak lower cell cannot receive a second distinct
deferred mate from another top-only shared edge.  The assignment from
free mates to weak lower cells is injective.

The lower star cells partition the (4m) targets of (G).  Hence the
three targets in \(\mathcal L_j\setminus F\), as (j) ranges over the
charged cells, are pairwise disjoint.  This proves (3.4).  Once all
previously determined labels and the cell-incidence record are fixed,
each free mate has at most (n) possible values.  Multiplication and
(3.4) give (3.5).  \(\square\)

The injection remains valid if several common edges name the same mate:
they are one deferred label and are counted only once.  It also remains
valid when the edge is a shore edge in one packet and a top-only edge in
the other; only the canonical (G)-cell incidence in (1.3)--(1.4) is
used.

## 4. The complementary four-target reconnection charge

There is a second exact bookkeeping fact.  Every domino (C_j) labels
two shores of the alternating cell chain.  Together those two shores
contain four distinct targets, and the resulting (m) four-slot
families partition (G).

If a domino has no common target in either occurrence, all four of its
slots lie in (G\setminus F).  Conditional on the positions and the
residual set of individual labels, reconnecting (2h) such labels into
(h) unordered dominoes has at most

\[
 (2h-1)!!\le n^h                                       \tag{4.1}
\]

possibilities, whereas these (h) dominoes account for (4h) distinct
missing targets.  Thus an owner-fixed completely dark reconnection has
the sharp charge

\[
 \boxed{\text{one factor }n\text{ per four missing targets}.} \tag{4.2}
\]

This proves the desired (1/4) exponent for the pure reconnection
layer.  It does not count the assignment of the resulting dominoes to
as-yet-unresolved cyclic positions.  That assignment belongs to the
remaining paired-window corridor problem.

## 5. Audit of the claimed (c=1/3) inverse theorem

The following parts of the current inverse-stability proof are valid:

1. three or four common targets in one (F)-lower cell force the same
   lower core in (G);
2. every induced Johnson edge of a twin packet lies in a canonical star
   or top, by the exact edge census;
3. star/top phase and shore data have only exponential-in-(m) entropy;
4. the star-to-top branch satisfies the rigorous (n^{s/3}) bound of
   Theorem 3.2; and
5. completely dark, position-fixed reconnections satisfy the
   (n^{s/4}) bound of Section 4.

Even before the double-segment obstruction is applied, the written proof
does not establish the full theorem

\[
 |\{G:|F\setminus G|\le s\}|\le \exp(O(m))n^{s/3}
\]

does not follow from the written zipper proof.  Its table treats a
two-point top anchor as releasing no labels before proving the
deferred-mate injection, and it does not provide an injective encoding
for assigning dark or one-point dominoes to unresolved cyclic
positions.  The exact remaining lemma is:

> **Two-front corridor lemma.**  After all mates charged by Theorem 3.2
> and all position-fixed dark reconnections in Section 4 are removed,
> the remaining unresolved cyclic-position assignments admit an
> encoding with at most one (n)-ary symbol per disjoint three-target
> defect charge (or one per disjoint four-target dark charge).

Such a lemma cannot hold with globally disjoint charges.  The audited
double-segment family reuses one remote front for two independent
repartitions and reaches exponent (1/2-o(1)).  Theorem 3.2 rules out
reuse of one *individual* weak lower cell by two deferred mates; it does
not prevent two long collar systems from sharing nearly all of a remote
front.

## 6. Proved boundary

Proved here:

1. the exact alternating lower/upper four-cell normal form;
2. validity of the canonical star/top edge dichotomy;
3. the failure of the pointwise claim that a top edge fixes both endpoint
   dominoes;
4. the deferred-mate injection and the charge of three missing targets
   per free star-to-top label;
5. the charge of four missing targets per owner-fixed dark
   reconnection; and
6. the (n^{s/3}) upper bound for the whole star-to-top part of a fixed
   cell-incidence record.

Not proved here:

1. the complete close-neighbour list bound with any fixed (c<1/2)
   (which is false uniformly for (s=o(m)));
2. a terminal-scale estimate with an explicit additive constant at
   (s=\Theta(m/\log m));
3. a trajectory theorem excluding simultaneous paired-segment survival;
   or
4. coefficient one.
