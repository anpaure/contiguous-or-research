# Repaired promotion rings on the packing side: owner codegrees, the sharp first bite, and the remaining regeneration gate

Date: 2026-07-26

Scope: constant-one owner packing only.  All combinatorial arguments below
are hand arguments.  The only external theorem audited is Gould--Kelly's
2025 hypergraph-matching theorem.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q},
\tag{0.1}
\]

and let \(H\) be the least integer for which

\[
 \lambda_H\ge M:=m+H.
\tag{0.2}
\]

Thus \(H=(1+o(1))\sqrt{m\log m}\).  Let

\[
 1\le k=o(m),\qquad r=M-k,
\tag{0.3}
\]

and repair a promotion ring by deleting \(k\) consecutive phases and
retaining the other \(r\) middle owners.  The rooted owner hypergraph has
one root vertex and \(r\) owner vertices in every edge.

The audit gives the following exact conclusions.

1. An \(\mathcal A\)-perfect matching, meaning one edge at every root,
   would leave exactly

   \[
      W-rN_H=N_H(\lambda_H-r)
       =O\!\left({H+k\over m}W\right)=o(W)
   \tag{0.4}
   \]

   middle owners.  More generally, a matching missing \(s\) roots leaves

   \[
                         W-rN_H+rs.                 \tag{0.5}
   \]

   Hence the desired owner conclusion is **exactly** \(s=o(N_H)\).

2. After quotienting the uniform representation multiplicity, every root
   has degree \(R\), every owner has degree \(\rho R\), where

   \[
        \rho={r\over\lambda_H}=1-O((H+k)/m),         \tag{0.6}
   \]

   and the uniform edge weight \(1/R\) is an exact fractional
   \(\mathcal A\)-perfect matching.  Thus the rooted fractional matching
   number is exactly \(N_H\).

3. The exact largest pair codegree is the distance-one owner pair:

   \[
     {\Delta_2\over R}
       ={2\rho(r-1)\over r m^2}
       ={2+o(1)\over m^2}.                            \tag{0.7}
   \]

   Consecutive owner strings give an exact all-order codegree spine.  A
   circular-arc endpoint decomposition gives, for the complete codegree
   sequence,

   \[
      \left({R\over\Delta_j}\right)^{1/(j-1)}
         \ge c\,{m\over H}\qquad(4\le j\le r+1)      \tag{0.8}
   \]

   with an absolute \(c>0\).  Thus every static higher-codegree scale tends
   to infinity; there is no projective-plane or bounded-\(B\) obstruction.

4. The repaired linear path has a stronger local statistic which is lost
   by maximum-codegree notation.  For an owner \(X\) and an edge \(e\) not
   containing it, let \(a_X(e)\) be the number of options through \(X\)
   which conflict with \(e\).  Then

   \[
                    \boxed{a_X(e)\le {20+o(1)\over m^2}D_X,}
      \qquad D_X=\rho R.                              \tag{0.9}
   \]

   The earlier crude union bound was \(O(D_X/m)\).  With marking
   probability \(p=\gamma/(rR)\), (0.9) gives a one-bite link variance

   \[
                    \operatorname {Var}Z_X
                       \le {C\gamma\over m^2}D_X^2,   \tag{0.10}
   \]

   and hence a Bernstein exponent of order \(m^2\), not order \(m\).

5. One unconditional isolated bite therefore produces a rooted matching of
   size

   \[
            (1-3\gamma-o(1)){\gamma N_H\over r}.      \tag{0.11}
   \]

   A deterministic maximal-matching argument gives the same order
   \(\nu\ge(1+o(1))N_H/m\).  These are genuine integral theorems, but they
   cover only \(\Theta(1/m)\) of the roots and do **not** give (0.5) with
   \(s=o(N_H)\).

6. Gould--Kelly does not close the gap.  Even granting a diagonal use of
   their fixed-uniformity theorem, its mandatory pair term gives
   \(B\le(1+o(1))m/\sqrt2\), while

   \[
                 \log R=(1+o(1))m\log m.             \tag{0.12}
   \]

   Their error factor \(B^{-1+\gamma}(\log R)^{\mathsf A}\), with
   \(\mathsf A\ge1\), is therefore larger than one.  Independently, the
   theorem is quantified with the uniformity fixed first.  Its proof has
   powers such as \((\log R)^{6r}\), so factorial degree does not supply an
   audited diagonal application.

7. The precise surviving gate is now **hereditary regeneration**, not a
   static codegree calculation.  To iterate the bite for \(\Theta(m)\)
   rounds one must prove that the residual links continue to satisfy the
   scaled version of (0.9).  Static full-codegree bounds do not imply this:
   a residual can concentrate a positive fraction of one owner link inside
   a small family of surviving path options.  No unconditional
   near-\(\mathcal A\)-perfect matching follows until this trajectory
   statement, or an absorber replacing it, is proved.

Consequently this note does **not** claim an \(o(W)\)-leave theorem.  It
does sharpen the owner-only problem to a theorem-sized statement: the
complete static catalogue is spread, and even its one-step influence has
the correct \(m^{-2}\) scale; the only missing matching input is preservation
of that scale under \(\Theta(m)\) dependent restrictions.

## 1. Packing-side calibration and the exact leave ledger

The exact ratio is

\[
 \lambda_q=\prod_{i=1}^q{m+i\over m-i+1}.
\tag{1.1}
\]

Minimality of \(H\) and

\[
 {\lambda_H\over\lambda_{H-1}}
    ={m+H\over m-H+1}={M\over m-H+1}
\tag{1.2}
\]

give

\[
  M\le\lambda_H
   <(M-1){M\over m-H+1}.
\tag{1.3}
\]

Therefore

\[
 0\le\lambda_H-M
   <{2M(H-1)\over m-H+1}=O(H).                       \tag{1.4}
\]

The usual logarithmic expansion of (1.1) gives

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N_H=(1+o(1)){W\over m}.                             \tag{1.5}
\]

For \(r=M-k\), (1.4) yields

\[
\begin{aligned}
 W-rN_H
   &=N_H(\lambda_H-M+k)\\
   &=O((H+k)N_H)
    =O\!\left({H+k\over m}W\right)=o(W).
\end{aligned}                                        \tag{1.6}
\]

If a rooted matching uses \(N_H-s\) edges, it covers exactly
\(r(N_H-s)\) distinct owners.  Subtraction from \(W\) proves (0.5).
Since \(rN_H=(1-o(1))W\), the second term in (0.5) is \(o(W)\) if and
only if \(s=o(N_H)\).

This equivalence is worth recording.  A theorem missing merely
\(o(W)\) roots would be meaningless because \(N_H\asymp W/m\).  The
required accuracy is a little-oh **fraction of the root shore**.

## 2. The repaired rooted hypergraph

Let

\[
 \mathcal A=\binom{[2m]}{m-H},\qquad
 \mathcal X=\binom{[2m]}m.
\tag{2.1}
\]

For \(A\in\mathcal A\), put \(U_A=[2m]\setminus A\), so \(|U_A|=M\).
Choose a directed cyclic order \(\pi\) of \(U_A\), modulo rotation.  Its
middle owners are

\[
 X_i(A,\pi)=A\cup I_\pi(i,H),\qquad i\in\mathbb Z_M. \tag{2.2}
\]

Choose a cyclic block of \(k\) consecutive phases to delete.  Its
complement is a cyclic block \(J\) of \(r=M-k\) consecutive phases.  The
rooted repaired edge is

\[
 e(A,\pi,J)=\{A\}\cup\{X_i(A,\pi):i\in J\}.          \tag{2.3}
\]

Initially retain cyclic-order/deletion representations as parallel edges.
There are

\[
                         M!                          \tag{2.4}
\]

representations at every root.

### Proposition 2.1 (uniform representation multiplicity)

Assume \(k\ge1\), and put

\[
                         u=(k-H+1)_+.                \tag{2.5}
\]

Every physical rooted edge in (2.3) has exactly

\[
                         \mu_k=2u!                   \tag{2.6}
\]

representations.  Consequently the simple rooted hypergraph has root
degree

\[
                         R={M!\over\mu_k}.            \tag{2.7}
\]

#### Proof

The Johnson-distance-one graph induced by the retained owner family is a
path.  Indeed, two cyclic \(H\)-windows are at Johnson distance one exactly
when their starts are consecutive, while the two endpoints of the retained
phase block are separated through the deleted block by \(k+1\ge2\) starts.
Thus the physical owner family recovers its phase order up to reversal.

Fix one of the two path orientations and index its starts by
\(0,1,\ldots,r-1\).  Consecutive differences identify the coordinate in
position \(i\) and the coordinate in position \(i+H\) for
\(0\le i\le r-2\).  The two identified position intervals leave a common
unidentified block of size

\[
 \max\{M-(r-1)-H,0\}=\max\{k-H+1,0\}=u.
\]

The set of labels in this block is known, but its internal order is not;
all \(u!\) orders give the same retained owner family.  Reversal supplies
the factor two.  No other freedom remains. \(\square\)

The quotient is harmless for matching and important for auditing degree:
the useful factorial degree is not manufactured by arbitrary parallel
repetition.

### Proposition 2.2 (exact degrees and the fractional root factor)

Every root and owner have degrees

\[
 \boxed{
  d(A)=R={M!\over\mu_k},\qquad
  d(X)=D_X={r(m!)^2\over (m-H)!\mu_k}.}               \tag{2.8}
\]

Moreover

\[
                         {D_X\over R}={r\over\lambda_H}=\rho\le1.
\tag{2.9}
\]

Giving every edge weight \(1/R\) is a fractional matching which has load
one at every root and load \(\rho\) at every owner.  Its total weight is
\(N_H\), and this is the fractional matching number because every edge
uses a root.

#### Proof

The root count is Proposition 2.1.  Fix an owner \(X\).  First choose a
root \(A\subset X\), in \(\binom mH\) ways.  The prescribed residual
\(H\)-set \(X\setminus A\) is a cyclic interval in \(H!m!\) directed
cyclic orders.  Exactly \(r\) retained phase blocks contain its phase.
Division by \(\mu_k\) gives

\[
 d(X)={1\over\mu_k}\binom mH H!m!r
     ={r(m!)^2\over(m-H)!\mu_k}.
\]

Since \(\lambda_H=M!(m-H)!/(m!)^2\), (2.9) follows.  The stated edge
weight has the asserted vertex loads.  Root capacity bounds every
fractional matching by \(N_H\), proving optimality. \(\square\)

The near-regularity error with maximum degree \(R\) is exactly

\[
 \varepsilon=1-\rho={\lambda_H-r\over\lambda_H}
   =O\!\left({H+k\over m}\right),
 \qquad \varepsilon\ge {k\over\lambda_H}.            \tag{2.10}
\]

## 3. Exact pair codegrees

Let two owners \(X,Y\) have Johnson distance

\[
                         d=|X\setminus Y|=|Y\setminus X|.
\tag{3.1}
\]

For \(1\le d<H\), their phases in a common frame have cyclic separation
\(d\).  The number of retained blocks of length \(r\) containing both
phases is

\[
 b_k(d)=M-2k+(k-d)_+
       =r-\min\{k,d\}.                               \tag{3.2}
\]

### Theorem 3.1 (overlapping pair sequence)

For \(1\le d<H\),

\[
 {d(X,Y)\over D_X}
       ={2b_k(d)\over r\binom md^2}.                 \tag{3.3}
\]

For \(d=H\),

\[
 {d(X,Y)\over D_X}
       \le {m-H+1\over\binom mH^2},                  \tag{3.4}
\]

and for \(d>H\) the codegree is zero.  A root--owner pair has codegree
zero unless \(A\subset X\), and in the latter case

\[
 {d(A,X)\over R}={r\over\binom MH}.                  \tag{3.5}
\]

In particular

\[
 \boxed{
 {\Delta_2\over D_X}={2(r-1)\over r m^2},\qquad
 {\Delta_2\over R}={2\rho(r-1)\over r m^2}.}         \tag{3.6}
\]

#### Proof

For \(d<H\), the number of common roots is

\[
                         \binom{m-d}{H-d}.            \tag{3.7}
\]

For a fixed common root, the two residual \(H\)-sets are overlapping
cyclic intervals in

\[
                         2d!^2(H-d)!(m-d)!            \tag{3.8}
\]

directed cyclic orders.  Multiplication by (3.2), division by \(\mu_k\),
and then division by (2.8) give (3.3).

At \(d=H\), the residual intervals are disjoint.  Ignoring the restriction
on the deleted block gives the full-ring normalized codegree in (3.4), so
the displayed inequality is sufficient and literal.  No common root exists
for \(d>H\).  Formula (3.5) is the one-interval count.  Finally (3.3) is
maximal at \(d=1\); (3.4) and (3.5) are superpolynomially smaller. \(\square\)

## 4. The all-order codegree spine

There is a useful exact family at every order.  Fix \(t\) consecutive
owners of one repaired phase path.  First keep the root fixed.  In the
parallel representation catalogue their common degree is

\[
 K_1=rH!m!,                                             \tag{4.1}
\]

and, for \(t\ge2\),

\[
 K_t=2(r-t+1)\begin{cases}
  (H-t+1)!(m-t+1)!,&2\le t\le H+1,\\
  (m-t+1)!,&H+1\le t\le m+1,\\
  1,&m+1\le t\le r.
 \end{cases}                                           \tag{4.2}
\]

At the common endpoints the formulas agree.  If the root is not prescribed,
then for \(2\le t\le H+1\) it can be chosen in
\(\binom{m-t+1}{H-t+1}\) ways.  Thus the owner-only consecutive degree is

\[
 G_t=\begin{cases}
 \displaystyle {2(r-t+1)(m-t+1)!^2\over(m-H)!},
     &2\le t\le H+1,\\[2mm]
 K_t,&H+1\le t\le r.
 \end{cases}                                           \tag{4.3}
\]

Simple-hypergraph codegrees are \(K_t/\mu_k\) and \(G_t/\mu_k\).

### Proposition 4.1 (consecutive-string count)

Equations (4.1)--(4.3) are exact.

#### Proof

The \(t-1\) consecutive differences identify the leaving and entering
coordinate at each exposed boundary.  If \(t\le H+1\), there remain an
unordered common block of size \(H-t+1\) and an unordered outside block of
size \(m-t+1\).  There are two path orientations and \(r-t+1\) retained
phase blocks containing the prescribed string.  This gives the first line
of (4.2).

Once \(t\ge H+1\), the common block has disappeared.  The outside block has
size \(m-t+1\) until \(t=m+1\), after which every coordinate position is
identified.  This gives the other lines.  Without a prescribed root, the
intersection of the first \(t\) owners has size \(m-t+1\) for
\(t\le H+1\), giving the displayed binomial number of roots.  At
\(t=H+1\) their intersection is the original root, hence it is unique from
then on. \(\square\)

The consecutive spine by itself is not an upper bound on every codegree,
because a prescribed owner family can have several circular-interval
representations.  The following endpoint decomposition controls that
multiplicity without a fixed-uniformity constant.

### Lemma 4.2 (equal-arc representation envelope)

Let \(\mathcal S\) be \(t\) distinct \(H\)-sets of an \(M\)-set which are
simultaneously cyclic intervals.  Decompose their interval-intersection
graph into components.  There are at most \(\lceil M/H\rceil\) components,
and, after their cyclic order and orientations are fixed, the realizing
coordinate orders are counted by the product of factorials of the endpoint
atoms.  Consequently:

* for \(t\le2H\), the codegree of \(\mathcal S\) is bounded by the
  codegree of one pair at Johnson distance at least
  \(\min\{H,\lfloor t/2\rfloor\}\), times \(\binom t2\);
* for \(t\ge2H\), the number of admissible component orders and
  orientations contributes at most

  \[
                  L_t:=2^t t^{\lceil M/H\rceil},      \tag{4.4}
  \]

  while the endpoint-atom factorial product is at most its coarsest
  consecutive-string value in (4.2)--(4.3).

#### Proof

For the first assertion, place the \(t\) starts on the coordinate cycle.
Some two have cyclic separation at least \(\lfloor t/2\rfloor\).  Their
two intervals have Johnson distance equal to that separation until it
reaches \(H\), and distance \(H\) thereafter.  In different containing
orders the witnessing pair may differ, so partition by its identity and
pay \(\binom t2\).

For the second assertion, intervals in different intersection components
have disjoint unions.  Every component union contains an \(H\)-interval,
so their number is at most \(\lceil M/H\rceil\).  Choose the component
order in at most \(t^{\lceil M/H\rceil}\) ways and orient every component
in at most \(2^t\) ways.  With this endpoint order fixed, coordinates with
the same membership signature form one endpoint atom and may be permuted
only inside that atom.  The count is therefore the product of the atom
factorials.  Moving two adjacent endpoints together merges atoms; the
elementary inequality \(a!b!\le(a+b)!\) shows that repeated merging can
only increase this product.  The coarsest permitted endpoint pattern is a
consecutive string, whose free atoms are exactly those counted in
(4.2)--(4.3). \(\square\)

### Theorem 4.3 (uniform full-codegree scale)

For the simple rooted repaired-ring hypergraph there is an absolute
constant \(c>0\) such that

\[
 \boxed{
  \left({R\over\Delta_j}\right)^{1/(j-1)}
      \ge c\,{m\over H}\qquad(4\le j\le r+1).}        \tag{4.5}
\]

#### Proof

For \(j\le2H\), Lemma 4.2 and Theorem 3.1 give, with
\(d=\min\{H,\lfloor j/2\rfloor\}\),

\[
 {\Delta_j\over R}
 \le \binom j2\max\left\{
     {2\rho\over\binom md^2},
     {\rho(m-H+1)\over\binom mH^2}
     \right\}.                                       \tag{4.6}
\]

Taking the \((j-1)\)-st root and using
\(\binom md^{1/d}\ge c_0m/d\) gives at least \(c_1m/H\).

Now let \(j\ge2H\).  If the prescribed set has no root, use (4.3); if it
has a root, use (4.2) with \(t=j-1\).  Lemma 4.2 contributes \(L_t\).
For \(t\ge2H\),

\[
 L_t^{1/t}
 \le2\exp\left({M\log t\over Ht}+o(1)\right)=O(1),  \tag{4.7}
\]

because \(H^2\sim m\log m\).  On the other hand, every quotient of
\(R\) by a factorial expression in (4.2)--(4.3) contains at least the
top \(t\) factors of \(M!\), up to a polynomial factor.  Their geometric
mean is at least \((1-o(1))M/e\).  The bounded factor in (4.7) therefore
leaves a lower bound \(c_2m\), stronger than (4.5).  At \(j=r+1\), the
simple full-edge codegree is one; Proposition 2.1 and \(k=o(m)\) give

\[
 R^{1/r}=\exp\left({\log M!-\log(2u!)\over r}\right)=m^{1-o(1)},
\]

which again implies (4.5). \(\square\)

Thus the natural Gould--Kelly full-sequence parameter, before its
near-regularity term is imposed, tends to infinity.  Combining (2.10),
(3.6), and (4.5), one may formally choose

\[
 B\ge c{m\over H+k}\longrightarrow\infty,            \tag{4.8}
\]

while every allowable \(B\) satisfies

\[
 B\le\sqrt{R/\Delta_2}=(1+o(1)){m\over\sqrt2}.       \tag{4.9}
\]

## 5. A path-metric improvement to one-step influence

For an owner \(X\) and repaired edge \(e\not\ni X\), let

\[
 a_X(e)=|\{f:X\in f,\ f\cap e\ne\varnothing\}|,      \tag{5.1}
\]

where a common root is also counted as a conflict.

### Lemma 5.1 (few path vertices on a Johnson sphere)

For \(1\le d<H/4\), a repaired promotion path contains at most
\(4d+2\) owners at Johnson distance \(d\) from a fixed owner \(X\).

#### Proof

If \(Y,Z\) both have distance \(d\) from \(X\), then
\(d_J(Y,Z)\le2d\).  In a promotion ring, the Johnson distance between two
owner windows is their cyclic start distance until that distance reaches
\(H\).  Since \(2d<H/2\), all starts in question lie in one cyclic arc of
length at most \(4d+1\): otherwise two of them would have cyclic distance
strictly between \(2d\) and \(M-2d\).  Such an arc contains at most
\(4d+2\) phase starts. \(\square\)

### Theorem 5.2 (width-two influence bound)

Uniformly in \(X\) and \(e\not\ni X\),

\[
                         a_X(e)\le {20+o(1)\over m^2}D_X.
\tag{5.2}
\]

#### Proof

Ignore the common-root conflict initially.  By Theorem 3.1 and Lemma 5.1,

\[
 {1\over D_X}\sum_{Y\in e}d(X,Y)
 \le\sum_{d< H/4}(4d+2){2\over\binom md^2}
     +r\max_{d\ge H/4}{d(X,Y)\over D_X}.             \tag{5.3}
\]

The \(d=1\) term is at most \(12/m^2\), the sum over \(d\ge2\) is
\(O(m^{-4})\), and the last term is superpolynomially smaller than
\(m^{-2}\) by (3.3)--(3.4).  If the root of \(e\) is contained in \(X\),
the additional options through \(X\) with that root form a fraction
\(1/\binom mH\) of its owner link.  This too is superpolynomially small.
The slack from replacing exact sphere counts by (5.3) is absorbed by the
constant 20. \(\square\)

This estimate uses the fact that deletion turns the ring into a path.  The
crude estimate \(r\Delta_2=O(D_X/m)\) discards that geometry.

## 6. The strongest unconditional integral extraction

Mark every simple edge independently with probability

\[
                         p={\gamma\over rR},
       \qquad 0<\gamma<1/20,                          \tag{6.1}
\]

and retain a marked edge only if no other marked edge meets it at a root or
owner.

### Theorem 6.1 (isolated repaired-ring bite)

There is a rooted owner matching of size at least

\[
                  (1-3\gamma-o(1)){\gamma N_H\over r}.
\tag{6.2}
\]

#### Proof

The expected number of marked edges is

\[
                         N_HRp={\gamma N_H\over r}.   \tag{6.3}
\]

Conditional on one edge being marked, the expected number of other marked
edges meeting it is at most

\[
 p(R+rD_X)\le {\gamma\over r}+\gamma\rho
             \le2\gamma.                             \tag{6.4}
\]

The union bound shows that the conditional isolation probability is at
least \(1-2\gamma-o(1)\).  Taking expectation and allowing one further
\(\gamma\) of slack proves (6.2). \(\square\)

There is a deterministic bound of the same order.  A physical edge
conflicts with at most \(R+rD_X\) catalogue edges, while the total number
of edges is \(N_HR\).  Greedy selection gives

\[
 \nu\ge {N_HR\over R+rD_X}
       ={N_H\over1+r\rho}
       =(1+o(1)){N_H\over m}.                         \tag{6.5}
\]

Neither (6.2) nor (6.5) is near-\(\mathcal A\)-perfect.

The width-two bound does give a sharper concentration theorem inside the
one bite.  Put

\[
 Z_X=\sum_{e\not\ni X}a_X(e)\xi_e,                   \tag{6.6}
\]

where \(\xi_e\) is the marking indicator.  Reversing the conflict count
gives

\[
 \sum_ea_X(e)\le D_X(R+rD_X).                        \tag{6.7}
\]

Theorem 5.2, (6.1), and (6.7) yield

\[
 \operatorname {Var}Z_X
 \le p\max_ea_X(e)\sum_ea_X(e)
 \le {C\gamma\over m^2}D_X^2.                       \tag{6.8}
\]

Bernstein's inequality therefore gives, for \(0<\eta\le1\),

\[
 \Pr\bigl(|Z_X-\mathbb EZ_X|>\eta D_X\bigr)
 \le2\exp\left[-c{m^2\eta^2\over\gamma+\eta}\right].
\tag{6.9}
\]

This is the strongest unconditional probabilistic gain in the present
audit.  It is precisely the scale needed for a plausible \(\Theta(m)\)-round
nibble, but (6.9) is a statement about the initial catalogue only.

## 7. Quantitative Gould--Kelly audit

The relevant source is Stephen Gould and Tom Kelly,
[*Advancing the R\"odl Nibble: New bounds on matchings and the list
chromatic index of hypergraphs*](https://arxiv.org/abs/2511.11375),
Theorem 1.4.

In their notation, a \((q+1)\)-uniform \((n,D,\varepsilon)\)-regular
hypergraph admits a parameter

\[
 B\le\min\left\{
   \sqrt{D/D_2},
   \min_{4\le j\le q+1}(D/D_j)^{1/(j-1)},
   1/\varepsilon
   \right\}.                                         \tag{7.1}
\]

The resulting matching leaves at most

\[
                   nB^{-1+\gamma}(\log D)^{\mathsf A}\tag{7.2}
\]

vertices, under the hierarchy

\[
                  1/D\ll1/\mathsf A\ll\gamma\ll1/q. \tag{7.3}
\]

For the present hypergraph, \(q=r\sim m\), \(D=R\), and Theorem 4.3
shows that the complete static codegree sequence is not the problem.
Formally, (4.8) tends to infinity.  Nevertheless, (4.9) and

\[
 \log R=\log M!-\log(2u!)=(1+o(1))m\log m            \tag{7.4}
\]

give, for every allowed \(B\),

\[
 B^{-1+\gamma}(\log R)^{\mathsf A}
 \ge B^{-1+\gamma}\log R
 \ge(c+o(1))m^\gamma\log m\longrightarrow\infty.   \tag{7.5}
\]

Thus the numerical conclusion (7.2) is larger than the whole vertex set.
This remains true if every intermediate codegree is replaced by its best
possible value: the pair term alone forces (4.9).

There is also an independent quantifier failure.  Equation (7.3) fixes the
uniformity before taking \(D\) large.  Here \(r\to\infty\), and the paper
states no threshold uniform in \(r\).  Explicit proof terms such as
\((\log D)^{6r}\) are not dominated by the present factorial degree:

\[
 \log\big((\log R)^{6r}\big)
   =(6+o(1))m\log m
   >(1+o(1))\log R.                                   \tag{7.6}
\]

Consequently Gould--Kelly is structurally relevant but supplies neither a
literal application nor a useful formal error bound.

## 8. The precise surviving custom-nibble theorem

One slow bite removes a \(\Theta(1/r)\) fraction of the root shore.  To
leave a fixed fraction \(z>0\) of the roots requires \(\Theta_z(r)\)
bites.  During such a run, the expected surviving degrees remain enormous:

\[
                 \log R_t=\log R-O_z(r)
                          =(1+o(1))m\log m.           \tag{8.1}
\]

Thus raw concentration is not the issue.  What must be regenerated is the
path-distributed form of the links.

The earlier version imposed an exceptional-neighbourhood condition: the
exceptional vertices were required to meet only \(o(N_H)\) root links.
That condition is sufficient but not necessary.  It is false for some
support-reachable residuals even when their exceptional owner edge mass is
negligible.  The correct packing invariant is weighted.

### \(\mathrm{WRPRN}(z)\) (weighted repaired-ring regeneration)

Run the marking rule (6.1), with the current common degree in place of
\(R\), and delete accepted roots and owners.  For every fixed \(z>0\), up
to the first time when only a \(z\)-fraction of the roots remains, the
nonexceptional surviving roots and owners satisfy

\[
\begin{aligned}
 d_t(A)&=(1+o(1))R_t,\\
 d_t(X)&=(\rho_t+o(1))R_t,\\
 \max_{e\not\ni X}a_{X,t}(e)&\le {C_z\over m^2}d_t(X),
\end{aligned}                                         \tag{8.2}
\]

Let \(\mathcal B^R_t,\mathcal B^O_t\) be the exceptional root and owner
sets.  The replacement condition is

\[
 \boxed{
 \sum_{A\in\mathcal B^R_t}d_t(A)
 +\sum_{X\in\mathcal B^O_t}d_t(X)
 =o(N_HR_t).}                                       \tag{8.3}
\]

For fixed \(z\), the active edge count is
\(\Theta_z(N_HR_t)\), so (8.3) says exactly that exceptional vertices
carry \(o(1)\) of the residual edge mass.  No restriction is placed on
the union of their static containment neighbourhoods or even on the union
of their literal residual root links.

### Theorem 8.1 (exact consequence of regeneration)

If \(\mathrm{WRPRN}(z)\) holds for every fixed \(z>0\), then the repaired
promotion-ring hypergraph has a matching missing \(o(N_H)\) roots and hence
leaving \(o(W)\) owners.

#### Proof

Delete from the marking pool every edge incident to an exceptional
vertex.  The number of deleted active edges is at most the left side of
(8.3), hence is \(o(N_HR_t)\).  By incidence averaging, all but
\(o(N_H)\) active roots lose \(o(R_t)\) options to this deletion.  Add
those roots to \(\mathcal B^R_t\); their total degree mass is still
\(o(N_HR_t)\).  On the remaining pool, (8.2) and the one-bite calculation
(6.2) apply with constants depending only on \(z\).  Suppressing the
exceptional edge mass changes the accepted-edge count and every
conditional drift by \(o(1)\).

Hence after \(C_zr\) rounds the surviving root fraction is at most \(z\),
plus \(o(1)\).  For each integer \(a\ge1\),
apply this with \(z=1/a\).  Choose a diagonal sequence \(a=a(m)\to\infty\)
slowly enough that the corresponding asymptotic statement is valid.  The
resulting matching misses \(o(N_H)\) roots.  Equation (0.5) and (1.6) give
the \(o(W)\) owner leave. \(\square\)

The initial instance of the last line of (8.2) is Theorem 5.2, and its
one-round variance is (6.8).  What is not proved is its hereditary return
after conditioning on all earlier accepted edges.  Maximum codegrees alone
do not give that return: they control each fixed link in the original
catalogue but do not prevent the surviving part of a link from clustering
on the few options which meet a particular path segment.

This is the sharp boundary of the present argument.  A proof of
\(\mathrm{WRPRN}(z)\), or a sparse absorber which takes over before (8.2)
can fail, would give the requested near-\(\mathcal A\)-perfect matching.
Without one of those inputs, iterating (6.9) is not a proof.

## 9. Dependency ledger

Proved here:

* the packing-side leave identity (0.5);
* the uniform physical-edge multiplicity (2.6);
* exact root and owner degrees and an exact fractional
  \(\mathcal A\)-perfect matching;
* the exact overlapping pair sequence (3.3) and maximum pair codegree;
* the consecutive all-order codegree spine (4.1)--(4.3);
* the uniform full-codegree lower scale (4.5);
* the path-sphere and external-influence bound (5.2);
* the integral one-bite and greedy matchings (6.2), (6.5);
* the \(m^2\)-exponent one-bite concentration (6.9);
* the quantitative failure of the published Gould--Kelly theorem; and
* the implication \(\mathrm{WRPRN}(z)\Rightarrow o(W)\) owner leave.

Not proved:

* \(\mathrm{WRPRN}(z)\) for any interval of densities tending to zero;
* a matching missing \(o(N_H)\) roots;
* an \(o(W)\) integral owner leave; or
* any nested flag, chronology, or all-depth conclusion.

The repaired owner hypergraph is therefore no longer blocked by fractional
capacity, pair codegree, the full static codegree sequence, or one-step
concentration.  Its exact remaining packing gate is a hereditary
path-link regeneration/absorption theorem.
