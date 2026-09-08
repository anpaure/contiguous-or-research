# Complement-paired tail witnesses admit independent resident connectors

**Date:** 2026-08-06  
**Method:** explicit two-sided collars, antipodal distance, and the sparse
clipped-flag interval-Hall theorem; no computation or search  
**Status:** unconditional asymptotic residence/topology theorem.  After
closing the tail family under external complementation, every short-tail
witness can be thickened by two private-coordinate monotone collars and the
resulting low/high macros can be connected cyclically by independently
chosen monotone geodesics.  Every positive run and every zero gap is then
resident.  This note does not pack the new owners or either immediate
palette against the already protected bank.

## 1. Tail paths

Write

\[
 K\mathbin{\dot\cup}E=[2m-1],
 \qquad |K|=m-1,
 \qquad |E|=m,
\tag{1.1}
\]

and let `d=O(sqrt(m))`.  Let `L` be any family of external traces satisfying

\[
                         1\le |T|\le2d.
\tag{1.2}
\]

For `T in L`, put `q=|T|` and use the shortened low witness

\[
 Q_T^{\rm low}=(T\cup W_0,\ldots,T\cup W_{q-1}),
\tag{1.3}
\]

where the `W_j` are the consecutive `(m-q)`-windows of a linear order of
`K`.  Use also the balanced two-port monotone high witness for
`bar T=E setminus T` constructed in Section 3 below.

If the original protected tail family is not complement-closed, adjoining
these complementary paths costs only another `2^{o(m)}` paths.  They may be
treated as auxiliary witnesses; no target-coverage claim is needed for an
adjoined path.

When `m>=4d`, the low window length `m-q` is greater than the number `q` of
owners in (1.3).  Hence the occurrence interval of a `K`-coordinate cannot
both begin and end internally: every coordinate changes at most once on the
low path.  The same is true by construction on the monotone high witness. In
particular, every positive run or zero gap wholly internal to either path is
absent; only endpoint components need collars.

## 2. A literal two-sided collar for a short path

Let

\[
 Q=(Q_0,Q_1,\ldots,Q_\ell)=Q_T^{\rm low},
 \qquad \ell=q-1<2d.
\tag{2.1}
\]

The transition support of `Q` has size `2 ell<4d`.  Moreover

\[
 |Q_0\cap Q_\ell|=m-\ell,
 \qquad
 |[2m-1]\setminus(Q_0\cup Q_\ell)|=m-1-\ell.
\tag{2.2}
\]

For `m>=6d+1`, choose pairwise disjoint sets

\[
 D^-,D^+\subseteq K\cap Q_0\cap Q_\ell,
 \qquad
 I^-,I^+\subseteq E\setminus T,
\tag{2.3}
\]

each of size `d`.  Prepend the monotone `d`-step path from

\[
                         Q_0-D^-+I^-
\quad\hbox{to}\quad       Q_0
\tag{2.4}
\]

which deletes `I^-` and inserts `D^-`.  Append the monotone `d`-step path
from

\[
                         Q_\ell
\quad\hbox{to}\quad       Q_\ell-D^++I^+.
\tag{2.5}
\]

Call the resulting path `widehat Q_T`.

The original subpath `Q` remains a contiguous internal interval of
`widehat Q_T` and still has union exactly `K union T`.  The collar owners
are not included in that target occurrence.

Every outer endpoint has external trace `T union I^-` or `T union I^+`,
respectively, and hence external rank `q+d<=3d`.

### Lemma 2.1 (the thickened low path is internally biresident)

Every positive run and every zero gap of `widehat Q_T` which meets neither
outer endpoint has length at least `d+1`.  Its first and last `d`
transitions are monotone one-pass collars.  The path is simple.

#### Proof

The four active banks in (2.3) are disjoint from the transition support of
`Q`.  A coordinate changed in the left collar keeps its new value throughout
`Q` and the complete right collar, so its post-change component has at least
`d+1` owners; its pre-change component meets the outer left endpoint.  A
coordinate changed in the right collar had its old value throughout the
complete left collar and `Q`, so its pre-change component has at least
`d+1` owners; its post-change component meets the outer right endpoint.
The original path has no internal short component by Section 1.

An open left-collar owner differs from `Q_0` on a nonempty subset of the
left active bank, while every owner of `Q` and the right collar agrees with
`Q_0` there.  The symmetric statement holds for the right collar.  The
three pieces are individually monotone and simple, so no owner repeats.
\(\square\)

The high witness has `m-q-1>=2d` transitions once `m>=4d+1`.  Its first and
last `d` transitions therefore already provide the same fixed endpoint
contexts, and no extra collar is required.

## 3. A balanced two-port high witness

Fix `T`, put `q=|T|`, and write `U=E setminus T`.  Choose

\[
                         C\subseteq U,
 \qquad                  |C|=q+1.
\tag{3.1}
\]

This is possible once `m>=2q+1`.  Put

\[
 e=|U\setminus C|=m-2q-1,
 \qquad L=m-q-1,
 \qquad a=\lfloor e/2\rfloor.
\tag{3.2}
\]

Choose `X_E subseteq U setminus C` of size `a`, choose
`X_K subseteq K` of size `L-a`, and put

\[
 X=X_E\cup X_K,
 \qquad
 Y=((U\setminus C)\cup K)\setminus X.
\tag{3.3}
\]

Then `|X|=|Y|=L`.  Give `X,Y` arbitrary orders and define

\[
 H_j=C\cup\{x_{j+1},\ldots,x_L\}
          \cup\{y_1,\ldots,y_j\},
 \qquad 0\le j\le L.
\tag{3.4}
\]

### Lemma 3.1 (balanced high ports)

The path `(H_0,...,H_L)` is a simple monotone Johnson path of rank `m` and

\[
                         \bigcup_{j=0}^{L}H_j=K\cup\bar T.
\tag{3.5}
\]

Every coordinate changes at most once.  Its two endpoint external ranks are

\[
 |H_0\cap E|=q+1+a,
 \qquad
 |H_L\cap E|=q+1+e-a,
\tag{3.6}
\]

and hence are exactly

\[
 \left\lfloor{m+1\over2}\right\rfloor,
 \quad
 \left\lceil{m+1\over2}\right\rceil
\tag{3.7}

in some order.

#### Proof

The sets `C,X,Y` partition `K union U`; (3.2)--(3.3) give
`|C|+|X|=q+1+m-q-1=m`.  Every transition in (3.4) deletes one new `x` and
inserts one new `y`, proving simplicity and monotonicity.  Their union is
the full partition, proving (3.5).  Formula (3.6) is immediate, and its two
entries have sum

\[
                         2(q+1)+e=m+1
\]

and differ by at most one.  This proves (3.7). \(\square\)

Call this path `Q_(bar T)^bal`.  Its length is
`L=m-q-1>=m-2d-1`, so its first and last `d` transitions provide fixed
endpoint contexts for all sufficiently large `m`.

Order the macros cyclically as

\[
 \widehat Q_{T_1},Q_{\bar T_1}^{\rm bal},
 \widehat Q_{T_2},Q_{\bar T_2}^{\rm bal},\ldots .
\tag{3.8}
\]

### Lemma 3.2 (every requested connector is long)

For arbitrary choices of the displayed macro endpoints, every requested
Johnson distance in (3.8) is at least

\[
                         \left\lfloor{m+1\over2}\right\rfloor-3d.
\tag{3.9}
\]

#### Proof

An outer low-collar owner has external rank at most `3d`.  By (3.7), a
balanced high endpoint has external rank `s>=floor((m+1)/2)` and therefore
`K`-rank `m-s`.  Their intersection has size at most

\[
                         3d+(m-s).
\]

Both owners have rank `m`, so their Johnson distance is at least
`s-3d`, proving (3.9).  The argument does not use which low trace is paired
with the high endpoint and therefore applies on both sides of every high
macro. \(\square\)

In particular, when

\[
                         m\ge12d+1,
\tag{3.10}
\]

every requested distance is at least `3d`.

## 4. Independent connector theorem

### Theorem 4.1 (resident complement-paired tail chronology)

Assume `m>=12d+1`.  Between every consecutive pair of macro endpoints in
(3.8), there is a monotone Johnson geodesic such that the resulting cyclic
concatenation is positive- and zero-resident with deadline `d`.

The connector orders may be selected independently after all thickened
macros and their endpoint owners have been fixed.

#### Proof

Each macro supplies at least `d` transitions of fixed context at either
endpoint: explicitly by Lemma 2.1 for a low macro, and by the first and last
`d` transitions of a high monotone witness.  Corollary 3.5 of the clipped
connector theorem says that at most `d` short positive and at most `d`
short zero histories occur on either side of a requested connector.

Lemma 3.2 and (3.10) give connector distance at least `3d`.  The sparse-flag
Theorem 3.4 therefore supplies a deletion SDR and an insertion SDR for that
connector.  Its conclusion uses only the two already fixed adjacent macro
contexts, so the connector orders are independent across distinct seams.

A monotone connector changes every coordinate at most once, hence has no
positive run or zero gap wholly internal to it.  Lemma 2.1 and the analogous
property of the high witness handle components internal to a macro.  The
two interval matchings handle every component meeting a connector seam.
These cases exhaust the cyclic chronology. \(\square\)

### Theorem 4.2 (linear conditioned aperture in every tail connector)

Use the explicit three-zone schedule of Theorem 3.6 in the clipped
connector note.  Fix all constrained labels and fill any unused boundary
positions deterministically with seasoned labels.  Put

\[
                         q_0=q-3d.
\tag{4.1}
\]

The deletion and insertion labels assigned to the central position block

\[
                         [2d+1,q-d]
\tag{4.2}
\]

may then be ordered independently and uniformly.  At distance `s` into
this free block, every compatible owner has conditional probability

\[
                         {1\over\binom{q_0}{s}^2},
\tag{4.3}
\]

and every compatible immediate lower or upper colour between levels `s`
and `s+1` has probability

\[
             {1\over\binom{q_0}{s}\binom{q_0}{s+1}}.
\tag{4.4}
\]

For the complement-paired tails,

\[
 q_0\ge\left\lfloor{m+1\over2}\right\rfloor-6d
      =\Omega(m).
\]

#### Proof

Theorem 3.6 assigns every short-history label in the three boundary zones.
Every other label is seasoned at both ends and has the full legal interval
`[1,q]`; hence arbitrary completion of the boundary zones and arbitrary
ordering in (4.2) preserve residence.  After the fixed labels are removed,
an owner at free level `s` specifies independently an unordered prefix
`s`-set of the remaining deletion labels and an unordered prefix `s`-set of
the remaining insertion labels.  Uniform independent permutations give
(4.3).  A lower or upper colour specifies prefix sizes `s,s+1` in the two
orders, giving (4.4).  Lemma 3.2 gives
`q>=floor((m+1)/2)-3d`, hence the final bound.
\(\square\)

## 5. Size and the remaining resource gate

The complement closure of the tail family has size

\[
 2\sum_{j=0}^{2d}\binom mj=2^{o(m)}.
\tag{5.1}
\]

Every thickened low path, high path, and connector has `O(m)` roles, so the
complete chronological leave in Theorem 4.1 still has `2^{o(m)}` owner and
immediate-palette roles.

This theorem closes the **residence and abstract topology** of the tail
leave and leaves an exact linear random aperture in every connector.  It
does not prove that the collar or connector owners, lower
colours, and upper colours avoid the central antipodal bank, the low rolling
collars, the hinge paths, or one another.  That is now a separate
subexponential resource-packing theorem.  Nor does this theorem supply the
PBBS all-width occurrence bank or terminal compiler.

## 6. Dependencies

Used as inputs:

* `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md`;
* `MATH_THEOREM_CLIPPED_RESIDENCE_CONNECTOR_INTERVAL_MATCHING_20260806.md`;
* the elementary monotone-geodesic metric in a Johnson graph.
