# Flag-compressed physical-port EKR and the chart-holonomy gate

> **Superseded EKR boundary (2026-07-26).** The literal selected-closure
> failure and three-strip chart-holonomy example below remain correct, but
> they obstruct only the PHCR/chart-gluing proof.  They do **not** leave
> high-cover EKR open.  The later localized Boolean-envelope argument
> never assumes selected closure or global chart synchronization and
> proves every non-star intersecting selected-port family has size
> \(o(D_1/\sqrt m)\).  See
> `MATH_THEOREM_LOCALIZED_FLAG_BOUNDARY_ADAPTIVE_KERNEL_HIGH_COVER_EKR_20260726.md`
> and its independent audit
> `MATH_AUDIT_LOCALIZED_FLAG_BOUNDARY_EKR_QUANTIFIERS_20260726.md`.
> The remaining coefficient-one gate is the non-clique fractional
> matching/edge-colouring problem.

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Outcome

Ordinary target-cardinality spread fails for physical fine-strip ports
because an \(s\times s\) rank--phase rectangle has \(s^2\) targets but
only \(3s+O(1)\) boundary coordinates.  The correct local object is a
compressed flag chart.

This note proves three positive statements.

1. An abstract flag-compressed high-cover EKR theorem is proved.  If a
   target link has closures of size \(O(g^2)\), where \(g\) is its boundary
   rank, and its adaptive witness branches satisfy a weighted branching
   inequality with parameter \(R>1\), then every intersecting family with
   cover number larger than the largest closure obeys

   \[
   \boxed{|\mathcal F|\le bKD R^{-G}.}              \tag{0.1}
   \]

   Here \(D\) is maximum target degree, \(K\) is maximum edge width,
   \(b\) is the bounded chart multiplicity, and \(G\) is the boundary
   rank to which the adaptive tree is run.

2. A locked physical cyclic-interval chart satisfies the raw branching
   inequality with

   \[
   \boxed{R=c_0m/h}                                \tag{0.2}
   \]

   for an absolute \(c_0>0\).  A Cartesian grid is charged by its boundary
   prefixes, not by its number of cells.  For

   \[
   G\to\infty,\qquad G^2=o(\tau),                  \tag{0.3}
   \]

   the right side of (0.1) is \(o(D/m^A)\) for every fixed \(A\), both at
   the default and optimized strip scales.  Thus the distributed
   high-cover EKR theorem is proved for every **chart-coherent,
   flag-closed** physical subcatalogue.

3. The unqualified application to the selected port hypergraph is not
   proved, and two literal physical failures are identified.

   * A raw flag closure need not be a selected-port closure.  A target
     implied by already exposed boundary coordinates may be omitted from
     the selected edge, producing a zero-boundary-rank port state.
   * Compatible charts do not synchronize globally.  Three physical
     strips can meet pairwise at three different targets with no common
     target; their local flag charts have nontrivial triangle holonomy.

The second item is a concrete physical counterexample to any theorem whose
hypothesis silently assumes one global chart.  It is only a three-strip,
low-cover configuration, not a high-cover obstruction.  The exact
remaining theorem is a port-state/chart-resolution inequality stated in
Section 7.

Consequently the strongest conclusion proved **within this older chart
framework** is:

\[
 \boxed{
 \begin{array}{c}
 \text{flag compression closes high-cover EKR on every locked chart;}\\
 \text{global selected-port chart resolution remains open in this method.}
 \end{array}}                                      \tag{0.4}
\]

Even a complete EKR theorem would still have to be upgraded to the
all-weights matching dual to prove

\[
 \chi_f'(\mathcal H^\#)=D_1+o(D_1/\sqrt m).        \tag{0.5}
\]

## 1. Abstract compressed certificates

Let \(\mathcal H\) be a hypergraph with maximum vertex degree \(D\) and
maximum edge size \(K\).  A *compressed certificate* \(\sigma\) consists
of

* a link \(\mathcal L_\sigma\subseteq E(\mathcal H)\);
* a target closure \(Q_\sigma\) contained in every edge of
  \(\mathcal L_\sigma\); and
* a nonnegative integer boundary rank \(g(\sigma)\).

Write \(d(\sigma)=|\mathcal L_\sigma|\).

Fix integers \(G\ge1\), a chart multiplicity \(b\), and \(R>1\).  Say
that the certificates satisfy \(\mathrm{FC}(G,R,b)\) if the following
hold.

### FC1: small closure

For \(g(\sigma)\le G\),

\[
                         |Q_\sigma|\le c_1(g(\sigma)+1)^2.        \tag{1.1}
\]

### FC2: singleton initialization

For every target \(x\), its star is the union of at most \(b\) initial
certificate links, each of degree at most \(D\) and rank zero.

### FC3: compressed outside-witness branching

Let \(g(\sigma)<G\), and let \(E\in E(\mathcal H)\) satisfy

\[
                         E\cap Q_\sigma=\varnothing.              \tag{1.2}
\]

The members of \(\mathcal L_\sigma\) which meet \(E\) can be partitioned
among child certificates \(\sigma'\) with
\(g(\sigma')>g(\sigma)\), and

\[
 \boxed{
 \sum_{\sigma'}R^{g(\sigma')-g(\sigma)}d(\sigma')
 \le d(\sigma).}                                   \tag{1.3}
\]

The partition may use sublinks of the displayed certificate links;
replacing a sublink by the full link only enlarges the left side.

### Theorem 1.1 (flag-compressed high-cover EKR)

Assume \(\mathrm{FC}(G,R,b)\).  Every intersecting family \(\mathcal F\)
with

\[
                         \tau(\mathcal F)>c_1(G+1)^2              \tag{1.4}
\]

satisfies (0.1).

#### Proof

Choose \(E_0\in\mathcal F\).  Partition \(\mathcal F\) by one selected
target in its intersection with \(E_0\).  There are at most \(K\) target
classes.  By FC2, each class is further covered by at most \(b\) initial
certificate links.  It is therefore enough to bound one initial branch.

At a certificate \(\sigma\) of rank less than \(G\), (1.1) and (1.4)
supply a witness \(E_\sigma\in\mathcal F\) disjoint from
\(Q_\sigma\).  Every member of the current branch meets
\(E_\sigma\), because \(\mathcal F\) is intersecting.  Apply FC3 and
continue on the child branches.  Boundary rank strictly increases, so
every branch reaches rank at least \(G\).

Iterating (1.3) gives, for one initial link,

\[
 \sum_{\lambda\text{ leaf}}R^{g(\lambda)}d(\lambda)\le D.       \tag{1.5}
\]

Every leaf has rank at least \(G\), hence the sum of its branch sizes is
at most \(DR^{-G}\).  Multiply by the at most \(bK\) initial branches.
This proves (0.1). \(\square\)

The theorem contains no ordinary \(\kappa^{-|A|}\) hypothesis.  A closure
may contain \(\Theta(g^2)\) Cartesian-grid targets at boundary cost \(g\).

## 2. One locked physical flag chart

Fix a middle target \(S\).  A directed physical strip through \(S\) is
described by an ordered inside word and outside word

\[
 \alpha=(\alpha_0,\ldots,\alpha_{h-1})\subset S,
 \qquad
 \beta=(\beta_0,\ldots,\beta_{h-1})\subset[2m]\setminus S.       \tag{2.1}
\]

In the forward nonwrapping chart its targets are

\[
 T(u,v)=S\setminus\{\alpha_0,\ldots,\alpha_{u-1}\}
       \cup\{\beta_0,\ldots,\beta_{v-1}\},         \tag{2.2}
\]

where \(|v-u|\le H\).  The backward chart has the identical form using
the other two boundary arms.  Thus a general target set in one physical
strip is governed by at most four nested boundary flags.

Suppose a certificate fixes prefix sets at inside lengths

\[
 0=u_0<u_1<\cdots<u_a=p
\]

and outside lengths

\[
 0=v_0<v_1<\cdots<v_b=q.
\]

The raw probability, conditional on the anchor \(S\), of these prefix-set
constraints is exactly

\[
 {\prod_{i=1}^a(u_i-u_{i-1})!\over(m)_p}
 {\prod_{j=1}^b(v_j-v_{j-1})!\over(m)_q}.           \tag{2.3}
\]

Indeed, the elements inside each prescribed prefix block may be ordered
arbitrarily, and every other position is free.  Formula (2.3) is the exact
flag-compressed substitute for ordinary target spread.

Let the boundary rank be the total number of exposed coordinates on the
four arms.  Close a certificate by adding every band target whose two
endpoint prefixes are already exposed.  With total boundary rank \(g\),
the closure has size at most

\[
                         |Q_\sigma|\le4(g+1)^2.     \tag{2.4}
\]

The rectangle from the crossing-grid audit is now correctly charged:
its \(r^2\) cells lie in a closure of boundary rank \(3r+O(1)\).

## 3. The compressed cyclic-kernel estimate

### Lemma 3.1 (one-target extension probability)

Let a locked chart certificate of rank \(g=o(m)\) be given.  Suppose a
new target extends its four boundary flags by a total of \(\ell\ge1\)
new coordinates, split into blocks of sizes
\(\ell_1,\ldots,\ell_j\), with \(j\le4\).  Conditional on the certificate,
the raw completion probability is at most

\[
 \prod_{i=1}^j{1\over\binom{m-g}{\ell_i}}
 \le\left({C\ell\over m-g}\right)^\ell.           \tag{3.1}
\]

#### Proof

On each arm, the new target prescribes the next prefix set but not the
order inside that new block.  The first expression is therefore the
conditional form of (2.3).  Use
\(\binom nk\ge(n/k)^k\) and
\(\sum_i\ell_i=\ell\). \(\square\)

### Lemma 3.2 (few interval placements at fixed increment)

Fix a physical witness strip \(E\).  Relative to a locked certificate,
the number of targets of \(E\) which are compatible with a specified
four-arm increment vector of total size \(\ell\) is at most two.  Summed
over all increment vectors of total size \(\ell\), it is at most

\[
                         C(\ell+1)^3.               \tag{3.2}
\]

The active-disjoint case has \(\ell\ge2(h-H)\) and contributes at most
\(2h\) placements.

#### Proof

After deleting the strip core, both targets are cyclic intervals.  If
they overlap without containment, their boundary differences determine
the second interval in at most the clockwise and counterclockwise
placements.  A comparable interval has only one nonzero side and at most
\(\ell+1\) placements, which is absorbed by (3.2).  There are
\(O((\ell+1)^3)\) compositions into four nonnegative arm increments.
Disjoint active intervals use at least \(h-H\) coordinates on both sides,
as in the cyclic pair kernel. \(\square\)

### Theorem 3.3 (raw flag-compressed branching)

There is an absolute \(c_0>0\) such that the raw locked-chart links satisfy
FC3 with

\[
                         R=c_0m/h.                  \tag{3.3}
\]

#### Proof

Let \(E\) avoid the closed target set \(Q_\sigma\).  Hence every target of
\(E\) which can extend the current link adds at least one boundary
coordinate.  Partition link members by a selected target of their
intersection with \(E\), then by its increment vector.  Lemmas 3.1--3.2
bound the normalized left side of (1.3) by

\[
 \sum_{\ell\ge1}C(\ell+1)^3
   \left({C\ell\over m-g}\right)^\ell R^\ell
 +2h\left({h+H\over m-H}\right)^{2(h-H)}R^{2(h-H)}.              \tag{3.4}
\]

Take \(g=o(h)\) and substitute \(R=c_0m/h\).  With \(c_0\) sufficiently
small, the first sum is at most \(1/3\): for small \(\ell\) it is a
convergent series in \(C c_0\ell/h\), and for
\(\ell=\Theta(h)\) the choice of \(c_0\) gives exponential decay.  The
second term is

\[
 2h\left({c_0(h+H)m\over h(m-H)}\right)^{2(h-H)}=o(1).           \tag{3.5}
\]

Enlarging finitely many small-\(m\) constants makes the total at most one,
which is (1.3). \(\square\)

The proof uses the cyclic interval kernel, not merely maximum codegree.
It charges an entire Cartesian grid through the prefixes which generate
it.

## 4. The chart-coherent EKR theorem

Call an intersecting physical strip family *chart coherent through rank
\(G\)* if every link generated by the adaptive proof of Theorem 1.1 can
be partitioned into at most \(b=m^{o(G)}\) locked four-arm certificates,
their closed target sets are contained in every corresponding selected
edge, and the raw branching estimate (3.4) remains valid for those
selected links up to a factor \(2^{o(G)}\).

### Theorem 4.1 (chart-coherent physical EKR)

Assume

\[
 G\to\infty,\qquad G=o(h),\qquad G^2=o(\tau(\mathcal F)),       \tag{4.1}
\]

and let \(\mathcal F\) be chart coherent through rank \(G\).  Then

\[
 |\mathcal F|
 \le m^{o(G)}KD\left({C h\over m}\right)^G.        \tag{4.2}
\]

In particular,

\[
                         |\mathcal F|=o(D/\sqrt m). \tag{4.3}
\]

#### Proof

The hypotheses supply \(\mathrm{FC}(G,R',b)\) with
\(R'=m/(Ch)\), after absorbing the subexponential chart and port factors.
Apply Theorem 1.1 to obtain (4.2).

At the default scale, \(m/h=m^{1/3-o(1)}\); at the optimized scale,
\(m/h=\sqrt m/\operatorname{polylog}m\).  Hence

\[
 G\log(m/(Ch))-\log K\longrightarrow\infty
\]

faster than every fixed multiple of \(\log m\).  This proves (4.3).
\(\square\)

For example, one may take \(G=m^\gamma\) with any sufficiently small fixed
\(\gamma>0\) satisfying \(G^2=o(\tau)\).  Thus the cover budget is much
larger than every compressed closure used by the proof.

## 5. Why selected ports are not automatically flag closed

Theorem 3.3 concerns raw physical links.  The selected port edge retains
only chosen nonmiddle incidences.  Exact target degrees do not make this
selection hereditary.

Return to the rectangle \(\mathcal A_r\) of the crossing-grid audit.  Its
boundary words already determine the target

\[
 T_{0,r}=T\cup\{\beta_0,\ldots,\beta_{r-1}\}.      \tag{5.1}
\]

Thus

\[
 d_{\rm raw}(\mathcal A_r\cup\{T_{0,r}\})
 =d_{\rm raw}(\mathcal A_r).                       \tag{5.2}
\]

The new target has boundary increment zero.  Nevertheless a selected edge
containing \(\mathcal A_r\) need not retain its incidence at \(T_{0,r}\).
Therefore the raw closure is not necessarily contained in every selected
completion of the same boundary certificate.

### Proposition 5.1 (literal zero-generator port hole)

For every \(2\le r\le H\) with \(r^2=o(h\sqrt m)\), the exact-degree ports
can be chosen, while retaining the pair-codegree, width, and off-edge-star
bounds of the physical-port theorem, so that some selected strip contains
all targets of \(\mathcal A_r\) but omits \(T_{0,r}\).

#### Proof

Start with a port outcome supplied by the simultaneous sparsification
theorem and fix one raw rectangle occurrence in a strip \(C\).  For each
nonmiddle target of \(\mathcal A_r\) not already retained at \(C\), insert
the incidence \((C,T)\) and delete any other retained incidence at the same
target.  At \(T_{0,r}\), perform the reverse swap if necessary.  Every
target degree remains exactly \(D_1\).

Only \(O(r^2)\) incidences are changed.  Consequently every selected pair
codegree and every off-edge-star count changes by at most \(O(r^2)\),
which is \(o(D_1/m)\) and \(o(\widehat\rho_mD_1)\), respectively.  The
width of \(C\) increases by at most \(r^2=o(h\sqrt m)\), and every donor
strip changes by at most one incidence.  Thus the same asymptotic conclusions hold,
while the required selected closure failure is literal. \(\square\)

At shallow rank \(r=o(\sqrt m)\), only an
\(O(r^2/m)\)-fraction of the \(T_{0,r}\)-star is deleted.  This makes the
failure rare in the whole catalogue, but a putative adversarial
intersecting family may concentrate on precisely those omitted incidences.
The existing exact-degree, pair-codegree, and off-edge-star theorems give
no conditional bound excluding that concentration.

Hence the exact port-stability hypothesis missing from Theorem 4.1 is:

\[
 \boxed{
 \text{every zero-generator port state is either absorbed into the
 closure or pays its true conditional deletion entropy}.}       \tag{5.3}
\]

Ordinary boundary rank assigns no cost to such a state, so (5.3) is not a
formal consequence of Theorem 3.3.

## 6. A concrete chart-holonomy counterexample

There is no global chart synchronization theorem for arbitrary physical
strips.  Choose nested targets

\[
 S\subset T\subset U,
 \qquad |S|=m-1,\quad |T|=m,\quad |U|=m+1.        \tag{6.1}
\]

The physical construction in Proposition 5.1 of
`MATH_THEOREM_PHYSICAL_PORT_EKR_HIGH_COVER_REDUCTION_20260726.md` gives
three strips \(E_1,E_2,E_3\) such that, after generic completion of their
unused active orders,

\[
 \begin{array}{c|ccc}
       &S&T&U\\ \hline
 E_1   &0&1&1\\
 E_2   &1&0&1\\
 E_3   &1&1&0
 \end{array}                                      \tag{6.2}
\]

and no other selected target is common to all three.  Thus

\[
 E_1\cap E_2\supseteq\{U\},\qquad
 E_2\cap E_3\supseteq\{S\},\qquad
 E_3\cap E_1\supseteq\{T\},                       \tag{6.3}
\]

but

\[
                         E_1\cap E_2\cap E_3=\varnothing.        \tag{6.4}
\]

Write \(U\setminus S=\{x,y\}\) and \(T=S\cup\{x\}\).  The
\(E_3E_1\) and \(E_1E_2\) charts use the boundary order \(x,y\), whereas
the \(E_2\) chart realizes \(S\subset U\) through the competing order
\(y,x\), thereby avoiding \(T\).  Transport around the triangle therefore
acts by the transposition \((x\ y)\).

The chart used at the \(E_1E_2\) intersection cannot be transported
around the triangle and return as the chart used at \(E_3E_1\).  This is
literal chart holonomy.  It refutes an unqualified assertion that local
flag charts of an intersecting family glue to one global flag chart.

The example has cover number two and only three principal strips.  The
larger Hilton--Milner family built from the same triangle has size
\((2+o(1))D/m\), still \(o(D/\sqrt m)\).  Therefore (6.2) is a counterexample
to the **method hypothesis**, not to high-cover EKR itself.

## 7. The exact surviving theorem

To remove “chart coherent” from Theorem 4.1, one needs the following
selected-port resolution.

### PHCR\(_G\): port-holonomy compressed resolution

For some \(G\to\infty\) with \(G^2=o(\tau_0)\), every selected target link
encountered by the adaptive witness tree admits a partition into
certificate states such that:

1. the total chart multiplicity over a root-to-leaf history is
   \(m^{o(G)}\);
2. every state has a closed target set of size \(O(g^2)\);
3. ordinary boundary extensions obey the weighted branching norm (1.3)
   with \(R=m/(Ch)\);
4. zero-boundary port omissions are assigned an additional defect rank
   equal to their conditional negative logarithm in base \(R\); and
5. chart changes around cycles, including (6.2), either cancel inside one
   state or pay positive defect rank.

### Corollary 7.1

PHCR\(_G\) implies that every non-star intersecting physical port family
of cover number at least \(\tau_0\) has size \(o(D/\sqrt m)\).

#### Proof

Add boundary rank and defect rank.  Conditions 1--5 give
\(\mathrm{FC}(G,R,m^{o(G)})\).  The closure bound and
\(G^2=o(\tau_0)\) permit every witness step.  Apply Theorem 1.1 and then
the estimate in Theorem 4.1. \(\square\)

PHCR is strictly more precise than ordinary KZ spread.  It identifies the
two correlations that must be paid for: port-retention bits and chart
holonomy.  The crossing-grid rectangle itself is no longer an obstruction,
because its \(s^2\) cells have boundary rank \(O(s)\).

## 8. Fractional-colouring boundary

Corollary 7.1 would close the remaining high-cover **clique** gate.  It is
not by itself the all-weights theorem.  The fractional-colouring target is

\[
 \sum_Cy_C
 \le\left(D+o(D/\sqrt m)\right)
      \max_{M\text{ matching}}\sum_{C\in M}y_C.     \tag{8.1}
\]

The pair-core theorem already proves (8.1) for every graph-like support.
A full conclusion would require a weighted PHCR statement, with the
branching norm applied to weighted links and compatible with one common
matching throughout the adaptive decomposition.  No such synchronization
is proved here.

## 9. Audited boundary

Proved:

1. the abstract flag-compressed high-cover EKR theorem, Theorem 1.1;
2. exact prefix-block probabilities (2.3);
3. the raw cyclic flag-compressed branching theorem with
   \(R=\Theta(m/h)\), Theorem 3.3;
4. high-cover EKR for chart-coherent, flag-closed physical families; and
5. a literal three-strip chart-holonomy counterexample to global chart
   synchronization.

Not proved:

1. PHCR for the actual selected target-regular ports;
2. high-cover EKR without chart coherence; or
3. the weighted fractional-colouring inequality (8.1).

The concrete failure is no longer the Cartesian grid: flag compression
handles it optimally.  The exact remaining obstruction is the interaction
of zero-generator port omissions with nontrivial chart holonomy.
