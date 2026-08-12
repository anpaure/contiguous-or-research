# MLD exceptional whole jobs have an occurrence-faithful adjacent-tail absorber

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional lower-side absorber theorem, conditional only on the
ordinary configuration hypotheses already used by the MLD birth theorem.  The
at most `D` exceptional whole jobs left by extreme-point rounding can be
fragmented onto genuine next-depth Boolean collar occurrences.  Their capacity
types can be fixed before path realization, so MLD is preserved, and their
named tops can be matched jointly with the ordinary MLD tops.  No separate
exceptional-bank Rado or frozen-socket premise remains.  This theorem does not
co-realize the resulting collar forest with one upper-complete resident source
word.

## 1. Adjacent collars and their exact tail difference

Work in `B_(2r)`.  Put

\[
 C_s={2r\choose s},\qquad H_s=C_s-C_{s-1},\qquad W=C_r.
\tag{1.1}
\]

Let the old depth be `D>=1`, put

\[
 t=r-D,
\tag{1.2}
\]

and move to the adjacent bottom

\[
 b=t-1,
 \qquad D^+=r-b=D+1.
\tag{1.3}
\]

A collar chain born at rank `b+g` is one genuine socket occurrence of
capacity `g`.  Hence the exact capacity-`g` multiplicity in the new collar is

\[
 H_{b+g}\qquad(1\le g\le D+1),
\tag{1.4}
\]

and its capacity tails are

\[
 K_q^+=\sum_{g=q}^{D+1}H_{b+g}
      =W-C_{b+q-1}.
\tag{1.5}
\]

The old tails are

\[
 K_q=W-C_{t+q-1}\qquad(1\le q\le D).
\tag{1.6}
\]

Therefore

\[
 \boxed{K_q^+-K_q=H_{t+q-1}}
 \qquad(1\le q\le D),
\tag{1.7}
\]

while

\[
 \boxed{K_{D+1}^+=H_r.}
\tag{1.8}
\]

These are differences of actual occurrence multisets, not only differences
of total scalar capacity.

## 2. The exceptional bank

Assume the whole-job configuration extreme point, after the adjacent-depth
terminal deletion when this theorem is used inductively, leaves a family
`mathcal E` of at most `D` exceptional paths.  Every surviving path lies
strictly below the new collar bottom `b`; in particular every eventual chunk
top has rank at most `b-1`.  Let every exceptional path have length at most
`L_max`.  Split each one consecutively into pieces of
length at most `D`.  If `p` is the total number of resulting pieces, then

\[
 p\le \sum_{J\in\mathcal E}\left\lceil{|J|\over D}\right\rceil
 \le D\left\lceil{L_{\max}\over D}\right\rceil=:h.
\tag{2.1}
\]

The fragmentation is canonical once the birth length is known: take
successive blocks of length `D` and one terminal remainder.  In particular,
it does not inspect the realized Boolean path.

Let `A_q` be the number of transported ordinary pieces of length at least
`q`.  The ordinary extreme-point configurations and terminal-deletion map
satisfy

\[
 A_q\le K_q\quad(1\le q\le D),
 \qquad A_{D+1}=0.
\tag{2.2}
\]

We first give the exact finite reserve statement.

### Theorem 2.1 (capacity-faithful adjacent-tail reserve)

Let `Delta_1,...,Delta_(D+1)` be nonnegative integers.  If

\[
 h+\sum_{g=q}^{D+1}\Delta_g
 \le H_{t+q-1}
 \qquad(1\le q\le D)
\tag{2.3}
\]

and

\[
 h+\Delta_{D+1}\le H_r,
\tag{2.4}
\]

then one may simultaneously:

1. assign every ordinary piece to a distinct genuine new-collar occurrence
   of sufficient capacity;
2. assign every exceptional piece to a distinct genuine capacity-`D+1`
   occurrence;
3. leave at least `Delta_g` further capacity-`g` occurrences unused for
   every `g`.

#### Proof

Delete `h` capacity-`D+1` occurrences and, for every `g`, delete another
`Delta_g` capacity-`g` occurrences.  The remaining capacity tail at `q` is

\[
 K_q^+-h-\sum_{g=q}^{D+1}\Delta_g.
\tag{2.5}
\]

For `q<=D`, equations (1.7), (2.2), and (2.3) imply

\[
 A_q\le K_q
 \le K_q^+-h-\sum_{g=q}^{D+1}\Delta_g.
\tag{2.6}
\]

At `q=D+1`, there are no ordinary pieces.  Thus the conjugate-tail, or
sorted decreasing, matching criterion injects all ordinary pieces into the
remaining actual occurrence multiset.

Put the `p<=h` exceptional pieces on `p` of the deleted maximum-capacity
occurrences.  Their lengths are at most `D<D+1`.  The unused members of that
`h`-bank may simply remain empty.  Restore the declared `Delta_g` reserve.
Every assignment is to a distinct actual collar-chain occurrence.  `square`

With no extra spread reserve, the sufficient condition is simply

\[
 \boxed{h\le\min_{t\le s\le r}H_s.}
\tag{2.7}
\]

### Corollary 2.2 (the reserve exists eventually)

Suppose `D=O(sqrt(r))` and `L_max<=t=r-D`.  Then (2.7) holds for all
sufficiently large `r`.  The stronger inequalities (2.3)--(2.4) also hold
for the vanishing spread reserves of the pointwise-codegree theorem.

#### Proof

First,

\[
 h=D\left\lceil{L_{\max}\over D}\right\rceil
 \le D\left\lceil{t\over D}\right\rceil< t+D=r.
\tag{2.8}
\]

The strict inequality is immediate whether or not `D` divides `t`.
Uniformly in the central collar `t<=s<=r`, the standard local
central-binomial estimate gives

\[
 H_s
 ={2r-2s+1\over2r-s+1}{2r\choose s}
 \ge c{W\over r}
\tag{2.9}
\]

for an absolute `c>0` once `D=O(sqrt(r))`.  Hence

\[
 \min_{t\le s\le r}H_s\gg r>h.
\tag{2.10}
\]

For a start rank `u_g=b+g`, every chunk top has rank at most `b-1`, so put

\[
 d_g={2r-b+1\choose g+1}.
\tag{2.11}
\]

For the spread reserve

\[
 \Delta_g=
 \left\lceil A\sqrt{rC_{b+g}H_{b+g}/d_g}\right\rceil,
\tag{2.12}
\]

the tail-faithful reserve theorem proves, uniformly in `q`,

\[
 \sum_{g=q}^{D+1}\Delta_g=o(H_{t+q-1})
 \quad(q\le D),
 \qquad
 \Delta_{D+1}=o(H_r).
\tag{2.13}
\]

Since `h=O(r)` is polynomial and every displayed `H` is exponential,
(2.3)--(2.4) follow.  `square`

## 3. Fix the capacity marks before realizing the paths

There is a quantifier issue which must not be suppressed.  Sorted-tail
matching may upgrade a piece from one socket capacity to another.  If this
recolouring were performed after the Boolean paths were exposed, it would
not be a permitted MLD refinement.

The correction is exact.

### Lemma 3.1 (deterministic marked-configuration refinement)

The capacity assignment in Theorem 2.1 can be incorporated into complete
birth-configuration labels before any path geometry or future interface
matching is realized.  The resulting marked path process remains MLD.

#### Proof

The ordinary configuration counts, their piece-length multisets, the
exception counts by birth cohort, and the new exact socket multiplicities
are deterministic integers.  Run the sorted-tail matching on this finite
labelled multiset before realizing the Boolean matchings.  For each
ordinary job occurrence it produces a vector of final capacity marks, one
for each piece.  Group equal vectors inside every birth/configuration
class.  For an exceptional path of birth length `L`, use the canonical
fragmentation from Section 2 and mark every piece by capacity `D+1`.

At birth, refine each cohort uniformly into cells of exactly these marked
configuration sizes.  Eligibility depends only on the deterministic birth
rank, length, and resource table.  The MLD uniform-refinement and transport
theorem therefore preserves MLD through every later Boolean interface.
No realized target or path geometry was used in selecting a mark.  `square`

Consequently every ordinary or exceptional marked top family is a union of
birth/configuration labels.  It has the exact binomial Laplace benchmark
needed by the MLD--Hölder theorem.

## 4. Joint named-top attachment

Let `m_u` be the total number of ordinary **and exceptional** chunks marked
for collar start rank `u`.  The capacity construction gives

\[
 m_{b+g}\le H_{b+g}-\Delta_g.
\tag{4.1}
\]

At every rank, the exceptional tops are not an adversarial frozen family:
by Lemma 3.1 they are MLD labels in the same random path cover as the
ordinary tops.  Therefore they may be included directly in the weighted
multi-rank Hall statistic.

### Theorem 4.1 (one joint MLD collar matching)

Assume the reserves `Delta_g` satisfy the sharp ordinary-top concentration
condition

\[
 {\Delta_g^2d_g\over C_{b+g}H_{b+g}}\ge A_0(2r)
 \qquad(1\le g\le D+1),
\tag{4.2}
\]

with the notation of the MLD--Hölder theorem.  Then one realization of the
birth-labelled Boolean path cover admits a collar-saturated named
chainization which attaches every ordinary and every exceptional chunk to
the actual occurrence carrying its declared capacity mark.

#### Proof

For fixed `(u,T)`, sum the normalized containment indicators over all
marked top ranks, including the exceptional configuration labels.  Every
one-rank family has binomial Laplace domination by Lemma 3.1.  Generalized
Hölder gives the weighted Bernstein estimate with mean

\[
 {m_u\over C_u}
 \le {H_u-\Delta_{u-b}\over C_u}.
\tag{4.3}
\]

Condition (4.2) and the union bound give, simultaneously for every
`u,T`,

\[
 \sum_{F:\,S_F\subset T}{1\over {2r-|S_F|\choose u-|S_F|}}
 \le {H_u\over C_u}.
\tag{4.4}
\]

The pointwise codegree theorem now builds one integral augmented matching:
every rank-`u-1` continuation is matched upward and every marked request is
matched to a distinct containing rank-`u` start.  Its request images are
actual chain starts and therefore actual socket occurrences.  Applying this
at every tagged rank constructs one collar chainization containing all
ordinary and exceptional attachments.  `square`

This argument is stronger than first choosing the exceptional starts and
then asking the ordinary bulk to avoid them.  The latter would require a
new concentration theorem in a contracted start matroid.  The joint MLD
matching avoids that unnecessary gap.

### Deterministic-frozen exceptional variant

Even if one freezes the exceptional top names instead of retaining their
MLD labels, the result survives with a slightly larger reserve.  Assign all
exceptional chunks to rank `r`.  If their ranks are at most `s_max<r`, put

\[
 d_*=\min_{s\le s_{\max}}{2r-s\choose r-s}.
\tag{4.5}
\]

Their total pointwise normalized load is at most `h/d_*`.  Hence it is
enough to strengthen the rank-`r` ordinary margin so that

\[
 {h\over d_*}\le {\Delta_{D+1}\over2C_r}
\tag{4.6}
\]

and apply the MLD concentration theorem with the other half of the gap.
For the one-depth parameters, `h=O(r)` while `d_*` is superpolynomial, and
the reserve (2.11), with its constant enlarged, satisfies (4.6)
eventually.  Thus no start-matroid contraction premise is needed in either
formulation.

## 5. Exact conclusion and exact surviving obstruction

Combine the MLD birth-configuration theorem with Theorems 2.1 and 4.1.
Under the same fractional configuration and concentration hypotheses as
the ordinary MLD theorem, the complete lower ideal—including all jobs
discarded by extreme-point rounding—has

* literal target-once fragmented inclusion chains;
* a deterministic capacity mark on every chunk;
* an assignment to distinct genuine Boolean collar occurrences;
* named containment of every chunk top in its socket bottom;
* one collar-saturated chain forest realizing all those assignments.

Thus the former exceptional-bank premise

\[
 \text{``physically expose }D\lceil L_{\max}/D\rceil
 \text{ maximum sockets and attach their tops''}
\]

is closed on the lower Boolean-chain side.

What is **not** closed is source-word residence and upper-carrier
co-realization.  A collar-chain occurrence is a genuine occurrence in the
Boolean chain forest, but the present theorem does not embed that forest as
the suffix-cell system of one central owner chronology.  In particular it
does not prove, on one common word,

1. coordinate residence through `D+1` physical source positions;
2. complete arbitrary-width upper interval-OR coverage;
3. one connected owner order with the required endpoint state;
4. compatibility of the MLD path law with a separately protected carrier.

The exact remaining physical map is therefore a **protected serialization
map** from the named collar forest to occurrences of one upper-complete
resident central word.  It must preserve each socket bottom and capacity,
the target-once lower attachments, and every upper/residence guard
simultaneously.  Scalar capacity, whole-job rounding, exceptional
occurrence exposure, and named-top Hall are no longer separate
obstructions.

## 6. Dependencies

1. `MATH_THEOREM_MLD_BIRTH_CONFIGURATION_CHAINIZATION_AND_WEIGHTED_HALL_GATE_20260805.md`;
2. `MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`;
3. `MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`;
4. `MATH_THEOREM_NAMED_FRAGMENTATION_START_MATROID_RADO_AND_SMALL_FREED_SOCKET_LIFT_20260805.md`;
5. the conjugate-tail matching criterion and bipartite matching integrality.
