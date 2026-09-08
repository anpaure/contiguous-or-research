# The three-top conveyor crosses ordered-core sectors, but its fixed-chart catalyst is not reusable at coefficient one

Date: 2026-07-27

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-H,\qquad c=2H,
 \qquad W=\binom{2m}{m}.
\tag{0.1}
\]

This note combines the maximal ordered-core invariant with the exact
three-top, two-base conveyor. The conclusions split sharply.

1. A conveyor whose three tops all contain a fixed \(2H\)-core \(K\)
   does not change the induced cyclic order on \(K\). Its common
   \((M-2)\)-core necessarily contains \(K\).

2. The conveyor does cross the ordered-core barrier as soon as it is
   allowed to leave the \(K\)-star. If its common core omits one label
   \(x\in K\), then two of its tops contain \(K\), the third does not,
   and the same insertion move of \(x\) is made at the two \(K\)-tops.
   If the common core omits two labels of \(K\), exactly one top may
   contain \(K\), and that top can undergo a single transposition.

3. On a maximal Boolean cell, a perfect matching of cube edges gives a
   squarefree layer of \(2^{d-1}\) conveyors. It changes one prescribed
   insertion of the ordered core at every cell top and uses
   \(2^{d-1}\) distinct outside catalyst tops. Its entire occurrence
   mass is

   \[
        \frac32 M2^d=o(W).
   \tag{0.2}
   \]

   Thus the ordered-core invariant is not a global invariant after the
   conveyor is admitted. Uniform ordered-core sectors of one maximal
   cell are connected modulo an explicitly listed \(o(W)\) boundary.

4. The outside top is not a reusable catalyst in one fixed squarefree
   chart. Modulo two, a conveyor is the incidence vector of a triangle

   \[
        xu+xv+uv.
   \tag{0.3}
   \]

   Here \(xu,xv\) are the two core-star owners and \(uv\) is the
   outside owner. If every outside owner is restored, then every
   triangle has been used evenly, and every star owner is restored as
   well. This is an exact relative invariant, not a counting heuristic.

5. Two oppositely routed conveyors do cancel the catalyst as an
   integer-table identity. But the resulting move has two source and
   two target frame columns at each of two star tops. It is therefore a
   top-margin-two binomial, not an applicable move in a coefficient-one
   owner transversal.

The remaining global gate is consequently precise. A positive-density
construction must move the catalyst between different common cores, or
recouple it through a genuinely squarefree higher template. The present
argument neither proves such moving-core connectivity nor gives an
\(\Omega(W)\) invariant against it.

## 1. The support classification relative to a fixed core

Let \(K\subset[n]\) have size \(2H\). Write the three conveyor tops as

\[
 U_{xy}=D\cup\{x,y\},\qquad
 U_{xa}=D\cup\{x,a\},\qquad
 U_{ay}=D\cup\{a,y\},
\tag{1.1}
\]

where \(|D|=M-2\) and \(x,a,y\notin D\) are distinct. Put

\[
                         B=K\setminus D.
\tag{1.2}
\]

A top \(D\cup e\), with \(e\in\{xy,xa,ay\}\), contains \(K\) if and
only if

\[
                         B\subseteq e.
\tag{1.3}
\]

This gives the complete classification.

### Proposition 1.1 (zero-, one-, and two-label crossings)

Assume at least one of the three tops in (1.1) contains \(K\).

1. If \(|B|=0\), all three tops contain \(K\). The conveyor fixes the
   induced order on \(K\) at every top.
2. If \(|B|=1\), exactly two tops contain \(K\). On both of them the
   unique label of \(B\) is one of the swapped placeholders.
3. If \(|B|=2\), exactly one top contains \(K\). Both labels of \(B\)
   are its swapped placeholders.
4. If \(|B|\ge3\), no touched top contains \(K\).

#### Proof

The number of two-subsets of \(\{x,a,y\}\) containing \(B\) is,
respectively, \(3,2,1,0\). If \(B=\varnothing\), every label of \(K\)
lies in the ordinary core \(D\), and the plus-to-minus change swaps only
the two noncore placeholders. Hence deletion of those placeholders
leaves the same cyclic order on \(K\). The other assertions follow
directly from (1.3). \(\square\)

In particular, the all-cube ordered-core invariant remains exact on
the face supported by

\[
 \mathcal S_K=\{U\in\tbinom{[n]}M:K\subseteq U\}.
\tag{1.4}
\]

Any conveyor wholly supported in this face has \(K\subseteq D\), since
\(D\) is the intersection of its three tops. Such a conveyor cannot
cross an ordered-core sector. Crossing is possible only by changing at
least one top outside (1.4).

## 2. The one-catalyst core insertion is literal

Suppose

\[
                         K\setminus D=\{x\},
\tag{2.1}
\]

and \(a,y\notin K\). Then \(U_{xy}\) and \(U_{xa}\) contain \(K\),
whereas \(U_{ay}\) does not.

Recall the two positional bases \(\omega,\omega'\) from the conveyor
theorem. Four inner arms of total size \(4H-4\) are permuted when one
passes from \(\omega\) to \(\omega'\). The four outer arms and the two
filler blocks remain in the same cyclic block order. Hence there are

\[
                         M-4H+2
\tag{2.2}
\]

ordinary positions whose induced order is common to the two bases after
the inner-arm labels are deleted. Under the standing conveyor hypothesis
\(M\ge8H\), this is more than enough to place all \(2H-1\) labels of
\(K\setminus\{x\}\).

### Lemma 2.1 (same transition at the two core tops)

Let \(\rho\) be a cyclic order on \(K\setminus\{x\}\), and choose two
insertion gaps of \(\rho\). The ordinary labels can be assigned to the
common positions of \(\omega,\omega'\) so that

\[
 \begin{aligned}
  \operatorname{ord}_K\omega^+(x,y)
    &=\operatorname{ord}_K(\omega')^+(x,a)=\rho_A,\\
  \operatorname{ord}_K\omega^-(x,y)
    &=\operatorname{ord}_K(\omega')^-(x,a)=\rho_B,
 \end{aligned}
\tag{2.3}
\]

where \(\rho_A\) and \(\rho_B\) are obtained by inserting \(x\) into
the two prescribed gaps.

#### Proof

After deletion of the four inner arms, the common positions occur in the
same cyclic order in both bases. Each of the two arcs from placeholder
\(A\) to placeholder \(B\) contains at least two outer arms and hence at
least \(2H\) common ordinary positions. Assign the labels of \(\rho\),
in order, to those positions, splitting them at the two desired gaps.
In the plus specialization \(x\) occupies \(A\), while in the minus
specialization it occupies \(B\). Deleting \(y\) or \(a\) gives (2.3).
\(\square\)

Thus a single legal squarefree conveyor changes the same ordered-core
insertion at two \(K\)-tops and stores the interface state at the one
top not containing \(K\). The ordered-core charge from the maximal-cell
theorem is therefore only a face invariant, not an invariant of the
enlarged global move graph.

## 3. A squarefree matching layer on a maximal Boolean cell

Partition the complement of \(K\) into pairs

\[
 [n]\setminus K=\bigsqcup_{j=1}^{d}\{b_{j,0},b_{j,1}\}
\tag{3.1}
\]

and let

\[
 \mathcal Q(K)=
 \left\{
 K\cup\{b_{j,\epsilon_j}:1\le j\le d\}:
 \epsilon\in\{0,1\}^d
 \right\}.
\tag{3.2}
\]

Fix \(x\in K\), fix a cube coordinate \(i\), and pair each
\(\epsilon\) with \(\epsilon\oplus e_i\). For one such edge set

\[
 D_\epsilon=
 (K\setminus\{x\})
 \cup
 \{b_{j,\epsilon_j}:j\ne i\}.
\tag{3.3}
\]

The two cell endpoints and the outside top are

\[
 \begin{aligned}
 U_{\epsilon,0}&=D_\epsilon\cup\{x,b_{i,0}\},\\
 U_{\epsilon,1}&=D_\epsilon\cup\{x,b_{i,1}\},\\
 C_\epsilon&=D_\epsilon\cup\{b_{i,0},b_{i,1}\}.
 \end{aligned}
\tag{3.4}
\]

### Theorem 3.1 (perfect-matching conveyor layer)

For any prescribed insertion move \(\rho_A\to\rho_B\) of one core
label \(x\), there is a simultaneous family of \(2^{d-1}\) legal
three-top conveyors such that:

1. every top of \(\mathcal Q(K)\) occurs exactly once;
2. its induced \(K\)-order changes from \(\rho_A\) to \(\rho_B\);
3. the outside tops \(C_\epsilon\) are pairwise distinct and disjoint
   from \(\mathcal Q(K)\); and
4. no owner is repeated anywhere in the layer.

#### Proof

Use Lemma 2.1 independently on every matched cube edge. The cube
matching makes the two cell tops disjoint between conveyors. Every
\(C_\epsilon\) omits \(x\), so it is outside \(\mathcal Q(K)\).

It remains only to check that the outside tops are distinct. From
\(C_\epsilon\) one recovers the unique pair index \(i\) for which both
pair labels occur, and for every \(j\ne i\) one recovers the selected
label \(b_{j,\epsilon_j}\). Thus \(C_\epsilon=C_{\epsilon'}\) implies
that the two matched cube edges are equal. No outside top equals a cell
top because the former omits \(x\) and the latter contains all of
\(K\). \(\square\)

The layer uses \(2^d\) cell owners and \(2^{d-1}\) outside owners. Its
promotion occurrence mass is at most

\[
                         \frac32 M2^d.
\tag{3.5}
\]

Since

\[
 \frac{M2^{m-H}}{W}
 =O\!\left(m^{3/2}2^{-m-H}\right)=o(1),
\tag{3.6}
\]

this is \(o(W)\). Consequently the conveyor crosses a complete uniform
ordered-core sector of one maximal Boolean cell with an explicitly
audited \(o(W)\) outside boundary. Since insertion moves generate the
symmetric group on \(K\), at most \(2H\) such layers connect any two
uniform core orders. Their union has mass
\(O(HM2^{m-H})=o(W)\). Thus all uniform ordered-core sectors are
connected after quotienting by changes on \(o(W)\) owner-occurrence
mass.

The last sentence is deliberately a modulo-exception statement. It is
not a claim that successive layers can use the same outside owners or
that their full frame states concatenate without an interface reset.

## 4. The exact fixed-chart catalyst invariant

We now test reuse rather than fresh boundary. Fix one common core \(D\),
one missing core label \(x\), and a set \(L\) of outside labels. Restrict
to conveyors on triples \(x,u,v\), with \(u,v\in L\), in one fixed
two-slot chart. Let

\[
 S_u=D\cup\{x,u\},\qquad
 C_{uv}=D\cup\{u,v\}.
\tag{4.1}
\]

The \(S_u\) are star owners and the \(C_{uv}\) are catalyst owners.
Record only whether the two placeholder labels have been swapped an odd
number of times. This gives one bit for every owner in (4.1). A conveyor
on \(x,u,v\) adds

\[
                         e_{S_u}+e_{S_v}+e_{C_{uv}}
\tag{4.2}
\]

over \(\mathbb F_2\).

### Theorem 4.1 (no closed squarefree catalyst in one chart)

For any sequence of fixed-chart conveyors, let \(t_{uv}\in\mathbb F_2\)
be the parity with which the support triangle \(xuv\) is used. Then

\[
 \Delta C_{uv}=t_{uv},\qquad
 \Delta S_u=\sum_{v\in L\setminus\{u\}}t_{uv}.
\tag{4.3}
\]

In particular,

\[
 \boxed{
  \Delta C_{uv}=0\ \hbox{for every }uv
  \quad\Longrightarrow\quad
  \Delta S_u=0\ \hbox{for every }u.}
\tag{4.4}
\]

Thus restoration of every catalyst owner forces restoration of the
core-insertion parity at every star owner.

#### Proof

The catalyst top \(C_{uv}\) occurs in exactly one support triangle with
fixed apex \(x\), namely \(xuv\). Hence its change bit is exactly
\(t_{uv}\). The star top \(S_u\) occurs in precisely the triangles
\(xuv\), giving the second identity. If all catalyst bits vanish, every
\(t_{uv}\) vanishes separately, and so do all star bits. \(\square\)

This invariant is stronger than an aggregate parity statement: each
outside edge is a private ledger entry for its triangle. It survives
arbitrary choices of the retained phase schedule, because it records
frame ownership before interval loads are projected.

Its scope is equally important. It assumes one fixed common core, one
fixed apex, and one two-slot chart. A conveyor with a different common
core can use a former catalyst top in a different role. Theorem 4.1 does
not forbid such moving-core transport.

## 5. Why the apparent two-conveyor cure has coefficient two

For a positional base \(\theta\), write

\[
 \delta_\theta(u,v)=
 e_{\theta^-(u,v)}-e_{\theta^+(u,v)}.
\tag{5.1}
\]

The conveyor routed directly from \(x\) to \(y\) and through \(a\) is

\[
 T(x;a,y)=
 \delta_\omega(x,y)+
 \delta_{\omega'}(x,a)+
 \delta_{\omega'}(a,y).
\tag{5.2}
\]

Interchanging the internal and terminal labels gives

\[
 T(x;y,a)=
 \delta_\omega(x,a)+
 \delta_{\omega'}(x,y)+
 \delta_{\omega'}(y,a).
\tag{5.3}
\]

Since \(\delta_\theta(y,a)=-\delta_\theta(a,y)\), their sum is

\[
 \boxed{
 T(x;a,y)+T(x;y,a)=
 \delta_\omega(x,y)+\delta_{\omega'}(x,y)
 +\delta_\omega(x,a)+\delta_{\omega'}(x,a).}
\tag{5.4}
\]

The catalyst top \(D\cup\{a,y\}\) has disappeared exactly. However, on
each of the two remaining tops, the negative shore contains both the
\(\omega\)-plus and \(\omega'\)-plus columns, and the positive shore
contains both corresponding minus columns. Each shore therefore has top
multiplicity two.

### Corollary 5.1 (formal catalyst versus reusable catalyst)

Equation (5.4) is a valid degree-four integer-table trade and can change
the induced order on \(K\) when the two placeholder gaps remain distinct
after restriction to \(K\). It is not applicable to a table with one
chosen frame per top.

Moreover it cannot be implemented sequentially by first applying (5.2)
and then (5.3). After (5.2), the frame on \(D\cup\{x,y\}\) is an
\(\omega\)-minus frame, while (5.3) requires an \(\omega'\)-plus source
there. The analogous mismatch occurs on \(D\cup\{x,a\}\). The algebraic
cancellation is exactly the multiplicity-two phenomenon detected by
Theorem 4.1.

At coefficient one, using (5.4) on a positive density of owners would
create a positive-density duplicate-owner excess. Thus (5.4) is not a
constant-one compiler primitive, even though it is a genuine element of
the unrestricted integer move lattice.

## 6. The surviving fixed-star invariant and its scale

If all intermediate supports are required to stay in the top star
\(\mathcal S_K\), then every higher placeholder cube has common core
containing \(K\), and so does every three-top conveyor. Hence the
cornerwise ordered-\(K\) histogram from the maximal-cell theorem remains
an exact invariant on that face, even after conveyors are added.

One can place the six-frame alternating core-order trade on every top of
\(\mathcal S_K\). The two shores have equal phasewise interval ledgers
and different ordered-core histograms. The size of this face is

\[
 |\mathcal S_K|=\binom{2m-2H}{m-H},
\tag{6.1}
\]

and

\[
 \frac{|\mathcal S_K|}{W}
 =4^{-H}\sqrt{\frac{m}{m-H}}\,(1+o(1)).
\tag{6.2}
\]

Thus its promotion mass is

\[
 3M\binom{2m-2H}{m-H}=O(M4^{-H}W)=o(W)
\tag{6.3}
\]

for growing \(H\). This is a genuine global face invariant, but it is
too small to force a coefficient-scale toll.

## 7. Exact boundary

Proved:

1. the complete support classification of a conveyor relative to a
   fixed \(2H\)-core;
2. an explicit one-catalyst move changing the same core insertion at
   two core-star tops;
3. a squarefree perfect-matching layer changing that insertion on every
   top of a maximal Boolean cell, with \(o(W)\) total boundary mass;
4. an exact mod-two private-edge invariant forbidding restoration and
   reuse of all catalysts in one fixed chart;
5. the exact two-conveyor cancellation and its unavoidable top
   multiplicity two; and
6. persistence, but only at \(o(W)\) scale, of the ordered-core
   obstruction on the fixed \(K\)-star face.

Not proved:

1. squarefree transport of a catalyst through changing common cores;
2. compatibility of many successive insertion layers without resetting
   their full frame states;
3. connectivity of the global one-frame-per-top all-depth fibre; or
4. an \(\Omega(W)\) invariant surviving all moving-core conveyors and
   higher placeholder cubes.

Therefore the three-top two-base conveyor is the first literal move in
the present library that crosses an ordered-core sector. It gives
maximal-cell connectivity modulo an audited \(o(W)\) boundary, but it
does not supply a reusable catalyst at coefficient one. The next exact
lemma is a moving-core catalyst-routing theorem with a squarefree owner
ledger; without that ledger, the formal cancellation (5.4) pays
coefficient two.
