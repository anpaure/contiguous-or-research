# A logarithmic aligned-support barrier for multistep exact-factor switching

Date: 2026-07-25

Method: pure mathematics only. No search, computation, solver, or external
black box is used.

## 0. Outcome

The invariant mixed-seed obstruction persists through an arbitrary number
of exact component-switch steps, provided the coordinate transpositions use
too small a common support.

Let \(B\) be a coordinate set of size \(b<n=2m+1\). Choose the distinguished
odd coordinate outside \(B\), relabel the **pair consisting of the factor
and the support** so that \(B\) is the first \(b\) finite coordinates, and
start from that correspondingly relabelled canonical MSW factor.

This alignment is part of the hypothesis. It is not claimed that an
arbitrary \(b\)-subset relative to one fixed canonical labelling has the
same prefix count.

Let \(\mathcal R_{B,m}\) be the set of exact factors reachable by any finite
sequence of operations of the following form:

1. choose a transposition \(\tau\) whose two endpoints lie in \(B\);
2. overlay the current exact factor \(F\) with \(\tau F\);
3. independently choose either side of every interaction component.

For \(0\le b\le m-4\), put

\[
 \boxed{
  I_{m,b}
  =
  [z^{m-b-4}]C(z)^{b+1}
  =
  \frac{b+1}{2m-b-7}
  \binom{2m-b-7}{m-b-4}.
 }
 \tag{0.1}
\]

Then every \(G\in\mathcal R_{B,m}\), under every balanced quota system
containing depth one, satisfies

\[
 \boxed{
  \vartheta(G,\beta)\ge I_{m,b}.
 }
 \tag{0.2}
\]

The robust form is

\[
 \boxed{
  \vartheta(F,\beta)+d(F,\mathcal R_{B,m})\ge I_{m,b}
 }
 \tag{0.3}
\]

for every exact factor \(F\).

Uniformly for \(b=o(\sqrt m)\),

\[
 \boxed{
  \frac{I_{m,b}}{\operatorname{Cat}_m}
  =
  \frac{b+1}{256\,2^b}
  \left(1+O\left(\frac{(b+1)^2}{m}\right)\right).
 }
 \tag{0.4}
\]

Consequently a multistep component-switch construction satisfying the
fractional packet target \(o(\operatorname{Cat}_m/\sqrt m)\) must use a
coordinate support \(b=b(m)\) with

\[
 \boxed{
  \frac{2^b}{b+1}\gg\sqrt m.
 }
 \tag{0.5}
\]

Equivalently,

\[
 b-\frac12\log_2m-\log_2(b+1)\longrightarrow+\infty.
 \tag{0.6}
\]

In rough form this requires

\[
 b\ge\frac12\log_2m+\log_2\log m+\omega(1).
 \tag{0.7}
\]

Thus bounded-coordinate switching on an aligned support, and even such
switching on a support well below logarithmic size, cannot prove
\((\mathrm{FSP}_A)\).

For fixed \(b\), the recursive matching from the preceding report gives the
stronger density

\[
 \boxed{
  \delta_b
  =
  2^{-b}
  \left(\frac{275}{19321}+\frac b{139}\right),
 }
 \tag{0.8}
\]

but the exact immediate-seed count (0.1) is used for the uniform growing
\(b\) conclusion.

## 1. Every row has a bijective descendant

### Lemma 1.1 -- a row and its transposed row lie in one component

Let \(F\) be any exact wreath factor, let \(\tau=(x\ y)\) be any coordinate
transposition, and let \(E\in F\) be one wreath. In the overlap graph
between \(F\) and \(\tau F\), the left row \(E\) and the right row
\(\tau E\) lie in the same connected component.

#### Proof

The wreath \(E\) has \(n=2m+1\) cyclic middle \(m\)-windows. Each coordinate
belongs to exactly \(m\) of them, so the total number of incidences of
\(x,y\) with these windows is

\[
 2m=n-1.
\]

If every window contained exactly one of \(x,y\), the incidence total would
be \(n\), a contradiction. Hence some middle window contains either both
or neither. That \(m\)-set is fixed by \(\tau\), is owned by \(E\) on the
left, and is owned by \(\tau E\) on the right. It supplies an overlap edge
joining the two rows into one component. \(\square\)

### Corollary 1.2 -- bijective row lineage

In one component-switch step, every row \(E\in F\) has exactly one selected
descendant,

\[
 E\qquad\text{or}\qquad\tau E,
 \tag{1.1}
\]

according to the side chosen in its component. The descendant map is a
bijection from the rows of \(F\) to the rows of the child factor.

#### Proof

Lemma 1.1 shows that \(E\) and \(\tau E\) occur on the two sides of the
same component. Choosing that component's left side selects \(E\); choosing
its right side selects \(\tau E\). The map is injective componentwise
because \(\tau\) is a bijection, and different selected components contain
disjoint row families. Both factors have the same row count, so it is
bijective. \(\square\)

After a sequence of transpositions supported in \(B\), every initial row
\(E\) therefore has one descendant

\[
 g_EE,\qquad g_E\in\langle\tau_1,\tau_2,\ldots\rangle
 \le\operatorname{Sym}(B).
 \tag{1.2}
\]

The permutation \(g_E\) may depend on the row; no common relabelling is
assumed.

## 2. Invariant prefix targets

For \(b\ge1\), let \(P\) be a primitive Dyck word whose first \(b\) steps
are all up-steps:

\[
 P=1^b(\cdots).
 \tag{2.1}
\]

For every Dyck suffix \(V\), prefix suspension of the canonical seed gives
the three owner roots

\[
 PAV,\qquad PBV,\qquad PDDV
 \tag{2.2}
\]

and common upper-core word

\[
 \overline P\,T_0V.
 \tag{2.3}
\]

The first \(b\) bits of (2.3) are zero. Thus the complementary lower target
contains every coordinate in \(B\), and is invariant under
\(\operatorname{Sym}(B)\).

By (1.2), each of the three rows in (2.2) has exactly one descendant
\(g_EE\). Since its target is fixed by every \(g_E\), that descendant still
owns the same target. The three descendants are distinct and therefore
form a three-owner set in every reachable factor.

Primitive prefixes form a prefix-free family. As \(P,V\) vary, the source
triples (2.2) are pairwise row-disjoint, and bijective lineage preserves
that disjointness.

At depth one, quota one selects any two descendants and quota two selects
all three. Hence every source triple gives a disjoint packet under every
balanced quota system.

For \(b=0\), use the empty prefix \(P=\varnothing\); the same conclusions
hold with the trivial coordinate group.

## 3. Exact enumeration

The generating function for primitive Dyck prefixes beginning with \(b\)
up-steps is

\[
 \boxed{
  H_b(z)=z^bC(z)^b=(zC(z))^b.
 }
 \tag{3.1}
\]

Indeed, a primitive word is \(1R0\). Requiring \(b\) initial up-steps is
equivalent to requiring \(b-1\) initial up-steps in \(R\). The standard
first-return decomposition of a Dyck word with \(r\) prescribed initial
up-steps has generating function \(z^rC^{r+1}\), which gives (3.1).

The inserted seed has semilength four, and \(V\) is arbitrary. Thus the
packet count has generating function

\[
 z^4H_b(z)C(z)=z^{b+4}C(z)^{b+1}.
 \tag{3.2}
\]

The generalized Catalan coefficient identity

\[
 [z^N]C(z)^r
 =
 \frac r{2N+r}\binom{2N+r}{N}
 \tag{3.3}
\]

with \(N=m-b-4\) and \(r=b+1\) proves (0.1), and the disjoint packet
construction proves (0.2).

If \(F\) lies at row distance \(d\) from a reachable factor \(G\), at most
\(d\) of its row-disjoint packets are hit. Hence

\[
 \vartheta(F,\beta)\ge(I_{m,b}-d(F,G))_+.
\]

Minimizing over \(G\in\mathcal R_{B,m}\) proves (0.3).

## 4. Uniform asymptotics

From (0.1) and

\[
 \operatorname{Cat}_m=\frac1{m+1}\binom{2m}{m},
\]

one obtains

\[
\begin{aligned}
 \frac{I_{m,b}}{\operatorname{Cat}_m}
 &=
 \frac{(b+1)(m+1)}{2m-b-7}\\
 &\quad\cdot
 \frac{(2m-b-7)!\,m!\,m!}
 {(m-b-4)!\,(m-3)!\,(2m)!}.
 \tag{4.1}
\end{aligned}
\]

For \(b=o(\sqrt m)\), expand each finite product around \(m\) and \(2m\):

\[
 \frac{m!}{(m-b-4)!}
 =m^{b+4}
 \left(1+O\left(\frac{(b+1)^2}{m}\right)\right),
 \tag{4.2}
\]

\[
 \frac{m!}{(m-3)!}
 =m^3\left(1+O(m^{-1})\right),
 \tag{4.3}
\]

and

\[
 \frac{(2m-b-7)!}{(2m)!}
 =(2m)^{-b-7}
 \left(1+O\left(\frac{(b+1)^2}{m}\right)\right).
 \tag{4.4}
\]

The prefactor in (4.1) is

\[
 \frac{b+1}{2}
 \left(1+O\left(\frac{b+1}{m}\right)\right).
 \tag{4.5}
\]

Multiplying (4.2)--(4.5) gives

\[
 \frac{I_{m,b}}{\operatorname{Cat}_m}
 =
 (b+1)2^{-b-8}
 \left(1+O\left(\frac{(b+1)^2}{m}\right)\right),
\]

which is (0.4).

If an endpoint satisfies the FSP target

\[
 \vartheta=o(t/\sqrt m),
\]

then (0.2)--(0.4) force

\[
 \frac{(b+1)\sqrt m}{2^b}\longrightarrow0.
\]

This is equivalent to (0.5)--(0.6), and implies the rough form (0.7).

## 5. Stronger fixed-support constant

For fixed \(b\), prepend every primitive \(1^b\)-prefix not merely to the
immediate seed but to the full recursive matching with generating function

\[
 M(z)
 =
 \frac{z^4C(z)}
 {1-(1+z^2)(zC(z)-z^2-2z^4)-2z^6}.
 \tag{5.1}
\]

The packet series is

\[
 (zC(z))^bM(z).
 \tag{5.2}
\]

At \(s=\sqrt{1-4z}\),

\[
 (zC(z))^b
 =2^{-b}(1-bs+O(s^2)),
\]

while

\[
 M(1/4)=\frac2{139},
 \qquad
 \frac{[z^m]M(z)}{\operatorname{Cat}_m}
 \longrightarrow\frac{275}{19321}.
\]

Square-root coefficient comparison in (5.2) gives (0.8).

## 6. A relabelling-average bound for arbitrary supports

The alignment hypothesis can be replaced by an existential relabelling
whose quantitative loss is explicit.

Let \(B\subset[n]\) be any fixed coordinate set of size \(b<n\). Take the
\(L_m\) row-disjoint packet triples from
FRACTIONAL_PACKET_GLOBAL_SEED_MATCHING_20260725.md, and apply a uniformly
random common coordinate relabelling \(\sigma\) to their exact factor,
owners, and targets.

Every depth-one target has size

\[
 r=m-1.
\]

For one fixed target, \(\sigma S\) is a uniform \(r\)-subset of \([n]\).
It is invariant under every permutation supported on \(B\) whenever it
contains all of \(B\) or none of \(B\). The probability of this event is

\[
 \boxed{
  p_{m,b}
  =
  \frac{\binom{n-b}{r-b}+\binom{n-b}{r}}
       {\binom nr}
  =
  \frac{(r)_b+(n-r)_b}{(n)_b}.
 }
 \tag{6.1}
\]

Therefore the expected number of invariant triples is \(p_{m,b}L_m\).
Some relabelling \(\sigma\) has at least that many. Starting from
\(\sigma F_m^{\rm MSW}\), every multistep switch path supported on the
arbitrary set \(B\) preserves these packets by the row-lineage lemma.

Thus, if \(\mathcal R_{B,m}^{\sigma}\) is the corresponding reachable set,

\[
 \boxed{
  \vartheta(F,\beta)+d(F,\mathcal R_{B,m}^{\sigma})
  \ge p_{m,b}L_m
 }
 \tag{6.2}
\]

for a suitable \(\sigma\).

Uniformly for \(b=o(\sqrt m)\),

\[
 p_{m,b}
 =
 2^{1-b}
 \left(1+O\left(\frac{(b+1)^2}{m}\right)\right).
 \tag{6.3}
\]

Indeed \(r=m-1\), \(n-r=m+2\), and each falling-factorial ratio in (6.1)
is \(2^{-b}(1+O(b^2/m))\).

This gives a coordinate-geometry-independent, but existentially relabelled,
packet density

\[
 \left(2^{1-b}\frac{275}{19321}+o(2^{-b})\right)t.
 \tag{6.4}
\]

It forces \(2^b\gg\sqrt m\) for such a relabelled path to meet the FSP
scale. The stronger factor \(b+1\) in (0.5) uses the special aligned prefix
geometry and is not claimed uniformly over arbitrary supports.

## 7. Boundary and next travel gate

The theorem allows arbitrarily many exact component switches and arbitrary
adaptation of the component choices. It uses only the common support of the
coordinate transpositions.

It does not obstruct a path whose transposition support grows beyond the
threshold (0.5), nor genuinely nonlocal exact-factor trades which are not
built from such component switches.

The next gate is therefore sharper than “use more than one cube”:

> A successful multistep heat-bath route must spread its coordinate action
> over at least logarithmically many coordinates, quantitatively beyond
> (0.5), before invariant packet seeds can disappear.

## 8. Adversarial self-audit

1. **\(b\) counts coordinate support, not primitive components.** The
   prefix condition is \(b\) initial up-steps, and its series is
   \((zC)^b\).
2. **Row lineage is bijective.** Lemma 1.1 places \(E,\tau E\) in the same
   component; no row is lost without one selected descendant.
3. **The target is invariant under the whole generated group.** Its lower
   mask contains all of \(B\), not merely both endpoints of one
   transposition.
4. **The growing-\(b\) estimate is uniform.** The exact coefficient formula,
   not a fixed-parameter singular expansion, proves (0.4).
5. **The recursive constant is claimed only for fixed \(b\).**
6. **Alignment is not free relative to a fixed factor.** Simultaneous
   relabelling sends both the support and the canonical factor. The theorem
   applies to this aligned pair; arbitrary support geometry in a fixed
   canonical labelling remains open.
7. **The averaging lemma is existential in the relabelling.** It proves a
   barrier for some conjugate canonical start adapted to \(B\), not for
   every relabelling of one fixed canonical factor.
8. **A distinguished coordinate is needed outside \(B\).** This is why the
   theorem assumes \(b<n\); the relevant logarithmic regime is far inside
   that range.
