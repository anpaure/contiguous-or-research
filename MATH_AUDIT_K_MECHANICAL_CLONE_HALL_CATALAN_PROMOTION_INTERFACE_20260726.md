# Mechanical clone Hall at the Catalan-to-promotion interface: exact capacities, star colours, and chronology obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.  This note does not repeat any Catalan component census.

## 0. Verdict

Put

\[
 V=[2m],\quad H=(1+o(1))\sqrt{m\log m},\quad
 {H^2\over m}=\log m+o(1),\quad M=m+H,\quad
 W=\binom{2m}{m},\quad
 N_H=\binom{2m}{m-H},
\tag{0.1}
\]

and assume the packing-side tuning

\[
 (M-1)N_H\le W,qquad MN_H=(1+o(1))W.
\tag{0.2}
\]

The mechanical clone-Hall theorem in
`MATH_THEOREM_GLOBAL_PROMOTION_MECHANICAL_ATLAS_AND_CLONE_HALL_20260726.md`
passes audit.  Its exact content is

\[
 \nu(\Gamma_0)
 =\sum_k\min(S_k^{(0)},B_k^{(0)})=W-o(W),
\tag{0.3}
\]

and, for every \(r=m-q\) with \(q=o(\sqrt m)\),

\[
 \nu(\Gamma_r)
 =\sum_k\min(S_k^{(r)},B_k^{(r)})=N_q-o(W).
\tag{0.4}
\]

Deleting one prescribed phase at every promotion root loses at most
\(N_H=o(W)\) from either matching.  These are integral clone matchings;
no fractional or floor gap remains at the ungrouped level.

The new positive Catalan interface is exact.  An anchored Catalan factor
has \(W\) primary owner occurrences, one for every middle target.  Compose
the inverse primary-owner bijection with a matching in \(\Gamma_0\).  This
gives a literal injection

\[
 \boxed{
  W-o(W)\text{ promotion phase clones}
  \longrightarrow
  W-o(W)\text{ distinct Catalan primary owner occurrences}.}
\tag{0.5}
\]

If clone \((A,i)\) is matched to middle target \(D\), then
\(A\subset D\), and \(J=D\setminus A\) is an actual consecutive
\(H\)-window in the restriction of the owner row to \(U=A^c\).  Thus
every matched clone has a literal one-phase Catalan chronology
certificate.

There are nevertheless two different notions of monochromaticity.

1. Give every middle target \(D\) the colour \(\kappa(D)\) of its unique
   Catalan ownership component.  Every clone edge incident with \(D\)
   then has the same colour.  Hence each promotion provider star is
   **exactly edge-monochromatic**.
2. A block-product promotion construction requires a colour on each
   promotion root \(A\), because all \(M-1\) phases of that root must be
   controlled jointly.  Edge monochromaticity does not supply such a
   root colouring: one root is incident with targets of many Catalan
   colours.

The exact root-colouring obstruction is the following deletion-decoding
functional.  Let \(\{E_\lambda\}\) be the Catalan primary-owner blocks,
and set

\[
 d_{A,\lambda}
 =|\{D\in E_\lambda:A\subset D\}|,
 \qquad L=\binom MH.
\tag{0.6}
\]

For a promotion-root colouring \(b(A)\), put

\[
 \operatorname {Err}(b)
 =\sum_A\bigl(L-d_{A,b(A)}\bigr)
 =\sum_D\left[\binom mH-
  |\{A\subset D:b(A)=\kappa(D)\}|\right].
\tag{0.7}
\]

The unconstrained optimum is exactly

\[
 \boxed{
 \mathfrak M(\kappa)
 =\sum_A\left(L-\max_\lambda d_{A,\lambda}\right).}
\tag{0.8}
\]

An independently selected Catalan-component controller with uniform
single-root frame marginals can have \(o(W)\) holes only if

\[
                         \boxed{\mathfrak M(\kappa)=o(W\binom mH).}
\tag{0.9}
\]

More generally, if component \(\lambda\) contains \(w_\lambda\) primary
owners and \(n_\lambda\) promotion roots are assigned its colour, target
simplicity forces the exact capacity inequality

\[
                         \boxed{(M-1)n_\lambda\le w_\lambda+o(W).}
\tag{0.10}
\]

Thus the authoritative coloured interface is a capacity-constrained
minimum-cost root assignment, with cost \(L-d_{A,\lambda}\), not the
uncoloured clone Hall problem.  No current Catalan theorem evaluates
(0.8) or its capacity-constrained version.

Finally, even (0.9)--(0.10) would not solve chronology.  Clone Hall
assigns phases independently.  A legal root deck \((J_i)\) must satisfy

\[
 |J_i\cap J_{i+1}|=H-1,
\qquad
 J_{i+1}\setminus J_i=J_{i+H}\setminus J_{i+H+1},
\tag{0.11}
\]

and the deletion labels must exhaust \(U\).  The unique Catalan owners of
the individually assigned \(D_i=A\cup J_i\) generally lie in unrelated
rows and impose none of (0.11).  One ambient row can certify at most
\(H+1\) phases of one promotion ring, so any Catalan inheritance needs at
least

\[
                 \boxed{\left\lceil{M-1\over H+1}\right\rceil
                         =\Omega(m/H)}
\tag{0.12}
\]

ambient row pieces per root, followed by a literal lag-\(H\) seam braid.
No such braid follows from clone Hall or from ownership-component
membership.

Therefore the new atlas yields a real positive advance but not a completed
construction:

\[
 \boxed{
 \begin{gathered}
 \text{Catalan primary ownership and mechanical clone Hall compose
 perfectly phase by phase;}\\
 \text{promotion-star root colouring and common cyclic chronology remain
 independent exact gates.}
 \end{gathered}}
\tag{0.13}
\]

Failure of (0.9), of the constrained capacity problem, or of the grouped
lag-\(H\) equations is a rigorous obstruction.  Passing the first two is
not sufficient without the third.

## 1. Audit of the mechanical clone capacities

Fix a balanced half \(P\in\binom Vm\).  A promotion root is
\(A\in\binom V{m-H}\), with top \(U=A^c\), \(|U|=M\).  Put

\[
                         t=|U\cap P|.
\tag{1.1}
\]

The mechanical binary word of length \(M\) and weight \(t\) has, at
every interval length \(s\), only the two weights

\[
 \left\lfloor{st\over M}\right\rfloor,qquad
 \left\lceil{st\over M}\right\rceil.
\tag{1.2}
\]

The number of roots of type \(t\) is exactly

\[
                         n_t=\binom mt\binom m{t-H}.
\tag{1.3}
\]

For the middle, let \(S_k^{(0)}\) be the number of root-phase clones
whose mechanical \(H\)-window produces \(P\)-profile \(k\).  For direct
entrance length \(r\), define \(S_k^{(r)}\) similarly.  The target counts
are

\[
 B_k^{(0)}=\binom mk^2,qquad
 B_k^{(r)}=\binom mk\binom m{r-k}.
\tag{1.4}
\]

The audited mechanical-profile theorem gives

\[
 \sum_k|S_k^{(0)}-B_k^{(0)}|=o(W),
 \qquad
 \sum_k|S_k^{(r)}-B_k^{(r)}|=o(W).
\tag{1.5}
\]

Now fix one source type, one phase, and one target profile.  The action of
\(S_P\times S_{P^c}\) is transitive on both shores of the corresponding
clone-target cell and preserves adjacency.  Hence the cell is biregular.
Normalize its edges so that every left clone has fractional degree one.
After all cells of profile \(k\) are superposed, every right target has
fractional degree \(S_k/B_k\).  If \(S_k\le B_k\), this saturates the
left; if \(S_k\ge B_k\), multiply all weights by \(B_k/S_k\) and
saturate the right.  Thus there is a fractional matching of size
\(\min(S_k,B_k)\).

The bipartite matching polytope is integral, and different profiles have
disjoint vertices.  Therefore

\[
 \nu(\Gamma)=\sum_k\min(S_k,B_k)
 ={1\over2}\left(\sum_kS_k+\sum_kB_k-sum_k|S_k-B_k|\right),
\tag{1.6}
\]

which proves (0.3)--(0.4).  Removing one phase clone at each root removes
\(N_H\) left vertices and can lower a maximum matching by at most
\(N_H\).  No grouping, acyclicity, or common-order claim is used in this
argument.

There is also a marginal-scope distinction.  With \(P\) fixed, a uniform
labelling of the mechanical binary pattern is not the uniform law on all
cyclic frames; it is supported on frames whose every \(P\)-interval count
is mechanically balanced.  A full coordinate symmetrization of the
entire atlas can make the one-root marginal uniform by transitivity, but
the same global conjugation acts on every root and on the Catalan owner
partition.  It therefore creates global dependence rather than an
independent-root rounding.  The block-factor theorem may be invoked only
after this distinction is respected.

## 2. Exact phasewise Catalan lift

Rotate every anchored Catalan factor row at infinity and delete infinity.
For row \(x\), let

\[
                         P_{x,j},\qquad1\le j\le m+1,
\tag{2.1}
\]

be its nonwrapping length-\(m\) primary intervals.  Exact factor ownership
gives the bijection

\[
 \boxed{
 (x,j)\longmapsto P_{x,j}quad	ext{from the \(W\) primary occurrences
 onto }\binom Vm.}
\tag{2.2}
\]

Let \(\mathcal M\) be a matching in \(\Gamma_0\).  If
\((A,i)D\in\mathcal M\), assign clone \((A,i)\) the unique primary
occurrence \((x(D),j(D))\) from (2.2).  Matching on the right makes these
occurrences distinct, proving (0.5).  If the promotion-ring convention
names the literal middle owner by \(D^c\) rather than \(D\), apply the
same construction after the global complement bijection; none of the
counts or injectivity statements changes.

There is also a literal one-phase chronology statement.

### Lemma 2.1 (restriction certificate)

Let \(D\) be a cyclic length-\(m\) interval of an ambient order \(\pi\),
let \(A\subset D\) have size \(m-H\), and put \(U=V\setminus A\).  Then

\[
                         J=D\setminus A
\tag{2.3}
\]

is a cyclic length-\(H\) interval of the restricted order \(\pi|_U\).

#### Proof

Along the ambient interval representing \(D\), every label belongs to
\(D\).  Deleting the labels of \(A\) leaves precisely the labels of
\(J\), with no label of \(U\setminus J\) between them.  Hence they are
consecutive in the induced cyclic order on \(U\). \(\square\)

For a mechanical clone edge, the \(P\)-count of \(J\) equals the binary
weight prescribed at phase \(i\).  Therefore one may also place the
labels of \(J\) in that mechanical interval and the other labels in the
remaining positions, respecting the two \(P/P^c\) classes.  This proves
existence of a mechanical one-phase realization.  The restricted owner
order and this mechanical realization need not agree away from that
phase.  Conflating them would be the first false completion step.

## 3. Edge colours versus promotion-root blocks

Let \(\{E_\lambda\}\) be the partition of middle targets induced by any
completed Catalan ownership-component decomposition, and write

\[
                         \kappa(D)=\lambda
                 \quad\Longleftrightarrow\quad D\in E_\lambda.
\tag{3.1}
\]

Every clone edge ending at \(D\) inherits \(\kappa(D)\).  Thus every
edge which the fixed mechanical atlas actually places over the abstract
provider star of \(D\) has the same colour.  Moreover the entire abstract
incidence star \(\{(A,D):A\subset D\}\) can be labelled by
\(\kappa(D)\), independently of whether a particular fixed-\(P\) clone
edge is present.  This is an exact improvement over a coordinate-orbit
transport, where one component met a provider star in only a negligible
number of roots.  It does not say that a fixed mechanical pattern makes
\(D\) adjacent to a clone over every one of its \(R\) roots.

It is not yet the monochromaticity required by the block-factor theorem.
That theorem partitions the *root variables*.  Choose a root colouring

\[
                         b:\binom V{m-H}\to\Lambda.
\tag{3.2}
\]

For target \(D\), the number of providers lying in its intended block is

\[
                         g_D(b)
 =|\{A\subset D:b(A)=\kappa(D)\}|.
\tag{3.3}
\]

Double counting the incident pairs \((A,D)\) gives (0.7).  In particular,

\[
 \sum_D(R-g_D(b))=o(WR)
\tag{3.4}
\]

if and only if, for every fixed \(\eta>0\), all but \(o(W)\) targets
satisfy

\[
                         g_D(b)>(1-\eta)R.
\tag{3.5}
\]

The forward implication is Markov's inequality; the reverse follows by
first fixing \(\eta\), bounding every exceptional target by \(R\), and
then diagonalizing \(\eta\downarrow0\).

For each root \(A\), the choice minimizing its contribution to (0.7) is
any \(\lambda\) maximizing \(d_{A,\lambda}\).  This proves (0.8).

Suppose now that blocks are independently randomized with uniform
single-root cyclic-frame marginals.  If a fixed positive fraction of
targets has \(g_D(b)\le(1-\eta)R\), the targetwise block-factor proof
gives a positive lower bound on its miss probability and hence
\(\Omega(W)\) expected holes.  Therefore (0.9) is necessary.

The target-capacity condition is independent.  If \(n_\lambda\) roots
are assigned colour \(\lambda\), their repaired decks contain
\((M-1)n_\lambda\) phase occurrences.  If all but \(o(W)\) of these are
to use distinct targets of \(E_\lambda\), then (0.10) follows.  With hard
zero cross-colour error the exact inequality is

\[
                         (M-1)n_\lambda\le w_\lambda.
\tag{3.6}
\]

Consequently the exact scalar relaxation is the finite transportation
problem

\[
 \min_b\sum_A(L-d_{A,b(A)})
 \quad\text{subject to}\quad
 (M-1)|b^{-1}(\lambda)|\le w_\lambda+e_\lambda,
 \quad\sum_\lambda e_\lambda=o(W).
\tag{3.7}
\]

The uncoloured clone matching proves neither feasibility nor infeasibility
of (3.7), because the Catalan colour classes are not unions of the
\(S_P\times S_{P^c}\)-biregular profile cells used in its proof.

Near-monochromaticity and capacity together actually force the root
quotas.  Put

\[
                         \bar n_\lambda={N_H\over W}w_\lambda.
\tag{3.8}
\]

If (3.4) holds and the total cross-colour/repeat allowance in (0.10) is
\(o(W)\), then

\[
                         \boxed{
 \sum_\lambda|n_\lambda-\bar n_\lambda|=o(N_H).}
\tag{3.9}
\]

Indeed, write

\[
 G_\lambda=\sum_{A:b(A)=\lambda}d_{A,\lambda}
           =\sum_{D\in E_\lambda}g_D(b).
\tag{3.10}
\]

Then \(G_\lambda\le n_\lambda L\), while

\[
 \sum_\lambda(w_\lambda R-G_\lambda)
 =\operatorname {Err}(b)=o(WR).
\tag{3.11}
\]

Using \(R/L=N_H/W\) gives the lower quota up to total \(o(N_H)\).
The capacity upper bound gives

\[
 n_\lambda\le{w_\lambda+e_\lambda\over M-1}.
\tag{3.12}
\]

After summing, the difference between this upper normalization and
\(\bar n_\lambda\) is

\[
 {W-(M-1)N_H\over M-1}+o(N_H)=o(N_H),
\tag{3.13}
\]

which proves (3.9).  Thus a successful monochromatic controller has no
macroscopic freedom in how many promotion roots each Catalan owner block
receives.

## 4. Exact chronology gate

For one promotion root \(A\), write its assigned middle targets as

\[
                         D_i=A\cup J_i,qquad |J_i|=H.
\tag{4.1}
\]

They arise from one cyclic order on \(U=A^c\) if and only if, after the
one missing phase is restored, consecutive windows satisfy

\[
 |J_i\cap J_{i+1}|=H-1,
\tag{4.2}
\]

the deleted labels \(x_i\in J_i\setminus J_{i+1}\) are all distinct, and

\[
                         J_{i+1}\setminus J_i=\{x_{i+H}\}.
\tag{4.3}
\]

Equivalently, (0.11) holds and the singleton deletion labels exhaust
\(U\).  These conditions are necessary and sufficient: a label \(x_j\)
is inserted at transition \(j-H\), deleted at transition \(j\), and
therefore occupies exactly the \(H\) consecutive windows ending at
\(j\).

Clone Hall constrains each \(J_i\) only by its size and its mechanical
\(P\)-count.  It does not impose (4.2)--(4.3).  The relaxation is strict
inside every typical root type: starting from a legal mechanical deck,
replace one inserted label by a different unused label in the same
\(P/P^c\) class.  The modified phase remains adjacent to its individual
clone but violates (4.3).  Thus integrality of the bipartite clone
matching polytope does not imply integrality of the grouped frame polytope.

Composing with the Catalan primary-owner bijection does not change this.
The owners of \(D_i\) and \(D_{i+1}\) may lie in unrelated ambient rows.
Lemma 2.1 certifies each \(J_i\) separately but supplies no equality
between the label inserted at phase \(i\) and the label deleted at phase
\(i+H\).

There is an exact lower bound on any attempt to inherit one ring from
ambient row chronologies.

### Lemma 4.1 (ambient-row piece lower bound)

Fix an ambient cyclic order \(\pi\) on \(V\) and a promotion top
\(U\subset V\) of size \(M\).  At most \(H+1\) cyclic length-\(m\)
windows of \(\pi|_U\) are also cyclic length-\(m\) windows of \(\pi\).

#### Proof

Decompose the labels of \(U\) into maximal runs in \(\pi\).  A common
length-\(m\) window must lie in one run.  Since \(|U|=m+H<2m\), at most
one run has length at least \(m\).  A run of length \(s\le m+H\)
contains at most \(s-m+1\le H+1\) such windows. \(\square\)

A repaired promotion ring uses \(M-1\) phases.  Covering its phase targets
by ambient Catalan owner rows therefore needs at least (0.12) row pieces.
Indeed the complement in \(V\) of a promotion target
\(D=A\cup J\) is the length-\(m\) window \(U\setminus J\) of the
restricted order, while the complement of an ambient primary owner is
the antipodal ambient length-\(m\) window.  Lemma 4.1 therefore applies
to the promotion phases after complementation.
At every change of row, equations (4.2)--(4.3) impose the same common
lag-\(H\) labels across the seam.  Neither component membership nor
phasewise clone matching supplies these seam equalities.

Once a legal middle order is fixed, every entrance interval is forced:

\[
                         S_i=\{x_i,x_{i+1},\ldots,x_{i+r-1}\}.
\tag{4.4}
\]

Hence the separately proved entrance clone matching cannot be chosen
independently either.  It is only a capacity certificate for the targets
which the final common orders must cover.

## 5. Positive construction and obstruction boundary

The following positive statements are now proved.

1. The mechanical support has the correct simultaneous middle and
   sub-Gaussian entrance profiles.
2. It admits integral near-perfect middle and entrance clone matchings.
3. The middle clone matching lifts canonically to distinct Catalan primary
   owner occurrences, giving (0.5).
4. Every lifted edge has a literal restricted-row \(H\)-window
   certificate.
5. Catalan ownership colours make every target provider star exactly
   monochromatic at the edge level.

The following are rigorous obstruction tests.

1. If the minimum in (0.8), or its capacity-constrained version (3.7),
   is not \(o(WR)\), then no Catalan-component block-product controller
   with uniform root marginals can have \(o(W)\) middle holes.
2. Even if that test passes, a clone assignment which violates
   (4.2)--(4.3) is not a literal promotion frame selection.
3. Any ambient-row inheritance must use \(\Omega(m/H)\) pieces per ring
   and prove all corresponding lag-\(H\) seam identities.

No present theorem evaluates the coloured deletion-decoding functional,
constructs the capacity-constrained root colouring, or groups the clone
matching into common cyclic orders.  Thus the mechanical atlas crosses
the former raw Hall barrier but stops exactly at a two-part interface:

\[
 \boxed{
 \begin{gathered}
 \text{near-monochromatic promotion-root assignment with Catalan owner
 capacities,}\\
 \text{followed by a globally correlated lag-\(H\) permutation coupling.}
 \end{gathered}}
\tag{5.1}
\]

This is sharper than the earlier component-cardinality question.  It
identifies an actual positive phasewise lift and the first two exact
conditions which prevent that lift from being a completed factor.
