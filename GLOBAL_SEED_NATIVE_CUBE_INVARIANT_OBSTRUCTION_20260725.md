# A mixed-seed obstruction throughout the entire native MSW switch cube

Date: 2026-07-25

Method: pure mathematics only. No search, computation, solver, or external
black box is used.

## 0. Outcome

Let

\[
 n=2m+1,\qquad t=\operatorname{Cat}_m,
\]

let \(F_m^{\rm MSW}\) be the canonical exact factor, let
\(\tau=(2\ 3)\), and let \(\mathcal Q_{\tau,m}\) be the entire exact-factor
cube obtained by choosing independently, in every interaction component
between \(F_m^{\rm MSW}\) and \(\tau F_m^{\rm MSW}\), either its canonical
side or its transposed side.

Define

\[
 C(z)=\sum_{m\ge0}\operatorname{Cat}_mz^m,
 \tag{0.1}
\]

\[
 M(z)
 =
 \frac{z^4C(z)}
 {1-(1+z^2)\bigl(zC(z)-z^2-2z^4\bigr)-2z^6},
 \tag{0.2}
\]

and

\[
 H(z)
 =
 \sum_{p\ge3}
 \bigl(\operatorname{Cat}_{p-1}-\operatorname{Cat}_{p-2}\bigr)z^p
 =
 z(1-z)(C(z)-1)-z^2.
 \tag{0.3}
\]

Put

\[
 \boxed{
  J(z)=z^5C(z)+H(z)M(z)
      =\sum_{m\ge0}J_mz^m.
 }
 \tag{0.4}
\]

Then for **every** exact cube child \(G\in\mathcal Q_{\tau,m}\), every
balanced quota system containing depth one satisfies

\[
 \boxed{
  \vartheta(G,\beta)\ge J_m.
 }
 \tag{0.5}
\]

More robustly, for every exact factor \(F\),

\[
 \boxed{
  \vartheta(F,\beta)
  +d(F,\mathcal Q_{\tau,m})
  \ge J_m,
 }
 \tag{0.6}
\]

where

\[
 d(F,\mathcal Q_{\tau,m})
 =\min_{G\in\mathcal Q_{\tau,m}}d(F,G).
\]

The exact asymptotic density is

\[
 \boxed{
  \frac{J_m}{\operatorname{Cat}_m}
  \longrightarrow
  \delta_{\rm inv}
  :=
  \frac{107897}{19784704}
  \approx0.00545.
 }
 \tag{0.7}
\]

Therefore every factor satisfying \((\mathrm{FSP}_A)\) must lie at row
distance

\[
 \bigl(\delta_{\rm inv}-o(1)\bigr)t
\]

from the **entire** native component-switch cube, not merely from the
canonical factor.

By coordinate relabelling, the same conclusion holds for every conjugate
cube \(\sigma\mathcal Q_{\tau,m}\).  Thus an FSP candidate must stay
positive-density far from every one-transposition canonical switch cube.

This is the requested compensating-seed inequality.  Component switching
can mix the old and transposed owners, but a positive-density family of
targets is \(\tau\)-invariant, so every mixed triple remains a packet.

## 1. The invariant-target principle

### Lemma 1.1 -- mixed owners survive an invariant target

Let \(S\) be a depth-one target satisfying

\[
 \tau S=S.
 \tag{1.1}
\]

Suppose distinct canonical rows \(E_1,E_2,E_3\) all own \(S\).  In an
arbitrary child \(G\in\mathcal Q_{\tau,m}\), replace each \(E_i\) by the row
selected from its interaction component:

\[
 E_i'\in\{E_i,\tau E_i\}.
\]

Then \(E_1',E_2',E_3'\) are three distinct rows of \(G\), and all own \(S\).

#### Proof

If \(E_i\) owns \(S\), then \(\tau E_i\) owns \(\tau S=S\).  Thus either
side choice owns the same target.  Component switching produces an exact
factor, so the three selected rows are distinct. \(\square\)

At depth one a balanced quota is one or two.  Hence every invariant
three-owner set supplies a packet of size two or three, independently of
the component signs.

## 2. The immediate \(P=10\) family

Use the canonical collision variants

\[
 A=11110000,\qquad
 B=11101000,\qquad
 DD=11001100,
 \tag{2.1}
\]

with common upper-core word

\[
 T_0=10111101.
 \tag{2.2}
\]

Prefix suspension by \(P=10\) gives, for every
\(V\in\mathcal D_{m-5}\), the three owner roots

\[
 10AV,\qquad10BV,\qquad10DDV
 \tag{2.3}
\]

and common upper-core word

\[
 \overline{10}\,T_0V
 =01\,T_0V.
 \tag{2.4}
\]

The second and third bits of (2.4) are both one: bit two is the final bit of
\(01\), while bit three is the first bit of \(T_0\).  Therefore the
corresponding lower target is fixed by \(\tau=(2\ 3)\).

The owner triples (2.3) are pairwise disjoint as \(V\) varies.  Lemma 1.1
therefore gives

\[
 \operatorname{Cat}_{m-5}
 \tag{2.5}
\]

disjoint packets in every cube child.  Their generating function is the
first term \(z^5C(z)\) in (0.4).

This is exactly the point missed by the naive NAE interpretation: even when
the three components have mixed signs, all three selected rows still own
the same invariant target.

## 3. Primitive invariant prefixes

Call a Dyck word primitive when it returns to height zero only at its final
step.  Let \(\mathscr H\) be the family of primitive Dyck words beginning
with

\[
 111.
 \tag{3.1}
\]

If \(P\in\mathscr H\), then \(\overline P\) begins \(000\).  Hence every
prefix-suspended target whose upper-core word begins

\[
 \overline P\,(\cdots)
\]

has equal second and third bits and is fixed by \(\tau\).

The number of primitive words of semilength \(p\ge3\) beginning \(111\) is

\[
 \operatorname{Cat}_{p-1}-\operatorname{Cat}_{p-2}.
 \tag{3.2}
\]

Indeed there are \(\operatorname{Cat}_{p-1}\) primitive words in total.
Those beginning \(110\) are counted by \(\operatorname{Cat}_{p-2}\);
the two possibilities \(110\) and \(111\) exhaust the third step of a
primitive word of semilength at least three.  Summing (3.2) gives (0.3):

\[
\begin{aligned}
 H(z)
 &=
 \sum_{p\ge3}
 \bigl(\operatorname{Cat}_{p-1}-\operatorname{Cat}_{p-2}\bigr)z^p\\
 &=z(1-z)(C(z)-1)-z^2.
\end{aligned}
\]

Primitive words form a prefix-free family.  Thus the root cylinders
\([P]\), \(P\in\mathscr H\), are pairwise disjoint and are also disjoint
from the \(P=10\) cylinder in Section 2.

## 4. Recursive matching inside every invariant cylinder

The report
FRACTIONAL_PACKET_GLOBAL_SEED_MATCHING_20260725.md constructs a recursive
pairwise disjoint family of canonical owner triples with generating
function \(M(z)\) in (0.2).

Fix \(P\in\mathscr H\) and prepend \(P\) to every root in that recursive
matching.  Exact MSW concatenation suspends every common target by the
prefix \(\overline P\).  Since its second and third bits are equal, every
such target is \(\tau\)-invariant.

The resulting triples are disjoint:

* within one \(P\)-cylinder, this is the recursive matching theorem;
* different primitive \(P\)'s are prefix-free;
* all begin \(11\), so none meets the separate \(P=10\) family.

Lemma 1.1 turns every triple into a packet in every cube child, regardless
of its quota.  The generating function for these triples is

\[
 H(z)M(z).
 \]

Together with Section 2 this proves (0.4)--(0.5).

## 5. Asymptotic density

Put

\[
 s=\sqrt{1-4z}.
\]

The global matching report proves

\[
 \frac{[z^m]M(z)}{\operatorname{Cat}_m}
 \longrightarrow
 \delta_*=\frac{275}{19321}.
 \tag{5.1}
\]

At \(z=1/4\),

\[
 H(z)=\frac18-\frac38s+O(s^2),
 \tag{5.2}
\]

and

\[
 M(1/4)=\frac2{139}.
 \tag{5.3}
\]

Since \(C(z)=2-2s+O(s^2)\), square-root coefficient comparison gives

\[
 \frac{[z^m]H(z)M(z)}{\operatorname{Cat}_m}
 \longrightarrow
 \frac18\delta_*
 +\frac{3}{16}\,\frac2{139}
 =
 \frac{173}{38642}.
 \tag{5.4}
\]

The immediate family has density

\[
 \frac{[z^m]z^5C(z)}{\operatorname{Cat}_m}
 \longrightarrow4^{-5}=\frac1{1024}.
 \tag{5.5}
\]

Therefore

\[
\begin{aligned}
 \delta_{\rm inv}
 &=
 \frac1{1024}+\frac{173}{38642}\\
 &=
 \frac{107897}{19784704},
\end{aligned}
 \tag{5.6}
\]

proving (0.7).

## 6. Distance robustness

Fix a cube child \(G\).  Sections 2--4 give \(J_m\) pairwise row-disjoint
packets in \(G\).  If an exact factor \(F\) differs from \(G\) in \(d\)
removed rows, at most \(d\) packets are hit.  Hence

\[
 \vartheta(F,\beta)\ge(J_m-d(F,G))_+.
 \tag{6.1}
\]

Choose a nearest \(G\in\mathcal Q_{\tau,m}\).  Equation (6.1) is equivalent
to (0.6).

Coordinate relabelling carries packet packings, exact factors, and row
distance bijectively.  Applying (0.6) after a common relabelling proves the
same potential inequality around every conjugate cube
\(\sigma\mathcal Q_{\tau,m}\).

## 7. Boundary and next gate

This theorem closes the native one-transposition escape attempted by the
NAE colouring.  Every child of that cube, and every \(o(t)\)-neighbourhood
of the cube, retains positive-density packet mass.

It does not rule out:

1. exact factors at positive-density distance from every conjugate native
   cube;
2. multistage walks coupling different transpositions;
3. genuinely nonlocal trades not represented in one canonical interaction
   cube.

The next exact question is therefore geometric:

> Can an exact factor be simultaneously
> \((\delta_{\rm inv}-o(1))t\)-far from every relabelled native
> one-transposition cube while keeping all fixed-window packet resources
> small?

Any global expansion theorem must now control travel between distinct
factor cubes, not merely mixing inside one cube.

## 8. Adversarial self-audit

1. **NAE is not packet destruction.**  Mixed rows still own an invariant
   target.  This is the central correction.
2. **No quota budget is used.**  Three owners persist, so quota one selects
   a pair and quota two selects the triple.
3. **The \(P=10\) family cannot take the full recursive suffix matching.**
   After an additional nonempty Dyck prefix, bit three becomes the first
   bit of its complement and differs from bit two.  Section 2 therefore
   uses only the immediate seed.
4. **Primitive \(111\)-prefixes may take the full recursive matching.**
   Their complemented bits two and three are fixed before anything in the
   suffix.
5. **Packet disjointness survives component mixing.**  A cube child chooses
   exactly one distinct row for every canonical source row; disjoint source
   triples therefore map to disjoint child triples.
6. **The theorem is cube-wide, not fibre-wide.**  The distance term in
   (0.6) is essential.

