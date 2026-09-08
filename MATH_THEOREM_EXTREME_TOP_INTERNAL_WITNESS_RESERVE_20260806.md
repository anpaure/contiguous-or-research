# Every extreme top target has a resource-disjoint internal-ring witness

## Status

The buffered masked collar reduces the unresolved extreme upper bank to

\[
 \mathcal E_h^{\rm proper}
   =\{R-X:3\le |X|\le h-1\}.                           \tag{0.1}
\]

This note gives a deterministic protected reserve for that entire bank.
For every target `Z=R-X`, choose one near-maximal period-`(q+h-2)` ring
whose unused coordinate lies in `X` and whose moving order has
`Z-K` as one consecutive block.  The source interval on that block has
union exactly `Z`; open the ring inside the complementary block, so the
witness is internal and survives the opening.

The candidate lists are exponentially larger than all conflicts caused by
the subexponential target bank.  A greedy choice therefore gives one ring
per target with pairwise disjoint owner and root resources.  The complete
reserve uses `exp(o(q))=o(W)` rings and source positions at critical width.

This closes the **internal witness selection** problem for the extreme
bank.  It does not prove that an arbitrary `o(W)` protected partial ring
factor extends to an exact one-copy factor, nor that the selected safe cuts
simultaneously expose compatible masked-tree collars.  Those are explicit
remaining extension/linkage premises.  No computation or search is used.

## 1. Parameters and the complement formula

Put

\[
 n=2q-1,qquad s=q-h,qquad
 \ell=q+h-2=n-s-1,                                    \tag{1.1}
\]

and assume `h=o(q)`, with `h>=4`.  A period-`ell` antipodal ring is an
ordered partition

\[
                         R=K\mathbin{\dot\cup}F
                              \mathbin{\dot\cup}U,      \tag{1.2}
\]

where

\[
                         |K|=s,quad |F|=\ell,quad |U|=1,               \tag{1.3}
\]

together with an oriented cyclic order on `F`.  Its source letters are
`K+f` in that order.

For any cyclic mover interval `I subseteq F`, the corresponding source
interval has value

\[
                         K\cup I,
\]

and hence complement

\[
                         R-(K\cup I)=U\cup(F-I).        \tag{1.4}
\]

Thus a top target `R-X` occurs precisely when the unused set is contained
in `X` and the omitted moving set is `X-U`.

## 2. An explicit internal witness

Fix

\[
                         X\subseteq R,qquad |X|=j,qquad3\le j\le h-1,
                                                               \tag{2.1}
\]

and put `Z=R-X`.  Choose

\[
                         x\in X,qquad
                         K\in\binom Zs,                 \tag{2.2}
\]

and set

\[
 A=Z-K,qquad B=X-\{x\}.                               \tag{2.3}
\]

Then

\[
 |A|=n-j-s=q+h-1-j,qquad |B|=j-1,                    \tag{2.4}
\]

and `A dotcup B` has size `ell`.  Let

\[
                         U=\{x\},qquad F=A\dotcup B.   \tag{2.5}
\]

Choose arbitrary linear orders of `A` and `B`, concatenate them as

\[
                         A\,B,                          \tag{2.6}
\]

and regard (2.6) as an oriented cyclic order of `F`.

### Lemma 2.1 (literal internal extreme witness)

The source interval on the consecutive mover block `A` has union exactly

\[
                         K\cup A=Z.                    \tag{2.7}
\]

Moreover, because `|B|=j-1>=2`, the ring can be opened at an arc internal
to `B`.  The interval (2.7) then remains a literal internal interval of the
opened linear block.

#### Proof

Every source letter on the block `A` contains the common core `K` and one
element of `A`.  Their union is `K union A=Z`.  An opening arc whose two
ends lie in the complementary block `B` does not cut the block `A`, so the
same consecutive source interval survives after opening. \(\square\)

The opening is a protected seam: later topology may use it only through a
splice which leaves the internal block `A` intact.  No claim is made that
an arbitrary masked collar is already present at that arc.

## 3. Exact candidate degree

Oriented cyclic orders are taken modulo rotation but not reversal.  Once
the two blocks `A,B` are specified, choosing their two linear orders gives
one such cyclic order, with the boundary from `B` to `A` as its canonical
origin.  Therefore the number of candidate rings constructed above for a
fixed `j`-target is exactly

\[
 \begin{aligned}
 N_j
 &=j\binom{n-j}{s}(n-j-s)!(j-1)!\\
 &=\boxed{{j!(n-j)!\over s!}}.                         \tag{3.1}
 \end{aligned}
\]

No factor two is lost: reversal is a different oriented source ring.  If
one deliberately quotients by dihedral symmetry, `N_j/2` is still a valid
uniform lower bound and all conclusions below remain unchanged.

## 4. Exact ambient resource codegree

Let `mathcal R_ell` be the set of all oriented period-`ell` ring states
with core size `s` and one unused coordinate.  Its size is

\[
 |\mathcal R_\ell|
   =\binom ns(n-s)(\ell-1)!
   ={n!\over s!\ell}.                                  \tag{4.1}
\]

Every ring contains `ell` distinct rank-`q` owners and `ell` distinct
rank-`(q-1)` roots.  The symmetric group is transitive on either central
shore, each of size

\[
                         W=\binom nq=\binom n{q-1}.     \tag{4.2}
\]

Consequently the number of ambient ring states containing one fixed owner
or one fixed root is exactly

\[
 D={|\mathcal R_\ell|\ell\over W}
   =\boxed{{q!(q-1)!\over s!}}.                        \tag{4.3}
\]

The codegree of a fixed resource inside any one target's candidate list
is at most `D`.  This ambient value is deliberately used instead of a
smaller target-dependent estimate, so no relative-position case is hidden.

The exact list-to-codegree ratio is

\[
 {N_j\over D}
   ={j!(n-j)!\over q!(q-1)!}
   =\boxed{
      {\binom{n-j}{q}\over\binom{q-1}{j}}}.            \tag{4.4}
\]

For `j=O(sqrt(q))`, Stirling's formula uniformly gives

\[
 \log {N_j\over D}
      =(2\log2+o(1))q.                                 \tag{4.5}
\]

Indeed `binom(n-j,q)=exp((2 log 2+o(1))q)`, while
`log binom(q-1,j)=O(j log(q/j))=o(q)`.

## 5. Deterministic conflict packing

Let

\[
 M=\sum_{j=3}^{h-1}\binom nj.                          \tag{5.1}
\]

For `h=O(sqrt(q))`,

\[
                         M=\exp(o(q)).                  \tag{5.2}
\]

### Theorem 5.1 (pairwise one-copy extreme reserve)

For all sufficiently large `q`, one can choose one candidate ring for
every target in (0.1) so that no two selected rings share a rank-`q` owner
or a rank-`(q-1)` root.

#### Proof

Order the `M` targets arbitrarily and choose greedily.  After fewer than
`M` rings have been chosen, at most

\[
                         2\ell M                        \tag{5.3}
\]

owner/root resources have been used.  By (4.3), one used resource belongs
to at most `D` candidates in the next target list.  Hence fewer than

\[
                         2\ell M D                      \tag{5.4}
\]

candidates are forbidden.

Uniformly for `3<=j<=h-1`, equations (4.4)--(4.5) give

\[
                         {N_j\over D}=\exp(\Theta(q)),  \tag{5.5}
\]

whereas `2ell M=exp(o(q))` by (5.2).  Thus

\[
                         N_j>2\ell M D                  \tag{5.6}

\]

for all sufficiently large `q`.  At least one allowed candidate remains
at every greedy step. \(\square\)

Every selected ring comes with the internal witness (2.7) and a safe
opening arc in its omitted block.  The theorem is stronger than ordinary
target Hall at this stage: it simultaneously enforces the two one-copy
resource shores.

### Corollary 5.2 (the reserve is negligible)

The selected bank uses exactly `M` rings, `ell M` owners, `ell M` roots,
and `ell M` source positions.  At critical width,

\[
                         \ell M=\exp(o(q))=o(W/q^A)     \tag{5.7}
\]

for every fixed `A`.

Thus deleting or preplanting this bank has zero asymptotic density in both
central shores.

## 6. Complements of size zero, one, and two

The construction above starts at `j=3` only to leave an internal opening
arc in the omitted moving block.

* If `j=1`, a period-`ell` ring with unused set `X` has full-block union
  `R-X`.
* If `j=2`, a period-`(ell-1)` ring with its two-element unused set equal
  to `X` has full-block union `R-X`.
* The unique `j=0` target `R` is supplied by an interval containing two
  complete consecutive blocks with different unused sets.

The `j<=2` bank has only `1+n+binom(n,2)=O(q^2)` targets and can be added
to the same greedy reserve with no change to (5.6).  For `j=0`, the final
connector chronology must retain one adjacent pair of blocks with
different unused sets; this is a single named top ticket.

## 7. Exact remaining extension gate

Theorem 5.1 proves the following deterministic object:

\[
 \boxed{
 \text{one internal literal witness for every extreme target, on a
 pairwise owner/root-disjoint }o(W)\text{ ring bank}.}                  \tag{7.1}
\]

Two global implications are not automatic.

1. **Protected factor extension.**  The complement of this prescribed
   `o(W)` bank must still decompose into one-copy near-maximal rings.
   Small density alone does not prove exact extension.
2. **Connector compatibility.**  Every reserved witness must remain
   internal when its ring is joined into the global chronology.  Its safe
   opening lies in `X-U`, but that opening has not been shown to carry the
   buffered masked collar, companion ring states, or terminal common-cap
   tickets.

These are now the only reasons the extreme bank is not yet an
unconditional part of the all-dimensional construction.  There is no
candidate-degree, codegree, cardinality, or owner/root resource obstruction
to reserving it.

