# Fourth-wave lane V: incidence-faithful portal membership and MTF fusion

Date: 2026-07-25

## 0. Verdict

This report combines the surface-scale portal-membership theorem from
MATH_ATTACK_V3_PORTAL_SHARING_CAPACITY_20260724.md with the audited global
portal construction in GLOBAL_PORTAL_CONSTRUCTION_AFTER_DRAY_20260724.md.

The answer has three parts.

1. **The isolated selected portals do not pay the full exact demand in the
   coefficient-one use.**
   A reverse-difference portal appendage of length \(Q\) has at most \(Q\)
   endpoint--box memberships when every arm start is private. Hence an
   \(o(W)\)-length isolated appendage supplies only \(o(W)\) memberships,
   while the V3 plateau ledger requires \(\Omega(W)\). More exactly, if the
   appendage is the only designated source of right-endpoint sharing, then
   the off-appendage leakage is at least
   \[
   G_s-2E-Q,
   \]
   where \(E=n-W\) and \(G_s\) is the exact full-plateau endpoint demand.
   Thus the isolated global portals cannot be the entire near-width repair.

2. **A fused modification does meet the stronger surface demand.**
   Cut an exact odd factor into its complementary Johnson geodesics and use
   the audited canonical radius-\(H\) adaptive-MTF lift on every geodesic.
   The resulting literal word has exact length
   \[
   \boxed{
   W+(2H+1)\frac{W}{m+1}
   =W+O_A(W/\sqrt m).}
   \tag{0.1}
   \]
   Its internal upper depth-one targets partition the whole rank-\((m+1)\)
   layer. After one common coordinate relabelling, all but \(o(W)\) of the
   selected window-dominant upper targets occur at endpoints whose paired
   middle targets lie in different product boxes.

   If \(\Pi_{\mathcal B}\) is the set of these shared endpoint positions
   serving a window-dominant box \(\mathcal B\), then
   \[
   \boxed{
   \sum_{\mathcal B\in\mathscr D_s}|\Pi_{\mathcal B}|
   \ge I_s-\frac{3W}{m+1},}
   \tag{0.2}
   \]
   where \(I_s\) is the number of rank-\((m+1)\) targets in the dominant
   boxes. Consequently
   \[
   \boxed{
   \frac1{|\mathscr D_s|}
   \sum_{\mathcal B\in\mathscr D_s}|\Pi_{\mathcal B}|
   \ge s-O(1),}
   \tag{0.3}
   \]
   and all but \(O(|\mathscr D_s|/\sqrt s)\) dominant boxes individually
   have
   \[
   |\Pi_{\mathcal B}|\ge s-\sqrt s.
   \tag{0.4}
   \]
   This is stronger than the V3 necessary average
   \((2/15-o(1))s\).

   The same depth-one endpoints already carry more right-sharing surplus
   than the complete V3 plateau dual demands:
   \[
   \boxed{
   \sum_{j\in S}(r_j-1)_+
   \ge I_s-\frac{3W}{m+1}>G_s}
   \tag{0.5}
   \]
   for all sufficiently large \(s\). This does not cover the remaining
   plateau targets, but it proves that membership and endpoint chronology are
   already installed inside one \(W+o(W)\) middle-productive word.

3. **The remaining high-degree gate is support, not chronology.**
   The depth-one fusion uses \(\Theta(W)\) degree-two endpoints. Compressing
   the same \(\Theta(W)\) genuine incidence into
   \(\Theta(W/\sqrt m)\) endpoints requires distinct supported targets at
   \(\Theta(\sqrt m)\) ranks. The fused MTF word supplies the literal
   occurrence chronology, but its deep canonical masks may repeat.

   An exact bipartite matching theorem below converts supported MTF
   occurrences into genuine target--endpoint--box incidences. It shows that
   a linear-size supported matching is sufficient and exactly identifies the
   missing obstruction. Independently fresh, residual-consuming canonical
   components cannot bypass it: their exact MTF bridge excess is
   \(2H\) per seam, so \(\Theta(W/H)\) short components cost
   \(\Theta(W)\). Long fused components, including the odd-factor
   geodesics, evade this chronology obstruction.

Thus the V3 surface-membership requirement is **not** an obstruction to
global MTF fusion. It is met unconditionally at depth one. What remains
open is the deep distinct-support theorem needed to attain the simultaneously
sharp physical portal count and degree.

No web search, finite search, or computational experiment is used.

---

## 1. The exact V3 demand

Let

\[
2m=3s,\qquad s\ \text{even},\qquad
W=\binom{2m}{m},\qquad
W_s=\binom{s}{s/2}.
\]

Split the \(2m=3s\) coordinates into three \(s\)-blocks and fix an arbitrary
SCD in each block. Their Cartesian products partition the Boolean cube into
\(W_s^3\) product boxes.

Use all three orientations of the height windows

\[
\sqrt s\le p,q\le1.1\sqrt s,
\qquad
3\sqrt s\le r\le3.1\sqrt s,
\tag{1.1}
\]

with admissible even heights. Let \(\mathscr D_s\) be the resulting family
of window-dominant boxes. For \(\mathcal B\in\mathscr D_s\), write

\[
\Delta_{\mathcal B}=r-p-q,
\qquad
w_{\mathcal B}=(p+1)(q+1).
\tag{1.2}
\]

The full plateau of \(\mathcal B\) consists of
\(\Delta_{\mathcal B}+1\) global ranks centered at \(m\), each containing
exactly \(w_{\mathcal B}\) targets. Put

\[
I_s=\sum_{\mathcal B\in\mathscr D_s}w_{\mathcal B}.
\tag{1.3}
\]

For all sufficiently large \(s\), rank \(m+1\) belongs to every one of these
plateaux, so \(I_s\) is exactly the number of selected rank-\((m+1)\) targets
in the window-dominant boxes.

Let

\[
\kappa_L=e^{-1/2}-e^{-121/200},
\qquad
\kappa_H=e^{-9/2}-e^{-961/200},
\qquad
\kappa=\kappa_L^2\kappa_H>0.
\tag{1.4}
\]

The SCD height law gives

\[
|\mathscr D_s|=(3\kappa+o(1))W_s^3.
\tag{1.5}
\]

The window inequalities imply

\[
\begin{gathered}
0.8\sqrt s\le\Delta_{\mathcal B}\le1.1\sqrt s,\\
\frac4{15}\le
\frac{\Delta_{\mathcal B}}{r_{\mathcal B}}
\le\frac{11}{30},\\
w_{\mathcal B}\ge s.
\end{gathered}
\tag{1.6}
\]

The upper ratio \(11/30\) is deliberately nonsharp but uniform:
\(\Delta_{\mathcal B}\le1.1\sqrt s\) and
\(r_{\mathcal B}\ge3\sqrt s\). Therefore

\[
I_s\ge s|\mathscr D_s|=\Theta(W),
\tag{1.7}
\]

where

\[
\frac{sW_s^3}{W}\longrightarrow\frac{2\sqrt3}{\pi}.
\tag{1.8}
\]

Define the exact full-plateau endpoint demand

\[
G_s=
\sum_{\mathcal B\in\mathscr D_s}
\left\lceil
\frac{w_{\mathcal B}\Delta_{\mathcal B}}{r_{\mathcal B}}
\right\rceil.
\tag{1.9}
\]

Equations (1.6)--(1.7) give both sides

\[
\boxed{
\frac4{15}I_s
\le G_s
\le\frac{11}{30}I_s+|\mathscr D_s|.}
\tag{1.10}
\]

In particular,

\[
\liminf_{s\to\infty}\frac{G_s}{W}
\ge
\frac{8\sqrt3}{5\pi}\kappa>0.
\tag{1.11}
\]

### The imported V3 endpoint and membership ledger

Select every plateau target in \(\mathscr D_s\), and only the global middle
layer in every other box. If a word of length \(n=W+E\) covers these
targets and one witness is chosen for each target, let
\(\ell_j,r_j\) be the left- and right-endpoint box degrees. Then V3 proves

\[
\boxed{
\mathcal C_\partial
:=\sum_j\bigl((\ell_j-1)_++(r_j-1)_+\bigr)
\ge G_s-2E.}
\tag{1.12}
\]

After deleting one baseline incidence from every occupied oriented endpoint
slot, at least \((G_s-2E)_+\) charged incidences remain, all on boxes in
\(\mathscr D_s\).

If \(\Pi_{\mathcal B}\) contains every physical position at which
\(\mathcal B\in\mathscr D_s\) participates in same-orientation endpoint
sharing, then each physical position contributes at most two oriented
incidences to one box. Hence

\[
2\sum_{\mathcal B\in\mathscr D_s}|\Pi_{\mathcal B}|
\ge G_s-2E.
\tag{1.13}
\]

For \(E=o(W)\), (1.5), (1.7), and (1.10) yield

\[
\frac1{|\mathscr D_s|}
\sum_{\mathcal B\in\mathscr D_s}|\Pi_{\mathcal B}|
\ge\left(\frac2{15}-o(1)\right)s.
\tag{1.14}
\]

This is the surface-scale demand to be tested.

---

## 2. Why the isolated global portals do not suffice

Let \(J\) be a family of designated right endpoints in an arbitrary word.
At \(j\in J\), suppose \(d_j\) distinct selected targets are represented by
intervals ending at \(j\). Let

\[
s_i=\#\{\text{these designated intervals whose left endpoint is }i\}.
\]

### Lemma 2.1 -- exact arm-start identity

\[
\boxed{
\sum_{j\in J}d_j=\sum_i s_i.}
\tag{2.1}
\]

#### Proof

Both sides count the same designated intervals, once by their right endpoint
and once by their left endpoint. Distinct targets ending at one \(j\) have
distinct left endpoints, because one pair of physical endpoints determines
one interval and one OR. \(\square\)

In an isolated reverse-difference block, every arm position starts at most
one designated suffix. Therefore an isolated appendage of length \(Q\)
satisfies

\[
\sum_{j\in J}d_j\le Q,
\qquad
\sum_{j\in J}(d_j-1)\le Q-|J|.
\tag{2.2}
\]

### Theorem 2.2 -- isolated-membership incompatibility

Suppose a word of length \(W+E\) covers the full V3 selected family, and let
\(J\) be a family of isolated right portals contained in an appendage of
length \(Q\). Put

\[
R_{\mathrm{off}}
=
\sum_j(\ell_j-1)_+
+\sum_{j\notin J}(r_j-1)_+.
\tag{2.3}
\]

Then

\[
\boxed{
R_{\mathrm{off}}
\ge G_s-2E-Q.}
\tag{2.4}
\]

Consequently, if \(E=o(W)\) and \(Q=o(W)\), then

\[
R_{\mathrm{off}}=\Omega(W).
\tag{2.5}
\]

#### Proof

The endpoints in \(J\) contribute at most
\(\sum_{j\in J}(r_j-1)_+\le Q\) by (2.2). Subtract this contribution from
(1.12). \(\square\)

Using (1.11), if \(Q\le\varepsilon W\) and \(E=o(W)\), then

\[
\liminf\frac{R_{\mathrm{off}}}{W}
\ge
\frac{8\sqrt3}{5\pi}\kappa-\varepsilon.
\tag{2.6}
\]

Thus a fixed small-\(\varepsilon\) isolated portal construction pays only a
corresponding fraction of the demand.  For fixed \(\varepsilon>0\), its
aggregate dominant-box membership is nevertheless \(\Theta_\varepsilon(W)\),
so its average has the correct **order**
\(\Theta_\varepsilon(s)\): the construction has
\(\Omega(\varepsilon W)\) useful incidences, while its
\(\Theta_\varepsilon(W/\sqrt s)\) endpoints contribute at most one
global-middle incidence each, so the remaining linear incidence lies in the
dominant plateaux.  What it does not prove is the exact V3 constant,
an almost-every-box distribution, or absorption of the full charged graph.
In the coefficient-one regime one must eventually take
\(\varepsilon\to0\), and its selected endpoints then pay \(o(W)\), not the
required \(\Omega(W)\).

The membership statement is equally direct. The total number of
endpoint--box memberships of these isolated flags is at most \(Q\). Since
\(|\mathscr D_s|=\Theta(W/s)\), an \(o(W)\) appendage supplies only
\(o(s)\) average membership per window-dominant box, contradicting (1.14)
if it is asked to carry the entire charged graph.

This is more than a physical portal-count obstruction: it is an exact
chronological arm-start obstruction. The arm positions must either acquire
unbounded start multiplicity or become positions already needed by the
middle-owning word.

---

## 3. Exact depth-one incidence-to-MTF fusion

The second alternative occurs in the audited adaptive-MTF construction.

### Audited input 3.1 -- odd-factor MTF word

For \(1\le H<m/2\), an exact odd factor cuts into

\[
B=\frac{W}{m+1}
\tag{3.1}
\]

vertex-disjoint oriented complementary Johnson geodesics, each with
\(m+1\) middle vertices. These paths partition
\(\binom{[2m]}m\). Their \(mB\) internal upper edge unions are pairwise
distinct and partition
\(\binom{[2m]}{m+1}\).

Every path is \(H\)-legal. Its canonical radius-\(H\) adaptive-MTF lift
uses one word update per middle edge and, after one exact reverse
initialization, exposes a saturated suffix flag from rank \(m-H\) through
rank \(m+H\) at every middle endpoint.

Independently initializing the \(B\) paths gives one literal nonzero word
\(\mathcal W_H\) of exact length

\[
\boxed{
|\mathcal W_H|
=W+(2H+1)B.}
\tag{3.2}
\]

Every middle mask is represented at its state endpoint, and every internal
upper edge union is represented as the depth-one upper member at the
corresponding noninitial endpoint.

These properties are the audited odd-cut and adaptive-MTF facts. No
unproved deep-support assertion is included in Audited input 3.1.

### Lemma 3.2 -- one relabelling makes almost every depth-one pair cross-box

There is a coordinate permutation \(\sigma\) for which at most
\(3W/(m+1)\) of the
internal pairs

\[
\sigma T\subset\sigma U,
\qquad |T|=m,\quad |U|=m+1,
\tag{3.3}
\]

lie in one product box.

#### Proof

Fix one nested pair \(T\subset U\). Under a uniform coordinate permutation,
conditional on \(\sigma U\), the lower mask \(\sigma T\) is uniform among
the \(m+1\) lower neighbours of \(\sigma U\). A product box contains at
most three lower neighbours of one Boolean mask, one for each factor-chain
coordinate. Therefore

\[
\Pr(\sigma T,\sigma U\text{ lie in one product box})
\le\frac3{m+1}.
\tag{3.4}
\]

There are

\[
mB=\binom{2m}{m+1}<W
\]

internal pairs. By linearity of expectation, their expected same-box count
is at most \(3W/(m+1)=o(W)\). Some common permutation attains this bound.
\(\square\)

Relabel the entire word, every path, and every suffix witness by this one
\(\sigma\). MTF updates and literal interval unions are preserved.

### Theorem 3.3 -- fused surface-membership theorem

Take

\[
H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\), and use the relabelled word
\(\sigma\mathcal W_H\). For every rank-\((m+1)\) target \(U\) lying in a box
\(\mathcal B\in\mathscr D_s\), let \(j(U)\) be its unique internal
upper-edge endpoint, and let \(T(U)\) be the paired middle target at that
endpoint.

Discard the targets for which \(T(U)\) and \(U\) lie in one product box.
For every \(\mathcal B\in\mathscr D_s\), define

\[
\Pi_{\mathcal B}
=
\{j(U):U\in\mathcal B,\ |U|=m+1,\ 
T(U)\text{ lies in a different product box}\}.
\tag{3.5}
\]

Then:

1. the word has length
   \[
   W+O_A(W/\sqrt m);
   \tag{3.6}
   \]
2. every \(j(U)\in\Pi_{\mathcal B}\) is a literal right-sharing endpoint
   serving \(\mathcal B\) and the distinct box containing \(T(U)\);
3. the total membership is
   \[
   \boxed{
   \sum_{\mathcal B\in\mathscr D_s}|\Pi_{\mathcal B}|
   \ge I_s-\frac{3W}{m+1};}
   \tag{3.7}
   \]
4. its average and almost-everywhere forms are
   \[
   \boxed{
   \frac1{|\mathscr D_s|}
   \sum_{\mathcal B\in\mathscr D_s}|\Pi_{\mathcal B}|
   \ge s-O(1),}
   \tag{3.8}
   \]
   and, for all but \(O(|\mathscr D_s|/\sqrt s)\) boxes,
   \[
   \boxed{
   |\Pi_{\mathcal B}|\ge s-\sqrt s;}
   \tag{3.9}
   \]
5. if \(S=\bigcup_{\mathcal B}\Pi_{\mathcal B}\), and witnesses are selected
   for the middle targets \(T(U)\) and upper targets \(U\), then
   \[
   \boxed{
   \sum_{j\in S}(r_j-1)_+
   \ge I_s-\frac{3W}{m+1}>G_s}
   \tag{3.10}
   \]
   for all sufficiently large \(s\).

#### Proof

Equation (3.6) follows from (3.2), because
\[
(2H+1)B=O_A(W/\sqrt m).
\]

The upper edge unions before relabelling partition the entire
rank-\((m+1)\) layer; a coordinate permutation preserves that layer.
Therefore exactly \(I_s\) of them lie in the window-dominant boxes after
relabelling. Their endpoints are distinct, and their upper targets are
globally distinct. Lemma 3.2 discards at most \(3W/(m+1)\) same-box pairs,
proving (3.7).

At a retained endpoint, the canonical suffix flag literally represents both
\(T(U)\) and \(U\). They belong to distinct boxes, so that endpoint has
right degree at least two and belongs to \(\Pi_{\mathcal B}\). This proves
the second claim and the first inequality in (3.10).

By (1.7), \(I_s=\Theta(W)\), while
\(|\mathscr D_s|=\Theta(W/s)\).  Since \(m=3s/2\),
\[
\frac{W/(m+1)}{|\mathscr D_s|}=O(1).
\]
Divide (3.7) by \(|\mathscr D_s|\) and use
\(I_s\ge s|\mathscr D_s|\) to obtain (3.8).

For the almost-everywhere claim, let \(b_{\mathcal B}\) be the number of
discarded targets in box \(\mathcal B\).  Since
\[
\sum_{\mathcal B}b_{\mathcal B}\le\frac{3W}{m+1}
=O(W/s)
=O(|\mathscr D_s|),
\]
at most \(O(|\mathscr D_s|/\sqrt s)\) boxes have
\(b_{\mathcal B}>\sqrt s\). Every other box satisfies
\[
|\Pi_{\mathcal B}|
=w_{\mathcal B}-b_{\mathcal B}
\ge s-\sqrt s.
\]
This proves (3.9).

Finally, (1.10) gives
\[
G_s\le\frac{11}{30}I_s+|\mathscr D_s|
=\left(\frac{11}{30}+o(1)\right)I_s.
\]
Together with (3.7), and \(W/(m+1)=o(I_s)\), this proves the strict final
inequality in (3.10).
\(\square\)

### Scope of Theorem 3.3

The theorem is a literal, integral fusion theorem. Its arm updates are not
an appendage: they are the MTF updates which traverse all \(W\) middle
owners. It meets the V3 membership scale by a factor bounded away from one
and pre-installs enough scalar right-sharing surplus to pay the whole V3
plateau dual.

It does **not** assert that \(\sigma\mathcal W_H\) covers every target in
the full plateaux. If a future \(o(W)\)-length repair covers the missing
targets, the witnesses from Theorem 3.3 remain valid and no new
surface-membership supply is needed. The remaining issue is coverage or
support, not endpoint membership.

The price is physical dispersion: \(S\) has \(\Theta(W)\) positions and
each displayed endpoint is used only at depths \(0\) and \(1\). Rank
injectivity therefore permits no compression of this particular
depth-one selection to \(\Theta(W/\sqrt m)\) positions.

---

## 4. Exact occurrence-to-incidence matching

The preceding theorem uses a rank at which the odd factor has perfect
global support. At deeper ranks the canonical MTF flags remain literal,
but their masks may repeat. The following theorem separates support loss
from endpoint chronology exactly.

Let \(\mathcal O\) be a finite family of literal selected occurrences.
Every occurrence \(o\in\mathcal O\) has:

* a target mask \(T(o)\);
* a physical endpoint \(j(o)\);
* the unique product box \(\mathcal B(o)\) containing \(T(o)\).

Let

\[
\mathcal T(\mathcal O)=\{T(o):o\in\mathcal O\},
\qquad
\mathcal C(\mathcal O)=
\{(j(o),\mathcal B(o)):o\in\mathcal O\}.
\tag{4.1}
\]

Form the bipartite occurrence graph \(\Gamma_{\mathcal O}\) between the
target vertices \(\mathcal T(\mathcal O)\) and endpoint--box cell vertices
\(\mathcal C(\mathcal O)\), with one edge for every occurrence.

### Theorem 4.1 -- exact incidence-to-MTF matching theorem

The maximum number \(M(\mathcal O)\) of occurrences which can be selected
with pairwise distinct target masks and pairwise distinct endpoint--box cells
is the matching number of \(\Gamma_{\mathcal O}\). Equivalently,

\[
\boxed{
M(\mathcal O)
=
\min_{\mathcal X\subseteq\mathcal T(\mathcal O)}
\left(
|\mathcal T(\mathcal O)\setminus\mathcal X|
+|N_{\Gamma}(\mathcal X)|
\right).}
\tag{4.2}
\]

Put

\[
U=|\mathcal O|,
\qquad
R_T=U-|\mathcal T(\mathcal O)|,
\tag{4.3}
\]

and, for a cell \(c\), let \(n_c\) be its occurrence multiplicity. Define

\[
R_C=\sum_c(n_c-1)_+,
\qquad
C=\sum_c\binom{n_c}{2}.
\tag{4.4}
\]

Then

\[
\boxed{
M(\mathcal O)\ge U-R_T-R_C\ge U-R_T-C.}
\tag{4.5}
\]

Every matched edge is already a literal interval witness in the same MTF
word; no connector or reset is added by the matching.

#### Proof

Selecting pairwise distinct targets and cells is exactly selecting a
matching in \(\Gamma_{\mathcal O}\). Formula (4.2) is the deficiency form
of Hall's theorem:
\[
\nu(\Gamma)
=|\mathcal T|-\max_{\mathcal X\subseteq\mathcal T}
\bigl(|\mathcal X|-|N(\mathcal X)|\bigr).
\]

For (4.5), first delete all but one occurrence of each repeated target,
losing exactly \(R_T\) occurrences. Next delete all but one remaining
occurrence in each repeated cell. This loses at most the original \(R_C\)
occurrences, and target distinctness is preserved. The surviving
occurrences form a matching. Finally
\((n-1)_+\le\binom n2\) gives \(R_C\le C\). \(\square\)

### Corollary 4.2 -- concentrated high-degree fusion criterion

Suppose one literal fused MTF word has \(W\) state endpoints and at most
\(2h+1\) selected flag occurrences at each endpoint. Assume an occurrence
family satisfies

\[
\boxed{
U-R_T
=|\mathcal T(\mathcal O)|
\ge c\,hW,}
\qquad
C=o(hW)
\tag{4.6}
\]

for a fixed \(c>0\). Then there are

\[
P=\left\lceil\frac Wh\right\rceil
\tag{4.7}
\]

physical endpoints carrying \(\Omega(W)\) genuine distinct
target--endpoint--box incidences. Their average degree is \(\Omega(h)\).

#### Proof

Theorem 4.1 gives \(M(\mathcal O)=\Omega(hW)\). Assign every matched edge to
its endpoint, order the \(W\) endpoint degrees decreasingly, and retain the
largest \(P\). Their average is at least the global average, so their total
degree is at least
\[
\frac PW M(\mathcal O)=\Omega(W).
\]
The per-endpoint cap \(2h+1\) gives the asserted scale. \(\square\)

The exact condition is (4.2), not the sufficient support/collision bound
(4.6).
Corollary 4.2 shows what the global MTF construction already solves and what
it does not:

* canonical suffix intervals solve chronology;
* the relabelling collision theorem solves endpoint--box cell repetition;
* deep repeated target masks are the remaining Hall defect.

A PTAD-type trace/support theorem supplies a family satisfying (4.6), and
then Corollary 4.2 yields the sharp
\(\Theta(W/\sqrt m)\)-portal, \(\Theta(\sqrt m)\)-degree conclusion.
The unconditional odd-factor word supplies (4.6) only at depth one, where
\(h=1\) and the physical endpoint count is \(\Theta(W)\).

---

## 5. The exact chronology obstruction for short canonical pieces

The support gate cannot be avoided by returning to independently initialized
short portal blocks.

Let an MTF state be an ordered partition. For a source state
\(\Sigma\) and target state

\[
\Pi=(B_1,\ldots,B_t),
\]

put

\[
U_a=B_1\cup\cdots\cup B_a
\]

and define \(a_*(\Sigma,\Pi)\) to be the least \(a\) for which deleting
\(U_a\) from every source block leaves exactly the target suffix
\((B_{a+1},\ldots,B_t)\).

### Audited input 5.1 -- exact MTF bridge metric

The minimum length of a nonempty MTF word carrying \(\Sigma\) to \(\Pi\) is

\[
\boxed{
d_{\mathrm{MTF}}^+(\Sigma,\Pi)
=\max\{1,a_*(\Sigma,\Pi)\}.}
\tag{5.1}
\]

Indeed, after \(q\) updates the positive-last-occurrence blocks form a
prefix of the target state and the undeleted source blocks form its suffix.
Conversely, the chronological updates
\(U_a,U_{a-1},\ldots,U_1\) realize the target whenever the deletion-suffix
condition holds.

For a fresh canonical radius-\(H\) state there are

\[
t=2H+2
\tag{5.2}
\]

blocks: a first \((m-H)\)-block, \(2H\) singletons, and a final
\((m-H)\)-residual block.

### Audited input 5.2 -- residual-depletion obstruction

Assume \(m-H\ge2\). If a canonical component consumes even one coordinate
of its initial residual block, then every bridge from its terminal state to
any fresh canonical radius-\(H\) state has length at least

\[
2H+1.
\tag{5.3}
\]

The reason is exact. A target suffix of at least two blocks ends in an
\((m-H)\)-block. After depletion, the only source block large enough to
supply it is the source first block. Preserving that block's full size
makes it the first surviving source block, so it cannot be the last block of
a suffix of length at least two.

### Theorem 5.3 -- short-component incompatibility

Suppose \(K\) canonical radius-\(H\) components are concatenated, every
component except possibly the last is residual-consuming, and one word
position per middle owner is counted as principal cost. Then the reset and
bridge excess is at least

\[
\boxed{
(2H+1)+2H(K-1).}
\tag{5.4}
\]

Consequently:

1. if \(K=\Theta(W/H)\), the excess is \(\Theta(W)\);
2. if the excess is \(o(W)\), then
   \[
   K=o(W/H);
   \tag{5.5}
   \]
3. if the components contain \(W-o(W)\) middle owners in total, their
   average number of owners is
   \[
   \omega(H).
   \tag{5.6}
   \]

#### Proof

The first fresh canonical initialization costs \(2H+1\) beyond its first
middle-owner endpoint. By (5.3), every subsequent incoming bridge has
length at least \(2H+1\); its last update may also serve as the next
component's first principal owner position, leaving bridge excess at least
\(2H\). Summing proves (5.4). The three consequences are immediate.
\(\square\)

The odd-factor MTF word evades this obstruction sharply:

\[
K=\frac{W}{m+1}=o(W/H),
\qquad
\text{owners per component}=m+1\gg H
\tag{5.7}
\]

when \(H=\Theta(\sqrt m)\). Therefore there is no general chronology
obstruction to fused portals. The obstruction applies precisely to
isolated or short fresh canonical pieces.

---

## 6. Independent audit and implication scope

The decisive statements were rederived independently from the two source
reports. The audit classifications are as follows.

### Valid

1. The V3 full-plateau endpoint demand, its factor \(2E\), and its
   per-served-box surface-membership consequence.
2. The global SCD collision theorem and the literal isolated suffix
   construction.
3. The arm-start identity and its \(\Omega(W)\) tax for isolated
   \(\Omega(W)\)-incidence appendages.
4. The exact odd-cut geodesic count \(W/(m+1)\), the rank-\((m+1)\)
   upper-union partition, the canonical adaptive-MTF path lift, and the
   exact length (3.2).
5. The common-relabelling depth-one collision estimate (3.4).
6. The exact bridge metric and the residual-depletion lower bound under the
   necessary hypothesis \(m-H\ge2\).

### Strengthened here

The previously stated honest depth-one theorem retained only a fixed
\(\alpha W/4\) subset by a weighted expectation. That loss is unnecessary.
The internal upper edge unions partition the **entire** rank-\((m+1)\)
layer, so the number \(I_s\) falling in the dominant target family is
deterministic under every relabelling. Only the same-box pair count is
random. Choosing a relabelling with \(o(W)\) such pairs gives the stronger
bound (3.7), the almost-every-box membership statement (3.9), and the
surplus domination (3.10).

The existing endpoint Pareto statement should also be read with the
transcription

\[
\Delta_*\le1.1\sqrt s;
\]

the missing inequality symbol in its displayed definition is only a
typographical error.

### Unsupported without an extra hypothesis

The box-rainbow **occurrence** flags in the fused word do not by themselves
give deep, globally distinct selected targets. Repeated occurrences of one
mask cannot be credited as different V3 targets. Therefore the following
unconditional implication is not proved:

\[
\text{box-rainbow canonical occurrences}
\Longrightarrow
\Theta(W/\sqrt m)\text{ genuine degree-}\Theta(\sqrt m)
\text{ portals}.
\]

The exact missing condition is a matching of size \(\Omega(HW)\) in (4.2),
with (4.6) as a clean sufficient form.  It is neither necessary nor
generally possible to demand repetition loss \(R_T=o(HW)\): at Gaussian
depth the rank size itself is a fixed fraction of \(W\).  PTAD or another
deep-support theorem would supply the required linear support.
it. This is an unproved support statement, not labelled common-owner
synchronization and not MWB.

### Final implication scope

The unconditional theorem proved here is

\[
\boxed{
\begin{gathered}
\text{one literal }W+O(W/\sqrt m)\text{ MTF word}\\
\text{covers every middle and rank-}(m+1)\text{ target and carries}\\
\left(I_s-O(W/m)\right)=\Theta(W)\text{ honest cross-box depth-one sharing,}\\
\text{with average dominant-box membership }s-O(1).
\end{gathered}}
\tag{6.1}
\]

This settles the stronger V3 membership question positively. It does not
cover the full Gaussian window and therefore does not prove the contiguous-OR
conjecture.

The sharp remaining theorem is:

> Find, inside one fused \(W+o(W)\) MTF chronology, a central-band occurrence
> graph whose target--endpoint-box matching number is \(\Omega(HW)\).

If this is achieved for \(H=\Theta(\sqrt m)\), Corollary 4.2 produces the
simultaneously sharp \(\Theta(W/\sqrt m)\) physical portals,
\(\Theta(\sqrt m)\) genuine degree, and \(\Theta(W)\) distinct selected
incidence. The short-component theorem proves that this cannot be replaced
by \(\Theta(W/H)\) independently fresh residual-consuming portal pieces.
