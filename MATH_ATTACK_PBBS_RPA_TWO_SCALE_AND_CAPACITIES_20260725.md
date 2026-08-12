# Exact pruning capacities and a sub-Catalan quotient bound (insufficient for RP_A)

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Corrected verdict

Let

\[
 N=2r+1,
 \qquad B=\operatorname{Cat}_r,
\]

and let \(\overline P_r\) be the step-two PBBS quotient by coordinate
rotation.  For every cutoff \(H\), let \(\overline\nu_H\) be the maximum
number of pairwise quotient-edge-disjoint nonwrapping residence intervals
on the long quotient cycles, as in Section 17 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.

> **Normalization correction.**  RP_A is the physical assertion
> \(\nu_{H_A}(P_r)=o(B)\).  By the deck lower bound
> \(N\overline\nu_{H_A}\le\nu_{H_A}(P_r)\), its quotient target is
> \(\overline\nu_{H_A}=o(B/N)\), not merely \(o(B)\).  An earlier version
> of this note incorrectly called (0.1) below RP_A.  That claim is retracted.

What is unconditional is only the weaker quotient estimate

\[
 \boxed{
 \overline\nu_H=o(B)}
 \tag{0.1}
\]

uniformly in \(H\).  More explicitly,

\[
 \boxed{
 \overline\nu_H
 =O\!\left(B\frac{\log r}{\sqrt r}\right)}
 \tag{0.2}
\]

with a superpolynomially smaller additive term.

The proof is a two-scale argument.  Returns of residence at most
\(L=\lfloor\sqrt r/\log r\rfloor\) have Dyck height at most \(L-1\) and
are spectrally rare.  Every longer member of an edge-disjoint family uses
at least \(L+2\) of the \(B\) quotient edges.

This does **not** prove RP_A or the residence gate

\[
 \overline\nu_H=O(B/N).
 \tag{0.3}
\]

The second half of the note gives the exact peak-deletion capacities and
locates the first false contraction at that stronger scale.  A fixed
reduced gap-seven passage can carry a constant fraction of its entire
Pascal fibre and an exponentially large edge-disjoint outer packing.  Thus
neither bounded projection multiplicity nor a pointwise fibre contraction
is available.

## 1. Exact edge capacities under peak deletion

Identify the directed step-two quotient-edge set with the Dyck roots
\(\mathcal D_r\).  Simultaneous peak deletion is a semiconjugacy

\[
 \partial\tau_r=\tau_d\partial,
 \qquad \tau=\phi^2,
 \tag{1.1}
\]

where the rank

\[
 d(D)=r-\operatorname{pk}(D)
\]

is invariant along a PBBS quotient orbit.

For a nonempty reduced edge \(E\in\mathcal D_d\), put

\[
 k(E)=\operatorname{pk}(E).
\]

The exact one-step fibre size from the plane-tree leaf-slot decomposition is

\[
 \boxed{
 F_r(E)
 :=|\{D\in\mathcal D_r:\partial D=E\}|
 =\binom{r+d-k(E)}{2d}.}
 \tag{1.2}
\]

For \(d=0\), the only inverse root is the height-one star \((10)^r\), so
put \(F_r(\varnothing)=1\).  The fibres partition \(\mathcal D_r\), hence

\[
 \boxed{
 \sum_{d=0}^{r-1}\ \sum_{E\in\mathcal D_d}F_r(E)=B.}
 \tag{1.3}
\]

Let \(\mathcal P\) be an arbitrary pairwise quotient-edge-disjoint family
of nonwrapping outer return intervals.  For a reduced quotient edge \(E\),
define the projected occurrence multiplicity

\[
 M_{\mathcal P}(E)
 =\sum_{I\in\mathcal P}
   \#\{e\in I:\partial e=E\}.
 \tag{1.4}
\]

The projected trace can wrap a shorter reduced cycle, so occurrences, not
only distinct reduced edges, are counted in (1.4).

### Lemma 1.1 (exact projected capacity)

For every reduced edge \(E\),

\[
 \boxed{M_{\mathcal P}(E)\le F_r(E),}
 \tag{1.5}
\]

and

\[
 \boxed{
 \sum_E M_{\mathcal P}(E)=\sum_{I\in\mathcal P}|I|.}
 \tag{1.6}
\]

#### Proof

All outer edges used by members of \(\mathcal P\) are distinct.  The outer
edges projecting to \(E\) form exactly the fibre \(\partial^{-1}(E)\), of
size \(F_r(E)\).  This proves (1.5).  Counting every used outer edge first
by its interval and then by its reduced image proves (1.6).  \(\square\)

The same statement holds for any canonically chosen reduced subtrace of
each interval, such as the nested return ending at the first reselection of
the distinguished equality particle: its occurrence multiplicities are
bounded by the same \(F_r(E)\)'s.

## 2. Exact passage-start multiplicities

Use the notation of
`MATH_ATTACK_PBBS_QUOTIENT_PASCAL_PASSAGE_GATE_20260725.md`.  If
\(E\in\mathcal D_d\) has a predecessor passage at time \(g<N\), let

\[
 z_E(g)=\frac{1}{2}
 \left(
 \#\{0\le t<g:\kappa_t(E)=-1\}-1
 \right).
 \tag{2.1}
\]

The number of rank-\(r\) start edges above this one passage is exactly

\[
 \boxed{
 K_r(E,g)
 =\binom{r+d-k(E)-z_E(g)-1}{2d-1},}
 \tag{2.2}
\]

with value zero when the binomial is inadmissible.

If \(A_{\mathcal P}(E,g)\) is the number of members of \(\mathcal P\)
whose return root has reduced passage data \((E,g)\), distinctness of their
outer start edges gives

\[
 \boxed{
 A_{\mathcal P}(E,g)\le K_r(E,g).}
 \tag{2.3}
\]

More generally, let \(W(E,g)\) be any fixed ordered reduced subtrace of
this passage and let \(\operatorname{occ}_QW(E,g)\) count occurrences of a
reduced edge \(Q\) in that trace.  If every outer interval is charged to
the corresponding lifted subtrace, Lemma 1.1 gives the capacitated system

\[
 \boxed{
 \sum_{E,g}A_{\mathcal P}(E,g)
          \operatorname{occ}_QW(E,g)
 \le F_r(Q)
 \qquad(Q\text{ a reduced edge}).}
 \tag{2.4}
\]

Equations (1.2), (2.2), and (2.4) are the exact data available to a
one-step peak-deletion induction.

## 3. A two-scale split gives only a sub-Catalan quotient bound

### Theorem 3.1 (uniform sub-Catalan quotient packing; insufficient for RP_A)

Uniformly for every cutoff \(H\),

\[
 \overline\nu_H
 =O\!\left(B\frac{\log r}{\sqrt r}ight)
 =o(B).
 \tag{3.1}
\]

#### Proof

Put

\[
 L=\left\lfloor\frac{\sqrt r}{\log r}\right\rfloor.
 \tag{3.2}
\]

For small \(r\), enlarge the implicit constant, so assume \(L\ge4\).
Let \(\mathcal P\) be an edge-disjoint family counted by
\(\overline\nu_H\), and split it as

\[
 \mathcal P=\mathcal P_{\le L}\sqcup\mathcal P_{>L}
\]

according to projected residence length \(\ell\).

If \(I\in\mathcal P_{\le L}\), its odd omitted-label gap is

\[
 g=2\ell-1\le2L-1.
\]

The height-gap theorem gives

\[
 \operatorname{ht}(D_I)\le\frac{g-1}{2}=\ell-1\le L-1
 \tag{3.3}
\]

for its normalized return root.  The number of Dyck paths of semilength
\(r\) and height at most \(L-1\) is at most

\[
 \left(2\cos\frac{\pi}{L+1}\right)^{2r}
 \le4^r\exp\!\left(-c\frac r{L^2}\right)
 \tag{3.4}
\]

for an absolute \(c>0\).  There is at most one next-return interval at each
quotient root, so

\[
 |\mathcal P_{\le L}|
 \le4^r e^{-c r/L^2}
 \le4^r e^{-c(\log r)^2}.
 \tag{3.5}
\]

Since \(B\asymp4^r/r^{3/2}\), the last quantity is \(o(B)\).

If \(I\in\mathcal P_{>L}\), then its quotient trace contains

\[
 |I|=\ell+1\ge L+2
\]

edges.  The traces are pairwise edge-disjoint and the entire quotient has
exactly \(B\) directed edges.  Therefore

\[
 |\mathcal P_{>L}|
 \le\frac{B}{L+2}
 =O\!\left(B\frac{\log r}{\sqrt r}\right).
 \tag{3.6}
\]

Equations (3.5)--(3.6) prove (3.1).  Notice that the proof never uses the
value of \(H\), only the residence length of the intervals actually
selected.  \(\square\)

Theorem 3.1 can also be written using the exact capacities: (1.5)--(1.6)
give

\[
 (L+2)|\mathcal P_{>L}|
 \le\sum_EF_r(E)=B.
\]

Thus peak deletion loses no edge mass in the long part; the recursive
height theorem supplies the contraction in the short part.

## 4. First false pointwise contraction at the (1/N) scale

The exact capacities do not iterate with bounded congestion.

Take

\[
 E_d=(10)^{d-2}1100,
 \qquad k(E_d)=d-1.
\]

Its time-seven passage has \(z_{E_d}(7)=0\).  Hence

\[
 K_r(E_d,7)=\binom r{2d-1},
 \qquad
 F_r(E_d)=\binom{r+1}{2d},
 \tag{4.1}
\]

and the exact retained fibre fraction is

\[
 \boxed{
 \frac{K_r(E_d,7)}{F_r(E_d)}
 =\frac{2d}{r+1}.}
 \tag{4.2}
\]

Choose \(d\) with \(2d-1=r/2+O(1)\).  Then (4.2) tends to \(1/2\), and
the five-edge greedy argument gives an edge-disjoint outer family of size
at least

\[
 \frac19\bigl(K_r(E_d,7)-Z_H\bigr)
 \tag{4.3}
\]

on the long quotient cycles.  Under \(H\log N=o(r)\), this is
\((1-o(1))F_r(E_d)/18\).  Every member maps to the same ordered reduced
passage trace, and even its second pruned core is the same word \(10\).

Thus each of the following prospective induction inputs is false:

1. a reduced passage has bounded or polynomially bounded outer packing
   multiplicity;
2. edge-disjointness upstairs gives bounded-overlap reduced passages; or
3. fixing the seam slot retains \(o(F_r(E))\) lifts pointwise.

There is also no telescoping rank-ratio inequality.  At the minimum outer
rank \(r=2d-1\), formula (4.2) equals one, whereas

\[
 \frac{2d+1}{2r+1}\longrightarrow\frac12.
\]

Hence the tempting bound

\[
 \frac{K_r(E,g)}{F_r(E)}
 \le\frac{2d+1}{2r+1}
 \tag{4.4}
\]

is already false on the exact gap-seven family.

## 5. Why the argument stops before (B/N)

For any threshold \(L\), the preceding method has the form

\[
 \overline\nu_H
 \le
 \#\{D:\operatorname{ht}(D)\le L-1\}
 +\frac{B}{L+2}.
 \tag{5.1}
\]

To make the volume term \(O(B/N)\), one must take \(L=\Omega(N)\).  At
that scale every Dyck path passes the height cutoff, so the first term is
of order \(B\).  Therefore height plus edge volume cannot prove (0.3).

The exact remaining input at the \(1/N\) scale is a **Pascal-weighted
aggregate passage-packing inequality** for the capacitated system
(2.2)--(2.4).  It must use correlations across reduced core types or
quotient cycles.  The gap-seven fibre proves that no pointwise contraction
or unweighted recursive charge can substitute for that aggregate theorem.
