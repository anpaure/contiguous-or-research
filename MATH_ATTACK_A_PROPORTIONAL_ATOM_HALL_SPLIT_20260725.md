# Proportional tight atoms: exact Boolean Hall packing and the first/second-collision split

Date: 2026-07-25

Put

\[
n=2m+1,\qquad N_q=\binom n{m+q},\qquad
p=\left\lfloor\frac{W}{b}\right\rfloor,\qquad
b_q=\left\lfloor\frac{N_q}{p}\right\rfloor .
\]

The notation and atom template are those of
`PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md`.  This note proves
two positive statements with every floor retained.  It also audits the
tempting inference obtained by deleting the adjacent-rank part of the local
overlap sum.

## 1. Exact proportional packing in the Boolean nested-flow relaxation

For (0\le d\le H), write

\[
M_d=pb_{-d}=pb_{d+1},
\]

and put

\[
a_d=b_{-d}-b_{-(d+1)}\quad(0\le d<H),
\qquad a_H=b_{-H}.
\]

### Theorem 1.1 (all proportional floor quotas are jointly integral)

There are (p) pairwise vertex-disjoint abstract proportional bundles in
the Boolean lattice.  Every bundle contains exactly (a_d) saturated
symmetric chains truncated to radius (d), for every (0\le d\le H).
Consequently every bundle contains exactly (b_q) vertices in rank
(m+q), for every (-H\le q\le H+1), and globally the selected bundles
use exactly

\[
pb_q=N_q-R_q,\qquad 0\le R_q<p,
\]

vertices of that rank.

#### Proof

Fix any symmetric-chain decomposition \(\mathscr D\) of (B_n).  Let
\(\mathscr D_{\ge d}\) be the chains whose radius is at least (d).  Every
such chain contains exactly one vertex in rank (m-d), and every vertex of
that rank lies on one such chain.  Therefore

\[
|\mathscr D_{\ge d}|=N_{-d}.
\tag{1.1}
\]

The sets \(\mathscr D_{\ge d}\) decrease with (d), while the integers
(M_d) also decrease with (d).  Choose nested chain-index sets

\[
K_H\subseteq K_{H-1}\subseteq\cdots\subseteq K_0,
\qquad K_d\subseteq\mathscr D_{\ge d},\qquad |K_d|=M_d.
\tag{1.2}
\]

This is possible recursively.  Having chosen (K_{d+1}), the number of
available chains in \(\mathscr D_{\ge d}\setminus K_{d+1}) is

\[
N_{-d}-M_{d+1}\ge M_d-M_{d+1},
\]

because (M_d\le N_{-d}).

For a chain (C\in K_0), let \(\rho(C)\) be the largest (d) for which
(C\in K_d), and retain from (C) only its symmetric central segment from
rank (m-\rho(C)) through rank (m+\rho(C)+1).  At depth (d), the
retained segment is present exactly when (C\in K_d).  Hence the number of
retained vertices in each of the symmetric ranks (m-d,m+d+1) is exactly

\[
|K_d|=M_d=pb_{-d}=pb_{d+1}.
\tag{1.3}
\]

The number of retained segments of exact radius (d<H) is

\[
M_d-M_{d+1}=p(b_{-d}-b_{-(d+1)})=pa_d,
\]

and the number of radius-(H) segments is (M_H=pa_H).  Partition the
segments of each radius into (p) groups of size (a_d), and combine one
group of every radius into each bundle.  The bundles are disjoint because
they use subchains of the fixed decomposition.  Telescoping gives exactly
(b_q) vertices per rank in every bundle.  \(\square\)

The adjacent-rank Hall expansion used by this construction has an exact
quantitative form.  If

\[
\mathcal A\subseteq\binom{[n]}{m-d},\qquad d\ge0,
\]

then flag counting gives

\[
|\nabla\mathcal A|
\ge\frac{m+d+1}{m-d+1}|\mathcal A|
=|\mathcal A|+\frac{2d}{m-d+1}|\mathcal A|.
\tag{1.4}
\]

Thus every Boolean adjacent-layer cut, including the corresponding
depth-three proportional-flow cut, is integrally feasible in the abstract
nested-flow relaxation.  This is not an assertion about the earlier
fixed-core high-set cut.  Theorem 1.1 makes no physical tight-row claim.

## 2. The exact first/second-collision split

Let (P,Q) be designated position intervals, let (r=|P|), and put

\[
a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\]

For fixed (P,a,c), at most (a+c+1) designated intervals (Q) have
these two differences.  Fix a test atom (e), a target (v\in e), and
the slot (P_0) occupied by (v) in (e).  At most (a+c+1) targets
(w\in e\setminus\{v\}) have

\[
|v\setminus w|=a,\qquad |w\setminus v|=c.
\tag{2.1}
\]

Condition a uniformly random labelled atom (F) containing (v) on the
slot (P) occupied by (v).  For a fixed such (w), the second interval
can occupy at most (a+c+1) slots, and the exact conditional probability
at each possible slot is

\[
\frac1{\binom r a\binom{n-r}c}.
\]

The possible-slot events are disjoint.  Consequently

\[
\sum_{w\in e\setminus\{v\}}
 \Pr(w\in F\mid v\hbox{ occupies }P)
\le
\sum_{a+c\ge1}
\frac{(a+c+1)^2}{\binom r a\binom{n-r}c}.
\tag{2.2}
\]

Both interval multiplicities are present in the square: one counts the
locations of (w) in the test atom and one counts its possible locations
in (F).

### Lemma 2.1 (adjacent ranks are the whole (m^{-1}) term)

Uniformly for (m-H\le r\le m+H+1),

\[
\sum_{a+c=1}
\frac{(a+c+1)^2}{\binom r a\binom{n-r}c}
=\frac4r+\frac4{n-r}=O(m^{-1}),
\tag{2.3}
\]

whereas

\[
\sum_{a+c\ge2}
\frac{(a+c+1)^2}{\binom r a\binom{n-r}c}
=O(m^{-2}).
\tag{2.4}
\]

#### Proof

For (a+c=1), the pairs are ((1,0)) and ((0,1)), giving (2.3)
exactly in the displayed upper bound.  Geometrically these are precisely
nested position intervals differing by one endpoint.

Put (R=m-H).  All relevant values of (r,n-r) are at least (R), and
all nonzero (a,c) are at most (b+2H=o(R)).  The one-variable estimates

\[
\sum_{j\ge1}\frac{(j+1)^2}{\binom Rj}=O(R^{-1}),
\qquad
\sum_{j\ge2}\frac{(j+1)^2}{\binom Rj}=O(R^{-2})
\tag{2.5}
\]

hold uniformly over the truncated range.  Indeed, the first terms are
(4/R) and (9/\binom R2), respectively, and the ratio of successive
polynomially weighted terms is (O((b+2H)/R)=o(1)).

The terms in (2.4) with exactly one of (a,c) zero are covered by the
second estimate in (2.5).  If (a,c\ge1), use

\[
(a+c+1)^2\le 2(a+1)^2(c+1)^2
\]

and the product of the two first estimates in (2.5).  This proves
(2.4).  \(\square\)

Averaging over the possible slots occupied by (v) yields the intrinsic
split

\[
\max_{v,e\ni v}
\sum_{\substack{w\in e\setminus\{v\}\\ |v\triangle w|=1}}
\frac{\deg(v,w)}{\deg(v)}=O(m^{-1}),
\tag{2.6}
\]

and

\[
\max_{v,e\ni v}
\sum_{\substack{w\in e\setminus\{v\}\\ |v\triangle w|\ge2}}
\frac{\deg(v,w)}{\deg(v)}=O(m^{-2}).
\tag{2.7}
\]

These statements hold for the simple atom hypergraph as well.  Indeed,
the set of injective words is one transitive (S_n)-set, the map from a
word to its designated simple target system is equivariant, and its image
is one (S_n)-orbit.  Every simple atom therefore has the same number of
word representatives.  Collapsing labels divides every degree and every
codegree by that same constant.

## 3. A genuine local Hall consequence

Let (D_e=\min_{v\in e}\deg(v)).  The split is strong enough to give a
large integral collar fan around one atom.

### Proposition 3.1 (star-collar clone Hall)

There is an absolute (C) such that, for every atom (e), one may assign

\[
h_e=\left\lfloor(1-C/m)D_e\right\rfloor
\]

distinct simple atoms to every (v\in e), each assigned atom containing
its assigned (v), with no simple atom assigned twice anywhere in the
whole family.

#### Proof

For (S\subseteq e), let \(\Gamma(S)\) be the set of simple atoms meeting
(S).  Bonferroni and the full row-sum estimate give

\[
\begin{aligned}
|\Gamma(S)|
&\ge \sum_{v\in S}\deg(v)
 -\sum_{\{v,w\}\subseteq S}\deg(v,w)\\
&\ge \left(1-\frac C m\right)
       \sum_{v\in S}\deg(v)
\ge h_e|S|.
\end{aligned}
\tag{3.1}
\]

Replace every (v\in e) by (h_e) clones, all with neighborhood
\(\Gamma(\{v\})\).  For an arbitrary set of clones with support (S),
its size is at most (h_e|S|\le|\Gamma(S)|).  Hall's theorem supplies the
claimed integral assignment.  \(\square\)

This relative (O(m^{-1})=o(m^{-1/2})) loss is a real absorber reservoir.
It is local: the assigned atoms are distinct, but Proposition 3.1 does not
say that they are mutually target-disjoint.

The sharpened non-cover estimate gives the corresponding (m^{-2})
statement whenever the first-order pairs have genuinely been removed.

### Proposition 3.2 (non-cover private collar)

Let (S\subseteq e) satisfy

\[
 |v\mathbin\triangle w|\ge2\qquad(v,w\in S,\ v\ne w).
\tag{3.2}
\]

There is an absolute (C) such that every (v\in S) belongs to at least

\[
 \left(1-\frac{C}{m^2}\right)\deg(v)
\tag{3.3}
\]

simple atoms which contain no other member of (S).  Consequently, with

\[
 h_S=\left\lfloor
 \left(1-\frac{C}{m^2}\right)\min_{v\in S}\deg(v)
 \right\rfloor,
\tag{3.4}
\]

one can assign (h_S) distinct private atoms to every (v\in S), with
no assigned atom used for two vertices of (S).

#### Proof

For (v\in S), let

\[
 \mathcal L_v=\{F:v\in F,\ F\cap S=\{v\}\}.
\]

By the union bound and (2.7),

\[
 |\mathcal L_v|
 \ge \deg(v)-\sum_{w\in S\setminus\{v\}}\deg(v,w)
 \ge \left(1-\frac{C}{m^2}\right)\deg(v).
\tag{3.5}
\]

The families \(\mathcal L_v\) are pairwise disjoint: an atom in both
\(\mathcal L_v\) and \(\mathcal L_w\) would meet (S) in both (v) and
(w).  Choose any (h_S) atoms from each family.  This is an integral
private-collar assignment and, equivalently, the associated cloned Hall
system has zero cross-fibre intersections. \(\square\)

Proposition 3.2 is the exact Hall gain suggested by the
(O(m^{-2})) tail.  Its hypothesis is a statement about actual target
pairs.  Section 4 shows why a one-chain nested resolution does not produce
such a residual family of physical rows.

Nor can the \(m^{-2}\) statistic alone imply a global matching theorem.

### Proposition 3.3 (second-order overlap alone has no rounding theorem)

For every sufficiently large \(m\), there is a regular partite simple
hypergraph \(\mathcal G_m\) with fractional matching number \(Q\), matching
number \(1\), and

\[
 \max_{x\ne y}
 \frac{\deg(x,y)}{\deg(x)}\le \frac1{m^2}.
\tag{3.6}
\]

#### Proof

Choose a prime power \(Q\ge m^2\) and a projective plane of order \(Q\).
Fix a point \(z\).  The \(Q+1\) lines through \(z\), with \(z\) deleted,
are the vertex parts, each of size \(Q\).  The hyperedges are the \(Q^2\)
projective lines not through \(z\).  Every edge meets every part once,
every vertex has degree \(Q\), and two distinct vertices lie on at most
one common edge.  Thus (3.6) holds.  Weighting every edge by \(1/Q\)
gives a fractional matching of total weight \(Q\).  But every two
projective lines meet, so the integral matching number is \(1\).
\(\square\)

This counterexample is not an atom counterexample.  It proves the exact
logical boundary: a global long-row Hall expansion, not merely the
non-cover codegree row sum, is indispensable.

## 4. Why an SCD cannot simply remove (2.6)

Theorem 1.1 resolves every adjacent Boolean marginal, but it does not
turn (2.7) into the codegree statistic of a residual physical-atom
hypergraph.

Fix one adjacent template pair (P\subset Q), with 

\[
|Q|=|P|+1,
\]

and condition on target (v) occupying (P).  The point of (Q\setminus
P) is uniform over the (n-|v|=\Theta(m)) points outside (v).  A fixed
symmetric-chain decomposition prescribes at most one upper mate of (v).
Therefore only

\[
\frac1{n-|v|}=\Theta(m^{-1})
\tag{4.1}
\]

of the atoms using that adjacent slot pair follow the prescribed SCD edge.
The analogous lower figure is (1/|v|=\Theta(m^{-1})).  Requiring an
entire radius-(d) physical column to follow one fixed SCD retains at most
a product of (d) such factors.  At the radii occurring in the Gaussian
profile this is not a (1-o(m^{-1/2})) restriction; it destroys essentially
all atom degree.

Equivalently, an SCD chooses one adjacent partner for a target, whereas
the atoms containing that target realize all Boolean adjacent partners.
The choices made independently for different targets do not have common
physical-row ownership.  Thus there is no globally defined operation
"contract the (a+c=1) pairs" on the current atom hypergraph.

There is a second exact logical distinction.  Estimate (2.7) controls a
second collision:

\[
F\hbox{ meets a fixed atom }e\hbox{ in two specified nonadjacent targets}.
\]

A near-perfect packing is governed first by

\[
F\hbox{ meets the union of the already selected atoms at least once}.
\]

Near saturation the latter event has order one.  A second-moment row sum
does not supply the correlation needed to make the remaining targets occur
in whole physical columns.

Hence the (O(m^{-2})) statistic, even after the exact abstract packing of
Theorem 1.1, does not by itself imply a matching of
(p-o(p/\sqrt m)) physical atoms.

There is an exact obstruction already at the two central ranks.  Put

\[
 P_i=[i,i+m-1],\qquad U_i=[i,i+m]\qquad(0\le i<b).
\tag{4.2}
\]

Because (b_0=b_1=b), every atom contains both cover edges

\[
 P_i\subset U_i,\qquad P_{i+1}\subset U_i\quad(0\le i<b-1),
\tag{4.3}
\]

forming the alternating path

\[
 P_0-U_0-P_1-U_1-\cdots-P_{b-1}-U_{b-1}.
\tag{4.4}
\]

For every actual cover pair (A\subset B), (|A|=m), the exact labelled
ratio is

\[
 \frac{\deg(A,B)}{\deg(A)}
 =\frac{2b-1}{b(m+1)}.
\tag{4.5}
\]

Indeed there are (b) same-start and (b-1) adjacent-start slot
representations, each contributing conditional probability (1/(m+1)),
while (A) has (b) possible central slots.  A nested-chain flow is a
matching between the two central Boolean ranks, so it can contain at most
(b) of the (2b-1) ladder edges of any atom.  At least (b-1) cover
edges remain.  If \(R_e\) is this set of uncontracted actual ladder pairs,
their exact average normalized contribution over the \(b\) lower targets is

\[
 \frac1b\sum_{(A,B)\in R_e}\frac{\deg(A,B)}{\deg(A)}
 =\frac{|R_e|(2b-1)}{b^2(m+1)}
 \ge\frac{(b-1)(2b-1)}{b^2(m+1)}
 =(2+o(1))m^{-1}.
\tag{4.6}
\]

Thus an actual-target chain matching leaves \(\Omega(m^{-1})\), not
\(O(m^{-2})\).

At the labelled slot-representation level, deleting only the \(b\)
same-start representations leaves the explicit contribution

\[
 \frac{b-1}{b(m+1)}=(1+o(1))m^{-1}.
\tag{4.7}
\]

This is not a separate simple-hypergraph codegree: after parallel
representations are collapsed, an actual cover pair carries the full ratio
(4.5).  Both formulations give the same required conclusion that the
first-order term survives.

Contracting both kinds of cover edge identifies the whole central ladder.
For the nested multiradius start profile, every deeper designated slot is
joined by same-start cover edges to this ladder.  Thus the full
(a+c=1) slot graph is connected: contracting it contracts one entire
physical atom, which is the desired long-row object rather than a smaller
residual object.

The obstruction is to extending the ladder resolution through all depths,
not to the central ladder by itself.  The latter has the following sharp
physical construction.

### Proposition 4.1 (near-perfect physical central-ladder packing)

Assume an exact middle wreath factor, as is already known.  Put

\[
 K=\left\lceil\frac{n}{m^{3/4}}\right\rceil,
 \qquad b=\left\lfloor\frac nK\right\rfloor,
 \qquad n=Kb+r,\quad 0\le r<K.
\tag{4.8}
\]

This admissible choice still satisfies \(b=(1+o(1))m^{3/4}\), so every
estimate in the proportional-atom reduction is unchanged.  If
\(p=\lfloor W/b\rfloor\), there are

\[
 s=p-t,\qquad \frac{t}{p}=O(m^{-3/4})=o(m^{-1/2}),
\tag{4.9}
\]

physical \(b\)-start tight segments whose rank-\(m\) and rank-\((m+1)\)
targets are pairwise disjoint.  Thus the complete central alternating
ladders can be resolved with more than the required quantitative accuracy.

#### Proof

An exact middle wreath factor has

\[
 B=\frac Wn
\]

cyclic coordinate rows, and the \(n\) rank-\(m\) windows on those rows
partition \(\binom{[n]}m\).  The rank-\((m+1)\) windows also partition:
the complement of the length-\((m+1)\) window starting at \(i\) is the
length-\(m\) window starting at \(i+m+1\) on the same cyclic row.

Since \(r<K<b\) for large \(m\), every cyclic row has exactly \(K\)
disjoint blocks of \(b\) consecutive starts, leaving \(r\) starts.  Taking
these blocks on all \(B\) rows gives \(s=KB\) physical tight segments and
keeps both central ranks disjoint.  Moreover

\[
 p=\left\lfloor\frac{(Kb+r)B}{b}\right\rfloor
   =KB+\left\lfloor\frac{rB}{b}\right\rfloor,
\]

so

\[
 0\le t=p-s\le\frac{rB}{b},
 \qquad
 \frac tp
 \le\frac{rB/b}{KB}
 =\frac r{Kb}
 =\frac r{n-r}
 \le\frac K{n-K}=O(m^{-3/4}).
\]

Finally \(p>b\), and

\[
 b\le\frac Wp<\frac{W}{W/b-1}<b+1
\]

for all large \(m\), so \(b_0=b_1=b\) exactly.  Also \(m+b+H<n\), so
each cyclic block has the injective collar needed to be a legal
proportional-atom word. \(\square\)

Proposition 4.1 absorbs the first central ladder using whole physical rows,
not a one-parent chain matching.  At the next depths, the targets induced
by different wreath rows may coincide.  The exact common-owner theorem
needed to prevent those coincidences is still absent; neither Proposition
3.2 nor an abstract SCD chooses it.

There is also a precise conditioning loss.  Fixing the central ladder
freezes almost all fixed-window targets of that row.

### Lemma 4.2 (central-ladder conditioning rigidity)

Fix the sets

\[
 P_i=A_{i,0},\qquad U_i=A_{i,1}\qquad(0\le i<b)
\]

of one realizable central ladder.  In every injective tight-word
completion of this ladder:

1. \(A_{i,-d}\) is already determined for every \(i\ge d\);
2. \(A_{i,d}\) is already determined for every \(i\le b-d\).

Consequently, at signed depth \(q\), at most \(|q|+1\) of the designated
targets can depend on the unexposed endpoint collar.  For every fixed
\(A\), uniformly over \(|q|\le A\sqrt m\), this is \(O_A(\sqrt m)\),
whereas \(b_q=\Theta_A(b)\).  Thus a proportion

\[
 1-O_A\!\left(\frac{\sqrt m}{b}\right)
 =1-O_A(m^{-1/4})
\tag{4.10}
\]

of every row's designated targets is fixed once its central ladder is
fixed.

#### Proof

Write

\[
 P_i=\{x_i,\ldots,x_{i+m-1}\},\qquad
 U_i=P_i\cup\{x_{i+m}\}.
\]

The ladder therefore determines each entering coordinate
\(y_i:=x_{i+m}=U_i\setminus P_i\) for \(0\le i<b\).  If \(i\ge d\), then

\[
 A_{i,-d}
 =P_i\setminus\{y_{i-d},y_{i-d+1},\ldots,y_{i-1}\},
\]

which proves the first assertion.  If \(i\le b-d\), then

\[
 A_{i,d}
 =P_i\cup\{y_i,y_{i+1},\ldots,y_{i+d-1}\},
\]

which proves the second.  Only the first \(d\) lower starts and the last
at most \(d\) upper starts can use unexposed collar coordinates.  Intersect
these exceptional starts with the chosen \(I_q\).  Finally the local
Gaussian estimate gives \(N_q/W=\Theta_A(1)\) and hence
\(b_q=\Theta_A(b)\) on the fixed window, proving (4.10). \(\square\)

Lemma 4.2 blocks one further shortcut.  The \(O(m^{-2})\) overlap estimate
is averaged over unrestricted tight rows.  After the central ladders from
Proposition 4.1 are fixed, almost all deeper targets are deterministic, so
the same conditional estimate need not hold.  Proving it for a selected
exact factor would itself be a new common-owner pseudorandomness theorem.

The resulting unavoidable ledger can be stated exactly.  For a family
\(\mathscr B\) of central ladders and a signed depth \(q\), let
\(\mathcal D_q(B)\) be the designated targets whose starts lie in the
determined range of Lemma 4.2, and put

\[
 \mu_q(X)=|\{B\in\mathscr B:X\in\mathcal D_q(B)\}|,
 \qquad
 E_q^{\rm int}=\sum_X(\mu_q(X)-1)_+.
\tag{4.11}
\]

### Lemma 4.3 (interior-overload deletion bound)

If deleting \(t\) central ladders leaves a family admitting pairwise
target-disjoint physical completions, then

\[
 t\,b_q\ge E_q^{\rm int}
\tag{4.12}
\]

at every depth.  More generally, on a fixed window \(\mathcal Q_A\),

\[
 t\sum_{q\in\mathcal Q_A}b_q
 \ge \sum_{q\in\mathcal Q_A}E_q^{\rm int}.
\tag{4.13}
\]

#### Proof

For a target occurring \(\mu_q(X)\) times among the determined slots, at
least \(\mu_q(X)-1\) of those occurrences must be removed; endpoint-collar
choices cannot change them.  Hence at least \(E_q^{\rm int}\) determined
occurrences must disappear.  Deleting one ladder removes at most \(b_q\)
occurrences at depth \(q\), proving (4.12).  Summing before applying the
same deletion bound gives (4.13). \(\square\)

Since \(\sum_{q\in\mathcal Q_A}b_q=\Theta_A(b\sqrt m)\), a completion
with \(t=o(p/\sqrt m)\) necessarily has

\[
 \sum_{q\in\mathcal Q_A}E_q^{\rm int}=o(pb)=o(W).
\tag{4.14}
\]

Thus the conditioned long-row Hall theorem needs an \(o(W)\) common-owner
interior-overload bound in addition to the unrestricted \(m^{-2}\)
second-collision estimate.  Equation (4.14) is not supplied by Boolean
shadow expansion or by marginal nested-flow integrality.

## 5. Smallest remaining physical statement

The missing input is an **atom-coherent physical lift**, not another
rankwise quota estimate:

> Choose the nested chain sets (K_d) and their grouping in Theorem 1.1
> so that all but (o(p/\sqrt m)) of the resulting proportional bundles
> are simultaneously realizable as tight interval rows.

Because the Boolean chains in Theorem 1.1 are globally disjoint, any such
realizing rows would automatically be a physical atom matching of the
required size.  Conversely, neither (1.4) nor (2.7) controls this common
bundle realization: (1.4) sees individual adjacent inclusions, and (2.7)
sees repeated intersections of two already physical atoms.  What is absent
is a Hall theorem whose right-hand objects are whole (b)-column tight
rows and whose left-hand objects retain the common chain ownership across
all depths.

Thus the positive boundary is exact.  Proportional floors have no common-
flow obstruction, the local collar has an integral (1-O(1/m)) Hall fan,
and every nonadjacent overlap has normalized mass (O(m^{-2})).  The sole
unproved step is the common physical lift of those integral chains into
long tight rows.
