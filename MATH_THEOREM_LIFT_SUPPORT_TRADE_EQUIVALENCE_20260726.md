# Phase-free support form of a cyclic lift

Date: 2026-07-26

Method: pure mathematics only.

## 1. Exact support criterion

Let `p=2m+1` be prime, let `sigma` be a coordinate `p`-cycle, and let
`F` be an exact middle wreath factor.  For a wreath row `C`, write
`M(C)` for its set of `p` middle windows.  Given exponents

\[
                         a:F\longrightarrow\mathbb F_p,
\]

put

\[
 U_v=\bigsqcup_{C:a(C)=v}M(C).                              \tag{1.1}
\]

The sets `(U_v)` partition the middle layer because `F` is exact.

### Theorem 1.1 (phase-free legality)

The lifted row family

\[
                         F_a=\{\sigma^{a(C)}C:C\in F\}
\]

is an exact middle factor if and only if the sets

\[
                         \{\sigma^vU_v:v\in\mathbb F_p\}     \tag{1.2}
\]

partition the middle layer.  Equivalently,

\[
 \boxed{
 U_v\cap\sigma^{,v'-v}U_{v'}=\varnothing
 \quad(v\ne v').}                                          \tag{1.3}
\]

#### Proof

The middle support of the shifted row `sigma^v C` is
`sigma^v M(C)`.  Taking the union over the level set `a(C)=v` gives
`sigma^vU_v`, so exactness is exactly (1.2).  The total cardinality in
(1.2) is already

\[
                         \sum_v|U_v|=\binom p m.
\]

Thus covering, pairwise disjointness, and being a partition are
equivalent, and translating a pairwise intersection gives (1.3).
\(\square\)

This criterion contains the complete-residue/Latin equations but has no
phase variables.

## 2. Three levels are exactly trades

Assume now that every row is transversal for the `sigma`-necklaces and
that

\[
                         a(C)\in\{0,+t,-t\},\qquad t\ne0.     \tag{2.1}
\]

Let `F_+` and `F_-` be the positive and negative row sets, and assume
`|F_+|,|F_-|<p`.  Transversality then prevents either sign from occupying
all phases of a necklace.

### Theorem 2.1 (`+/-t` collapse)

The assignment (2.1) is legal if and only if

\[
 \boxed{
 \bigsqcup_{D\in F_-}M(D)
 =
 \bigsqcup_{C\in F_+}M(\sigma^tC).}                         \tag{2.2}
\]

In particular `|F_+|=|F_-|`, and every nonconstant legal three-level lift
is exactly a relabeling wreath trade.

#### Proof

Fix one `sigma`-necklace and identify its phases with `F_p`.  Let `P` and
`N` be the phase sets occupied there by positive and negative rows.
Legality says

\[
                         (P+t)\sqcup(N-t)=P\sqcup N.          \tag{2.3}
\]

Equivalently the map which moves a point of `P` by `+t`, a point of `N`
by `-t`, and fixes every other point is a permutation.  After scaling
`t=1`, every nonfixed arrow is an edge of the cycle `C_p`.  A permutation
cycle of length at least three would have to be the whole `C_p`, with all
arrows carrying the same sign.  The hypotheses `|P|,|N|<p` exclude that
case.  Hence every nontrivial cycle is a transposition

\[
                         x\longleftrightarrow x+t,
\]

with `x in P` and `x+t in N`.  Therefore `N=P+t` on every necklace.
Assembling the necklace identities gives (2.2).  The converse follows by
reversing the same argument. \(\square\)

### Corollary 2.2 (interaction-overlay form)

If `h=|F_+|=|F_-|`, then (2.2) is a union of components of the ownership
overlay between `sigma^tF` and `F`, with total side size `h`.  Thus:

* `h=1` is an inert row swap;
* `h=2` is a two-for-two wreath trade and a size-two interaction
  component when its overlay is connected;
* excluding two-for-two trades rules out only the first useful case, not
  the cases `h>=3`.

The last point is important: a minimal `h`-trade need not contain any
smaller subtrade.

For later audits, if `C,D in F`, define the phase-`t` agreement number by

\[
 \operatorname{ag}_t(C,D)
 =\#\{O:\phi(D,O)=\phi(C,O)+t\}.                            \tag{2.4}
\]

Then

\[
 \boxed{
 \operatorname{ag}_t(C,D)
 =|M(D)\cap M(\sigma^tC)|,
 \qquad
 \sum_{D\in F}\operatorname{ag}_t(C,D)=p.}                 \tag{2.5}
\]

Indeed an agreement in one necklace is exactly equality of the two
physical middle sets after shifting `C`, and the exact factor `F`
partitions the `p` members of `M(sigma^tC)`.  Thus cross-phase agreement
is not a surrogate statistic: it is precisely the edge multiplicity in
the ownership overlay between `sigma^tF` and `F`.

## 3. One row is rigid

### Lemma 3.1 (middle support determines a wreath)

The middle support of a wreath determines its cyclic coordinate order up
to rotation and reversal.

#### Proof

For the middle windows `I(j,m)` of one cyclic order, if the cyclic start
distance is `d`, then

\[
 |I(j,m)\cap I(j+d,m)|=
 \begin{cases}
 m-d,&0\le d\le m,\\
 d-m-1,&m+1\le d\le2m.
 \end{cases}                                                \tag{3.1}
\]

The intersection has size `m-1` exactly for `d=+/-1`.  Hence the Johnson
distance-one graph induced on the support is precisely its `p`-cycle.
The successive set differences along either orientation recover the
coordinate order; changing orientation gives reversal. \(\square\)

Consequently a one-for-one equality in (2.2) has
`D=sigma^tC` as a wreath row and changes no row family.  This is the
phase-free explanation of minimal-packet rigidity.

## 4. Exact frontier

The theorem identifies, but does not solve, the productive lift gate.
One must either

1. produce `sigma^t`-paired `h`-trades in a smoothing-good factor in
   sufficient supply, or
2. prove a wreath-geometric obstruction to such trades.

Raw existence of a two-for-two trade is not enough.  Such trades already
occur in the recorded `m=4` alternating-`C_8` family; the missing content
is compatibility with one common prime-cycle shift, the `p+2` packet
incidence, and the multidepth energy sign.
