# Lane W: complete-column Hall obstruction for proportional tight atoms

Date: 2026-07-25

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m=n\operatorname{Cat}_m,
 \qquad p=\left\lfloor\frac Wb\right\rfloor,
\]

and, for \(-H\le q\le H+1\),

\[
 N_q=\binom n{m+q},\qquad b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
\]

This note gives three exact conclusions about the proposed composition of
proportional tight atoms with correlated shadow-twin rounding.

1. There is no arithmetic obstruction to cutting an exact middle wreath
   factor into the required physical rows.  If

   \[
   H=\sqrt m\,\omega(m),\qquad H\ll b\ll\sqrt m\log m,
   \]

   then \(b\) may be chosen so that \(n\bmod b=o(\sqrt m)\).  Cutting every
   wreath into consecutive \(b\)-column rows then loses

   \[
   o(p/\sqrt m)
   \]

   rows, with every remaining row a literal injective tight row through
   depth \(H\).

2. Complete-column survival has an exact integral formulation.  At radius
   \(h\), every middle-owner column is one edge joining its lower
   \((m-h)\)-flag to its upper \((m+h+1)\)-flag.  A proportional bundle is a
   nested sequence of matchings in these paired flag graphs, with an exact
   number \(b_{-h}\) of surviving columns in every physical row.  The full
   zero-one system is stated in Theorem 2.1 below.

3. Marginal balanced factorial collision, even when it is exactly zero on
   both shores, does not control the paired Hall deficiency.  For every
   fixed

   \[
   0<a<\sqrt{\log(4/3)}
   \]

   and \(h=\lfloor a\sqrt m\rfloor\), there is an abstract paired-column
   graph having the exact values \(N_h,W\), the exact floor-optimal degree
   multiset on both shores, and hence zero balanced factorial excess, but
   maximum matching deficiency

   \[
   W-N_h=(e^{a^2}-1+o(1))N_h=\Theta_a(N_h).
   \]

   Its columns can moreover be partitioned, up to one row, into internally
   collision-free \(b\)-column blocks.  Any attempt to retain \(b_{-h}\)
   columns from every surviving block must delete \(\Omega_a(p)\) blocks,
   not \(o(p/\sqrt m)\).

The construction in item 3 is an obstruction to every proof which uses
only marginal curvature/type capacity, complete ledgers, and internal
row-disjointness.  It is not asserted to extend to an exact wreath factor.
Therefore it does not disprove the physical proportional-atom theorem.
It identifies the new theorem which a physical proof must supply: paired,
row-coloured, nested Hall expansion.  Shadow-twin cancellation of marginal
load vectors does not supply that theorem.

## 1. Exact arithmetic cutting lemma

Let

\[
 t=\operatorname{Cat}_m=\frac Wn.
\]

An exact middle wreath factor has exactly \(t\) wreaths, each with \(n\)
middle-owner columns.  Write

\[
 n=Ab+r,\qquad 0\le r<b.
\tag{1.1}
\]

Cut each wreath into \(A\) consecutive blocks of \(b\) columns and leave
its last \(r\) columns uncut.  The number of physical rows obtained is

\[
 P=At.
\tag{1.2}
\]

### Lemma 1.1 (exact cut deficiency)

One has

\[
 \boxed{p-P=\left\lfloor\frac{rt}{b}\right\rfloor.}
\tag{1.3}
\]

If \(b=o(n)\), then

\[
 p-P=o(p/\sqrt m)
 \quad\Longleftrightarrow\quad
 r=o(\sqrt m).
\tag{1.4}
\]

#### Proof

Since \(W=nt=(Ab+r)t\),

\[
 p=\left\lfloor\frac{W}{b}\right\rfloor
   =At+\left\lfloor\frac{rt}{b}\right\rfloor,
\]

which proves (1.3).  Moreover \(p\sim nt/b\), while the second term in
(1.3) is asymptotic to \(rt/b\) unless \(r=0\).  Hence

\[
 \frac{p-P}{p/\sqrt m}
 =\left(1+o(1)\right)\frac{r\sqrt m}{n}
 =\left(\frac12+o(1)\right)\frac r{\sqrt m}.
\]

This proves (1.4), including the case \(r=0\).  \(\square\)

### Lemma 1.2 (a compatible choice of \(b\))

Assume \(\omega(m)\to\infty\) and \(\omega(m)=o(\log m)\).  There is an
integer \(b=b(m)\) such that

\[
 \sqrt m\,\omega(m)\ll b\ll\sqrt m\log m,
 \qquad n\bmod b=o(\sqrt m).
\tag{1.5}
\]

#### Proof

Choose any \(L=L(m)\) with

\[
 \omega\ll L\ll\log m.
\]

Put

\[
 A=\left\lfloor\frac{n}{\sqrt m\,L}\right\rfloor,
 \qquad b=\left\lfloor\frac nA\right\rfloor.
\]

Then

\[
 A=(2+o(1))\frac{\sqrt m}{L},
 \qquad b=(1+o(1))\sqrt m\,L.
\]

Writing \(n=Ab+r\), the definition of \(b\) gives \(0\le r<A\), and so

\[
 r=O(\sqrt m/L)=o(\sqrt m).
\]

The two comparisons for \(b\) follow from \(\omega\ll L\ll\log m\).
\(\square\)

Because \(b+H=o(m)\), every consecutive \(b\)-column block, together with
its depth-\(H\) cyclic context, linearizes to an injective physical tight
row.  Lemmas 1.1--1.2 therefore remove the bare cycle-cutting obstruction.
For a generic untuned \(b\), however, (1.4) is a genuine necessary
arithmetic condition.

## 2. Exact complete-column formulation

Fix one exact middle wreath factor \(F\).  Its \(W\) pointed middle-owner
columns form a set \(\mathcal C(F)\).  If \(e\in\mathcal C(F)\) is the
column at a specified cyclic start, define its paired radius-\(h\) flags by

\[
 L_h(e)=\text{the length-}(m-h)\text{ interval at that start},
\]

\[
 U_h(e)=\text{the length-}(m+h+1)\text{ interval at that start}.
\tag{2.1}
\]

Thus \(L_h(e)\subset U_h(e)\), and a complete column surviving to radius
\(h\) contains both endpoints and every intervening flag.  Let

\[
 \beta_h=b_{-h}=b_{h+1}\qquad(0\le h\le H),
 \qquad \beta_{H+1}=0.
\tag{2.2}
\]

For the row blocks \(\mathcal R\) produced in Section 1, introduce binary
variables

\[
 x_R\in\{0,1\}\quad(R\in\mathcal R),
 \qquad y_{e,h}\in\{0,1\}\quad(e\in R,\ 0\le h\le H).
\]

Here \(x_R=1\) means that row \(R\) is retained, and \(y_{e,h}=1\) means
that its complete column \(e\) survives through radius \(h\).

Call a **profile-count proportional row** a physical tight row which has
the prescribed number \(\beta_h-\beta_{h+1}\) of radius-\(h\) columns,
but whose radius classes may occupy different start positions in different
rows.  This is slightly more flexible than the original homogeneous
proportional-atom hypergraph, where one fixed partition of the start
positions is used in every labelled atom.  The extra flexibility is
literal: every such row still has the same word length, rank counts, and
Pascal-column identities.

### Theorem 2.1 (complete-column equivalence)

For an integer \(z\ge0\), the cut factor contains at least

\[
 P-z
\]

pairwise target-disjoint profile-count proportional rows if and only
if the following zero-one system is feasible:

\[
 \sum_{R\in\mathcal R}x_R\ge P-z,
\tag{2.3}
\]

\[
 y_{e,0}=x_R\qquad(e\in R),
\tag{2.4}
\]

\[
 y_{e,h+1}\le y_{e,h}\qquad(0\le h<H),
\tag{2.5}
\]

\[
 \sum_{e\in R}y_{e,h}=\beta_hx_R
 \qquad(R\in\mathcal R,\ 0\le h\le H),
\tag{2.6}
\]

and, for every \(h\) and every target on either shore,

\[
 \sum_{e:L_h(e)=S}y_{e,h}\le1,
 \qquad
 \sum_{e:U_h(e)=T}y_{e,h}\le1.
\tag{2.7}
\]

#### Proof

Suppose first that (2.3)--(2.7) hold.  In a retained row \(R\), give column
\(e\) the radius

\[
 d(e)=\max\{h:y_{e,h}=1\}.
\]

Nesting (2.5) makes this well-defined.  Equation (2.6) says that exactly

\[
 \beta_h-\beta_{h+1}
\]

columns have radius exactly \(h\).  These are precisely the proportional
radius counts.  The fixed cyclic row makes every column a literal complete
Pascal flag, and (2.7) makes all flags of all retained rows pairwise
distinct at every rank.  Hence the retained rows are disjoint profile-count
proportional tight rows.

Conversely, in a disjoint family of such atoms, set \(x_R=1\) on retained
rows and let \(y_{e,h}\) record whether column \(e\) has radius at least
\(h\).  The proportional radius profile gives (2.4)--(2.6), and target
disjointness gives (2.7).  \(\square\)

This is the exact column-preserving replacement for a vertex-independent
residual in the variable-pattern setting.  Requiring the original fixed
start partition adds the further constraints that \(y_{e,h}\) be prescribed
by the relative position of \(e\) inside its row.  Thus Theorem 2.1 is a
necessary relaxation of the fixed-pattern proportional-atom matching
problem, and is itself sufficient for the literal constant-one reduction.
It also shows why separate depthwise rounding is insufficient: the same
variable \(y_{e,h}\) occurs at both signed endpoints, and the variables must
be nested in \(h\).

## 3. Floor-corrected paired Hall deficiency

For one radius \(h\), let \(G_h(F)\) be the bipartite multigraph with
shores

\[
 \binom{[n]}{m-h},\qquad \binom{[n]}{m+h+1},
\]

and one edge

\[
 e=(L_h(e),U_h(e))
\]

for every column \(e\in\mathcal C(F)\).  Both shores have size

\[
 N_h^-:=N_{-h}=N_{h+1}.
\]

Write

\[
 \nu_h(F)=\nu(G_h(F)),\qquad
 \delta_h(F)=N_h^- -\nu_h(F),
\tag{3.1}
\]

and retain the exact division

\[
 N_h^-=p\beta_h+R_h,
 \qquad 0\le R_h<p.
\tag{3.2}
\]

### Proposition 3.1 (exact row-leave lower bound)

If \(p-z\) proportional rows can be selected, even without demanding
nesting between different radii, then

\[
 \boxed{
 z\ge
 \left\lceil\frac{(\delta_h(F)-R_h)_+}{\beta_h}\right\rceil
 }
 \qquad(\beta_h>0).
\tag{3.3}
\]

Consequently the target \(z=o(p/\sqrt m)\) requires, at every active
radius,

\[
 \boxed{
 \delta_h(F)
 \le R_h+o\!\left(\frac{p\beta_h}{\sqrt m}\right)
 =R_h+o\!\left(\frac{N_h^-}{\sqrt m}\right).
 }
\tag{3.4}
\]

#### Proof

At radius \(h\), the surviving columns are edges of \(G_h(F)\) with no
repeated endpoint.  They are therefore a matching of size

\[
 (p-z)\beta_h.
\]

Using (3.1)--(3.2),

\[
 (p-z)\beta_h
 \le\nu_h(F)
 =p\beta_h+R_h-\delta_h(F).
\]

Rearrangement proves (3.3), and (3.4) follows.  \(\square\)

The deficiency has the usual exact Hall form

\[
 \delta_h(F)
 =\max_{X\subseteq\binom{[n]}{m-h}}
   \bigl(|X|-|N_{G_h(F)}(X)|\bigr).
\tag{3.5}
\]

It is a paired invariant.  The two marginal degree histograms do not
determine it.

There is also an exact deletion interpretation.  If \(D_h(F)\) is the
least number of columns which must be deleted to leave a paired matching,
then

\[
 D_h(F)=W-\nu_h(F)
       =(W-N_h^-)+\delta_h(F).
\tag{3.6}
\]

Thus \(W-N_h^-\) is the unavoidable proportional discard baseline, while
\(\delta_h(F)\) is precisely the extra discard caused by incompatible
lower/upper collision routing.

## 4. Zero marginal energy with linear paired deficiency

The next theorem is purely combinatorial.  It has the exact binomial
sizes of one Gaussian radius, but no exact-factor realizability is claimed.

For a bipartite graph \(G\) with equal shore size \(N\) and \(W\) edges,
put \(c=\lfloor W/N\rfloor\), and define the balanced second-factorial
excess on either shore by

\[
 \Delta^\pm(G)
 =\sum_v\frac{(\deg(v)-c)(\deg(v)-c-1)}2.
\tag{4.1}
\]

### Theorem 4.1 (balanced-star obstruction)

Fix \(0<a<\sqrt{\log(4/3)}\), set

\[
 h=\lfloor a\sqrt m\rfloor,
 \qquad N=\binom n{m-h},
\]

and retain \(W=\binom n m\).  For all sufficiently large \(m\), there is
a simple bipartite graph \(G\) such that

\[
 |L(G)|=|U(G)|=N,\qquad |E(G)|=W,
\tag{4.2}
\]

\[
 \Delta^-(G)=\Delta^+(G)=0,
\tag{4.3}
\]

but

\[
 \boxed{
 \nu(G)=2N-W,
 \qquad N-\nu(G)=W-N=\Theta_a(N).
 }
\tag{4.4}
\]

Moreover, the edges of \(G\) can be partitioned, after discarding fewer
than \(2b\) edges, into at least \(p-1\) blocks of \(b\) edges, every block
being a matching in \(G\).

#### Proof

The exact ratio is

\[
 \frac WN
 =\prod_{j=1}^{h}
   \frac{m+1+j}{m-h+j}.
\tag{4.5}
\]

Since \(h=a\sqrt m+O(1)\), taking logarithms gives

\[
 \log(W/N)=a^2+o(1).
\]

Hence, for all large \(m\),

\[
 1<W/N<4/3.
\tag{4.6}
\]

Put

\[
 r=W-N,
 \qquad y=N-3r.
\]

By (4.6), \(r>0\) and \(y\ge0\).  Take \(r\) disjoint six-vertex gadgets.
In one gadget, with left vertices \(\ell_1,\ell_2,\ell_3\) and right
vertices \(u_1,u_2,u_3\), use the four edges

\[
 \ell_1u_1,\quad \ell_2u_1,
 \quad \ell_3u_2,\quad \ell_3u_3.
\tag{4.7}
\]

Add \(y\) disjoint one-edge components.  Each shore then has

\[
 3r+y=N
\]

vertices, and the number of edges is

\[
 4r+y=N+r=W.
\]

On each shore a gadget has degree multiset \(\{1,1,2\}\), and every
one-edge component contributes degree one.  Thus exactly \(r=W-N\)
vertices have degree two and the other \(N-r\) have degree one.  This is
the exact floor/ceiling degree vector for \(c=1\), so every summand in
(4.1) vanishes and (4.3) follows.

The maximum matching in a gadget has size two, while every one-edge
component contributes one.  Therefore

\[
 \nu(G)=2r+y=N-r=2N-W,
\]

which proves (4.4).

Finally, colour the two edges in each two-edge star differently.  Give one
edge from each star in a gadget the first colour and the other edge the
second colour.  Distribute the one-edge components so that the two colour
classes differ in size by at most one.  Each colour class is a matching.
Splitting the two classes into consecutive groups of \(b\) edges yields

\[
 \left\lfloor\frac{|E_1|}{b}\right\rfloor
 +\left\lfloor\frac{|E_2|}{b}\right\rfloor
 \ge\left\lfloor\frac Wb\right\rfloor-1=p-1
\]

full internally disjoint blocks and leaves fewer than \(2b\) edges.
\(\square\)

Let \(\beta=\lfloor N/p\rfloor\), and let \(R=N-p\beta\).  Any family of
row blocks from Theorem 4.1 which retains \(\beta\) paired-disjoint columns
per row has size at most \(\nu(G)/\beta\).  Hence its row leave \(z\) obeys

\[
 z\ge\frac{(W-N)-R}{\beta}-O(1).
\tag{4.8}
\]

Here \(\beta=(e^{-a^2}+o(1))b\to\infty\), \(R<p=o(W-N)\), and

\[
 \boxed{
 \frac zp\ge e^{a^2}-1-o(1).
 }
\tag{4.9}
\]

Thus the required leave fails by a constant factor even though both
marginal factorial excesses are exactly zero and almost all columns have
already been grouped into internally valid physical-row-sized blocks.

The obstruction is the failure to align the two shore collisions.  In one
gadget, the duplicated upper target uses the first two columns, while the
duplicated lower target uses the last two.  The proportional discard
budget pays for one duplicate on each shore only if the same discarded
column can resolve both.  Here two distinct columns are compulsory.

## 5. Separate Hall is not complete-column Hall

There is an independent fixed-coordinate integrality obstruction.  Let
the lower shore be \(\{a,b\}\), the upper shore \(\{x,y\}\), and take two
row colours

\[
 R_1:\ (a,x),(b,y),
 \qquad
 R_2:\ (a,y),(b,x).
\tag{5.1}
\]

Demand one edge of each colour.  On the lower shore alone, and on the
upper shore alone, every row-subfamily satisfies the exact Hall
inequality.  The uncoloured paired graph is \(K_{2,2}\) and has a perfect
matching.  Nevertheless every choice of one edge from each colour repeats
one endpoint.  Hence no complete-column selection exists.

The obstruction amplifies at exact half quota.  Let \(b\) be even, let
\(R_1\) be the identity perfect matching on two \(b\)-sets, and let \(R_2\)
be the perfect matching given by one \(b\)-cycle \(\pi\).  If one chooses
\(b/2\) edges of each colour, write \(I\) and \(J\) for their lower
coordinates.  Lower disjointness forces \(J=I^c\).  Upper disjointness then
forces

\[
 \pi(J)=J.
\]

A single cycle has no nonempty proper invariant set, a contradiction.
Replicating this construction in disjoint pairs of row colours forces the
deletion of at least half the rows.  All marginal degrees are constant,
both one-sided row-Hall systems hold, and the uncoloured graph has a
perfect matching.

This example isolates a second missing assertion beyond (3.4): even small
uncoloured paired Hall deficiency does not distribute a matching in the
prescribed amount among every row block.  The shared column coordinate
must be retained explicitly.

## 6. Exact remaining lemma

For the parameter choice of Lemma 1.2, define

\[
 \varepsilon_m=o(1/\sqrt m).
\]

The precise sufficient statement for this route is the following.

> **Nested paired-column expansion \(\mathrm{NPCE}(H,b,\varepsilon_m)\).**
> There is one exact middle wreath factor \(F\), cut into the \(P\) physical
> \(b\)-column rows of Section 1, for which the zero-one system
> (2.3)--(2.7) is feasible with
> \[
> z\le\varepsilon_m p.
> \]

By Theorem 2.1 and Lemmas 1.1--1.2, NPCE gives

\[
 p-o(p/\sqrt m)
\]

disjoint profile-count proportional tight rows.  Their word cost, floor
repair, and missing-row repair obey exactly the same calculation as in the
proportional-atom reduction, because that calculation uses only the
per-rank counts and the literal interval identity;
the already audited product-tail word handles the complement of the
growing band.  Hence NPCE composes into the constant-one theorem.

Every proof of NPCE must in particular establish the floor-corrected
paired Hall inequalities (3.4).  It must then prove row-coloured
integrality and common nesting, neither of which follows from (3.4) alone.
Theorems 4.1 and Section 5 show respectively that

\[
 \text{marginal factorial energy}
 \not\Rightarrow
 \text{paired Hall expansion},
\]

and

\[
 \text{two separate Hall systems}
 \not\Rightarrow
 \text{common-column integrality}.
\]

Thus a correlated shadow-twin theorem can enter this route only if it
controls the paired graphs \(G_h(F)\) and the common column variables, not
merely the lower and upper load vectors.  An \(O(H\operatorname{Cat}_m)\)
marginal curvature/type-capacity estimate, by itself, does not address the
new invariant.

## 7. Proved and unproved boundary

Proved here:

1. the exact cycle-cut deficiency and a compatible choice of \(b\);
2. the exact necessary-and-sufficient complete-column zero-one system;
3. the exact floor-corrected one-radius Hall lower bound;
4. a zero-marginal-energy, linear-paired-deficiency obstruction with the
   exact binomial values \(W,N_h\);
5. a fixed-coordinate obstruction showing that separate Hall and an
   uncoloured perfect matching still do not imply row-balanced column
   selection.

Not proved here:

1. realization of the abstract obstruction of Theorem 4.1 by one exact
   wreath factor;
2. failure of NPCE for all exact factors;
3. any positive paired-Hall consequence of the known shadow-twin menu;
4. the constant-one theorem.

The rigorous conclusion is therefore a no-go for the proposed implication
from marginal shadow-twin collision rounding to proportional-atom
matching.  The physical route remains open exactly at NPCE.

## 8. A stronger depth-one obstruction for two deletion profiles

There is a second obstruction which applies directly to any two-state
profile obtained by deleting complete columns from the same starting
factor.

Let \(\mu(S)\) be the starting depth-one load.  In state
\(\varepsilon\in\{0,1\}\), delete \(d_\varepsilon(S)\) of those
occurrences, so that

\[
 \mu^\varepsilon(S)=\mu(S)-d_\varepsilon(S)\ge0.
\tag{8.1}
\]

Assume both states delete the same total number

\[
 \sum_Sd_0(S)=\sum_Sd_1(S)=D.
\tag{8.2}
\]

Their invariant pair sum at \(S\) is

\[
 t(S)=2\mu(S)-d_0(S)-d_1(S).
\tag{8.3}
\]

Because the selected depth-one total is below the target-class size, its
floor is \(c=0\).  The coordinatewise pair-floor from the exact two-state
identity is therefore

\[
 b_0(t)=\left\lfloor\frac{(t-1)^2}{4}\right\rfloor.
\tag{8.4}
\]

Put

\[
 C_1(F)=\sum_S(\mu(S)-1)_+,
\qquad
 B_1=\sum_Sb_0(t(S)).
\tag{8.5}
\]

### Theorem 8.1 (pair-floor survives column thinning)

Under (8.1)--(8.5),

\[
 \boxed{B_1\ge C_1(F)-D.}
\tag{8.6}
\]

#### Proof

If \(\mu=0\), then \(d_0=d_1=t=0\), and the pointwise inequality is
zero.  If \(\mu\ge1\), write \(d=d_0+d_1\).  Since \(t=2\mu-d\),

\[
 (\mu-1)-\frac d2=\frac t2-1.
\tag{8.7}
\]

For every integer \(t\ge0\),

\[
 \left\lfloor\frac{(t-1)^2}{4}\right\rfloor
 \ge\frac t2-1.
\tag{8.8}
\]

Indeed, for \(t=2k\) the difference between the two sides is
\((k-1)^2\), while for \(t=2k+1\) it is
\(k^2-k+1/2\).  Thus

\[
 b_0(t(S))
 \ge(\mu(S)-1)_+
   -\frac{d_0(S)+d_1(S)}2.
\]

Summing and using (8.2) proves (8.6).  \(\square\)

The quasi-divisor cutting of Lemma 1.2 gives \(D=O(W/b)\).  In fact the
no-go needs much less.  Let

\[
 N_{-1}=p b_{-1}+R_1,\qquad 0\le R_1<p.
\]

Since

\[
 W-N_{-1}=\frac{2W}{m+2},
\]

any state retaining \(s=p-o(p/\sqrt m)\) rows has

\[
\begin{aligned}
 D
 &=W-sb_{-1}\\
 &=\frac{2W}{m+2}+R_1+(p-s)b_{-1}\\
 &=o(W),
\end{aligned}
\tag{8.9}
\]

using \(p=O(W/b)\), \(b=o(m)\), and \(b_{-1}\le b\).  Therefore:

### Corollary 8.2 (linear-collision same-factor no-go)

If a sequence of starting exact factors satisfies

\[
 C_1(F_m)\ge cW
\]

for some fixed \(c>0\), then every two-profile construction which only
deletes complete columns from \(F_m\), deletes the same total in its two
states, and retains \(p-o(p/\sqrt m)\) rows satisfies

\[
 \boxed{B_1\ge(c-o(1))W.}
\tag{8.10}
\]

It therefore cannot meet a pair-floor hypothesis \(B_1=o(W)\).

For the canonical MSW factor, the audited marked-gap estimate gives

\[
 C_1(F_m^{\mathrm{MSW}})
 \ge (2m-3)\operatorname{Cat}_{m-2}
 =\left(\frac1{16}+o(1)\right)W.
\tag{8.11}
\]

Hence every allowed-leave two-profile thinning of that same factor has

\[
 B_1\ge\left(\frac1{16}-o(1)\right)W.
\tag{8.12}
\]

This statement has a narrow but exact scope.  It rules out profile changes
which only delete occurrences from one fixed depth-one system.  A genuine
depth-one-active exact trade can replace old flags by new flags and is not
of the form (8.1); such a trade is not excluded by Theorem 8.1.
