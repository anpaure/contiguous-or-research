# Catalan many local hexagons cannot repair the canonical marked-gap shadow

**Date:** 2026-08-21  
**Method:** pure mathematics; the finite checker is an audit only  
**Status:** unconditional local-switch obstruction, with an exact all-depth
footprint bound

## 0. Outcome

Put

\[
 b=2r+1,\qquad
 \Omega_r=\binom{[b]}r,\qquad
 A_r=|\Omega_r|,\qquad
 C_r=\operatorname {Cat}_r={A_r\over b}.
\tag{0.1}
\]

Let \(F_r^{\rm can}\) be the canonical MSW \(C_b\)-factor of the odd graph
\(O_r=KG(b,r)\).  The already proved marked-gap theorem supplies

\[
 K_r=(2r-3)C_{r-2}
\tag{0.2}
\]

pairs of equal first-shadow occurrences, with no occurrence used in two
pairs.  This note does not reprove that theorem.  It determines exactly how
many of those certificates a local hexagon trade can even touch.

There are two common hexagon conventions.

* A factor-alternating \(C_6\) toggled directly in the odd graph changes the
  two factor neighbours of at most six odd-graph vertices.  It can therefore
  invalidate at most six marked-gap pairs.
* A factor-alternating \(C_6\) in the bipartite Middle-Levels incidence lift
  changes exactly three projected tight-edge slots after the upper shore is
  suppressed.  It can therefore invalidate at most three marked-gap pairs.

Consequently, after \(T\) local hexagons, the final first-shadow hole count
obeys

\[
 \boxed{
 h_1(F_T)\ge
 K_r-sT-{2A_r\over r+2},
 \qquad
 s=6\ \hbox{(direct odd)},\quad
 s=3\ \hbox{(projected incidence)}.}
\tag{0.3}
\]

This holds whenever the final object is a spanning odd-graph two-factor; in
particular it holds when every intermediate object and the final object are
\(C_b\)-factors.  Factor-preservation only removes candidate trades and
cannot weaken (0.3).

Since

\[
 {K_r\over A_r}
 ={r(r+1)\over4(2r-1)(2r+1)}
 \longrightarrow {1\over16},
\tag{0.4}
\]

every bank of \(T=O(C_r)=O(A_r/r)\) hexagons leaves

\[
                         h_1(F_T)\ge(1/16-o(1))A_r.
\tag{0.5}
\]

Thus Catalan many pairwise disjoint MNW-type hexagons cannot reduce the
canonical \(q=1\) holes to \(o(A_r)\).  Disjointness is irrelevant to this
negative conclusion.  Any such repair needs at least

\[
 T\ge
 \begin{cases}
  (1/96-o(1))A_r,&\text{direct odd hexagons},\\
  (1/48-o(1))A_r,&\text{incidence hexagons},
 \end{cases}
\tag{0.6}
\]

so it needs \(\Omega(rC_r)\), not merely \(O(C_r)\), bounded local trades.

One switch nevertheless has controlled shallow damage.  At depth \(q\), a
direct odd hexagon changes at most \(6q\) old and \(6q\) new every-second
slots; an incidence hexagon changes at most \(3q\) old and \(3q\) new
projected slots.  Hence one switch has aggregate footprint \(O(H^2)\)
through all \(q\le H\).  The obstruction is supply, not locality of one
move.

## 1. Exact every-second slot formula

Every \(C_b\) in \(O_r\) is a wreath.  If its omitted-label word is

\[
                         a=(a_0,\ldots,a_{b-1}),
\]

then, with indices modulo \(b\), its vertices may be written

\[
 V_i=\{a_{i+1},a_{i+3},\ldots,a_{i+2r-1}\}.
\tag{1.1}
\]

For \(1\le q\le r-1\), the lower depth-\(q\) slot on the unoriented
\(2q\)-edge segment from \(V_{i-2q}\) to \(V_i\) is

\[
 \begin{aligned}
 L_{i,q}
   &=\bigcap_{j=0}^{q}V_{i-2j}\\
   &=\{a_{i+1},a_{i+3},\ldots,a_{i+2r-2q-1}\},
 \end{aligned}
\tag{1.2}
\]

and therefore \(|L_{i,q}|=r-q\).  Reversing the segment leaves the
intersection unchanged.  Its complement is the corresponding upper target
of rank \(r+q+1\).  Thus each \(C_b\) has exactly \(b\) unoriented slots at
every depth, and a spanning \(C_b\)-factor has exactly \(A_r\) slots.

At \(q=1\), a slot has the orientation-free local form

\[
                         L_F(v)=x\cap y,
\tag{1.3}
\]

where \(x,y\) are the two factor neighbours of its centre \(v\).  Since
\(x,y\) are distinct \(r\)-subsets of the \((r+1)\)-set \([b]\setminus v\),
this is always an \((r-1)\)-set.  Formula (1.3) remains valid for every
spanning two-factor of \(O_r\), even if its component lengths are not \(b\).

## 2. Direct odd-graph hexagons

Let \(F\) be a spanning two-factor of \(O_r\), let \(Z\cong C_6\) alternate
between three edges of \(F\) and three edges outside \(F\), and put

\[
                         F'=F\mathbin\triangle E(Z).
\tag{2.1}
\]

Then \(F'\) is again a spanning two-factor.  Call the switch
**wreath-legal** when \(F'\) is again a \(C_b\)-factor.

### Lemma 2.1 (six first-shadow slots)

The first-shadow occurrence at a vertex outside \(V(Z)\) is identical in
\(F\) and \(F'\).  Hence a direct odd-graph hexagon changes at most six
first-shadow occurrences, fills at most six old holes, and destroys at most
six old marked-gap certificates.

#### Proof

Every vertex of \(Z\) loses one incident factor edge and gains one incident
factor edge.  No factor edge incident with a vertex outside \(V(Z)\) changes.
The assertion follows immediately from the local formula (1.3).  A marked
certificate is destroyed only if at least one of its two occurrence slots
changes.  Since the marked-gap theorem uses every occurrence in at most one
certificate, six changed occurrences destroy at most six certificates.
\(\square\)

### Lemma 2.2 (exact \(q\)-collar bound)

Assume that both \(F\) and \(F'\) are \(C_b\)-factors.  At depth \(q\),
\(1\le q\le r-1\), at most \(6q\) old slots disappear and at most \(6q\)
new slots appear.  Consequently

\[
 \begin{aligned}
 \#\{\text{newly covered lower targets}\}&\le6q,\\
 \#\{\text{newly missing lower targets}\}&\le6q,
 \end{aligned}
\tag{2.2}
\]

and the same bounds hold on the complementary upper shore.  The
\(\ell^1\)-distance of either target-load histogram is at most \(12q\).

#### Proof

An old \(2q\)-edge segment survives literally in \(F'\) unless it contains
one of the three removed edges.  On a \(b\)-cycle, with \(2q<b\), a fixed
edge lies in exactly \(2q\) such segments.  The union bound gives at most
\(3(2q)=6q\) disappearing old slots.  Apply the same argument to the three
inserted edges in \(F'\).  Common segments have the same intersection
target by (1.2).  The support and histogram claims follow. \(\square\)

In particular, for one direct hexagon,

\[
 \sum_{q=1}^{H}\#\{\text{disappearing old slots at depth }q\}
 \le3H(H+1),
\tag{2.3}
\]

and the same bound holds for new slots and separately for the complementary
upper shore.

## 3. Incidence-hexagon convention

Let \(\widetilde F\) be a spanning two-factor of the bipartite incidence
graph between ranks \(r\) and \(r+1\).  Suppress every upper vertex: its two
lower factor neighbours become one labelled projected transition.  Let
\(Z\cong C_6\) be factor-alternating in this bipartite graph.

### Lemma 3.1 (three projected slots)

Toggling \(Z\) replaces exactly the three projected transitions labelled by
the three upper vertices of \(Z\), and no others.  At projected depth \(q\),
at most \(3q\) old and \(3q\) new windows change.

#### Proof

At each upper vertex of \(Z\), one selected incidence edge is removed and
the other hexagon edge is inserted; its other selected incidence edge is
unchanged.  Thus its suppressed lower-neighbour pair changes.  The
neighbour pair of every upper vertex outside \(Z\) is unchanged.  This gives
three changed projected transitions.  A fixed projected transition lies in
exactly \(q\) cyclic \(q\)-transition windows, so the window bound is
\(3q\). \(\square\)

When the incidence factor is the lift of an odd \(C_b\)-factor, these are
the tight every-second slots.  A single incidence hexagon need not preserve
the lift symmetry or the \(C_b\)-component condition.  If a proposed repair
uses only those hexagons, paired hexagons, or compound trades whose final
projection again encodes a \(C_b\)-factor, Lemma 3.1 still bounds its local
footprint.  A lift-symmetric pair of incidence hexagons has the conservative
direct-odd constants \(6q\) and six certificates.

## 4. The certificate-cover trade hypergraph

Let \(\mathcal M_r\) be the marked-gap family from (0.2).  Its vertices are
collision certificates, not factor vertices.  For every proposed local
trade \(\tau\), let \(S(\tau)\) be the set of **canonical first-shadow
occurrence slots** whose local rule is touched by the trade, and make the
hyperedge

\[
 E_\tau
 =\{P\in\mathcal M_r:
      \text{one of the two occurrence slots of }P\text{ lies in }S(\tau)\}.
\tag{4.1}
\]

Because the pairs in \(\mathcal M_r\) use disjoint occurrence slots,

\[
                         |E_\tau|\le |S(\tau)|.
\tag{4.2}
\]

Thus direct odd hexagons give a \(6\)-bounded cover hypergraph and incidence
hexagons give a \(3\)-bounded cover hypergraph.

This is the smallest necessary local relaxation of the repair problem: it
forgets edge conflicts, switch interference, signs of target changes, and
the global requirement that every final component have length \(b\).  It
even credits a certificate as killed whenever merely one of its slots is
touched.  Every genuine factor-preserving repair is therefore a feasible
selection only after satisfying strictly more constraints.

For a dynamic switch sequence, use the same static hypergraph on the
original canonical occurrence slots.  A switch can newly touch at most
\(s\) of those slots, so \(T\) switches cover at most \(sT\) certificates,
even if later switches overlap earlier ones or the intermediate factors are
chosen adaptively.

## 5. Exact surviving-certificate ledger

Let \(U_T\) be the number of original marked-gap certificates none of whose
two occurrence slots was touched.  Sections 2--4 give

\[
                         U_T\ge K_r-sT.
\tag{5.1}
\]

Every such certificate remains a pair of equal occurrences in the final
first-shadow histogram.  If \(\mu(S)\) is the final multiplicity of an
\((r-1)\)-target, its duplicate excess satisfies

\[
 U_T
 \le\sum_S\left\lfloor{\mu(S)\over2}\right\rfloor
 \le\sum_S(\mu(S)-1)_+.
\tag{5.2}
\]

There are \(A_r\) occurrence slots and

\[
 N_r=\binom{2r+1}{r-1}={r\over r+2}A_r
\tag{5.3}
\]

possible targets.  If \(h_1(F_T)\) are missing, exact counting gives

\[
 \sum_S(\mu(S)-1)_+
   =A_r-(N_r-h_1(F_T))
   ={2A_r\over r+2}+h_1(F_T).
\tag{5.4}
\]

Combining (5.1)--(5.4) proves (0.3).  Substituting (0.4) and
\(C_r=A_r/(2r+1)\) proves (0.5)--(0.6).

## 6. Scope

This theorem is a sharply local no-go.

* It rules out \(O(C_r)\) bounded hexagon trades as a repair of the
  canonical marked-gap defect, even if every trade is chosen optimally and
  all compatibility and \(C_b\)-factor constraints happen to be soluble.
* It does not rule out \(\Theta(A_r)\) local trades, longer trades touching
  \(\Theta(r)\) slots each, or a genuinely global replacement of the
  canonical factor.
* The \(O(H^2)\) one-switch footprint is an upper bound on collateral slot
  changes.  It does not assert favorable signs, target novelty, or
  cancellation among many switches.
* The theorem concerns the local wreath/interval palette.  It makes no
  endpoint-disjoint matching, labelled factor-order coinstantiation, or
  physical universal-word claim.

The marked-gap input is exactly the already frozen result in
`MATH_ATTACK_A_PHASE_ONE_MULTIDEPTH_SHADOW_BARRIER_20260725.md` and
`MATH_THEOREM_MSW_Q1_INVERSE_AND_SQRT_BOUND_20260725.md`.  The new content
here is the certificate-cover reduction, the \(3/6\)-slot convention split,
and the resulting \(\Omega(A_r)\) local-switch lower bound.
