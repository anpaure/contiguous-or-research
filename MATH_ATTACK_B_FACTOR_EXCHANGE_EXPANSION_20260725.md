# Mathematical attack B: expansion of the exact-factor exchange graph

## Small-trade cubes, parity separators, orbit bottlenecks, and relative Graver expansion

### 25 July 2026

## 0. Verdict

This route does **not** prove fixed-window overload MWB, labelled
synchronization, or the contiguous-OR conjecture. It gives a sharp
positive/negative separation.

1. For the full mobile-quota lifted-Graver exchange graph, every exact factor
   \(F\) admits pairwise middle-root-disjoint applicable improving trades
   whose certified gains sum to the complete relative overload gap
   \(J_A(F)-J_A^\star\). Thus genuine local expansion is available when
   arbitrary lifted-Graver packets are allowed.

2. Truncating to the explicit small trades loses this theorem. The canonical
   MSW factor contains an isometric exchange cube of dimension
   \[
      \operatorname{Cat}_{m-2}
      =\left(\frac1{16}+o(1)\right)\operatorname{Cat}_m.
   \]
   It has the usual hypercube edge-isoperimetry and every vertex has
   that many support-disjoint legal switches. Nevertheless, on every fixed
   Gaussian window its entire overload diameter is \(o(W)\). Raw exchange
   expansion and availability therefore do not imply useful overload
   direction.

3. For even \(m\), every explicit rooted profile-\(3\) alternating
   \(C_8\) two-for-two switch preserves the exact number of odd cyclic
   orders. The small-trade graph has at least
   \[
      \operatorname{Cat}_{m-3}+1
      =\left(\frac1{64}+o(1)\right)\operatorname{Cat}_m
   \]
   connected components. This is a genuine signed-lattice separator for
   the explicit atlas, not merely a long-distance statement.

4. The medium transposition-component graph has a different exact
   bottleneck. From every factor \(F\), asymptotically at least one third of
   all transpositions \(\tau\) preserve an orbit-profile floor at least
   \((1/4-o(1))J_A(F)\). Minimizing within that entire recomputed
   \(\tau\)-switch component produces a local minimum still carrying that
   fixed fraction of the starting overload. This does not give one factor
   locally minimal for all transpositions.

5. The scale-correct remaining statement is a **weighted improving-matching
   theorem** for a medium trade atlas. Ordinary graph conductance controls
   only the distribution of overload around the component median; it gives
   no low-energy anchor and no pointwise improving neighbor.

Everything below concerns the unlabelled fixed-window overload objective.
No conversion to a common nested labelled owner flow is asserted.

The only imported ingredients are previously proved and audited exact
factor facts: (i) switching arbitrary interaction components between
\(F\) and \(\tau F\) preserves exact ownership; (ii) the canonical MSW
overlay has independent strata of side sizes
\(\operatorname{Cat}_j+\operatorname{Cat}_{j+1}\), including
\(\operatorname{Cat}_{m-2}\) size-two components and
\(\operatorname{Cat}_{m-3}\) size-three components; (iii) an aligned
size-two switch has the actions in (2.1), while the general rooted
profile-\(3\) switch has the seam bounds in (2.3); and (iv) fixed-window
overload MWB implies the coefficient-one contiguous-OR bound by the audited
slow diagonal with \(H=o(m^{2/3})\). No unproved trade classification or
expansion assertion is used below.

## 1. Exact factor graph and overload metric

Put

\[
 n=2m+1,\qquad
 W=\binom nm,\qquad
 B=\frac Wn=\operatorname{Cat}_m.
\tag{1.1}
\]

Let \(\mathfrak F_m\) be the set of exact wreath factors. For
\(1\le q\le H_A:=\lceil A\sqrt m\rceil\), put

\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor.
\tag{1.2}
\]

Throughout, \(A>0\) is fixed and \(m\) is sufficiently large that
\(H_A\le m-2\). All fixed-window asymptotics and all uses of the exact
small-trade actions are understood in this range.

If \(\mu_q^F\) is the rank-\((m-q)\) wreath-shadow load of \(F\), let
\(O_q(F)\) be its minimum overload above a floor/ceiling-balanced quota
vector. Define

\[
 J_A(F):=\sum_{q=1}^{H_A}\frac{O_q(F)}{c_q},
\qquad
 J_A^\star:=\min_{F\in\mathfrak F_m}J_A(F).
\tag{1.3}
\]

For later use write

\[
 S_A(m):=\sum_{q=1}^{H_A}\frac1{c_q},
\qquad
 T_A(m):=\sum_{q=1}^{H_A}\frac q{c_q}.
\tag{1.4}
\]

The fixed-window estimates are

\[
 S_A(m)=(\kappa_A+o(1))\sqrt m,\qquad
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor},
\tag{1.5}
\]

and

\[
 T_A(m)=(\lambda_A+o(1))m,\qquad
 \lambda_A=\int_0^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}.
\tag{1.6}
\]

These follow from
\(\log(W/N_q)=q^2/m+O_A(m^{-1/2})\) by ordinary Riemann sums.

A reduced support-feasible trade is

\[
 z=\mathbf1_P-\mathbf1_N\in\ker_{\mathbb Z}A_m,
\qquad |P|=|N|=:k,
\tag{1.7}
\]

where each sign is a middle-wreath packing. It is applicable at \(F\) when
\(N\subseteq F\). Its degree is \(k\). An exchange graph is obtained by
choosing a symmetric library of such trades and joining every applicable
pair of exact factors.

### Lemma 1.1 (exact half-\(\ell_1\) overload modulus)

Let \(\mathcal B_q\) be the set of rank-\((m-q)\) vectors having exactly
\(r_q\) entries \(c_q+1\) and all other entries \(c_q\), where
\(W=c_qN_q+r_q\). Then

\[
 \boxed{
 O_q(\mu)
 =\frac12\min_{b\in\mathcal B_q}\|\mu-b\|_1.}
\tag{1.8}
\]

Consequently,

\[
 \boxed{
 |O_q(\mu)-O_q(\nu)|
 \le\frac12\|\mu-\nu\|_1.}
\tag{1.9}
\]

#### Proof

For fixed \(b\), the vectors \(\mu,b\) have the same total \(W\), so the
positive and negative parts of \(\mu-b\) have equal \(\ell_1\)-mass. The
minimum positive mass is precisely the minimum floor/ceiling overload,
which gives (1.8). Distance to a fixed set in the metric
\(\frac12\|\cdot\|_1\) is one-Lipschitz, proving (1.9). \(\square\)

For a trade \(z\), define its depth action and fixed-window footprint by

\[
 a_q(z):=\frac12\|A_{m-q}z\|_1,\qquad
 \ell_A(z):=\sum_{q=1}^{H_A}\frac{a_q(z)}{c_q}.
\tag{1.10}
\]

### Corollary 1.2 (one-edge modulus)

For every applicable trade,

\[
 \boxed{|J_A(F+z)-J_A(F)|\le\ell_A(z).}
\tag{1.11}
\]

If \(z\) has degree \(k\), then

\[
 a_q(z)\le nk,\qquad
 \boxed{\ell_A(z)\le nkS_A(m).}
\tag{1.12}
\]

#### Proof

Equation (1.11) is (1.9), weighted and summed. Each sign of a degree-\(k\)
trade contains \(nk\) rank-\((m-q)\) cyclic occurrences, so
\(\|A_{m-q}z\|_1\le2nk\). \(\square\)

The factor in (1.12) is \(nk\), not \(2nk\).

## 2. Three trade scales and exact speed limits

The known two-for-two trades occur at two different geometric scales and
must not be conflated.

### 2.1 Aligned common-tail four-letter edges

For the audited aligned MSW four-letter trade, the exact depth action has
four unit cells at depth one and eight unit cells at every
\(2\le q\le H_A\). Hence

\[
 a_1=2,\qquad a_q=4\quad(2\le q\le H_A),
\tag{2.1}
\]

and

\[
 \boxed{
 L_A^{\rm tail}:=\ell_A(z)=4S_A(m)-2
 =(4\kappa_A+o(1))\sqrt m.}
\tag{2.2}
\]

### 2.2 General rooted profile-\(3\) \(C_8\) switches

For an arbitrary rooted profile-\(3\) partner, the exact seam
removal/addition bounds are

\[
 s^{\rm prof}_1=8,\qquad
 s^{\rm prof}_q=4q+6\quad(q\ge2).
\tag{2.3}
\]

They are upper bounds for the half-\(\ell_1\) action, and give

\[
\boxed{
 L_A^{\rm prof}:=
 \frac8{c_1}+\sum_{q=2}^{H_A}\frac{4q+6}{c_q}
 =4T_A(m)+6S_A(m)-2
 =(4\lambda_A+o(1))m.}
\tag{2.4}
\]

The displayed equality uses \(c_1=1\), valid for \(m\ge3\), which is the
asymptotic range considered here.
The sharper \(\Theta(\sqrt m)\) bound (2.2) applies only to the aligned
common-tail subfamily.

### Theorem 2.1 (sequential speed limits)

Suppose a path \(F_0,\ldots,F_R\) lowers \(J_A\) by \(\Delta>0\).
Then:

\[
 R\ge\frac{\Delta}{nDS_A(m)}
\tag{2.5}
\]

if all moves have degree at most \(D\);

\[
 R\ge\frac{\Delta}{L_A^{\rm prof}}
\tag{2.6}
\]

for general rooted profile-\(3\) switches; and

\[
 R\ge\frac{\Delta}{L_A^{\rm tail}}
\tag{2.7}
\]

for aligned common-tail edges.

If \(\Delta\ge\varepsilon W\), these become respectively

\[
 R\ge
 \left(\frac{\varepsilon}{\kappa_A}+o(1)\right)
 \frac{B}{D\sqrt m},
\tag{2.8}
\]

\[
 R\ge
 \left(\frac{\varepsilon}{2\lambda_A}+o(1)\right)B,
\tag{2.9}
\]

and

\[
 \boxed{
 R\ge
 \left(\frac{\varepsilon}{2\kappa_A}+o(1)\right)B\sqrt m.}
\tag{2.10}
\]

#### Proof

Telescope (1.11), using (1.12), (2.2), or (2.4). Substitute
\(W=nB\), \(n=(2+o(1))m\), and (1.5)--(1.6). \(\square\)

Call trades at one factor **root-disjoint** if their negative middle-root
packets are disjoint. Since \(F\) is exact, disjoint negative wreath
supports already give disjoint root packets; equality of the two sides of
each trade makes the union of a root-disjoint family jointly support
feasible.

### Theorem 2.2 (parallel common-tail obstruction)

A root-disjoint round contains at most \(B/2\) aligned two-for-two trades and
has total possible fixed-window displacement at most

\[
 \boxed{
 \frac B2(4S_A-2)
 =(2S_A-1)B
 =O_A(H_AB)
 =O_A(W/\sqrt m)
 =o(W).}
\tag{2.11}
\]

Thus an \(\varepsilon W\) repair by recomputed root-disjoint common-tail
rounds requires at least

\[
 \boxed{
 \left(\frac{\varepsilon}{\kappa_A}+o(1)\right)\sqrt m}
\tag{2.12}
\]

rounds.

#### Proof

Every trade consumes two old wreaths, giving the \(B/2\) packing ceiling.
The change produced by a simultaneous union is at most the sum of the
half-\(\ell_1\) footprints, irrespective of whether the individual overload
gains add. Divide \(\varepsilon W\) by (2.11). \(\square\)

More generally, if every degree-\(d\) move in a library satisfies
\(a_q(z)\le Kd\) throughout the window, then one negative-support-disjoint
round has displacement at most \(KBS_A\). Thus \(K=o(\sqrt m)\) rules out
linear one-round progress.

## 3. The explicit small graph: expansion without movement

Let \(\mathcal X_2(m)\) be the exact-factor graph whose edges are all rooted
profile-\(3\) alternating \(C_8\) two-for-two switches. The aligned
four-letter edges form a distinguished subgraph. Let \(L_{\rm prof}\) be
the integer span of the oriented edge vectors of \(\mathcal X_2(m)\).

### Theorem 3.1 (large isometric MSW cube)

The canonical MSW factor has

\[
 t_0=\operatorname{Cat}_{m-2}
 =\left(\frac1{16}+o(1)\right)B
\tag{3.1}
\]

pairwise independent size-two components for one distinguished
transposition. Switching arbitrary subsets gives an isometric hypercube
\(Q_{t_0}\) inside \(\mathcal X_2(m)\).

If two cube vertices differ in \(h\) coordinates, their exchange distance is
exactly \(h\). Every cube vertex has \(t_0\) incident root-disjoint aligned
four-letter trades.

#### Proof

The imported MSW component hierarchy gives the \(t_0\) independent
size-two components, and component-side choices are exact factors. Toggling
the \(h\) differing components gives a path of length \(h\).

The endpoint factors differ in exactly \(2h\) old wreaths. A degree-two move
can remove at most two of them, so every path has length at least \(h\).
Thus the displayed cube is isometric. \(\square\)

The asymptotic in (3.1) follows from the exact ratio

\[
 \frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}
 \longrightarrow\frac1{16}.
\]

For every nonempty \(U\subseteq Q_t\), its internal cube boundary satisfies

\[
 \boxed{
 |\partial_{Q_t}U|
 \ge |U|\bigl(t-\log_2|U|\bigr).}
\tag{3.2}
\]

Indeed, induction on \(t\) gives
\(e(U)\le |U|\log_2|U|/2\), and
\(|\partial U|=t|U|-2e(U)\).

### Corollary 3.2 (overload-flat expander chart)

For every fixed \(A\),

\[
 \boxed{
 \operatorname{diam}_{J_A}(Q_{t_0})
 \le t_0(4S_A-2)
 =O_A(B\sqrt m)
 =O_A(W/\sqrt m)
 =o(W).}
\tag{3.3}
\]

Here
\(\operatorname{diam}_{J_A}(Q)=\max_{F,G\in Q}|J_A(F)-J_A(G)|\).
Thus an exponentially large exact-factor chart with strong raw
edge-isoperimetry,
with a positive-density root-disjoint trade family at every vertex, is
asymptotically flat at the linear fixed-window overload scale.

#### Proof

Join any two cube vertices by at most \(t_0\) aligned edges and use (2.2).
Equations (1.1), (1.5), and (3.1) give the last estimates. \(\square\)

Corollary 3.2 is the first exact bottleneck: unsigned availability and
hypercube expansion do not supply overload direction.

## 4. An exact parity separator for the profile-\(3\) graph

Assume throughout this section that \(m\) is even.

For a cyclic order \(C\), define \(\epsilon(C)\in\{\pm1\}\) to be the
permutation sign of any linear readout. This is well-defined on an
unoriented cyclic order. A rotation of length \(n=2m+1\) is even, and
reversing after one label is fixed reverses \(2m\) entries, with sign

\[
 (-1)^{\binom{2m}{2}}=(-1)^m=1.
\tag{4.1}
\]

Put

\[
N_-(F):=|\{C\in F:\epsilon(C)=-1\}|.
\tag{4.2}
\]

### Lemma 4.0 (rooted profile-\(3\) normal form)

Up to a common relabelling, reversal, and cyclic choice of origins, every
rooted profile-\(3\) alternating-\(C_8\) trade has old omitted-label words

\[
 e=(a,c,b,d,P),\qquad f=(c,d,a,b,Q),
\tag{4.2a}
\]

and new words

\[
 g=(c,b,a,\operatorname{rev}Q,d),\qquad
 h=(d,a,c,P,b),
\tag{4.2b}
\]

where \(a,b,c,d\) are distinct and \(P,Q\) are orderings of
\([n]\setminus\{a,b,c,d\}\), a set of size \(L=n-4\).

#### Proof

First derive the universal eight-cycle word. Write its odd-graph vertices
as \(V_0,\ldots,V_7\), and let \(\lambda_i\) be the unique coordinate
omitted by the edge \(V_iV_{i+1}\). The odd-graph recurrence is

\[
 V_{i+2}=(V_i\cup\{\lambda_i\})\setminus\{\lambda_{i+1}\}.
\]

For each coordinate \(x\), the number of occurrences of \(x\) among the
eight \(\lambda_i\)'s is even: membership of \(x\) toggles across every
edge not labelled \(x\) and is zero at both ends of an edge labelled
\(x\). Consecutive labels are distinct by the recurrence and simplicity.
Between consecutive cyclic occurrences of one label, the gap is odd and at
least three, because membership must return to zero at the next such edge.
Four occurrences would therefore require four gaps of total at least
twelve. Hence every used label occurs exactly twice, the two cyclic gaps
being three and five. Pairing positions at distance three in
\(\mathbb Z/8\mathbb Z\) has, up to a dihedral change of origin, the unique
pattern

\[
 a,b,c,a,d,c,b,d.
\]

Cutting the two old cycles at their two pairs of edges on this alternating
cycle isolates a three-vertex path (two retained internal edges) from each.
Choose the root at the first cut
of the first old cycle and orient its retained long arc forward. The four
active labels are then read as \(a,c,b,d\). The complementary incidences of
the displayed eight-cycle force the second old active block to be
\(c,d,a,b\); all other labels lie on the two retained long arcs and give
the words \(P,Q\). The alternating reconnection has only the crosswise
endpoint pairing. Reading its two cycles from the inherited orientations
gives respectively
\((d,a,c,P,b)\) and \((c,b,a,\operatorname{rev}Q,d)\); the reversal of
\(Q\) occurs because that retained arc is traversed from its opposite end.
These are (4.2b). Conversely, cutting (4.2a) at the four displayed active
seams and reconnecting crosswise recovers the same eight edge labels, so
the list is exhaustive. \(\square\)

### Theorem 4.1 (profile-\(3\) parity-census invariance)

Every rooted profile-\(3\) \(C_8\) switch preserves the multiset of the two
cyclic-order signs on its old and new sides. Consequently,

\[
 \boxed{N_-(F')=N_-(F)}
\tag{4.3}
\]

on every edge of \(\mathcal X_2(m)\), and on every support-feasible signed
composite of these edge vectors.

#### Proof

Use Lemma 4.0. The two old omitted-label words are

\[
 e=(a,c,b,d,P),\qquad f=(c,d,a,b,Q),
\tag{4.4}
\]

where \(P,Q\) order the same \(L=n-4=2m-3\) remaining labels. Following
the universal alternating \(C_8\) through the two re-sewn cycles gives,
up to cyclic rotation and reversal,

\[
 g=(c,b,a,\operatorname{rev}Q,d),\qquad
 h=(d,a,c,P,b).
\tag{4.5}
\]

Relative to \(e\), the position word of \(h\) is

\[
 (4,1,2,5,\ldots,n,3),
\]

with \(3+L=2m\) inversions. Hence \(\epsilon(h)=\epsilon(e)\).
Relative to \(f\), the position word of \(g\) is

\[
 (1,4,3,n,n-1,\ldots,5,2),
\]

with

\[
 3+L+\binom L2
 =2m+(2m-3)(m-2)
\tag{4.6}
\]

inversions. This is even when \(m\) is even, so
\(\epsilon(g)=\epsilon(f)\). Common relabelling multiplies all four signs
by the same factor and does not change the conclusion.
The omitted-label and ordinary cyclic readouts differ by one fixed
positional permutation, whose common sign factor also cancels.

Thus the linear functional \(N_-\) annihilates every oriented profile edge,
and hence its full integer span. \(\square\)

### Theorem 4.2 (linearly many disconnected census classes)

For every even \(m\ge4\), the graph \(\mathcal X_2(m)\) has at least

\[
 \boxed{\operatorname{Cat}_{m-3}+1}
\tag{4.7}
\]

connected components. Moreover, the rational span of its edge lattice is
proper:

\[
 \boxed{
 \operatorname{span}_{\mathbb Q}L_{\rm prof}
 \subsetneq\ker_{\mathbb Q}A_m.}
\tag{4.7a}
\]

#### Proof

For the audited MSW overlay under \(\tau=(2\,3)\), the \(j=1\) stratum has

\[
 t_1=\operatorname{Cat}_{m-3}
\tag{4.8}
\]

independent components, each of side size
\(\operatorname{Cat}_1+\operatorname{Cat}_2=3\).

The transposition \(\tau\) reverses \(\epsilon\) on every wreath. If one
side of a component has \(a\) odd wreaths, its other side has \(3-a\);
switching changes \(N_-\) by

\[
 3-2a\in\{-3,-1,1,3\},
\tag{4.9}
\]

never zero. Choose independently in every such component the side having
fewer odd wreaths. Toggle the \(t_1\) components one at a time toward the
side having more. The resulting \(t_1+1\) exact factors have strictly
increasing \(N_-\), so Theorem 4.1 places them in distinct components.

The vector of any one size-three component lies in \(\ker A_m\) but has
nonzero \(N_-\)-change. It is therefore outside even the rational span of
the profile edges. \(\square\)

The exact density is

\[
 \frac{\operatorname{Cat}_{m-3}}{\operatorname{Cat}_m}
 =
 \frac{m(m-1)(m+1)}
 {8(2m-1)(2m-3)(2m-5)}
 \longrightarrow\frac1{64}.
\tag{4.10}
\]

The parity separator is real but is not itself an overload obstruction.

### Corollary 4.3 (equal-overload disconnected factors)

There are exact factors \(H,H'\) in different components of
\(\mathcal X_2(m)\) such that

\[
 \boxed{J_A(H)=J_A(H')}
\tag{4.11}
\]

simultaneously for every \(A\); indeed every coordinate-invariant rank
histogram objective agrees.

#### Proof

The endpoints of a size-three component have different \(N_-\), so at
least one endpoint \(H\) has \(N_-(H)\ne B/2\). Let \(\sigma\) be any
coordinate transposition and put \(H'=\sigma H\). Relabelling preserves
every unlabelled overload, while it flips every cyclic-order sign:

\[
 N_-(H')=B-N_-(H)\ne N_-(H).
\]

Apply Theorem 4.1. \(\square\)

For every realized census \(e\), define the slice minimum

\[
 \omega_{A,e}:=
 \min\{J_A(F):N_-(F)=e\}.
\tag{4.12}
\]

Every slice minimum is a profile-trade local minimum, and odd coordinate
relabelling gives

\[
 \omega_{A,e}=\omega_{A,B-e}.
\tag{4.13}
\]

Therefore a theorem saying that every \(J_A\)-large factor has even one
improving profile edge would force

\[
 \max_{e\ {\rm realized}}\omega_{A,e}=o(W),
\tag{4.14}
\]

whereas fixed-window MWB asks only
\(\min_e\omega_{A,e}=o(W)\). The desired pointwise expansion is thus a
classwise strengthening of MWB, not a consequence of signed lattice
generation.

## 5. Positive result: root-disjoint relative Graver expansion

The full lifted-Graver graph does satisfy an exact improving-trade theorem.
It is relative to the unknown global minimum \(J_A^\star\).

For each depth write \(W=c_qN_q+r_q\). Introduce nonnegative integral
variables

\[
 h_q+s_q=\mathbf1,\qquad
 \mathbf1^\top h_q=r_q,
\tag{5.1}
\]

and

\[
 A_{m-q}x-h_q-p_q+d_q=c_q\mathbf1.
\tag{5.2}
\]

For fixed factor \(x\), minimizing

\[
 \mathcal J(x,h,s,p,d)
 :=\sum_{q\le H_A}\frac{\mathbf1^\top p_q}{c_q}
\tag{5.3}
\]

over the auxiliary variables gives exactly \(J_A(x)\). The variable
\(h_q\) chooses the \(r_q\) high quotas, and (1.8) proves the equality.

### Theorem 5.1 (exact root-disjoint Graver expansion)

For every exact factor \(F\), there is a family of pairwise
middle-root-disjoint applicable exact trades \(z_i\), with positive numbers
\(g_i\), such that

\[
 J_A(F+z_i)\le J_A(F)-g_i,
\tag{5.4}
\]

\[
 \boxed{\sum_i g_i=J_A(F)-J_A^\star,}
\tag{5.5}
\]

and, writing \(k_i=\deg z_i\),

\[
 g_i\le nk_iS_A.
\tag{5.6}
\]

Consequently,

\[
 \boxed{
 \sum_i k_i
 \ge\frac{J_A(F)-J_A^\star}{nS_A}.}
\tag{5.7}
\]

#### Proof

Choose auxiliary-optimal extended vectors \(u,u^\star\) over \(F\) and a
global optimizer. Conformally decompose

\[
 u^\star-u=\sum_i G_i
\tag{5.8}
\]

into Graver elements of the complete equality matrix consisting of the
middle equations and (5.1)--(5.2). Let \(\gamma_i\) be the linear objective
change of \(G_i\).

Conformality makes \(u^\star-G_i\) feasible. If \(\gamma_i>0\), it would
have objective below the global optimum, so \(\gamma_i\le0\). If the factor
projection of \(G_i\) is zero, then \(u+G_i\) is feasible over the same
factor; optimality of the current auxiliaries gives \(\gamma_i\ge0\), hence
\(\gamma_i=0\).

Discard also the factor-changing summands with \(\gamma_i=0\); they carry
no objective gap. Every remaining factor projection \(z_i\) is squarefree, lies in
\(\ker A_m\), and is applicable at \(F\). After reoptimizing the auxiliary
variables at \(F+z_i\),

\[
 J_A(F+z_i)\le J_A(F)+\gamma_i.
\]

Take \(g_i=-\gamma_i>0\). Their sum is the endpoint objective gap.

The negative factor supports of different conformal summands are disjoint
subsets of \(F\). Since \(F\) is exact, their middle-root packets are
disjoint; each positive packet equals its negative packet. This proves the
root-disjoint assertion. Finally (1.12) bounds each actual improvement and
hence each certified \(g_i\), proving (5.6)--(5.7). \(\square\)

Define the weighted root-disjoint improving degree of a trade atlas
\(\mathscr T\) by

\[
 \operatorname{wd}_{\mathscr T}(F)
 :=
 \max_{\mathcal M}
 \sum_{z\in\mathcal M}
 \bigl(J_A(F)-J_A(F+z)\bigr)_+,
\tag{5.9}
\]

where \(\mathcal M\) ranges over root-disjoint applicable trades. Theorem
5.1 says

\[
 \boxed{
 \operatorname{wd}_{\rm Gr}(F)
 \ge J_A(F)-J_A^\star.}
\tag{5.10}
\]

The trades in Theorem 5.1 can be jointly applied as an exact factor move,
but their individual lower-shadow overload gains need not add under joint
application. Equation (5.10) concerns the individual gains from the common
starting factor.

### Corollary 5.2 (small-versus-macrotrade dichotomy)

Suppose

\[
 J_A(F)-J_A^\star\ge\varepsilon W.
\tag{5.11}
\]

Then

\[
 \sum_i k_i
 \ge
 \left(\frac{\varepsilon}{\kappa_A}+o(1)\right)
 \frac B{\sqrt m}.
\tag{5.12}
\]

For any \(D\) and \(0<\theta<1\), either:

1. trades of degree at most \(D\) carry at least a \(\theta\)-fraction of
   the gap, in which case there are at least
   \[
   \boxed{
   \left(\frac{\theta\varepsilon}{\kappa_A}+o(1)\right)
   \frac B{D\sqrt m}}
   \tag{5.13}
   \]
   root-disjoint improving trades; or

2. degree-\(>D\) cancellation packets carry the remaining fraction and use
   total old support at least
   \[
   \boxed{
   \left(\frac{(1-\theta)\varepsilon}{\kappa_A}+o(1)\right)
   \frac B{\sqrt m}.}
   \tag{5.14}
   \]

#### Proof

Apply (5.6) separately to the two classes and use
\(W=nB\), (1.5). \(\square\)

This proves every factor far from the **global optimum** has many
root-disjoint improving trades unless its gain is concentrated in large
packets. Replacing the relative hypothesis by \(J_A(F)\ge\varepsilon W\)
requires \(J_A^\star=o(W)\), which is exactly the unresolved fixed-window
MWB theorem.

### Corollary 5.3 (what an explicit profile refinement would give)

Suppose a conformal decomposition as in (5.8) has general rooted
profile-\(3\) projections carrying a \(\theta\)-fraction of the objective
gap. Under (5.11), it contains at least

\[
 \boxed{
 \left(\frac{\theta\varepsilon}{2\lambda_A}+o(1)\right)B}
\tag{5.15}
\]

pairwise root-disjoint improving profile-\(3\) trades.

#### Proof

Every such trade has certified gain at most (2.4). Divide
\(\theta\varepsilon W\) by \(L_A^{\rm prof}\) and use \(W=(2+o(1))mB\).
\(\square\)

No such auxiliary-conformal refinement into the explicit atlas is known.
Ordinary Markov connectivity and abelianized signed generation do not
control applicability or the signs of the auxiliary quota moves.

## 6. A medium-trade orbit bottleneck for many transpositions

Fix a coordinate transposition \(\tau\). Its action partitions the
rank-\((m-q)\) targets into singleton and two-point orbits. Let
\(\Omega_{q,\tau}(F)\) be the minimum overload among all nonnegative integer
load vectors having the same total as \(\mu_q^F\) on every such orbit. Put

\[
 \Omega_{A,\tau}(F)
 :=\sum_{q=1}^{H_A}\frac{\Omega_{q,\tau}(F)}{c_q}.
\tag{6.1}
\]

Every exact component switch between a factor and its \(\tau\)-image has
load change \((\tau-I)a\). Therefore every dynamically recomputed sequence
using only \(\tau\)-component moves preserves every orbit total and obeys

\[
                         J_A\ge\Omega_{A,\tau}(F).
\tag{6.2}
\]

### Theorem 6.1 (averaged transposition-orbit floor)

For a uniformly random coordinate transposition,

\[
 \boxed{
 \mathbb E_\tau\Omega_{q,\tau}(F)
 \ge \pi_qO_q(F),}
\tag{6.3}
\]

where

\[
\begin{aligned}
 \pi_q
 &=
 \frac{\binom{m-q}{2}+\binom{m+q+1}{2}}{\binom n2}\\
 &=\frac{m^2+q(q+1)}{m(2m+1)}.
\end{aligned}
\tag{6.4}
\]

Consequently, with

\[
 \pi_*:=\pi_1
 =\frac{m^2+2}{m(2m+1)}
 =\frac12+o(1),
\tag{6.5}
\]

\[
 \boxed{
 \mathbb E_\tau\Omega_{A,\tau}(F)
 \ge \pi_*J_A(F).}
\tag{6.6}
\]

#### Proof

Write

\[
 D_q^-=\sum_S(c_q-\mu_q(S))_+,\qquad
 D_q^+=\sum_S(\mu_q(S)-c_q-1)_+,
\tag{6.7}
\]

so \(O_q=\max(D_q^-,D_q^+)\).

A target \(S\) is fixed by \(\tau\) precisely when the two transposed
coordinates are both in \(S\) or both outside it. The proportion of
transpositions fixing a fixed rank-\((m-q)\) target is (6.4).

On a fixed singleton orbit, redistribution is impossible. Let
\(D_{q,\tau}^\pm\) denote the two sums in (6.7) restricted to fixed
targets. Then

\[
 \Omega_{q,\tau}\ge
 \max(D_{q,\tau}^-,D_{q,\tau}^+).
\tag{6.8}
\]

Averaging gives

\[
 \mathbb E_\tau D_{q,\tau}^\pm=\pi_qD_q^\pm.
\]

Since the maximum is convex,

\[
\begin{aligned}
 \mathbb E_\tau\Omega_{q,\tau}
 &\ge
 \max(\mathbb ED_{q,\tau}^-,
      \mathbb ED_{q,\tau}^+)\\
 &=\pi_qO_q.
\end{aligned}
\]

Sum with weights \(1/c_q\), observing that \(\pi_q\ge\pi_1\). \(\square\)

The same proof applies to the full nonnegative scalar floor energy: every
fixed singleton retains its complete scalar contribution.

### Corollary 6.2 (positive-density family of high directional traps)

For every \(0\le\alpha<\pi_*\),

\[
 \boxed{
 \frac{|\{\tau:\Omega_{A,\tau}(F)\ge\alpha J_A(F)\}|}
      {\binom n2}
 \ge
 \frac{\pi_*-\alpha}{1-\alpha}.}
\tag{6.9}
\]

In particular, taking \(\alpha=\pi_*/2\), the right side is
\(\pi_*/(2-\pi_*)\to1/3\), while \(\alpha\to1/4\).

For every such \(\tau\), choose a \(J_A\)-minimizer \(F_\tau^\star\) in
the finite exchange component generated from \(F\) by all recomputed
\(\tau\)-component moves. Then

\[
 \boxed{
 J_A(F_\tau^\star)
 \ge\alpha J_A(F),}
\tag{6.10}
\]

and \(F_\tau^\star\) has no improving \(\tau\)-component trade of any size.

#### Proof

If \(J_A(F)=0\), every transposition satisfies the displayed threshold and
the claim is immediate. Otherwise, the random variable
\(X_\tau=\Omega_{A,\tau}(F)/J_A(F)\) lies in \([0,1]\) and has mean at
least \(\pi_*\). If \(r=\Pr(X_\tau\ge\alpha)\), then
\(\mathbb EX_\tau\le r+(1-r)\alpha\), giving (6.9).

Every vertex in the \(\tau\)-component obeys (6.2). A minimizer exists
because the state space is finite, and by definition has no improving
allowed edge. \(\square\)

Thus, conditional only on starting with a linearly overloaded factor, a
positive fraction of transposition directions contain exact linearly
overloaded local minima. This is an actual medium-trade bottleneck. It does
not construct a high factor, and changing to a different transposition can
release the orbit floor.

## 7. Metric separators and what ordinary expansion proves

Two elementary separator theorems explain why connectivity and conductance
do not replace signed descent.

### Proposition 7.1 (overload shells)

Let \(\mathcal X\) be an exchange graph on which every edge satisfies
\(|\Delta J_A|\le L\). For \(t\in\mathbb R\), put

\[
 \mathcal H_t=\{F:J_A(F)>t\}.
\]

Every edge leaving \(\mathcal H_t\) is improving in the outward direction,
but its high endpoint lies in the shell

\[
                       t<J_A\le t+L.
\tag{7.1}
\]

If two vertices have objective difference \(\Delta\), every path between
them meets at least

\[
 \left\lfloor\frac{\Delta}{2L}\right\rfloor
\tag{7.2}
\]

pairwise disjoint \(L\)-thick objective shells.

#### Proof

An \(L\)-Lipschitz edge cannot jump over (7.1). Choose thresholds separated
by \(2L\) between the endpoint objective values. Their shells are disjoint
and every path crosses each threshold. \(\square\)

For a linear gap, (7.2) gives \(\Omega_A(B)\) shells for general profile
edges and \(\Omega_A(B\sqrt m)\) shells for aligned common-tail edges.

### Proposition 7.2 (neutral overlap magnetization)

Fix an exact factor \(F_0\) and a coordinate transposition \(\tau\). For
\(m\ge2\),

\[
 F_0\cap\tau F_0=\varnothing.
\tag{7.3}
\]

Define

\[
 M_{F_0}(G)
 :=|G\cap F_0|-|G\cap\tau F_0|.
\tag{7.4}
\]

A degree-\(D\) edge changes \(M_{F_0}\) by at most \(2D\), while

\[
 M_{F_0}(F_0)=B,\qquad
 M_{F_0}(\tau F_0)=-B.
\tag{7.5}
\]

Thus every bounded-degree path from \(F_0\) to \(\tau F_0\), if one exists,
has length at least \(B/D\) and crosses a chain of
\(\Omega(B/D)\) disjoint magnetization shells. Yet

\[
                         J_A(F_0)=J_A(\tau F_0)
\tag{7.6}
\]

exactly.

#### Proof

Every cyclic order shares a middle interval with its transposed image. If
the two transposed coordinates occur at cyclic distance \(d\), there are
middle windows containing both or neither; equivalently, their total
incidence \(2m=n-1\) cannot equal one in every one of the \(n\) windows.
Thus two such wreaths cannot coexist in an exact factor. A transposition
also cannot stabilize an unoriented odd cyclic order: its cycle type is
neither a nontrivial rotation nor a reflection of type \(1\,2^m\). This
proves (7.3).

A degree-\(D\) trade has \(D\) positive and \(D\) negative wreaths, while
the coefficient vector
\(\mathbf1_{F_0}-\mathbf1_{\tau F_0}\) takes values in
\(\{-1,0,1\}\). Hence the change in (7.4) is at most \(2D\). Equations
(7.5) give the distance bound. Equation (7.6) is coordinate-relabel
invariance. \(\square\)

Large exchange distance can therefore be completely overload-neutral.

### Theorem 7.3 (conductance gives concentration, not an anchor)

Let \(\mathcal X\) be one finite connected \(d\)-regular exchange
multigraph component, with \(d>0\), whose conductance is \(\phi>0\), where

\[
 \phi=\min_{0<|U|\le|V|/2}\frac{|\partial U|}{d|U|},
\tag{7.7}
\]

and suppose \(|J_A(x)-J_A(y)|\le L\) on every edge. If \(M\) is a median
of \(J_A\) under the uniform measure, then

\[
 \boxed{
 \frac1{|V|}\sum_{x\in V}|J_A(x)-M|
 \le\frac{L}{2\phi}.}
\tag{7.8}
\]

Moreover, for \(t\ge M\),

\[
 |\{J_A>t+L\}|
 \le(1-\phi)|\{J_A>t\}|.
\tag{7.9}
\]

#### Proof

Put \(U_t=\{J_A>t\}\). For \(t\ge M\), the median property gives
\(|U_t|\le|V|/2\). Every boundary edge of \(U_t\) has its high endpoint in
\(U_t\setminus U_{t+L}\), and every such vertex has degree \(d\). Therefore

\[
 \phi d|U_t|
 \le |\partial U_t|
 \le d|U_t\setminus U_{t+L}|.
\]

Rearrangement gives (7.9).

The coarea identity is

\[
 \sum_{\{x,y\}\in E}|J_A(x)-J_A(y)|
 =\int_{\mathbb R}|\partial\{J_A>t\}|\,dt.
\tag{7.10}
\]

Applying conductance above and below a median gives

\[
 \int|\partial\{J_A>t\}|\,dt
 \ge\phi d\sum_x|J_A(x)-M|.
\tag{7.11}
\]

Indeed, the layer-cake identity at a median is

\[
 \int_{\mathbb R}
 \min\bigl(|U_t|,|V\setminus U_t|\bigr)\,dt
 =\sum_{x\in V}|J_A(x)-M|.
\]

The left side is at most \(L|E|=Ld|V|/2\), proving (7.8). \(\square\)

Thus strong common-tail expansion would concentrate overload in a band of
width \(O_A(\sqrt m/\phi)\), and general profile expansion in a band of
width \(O_A(m/\phi)\), around the component median. It says nothing about
the absolute height of that median or the component minimum. Adding a
constant to the objective preserves all expansion and Lipschitz data.

Nor does state-graph expansion imply many root-disjoint moves at every
vertex. If the improving degree-\(\le D\) moves at \(F\) form a hypergraph
on their negative wreath supports and every wreath belongs to at most \(R\)
such moves, a greedy matching has size at least

\[
 \frac{|\mathcal I_F|}{DR}.
\tag{7.12}
\]

Neither the pointwise count \(|\mathcal I_F|\) nor the congestion \(R\)
follows from conductance of global overload shells.

## 8. The local-minimum gate and a scale-correct quantitative target

For an explicit medium atlas \(\mathscr T_A\), retain the weighted
root-disjoint improving degree (5.9). The strictly weaker unproved condition
needed for the exchange route is

> **Local-minimum gate \((\mathrm{LM}_A)\).**  There is a constant
> \(C_A<\infty\) such that every \(\mathscr T_A\)-local minimum satisfies
> \[
> J_A(F)\le C_AH_AB.
> \tag{LM\(_A\)}
> \]

A clean scale-correct quantitative sufficient condition for
\((\mathrm{LM}_A)\) is:

> **Unproved weighted exchange expansion \((\mathrm{EEX}_A)\).**  
> There exist constants \(\eta_A>0\) and \(C_A<\infty\) such that every
> exact factor satisfies
> \[
> \boxed{
> \operatorname{wd}_{\mathscr T_A}(F)
> \ge
> \eta_AJ_A(F)-C_AH_AB.}
> \tag{EEX\(_A\)}
> \]

### Theorem 8.1 (conditional implications)

If \((\mathrm{LM}_A)\) holds for every fixed \(A\), then

\[
 \min_FJ_A(F)=O_A(H_AB)=o(W)
\tag{8.1}
\]

for every fixed \(A\). Hence fixed-window overload MWB follows, and the
audited diagonalization gives the coefficient-one contiguous-OR bound.

#### Proof

From any starting factor, strict descent in the finite exchange graph ends
at a local minimum, to which \((\mathrm{LM}_A)\) applies. Finally

\[
 \frac{H_AB}{W}=\frac{H_A}{n}=O_A(m^{-1/2}).
\]

This proves (8.1). The fixed-window diagonal implication is the audited MWB
reduction; the diagonal may be chosen slowly enough that
\(H=o(m^{2/3})\), the proved uniform range. \(\square\)

Condition \((\mathrm{EEX}_A)\) implies \((\mathrm{LM}_A)\), with local-
minimum constant \(C_A/\eta_A\), because its left side vanishes at a local
minimum. Thus \((\mathrm{EEX}_A)\) also implies (8.1), but it is stronger
than the condition actually needed.

For the general profile-\(3\) atlas, every individual gain is at most
\(L_A^{\rm prof}=\Theta_A(m)\). Therefore, whenever
\(J_A(F)\ge\varepsilon W\), \((\mathrm{EEX}_A)\) would force
\(\Theta_A(B)\) pairwise root-disjoint improving trades. This is exactly the
positive-density expansion scale requested in the problem.

For aligned common-tail trades, however,

\[
 \operatorname{wd}_{\rm tail}(F)
 \le(2S_A-1)B
 =O_A(H_AB)=o(W)
\tag{8.2}
\]

for every factor. Hence no one-round common-tail theorem can put a positive
constant multiple of a linear overload on the right side. Those moves
require \(\Omega_A(\sqrt m)\) recomputed rounds or genuinely larger
footprints.

There is a precise combinatorial certificate for failure of “many
improving trades.” Suppose every trade in an atlas uses at most \(D\) old
wreaths and the maximum root-disjoint improving family at \(F\) has size
\(\nu\). The union of any maximal such family contains at most \(D\nu\)
wreaths and meets the negative support of every improving atlas trade.
Thus all improvement is funnelled through a small owner hitting set whenever
\(\nu=o(B/D)\), at that current factor. The hitting set need not persist
after a trade is applied and the atlas is recomputed.

No asymptotic high-overload exact-factor family with such an all-atlas
hitting set is presently constructed. The unconditional substitute is
Corollary 6.2: for roughly one third of individual transposition directions,
an orbit floor produces a genuine high restricted local minimum.

## 9. Adversarial audit and exact scope

1. **Absolute versus relative expansion.** Theorem 5.1 controls
   \(J_A(F)-J_A^\star\), not \(J_A(F)\). Replacing relative distance by
   absolute overload would already require \(J_A^\star=o(W)\), the fixed-
   window theorem being sought.

2. **Two small-trade scales.** The aligned common-tail footprint is
   \(4S_A-2=\Theta_A(\sqrt m)\). The general rooted profile-\(3\) bound is
   \(4T_A+6S_A-2=\Theta_A(m)\). Every speed and packing conclusion above
   uses the appropriate scale.

3. **Individual versus simultaneous gains.** Root-disjoint trades are
   jointly exact, but their lower-shadow overload gains need not add after
   simultaneous application. Weighted degree sums the individual gains
   from one common factor only.

4. **Parity scope.** Cyclic-order sign on unoriented wreaths is used only
   for even \(m\). The invariant covers the complete rooted profile-\(3\)
   \(C_8\) family and its signed composites, not arbitrary component or
   lifted-Graver moves. The explicit size-three component trade crosses it.

5. **Cube scope.** The MSW \(Q_{\operatorname{Cat}_{m-2}}\) is an isometric
   internal chart, not a claim about conductance of its ambient connected
   component. Its edge expansion is unsigned, and its \(o(W)\) overload
   diameter is exactly why it cannot certify bulk descent.

6. **Orbit-floor scope.** Theorem 6.1 survives arbitrary recomputation only
   while the same transposition is used. Switching to another transposition
   changes the invariant. Corollary 6.2 does not produce one factor locally
   minimal in every direction.

7. **No manufactured bad factor.** The orbit bottleneck is conditional on
   the starting value \(J_A(F)\). The report neither proves nor needs the
   existence of a linearly overloaded factor sequence. If all factors are
   already \(o(W)\)-balanced, MWB is true.

8. **Conductance scope.** Shell expansion gives average downward boundary
   edges and concentration around a median. It gives neither a low median
   nor an improving edge incident to each high vertex.

9. **No labelled conclusion.** All quantities are mobile unlabelled
   histogram overloads. A common balanced nested owner resolution remains a
   strictly stronger separate problem.

## 10. Final theorem-level status

The requested unconditional “every far factor has many edge-disjoint
improving explicit trades” is not proved. At the absolute scale it would
already imply fixed-window MWB; for the aligned four-letter library it is
also quantitatively impossible in one round.

What is proved is sharper than mere connectivity:

\[
\boxed{
\begin{gathered}
\text{full lifted-Graver exchange has exact root-disjoint relative gain;}\\
\text{the explicit small graph has a huge overload-flat expanding cube;}\\
\text{its profile-\(3\) lattice has }\Theta(B)\text{ parity components;}\\
\text{many one-transposition medium graphs have a constant overload floor.}
\end{gathered}}
\]

The weakest explicit exchange gate isolated here is \((\mathrm{LM}_A)\).
The stronger \((\mathrm{EEX}_A)\) is a scale-correct quantitative target.
An auxiliary-conformal refinement of a fixed fraction of the Graver gap
would instead prove only relative expansion
\(\operatorname{wd}\gtrsim J_A-J_A^\star\); it would still need the separate
input \(J_A^\star=o(W)\) and is not equivalent to \((\mathrm{EEX}_A)\).

Failure of \((\mathrm{EEX}_A)\) could, for example, manifest through a
high-overload factor whose improving atlas trades meet a small owner hitting
set, through a large matching of individually tiny gains, through gain
carried by wrong-geometry Graver moves outside the atlas, or through
genuinely large signed cancellation packets. No exact-factor obstruction
of these kinds is currently known.
