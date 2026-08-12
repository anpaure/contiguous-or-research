# Interval conflict profiles and a quantitative all-`k` compiler theorem

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` compiler/Hall lane  
Status: proved conditional theorems and a sharp abstract obstruction.  This
note strengthens the product-conflict-mass theorem for a fixed chronology by
giving checkable candidate-multiplicity and local-cover-profile conditions.
It does **not** prove that a known PBBS, MMM, GMM, or Pascal carrier satisfies
those conditions uniformly in `k`.

## 0. Statement of the advance

Use the notation and the negative-window conflict hypergraph `H(T)` from
`MATH_THEOREM_R_ALLK_NEGATIVE_WINDOW_CONFLICT_MASS_COMPILER_20260730.md`.
Thus the target parts are `V_S`, one for each lower target `S`, every edge is
transversal, and a full independent transversal is exactly an unrestricted
`COMP_d(T)` antecedent.  Throughout the physical interval sections assume
`1<=d<r`; the case `d=0` has no lower-target burden.

After omitting a target family `O`, choose a nonempty candidate sublist

\[
                     L_S\subseteq V_S\qquad(S\notin O).                 \tag{0.1}
\]

Let

\[
 M=\min_{S\notin O}|L_S|,                                                \tag{0.2}
\]

and, for `1<=j<=rho`, let

\[
 D_j=\max_{S\notin O}
 \#\{E\in\mathcal E(H(T)):
       |E|=j,\ E\subseteq\bigcup_{R\notin O}L_R,\ E\cap L_S\ne\varnothing\}.
                                                                            \tag{0.3}
\]

Here `rho<=r` is the proved conflict rank.  The new exact sufficient
condition is

\[
 \boxed{\qquad
 {1\over M}\le
 a\prod_{j=1}^{\rho}(1-a^j)^{D_j}
 \quad\hbox{for some }0<a<1.
 \qquad}                                                                  \tag{0.4}
\]

Under (0.4), the retained target parts have a compatible selector.  Hence,
if `T` is upper-complete,

\[
                         \nu(k)\le B(k)+|O|.                              \tag{0.5}
\]

A particularly transparent sufficient version is: for some `epsilon>0`
with `1+epsilon<M`,

\[
 \boxed{\qquad
 \sum_{j=1}^{\rho}D_j
       \left({1+\epsilon\over M}\right)^j
 \le {\epsilon\over1+\epsilon}.
 \qquad}                                                                  \tag{0.6}
\]

For example, when `M>2`, it is enough that

\[
                 \sum_{j=1}^{\rho}D_j(2/M)^j\le {1\over2}.              \tag{0.7}
\]

Thus a uniform all-dimensional family with `|O|<=C` and (0.4), or the
stronger elementary condition (0.6), proves the requested
`nu(k)<=B(k)+C`.

There is also an integral alteration estimate.  If `N` target parts remain,
then

\[
 \boxed{\qquad
 \tau(T)\le |O|+
 \left\lfloor N\sum_{j=1}^{\rho}{D_j\over jM^j}\right\rfloor.
 \qquad}                                                                  \tag{0.8}
\]

Equations (0.4)--(0.8) are not generic existence slogans: all quantities
refer to the literal interval-candidate atlas of one physical chronology.
Section 4 below bounds `D_j` explicitly by local positive/negative
coordinate-incidence counts.

## 1. Abstract part-profile transversal theorem

We first state the result independently of the Boolean application.

Let `H` be a hypergraph whose vertex set is partitioned into parts
`(L_s)_{s in Q}` and whose edges are transversal, meaning that an edge uses
at most one vertex of each part.  Suppose every part has at least `M`
vertices and every edge has size at most `rho`.  Put

\[
 D_j=\max_{s\in Q}\#\{E\in\mathcal E(H):|E|=j,\ E\cap L_s\ne\varnothing\}.
                                                                            \tag{1.1}
\]

### Theorem 1.1 (weighted part-product local lemma)

Choose an arbitrary probability distribution on every part, independently.
For an edge `E`, let `p_E` be the product probability that all of its
vertices are selected.  Suppose there is a real `c>1` such that

\[
 y_E=c^{|E|}p_E<1\qquad(E\in\mathcal E(H))                              \tag{1.2}
\]

and, for every target part `L_s`,

\[
 \boxed{\qquad
 Q_s:=\prod_{E:\ E\cap L_s\ne\varnothing}(1-y_E)\ge {1\over c}.
 \qquad}                                                                 \tag{1.3}
\]

Then `H` has an independent transversal.

A sufficient additive form of (1.3) is

\[
 \sum_{E:\ E\cap L_s\ne\varnothing}
 {c^{|E|}p_E\over1-c^{|E|}p_E}\le\log c
 \qquad(s\in Q).                                                         \tag{1.4}
\]

#### Proof

Let `B_E` be the event that all vertices of `E` are selected.  Its
dependency neighbors are precisely among the events whose edges share a
target part with `E`.  If `E` uses the `h` parts `s_1,...,s_h`, then

\[
 \prod_{F\in\Gamma(E)}(1-y_F)
 \ge\prod_{t=1}^hQ_{s_t}\ge c^{-h}.                                    \tag{1.5}
\]

The first inequality has the important favorable direction: the product
on the right repeats a neighbor which meets several parts of `E` and also
contains `h` extra copies of the factor for `E` itself.  All factors lie in
`(0,1]` (zero-probability edge events contribute the factor `1`), so this
only decreases that product.

It follows that

\[
 y_E\prod_{F\in\Gamma(E)}(1-y_F)
 \ge c^hp_Ec^{-h}=p_E.                                                    \tag{1.6}
\]

The asymmetric local lemma gives positive probability that no edge is
selected.  This is an independent transversal.

Finally, `log(1-y)>=-y/(1-y)` for `0<=y<1`.  Thus (1.4) implies
`log Q_s>=-log c`, proving the additive sufficient form.  QED.

This weighted statement is useful when a target has many candidates but a
few of them carry almost all small-cover incidence: its distribution may
downweight those candidates without deleting the target part.

### Theorem 1.2 (uniform part-profile independent transversal)

If there is `a in (0,1)` satisfying

\[
             M^{-1}\le a\prod_{j=1}^{\rho}(1-a^j)^{D_j},                \tag{1.7}
\]

then `H` has an independent transversal containing one vertex from every
part.

#### Proof

Choose one vertex uniformly and independently from each part.  For an edge
`E`, let `B_E` be the event that every vertex of `E` is chosen.  If
`h=|E|`, then

\[
                         \Pr(B_E)\le M^{-h}.                             \tag{1.8}
\]

Two such events are independent when their edges use disjoint target
parts.  Assign the local-lemma parameter

\[
                              y_E=a^{|E|}.                               \tag{1.9}
\]

Fix an edge `E` of size `h`.  For each of its `h` target parts, at most
`D_j` size-`j` edges meet that part.  Consequently `B_E` has at most
`hD_j` dependency neighbors of size `j`; this overcounts edges which share
several parts and also harmlessly allows `E` itself.  Since every factor is
in `(0,1)`,

\[
 \prod_{F\in\Gamma(E)}(1-y_F)
 \ge \prod_{j=1}^{\rho}(1-a^j)^{hD_j}.                                 \tag{1.10}
\]

Using (1.7),

\[
 y_E\prod_{F\in\Gamma(E)}(1-y_F)
 \ge
 \left(a\prod_{j=1}^{\rho}(1-a^j)^{D_j}\right)^h
 \ge M^{-h}
 \ge \Pr(B_E).                                                          \tag{1.11}
\]

The asymmetric local lemma, in precisely the form proved as Theorem 6.3 of
the negative-window report, now gives positive probability that no `B_E`
occurs.  The sampled vertices then form an independent transversal.  QED.

### Corollary 1.3 (elementary polynomial criterion)

If `epsilon>0`, `1+epsilon<M`, and

\[
 \sum_{j=1}^{\rho}D_j
       \left({1+\epsilon\over M}\right)^j
 \le {\epsilon\over1+\epsilon},                                       \tag{1.12}
\]

then an independent transversal exists.

#### Proof

Take `a=(1+epsilon)/M`.  For numbers `z_l in [0,1]`, induction gives

\[
                         \prod_l(1-z_l)\ge1-\sum_lz_l.                  \tag{1.13}
\]

Apply (1.13) to `D_j` copies of `a^j`.  The product in (1.7) is at least
`1/(1+epsilon)`, and therefore its product with `a` is at least `1/M`.
Theorem 1.2 applies.  QED.

Singleton conflict vertices may either be retained and charged through
`D_1`, or deleted from their candidate sublists before applying the
theorem.  If deletion leaves every retained part nonempty, the latter
choice makes the useful conflict girth at least two.

### Corollary 1.4 (minimum kill size versus one codegree bound)

Suppose every conflict edge has size at least `g`, `M>2`, and

\[
                         D_j\le D\qquad(g\le j\le\rho).                 \tag{1.14}
\]

Then an independent transversal exists whenever

\[
 D\le {1\over2}\left(1-{2\over M}\right)
                  \left({M\over2}\right)^g.                            \tag{1.15}
\]

In particular, for `M>=4`, the simpler condition

\[
                         D\le {1\over4}(M/2)^g                         \tag{1.16}
\]

is sufficient.

#### Proof

There are no terms below `g`, and

\[
 \sum_{j=g}^{\rho}D_j(2/M)^j
 \le {D(2/M)^g\over1-2/M}.                                              \tag{1.17}
\]

Condition (1.15) makes this at most `1/2`, so (0.7) applies.  If `M>=4`,
then `1-2/M>=1/2`, and (1.16) implies (1.15).  QED.

## 2. Integral alteration from the same profile

### Theorem 2.1 (profile alteration bound)

Under the hypotheses of Section 1, let `N=|Q|`.  There is an independent
partial transversal omitting at most

\[
                 \left\lfloor
                   N\sum_{j=1}^{\rho}{D_j\over jM^j}
                 \right\rfloor                                         \tag{2.1}
\]

parts.

#### Proof

Let `e_j` be the number of size-`j` edges.  Counting incidences between
edges and target parts gives

\[
                         je_j\le ND_j.                                  \tag{2.2}
\]

Under uniform independent selection, a size-`j` edge is present with
probability at most `M^{-j}`.  Hence the product conflict mass satisfies

\[
 \Psi\le\sum_{j=1}^{\rho}e_jM^{-j}
      \le N\sum_{j=1}^{\rho}{D_j\over jM^j}.                            \tag{2.3}
\]

The integral alteration theorem deletes at most `floor(Psi)` target parts
and leaves an independent selector.  QED.

The local-lemma and alteration conclusions serve different regimes.
Condition (1.7) can prove an exact transversal even when the total expected
number of conflicts grows with `N`.  Bound (2.1) is useful when the global
incidence mass itself is bounded.

## 3. Exact negative-window kill numbers

The profile theorem becomes meaningful only after its small conflict edges
are understood.  For the Boolean compiler atlas, this has an exact
set-cover formulation.

Fix candidate sublists `L_S`.  A candidate vertex `v=(S,I)` has label
`lab(v)=S`, interval `I(v)=I`, and target part `part(v)=S`.  For a
transversal family `X`, define its negative `x`-cover by

\[
        \operatorname{cov}_x(X)
          =\bigcup_{\substack{v\in X\\x\notin\operatorname{lab}(v)}}I(v).
                                                                            \tag{3.1}
\]

For every middle requirement `(i,x)` with `x in T_i`, put

\[
 \kappa_M(i,x)=\min\{|X|:
 X\text{ transversal and }
 E_x\cap[i,i+d]\subseteq\operatorname{cov}_x(X)\}.                      \tag{3.2}
\]

For a selected positive vertex `v=(S,I)` and `x in S`, put

\[
 \kappa_+(v,x)=1+\min\{|X|:
 \begin{array}{l}
 X\text{ transversal},\quad X\cap L_S=\varnothing,\\
 E_x\cap I\subseteq\operatorname{cov}_x(X)
 \end{array}\}.                                                         \tag{3.3}
\]

Finally, for a source position `p`, put

\[
 \kappa_0(p)=\min\{|X|:
 \begin{array}{l}
 X\text{ transversal},\\
 P_p\subseteq
 \displaystyle\bigcup_{\substack{v\in X\\p\in I(v)}}
             ([k]\setminus\operatorname{lab}(v))
 \end{array}\}.                                                         \tag{3.4}
\]

The minimum of an empty family of feasible covers is `infinity`.

### Lemma 3.1 (exact conflict-girth formula)

The minimum conflict-edge size in the restricted negative-window atlas is

\[
 \boxed{
 g=\min\left\{
       \min_{i,x\in T_i}\kappa_M(i,x),
       \min_{v=(S,I),\ x\in S}\kappa_+(v,x),
       \min_p\kappa_0(p)
       \right\}.}                                                       \tag{3.5}
\]

If the restricted conflict hypergraph has no edges, both sides of (3.5)
are understood as `infinity`.

#### Proof

A selector violates a middle row exactly when its negative intervals cover
`E_x cap [i,i+d]`, which is (3.2).  It violates a positive row of the
selected candidate `v` exactly when candidates from other target parts
negatively cover `E_x cap I`; including `v` gives (3.3).  It empties source
position `p` exactly when the omitted-coordinate sets of the candidates
using `p` cover every coordinate in `P_p`, which is (3.4).

Thus the right side of (3.5) is the minimum size of any incompatible
transversal family.  Minimizing such a family by inclusion produces a
conflict edge without increasing its size.  Conversely every conflict edge
is incompatible and fails at least one of these three row types.  QED.

This is the precise small-edge countercondition.  For example, asserting
that every target has many witness intervals says nothing about `g`: two
of those choices can still cover the last two surviving occurrences of a
middle coordinate.  To invoke the favorable `j>=2` or `j>=3` regimes of
(0.6), one must prove the corresponding cover lower bounds in (3.2)--(3.4).

## 4. An explicit interval-incidence bound for `D_j`

The following estimate is deliberately coarse but completely local and
requires no enumeration of global conflict edges.  Define

\[
 A^- =\max_{x,p}
 \#\{v:\ x\notin\operatorname{lab}(v),\ p\in I(v)\},                   \tag{4.1}
\]

\[
 A^+ =\max_{x,p}
 \#\{v:\ x\in\operatorname{lab}(v),\ p\in I(v)\},                    \tag{4.2}
\]

where the candidates range only over the retained sublists, and put

\[
                       M_+=\max_S|L_S|.                                 \tag{4.3}
\]

In the displayed degree bound below, the convention is `t^0=1`, including
when `t=0`; terms carrying the indicator `j>=2` are absent when `j=1`.

### Proposition 4.1 (local interval bound on part degrees)

For every `1<=j<=rho`,

\[
\begin{split}
D_j\le M_+\big[&
 2dk\big((d+1)A^-\big)^{j-1}
 +r(dA^-)^{j-1}\\
&+\mathbf 1_{j\ge2}\,kdA^+(dA^-)^{j-2}
 +d(rA^-)^{j-1}\big].                                      \tag{4.4}
\end{split}
\]

#### Proof

Fix one candidate `v=(S,I)` and count size-`j` minimal conflicts containing
it.

For a middle-row conflict, `v` must be negative in some coordinate `x` and
must meet the killed set `E_x cap [i,i+d]`; otherwise it is removable.
There are at most `k` choices of `x`.  An interval `I` of length at most
`d` meets at most `|I|+d<=2d` windows `[i,i+d]`.  Once the row and `v` are
fixed, every other member of a minimal cover meets one of at most `d+1`
positions, and each position lies in at most `A^-` negative candidates.
Ordering those other members only overcounts, giving

\[
                    2dk((d+1)A^-)^{j-1}.                                \tag{4.5}
\]

For a positive-row conflict, first suppose `v` is the positive candidate
whose equality is being killed.  There are at most `r` positive
coordinates, and the remaining `j-1` negative candidates each meet a set
of at most `d` positions.  This contributes at most

\[
                           r(dA^-)^{j-1}.                                \tag{4.6}
\]

If instead `v` is one of the negative candidates, it has a private killed
position in a minimal cover.  Choose the omitted coordinate in at most `k`
ways, that private position in at most `d` ways, and the positive candidate
through that coordinate-position pair in at most `A^+` ways.  The other
`j-2` negative candidates contribute at most `(dA^-)^{j-2}`.  This gives
the third term of (4.4).

For a source-nonemptiness conflict at `p`, minimality gives every candidate
a private coordinate of `P_p` which it omits.  The fixed interval `I`
contains at most `d` possible positions `p`; each of the other `j-1`
candidates is specified, with overcount, by one of at most `r` omitted
coordinates and one of at most `A^-` candidates through `(x,p)`.  This
gives

\[
                            d(rA^-)^{j-1}.                               \tag{4.7}
\]

Summing (4.5)--(4.7), then summing over the at most `M_+` choices of `v`
in a fixed target part, proves (4.4).  Multiple counting only strengthens
the upper bound.  QED.

Combining (4.4) with (0.6) is a fully explicit interval-atlas theorem.  It
also explains what a successful Pascal or PBBS proof must establish:
large target multiplicity `M` is useful only if the coordinate-position
loads `A^-`, `A^+` and the small-cover counts grow sufficiently more slowly.

## 5. Application to the compiler factorization

### Theorem 5.1 (bounded-defect compiler from local profiles)

Let `T` be a linearly `d`-resident, upper-complete permutation of the
rank-`r` layer.  Choose an exceptional lower-target family `O` and
candidate sublists satisfying the exact sandwich condition.  Then:

1. if (0.4), or its sufficient form (0.6), holds, then
   \[
                              \nu(k)\le B(k)+|O|;                         \tag{5.1}
   \]
2. without (0.4), the unconditional profile estimate is
   \[
   \nu(k)\le B(k)+|O|+
       \left\lfloor
       (\Lambda-|O|)\sum_{j=1}^{\rho}{D_j\over jM^j}
       \right\rfloor.                                                    \tag{5.2}
   \]

In particular, `|O_k|<=C` together with (0.4) for one physical chronology
in every dimension proves `nu(k)<=B(k)+C`.

#### Proof

Restrict `H(T)` to retained target parts and retained candidate vertices.
Any incompatible selector in the restriction contains an original minimal
incompatible family all of whose vertices remain, so its edges are exactly
  the relevant original conflict edges.  Theorem 1.2 gives a compatible full
selector of all retained parts under (0.4).  The exact partial-atlas theorem
constructs one nonzero antecedent with derivative `T`; append the targets in
`O` literally.  Upper completeness and the deadline lower bound give
(5.1).  Theorem 2.1 and the same literal augmentation give (5.2).  QED.

This theorem is integral inside one exact factor.  The random experiment is
only a proof that one deterministic selector exists; it does not combine
rankwise rows or independently chosen physical words.

## 6. Why multiplicity, rank, and linearity do not suffice

The local profile hypothesis cannot be discarded.

### Proposition 6.1 (rank-two repeated pigeonhole obstruction)

For every pair of integers `M,q>=1`, there is a linear rank-two partite
hypergraph with `q(M+1)` parts, exactly `M` candidates in every part, and
independent-transversal deficiency exactly `q`.

#### Construction and proof

Make `q` disjoint blocks.  In one block take parts

\[
 V_i=\{(i,c):c\in[M]\},\qquad i=1,\ldots,M+1.                           \tag{6.1}
\]

For every `i!=i'` and color `c`, put in the pair edge

\[
                         \{(i,c),(i',c)\}.                              \tag{6.2}
\]

Distinct edges meet in at most one vertex, so the hypergraph is linear and
has rank two.  An independent partial transversal in one block assigns
distinct colors to its chosen parts.  It therefore uses at most `M` of the
`M+1` parts, while omitting one part and assigning all `M` colors attains
that bound.  Deficiency is exactly one per block and hence exactly `q` in
their disjoint union.  QED.

This is precisely the abstract form of `M+1` residual targets competing
for the same `M` literal addresses in the robust-core Hall subclass.
Repeating disjoint deficient banks makes the compiler defect unbounded.
Thus no theorem based only on

* arbitrarily large candidate multiplicity,
* conflict rank two (hence certainly rank at most `r`),
* simplicity or linearity of the conflict hypergraph, or
* pair-of-candidate codegree one

can imply `tau(T)=O(1)`.  Some genuine expansion/local-load assertion is
logically necessary.  In this example `D_2=M^2`, so the profile criterion
detects, rather than hides, the obstruction.

## 7. Scope against the finite certificates

1. The audited `k=11,13,15` flat optimal words have actual full compatible
   selectors.  Hence their exact defect is zero.  The sufficient profile
   inequalities need not hold for an arbitrary choice of their candidate
   sublists; they are not claimed necessary.

2. The audited `k=9` compiler uses a genuine length-two witness.  The
   theorem permits that vertex and therefore does not impose the false
   one-cell normalization.

3. The authenticated `k=16` word of length `B(16)+1` does not identify a
   flat `B(16)` prefix with a named derivative chronology.  It therefore
   neither proves nor refutes (0.4) for any fixed `T`.

4. Residence, the run-boundary pair lemma, and the Pascal envelope
   identities help by pruning the candidate lists and lowering `A^-` and
   `D_j`.  None of them alone implies (0.4): the repeated Hall bank in
   Proposition 6.1 is the minimal missing expansion condition, while
   Lemma 3.1 records the additional higher-order coordinate-cover
   countercondition.

## 8. Exact remaining all-`k` target

A reusable `B(k)+O(1)` theorem is now reduced to either of two explicit
claims for one resident upper-complete chronology `T_k` in every dimension:

* find `|O_k|=O(1)` and candidate sublists satisfying (0.4), preferably via
  the elementary profile inequality (0.6); or
* prove the global alteration quantity
  \[
  (\Lambda_k-|O_k|)
       \sum_j{D_{k,j}\over jM_k^j}=O(1).                                \tag{8.1}
  \]

The exact minimal ways this route can fail are:

* an unbounded family of empty candidate parts;
* bounded-size kill covers from (3.2)--(3.4) with too much repeated local
  incidence; or
* Hall-type part banks whose `D_j/M^j` mass does not decay, as in
  Proposition 6.1.

This is stronger than merely saying that a Hall theorem is missing: it
specifies the candidate multiplicity, every relevant local codegree, exact
constants, and the integral augmentation conclusion.

## 9. Imported results and unproved assertions

Imported, already proved:

* the exact partial negative-window atlas criterion;
* the rank-`rho` conflict hypergraph representation;
* the product-mass alteration theorem; and
* the asymmetric local lemma stated and proved in the negative-window
  report.

Proved in this note:

* Theorems 1.1--1.2 and Corollary 1.3;
* the integral profile alteration bound;
* the exact kill-number formula;
* the explicit local interval-incidence estimate (4.4); and
* the repeated rank-two obstruction.

Unproved:

* no known all-dimensional carrier is shown to satisfy the profile
  inequality;
* (4.4) is an upper bound, not an assertion that its right side is small;
* no converse to Theorems 1.1--1.2 is claimed; and
* no architecture theorem says every near-optimal word must arise from a
  flat chronology plus literal augmentation.
