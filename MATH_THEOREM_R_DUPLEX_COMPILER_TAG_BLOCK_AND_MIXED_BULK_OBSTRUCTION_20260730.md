# Duplex compiler tag blocks, exact seam traces, and the mixed-bulk obstruction

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: exact lower-compiler composition theorem and sharp obstruction; no
unconditional global Pascal child.

## 0. Verdict

Fixing one common source removes a misleading Hall complication.  If a fresh
coordinate `z` occurs exactly on a declared source sector, every short source
interval has either a `z`-free label or a `z`-tagged label.  These two classes
form disjoint blocks of the exact compiler incidence graph.  For distinct
Boolean target masks, a physical interval has only one label, so after the
common-source quantifier the residual matching condition is pointwise: every
required mask must have one exact interval.  Cross-tag seam intervals are an
explicit trace bank, not scalar capacity.

This gives two deterministic composition statements.

1. An uncut canonical suspension of a complete rank-`r` parent lower compiler,
   together with modules covering all `z`-free child targets, covers every
   tagged child target except the singleton `{z}`.  One exact pure-tag source
   cell closes the whole lower compiler.
2. If the suspended parent compiler is cut at `b` source boundaries, at most
   `b binom(d,2)` distinguished parent witnesses of length at most `d` are
   destroyed.  Exact seam traces can restore them; otherwise literal appendage
   gives an overhead of at most `1+b binom(d,2)`.  For `b=O(1)` and the deadline
   scale `d=Theta(sqrt(k))`, this is `O(k)`.

There are two sharp obstructions.

* Under the nonzero parent-source convention, every canonical suspended letter
  is `{z} union Q_p` with `Q_p` nonempty.  No internal or cross-seam interval
  can then have union `{z}`.  Thus a pure-tag port is necessary, not merely a
  convenient boundary normalization.
* A full duplex round adds a second fresh coordinate `y` which the recursive
  sector avoids.  If every `z`-bearing cell lies in that `y`-free sector and
  every exterior cell is `z`-free, then every lower target containing both
  `z,y` must cross a tag boundary.  With `t` tag boundaries there are at most
  `t binom(d,2)` such short intervals, whereas a rank-`r+1` compiler on
  `2r+2` coordinates requires

  \[
      \sum_{j=0}^{r-2}\binom{2r}{j}
  \]

  distinct strict-lower masks containing `z,y`.  Hence `O(1)` or `O(k)`
  boundary ports cannot complete the two-step recursion.  A successful global
  Pascal child needs a **bulk mixed-tag module** (or comparably many tag
  alternations), not only the renewable duplex sector and seam collars.

All statements below concern the literal lower compiler.  Exact middle
ownership, upper bridge/seam completeness, residence, and the natural join of
all source fibres remain independent hypotheses.

## 1. Exact tag projection and block Hall decomposition

Let `Omega` be a finite old ground and `z` a fresh coordinate.  Fix one source
word

\[
       S=(S_0,\ldots,S_{N-1}),\qquad
       \varnothing\ne S_p\subseteq\Omega\cup\{z\}.
                                                        \tag{1.1}
\]

Put

\[
 J_z=\{p:z\in S_p\},\qquad \bar S_p=S_p\setminus\{z\}.
                                                        \tag{1.2}
\]

Let `C_d` be the nonempty contiguous source intervals of length at most `d`.
For `I in C_d`, define its old trace and tag bit by

\[
 \phi(I)=\bigcup_{p\in I}\bar S_p,
 \qquad
 \epsilon(I)=\mathbf 1[I\cap J_z\ne\varnothing].       \tag{1.3}
\]

Then its literal union is

\[
 \lambda(I)=\bigcup_{p\in I}S_p
            =\phi(I)\cup\epsilon(I)\{z\}.              \tag{1.4}
\]

Suppose a protected canonical suspended sector is an interval `P` on which

\[
            S_p=\{z\}\cup Q_p,qquad
            \varnothing\ne Q_p\subseteq\Omega.          \tag{1.5}
\]

Partition the physical interval cells into

\[
\begin{aligned}
 \mathcal C_0&=\{I:I\cap J_z=\varnothing\},\\
 \mathcal C_{z,\mathrm{int}}&=\{I:I\subseteq P\},\\
 \mathcal C_{z,\partial}&=
   \mathcal C_d\setminus
   (\mathcal C_0\cup\mathcal C_{z,\mathrm{int}}).
                                                        \tag{1.6}
\end{aligned}
\]

The last bank contains all tagged cells which are not internal to the
protected sector, including literal cross-tag and multi-seam intervals.

### Theorem 1.1 (exact tag-block decomposition)

Let `T_0` be a family of distinct required targets contained in `Omega`, and
let

\[
       \mathcal T_z=\{\{z\}\cup X:X\in\mathcal X\}      \tag{1.7}
\]

be a family of distinct tagged targets.  For the fixed source `S`, the exact
target-to-interval incidence graph has no edges between `T_0` and a tagged
cell, and no edges between `T_z` and `C_0`.  Consequently its matching number
is the sum of the matching numbers of the two tag blocks.

Moreover, for the ordinary universal-word problem, in which each Boolean mask
is required only once, a saturating matching exists if and only if

\[
\begin{aligned}
 &\forall A\in\mathcal T_0\quad
   \exists I\in\mathcal C_0:\ \phi(I)=A,\\
 &\forall X\in\mathcal X\quad
   \exists I\in
      \mathcal C_{z,\mathrm{int}}\cup\mathcal C_{z,\partial}:
      \phi(I)=X.                                      \tag{1.8}
\end{aligned}
\]

After the common source is fixed, no further Hall competition remains among
distinct target labels.

#### Proof

Equation (1.4) proves the absence of cross-block edges.  A fixed physical
interval has one literal union, and therefore is adjacent to at most one
distinct Boolean target mask.  Host families of distinct masks are disjoint.
Thus arbitrary choices of one host from each nonempty family in (1.8) are
automatically distinct.  The converse is immediate.  \(\square\)

If an auxiliary port formalism demands several occurrence-labelled copies of
the same mask, ordinary Hall inside that repeated-label block must be retained.
Theorem 1.1 is exact for literal universality, whose target vertices are the
distinct nonempty masks.

The quantifier order cannot be weakened.  For a joined source fibre
`F_*`, the exact statement is

\[
 \exists S\in\mathcal F_*\quad\text{such that all conditions in (1.8) hold}.
                                                        \tag{1.9}
\]

Separate sources for the two blocks, or Hall in the union of their incidence
graphs over `F_*`, do not give one physical word.

### Corollary 1.2 (protected interior plus boundary trace bank)

Assume, for one fixed source `S`, that

1. `C_0` covers every target in `T_0`;
2. internal suspended cells cover `{z} union X` for every
   `X in X_int subseteq X`; and
3. for every residual `X in R=X\X_int` there is a boundary cell
   `I in C_(z,partial)` with `phi(I)=X`.

Then the three packages combine into one exact lower-compiler matching.  With
the interiors frozen and every residual tagged target required to use the
boundary bank, condition 3 is also necessary.

This is the exact block composition theorem.  It uses target-labelled seam
traces, not a scalar count of seam slots.

For a fixed source, write

\[
 \Lambda_{\rm int}(S)=
   \{\phi(I):I\in\mathcal C_{z,\mathrm{int}}\}.       \tag{1.10}
\]

If every label in `X\Lambda_int(S)` occurs in the boundary bank, then the
minimum number of boundary occurrences in any completion is exactly

\[
 \boxed{\beta_z(S)=|\mathcal X\setminus\Lambda_{\rm int}(S)|.} \tag{1.11}
\]

If one of those labels has no boundary occurrence, boundary completion is
impossible.  Indeed, every missing label needs one boundary occurrence, while
choosing one occurrence for each missing label is automatically injective by
Theorem 1.1.  Thus an `O(k)` boundary-port theorem is equivalent, after the
common source is fixed, to near-complete internal tagged coverage together
with exact boundary traces.  A cardinality-one duplex germ alone gives no
such bound.

## 2. One fresh tag: the singleton theorem

Let a parent compiler have middle rank `r` on `Omega`, and suppose one fixed
parent source covers every nonempty target of rank below `r`.  Its canonical
suspension (1.5) carries every parent witness interval `I` to the tagged
target

\[
       \{z\}\cup\bigcup_{p\in I}Q_p.                 \tag{2.1}
\]

The strict lower ideal below rank `r+1` on `Omega union {z}` splits as

\[
\begin{aligned}
 \mathcal L_0'&=\{A\subseteq\Omega:1\le |A|\le r\},\\
 \mathcal L_z'&=\{\{z\}\cup A:A\subseteq\Omega,
                                      0\le |A|\le r-1\}.
                                                        \tag{2.2}
\end{aligned}
\]

### Theorem 2.1 (one pure-tag port is necessary and sufficient)

Assume one fixed collection of `z`-free modules covers `L_0'`, and the
complete parent lower compiler is retained internally in the canonical
suspended sector.  Then every target in `L_z'` except `{z}` is covered.
The combined lower compiler is complete if and only if the source word has a
nonempty interval all of whose letters are exactly `{z}`.  Equivalently, it
is enough and necessary that at least one source letter equal `{z}` occur.

In particular, a pure canonical suspended sector with nonempty parent letters,
together with exclusively `z`-free exterior modules, always misses `{z}`.
No cross-tag seam can repair it.

#### Proof

For every nonempty `A subseteq Omega` with `|A|<=r-1`, transport its parent
witness by (2.1).  The other modules supply (2.2)'s no-tag block.  A source
interval has union `{z}` exactly when it contains a `z`-bearing letter and
every letter in it has empty old projection.  Since source letters are
nonempty, every letter in such an interval equals `{z}`.  Conversely a
singleton interval at a `{z}` letter is a witness.  Under (1.5), every tagged
letter contains the nonempty set `Q_p`; adding exterior letters can only add
coordinates.  \(\square\)

Thus the compiler-side recursive port missing from a bare duplex suspension
is not another large Hall package.  At one tagged step it is precisely a
literal **pure-tag socket**.

### Lemma 2.2 (exact zeroable-cell criterion)

Suppose the canonical suspended source realizes owners at horizon `d`:

\[
       \{z\}\cup T_i
       =\bigcup_{q=i}^{i+d}(\{z\}\cup Q_q).           \tag{2.3}
\]

Fix a source position `p` and replace only its letter by `{z}`.  All owner
equations remain unchanged if and only if

\[
 Q_p\subseteq
 \bigcup_{\substack{q=i\\q\ne p}}^{i+d}Q_q
 \quad\text{for every }i\text{ with }p\in[i,i+d].    \tag{2.4}
\]

Likewise, a chosen transported witness interval `I` containing `p` keeps its
old trace if and only if

\[
       Q_p\subseteq\bigcup_{q\in I\setminus\{p\}}Q_q. \tag{2.5}
\]

Consequently, if (2.4) holds and one complete selected parent compiler can be
chosen so that every one of its intervals containing `p` satisfies (2.5),
then zeroing `p` produces the required pure-tag socket without changing the
middle owners or any selected lower witness.

#### Proof

Deleting `Q_p` from one union changes that union exactly when it contains a
coordinate supplied nowhere else.  Apply this observation first to every
incident owner window and then to every selected witness interval.  The tag
`z` remains in the modified cell, so the source letter stays nonempty and the
singleton interval at `p` realizes `{z}`.  \(\square\)

Condition (2.4), together with a compiler choice satisfying (2.5), is a
checkable PBBS/Pascal **zeroable-port condition**.  The present note does not
prove that every protected PBBS source has such a position.

## 3. Cut sectors and `O(k)` exact boundary ports

Assume here that the parent is a full linear horizon-`d` source: every
physical interval of `d+1` consecutive source positions is a declared
rank-`r` owner.  Equivalently, in a cyclic formulation assume `N>d`, count
the wrap adjacency among the declared cuts, and declare every cyclic short
arc of length `d+1` as an owner window.  This premise is not automatic for a
clipped extracted sector.

Retain one distinguished parent witness interval `I_X` for every nonempty
parent lower target `X`.  Every such interval has at most `d` source letters:
an interval of `d+1` letters contains a full owner window of rank `r` and
cannot have lower rank.

Cut the suspended source at `b` old adjacencies and rethread its resulting
pieces, without changing piece interiors.  Let `E` be the old target labels
whose distinguished intervals are destroyed and have no retained designated
alternative.

### Lemma 3.1 (sharp cut-casualty count)

At one cut, at most

\[
                       \binom d2                      \tag{3.1}
\]

distinguished intervals of length at most `d` cross the cut.  Hence

\[
                       |E|\le b\binom d2.             \tag{3.2}
\]

#### Proof

An interval crossing a fixed cut uses `u>=1` positions on its left and
`v>=1` on its right, with `u+v<=d`.  The number of positive pairs is

\[
   \sum_{\ell=2}^{d}(\ell-1)=\binom d2.
\]

Each distinguished target has only one selected interval, and a union bound
over the cuts proves (3.2).  Equality in the one-cut occurrence count is
possible.  \(\square\)

For a new seam `c`, write its old-coordinate suffix and prefix traces as

\[
 L_c(u)=\bigcup_{j=0}^{u-1}\bar S_{c-j},
 \qquad
 R_c(v)=\bigcup_{j=1}^{v}\bar S_{c+j}.               \tag{3.3}
\]

The literal crossing interval with `u` left and `v` right positions has old
trace

\[
                  L_c(u)\cup R_c(v),                 \tag{3.4}
\]

and is tagged exactly when one of its positions belongs to `J_z`.  If seams
are less than `d` positions apart, intervals crossing several seams must be
included as full suffix--whole-block--prefix traces; the one-seam grids are
not exhaustive in that case.

### Theorem 3.2 (deterministic cut-and-seam compiler composition)

Under the hypotheses of Theorem 2.1, allow `b` cuts of the suspended parent
compiler and retain every distinguished witness not in `E`.  Assume:

1. there is one pure-tag socket;
2. for every `X in E`, some allowed new tagged seam interval has old trace
   exactly `X`; and
3. the no-tag modules still cover `L_0'` under the same common source.

Then all strict child lower targets are covered by one literal source.  The
boundary repair uses at most

\[
                    1+b\binom d2                     \tag{3.5}
\]

target-labelled occurrence ports.  No additional matching or independence
choice is required.

If condition 2 fails for `e` distinct residual labels, appending those `e`
tagged masks and, when absent, the singleton `{z}` gives a literal
lower-coverage word with overhead at most `1+b binom(d,2)`.  If the retained
prefix already covers the complete middle and upper ideals, this is a
universal-word upper bound.  The appendage assertion does not preserve
`D^dS=T`, the fixed deadline carrier, or its endpoint type.

#### Proof

The retained internal intervals transport all tagged parent targets outside
`E`.  Conditions 1--2 supply `{z}` and the lost tagged targets; condition 3
supplies the no-tag block.  Theorem 1.1 composes them.  Equation (3.5) is
Lemma 3.1 plus the singleton port.  Literal appendage cannot destroy any old
witness.  \(\square\)

When `b=O(1)` and `d=Theta(sqrt(k))`, (3.5) is `O(k)`.  This order is sharp
from cut geometry alone: one cut has `binom(d,2)` crossing short intervals,
and a source with successively fresh singleton old traces makes all their
unions distinct.  Residence or source suspension does not improve the count
to `O(d)` without an additional cut-sparse matching hypothesis.

The theorem is an exact trace theorem, not a scalar-capacity result.  Every
residual label must occur in (3.4), or in the corresponding full multi-seam
trace, under the same source that realizes the owners.

## 4. A full duplex round needs a bulk mixed-tag compiler

The one-tag theorem does not iterate merely by copying the sector and adding
seam ports.  Let `r>=2`, let `Omega` have size `2r`, and enlarge it by fresh coordinates
`z,y`.  The new even middle rank is

\[
                         R=r+1.                     \tag{4.1}
\]

Let a linear source `S` satisfy `D^dS=T` for a rank-`R` middle chronology, so
every physical interval of `d+1` consecutive source positions is a rank-`R`
owner.  Assume
there is a set `P` of protected-sector source positions such that

\[
\begin{array}{ll}
 p\in P:& z\in S_p,\ y\notin S_p,\\
 p\notin P:& z\notin S_p.
\end{array}                                          \tag{4.2}
\]

Thus the renewable sector bears `z` and avoids `y`, while every exterior
module is `z`-free.  Let `t` be the number of adjacent source pairs on which
membership in `P` changes.  In a cyclic version the wrap adjacency must also
be counted.

### Theorem 4.1 (mixed-bulk boundary obstruction)

If the source covers the complete strict lower ideal below rank `R`, then

\[
 \boxed{
 t\binom d2\ \ge\
 M_r:=\sum_{j=0}^{r-2}\binom{2r}{j}.}                \tag{4.3}
\]

In particular, at deadline scale `d=Theta(sqrt(r))`, neither `t=O(1)` nor
`t=O(r)` is possible for all sufficiently large `r`.

#### Proof

For every `X subseteq Omega` with `|X|<=r-2`, the mask

\[
                        \{z,y\}\cup X                \tag{4.4}
\]

has rank at most `r=R-1` and is therefore a required strict-lower target.
There are exactly `M_r` such distinct masks.

Every source interval realizing a target of rank below `R` has at most `d`
letters: an interval of `d+1` letters contains a complete owner window of
rank `R`.  By (4.2), an interval whose union contains both `z` and `y` must
meet `P` and its complement, hence cross at least one of the `t` tag
boundaries.  Lemma 3.1 bounds the number of length-at-most-`d` intervals
crossing all those boundaries by `t binom(d,2)`.  One physical interval has
one union label, so these intervals can realize at most that many distinct
masks in (4.4).  This proves (4.3).  The asymptotic conclusion follows
because `M_r` is exponential in `r`.  \(\square\)

The obstruction survives adding one pure `{z}` cell and any `O(k)` catalogue
of ordinary seam ports.  It is not an obstruction to a different global
Pascal braid in which some bulk module bears both `z` and `y`, or in which
`z` alternates between modules exponentially often.

An exact necessary bulk condition follows under an explicit exhaustive
dichotomy.  Suppose a declared family of internally mixed modules realizes
`s` of the targets in (4.4), and every witness of each remaining mixed target
must cross one of the `t` charged boundaries (so `t` includes every possible
escape boundary).  Then

\[
                  s+t\binom d2\ge M_r.               \tag{4.5}
\]

Thus, under that dichotomy, a bounded-boundary construction must supply all
but `O(k)` of the mixed family through bulk internal witnesses.  Without the
exhaustive-boundary hypothesis, (4.5) is not asserted: an uncharged mixed
module relaxes (4.2) and can evade the count.  This is the compiler-side
content missing from a sector-only duplex induction.

## 5. Exact remaining PBBS/Pascal hypotheses

For one fresh-tag step, the weakest useful positive condition exposed here is:

> **Zeroable suspended compiler port (unproved for PBBS).**  There is one
> source position satisfying the owner redundancy conditions (2.4), and a
> complete parent lower witness selection satisfying (2.5), while every cut
> casualty is present in the exact seam trace bank (3.3)--(3.4).

Together with a same-source no-tag compiler, this condition gives an exact
one-step lower compiler by Theorem 3.2.  With no cuts, it is an `O(1)` port;
with `O(1)` cuts, it is an `O(k)` occurrence bank at the natural deadline
scale.

For a complete two-coordinate duplex round, this is insufficient.  The
minimal additional large-scale statement is:

> **Mixed-bulk compiler lemma (unproved).**  A Pascal/PBBS child contains a
> module with internal literal witnesses for all but `O(k)` masks in the
> mixed family (4.4), under the same common source used by the suspended
> compiler and the no-tag modules.

Theorem 4.1 proves that some hypothesis of this bulk size is necessary under
bounded tag-boundary complexity.  Therefore the global duplex-embedding lemma
cannot be closed by an `O(1)` or `O(k)` seam-only Hall argument.

## 6. Audit boundary

The proofs use only set unions, the rank separation of intervals shorter than
one owner window, and exact interval counting.  No finite search or
certificate data enter.

The following scope restrictions are essential.

1. The block-Hall collapse occurs only after fixing one common source.
2. Theorem 2.1 assumes complete internal retention of one parent lower
   compiler and separate coverage of the entire no-tag child block.
3. The cut count charges one distinguished witness per target.  It does not
   claim that all possible witnesses crossing a cut are simultaneously
   protected.
4. Seam capacity alone is never sufficient; exact trace equality is required.
5. Theorem 4.1 assumes the support separation (4.2).  Bulk modules containing
   both fresh coordinates evade it and are precisely the required new object.
6. None of the lower-compiler statements supplies middle ownership, upper
   completeness, residence, or endpoint legality.
