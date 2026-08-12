# The common-core tight-path configuration hypergraph: exact incidences and the rooted nibble boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Inputs used without reproving their local path lemmas:

* `MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md`;
* `MATH_THEOREM_S_COMMON_CORE_TRACE_FUSION_OBSTRUCTION_20260726.md`;
* `MATH_THEOREM_S_PROMOTION_RING_GLOBAL_DEGREES_CODEGREES_AND_CAPACITY_CUT_20260726.md`;
* `MATH_THEOREM_ROOTED_PROMOTION_EDGE_TRANSITIVITY_COLLAPSE_20260726.md`.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 N=N_H,
\tag{0.1}
\]

and work at the common-core calibrated height

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 M=m+H,\qquad s=m-H,\qquad L=m-3H+1,
\tag{0.2}
\]

where

\[
 \Lambda_q=\frac{N_q}{N},\qquad
 \Lambda=\Lambda_0=\frac WN,
 \qquad L<\Lambda=m+O(H).
\tag{0.3}
\]

This note builds a synchronized-tag joint object. Its roots are the rank-
\(M\) tops. Its target vertices are the middle layer and all controlled
lower and upper signed ranks. An edge is not a separate choice at each
rank: it is one literal \(L\)-phase common-core tight path, with one
fixed physical tag word, and it contains all traces of all its active
phases simultaneously.

The fixed tag word and the dynamically chosen core should be kept in
view.  A perfect matching here is exactly the **free-core,
synchronized-tag** form of CCTPF.  It is a sufficient subcase of the
calibrated fusion theorem, but it is not literally equivalent to the
earlier formulation in which preliminary cores are fixed and each root
may use a different placement of the same tag histogram.  Allowing all
tag words would destroy the single edge orbit used in Theorem 5.3.

The exact conclusions are as follows.

1. There is a fixed nonincreasing threshold profile \((b_q)\) whose
   intrinsic target shortage is \(o(W)\). Every root has degree

   \[
                              D=M!.
   \tag{0.4}
   \]

   Every rank-\((m+r)\) target has degree

   \[
    \boxed{
    d_r=b_{|r|}\frac{(m-r)!(m+r)!}{s!}
        =D\frac{b_{|r|}}{\Lambda_{|r|}}.}
   \tag{0.5}
   \]

2. For arbitrary targets at arbitrary signed ranks, Theorem 3.1 gives
   the exact codegree. It retains both the common top and the relative
   phase displacement; ranks and phases are never separated.

3. Uniformly over the chosen tag word, after deleting zero-degree rows,

   \[
    \boxed{
    \Delta_2\le\frac{4D}{m}}
   \tag{0.6}
   \]

   for all sufficiently large \(m\). Two configurations over distinct
   roots meet in at most

   \[
                              H(2H+1)
   \tag{0.7}
   \]

   target vertices.

4. The target-part size of one edge is

   \[
    k=L+2\sum_{q=1}^{H-1}b_q
      =(\sqrt\pi+o(1))m^{3/2}.
   \tag{0.8}
   \]

   Therefore

   \[
                  k\frac{\Delta_2}{D}=\Theta(\sqrt m),
   \tag{0.9}
   \]

   not \(o(1)\). More sharply, every edge has normalized vertical-spine
   pair mass \(\Omega(\sqrt m)\). Thus a bounded-rank nibble cannot be
   diagonalized from the pair-codegree estimate alone. The vertical
   ladders must be treated as one structured conflict.

5. The complete configuration LP has the exact fractional matching
   \(x_e=1/D\), saturating every root and loading every target by at most
   one. All nonnegative linear capacity cuts therefore pass.

6. Let \(\nu\) be the matching number of the joint configuration
   hypergraph. A matching of size \(\nu\) has exactly

   \[
    \boxed{
    \mathfrak H=\Delta+k(N-\nu)}
   \tag{0.10}
   \]

   uncovered target vertices, where \(\Delta=o(W)\) is the forced scalar
   shortage. Consequently

   \[
    \boxed{
    \mathfrak H=o(W)
    \quad\Longleftrightarrow\quad
    \nu=N-o(N/\sqrt m).}
   \tag{0.11}
   \]

7. Because the fixed-word catalogue is edge-transitive,

   \[
    \boxed{
    \chi_f'=\frac{ND}{\nu}.}
   \tag{0.12}
   \]

   Hence the strongest convex edge-colouring target
   \(\chi_f'=D+o(D/\sqrt m)\) is exactly equivalent to the unweighted
   rooted matching in (0.11); it is not a separate relaxation which can
   bypass the integral problem.

A literal joint first bite is proved in Theorem 6.1. It selects
\(\Theta(N/k)\) roots at once with no target collision at any rank. What
is not proved is regeneration through the \(\Theta(k\log m)\) bites
needed to reach the precision in (0.11), or an absorber at root leave
\(o(N/\sqrt m)\). Thus the construction supplies the exact joint
hypergraph and its full pair audit, but not coefficient one.

## 1. One physical tag profile and one literal edge per state

Use the common-core counts

\[
 b_0=L,
\tag{1.1}
\]

and, for \(1\le q<H\),

\[
 b_q=
 \min\left\{L-1,
   \max\left\{0,\left\lfloor\frac{N_q}{N}\right\rfloor-1\right\}
 \right\},
 \qquad b_H=0.
\tag{1.2}
\]

The sequence \(b_0,b_1,\ldots,b_H\) is nonincreasing. Hence there is a
word

\[
                         \mathbf d=(d_1,\ldots,d_L),
                         \qquad 0\le d_j<H,
\tag{1.3}
\]

such that

\[
                         |\{j:d_j\ge q\}|=b_q
                         \qquad(0\le q\le H).
\tag{1.4}
\]

Fix one such word once and for all. Its order is arbitrary; all incidence
bounds below are uniform in that order. The compulsory tag-\(H\) anchor
may be placed in the discarded collar outside the retained core-safe
path. Its entire boundary cost is \(O(HN)=o(W)\), so it is not a vertex
of the protected configuration hypergraph.

Let

\[
 \mathcal U=\binom{[2m]}M
\tag{1.5}
\]

be the root set. Put

\[
 \mathcal X_0=\binom{[2m]}m,
 \qquad
 \mathcal X_q^\pm=\binom{[2m]}{m\pm q}
 \quad(1\le q<H),
\tag{1.6}
\]

and let

\[
 \mathcal X=\mathcal X_0\mathbin{\dot\cup}
 \bigcup_{q=1}^{H-1}
       (\mathcal X_q^-\mathbin{\dot\cup}\mathcal X_q^+).
\tag{1.7}
\]

Fix a top \(U\in\mathcal U\). A state over \(U\) is a bijective word

\[
                         z=(z_1,\ldots,z_M)
\tag{1.8}
\]

on \(U\). Its core and tail are

\[
 Q_z=\{z_1,\ldots,z_{2H}\},
 \qquad
 t_i=z_{2H+i}\quad(1\le i\le s).
\tag{1.9}
\]

Thus the core is selected as part of the hyperedge. It is not frozen by
a preliminary rankwise Hall matching; the one integral state chooses the
core, tail order, phases, and every signed trace together.

For \(-H<r<H\), put

\[
                         \ell_r=H-r.
\tag{1.10}
\]

At phase \(1\le j\le L\), define the literal signed trace

\[
 C_{z,j}(r)
 =U\setminus
   \{t_{j+2H-\ell_r},\ldots,t_{j+2H-1}\}.
\tag{1.11}
\]

It has rank \(m+r\). The target part of the configuration is

\[
 \begin{aligned}
 P(U,z)=
 &\{C_{z,j}(0):1\le j\le L\}\\
 &\mathbin{\dot\cup}
 \{C_{z,j}(q),C_{z,j}(-q):
        1\le q<H,\ d_j\ge q\}.
 \end{aligned}
\tag{1.12}
\]

The common-core path theorem shows that (1.12) is one literal directed
promotion path, and that its targets are distinct inside every signed
rank. All of them contain the same core \(Q_z\).

Define the rooted configuration multihypergraph \(\mathcal K_{\rm cc}\)
on

\[
                         V(\mathcal K_{\rm cc})
                         =\mathcal U\mathbin{\dot\cup}\mathcal X
\tag{1.13}
\]

by placing the edge

\[
                         e(U,z)=\{U\}\mathbin{\dot\cup}P(U,z)
\tag{1.14}
\]

for every top and every bijective word on it. Parallel edges are retained,
because different core orders are different literal collar states.

Every root has degree

\[
                         D=M!,
\tag{1.15}
\]

and every edge has one root and exactly

\[
                         k=L+2\sum_{q=1}^{H-1}b_q
\tag{1.16}
\]

target vertices. Thus the total hyperedge cardinality is \(k+1\); below,
\(k\) always denotes the target-part size. This is the promised joint
rank-and-phase object.

## 2. Exact degrees and the scalar hole ledger

### Theorem 2.1 (one-target and root--target degrees)

Let \(X\) have rank \(m+r\), where \(-H<r<H\), and put
\(q=|r|\), \(\ell=H-r\). Then

\[
 \boxed{
 d(X)=d_r
 =b_q\frac{(m-r)!(m+r)!}{s!}
 =D\frac{b_q}{\Lambda_q}.}
\tag{2.1}
\]

For a fixed root \(U\),

\[
 \boxed{
 d(U,X)=
 \begin{cases}
 b_q\,\ell!(M-\ell)!,&X\subseteq U,\\
 0,&X\not\subseteq U.
 \end{cases}}
\tag{2.2}
\]

Distinct roots have codegree zero.

#### Proof

The target \(X\) lies in

\[
                         \binom{m-r}{H-r}=\binom{m-r}{\ell}
\tag{2.3}
\]

tops. Fix one such top. For any active phase, the prescribed set
\(U\setminus X\) must occupy one fixed interval of \(\ell\) tail
positions. Its labels may be ordered in \(\ell!\) ways and all remaining
labels in \((M-\ell)!\) ways. There are \(b_q\) active phases. Distinct
phases cannot produce the same positive-length deletion set, so this
counts each state once and proves (2.2).

Multiplying (2.2) by (2.3) gives

\[
 d_r
 =b_q\frac{(m-r)!}{s!\,\ell!}\ell!(m+r)!,
\]

which is the first equality in (2.1). Finally,

\[
 \frac{(m-r)!(m+r)!}{s!M!}
 =\frac{N}{N_q}=\frac1{\Lambda_q},
\]

proving the second. An edge has one root, so two roots have codegree
zero. \(\square\)

The definition of \(b_q\) gives

\[
                         0\le d_r\le D.
\tag{2.4}
\]

Thus assigning weight \(1/D\) to every configuration edge loads each
root exactly one and every target at most one.

### Proposition 2.2 (exact total deficit)

Let

\[
 B=W+2\sum_{q=1}^{H-1}N_q
\tag{2.5}
\]

be the number of target vertices and put

\[
 \Delta
 =(W-LN)+2\sum_{q=1}^{H-1}(N_q-b_qN).
\tag{2.6}
\]

Then

\[
 \boxed{
 \sum_{X\in\mathcal X}\left(1-\frac{d(X)}D\right)
 =\Delta=B-kN.}
\tag{2.7}
\]

Moreover,

\[
                         \Delta=O(H^{3/2}N)=o(W).
\tag{2.8}
\]

#### Proof

Equation (2.1) says that the degree ratio on either signed depth \(q\)
is \(b_qN/N_q\). Summing its deficit over that rank gives
\(N_q-b_qN\); the middle gives \(W-LN\). This proves (2.7), and its
second equality follows from (1.16).

For uncapped \(q\), the definition of \(b_q\) leaves fewer than \(2N\)
targets. The cap \(b_q=L-1\) is active only for
\(q=O(\sqrt H)\), and at each such depth the excess over \(L-1\) is
\(O(H)\). The capped contribution is therefore \(O(H^{3/2}N)\), while
all uncapped depths contribute \(O(HN)\). Finally

\[
 \frac{H^{3/2}N}{W}=O\left(\frac{H^{3/2}}m\right)=o(1).
\]

This proves (2.8). \(\square\)

### Proposition 2.3 (edge rank)

One has

\[
                         k=(\sqrt\pi+o(1))m^{3/2}.
\tag{2.9}
\]

#### Proof

Uniformly for \(q\le H\), Gaussian expansion gives

\[
 \frac{N_q}{N}
 =\Lambda\exp\left(-\frac{q^2}{m}+o(1)\right),
 \qquad \Lambda=(1+o(1))m.
\tag{2.10}
\]

The cap and integer rounding change the sum of the \(b_q\)'s by only
\(O(H^{3/2})+O(H)=o(m^{3/2})\). Hence

\[
 \sum_{q=1}^{H-1}b_q
 =(1+o(1))m\sum_{q\ge1}e^{-q^2/m}
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)m^{3/2}.
\]

Now use \(L=O(m)=o(m^{3/2})\) in (1.16). \(\square\)

## 3. Exact arbitrary-rank pair codegrees

For \(1\le j\le L\) and \(1\le\ell\le2H-1\), put

\[
 P_{j,\ell}
 =\{j+2H-\ell,\ldots,j+2H-1\}\subseteq[s].
\tag{3.1}
\]

These are the tail-position intervals deleted in (1.11).

Let \(X,Y\) be distinct target vertices of ranks \(m+r,m+t\). Put

\[
 q=|r|,\quad q'=|t|,\quad
 \ell=H-r,\quad h=H-t,
\tag{3.2}
\]

and define

\[
 a=M-|X\cup Y|,
 \qquad b=|Y\setminus X|=\ell-a,
 \qquad c=|X\setminus Y|=h-a,
 \qquad d=|X\cap Y|.
\tag{3.3}
\]

When any number in (3.3) is negative, all following expressions are
understood to be zero. Define the actual phase correlation

\[
 \Theta_{r,t}(a)
 =\#\left\{(j,k):
 \begin{array}{l}
 1\le j,k\le L,\ d_j\ge q,\ d_k\ge q',\\
 |P_{j,\ell}\cap P_{k,h}|=a
 \end{array}\right\}.
\tag{3.4}
\]

This integer retains the fixed tag word and the relative physical phase
positions.

Equivalently, define the linear tag autocorrelation

\[
 \alpha_{q,q'}(u)
 =|\{j:1\le j,j+u\le L,\ d_j\ge q,\ d_{j+u}\ge q'\}|,
\tag{3.4a}
\]

and the interval-overlap kernel

\[
 \iota_{\ell,h}(u)
 =|[2H-\ell,2H-1]
    \cap[u+2H-h,u+2H-1]|.
\tag{3.4b}
\]

Then the exact phase factor is

\[
 \boxed{
 \Theta_{r,t}(a)
 =\sum_{u=-(L-1)}^{L-1}
   \alpha_{q,q'}(u)\,
   \mathbf1_{\{\iota_{\ell,h}(u)=a\}}.}
\tag{3.4c}
\]

Thus the complete dependence on the common physical phase word is an
explicit one-dimensional autocorrelation, not an independent marginal
at each rank.

### Theorem 3.1 (joint signed-rank pair formula)

For arbitrary distinct signed targets \(X,Y\),

\[
 \boxed{
 d(X,Y)
 =\frac{(s+a)!}{s!}\,b!c!d!\,\Theta_{r,t}(a).}
\tag{3.5}
\]

Equivalently, if \(b_q>0\),

\[
 \boxed{
 \frac{d(X,Y)}{d_r}
 =\frac{\Theta_{r,t}(a)}{b_q}
   \frac{b!}{(s+a+1)_b}
   \frac{c!}{(d+1)_c}.}
\tag{3.6}
\]

#### Proof

A common edge has a top \(U\supseteq X\cup Y\). Since \(|U|=M\), it
adds exactly \(a\) coordinates outside the union. There are

\[
 \binom{2m-|X\cup Y|}{a}=\binom{s+a}{a}
\tag{3.7}
\]

such tops.

Fix one. The two deleted label sets are

\[
 I=U\setminus X,
 \qquad J=U\setminus Y.
\]

Their four Venn cells have sizes

\[
 |I\cap J|=a,\quad |I\setminus J|=b,\quad
 |J\setminus I|=c,\quad |U\setminus(I\cup J)|=d.
\]

For a fixed phase pair counted by \(\Theta_{r,t}(a)\), the corresponding
four position cells have the same sizes. The labels may be bijected onto
those cells in exactly

\[
                         a!b!c!d!
\tag{3.8}
\]

ways. Conversely every common configuration determines one such top,
phase pair, and four cell bijections. Multiplying (3.7)--(3.8) and using
\(\binom{s+a}{a}a!=(s+a)!/s!\) proves (3.5).

Now \(m-r=s+\ell=s+a+b\), while
\(m+r=|X|=d+c\). Divide (3.5) by (2.1) to obtain (3.6). \(\square\)

Formula (3.5) is the complete pair enumerator requested in the question.
It includes lower--lower, upper--upper, lower--upper, middle--signed, and
all unequal-phase pairs under one expression.

## 4. Maximum codegree and clustered path intersections

### Theorem 4.1 (universal relative pair bound)

For all sufficiently large \(m\), any two distinct positive-degree
target vertices satisfy

\[
 \boxed{
 d(X,Y)\le\frac4m\min\{d(X),d(Y)\}.}
\tag{4.1}
\]

Moreover every root--target pair satisfies

\[
                         d(U,X)\le\frac{3D}{m}.
\tag{4.2}
\]

Consequently the maximum codegree of \(\mathcal K_{\rm cc}\) is at most
\(4D/m\).

#### Proof

Condition first on an active phase \(j\) for \(X\). For fixed interval
lengths \(\ell,h\), the number of relative starts \(k-j\) giving
intersection size \(a\) is at most

\[
 \begin{cases}
 L,&a=0,\\
 2,&0<a<\min\{\ell,h\},\\
 |\ell-h|+1,&a=\min\{\ell,h\}.
 \end{cases}
\tag{4.3}
\]

Boundary truncation and the tag word can only decrease these numbers.
Put \(u=b+c\). If \(a>0\), distinctness gives \(u\ge1\), and (4.3)
implies

\[
                         \frac{\Theta_{r,t}(a)}{b_q}\le u+1.
\tag{4.4}
\]

Also \(s+a+1\ge m-3H\) and \(d+1\ge m-3H\). Therefore (3.6) gives

\[
 \frac{d(X,Y)}{d_r}
 \le\frac{(u+1)u!}{(m-3H)^u}
 \le\frac4m.
\tag{4.5}
\]

The last sequence is decreasing from \(u=1\), because
\((u+2)/(m-3H)<1\) throughout \(u\le4H\).

If \(a=0\), then \(\ell,h\ge1\) and hence \(u\ge2\). Equations
(3.6) and (4.3) give

\[
 \frac{d(X,Y)}{d_r}
 \le\frac{m\,u!}{(m-3H)^u}
 \le\frac4m,
\tag{4.6}
\]

the maximum occurring at \(u=2\). Interchanging \(X,Y\) proves (4.1).

For (4.2), equation (2.2) gives

\[
                         \frac{d(U,X)}D
                         =\frac{b_q}{\binom M\ell}.
\tag{4.7}
\]

If an upper target has \(\ell=1\), then

\[
 \frac{N_{H-1}}N=\frac{m+H}{m-H+1}<2,
\]

so (1.2) gives \(b_{H-1}=0\). Every positive-degree row therefore has
\(\ell\ge2\), or is middle/lower with still larger \(\ell\). Since
\(b_q\le M\),

\[
 \frac{b_q}{\binom M\ell}
 \le\frac M{\binom M2}=\frac2{M-1}\le\frac3m.
\]

Distinct roots have codegree zero, completing the proof. \(\square\)

The bound is sharp in order. If
\(X\in\mathcal X_0\), \(Y\in\mathcal X_1^+\), and \(X\subset Y\),
the configurations which realize the two targets at one common active
phase already give

\[
 \frac{d(X,Y)}D
 \ge
 \frac{b_1(m-1)!m!}{s!M!}
 =\frac1{m+1}\frac{b_1}{\Lambda_1}
 =\frac{1+o(1)}m.
\tag{4.7a}
\]

Thus

\[
                         \Delta_2=\Theta(D/m).
\tag{4.7b}
\]

### Theorem 4.2 (physical intersection clustering)

If \(e(U,z)\) and \(e(V,w)\) have distinct roots, then

\[
 \boxed{
 |P(U,z)\cap P(V,w)|\le H(2H+1).}
\tag{4.8}
\]

#### Proof

At deletion length \(1\le\ell\le2H\), the common-core span theorem
bounds the number of equal traces of two physical paths by \(\ell\).
The protected tag word merely deletes some of these traces. Summing over
all deletion lengths gives

\[
                         1+2+\cdots+2H=H(2H+1).
\]

\(\square\)

Thus pair coincidences between configurations at distinct roots are
highly clustered:

\[
 \frac{\max_{\operatorname{root}(e)\ne
                   \operatorname{root}(f)}|P(e)\cap P(f)|}{k}
 =O\left(\frac{H^2}{m^{3/2}}\right)
 =O\left(\frac{\log m}{\sqrt m}\right)=o(1).
\tag{4.9}
\]

The root qualifier is necessary.  Parallel edges obtained by changing
only the order of the \(2H\) core labels can have identical target parts,
and hence intersection \(k\).  Such edges can never occur together in a
rooted matching, so they are irrelevant to (4.9)'s intended nibble
application.

This is the favorable statistic which a path-aware nibble would have to
use instead of expanding one vertical ladder into separate generic rows.

### Proposition 4.3 (vertical-spine pair mass)

For every configuration edge \(e\),

\[
 \boxed{
 \frac1D\sum_{\{X,Y\}\subseteq P(e)}d(X,Y)
 \ge c\sqrt m}
\tag{4.10}
\]

for an absolute constant \(c>0\) and all sufficiently large \(m\).

#### Proof

For every \(q\ge1\) and every phase with \(d_j\ge q\), the edge contains
the adjacent nested upper pair

\[
                         C_{z,j}(q-1)\subset C_{z,j}(q).
\tag{4.11}
\]

The configurations in which this prescribed pair occurs at one common
phase alone contribute

\[
 \frac{b_q}{D}\frac{(m-q)!(m+q-1)!}{s!}
 =\frac1{m+q}\frac{b_q}{\Lambda_q}
\tag{4.12}
\]

to its normalized codegree. Uniformly for \(1\le q\le\sqrt m\), one has

\[
                         b_q/\Lambda_q\ge c_0
\tag{4.13}
\]

for an absolute \(c_0>0\). There are exactly \(b_q\) pairs (4.11) in
the edge. Hence their contribution to the left side of (4.10) is at
least

\[
 \sum_{q\le\sqrt m}
    b_q\frac{c_0}{m+q}
 \ge c\sqrt m,
\]

because \(b_q=\Theta(m)\) throughout this range. \(\square\)

Therefore the aggregate pair correction in one edge is not \(o(1)\),
even though every individual relative codegree is \(O(1/m)\). This is
the exact vertical-ladder reason that a generic pairwise nibble estimate
does not close.

## 5. Rooted matching, convex relaxation, and exact hole conversion

### Theorem 5.1 (fractional optimum and all linear cuts)

The rooted matching LP

\[
 \sum_{e\ni U}x_e\le1\quad(U\in\mathcal U),
 \qquad
 \sum_{e\ni X}x_e\le1\quad(X\in\mathcal X),
 \qquad x_e\ge0
\tag{5.1}
\]

has optimum exactly \(N\). The assignment

\[
                              x_e=\frac1D
\tag{5.2}
\]

saturates every root.

#### Proof

Every edge contains one root, so the root capacities bound the objective
by \(N\). Under (5.2), every root has load \(D/D=1\), while Theorem 2.1
gives target load \(d_r/D=b_q/\Lambda_q\le1\). Thus (5.2) is feasible
with total weight \(N\). \(\square\)

This fractional point is joint: each LP column is one complete physical
path with all ranks and phases already coupled. It is not a stack of
separate Hall matchings.

### Theorem 5.2 (exact integral target)

If \(Q\) is a matching of size \(|Q|\), then its number of uncovered
target vertices is exactly

\[
 \boxed{
 \mathfrak H(Q)=\Delta+k(N-|Q|).}
\tag{5.3}
\]

Consequently

\[
 \boxed{
 \mathfrak H(Q)=o(W)
 \quad\Longleftrightarrow\quad
 N-|Q|=o(N/\sqrt m).}
\tag{5.4}
\]

#### Proof

A matching has disjoint target parts, so it covers exactly \(k|Q|\) of
the \(B\) targets. Equations (2.7) and (2.9) give

\[
 B-k|Q|=(B-kN)+k(N-|Q|)=\Delta+k(N-|Q|),
\]

proving (5.3). Since \(\Delta=o(W)\),
\(k=(\sqrt\pi+o(1))m^{3/2}\), and
\(N=\Theta(W/m)\), equation (5.4) follows. \(\square\)

### Corollary 5.2a (completion to one path per top)

If \(Q\) satisfies the right side of (5.4), choose an arbitrary legal
state at every root missed by \(Q\). The resulting selection contains
exactly one literal core-safe path per top, has aggregate target holes
\(o(W)\), and has aggregate repeat excess \(o(W)\).

#### Proof

Adding states cannot create holes. Every added state has \(k\) target
occurrences, so all added states together create at most

\[
                         k(N-|Q|)=o(W)
\]

duplicate occurrences. The matching holes are \(o(W)\) by (5.3).
\(\square\)

### Corollary 5.2b (exact relation to calibrated CCTPF)

A perfect matching of \(\mathcal K_{\rm cc}\) is equivalent to CCTPF
with a freely chosen core at every root and the one synchronized tag word
\(\mathbf d\).  More generally,

\[
\nu(\mathcal K_{\rm cc})=N-o(N/\sqrt m)
\tag{5.4a}
\]

already implies the coefficient-one theorem, even if no perfect matching
exists.

#### Proof

A perfect matching chooses one state at every root and makes all of their
protected target parts disjoint, which is precisely the stated
synchronized-tag fusion.  The converse is immediate by reading every
chosen state as one hyperedge.

Now assume (5.4a), take such a matching, and complete its missed roots as
in Corollary 5.2a.  Let \(M_0,E_0\) be the middle hole and repeat-excess
counts of the completed selection.  Every root contributes \(L\) middle
occurrences, so

\[
LN+M_0=W+E_0.
\tag{5.4b}
\]

Corollary 5.2a gives \(E_0=o(W)\) and aggregate protected signed holes
\(o(W)\).  Compile every selected path by its \(L+2H\) delayed-atom word.
Appending the missing middle masks changes the path baseline to

\[
W+E_0+2HN=W+o(W).
\]

Append the protected signed holes, both depth-\(H\) boundary layers at
cost \(2N=o(W)\), and the calibrated product-SCD exterior word of length
\(o(W)\).  This is a literal word of length \(W+o(W)\).  The trimmed lift
handles the other parity. \(\square\)

Thus (5.4a) is exactly equivalent to \(o(W)\) target leave *inside this
fixed-word hypergraph* and is sufficient for constant one.  It is not a
logical equivalence with the broader fixed-core/root-dependent-tag CCTPF
statement, which has a larger and differently organized option space.

### Theorem 5.3 (edge-transitive convex collapse)

Let \(\nu=\nu(\mathcal K_{\rm cc})\) and let \(\chi_f'\) be its
fractional edge-chromatic number. Then

\[
 \boxed{
                         \chi_f'=\frac{ND}{\nu}.}
\tag{5.5}
\]

In particular,

\[
 \boxed{
 \chi_f'=D+o(D/\sqrt m)
 \quad\Longleftrightarrow\quad
 \nu=N-o(N/\sqrt m).}
\tag{5.6}
\]

#### Proof

The action of \(S_{2m}\) is transitive on configuration edges: a
coordinate bijection sending the word \(z\) positionwise to \(z'\)
sends \(e(U,z)\) to \(e(U',z')\), while the fixed tag word remains on
the same phase positions.

For any finite edge-transitive hypergraph, averaging a maximum matching
over the automorphism group gives a fractional edge colouring of total
weight \(|E|/\nu\). Conversely every fractional edge colouring has total
weight at least \(|E|/\nu\), by summing all edge-cover inequalities and
using that a matching contains at most \(\nu\) edges. Here
\(|E|=ND\), proving (5.5). Equation (5.6) follows by writing
\(\nu=N-\ell\) and expanding

\[
                         \frac{ND}{N-\ell}
                         =\frac D{1-\ell/N}.
\]

\(\square\)

Thus an entropy, arbitrary-weight, or convex edge-colouring theorem at
the required accuracy is exactly as hard as the unweighted rooted
matching. Symmetry removes the weighted dual, but does not create the
integral support point.

## 6. Nibble test

### Theorem 6.1 (one literal joint bite)

For every fixed \(0<\eta<1\), the hypergraph contains a matching of size
at least

\[
                         \frac{\eta(1-\eta)}kN.
\tag{6.1}
\]

Every selected edge is one complete common-core tight path, so the bite
is collision-free simultaneously at the middle and at every signed
rank.

#### Proof

Activate every root independently with probability

\[
                              p=\frac\eta k,
\]

and, at each activated root, choose one of its \(D\) states uniformly.
Keep an activated state only if its target part is disjoint from every
other activated state.

Condition on a chosen edge \(e\). For one target \(X\in P(e)\), the
expected number of other activated chosen edges containing \(X\) is at
most

\[
                              p\frac{d(X)}D\le p.
\]

A union bound over the \(k\) targets of \(e\) makes its conditional
conflict probability at most \(kp=\eta\). Thus the expected number of
kept roots is at least \(p(1-\eta)N\). The kept edges form a matching,
so some outcome has at least the expectation in (6.1). \(\square\)

The theorem validates a first bite but is far from (5.4). A bite removes
only \(\Theta(1/k)\) of the roots. Reaching residual fraction
\(o(m^{-1/2})\) would require \(\Theta(k\log m)\) comparable bites, with
the option degrees regenerated after every deletion.

The exact diagonal parameters are

\[
 \frac{\Delta_2}{D}=\Theta(1/m),
 \qquad
 k=\Theta(m^{3/2}),
 \qquad
 k\frac{\Delta_2}{D}=\Theta(\sqrt m).
\tag{6.2}
\]

Hence a theorem whose error analysis assumes fixed edge rank, or assumes
\(k\Delta_2/D=o(1)\), is inapplicable. Proposition 4.3 shows that this is
not merely a loose maximum-codegree product: the actual vertical-spine
pair mass of every edge is already \(\Omega(\sqrt m)\).

On the other hand, Theorem 4.2 shows that these pair terms cluster into
only \(O(H^2)\) common targets for each pair of physical paths. Therefore
the exact possible successor is a **ladder-contracted rooted nibble**:
it must expose whole path conflicts, preserve the degree ratios
\(b_q/\Lambda_q\) jointly over all signed ranks, and reach root leave

\[
                              o(N/\sqrt m),
\tag{6.3}
\]

followed by a common-history absorber. Neither the one-vertex degrees nor
the pair codegrees prove the required regeneration.

## 7. Audited boundary

Proved:

1. the literal joint common-core tight-path configuration hypergraph;
2. its exact root, target, and root--target degrees;
3. the exact arbitrary-signed-rank pair codegree (3.5);
4. the universal \(O(D/m)\) maximum-codegree bound;
5. the \(O(H^2)\) physical two-path intersection bound;
6. the exact \(\Theta(m^{3/2})\) edge rank and \(o(W)\) scalar deficit;
7. an exact fractional matching saturating every root;
8. the matching-to-hole identity (5.3);
9. completion of a sufficiently large matching to exactly one path per
   top at \(o(W)\) extra repeat cost;
10. the edge-transitive convex collapse (5.5); and
11. one collision-free joint nibble bite.

Not proved:

1. a matching of size \(N-o(N/\sqrt m)\);
2. residual degree/codegree regeneration for \(\Theta(k\log m)\) bites;
3. a ladder-contracted absorber at the precision (6.3); or
4. coefficient one.

The exact conclusion is that coupling ranks and phases removes every
separate-Hall ambiguity and leaves one honest integral problem. Its pair
statistics are locally favorable, but growing edge rank makes their
aggregate vertical mass too large for a generic nibble. Any positive
theorem must use whole-path conflict clustering, not another collection
of independent rank matchings.
