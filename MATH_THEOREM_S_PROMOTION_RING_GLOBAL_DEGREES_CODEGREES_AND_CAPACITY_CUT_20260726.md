# Promotion rings over all top fibres: exact mask degrees, codegrees, and the critical capacity cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 M=2m,\qquad n=m+H,\qquad
 N_t=\binom{2m}{m-t},\qquad W=N_0,
\]

where

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad H\asymp\sqrt{m\log m},
 \qquad H=o(m).
\]

For every top

\[
                         U\in\binom{[2m]}n
\]

consider the promotion-ring configurations of Theorem 3.6 in
`MATH_THEOREM_EP_MULTISCALE_ROTOR_AND_CONTEXT_HALL_OBSTRUCTION_20260726.md`:
choose a directed cyclic order of \(U\), and assign a tag in
\(\{0,\ldots,H\}\) to every phase, with at most one tag \(H\).

This note proves the exact one-mask and two-mask incidence formulas for
that catalogue.  The conclusions are as follows.

1. If \(a_t\) is the number of phase tags at least \(t\), a fixed mask
   \(X\) of rank \(m+r\) occurs in a uniform configuration over one
   containing top with probability

   \[
                  {a_{|r|}\over\binom n{H-r}}.
   \]

   Across all tops its degree is exactly

   \[
    |\Gamma_U|\,a_{|r|}{N_H\over N_{|r|}},
   \]

   where \(|\Gamma_U|\) is the common number of configurations in one
   top fibre.

2. For two masks \(X,Y\), their codegree depends only on their two ranks,
   \(|X\cap Y|\), and the two-point tag correlation at the displacement
   between the terminal endpoints of their omitted cyclic intervals.
   The exact formulas are Theorems 3.1 and 3.2 below.  They cover both a
   uniform random permutation of a tag multiset and nested contiguous tag
   blocks with a uniform cyclic shift.

3. For uniformly permuted tags, an adjacent nested pair
   \(X\subset Y\), at ranks \(m+r,m+r+d\), has the exact normalized
   codegree

   \[
    {d!\over(m+r+1)_d}
    \left(1+{d(a_{|r|}-1)\over n-1}\right)
   \]

   whenever \(0\le r<r+d<H\).  In particular, all distinct-pair
   relative codegrees are at most

   \[
                         {2\over m-H+1}=O(m^{-1}).
   \]

4. Small pair codegrees do not make independent ring choices useful.  In
   the exactly balanced fractional profile

   \[
                         a_{|r|}={N_{|r|}\over N_H},
   \]

   every mask has mean load one, but independent choices create

   \[
    {N_{|r|}\over2}
    \left(1-{a_{|r|}\over\binom n{H-r}}\right)
   \]

   expected collision pairs at rank \(m+r\).  Their aggregate over the
   central Gaussian range is \(\Theta(W\sqrt m)\).

5. There is a sharp configuration-Hall obstruction before codegrees are
   relevant.  One full ring in every top fibre uses \(nN_H\) distinct
   middle-mask slots.  Hence

   \[
                         \boxed{(m+H)N_H\le W}                 \tag{0.1}
   \]

   is necessary for pairwise mask disjointness.  If

   \[
                         H=\sqrt{m\log m}+c,
                         \qquad c=O(1),
   \]

   then

   \[
    \log{(m+H)N_H\over W}
      =(1-2c)\sqrt{\log m\over m}
       +o\!\left(\sqrt{\log m\over m}\right).                 \tag{0.2}
   \]

   Thus the exact full-ring capacity boundary is the additive half-step
   \(c=1/2\).  Merely writing \(H\sim\sqrt{m\log m}\) hides this
   obstruction.

6. Apart from (0.1), the rankwise support Hall cuts have no symmetric
   fractional deficit.  For every top family \(\mathcal A\), its
   rank-\((m+r)\) lower shadow satisfies

   \[
    |\partial_r\mathcal A|
       \ge {|\mathcal A|N_{|r|}\over N_H}.
   \]

   Hence the balanced profile passes every rankwise cut.  The unresolved
   theorem is genuinely a correlated, multirank cyclic-frame selection,
   not a one-rank capacity theorem.

No pairwise mask-disjoint selection is constructed here.  The formulas
isolate both the exact scalar obstruction and the remaining
configuration-Hall gate.

## 1. Ring and tag notation

Fix a top \(U\), \(|U|=n=m+H\), and a directed cyclic order

\[
                         c_0,c_1,\ldots,c_{n-1}.
\]

The phase-\(i\), tag-\(d_i\) chain owns at rank \(m+r\), whenever
\(|r|\le d_i\), the mask

\[
 C_i(r)=U\setminus
 \{c_{i+H+r},\ldots,c_{i+2H-1}\}.                \tag{1.1}
\]

The omitted set is a cyclic interval of length

\[
                         \ell_r=H-r.             \tag{1.2}
\]

Its terminal coordinate is \(c_{i+2H-1}\), independent of \(r\).
This terminal-end convention is important in the two-mask count: two
masks at different ranks lie on the same phase chain exactly when their
omitted intervals are nested and have the same terminal endpoint.

Fix tag multiplicities

\[
 g_0,g_1,\ldots,g_H\ge0,
 \qquad \sum_{d=0}^Hg_d=n,
 \qquad g_H\le1,                                  \tag{1.3}
\]

and put

\[
                         a_t=\sum_{d=t}^Hg_d.      \tag{1.4}
\]

Thus exactly \(a_{|r|}\) phases are active at rank \(m+r\).

Two tag models will be used.

* In the **uniform-multiset model**, every assignment of the multiset
  (1.3) to the \(n\) phase positions is allowed.  Its number is
  \[
                           \mathsf T={n!\over\prod_dg_d!}.
  \]
  One top fibre then has
  \[
                           G=(n-1)!\mathsf T                  \tag{1.5}
  \]
  configurations.

* In the **shifted-word model**, one deterministic cyclic tag word is
  shifted uniformly through all \(n\) positions.  This includes nested
  contiguous tag blocks.  Put
  \[
   A_t=\{i:d_i\ge t\},\qquad |A_t|=a_t,
  \]
  and define the ordered cyclic autocorrelation
  \[
   \alpha_{r,s}(\Delta)
    =|\{i:i\in A_{|r|},\ i+\Delta\in A_{|s|}\}|. \tag{1.6}
  \]
  One top fibre has \(n(n-1)!=n!\) frame-and-shift configurations.

The one-mask marginal is the same in both models.

## 2. Exact one-mask occurrence and degree

### Theorem 2.1 (one-mask formula)

Let \(X\subseteq[2m]\) have rank \(m+r\), where \(-H\le r\le H\).
For a fixed top \(U\supseteq X\), a uniform ring configuration contains
\(X\) with probability

\[
                         \boxed{
 p_{U,r}(X)={a_{|r|}\over\binom n{H-r}}.}          \tag{2.1}
\]

The number of containing tops is

\[
                         \binom{m-r}{H-r}.        \tag{2.2}
\]

Consequently, in the uniform-multiset catalogue, the degree of every
rank-\((m+r)\) mask is

\[
 \boxed{
 D_r=G\,a_{|r|}{N_H\over N_{|r|}}.}              \tag{2.3}
\]

In the shifted-word catalogue, replace \(G\) in (2.3) by \(n!\).

#### Proof

Put \(A=U\setminus X\), so \(|A|=H-r\).  A directed cyclic order has
exactly \(n\) intervals of this length, and all
\(\binom n{H-r}\) subsets are symmetric.  Thus \(A\) is an omitted
interval with probability \(n/\binom n{H-r}\).  Its terminal endpoint
determines one phase, and that phase is active with probability
\(a_{|r|}/n\).  This proves (2.1), including \(r=H\), where the unique
tag-\(H\) phase owns the top mask.

To extend \(X\) to a top, choose \(H-r\) coordinates from its complement,
which has size \(m-r\), proving (2.2).  Finally,

\[
 {\binom{m-r}{H-r}\over\binom n{H-r}}
 ={N_H\over N_{|r|}},                            \tag{2.4}
\]

and multiplying (2.1) by the number of tops and by the catalogue size in
one top proves (2.3). \(\square\)

The balanced marginal condition at rank \(m+r\) is therefore

\[
                         a_{|r|}={N_{|r|}\over N_H}.           \tag{2.5}
\]

It is generally nonintegral and should be read as the exact fractional
centre.  Integral tag profiles must distribute its floors and ceilings
across different tops.

## 3. Exact two-mask codegrees

Let \(X,Y\) be distinct masks of ranks \(m+r,m+s\), with
\(r,s<H\), and put

\[
 z=|X\cap Y|,
 \quad \ell=H-r,
 \quad h=H-s,
 \quad c=z-m+H-r-s.                              \tag{3.1}
\]

A common top exists exactly when \(|X\cup Y|\le n\).  The number of
common tops is

\[
 \boxed{
 B_{X,Y}=\binom{z-r-s}{m-H},}                    \tag{3.2}
\]

with the usual convention that an infeasible binomial coefficient is
zero.  In every such top,

\[
 |U\setminus X|=\ell,
 \quad |U\setminus Y|=h,
 \quad |(U\setminus X)\cap(U\setminus Y)|=c.     \tag{3.3}
\]

Since \(4H<n\) for all sufficiently large \(m\), define

\[
 \kappa_{\ell,h}(c)=
 \begin{cases}
  n-\ell-h+1,&c=0,\\
  2,&0<c<\min\{\ell,h\},\\
  |\ell-h|+1,&c=\min\{\ell,h\},\\
  0,&\text{otherwise},
 \end{cases}                                      \tag{3.4}
\]

and

\[
 F_0=c!(\ell-c)!(h-c)!(n-\ell-h+c)!.             \tag{3.5}
\]

Then \(\kappa_{\ell,h}(c)F_0\) is the exact number of directed cyclic
orders modulo rotation in which both omitted sets are intervals.

Put

\[
 a=a_{|r|},\qquad b=a_{|s|},\qquad
 e=a_{\max\{|r|,|s|\}}=\min\{a,b\}.              \tag{3.6}
\]

The equality in (3.6) uses the nested threshold sets of a tag profile.

### Theorem 3.1 (uniform-multiset pair codegree)

In the uniform-multiset catalogue, the codegree of \(X,Y\) is

\[
 \boxed{
 D(X,Y)=B_{X,Y}\,\mathsf T F_0
 \left[
  \chi_{X,Y}{e\over n}
  +\bigl(\kappa_{\ell,h}(c)-\chi_{X,Y}\bigr)
    {ab-e\over n(n-1)}
 \right],}                                       \tag{3.7}
\]

where

\[
 \chi_{X,Y}=\mathbf1_{\{X\subset Y\text{ or }Y\subset X\}}. \tag{3.8}
\]

#### Proof

Fix a common top and put \(A=U\setminus X\), \(B=U\setminus Y\).
For each admissible relative placement of the two intervals, the four
Venn atoms may be ordered in exactly \(F_0\) ways.  There are
\(\kappa_{\ell,h}(c)\) placements.

The two masks belong to the same phase chain precisely when \(A,B\) are
nested and share their terminal endpoint.  This is possible precisely
when \(X,Y\) are nested, and then exactly one of the containment
placements has the required common terminal endpoint.  For that placement
one phase must receive a tag at least
\(\max\{|r|,|s|\}\), which occurs in
\(\mathsf T e/n\) tag assignments.

For every other placement the two phase positions are distinct.  The
number of ordered tag tokens satisfying the two thresholds is
\(ab-e\), so the number of tag assignments is
\(\mathsf T(ab-e)/(n(n-1))\).  Multiply by \(F_0\), sum the placements,
and then multiply by the common-top count (3.2). \(\square\)

The top-rank case is simpler.  If \(r=H\), then a common configuration
requires \(U=X\) and \(Y\subset X\).  Its codegree is

\[
                         G{a_{|s|}\over\binom n{H-s}},          \tag{3.9}
\]

assuming \(g_H=1\); otherwise it is zero.  The analogous statement holds
with \(r,s\) interchanged.  Two distinct top masks have codegree zero.

### Theorem 3.2 (shifted-word and contiguous-block codegree)

For \(A\subset U\) a fixed \(\ell\)-interval position
\([0,\ell-1]\), define

\[
 \mathcal P_{\ell,h,c}
  =\{t\in\mathbb Z_n:
      |[0,\ell-1]\cap[t,t+h-1]|=c\}.             \tag{3.10}
\]

All intervals are cyclic.  For a placement \(t\), the displacement of
the two phase positions is the displacement of their terminal endpoints,

\[
                         \Delta(t)=t+h-\ell.      \tag{3.11}
\]

In the shifted-word catalogue the exact codegree is

\[
 \boxed{
 D_{\rm shift}(X,Y)
  =B_{X,Y}F_0
    \sum_{t\in\mathcal P_{\ell,h,c}}
       \alpha_{r,s}(\Delta(t)).}                 \tag{3.12}
\]

#### Proof

For each relative start \(t\), there are exactly \(F_0\) cyclic orders
with the prescribed two interval sets in that placement.  Their phase
indices differ by (3.11), because phase is terminal endpoint minus the
fixed offset \(2H-1\).  Exactly
\(\alpha_{r,s}(\Delta(t))\) cyclic shifts of the tag word activate both
positions.  Summation and (3.2) prove (3.12). \(\square\)

For nested contiguous tag blocks, (3.12) is completely explicit:
\(\alpha_{r,s}(\Delta)\) is the size of the intersection of two cyclic
intervals of lengths \(a_{|r|},a_{|s|}\), at displacement \(\Delta\).
The formula retains the displacement information lost by a uniformly
permuted tag multiset.

## 4. Normalized pair codegrees

### Proposition 4.1 (nested spine)

Assume the uniform-multiset model, and let

\[
 X\subset Y,\qquad |X|=m+r,\qquad |Y|=m+r+d,
\]

where \(0\le r<r+d<H\) and \(d\ge1\).  Then

\[
 \boxed{
 {D(X,Y)\over D_{r+d}}
 ={d!\over(m+r+1)_d}
  \left(1+{d(a_r-1)\over n-1}\right).}           \tag{4.1}
\]

#### Proof

Every top containing \(Y\) contains both masks.  Here

\[
 \ell=H-r,\quad h=H-r-d,\quad c=h,
\]

so \(\kappa=d+1\), \(\chi=1\), and

\[
 F_0=h!d!(m+r)!.
\]

Since the larger absolute threshold is \(r+d\), equation (3.7) has tag
factor

\[
 {a_{r+d}\over n}
 \left(1+{d(a_r-1)\over n-1}\right).
\]

Divide by the one-mask degree of \(Y\), using
\((m+r+d)!/(m+r)!=(m+r+1)_d\). \(\square\)

In particular, for \(d=1\),

\[
 {D(X,Y)\over D_{r+1}}
 ={1\over m+r+1}
  \left(1+{a_r-1\over n-1}\right)
 \le {2\over m+r+1}.                            \tag{4.2}
\]

### Theorem 4.2 (maximum relative pair codegree)

In either tag model, every two distinct non-top masks satisfy

\[
 \boxed{
 {D(X,Y)\over\min\{D_r,D_s\}}
 \le {2\over m-H+1}.}                            \tag{4.3}
\]

#### Proof

Condition on an occurrence of one of the masks, say \(Y\), of rank
\(m+s\).  Put

\[
 p=|X\setminus Y|,\qquad q=|Y\setminus X|,
 \qquad h=H-s.
\tag{4.4}
\]

The conditional top must contain the prescribed \(p\)-set
\(X\setminus Y\).  Among the \(\binom{m-s}{h}\) tops containing \(Y\),
the fraction which do so is

\[
 {\binom{m-s-p}{h-p}\over\binom{m-s}{h}}
 ={\binom hp\over\binom{m-s}p}.
\tag{4.5}
\]

In such a top, write \(B=U\setminus Y\) and \(A=U\setminus X\).
Then

\[
 |B|=h,\qquad |B\setminus A|=p,
 \qquad |A\setminus B|=q.
\]

Conditioned on \(B\) being a cyclic interval, (3.4)--(3.5) show that the
fraction of frames in which \(A\) is also an interval is

\[
 {\kappa_{\ell,h}(c)
    \over \binom hp\binom{m+s}q}.
\tag{4.6}
\]

Multiplying (4.5) and (4.6) gives the exact untagged conditional
probability

\[
 \boxed{
 \Pr_0(X\mid Y)
 ={\kappa_{\ell,h}(c)
    \over \binom{m-s}p\binom{m+s}q}.}
\tag{4.7}
\]

This formula also gives the maximum.  If \(p=0\) or \(q=0\), the two
intervals are nested and the numerator is respectively \(q+1\) or
\(p+1\).  The maximum occurs when the nonzero difference is one; the rank
constraint then makes the denominator at least \(m-H+1\).  Thus this case
is at most \(2/(m-H+1)\).  Explicitly, with \(K=m-H\), the relevant
denominator is at least \(\binom{K+d}{d}\), and

\[
 {d+1\over\binom{K+d}{d}}\le {2\over K+1}\qquad(d\ge1).
\]

Equality holds at \(d=1\), while the left side decreases thereafter
because
\((K+d+1)/(d+2)\ge1\).

If \(p,q>0\) and the overlap is nonempty, the numerator is \(2\) and both
binomial factors in (4.7) are nontrivial, so the same bound is strict for
all sufficiently large \(m\).  If the intervals are disjoint, then

\[
 \kappa=n-\ell-h+1\le m+H,
\]

while each binomial factor in (4.7) is at least its ground-set size.
Using

\[
 (m+H)(m-H+1)\le2(m^2-H^2)
                \le2(m^2-s^2)
\]

again gives the displayed bound.  These cases exhaust (3.4).

Finally, tag correlation can only discard an untagged placement.  In the
uniform-multiset model, relative to either conditioned occurrence, both
the same-position and distinct-position conditional tag factors are at
most one.  In the shifted-word model,

\[
 \alpha_{r,s}(\Delta)\le
 \min\{a_{|r|},a_{|s|}\}.
\]

Thus (4.7) bounds the tagged conditional probability relative to either
mask.  Choosing the mask whose degree is
\(\min\{D_r,D_s\}\) proves (4.3). \(\square\)

At \(q_0=m^{1/4}+O(1)\), a balanced profile has
\(a_{q_0}=(1+o(1))m\), so (4.2) is \((2+o(1))/m\).  The local codegree is
small, but only on the \(m^{-1}\) scale.

## 5. Cross-top collisions and independent-choice failure

Let two distinct tops \(U,V\) have Johnson distance

\[
                         j=|U\setminus V|=|V\setminus U|.
\]

Choose their ring configurations independently, with cumulative active
counts \(a_r(U),a_r(V)\).  At rank \(m+r\), a common mask must be a
rank-\((m+r)\) subset of \(U\cap V\).  Therefore:

### Proposition 5.1 (exact expected cross-top collision count)

The expected number of common masks at rank \(m+r\) is

\[
 \boxed{
 \mathbb E Z_r(U,V)
 =\mathbf1_{\{j\le H-r\}}
   \binom{n-j}{H-r-j}
   {a_{|r|}(U)a_{|r|}(V)\over\binom n{H-r}^{2}}.}             \tag{5.1}
\]

#### Proof

There are \(\binom{n-j}{m+r}=\binom{n-j}{H-r-j}\) possible common masks.
By Theorem 2.1, each occurs in the two independent rings with the product
of the two displayed marginal probabilities. \(\square\)

In particular, collisions are impossible unless \(j\le2H\).  At distance
one and rank \(m+H-1\), the unique possible common mask has probability

\[
                         {a_{H-1}(U)a_{H-1}(V)\over n^2}.      \tag{5.2}
\]

The top-conflict graph is local in Johnson distance, but independent
choices still have a macroscopic collision bill.

### Theorem 5.2 (exact independent collision expectation)

Assume the common balanced profile (2.5), and choose one ring
configuration independently in every top.  At rank \(m+r\), the expected
number of unordered pairs of ring occurrences which collide on one mask
is

\[
 \boxed{
 {N_{|r|}\over2}
 \left(1-{a_{|r|}\over\binom n{H-r}}\right).}     \tag{5.3}
\]

#### Proof

A fixed mask lies in

\[
                         d_r=\binom{m-r}{H-r}
\]

top fibres, and each of their independent rings contains it with
probability

\[
                         p_r={a_{|r|}\over\binom n{H-r}}.
\]

Balancedness and (2.4) give \(d_rp_r=1\).  Its expected number of
colliding unordered occurrence pairs is therefore

\[
 \binom{d_r}{2}p_r^2={1\over2}(1-p_r).
\]

Multiply by the \(N_{|r|}\) masks on the rank. \(\square\)

For \(q_0=m^{1/4}+O(1)\) and
\(H\asymp\sqrt{m\log m}\), summing (5.3) over either the full central
band or the two signed ranges \(q_0\le|r|\le H\) gives

\[
                         \Theta(W\sqrt m).         \tag{5.4}
\]

Thus independent frames miss the required absolute \(o(W)\) scale by a
factor of order \(\sqrt m\), despite the \(O(1/m)\) pair codegree.

## 6. Exact capacity and configuration-Hall cuts

### Theorem 6.1 (middle-slot obstruction)

If one complete promotion ring is selected in every top fibre and all its
truncated chains are pairwise mask-disjoint, then

\[
                         \boxed{nN_H\le W.}                    \tag{6.1}
\]

#### Proof

Every one of the \(n\) phase chains in a ring contains a middle mask, and
Theorem 3.6 makes those \(n\) middle masks distinct within the ring.
Pairwise mask disjointness across all \(N_H\) tops therefore requires
\(nN_H\) distinct members of the middle layer, which has size \(W\).
\(\square\)

More generally, if only the phase chains of tag at least \(q_0\) are put
in the retained path-cover scaffold, then necessarily

\[
                         \sum_Ua_{q_0}(U)\le N_{q_0}.           \tag{6.2}
\]

If every phase is assigned tag at least \(q_0\), this becomes

\[
                         nN_H\le N_{q_0}.                       \tag{6.3}
\]

The exact asymptotic location of (6.1) is sharper than
\(H\sim\sqrt{m\log m}\).  Uniform Taylor expansion gives

\[
 \log{N_H\over W}
  =-{H^2\over m}+O\!\left({\log^2m\over m}\right)             \tag{6.4}
\]

for \(H=O(\sqrt{m\log m})\), and hence

\[
 \log{nN_H\over W}
  =\log m-{H^2\over m}+{H\over m}
    +O\!\left({\log^2m\over m}\right).          \tag{6.5}
\]

Taking \(H=\sqrt{m\log m}+c\), with fixed \(c\), gives (0.2).  Thus
\(c<1/2-o(1)\) violates (6.1), while \(c>1/2+o(1)\) passes this scalar
test.  The retained-provider condition (6.3) adds
\(q_0^2/m=m^{-1/2}+o(m^{-1/2})\) to the logarithm, shifting the additive
threshold by only \(o(1)\).

There is a family of exact support Hall cuts beyond the whole-layer count.
For \(\mathcal A\subseteq\binom{[2m]}n\), define its rank-\((m+r)\)
lower shadow

\[
 \partial_r\mathcal A
 =\{X:|X|=m+r,\ X\subseteq U\text{ for some }U\in\mathcal A\}.
\]

### Theorem 6.2 (configuration-Hall shadow cut)

Any pairwise mask-disjoint ring selection with top loads \(a_{|r|}(U)\)
must satisfy

\[
 \boxed{
 \sum_{U\in\mathcal A}a_{|r|}(U)
 \le|\partial_r\mathcal A|
 \quad\text{for every }\mathcal A\text{ and every }r.}        \tag{6.6}
\]

On the other hand, every top family obeys

\[
 \boxed{
 |\partial_r\mathcal A|
 \ge {|\mathcal A|N_{|r|}\over N_H}.}           \tag{6.7}
\]

Hence the constant balanced fractional profile
\(a_{|r|}=N_{|r|}/N_H\) passes every rankwise configuration-Hall cut.

#### Proof

The selected ring over \(U\) uses \(a_{|r|}(U)\) distinct masks of rank
\(m+r\), all contained in \(U\).  If rings over \(\mathcal A\) are
mutually mask-disjoint, their total number cannot exceed the union of
available masks, proving (6.6).

For (6.7), double-count inclusion pairs \((X,U)\) with
\(X\subset U\), \(|X|=m+r\), and \(U\in\mathcal A\).  Every top has
\(\binom n{H-r}\) lower masks, while any lower mask lies in at most
\(\binom{m-r}{H-r}\) tops.  Therefore

\[
 |\mathcal A|\binom n{H-r}
 \le|\partial_r\mathcal A|\binom{m-r}{H-r}.
\]

The quotient of the two binomial coefficients is
\(N_{|r|}/N_H\), proving (6.7). \(\square\)

### Corollary 6.3 (the scalar cut exactly solves abstract middle ownership)

There is an assignment to every top \(U\) of \(n\) distinct middle masks
contained in \(U\), with no middle mask assigned to two tops, if and only
if

\[
                         nN_H\le W.
\tag{6.8}
\]

#### Proof

Necessity is the whole-layer count.  For sufficiency, replace every top
by \(n\) clones and join each clone to all its contained middle masks.
For a set of top clones, enlarging it to include all clones of every top
it meets can only increase the left side of Hall's inequality relative to
the common neighbourhood.  It therefore suffices to test \(n\) copies of
a top family \(\mathcal A\).  By (6.7) at \(r=0\),

\[
 |N(\mathcal A)|=|\partial_0\mathcal A|
 \ge {|\mathcal A|W\over N_H}
 \ge n|\mathcal A|.
\]

Integral Hall matching now gives the assignment. \(\square\)

Thus the additive half-step is the complete obstruction for the
unstructured middle-owner problem.  The extra local requirement is
substantial: for each top, the complements of its \(n\) assigned middle
masks must be exactly the \(n\) cyclic \(H\)-windows of one common order.
No conclusion of Corollary 6.3 supplies that tight-cycle structure, much
less the compatible windows at every other rank.

Theorems 6.1--6.2 isolate the configuration boundary.  Below the
half-step in (0.2), the full-ring plan is impossible.  Above it, symmetric
rankwise capacities do not produce a Hall obstruction; the missing
theorem must couple all ranks, all tag thresholds, and one common cyclic
frame in every top.

## 7. Why the pair-codegree estimate does not close the selection

In an exactly balanced all-tag census, one ring contains on average

\[
 K_{\rm ring}
 ={1\over N_H}\sum_{r=-H}^{H}N_{|r|}              \tag{7.1}
\]

mask cells across its truncated chains.  Since
\(H/\sqrt m\to\infty\), Gaussian summation gives

\[
 \sum_{r=-H}^{H}N_{|r|}
   =(\sqrt\pi+o(1))W\sqrt m.                      \tag{7.2}
\]

At the critical scale \(N_H=(1+o(1))W/m\),

\[
                         K_{\rm ring}=\Theta(m^{3/2}).         \tag{7.3}
\]

Even if only the signed annulus \(q_0\le|r|\le H\) is retained, removing
the \(2q_0-1\) central ranks changes (7.2) by only
\(O(Wm^{1/4})=o(W\sqrt m)\).

Thus the exact worst relative codegree \(O(1/m)\) obeys

\[
                         K_{\rm ring}\,\delta_2
                         =\Theta(\sqrt m),         \tag{7.4}
\]

not \(o(1)\).  A bounded-rank nibble or a direct local-lemma argument
cannot be imported merely from (4.3).  The exact correlations in
(3.7) or (3.12), together with a multirank absorber or a structured
configuration-Hall theorem, are still required.

## 8. Exact proved/conditional boundary

Proved:

1. the exact one-mask degree (2.3);
2. every two-mask codegree for uniform tag permutations, (3.7);
3. every two-mask codegree for shifted or contiguous tag words, (3.12);
4. the exact nested-spine ratio (4.1) and the universal
   \(2/(m-H+1)\) relative pair bound;
5. exact cross-top collision expectations (5.1) and the independent
   Poisson-scale failure (5.3)--(5.4);
6. the scalar middle-slot obstruction and its additive half-step
   threshold, together with its sufficiency for abstract middle-owner
   assignment; and
7. the exact rankwise configuration-Hall cuts, together with proof that
   the symmetric fractional profile passes all of them.

Not proved:

1. an integral distribution of tag profiles satisfying all nested
   thresholds and all cuts (6.6) simultaneously;
2. a choice of one cyclic frame per top whose masks are globally
   disjoint;
3. completion of the selected chains to one full SCD; or
4. the flag-coherent path-cover theorem and coefficient one.

The first obstruction is now exact: a full ring in every top is impossible
whenever \((m+H)N_H>W\).  Once that arithmetic cut is passed, no one-mask,
pair-codegree, or rankwise support argument decides the problem.  The
remaining gate is a genuinely correlated multirank configuration
selection.
