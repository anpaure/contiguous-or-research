# Safe-pair Shadow--Braids, deleted-seam grids, and the exact bounded-overhead gate

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: proved reusable upper-shadow linearization theorem; proved exact
catalogue theorem for disjoint adjacent OR-braids; proved a resident
reverse-grid obstruction showing that boundedly many such braids do not
follow from residence, local q1 squarefreeness, and the existence of a
quadratic cyclic upper-witness family.  No unconditional all-
dimension upper bound is claimed.

## 0. Outcome and exact boundary

Let

\[
 r=\lceil k/2\rceil,\qquad W={k\choose r},\qquad
 d=d(k),\qquad B(k)=W+d,
\]

with `d(k)` defined by the proved monotone-deadline lower bound.  The exact
carrier/compiler theorem says that a rank-`r` owner path `T` gives a word of
length `B(k)` once

1. `T` has a nonzero antecedent `A` with `D^d A=T` covering every target
   below rank `r`; and
2. every target above rank `r` is an interval union of `T`.

This note removes the second condition at an explicit, deterministic price.
If `T` is obtained by opening `c` cyclic components whose cyclic upper
intervals are complete, then all upper witnesses lost at the cuts can be
restored by appending at most

\[
                 c\bigl(2(k-r)+1\bigr)                 \tag{0.1}
\]

nonzero letters.  The sharper price is the sum of the two strict boundary-
union chain lengths at the actual cuts.  Thus, conditional only on the
lower compiler and residence hypotheses,

\[
 \nu(k)\le B(k)+\sum_e\gamma(e)
       \le B(k)+c\bigl(2(k-r)+1\bigr).                 \tag{0.2}
\]

The price is not an artefact of a loose proof.  There is an explicit
depth-`d`-resident, locally q1-rainbow Johnson cycle whose one opened edge
has

\[
                  \frac{s(s+1)}2,qquad s=k-r-1,       \tag{0.3}
\]

distinct upper targets witnessed only across that edge.  Any repair of its
antecedent by `t` pairwise disjoint adjacent replacements preserving each
edited pair OR must satisfy

\[
 \frac{s(s+1)}2
 \le 2t(k+1).                                           \tag{0.4}
\]

For the centered odd parameters this forces `t=Omega(k)`.  Hence residence,
q1 exactness on the component, and cyclic upper witnesses do **not** imply a
bounded local Shadow--Braid repair.

The precise bounded-overhead condition left by the theorem is the following.
After the Pascal/PBBS interiors are fixed, the seam-exclusive upper targets
must admit either

* a bounded total boundary-chain collar, or
* a bounded protected **safe-pair socket cover** in the exact catalogue of
  Theorem 3.1 below.

This is an additional post-cut condition, separate from cyclic all-depth
support and from the common lower compiler Hall condition.  The local
reverse-grid example proves nonimplication from the weaker hypotheses just
listed; it is not asserted to extend to a complete all-depth factor.  The
socket condition is the minimal additional condition inside the declared
collar/safe-pair architecture.

## 1. Notation and the upper projection identity

For a finite nonempty set word `X=(X_0,...,X_{N-1})`, write

\[
  \operatorname{Int}(X)
   =\left\{\bigcup_{i=a}^bX_i:0\le a\le b<N\right\}.
\]

For `q>=0`, put

\[
 (D^qX)_i=\bigcup_{j=0}^qX_{i+j}.
\]

We repeatedly use the following local form of the established
carrier/compiler factorization.

### Lemma 1.1 (upper intervals project to the owner path)

Let `T=(T_0,...,T_{M-1})` be a rank-`r` word and let `A` be a nonzero word
of length `M+d` satisfying `D^dA=T`.  If an interval of `A` has union `U`
with `|U|>r`, then

\[
             U=T_a\cup T_{a+1}\cup\cdots\cup T_b       \tag{1.1}
\]

for a nonempty consecutive interval of `T`.

#### Proof

Every interval of at least `d+1` source cells contains a full
`(d+1)`-window and therefore has rank at least `r`.  An interval of at most
`d` cells cannot have rank above `r`: every source cell is contained in all
owner windows using it, hence in the maximal erosion envelope, and the
standard intersection-tower identity bounds such a union by rank `r`.
Thus an interval for `U` has at least `d+1` cells.

Write the source interval as `[u,v]`.  Since `v-u+1>=d+1`, the full windows
contained in it have starts

\[
                  u\le i\le v-d.                     \tag{1.2}
\]

This range lies in `0<=i<M`: the source has length `M+d`, so
`v-d<=M-1`, while an interval of length `d+1` cannot start after `M-1`.
The windows in (1.2) cover every source position from `u` through `v`.
Taking their union therefore gives exactly the source interval, while each
window is one consecutive `T_i`.  This proves (1.1).  This is the same
argument as the converse direction of the exact linear chronology/compiler
theorem.  \(\square\)

The assertion uses the exact equality `D^dA=T`; separate rankwise rows do
not suffice.

## 2. The exact boundary grid of one deleted cycle edge

Let

\[
             Q=(X_0,X_1,\ldots,X_{L-1})              \tag{2.1}
\]

be a linearization of a cyclic rank-`r` set word obtained by deleting the
closure edge `X_(L-1)X_0`.  Define its prefix and suffix union chains

\[
 R_j=\bigcup_{i=0}^jX_i,
 \qquad
 L_i=\bigcup_{j=i}^{L-1}X_j.                         \tag{2.2}
\]

Delete repetitions and index the distinct chains increasingly as

\[
 R^0\subsetneq R^1\subsetneq\cdots\subsetneq R^b,
 \qquad
 L^0\subsetneq L^1\subsetneq\cdots\subsetneq L^a,    \tag{2.3}
\]

where `R^0=X_0` and `L^0=X_(L-1)`.

### Lemma 2.1 (deleted-seam grid)

The union labels of all cyclic intervals crossing the deleted closure edge
are exactly

\[
 \mathcal X(Q)=
 \{L_i\cup R_j:1\le i<L,\ 0\le j<i\}.                \tag{2.4}
\]

In particular they lie in the compressed boundary-grid envelope

\[
 \overline{\mathcal J}(Q)=
 \{L^p\cup R^q:0\le p\le a,\ 0\le q\le b\}.          \tag{2.4a}
\]

Moreover

\[
                         a,b\le k-r.                   \tag{2.5}
\]

If `Q` is a strict Johnson path and the union of its component is `[k]`,
then `a=b=k-r`.

#### Proof

A cyclic interval crossing the closure starts at some `X_i`, follows the
suffix through `X_(L-1)`, and ends at `X_j` after the closure.  Without
repeating a vertex this is exactly the condition `j<i`, proving (2.4).
Compressing the two chains gives containment in (2.4a).  Not every pair in
the Cartesian envelope need satisfy the original index compatibility; the
envelope is deliberately a safe superset.  Each strict step in either union
chain raises its rank by at least one, from the initial rank `r` to at most
`k`, proving (2.5).

For a Johnson path, adjoining the next owner to a running union introduces
at most its single inserted coordinate.  If the full component union is
`[k]`, the rank must rise from `r` to `k` in exactly `k-r` strict steps on
each side.  \(\square\)

The two chains may have many repeated joins.  Formula (2.4), including its
index compatibility, is the exact signature; (2.4a) is the envelope used by
the universal collar.

### Theorem 2.2 (explicit nonzero pair collar)

Put

\[
 \Delta L_p=L^p\setminus L^{p-1}\quad(1\le p\le a),
 \qquad
 \Delta R_q=R^q\setminus R^{q-1}\quad(1\le q\le b),  \tag{2.6}
\]

and `Z=L^0 union R^0`.  Then the nonzero word

\[
 C(Q)=\bigl(
   \Delta L_a,\ldots,\Delta L_1,
   Z,
   \Delta R_1,\ldots,\Delta R_b
          \bigr)                                      \tag{2.7}
\]

has length

\[
                 \gamma(Q)=a+b+1\le2(k-r)+1,          \tag{2.8}
\]

and contains every member of \(\overline{\mathcal J}(Q)\), hence every exact
crossing label in \(\mathcal X(Q)\), as an interval union.

#### Proof

All increments in (2.6) are nonempty by strictness of the compressed
chains, and `Z` is nonempty.  For fixed `p,q`, take the interval beginning
at `Delta L_p` (or at `Z` if `p=0`) and ending at `Delta R_q` (or at `Z` if
`q=0`).  Its union is

\[
 Z\cup\bigcup_{u=1}^p\Delta L_u
   \cup\bigcup_{v=1}^q\Delta R_v
 =L^p\cup R^q.                                       \tag{2.9}
\]

This proves both claims.  \(\square\)

### Theorem 2.3 (upper-shadow linearization at explicit cost)

Let `F` be a cycle cover on a set of rank-`r` owners.  Assume every desired
upper target is a cyclic interval union in some component of `F`.  Delete
one edge from each of its `c` components, orient the resulting paths, and
join them in any order to form an owner path `T`.  Suppose there is a
nonzero antecedent `A` with

\[
                         D^dA=T                       \tag{2.10}
\]

which covers every desired target of rank below `r`.

For each deleted edge `e`, form its collar `C_e` from Theorem 2.2.  Then

\[
                 A^+=A\,C_{e_1}\cdots C_{e_c}        \tag{2.11}
\]

covers every desired lower, middle, and upper target, and

\[
 |A^+|=|A|+\sum_e\gamma(e)
      \le |A|+c\bigl(2(k-r)+1\bigr).                 \tag{2.12}
\]

In particular, if the owner set is the complete rank-`r` layer,
`|A|=W+d=B(k)`, and `A` solves `COMP_d(T)`, then

\[
 \boxed{
 \nu(k)\le B(k)+\sum_e\gamma(e)
       \le B(k)+c\bigl(2(k-r)+1\bigr).}              \tag{2.13}
\]

#### Proof

Appending letters destroys no old interval witness.  Lower targets and the
middle owner windows therefore remain covered.  Let `U` be an upper target
and choose a cyclic witness in one component of `F`.  If it avoids the cut,
it is a consecutive interval of `T`, so (2.10) and Lemma 1.1's forward
identity give the same union on the corresponding source interval of `A`.
If it crosses the cut, Lemma 2.1 puts it in \(\mathcal X(Q)\), and Theorem 2.2 realizes
it inside the appended collar for that component.  Summing (2.8) proves
(2.12)--(2.13).  \(\square\)

For windows of at most `H+1` owners, truncate both chains after the first
`H` boundary transitions; the corresponding price is at most `2H+1` per
cut.  For arbitrary width one uses the full compressed chains.  Their number
of strict changes is at most `k-r`, even though those changes may occur only
after many more than `k-r` physical transitions; no bounded-window claim is
being made.

For odd `k=2m+1`, `r=m+1`, a full-support component has
`gamma=2m+1=k`.  Thus the raw collar is never constant-size in a growing
dimension.  The exact `k=15` construction avoids paying it because the
chosen joined path already has complete arbitrary-width upper support.

## 3. Exact catalogue for disjoint adjacent OR-braids

Let `A=(A_0,...,A_(n-1))`.  Choose pairwise disjoint adjacent blocks

\[
                    E_j=\{p_j,p_j+1\},\qquad 1\le j\le t,             \tag{3.1}
\]

and replace their two nonempty letters by nonempty letters
`B_(p_j),B_(p_j+1)` satisfying

\[
 B_{p_j}\cup B_{p_j+1}=A_{p_j}\cup A_{p_j+1}.         \tag{3.2}
\]

All other letters stay fixed.  Call this a disjoint safe-pair braid.

An interval is **protected** when it contains both positions or neither
position of every edited block.

For one edited block `j`, define its two endpoint-chain families in the new
word `B`:

\[
 \mathcal L_j=\left\{
    \bigcup_{i=a}^{p_j}B_i:0\le a\le p_j
                    \right\},                         \tag{3.3}
\]

\[
 \mathcal R_j=\left\{
    \bigcup_{i=p_j+1}^{b}B_i:p_j+1\le b<n
                    \right\}.                         \tag{3.4}
\]

### Theorem 3.1 (safe-pair Shadow--Braid catalogue)

The following statements hold.

1. Every protected interval has exactly the same union in `A` and `B`.
2. Every interval label of `B` which is not already forced by a protected
   interval belongs to

   \[
       \mathcal N(B)=
       \bigcup_{j=1}^t(\mathcal L_j\cup\mathcal R_j). \tag{3.5}
   \]
3. Each family in (3.3)--(3.4) is nested and has at most `k+1` distinct
   labels.  Consequently

   \[
       |\mathcal N(B)|
       \le 2t(k+1).                                    \tag{3.6}
   \]
4. Let `H` be a target family absent from `A`.  If `B` covers `H`, then
   `H subseteq N(B)` and in particular

   \[
                  |H|\le2t(k+1).                       \tag{3.7}
   \]
5. Conversely, suppose every target outside `H` has a protected witness in
   `A` and `H subseteq N(B)`.  Then `B` covers every target covered by `A`
   together with `H`.

#### Proof

If an interval contains both edited letters, their contribution to its OR
is unchanged by (3.2); if it contains neither, nothing changes.  This proves
item 1 simultaneously for all blocks.

A contiguous interval can partially meet at most two edited blocks: its
left endpoint can lie in the second cell of one block, and its right
endpoint can lie in the first cell of one block.  Every edited block strictly
between those endpoints is fully contained.  If exactly one block is met
partially, the interval is one of (3.3) or (3.4).  If two blocks `i<j` are
met partially, the interval `[p_i+1,p_j]` ends at the first cell of block
`j` and starts at the second cell of block `i`; hence it belongs to both
`L_j` and `R_i`.  Thus no separate pair-of-block bridge family is needed.
This proves item 2.

As the free endpoint in (3.3) or (3.4) moves outward, the union only grows.
A strictly growing chain of subsets of `[k]` has at most `k+1` values.
This proves (3.6).  An absent old target covered by `B` must be supplied by
an interval whose label changed, giving item 4 and (3.7).  Finally item 1
preserves all declared protected witnesses, while the inclusion in item 5
supplies every new target.  \(\square\)

The theorem is literal: all protected targets belong to one common physical
word.  It is not a collection of independent rankwise switches.

### Corollary 3.2 (compiler-ready safe-pair criterion)

Let `T` be a rank-`r` owner path and let `A` be a length-`W+d` solution of
`COMP_d(T)`.  Let `H` be the upper targets absent from `T`.  A disjoint
safe-pair braid of `A` produces an optimal universal word if

1. every lower target and every middle owner has a protected source witness;
2. every upper target already present in `T` has a protected source witness;
   and
3. `H subseteq N(B)`.

Under these hypotheses `nu(k)=B(k)`.

#### Proof

Theorem 3.1 preserves all old witnesses and supplies `H`.  The resulting
word has length `W+d=B(k)`, while the monotone-deadline theorem gives the
reverse inequality.  \(\square\)

Condition 3 is an exact finite socket-cover condition, not a marginal count.
Inequality (3.7) is its first necessary cut.  Overlapping pair moves,
three-cut segment transpositions, or operations which change a full-OR gap
are outside the theorem; those are precisely the known ways to evade the
catalogue.

## 4. A resident reverse-grid obstruction

The next family proves that the bounded safe-pair condition is not a
consequence of residence or of the existence of cyclic upper witnesses.

Fix `s>=1`, put

\[
             k=2s+3,\qquad r=s+2,                    \tag{4.1}
\]

and partition the ground set as

\[
 C=\{c_0,c_1,\ldots,c_s\},\qquad
 X=\{x_1,\ldots,x_s\},\qquad
 \{a,b\}.                                             \tag{4.2}
\]

For `0<=q<=s`, define rank-`r` states

\[
 Z_q=
 (C\setminus\{c_1,\ldots,c_q\})
 \cup\{b,x_s,x_{s-1},\ldots,x_{s-q+1}\},             \tag{4.3}
\]

\[
 Y_q=
 (C\setminus\{c_1,\ldots,c_q\})
 \cup\{a,x_1,x_2,\ldots,x_q\}.                       \tag{4.4}
\]

Empty displayed `x`-ranges are omitted.  Consider the cycle

\[
 Z_0,Z_1,\ldots,Z_s,Y_s,Y_{s-1},\ldots,Y_0,Z_0.       \tag{4.5}
\]

### Theorem 4.1 (reverse-grid cycle)

The cycle (4.5) has all of the following properties.

1. It is a simple strict Johnson cycle, and all its q1 edge colours are
   pairwise distinct.
2. After deleting the closure `Y_0Z_0`, the path

   \[
       Q=Z_0,\ldots,Z_s,Y_s,\ldots,Y_0                \tag{4.6}
   \]

   is strongly depth-`d` resident for every `1<=d<=s`.
3. For every `p,q>=0` with `p+q<=s-1`, the upper target

   \[
    U_{p,q}=C\cup\{a,b\}
       \cup\{x_1,\ldots,x_p\}
       \cup\{x_{s-q+1},\ldots,x_s\}                  \tag{4.7}
   \]

   has a cyclic witness crossing `Y_0Z_0` and has no interval witness in
   the open path `Q`.  These targets are pairwise distinct, so their number
   is exactly

   \[
                        h_s={s(s+1)\over2}.            \tag{4.8}
   \]
4. Let `P` be the maximal depth-`d` erosion of `Q`.  Then `P` is nonzero,
   `D^dP=Q`, and none of the `h_s` targets occurs in `P`.

#### Proof

Every displayed state has `(s+1)-q+1+q=s+2=r` elements.  Consecutive
`Z` states exchange `c_q` for one new `x`; consecutive `Y` states do the
reverse exchange.  The middle edge exchanges `a,b`, as does the closure.
The `Z` states contain `b` but not `a`, the `Y` states contain `a` but not
`b`, and their `x`-prefixes differ, so all states are distinct.  The q1
colours on the `Z` arm contain `b`, those on the `Y` arm contain `a`, and
the middle and closure colours contain neither.  Within each arm the
deleted `c`/present `x` pattern identifies the edge.  Thus all q1 colours
are distinct.

In the open path, `a` and `b` occur only in boundary runs.  Each `c_j`
with `j>=1` occurs in one left and one right boundary run; `c_0` occurs
everywhere.  Coordinate `x_j` occurs in one internal run from its insertion
on the `Z` arm through its deletion on the `Y` arm.  That run has exactly
`s+1` states.  Hence every internal positive run has length at least `d+1`
for `d<=s`.

The suffix `Y_p,Y_(p-1),...,Y_0` has union

\[
             C\cup\{a,x_1,\ldots,x_p\},              \tag{4.9}
\]

while the prefix `Z_0,...,Z_q` has union

\[
             C\cup\{b,x_{s-q+1},\ldots,x_s\}.        \tag{4.10}
\]

Their cyclic concatenation gives (4.7).  Distinct pairs with `p+q<s`
omit distinct nonempty middle intervals

\[
                     \{x_{p+1},\ldots,x_{s-q}\},      \tag{4.11}
\]

so the labels are distinct and (4.8) follows.

Any noncrossing interval containing both `a` and `b` must span the middle
edge `Z_sY_s`.  In order also to contain every `c_j`, it must reach `Z_0`
or `Y_0`: already `c_1` forces one of those alternatives.  Such an interval
passes through an arm endpoint and the middle, and therefore contains every
`x_j`; its union is `[k]`.  The targets in (4.7) omit a nonempty interval of
`X`, so none is a path interval.

Strong residence and `r-d>=2` make the maximal erosion nonzero and give
`D^dP=Q`.  Lemma 1.1 now shows that an upper target absent from `Q` is also
absent from `P`.  \(\square\)

### Corollary 4.2 (linear safe-pair lower bound)

If a word obtained from `P` by `t` pairwise disjoint safe-pair braids covers
all targets (4.7), then

\[
       {s(s+1)\over2}
       \le2t(k+1),                                    \tag{4.12}
\]

and hence

\[
 t\ge\left\lceil {s(s+1)\over4(k+1)}\right\rceil.   \tag{4.13}
\]

In particular `t=Omega(k)` as `s` tends to infinity; more precisely,

\[
                  t\ge(1/16+o(1))k.                  \tag{4.14}
\]

#### Proof

All `h_s` targets are absent from `P`, so Theorem 3.1(4) gives (4.12).
Rearranging gives (4.13).  Since `s=(k-3)/2`, its right side is
`(1/16+o(1))k`, proving (4.14).  \(\square\)

## 5. Residence is a separate seam-transversal condition

For a cycle/path cover `F`, let `nu_H(F)` be the maximum number of pairwise
transition-edge-disjoint positive coordinate-run intervals of length at
most `H`.  Suppose `F'` is obtained by deleting `J_-` transition edges,
retaining and possibly reversing every resulting interior, and inserting
`J_+` new seams.  The proved seam-cost identity is

\[
 \boxed{
 |\nu_H(F')-\nu_H(F)|\le\max(J_-,J_+).}               \tag{5.1}
\]

For completeness, the proof is one line after the correct common family is
chosen.  Let `U` be the short runs wholly inside retained interiors.  Every
old packed run outside `U` contains a distinct deleted edge, and every new
packed run outside `U` contains a distinct inserted edge.  Hence

\[
 \nu_H(U)\le\nu_H(F)\le\nu_H(U)+J_-,
 \qquad
 \nu_H(U)\le\nu_H(F')\le\nu_H(U)+J_+,                \tag{5.2}
\]

which gives (5.1).  Multi-seam runs and reversed interiors cause no change.

Consequently, reaching any target class with `nu_H<=b` from a source with
packing `N` requires

\[
                     \max(J_-,J_+)\ge N-b.            \tag{5.3}
\]

This does not charge word length: a seam can be length-neutral.  It does
prove that a bounded local connector cannot manufacture residence from a
source whose short-run packing diverges.  Residence and upper-grid
absorption are therefore two independent braid requirements.

## 6. Reusable bounded-overhead theorem

The preceding results can be packaged without reference to a particular
PBBS grammar.

### Theorem 6.1 (collar or safe-pair all-`k` interface)

Fix `k,r,d,W` with `W=binom(k,r)`.  Suppose a cyclic rank-`r` owner factor
has complete desired cyclic upper support.  Suppose cuts, orientations and
joins produce a path `T` for which `COMP_d(T)` is feasible; let `A` be its
nonzero lower-complete antecedent.

Then either one of the following independently suffices.

1. **Boundary-collar alternative.**  Append the collars of Theorem 2.2.
   The resulting universal word has length

   \[
                         W+d+\sum_e\gamma(e).          \tag{6.1}
   \]

2. **Zero-cost protected-braid alternative.**  Find disjoint source pairs
   and same-OR replacements satisfying Corollary 3.2.  The resulting word is
   universal at unchanged length `W+d`.

If `r` and `d` are the monotone-deadline parameters, alternative 1 proves

\[
                 \nu(k)\le B(k)+C                     \tag{6.2}
\]

whenever `sum_e gamma(e)<=C`; alternative 2 proves `nu(k)=B(k)`.

#### Proof

Alternative 1 is Theorem 2.3.  Alternative 2 is Corollary 3.2 followed by
the deadline lower bound.  \(\square\)

### Exact minimal countercondition in this architecture

For a uniform constant-additive theorem based on either one of the two
declared alternatives, the corresponding concrete condition is as follows.

* The sum of the actual compressed deleted-seam chain costs is bounded:
  `sum gamma(e)=O(1)`.
* The seam-exclusive upper family is contained in the exact protected
  safe-pair socket catalogue (3.5) of `O(1)` disjoint pairs.

The first condition is exactly what makes the displayed collar bound
constant.  The second is necessary and sufficient inside the protected
safe-pair class.  These are not asserted necessary for arbitrary words or
overlapping/nonlocal trades.  The reverse-grid
family proves that neither follows from depth-`d` residence, locally
squarefree q1 colours, and the displayed quadratic family of cyclic upper
witnesses.  It does not by itself refute an implication using the complete
PBBS all-depth factor as an additional hypothesis.  An all-`k` proof which
does not establish one of them must use an operation outside this class:
overlapping packets, a nonlocal segment braid, or an edit which opens a
full-OR gap and therefore changes the two-chain signature itself.

### Corollary 6.2 (deadline-tight consequence)

Fix a constant `C`.  In any growing family with `k-r` tending to infinity,
the raw boundary-collar alternative cannot give `B(k)+C` if even one opened
component has full coordinate union: Lemma 2.1 gives

\[
                     \gamma(e)=2(k-r)+1>C              \tag{6.3}
\]

for all sufficiently large `k`.  At exact equality `B(k)` there is no
positive collar budget at all.  Therefore a deadline-tight or uniformly
constant-additive proof based on full-support components must recycle their
seam-exclusive grids inside the final word, for example through the
protected socket condition of Theorem 3.1; cyclic support and later literal
appendage via the raw collar alone cannot do it.

#### Proof

The monotone-deadline theorem fixes the baseline at `B(k)`.  Theorem 2.3
adds exactly `sum gamma(e)` letters, and a full-support component has the
value in (6.3).  The conclusion follows.  \(\square\)

For Pascal lifts, the exact facet/union transducer identities transport all
interior lower and upper flags.  Hence only occurrences crossing the chosen
Pascal seams enter the socket condition.  The facet sector spends one unit
of one-run buffer, the union sector spends one unit of zero-gap buffer, and
the OR-neutral local triangle creates trace `1,0,1`; these proved facts are
fully consistent with (5.1) and show why the socket and residence conditions
must be checked simultaneously.  Likewise, the appended collar of Theorem
2.2 is an arbitrary-upper support repair only.  Its extra letters shift
fixed-depth windows and are not automatically residence-safe or compatible
with `COMP_d`; no such inference is made in Theorem 2.3, where the collar is
placed after the already compiled word and used only for literal upper
coverage.

## 7. Calibration and nonclaims

1. **`k=15`.**  Here `(r,d,W)=(8,3,6435)`.  The certified two-cycle opening
   already has complete arbitrary-width upper support and feasible
   `COMP_3`; hence the safe-pair theorem applies with an empty hole family
   and `t=0`.  The two missing q1 colours are handled by the separate exact
   two-boundary compiler pins.  This recovers length `B(15)=6438` without
   paying the crude collar bound `2*15`.
2. **`k=16`.**  The authenticated length-12874 word proves
   `B(16)<=nu(16)<=B(16)+1`, but it is not asserted to lie in the flat-middle
   or disjoint safe-pair class.  It neither proves nor contradicts Theorem
   6.1.
3. **PBBS.**  PBBS supplies cyclic all-depth flag support and at most
   `Cat_m` components in odd dimension.  Theorem 2.3 therefore buys the
   arbitrary-upper linearization gate at explicit cost at most
   `(2m+1)Cat_m=W`, conditional on the separate residence and compiler
   hypotheses.  This observation is not an unconditional `2W` word because
   those two hypotheses remain open.
4. **No false implication.**  The theorem does not infer the common compiler
   from containment Hall, does not infer residence from mean run length, and
   does not infer upper survival from cyclic support.  Each inference is
   isolated as a separate exact hypothesis.
5. **Deadline equality scope.**  The positive-slack identity
   `sigma=Delta_depth+Delta_repeat` does not force a flat middle derivative.
   This report therefore treats `D^dA=T` as the established sufficient
   carrier/compiler normal form, not as a characterization of every word of
   length `B(k)` or `B(k)+C`.

## 8. Adversarial proof audit

An independent root-level proof pass checked the collar construction, the
safe-pair catalogue after removal of the redundant bridge term, the
reverse-grid exclusivity/residence argument, and the `1/16` constant.  It
also forced the explicit indexing in Lemma 1.1 and the scope correction that
the local reverse-grid is not a complete PBBS all-depth factor.  The final
adversarial ledger is as follows.

1. The collar word is ordered `Delta L_a,...,Delta L_1,Z,Delta R_1,...`;
   reversing the left increments is essential.  In the opposite order a
   contiguous suffix would not produce `L^p`.
2. Empty increments are removed before the collar is formed.  Hence every
   appended letter is nonzero.
3. An interval can partially meet at most two disjoint adjacent pairs.  A
   third partial pair would lie strictly between its endpoints and would
   therefore be wholly contained.  This is the decisive catalogue step.
4. No separate bridge term is needed: an interval partially meeting two
   blocks belongs simultaneously to the left chain of its rightmost block
   and the right chain of its leftmost block.  This strengthens the capacity
   upper bound to `2t(k+1)`.
5. The reverse-grid count includes only `p+q<s`.  All pairs with `p+q>=s`
   give the same full set and are not counted among the exclusive targets.
6. In the reverse-grid path, the short `c_j` runs touch global endpoints and
   are therefore legal boundary runs.  The only internal runs are the
   `x_j` runs of exact length `s+1`; this is why the depth range is
   `d<=s`, not `d<=s+1`.
7. Substituting `s=(k-3)/2` into (4.13) gives the constant `1/16` in
   (4.14).
8. Seam-Lipschitz packing controls residence packing, not word length and
   not compiler feasibility.

The report uses no finite search, SAT solver, web result, or unproved PBBS
enumeration.  Its only finite calibrations are the already authenticated
`k=15` and `k=16` certificates cited in the handoff.
