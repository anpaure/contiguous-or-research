# Non-row-power PBBS/MSW residence trades: edit stability, hierarchical tolls, and the exact growing-fusion escape

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, web
search, or external data are used.

## 0. Exact outcome

Put

\[
 n=2m+1,\qquad B=\operatorname {Cat}_m,\qquad
 W=\binom{2m+1}{m}=nB,\qquad H=\lceil A\sqrt m\rceil,
\tag{0.1}
\]

where \(A>0\) is fixed. This note studies genuine factor/path trades,
not cyclic rerootings, reversals, or row powers.

The answer is a proved/conditional trichotomy for the analyzed compiler
classes rather than an unconditional no-go.

1. **Residence stability forces factor edits at the \(W/H\) scale, not
   at the \(W\) scale.** For any two odd-graph spanning \(2\)-factors
   \(F,G\),

   \[
   \boxed{
   |\nu_H(F)-\nu_H(G)|
       \le 2|E(F)\setminus E(G)|.}
   \tag{0.2}
   \]

   If the audited long-cycle quotient gate fails, so that

   \[
      \overline\nu_H\ge \varepsilon B/\sqrt m,
   \tag{0.3}
   \]

   then all \(n\) phase lifts of the selected nonwrapping quotient
   intervals are mutually edge-disjoint. Hence their physical packing has
   size at least \(\varepsilon W/\sqrt m\), and every exact wreath factor
   \(G\) satisfies

   \[
   \boxed{
   |E(F_{\rm PBBS})\setminus E(G)|
      \ge {\varepsilon\over2}{W\over\sqrt m}.}
   \tag{0.4}
   \]

   A route using alternating \(C_8\)'s therefore needs at least

   \[
   \boxed{{\varepsilon\over8}{W\over\sqrt m}}
   \tag{0.5}
   \]

   switch applications. In particular, the certified static clean
   \(C_8\) bank of size \((1/64-o(1))B\), and every bounded number of
   Catalan-size rounds, are too small by a factor \(\Theta(\sqrt m)\).
   Equations (0.4)--(0.5) use the long-cycle, nonwrapping definition in
   (0.3). They are false at this scale for an arbitrary wrapped quotient
   interval, for which only \(n/(2|I|)\) disjoint phase lifts are forced.

2. **Every additive collar/span hierarchy or self-contained bounded-group
   append hierarchy still pays \(\Omega(W)\).**
   If \(M\) destroyed edge-disjoint Gaussian residence traces, each of
   length at least \(L\), are serviced by clusters lying on proper carrier
   arcs of individual old cycles, with spans \(S_j\), and cluster \(j\)
   has additive charge

   \[
       \alpha H+\beta S_j-c_0,
       \qquad \alpha,\beta>0,
   \tag{0.6}
   \]

   with \(\alpha H>c_0\), then

   \[
   \boxed{
   L_{\rm new}\ge
   M\min\left\{\beta L,{\alpha H-c_0\over2}\right\}.}
   \tag{0.7}
   \]

   For the established dominance chart
   \((\alpha,\beta,c_0)=(7,3,3)\), the critical family has
   \(M=\Omega_{A,\varepsilon}(W/\sqrt m)\) and
   \(L=\Theta_{A,\varepsilon}(\sqrt m)\), so (0.7) is
   \(\Omega_{A,\varepsilon}(W)\). Thus arbitrary clustering admissible for
   the existing chart, in particular \(3H+S_j\le m+1\), does not rescue
   that collar/span compiler, even when the chosen cuts are phase-dependent
   and non-row-power.

   More generally, if one self-contained appended block services at most
   \(d\) clean cuts and each cut has \(q\) distinct equal-rank crossing
   targets, then

   \[
       \boxed{L_{\rm new}\ge q\left\lceil J/d\right\rceil.}
   \tag{0.8}
   \]

   At \(J=\Theta(W/H)\) and \(q=\Theta(H)\), fixed \(d\) gives a linear
   bill. A bounded-arity hierarchy of fixed depth \(r\) has effective
   \(d\le d_0^r=O(1)\) and is therefore closed. Growing depth can make
   \(d_0^r\to\infty\) and is not excluded; invariantly, sublinear cost
   requires unbounded top-level packet mass.

3. **A universal \(\Omega(W)\)-letter obstruction is false.** The exact
   two-parity simple-return chart has circular packet-interior contribution
   \(2s+3\) against \(2s+2\) owner occurrences; opening each literal
   chain costs a further \(s-1\) letters. If \(t_s\) height-\(s\) packets
   form \(c_s\) literal port chains, its exact excess is

   \[
      \boxed{
      \Delta=\sum_s\bigl[t_s+c_s(s-1)\bigr].}
   \tag{0.9}
   \]

   For Gaussian heights \(\alpha H\le s\le H\), writing
   \(t=\sum_st_s\), \(c=\sum_sc_s\), and
   \(M_0=\sum_s(2s+2)t_s\), one has the exact bounds

   \[
   {1\over2(H+1)}+{\alpha H-1\over2(H+1)}{c\over t}
   \le {\Delta\over M_0}
   \le
   {1\over2(\alpha H+1)}+{H-1\over2(\alpha H+1)}{c\over t}.
   \tag{0.10}
   \]

   Hence this packet interior has \(o(M_0)\) excess exactly when
   \(c/t\to0\). Bounded average chain length gives \(\Omega(M_0)\), while
   diverging average chain length removes the linear toll. A separated-star
   cross-atlas braid realizes the required unbounded **one-sided** path
   fusion in a nontrivial integral class, while the sliding-core model
   realizes the full abstract escape at critical residence density. Thus
   residence packing cannot by itself prove an
   \(\Omega(W)\) fresh-letter lower bound.

The canonical PBBS critical family is not yet placed in the positive
class. A near-minimal missing object is an exact, root-scale,
exterior-moving braid which makes \(\Theta(W/H)\) factor-edge changes,
hits the long-sector
double deck, fuses a diverging number of edits per terminal component,
and re-covers all lower and upper Gaussian crossing windows through one
common provider union. No existing PBBS \(C_8\), fixed MSW component,
localized pentagon, or suspended circuit proves this.

Only the lower bound \(\Omega_{A,\varepsilon}(W/H)\) is forced below;
the displayed \(\Theta(W/H)\) is the near-minimal design target. A valid
construction is not excluded from using \(\omega(W/H)\) but \(o(W)\)
factor edits.

## 1. Residence packing is Lipschitz in factor-edge distance

Let \(F\) be a spanning \(2\)-factor of \(KG(2m+1,m)\). At a middle
vertex \(X\), its two factor neighbours determine one complement-projected
step-two Johnson transition. Let \(\mathcal I_H(F)\) be the family of
positive coordinate-residence intervals of length at most \(H\), with
the insertion and removal transitions included, and let \(\nu_H(F)\) be
the maximum number with pairwise disjoint projected transition-edge
supports.

### Theorem 1.1 (factor-edge Lipschitz theorem)

For arbitrary spanning odd-graph \(2\)-factors \(F,G\),

\[
 \boxed{
 |\nu_H(F)-\nu_H(G)|
 \le2s(F,G),\qquad
 s(F,G):=|E(F)\setminus E(G)|.}
\tag{1.1}
\]

The assertion is uniform in \(H\).

#### Proof

Let \(D\) be the set of projected step-two transitions of \(F\) whose
unordered factor-neighbour pair changes in \(G\). One removed odd-graph
edge is incident with two vertices and can change only the projected
transition centred at each endpoint. Therefore

\[
 |D|\le2s(F,G).
\tag{1.2}
\]

Take a maximum edge-disjoint packing \(\mathcal P\subseteq\mathcal I_H(F)\).
At most \(|D|\) members of \(\mathcal P\) meet \(D\), since their
transition-edge supports are disjoint. Every other member lies wholly in
a common residual factor path. The new factor may traverse that path in
the opposite orientation, but reversing a positive coordinate run merely
interchanges its insertion and removal endpoints; its transition-edge set
and its length are unchanged. Hence every such interval remains a member
of \(\mathcal I_H(G)\). Thus

\[
 \nu_H(G)\ge\nu_H(F)-|D|
             \ge\nu_H(F)-2s(F,G).
\tag{1.3}
\]

Interchanging \(F\) and \(G\), and using
\(|E(F)\setminus E(G)|=|E(G)\setminus E(F)|\) for two spanning
\(2\)-factors, proves (1.1). \(\square\)

### Corollary 1.2 (exact wreath endpoint)

If \(G\) is an exact \(C_n\)-factor, then

\[
 \nu_H(G)=0\qquad(H\le m).
\tag{1.4}
\]

Consequently

\[
 \boxed{s(F,G)\ge\nu_H(F)/2.}
\tag{1.5}
\]

#### Proof

On a wreath \(C_n\), the omitted-label word is a permutation of the
\(n\) coordinates. The next cyclic occurrence of any omitted label is
one full lap later, giving projected positive residence \(m+1\). This
proves (1.4), and (1.5) follows from Theorem 1.1. \(\square\)

### Corollary 1.3 (alternating-cycle count)

A simple alternating \(C_{2a}\) removes \(a\) current factor edges, so
one switch changes \(\nu_H\) by at most \(2a\). Any route from \(F\) to
an exact wreath factor using \(r_a\) such switches obeys

\[
 \boxed{r_a\ge\nu_H(F)/(2a).}
\tag{1.6}
\]

For \(C_8\), this is \(r_4\ge\nu_H(F)/8\). Cancellations between
successive switches cannot improve the bound, because the final edge
distance is at most \(ar_a\).

## 2. The Gaussian long-deck scale and why the qualifier matters

Assume the strict quotient packing gate fails along a subsequence:

\[
 \overline\nu_H\ge\varepsilon B/\sqrt m.
\tag{2.1}
\]

By definition, \(\overline\nu_H\) maximizes over nonwrapping intervals on
quotient cycles longer than \(H+1\). Choose a maximizing quotient packing
\(\overline{\mathcal P}\). The argument (2.3)--(2.4) below applies to
every member of \(\overline{\mathcal P}\), not only to the later simple
subfamily, and distinct members have disjoint quotient traces. Therefore

\[
 \nu_H(F_{\rm PBBS})
 \ge n|\overline{\mathcal P}|
 \ge\varepsilon {W\over\sqrt m}.
\tag{2.1a}
\]

Corollaries 1.2--1.3 applied directly to (2.1a) prove the
\(\varepsilon/2\) and \(\varepsilon/8\) constants in (0.4)--(0.5).
The following stability extraction loses constants but supplies the
Gaussian lower trace length needed for the collar theorem.

The audited critical-saturation theorem supplies constants
\(a,c>0\) and a quotient-edge-disjoint family \(\mathcal Q\) of simple
fixed-core sectors such that

\[
 |\mathcal Q|\ge cB/\sqrt m,
 \qquad
 a\sqrt m\le |E(I)|\le H+1,
\tag{2.2}
\]

every selected interval is nonwrapping on a quotient cycle longer than
\(H+1\), and the one-edge translates are also pairwise disjoint.

For a quotient interval of \(k\) edges on a physical cycle \(C\), let
\(h\) be the spatial stabilizer size and \(d=|C|/h\) the quotient-cycle
length. The exact translate-packing formula is

\[
 \alpha_\Gamma(I)
 ={n\over h}
   \left\lfloor{h\over\lceil k/d\rceil}\right\rfloor.
\tag{2.3}
\]

Here \(k<d\), so \(\lceil k/d\rceil=1\), and therefore

\[
 \boxed{\alpha_\Gamma(I)=n.}
\tag{2.4}
\]

All phase lifts of one selected interval are disjoint. Lifts of different
selected intervals are disjoint because their quotient traces are
disjoint. Consequently the physical PBBS factor has a packing of size

\[
 M_{\rm phys}=n|\mathcal Q|
 \ge c{W\over\sqrt m}
 =(cA+o(1)){W\over H}.
\tag{2.5}
\]

Combining (2.5) with Corollaries 1.2--1.3 gives

\[
 |E(F_{\rm PBBS})\setminus E(G)|
 \ge {c\over2}{W\over\sqrt m},
\tag{2.6}
\]

and at least

\[
 {c\over8}{W\over\sqrt m}
\tag{2.7}
\]

alternating \(C_8\)'s in a \(C_8\)-only route.

The nonwrapping hypothesis is indispensable. For a generic wrapped
interval, (2.3) yields only

\[
 \alpha_\Gamma(I)\ge {n\over2k},
\tag{2.8}
\]

and a quotient family of size \(B/H\) may then force only \(O(B)\)
physical intervals. The explicit gap-five quotient three-cycle has
\(d=3,k=4\) and is exactly such a wrapped exception. It is excluded from
the long-cycle definition used in (2.1).

### Corollary 2.1 (static PBBS bank shortage)

The audited initial clean-\(C_8\) reservoir has

\[
 r_0=(1/64-o(1))B
\tag{2.9}
\]

pairwise vertex-disjoint candidates. Even granting exact-factor legality,
perfect targeting, and no cancellation, Theorem 1.1 lets this bank reduce
\(\nu_H\) by at most

\[
 8r_0=(1/8-o(1))B=o(B\sqrt m).
\tag{2.10}
\]

The critical physical packing in (2.5) is \(\Omega(B\sqrt m)\). Thus a
bounded number of static Catalan rounds cannot work. A successful dynamic
hierarchy must create \(\Omega(B\sqrt m)\) switch opportunities, or use
larger trades whose total final odd-edge support is
\(\Omega(B\sqrt m)\).

This is an availability obstruction, not a word-length obstruction:
\(B\sqrt m=W/\Theta(H)=o(W)\).

The conclusion is specific to bounded-edge templates. If a hybrid replaces
\(S\) complete wreath rows, then it can remove at most \(nS\) old factor
edges. Equation (2.6) forces only

\[
 S\ge {c\over2}{B\over\sqrt m}.
\tag{2.11}
\]

Thus a whole-row or cross-parent trade of growing edge support is not
excluded by the clean-\(C_8\) shortage. Its difficulty is exact ownership
and all-depth provider compatibility, not raw edge mass.

## 3. A multidepth dependency refinement

The preceding theorem is one-depth. Its exact multidepth form identifies
the only way to strengthen the factor-edge lower bound.

For each \(q\) in a depth set \(Q\), choose an edge-disjoint old packing
\(\mathcal P_q\), and let

\[
 U_q=\bigcup_{I\in\mathcal P_q}E(I),
 \qquad
 \kappa=\max_e|\{q\in Q:e\in U_q\}|.
\tag{3.1}
\]

### Theorem 3.1 (multidepth surgery with overlap parameter)

If a new projected factor removes the old transition set \(D\), then

\[
 \boxed{
 \sum_{q\in Q}
   \bigl(|\mathcal P_q|-\nu_q(F_1)\bigr)_+
 \le \sum_{q\in Q}|D\cap U_q|
 \le\kappa|D|.}
\tag{3.2}
\]

#### Proof

At depth \(q\), every packed interval avoiding \(D\) survives. Because
\(\mathcal P_q\) is edge-disjoint, the number destroyed is at most
\(|D\cap U_q|\). Sum over \(q\). Every edge of \(D\) is counted in at
most \(\kappa\) of the sets \(U_q\), proving the second inequality.
\(\square\)

Thus an aggregate annular reduction of order \(W\) forces
\(|D|=\Omega(W/\kappa)\). A bounded-congestion multidepth packing would
give an \(\Omega(W)\) factor-edit obstruction. The estimate permits the
maximally hereditary value \(\kappa=\Theta(H)\), and no PBBS theorem
available here excludes that dependency. In that case it leaves exactly
the \(\Omega(W/H)\) scale. Treating cube signs or depths as independent
would silently set \(\kappa=1\) and is invalid.

## 4. Exact lower bound for additive collar-plus-span hierarchies

The sublinear edge distance in (2.6) becomes a linear bill in all known
chronological seam compilers.

Let \(\mathcal P\) be \(M\) pairwise edge-disjoint old residence traces,
each containing at least \(L\) transition edges. Choose one hitting cut
from each trace and partition the chosen cuts, separately on each old
cycle, into \(K\) clusters. On one proper carrier arc for cluster \(j\),
let \(S_j\) be the distance between its first and last selected cuts, and
let \(k_j\) be the number of traces assigned to it.

### Lemma 4.1 (cluster span forced by disjoint long traces)

For every cluster,

\[
 S_j\ge L(k_j-2)_+.
\tag{4.1}
\]

Consequently

\[
 \boxed{\sum_{j=1}^KS_j\ge L(M-2K)_+.}
\tag{4.2}
\]

#### Proof

Order the assigned traces and their chosen cuts on the carrier arc. Every
trace except possibly the first and last lies wholly between the two
extreme selected cuts: otherwise it would cross an extreme trace, contrary
to edge-disjointness. These \(k_j-2\) internal traces are disjoint and
each has length at least \(L\), proving (4.1). Summing and using
\(\sum_j(k_j-2)_+\ge(M-2K)_+\) proves (4.2). \(\square\)

### Theorem 4.2 (collar--span hierarchy bound)

Suppose the literalization is additive across the clusters and obeys

\[
 L_{\rm new}\ge
 \sum_{j=1}^K(\alpha H+\beta S_j-c_0),
 \qquad \alpha,\beta>0,
\tag{4.3}
\]

and \(\alpha H>c_0\). Then

\[
 \boxed{
 L_{\rm new}\ge
 M\min\left\{\beta L,{\alpha H-c_0\over2}\right\}.}
\tag{4.4}
\]

#### Proof

Put \(a_0=\alpha H-c_0\). By Lemma 4.1,

\[
 L_{\rm new}
 \ge a_0K+\beta L(M-2K)_+.
\tag{4.5}
\]

If \(K\ge M/2\), the first term is at least \(a_0M/2\). If
\(K<M/2\), divide (4.5) by \(M\) and minimize the affine function

\[
 \beta L+{K\over M}(a_0-2\beta L)
\tag{4.6}
\]

on \([0,1/2]\). Its minimum is
\(\min\{\beta L,a_0/2\}\). \(\square\)

For the established dominance/QCF chart,

\[
 q_H(S)=7H+3S-3,
\tag{4.7}
\]

for admissible clusters satisfying \(3H+S\le m+1\). Therefore every
such clustering obeys

\[
 \boxed{
 L_{\rm new}\ge
 M\min\left\{3L,{7H-3\over2}\right\}.}
\tag{4.8}
\]

Apply this to all spatial lifts of the critical family in (2.2). There
are \(M\ge cW/\sqrt m\) disjoint traces and each has
\(L\ge a\sqrt m\). Hence

\[
 \liminf {L_{\rm new}\over W}
 \ge c\min\{3a,7A/2\}>0.
\tag{4.9}
\]

This permits arbitrary non-row-power choices of the hitting phase and all
cluster sizes admissible for the chart on proper old-cycle carrier arcs.
It rules out the additive collar-plus-span literalization, not a wholesale
replacement of the baseline chronology.

## 5. Bounded-group appended words and the fusion threshold

There is an even simpler obstruction when the repair is a union of
self-contained appended blocks.

Suppose \(J\) strongly clean cuts each expose \(q\) pairwise distinct
targets of one fixed rank, and a repair block is assigned at most \(d\)
cuts. Targets assigned to distinct blocks need not be distinct, but the
\(q\) targets assigned to one nonempty block require \(q\) distinct
witness endpoints in that block: equal-rank distinct OR targets cannot
share a left endpoint.

### Theorem 5.1 (bounded-group append toll)

Every such self-contained repair has

\[
 \boxed{L_{\rm new}\ge q\lceil J/d\rceil.}
\tag{5.1}
\]

In particular, if \(J\ge cW/H\) and \(q\ge\gamma H\), then

\[
 \boxed{L_{\rm new}\ge(c\gamma/d)W.}
\tag{5.2}
\]

The theorem does not charge the same target twice merely because it
occurs at two cuts; the strong-clean hypothesis supplies the \(q\)
distinct targets inside every serviced block. Its conclusion is exactly
that fixed packet mass \(d\) is insufficient. A hierarchy with terminal
mass \(d_m\) has lower bound \(\Omega(W/d_m)\); little-oh cost requires
\(d_m\to\infty\).

If the selected cuts have disjoint \(q\)-collars and every corresponding
window is eligible, then at depth \(q=\Theta(H)\),
\(J=\Theta(W/H)\) erased boundaries carry exactly
\(2qJ=\Theta(W)\) signed lower/upper crossing occurrences. If every
physical target has multiplicity at most \(D\) in this crossing
catalogue, any distinct-target append needs at least \(2qJ/D\) letters.
Thus bounded multiplicity is another fixed-block no-go. The PBBS
occurrence cap \(\binom{2q+1}{q}\) is exponential in \(q\), so counting
alone does not exclude the required unbounded provider multiplicity.

## 6. The one-parity certificate invariant and its exact failure

An isolated simple return of gap \(2s+1\) has one parity row with
\(s+1\) owner slots. Its lower/upper target grid contains
\(2s+1\) disjoint necessary certificate classes: one neutral class,
\(s\) left pin classes, and \(s\) right pin classes.

Consider pairwise owner-disjoint one-parity sectors indexed by \(I\).
Delete their \(\sum_I(s_I+1)\) baseline slots and \(C\) other old slots,
insert a word \(Z\), and put

\[
 E=|Z|-\sum_I(s_I+1)-C.
\tag{6.1}
\]

Choose one certificate position for every class. Let \(R\) be the number
assigned to unchanged exterior positions. For \(z\in Z\), let \(d_z\)
be the number assigned to \(z\), and put

\[
 \Sigma=\sum_{z\in Z}(d_z-1)_+.
\tag{6.2}
\]

### Theorem 6.1 (one-parity fusion-credit identity)

\[
 \boxed{E+C+R+\Sigma\ge\sum_I s_I.}
\tag{6.3}
\]

#### Proof

The number of required certificate assignments is

\[
 Q=\sum_I(2s_I+1).
\tag{6.4}
\]

The unchanged exterior supplies \(R\) of them, while

\[
 \sum_{z\in Z}d_z\le |Z|+\Sigma.
\tag{6.5}
\]

Therefore

\[
 \sum_I(2s_I+1)
 \le R+|Z|+\Sigma
 =R+E+C+\Sigma+\sum_I(s_I+1),
\tag{6.6}
\]

which rearranges to (6.3). \(\square\)

For \(\Theta(W/H)\) Gaussian sectors, the right side of (6.3) is
\(\Theta(W)\). Hence a one-parity hierarchy needs linear net excess,
linear collateral deletion, linear exterior export, or linear genuine
cross-sector sharing.

This theorem is sharp in scope and cannot be promoted to a two-parity
no-go. The second parity supplies exactly the missing linear collateral.
The two-core packet chart has circular length \(2s+3\) against
\(2s+2\) owner slots, as analyzed next.

## 7. Exact two-parity packet-chain criterion

Suppose, for each height \(s\), that \(t_s\) complete simple-return
packets are owner-occurrence-disjoint and form \(c_s\) literal chains with
matching ordered ports. The exact packet theorem gives word length

\[
 \sum_s\bigl[t_s(2s+3)+c_s(s-1)\bigr],
\tag{7.1}
\]

against baseline owner mass

\[
 M_0=\sum_s(2s+2)t_s.
\tag{7.2}
\]

Thus the excess is exactly (0.9).

Assume the family is nonempty, \(\alpha>0\) is fixed, and

\[
 \alpha H\le s\le H
\tag{7.3}
\]

for every selected packet, and put \(t=\sum_st_s\),
\(c=\sum_sc_s\). Then

\[
 2(\alpha H+1)t\le M_0\le2(H+1)t,
\tag{7.4}
\]

and

\[
 t+(\alpha H-1)c\le\Delta\le t+(H-1)c.
\tag{7.5}
\]

Dividing the lower numerator by the upper denominator, and conversely,
proves (0.10).

### Corollary 7.1 (necessary and sufficient packet fusion scale)

In the Gaussian regime \(H\to\infty\),

\[
 \boxed{\Delta=o(M_0)\quad\Longleftrightarrow\quad c=o(t).}
\tag{7.6}
\]

If every chain contains at most \(d\) packets, then \(c\ge t/d\) and

\[
 \liminf {\Delta\over M_0}\ge {\alpha\over2d}.
\tag{7.7}
\]

Thus uniformly bounded chain length (equivalently, bounded terminal packet
mass in this chain model) is linearly costly. Conversely, the normalized-
port type count is at most

\[
 2Hn^{H-1}=\exp(o(m))
\tag{7.8}
\]

for \(H=O(\sqrt m)\). If, in addition, equal normalized types in a supplied
owner-disjoint full phase deck can actually be concatenated into the
bounded number of literal chains per type used in the port-chain theorem,
then \(t=\Theta(W/H)\) implies \(c/t\to0\) and packet-interior excess
\(o(W)\).

Equation (7.8) is not a PBBS construction. Equal normalized ports omit
the two cores and boundary owners and do not imply a Johnson successor.
Adding the carrier and actual shared facet makes distinct maximal
fixed-carrier runs nonjoinable. Moreover the erosion replacement
provenance and every \(q\ge3\) crossing window remain unproved. Equation
(7.6) itself is unconditional under its stated packet-chain hypotheses;
only its applicability to the canonical critical family is conditional.

## 8. A genuine positive non-row-power class

The packet-chain criterion is not merely formal. There is an exact
cross-atlas family which realizes unbounded fusion.

Let \(P_i\) be pairwise owner-disjoint directed Johnson path pieces with
initial and terminal owners

\[
 Y_i=F\cup\{a_i\},\qquad X_i=F\cup\{b_i\},
\tag{8.1}
\]

where \(a_i\in\mathcal A\), \(b_i\in\mathcal B\), and
\(\mathcal A\cap\mathcal B=\varnothing\). Here \(|F|=m-1\),
\(F\cap(\mathcal A\cup\mathcal B)=\varnothing\), and
\(H+1\le m\). Assume each piece has no
positive residence of length at most \(H\), every insertion in its last
\(H\) edges lies in \(\mathcal A\), and every removal in its first
\(H\) edges lies in \(\mathcal B\).

### Theorem 8.1 (separated-star braid)

Every terminal owner \(F+b_i\) is Johnson-adjacent to every initial owner
\(F+a_j\), and every ordering of the pieces gives one path with no
positive residence of length at most \(H\). If the pieces have \(M\)
owners in total, their exact bridge-one word has length

\[
 \boxed{M+2H.}
\tag{8.2}
\]

#### Proof

The seam removes \(b_i\in\mathcal B\) and inserts
\(a_j\in\mathcal A\), so it is a nonlazy Johnson edge. A short positive
residence crossing a seam would have its insertion label in
\(\mathcal A\) and its removal label in \(\mathcal B\), impossible
because the alphabets are disjoint. Internal short residences are excluded
by hypothesis. The exact bridge-one residence theorem now gives the lift,
and its useful-prefix ledger is \(M+2H\). \(\square\)

This is a genuine non-row-power, exterior-moving, **one-sided
residence-safe** reordering. Its \(M+2H\) word represents the lower and
upper flags selected by the resulting bridge-one states. It does not prove
that the selected upper flags are the old PBBS chronological unions, nor
does it restore every old crossing target. Rainbow fixed-core PBBS rows
naturally supply the two insertion/removal alphabets. The unresolved
density theorem is the existence of enough shadow-twin pieces with the
common endpoint facet \(F\), together with a two-sided provider theorem
for the omitted old upper targets.

There is also an exact negative boundary. Inside one two-core packet atlas,
the induced Johnson graph is

\[
 C_{2s+1}\ \dot\cup\ C_{2s+1}
\tag{8.3}
\]

when the core has size at least two. For \(H\ge s\), an \(H\)-safe path
in either cycle has at most \(s+1\) owners. One physical packet therefore
needs at least two paths and pays at least \(4H\) bridge initialization.
Independent packet atlases have a constant relative toll. Thus a positive
hierarchy must use cross-atlas or moving-carrier chords of the kind in
Theorem 8.1; internal two-core moves cannot suffice.

Finally, the sliding-core model

\[
 X_i=G\cup\{a_i,a_{i+1},\ldots,a_{i+H-1}\}
\tag{8.4}
\]

has critically tiled residence intervals but admits a word of length
\(M+2H\): use the cyclic letters
\(E_i=G\cup\{a_i\}\), a \((2H-1)\)-letter linearization collar, and the
one additional set-letter \(G\). This gives a second exact counterexample
to any universal implication

\[
 \text{critical residence packing}
 \Longrightarrow \Omega(W)\text{ new letters}.
\tag{8.5}
\]

## 9. What the MSW trade hierarchy can and cannot do

Every certified MSW transposition-component switch replaces a row family
\(\mathcal L\) by \(\tau\mathcal L\). Coordinate relabelling sends the
positive run of \(x\) to the positive run of \(\tau x\) on the same cyclic
positions. Therefore

\[
 \boxed{\nu_H(\tau\mathcal L)=\nu_H(\mathcal L)}
\tag{9.1}
\]

for every \(H\). The same holds for a row-disjoint union of component
shores. More simply, every closed MSW row is already a wreath: its
omitted-label word is a permutation, and so every ordinary MSW exact factor
has

\[
 \nu_H=0\qquad(H\le m).
\tag{9.2}
\]

Thus the fixed MSW hierarchy transports shadow profiles inside the exact
wreath fibre; it is residence-isospectral and does not interpolate the
long PBBS components to wreaths. An active mixed PBBS/MSW mechanism must
replace PBBS residual paths, overlap/recompute component systems, or move
exteriors across parents.

For completeness, when \(1\le H\le m-2\), one isolated exact MSW
rectangle deletes two lower targets at depth one and four at each depth
\(2,\ldots,H\), with the complementary upper profile. Appending all
deleted occurrences separately emits

\[
 \boxed{8H-4}
\tag{9.3}
\]

target-occurrence letters per rectangle. At \(\Theta(W/H)\) active
rectangles this occurrence-by-occurrence strategy emits \(\Theta(W)\)
letters. This is an exact direct-restoration ledger, not a necessary
distinct-letter count or a universal lower bound: overlaps and a common
provider union may identify many deleted targets.

The exact lower-shadow boundary profile of one MSW \(C_8\) also gives

\[
 \|\Delta_1\|_1\le16,
 \qquad
 \|\Delta_q\|_1\le8q+12\quad(2\le q\le H),
\tag{9.4}
\]

and hence

\[
 \sum_{q=1}^H\|\Delta_q\|_1
 \le4H^2+16H-4.
\tag{9.5}
\]

The upper profile has the same bound. For \(C_{10}\) and \(C_{12}\),
the corresponding lower totals are at most

\[
 10H(H+1),\qquad 12H(H+1).
\tag{9.6}
\]

These are capacity ceilings, not favourable-sign theorems. In the fixed
MSW interaction cube the first-shadow increments are linearly independent,
so no nonempty simultaneous component selection is first-shadow invisible.
Among the audited libraries compared in this note, the localized rooted
pentagon is the only scalable non-row-power exact pair with genuine profile
transport, but its active carrier has fixed width nine; dense amplification
fuses \(5^k\)-row ownership components and loses independent signability.
None of these facts rules out a new correlated root-scale component.

## 10. Gaussian endpoint rethreading is independently necessary

The preceding trade bounds must be combined with the architecture-free
annulus theorem. Put

\[
 \rho_A={1\over2}e^{-A^2}.
\tag{10.1}
\]

Let \(h=o(\sqrt m)\), and suppose a word of length \(W+o(W)\) represents
the middle layer and every lower rank \(m-q\) for
\(h<q\le H\). Then at least

\[
 \boxed{{\rho_A\over8}W}
\tag{10.2}
\]

chosen middle witnesses have length at least

\[
 \boxed{{\rho_A\over3}(H-h).}
\tag{10.3}
\]

The reverse-word statement gives the same positive-density requirement for
upper right-endpoint flags. Therefore a successful non-row-power trade
cannot merely change \(\Theta(W/H)\) factor edges and retain the old
sub-Gaussian erosion witnesses elsewhere. It must use those sparse edits
to rethread a positive density of owner endpoints into heavily overlapping
Gaussian flags. The separated-star and sliding-core constructions show how
this can happen abstractly; no PBBS theorem supplies it at the required
density.

This also explains why factor-edit mass and new-letter mass have different
orders:

\[
 \Omega_{A,\varepsilon}(W/H)\text{ changed seams}
 \quad\hbox{must control}\quad
 \Theta(W)\text{ owner witnesses and }\Theta(HW)
 \text{ depth incidences}.
\tag{10.4}
\]

Only growing target multiplicity and common endpoint reuse can perform
that amplification at sublinear letter cost.

### Imported proved inputs and what is not re-proved here

All new deductions are proved where stated. The following
construction-specific, previously audited theorems are used as inputs
rather than silently re-proved:

* the critical long-cycle double-deck extraction from
  `MATH_AUDIT_CMS_AND_CRITICAL_RESIDENCE_SATURATION_20260726.md`;
* the exact spatial translate formula from
  `MATH_ATTACK_R_PBBS_DYCK_RESIDENCE_QUOTIENT_OBSTRUCTION_20260725.md`;
* the one-parity certificate lower bound, the two-parity packet chart, and
  the port-chain ledger from
  `MATH_ATTACK_K_PBBS_INPLACE_BASELINE_REPLACEMENT_AND_CROSSING_GATE_20260726.md`;
* the bridge-one residence theorem and separated-star construction from
  `MATH_ATTACK_W_PBBS_BRIDGE_ONE_RESIDENCE_BRAID_20260725.md`;
* the MSW all-rank rectangle profile from `MSW_MULTIRANK_LOCAL_TRADES.md`;
  and
* the endpoint-incidence annulus theorem from
  `MATH_THEOREM_GAUSSIAN_ANNULUS_LONG_ENDPOINT_RETHREADING_OBSTRUCTION_20260726.md`.

The clean-\(C_8\) count is used only as a candidate-reservoir count; no
claim here upgrades those candidates to a simultaneous exact wreath-factor
bank. The full PBBS/MSW braid stated below remains explicitly unproved.

## 11. Exact proved/conditional boundary

The following statements are proved.

1. Residence packing is \(2\)-Lipschitz in final odd-factor edge distance,
   uniformly in depth.
2. Failure of the audited long-cycle quotient gate forces
   \(\Omega_{A,\varepsilon}(W/H)\) final PBBS edge changes and
   \(\Omega_{A,\varepsilon}(W/H)\) alternating \(C_8\) switches.
3. The existing \(O(B)\) clean-\(C_8\) reservoir and every bounded number
   of Catalan rounds are asymptotically too small.
4. Under the stated admissibility, additivity, and clean-target hypotheses,
   every positive collar-plus-span hierarchy and every bounded-mass
   appended hierarchy pays \(\Omega_{A,\varepsilon}(W)\) on the critical long-sector
   family.
5. One-parity in-place replacement has the exact collateral/export/sharing
   inequality (6.3).
6. Complete two-parity packets defeat that one-parity obstruction, and
   their exact excess is governed by the chain ratio \(c/t\).
7. Separated-star cross-atlas braids prove unbounded one-sided path fusion,
   and sliding-core words prove that a full abstract unbounded-fusion
   escape is mathematically real.
8. Fixed MSW component switches are residence-isospectral; their local
   profile transport does not itself rebundle PBBS long components.

The following decisive statement is unproved.

> **PBBS/MSW hierarchical residence braid.** Construct one integral
> exact-factor or literal owner-path replacement which changes
> \(\Theta_{A,\varepsilon}(W/H)\) PBBS factor edges, hits every selected critical
> double-deck sector, and groups a diverging number of active seams per
> terminal component. Its common provider union must restore every lower
> and upper target through depth \(H\), including support-essential windows
> crossing the new packet boundaries, while using \(o_A(W)\) positions
> beyond a proved deletion of the old baseline.

For a final exact wreath factor the required fusion scale is visible
directly. There are exactly \(B\) output wreaths, while (2.6) requires
\(\Omega(B\sqrt m)\) removed old edges and therefore the same number of
new seams. The mean number of new seams per output wreath is
\(\Omega(\sqrt m)=\Omega_{A,\varepsilon}(H)\). This is the
required root-scale accumulation. It does not say that an individual local
switch has growing support: a successful hierarchy may accumulate bounded
switches, but their mean number per output wreath is
\(\Omega_{A,\varepsilon}(H)\). What is ruled out is
a bounded number of active seams per terminal output wreath on average.

Accordingly, the precise conclusion is

\[
 \boxed{
 \begin{array}{c}
 \text{bounded-mass appended or additive collar/span literalization}
 \Rightarrow\Omega(W)\text{ new letters};\\[2mm]
 \text{growing two-parity/exterior-moving fusion can have }o(W)
 \text{ excess};\\[2mm]
 \text{the required canonical PBBS all-depth braid remains open.}
 \end{array}}
\tag{11.1}
\]

No constant-one conclusion is claimed.
