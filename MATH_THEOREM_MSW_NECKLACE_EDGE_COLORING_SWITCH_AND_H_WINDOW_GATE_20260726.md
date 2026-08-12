# MSW necklace edge-colouring: the orbit-aware switch identity and the exact H-window gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Let

\[
 p=2m+1\text{ be prime},\qquad
 \Omega=\binom{\mathbb F_p}{m},\qquad
 W=|\Omega|,\qquad T={W\over p}=\operatorname {Cat}_m.
\tag{0.1}
\]

Orient the canonical MSW factor and project its \(W\) tagged arcs to the
translation-necklace shores. The projected bipartite multigraph is
\(p\)-regular, so it has a proper \(p\)-edge-colouring. Each colour lifts
to a translation-invariant exact odd-graph owner permutation.

The low-switch proposal has one important correction and one exact
surviving gate.

1. A switch is **not** merely a change between the colours of two
   consecutive tagged MSW arcs. Different tags can represent the same
   translation orbit of directed arcs. Selecting one such tag installs
   the whole orbit. The correct test asks whether the current colour is
   active anywhere on the orbit of the next MSW arc.
2. For colour \(c\), let \(s_c\) be the resulting number of orbit-aware
   quotient switches. Then the lifted colour has exactly

   \[
                            b_c=p s_c
   \tag{0.2}
   \]

   physical splice boundaries.
3. There are two parity-shifted inheritance-defect sets:

   \[
    \begin{aligned}
    D^-_{c,q}
      &=\bigcup_{j=0}^{2q-2}\widetilde S_c^{-j}B_c,\\
    D^+_{c,q}
      &=\bigcup_{j=1}^{2q-1}\widetilde S_c^{-j}B_c
       =\widetilde S_c^{-1}D^-_{c,q}.
    \end{aligned}
    \qquad
    |D^\pm_{c,q}|\le(2q-1)p s_c,
   \tag{0.3}
   \]

   where \(B_c\) is the physical splice set. Equality in the cardinality
   bound holds when those predecessor intervals are disjoint.
4. If \(\operatorname {Sw}(\chi)=\sum_cs_c\), some colour satisfies

   \[
    b_c\le\operatorname {Sw}(\chi),\qquad
    |D^\pm_{c,H}|\le(2H-1)\operatorname {Sw}(\chi),
   \tag{0.4}
   \]

   and the complete two-sign, all-depth inherited-defect ledger obeys

   \[
    \sum_{q=1}^H\bigl(|D^-_{c,q}|+|D^+_{c,q}|\bigr)
    \le2H^2\operatorname {Sw}(\chi).
   \tag{0.5}
   \]

Consequently a colouring with \(\operatorname {Sw}=O(T)\) gives one
colour with \(O(T)=o(W/H)\) physical splices and \(o(W)\) bad *maximal*
\(H\)-windows whenever \(H=o(p)\). But it gives an \(o(W)\) all-depth
signed defect ledger by this argument only when \(H^2=o(p)\). In general
the sufficient switch scale is

\[
                 \operatorname {Sw}(\chi)=o(W/H^2),
\tag{0.6}
\]

not merely \(o(W/H)\).

There is also a separate coverage gap. A switch-free inherited window is
a genuine translated MSW window, but many such windows may hit the same
target. Equations (0.2)--(0.5) control chronology and safety, not the
missing-shadow hinge.

No \(O(T)\) colouring theorem for the actual MSW quotient is proved
here. The exact integer optimization is given in Section 6. Ordinary
\(p\)-regularity cannot prove it: a \(p\)-regular transition multigraph
with distinct parallel loop-orbits can force \(pT=W\) switches in every
proper colouring. This sharp abstract obstruction is not asserted to be
an MSW projection. For the physical MSW graph, the low-switch
transition-system theorem remains open.

This report supersedes the earlier projected-MSW Latin edge-colouring
and tagged switch-seam report dated 2026-07-26.  Its tagged colour-change
identity ignores the possibility that several tags represent one
translation arc orbit, and its simple undirected two-factor wording
ignores reverse-orbit directed two-cycles.  The orbit-aware statistic
above repairs both points.

## 1. Tagged quotient arcs and translation arc orbits

Let \(S\) be the oriented MSW successor. Its rows are directed cycles of
length \(p\). For each \(X\in\Omega\), write

\[
                         e_X:X\longrightarrow S(X).
\tag{1.1}
\]

Let \(\rho:t\mapsto t+1\) act on coordinates. The directed translation
orbit of \(e_X\) is

\[
 \mathcal O_X
 =\{X+t\longrightarrow S(X)+t:t\in\mathbb F_p\}.
\tag{1.2}
\]

Project every tagged occurrence \(e_X\) to

\[
                         [X]_{\rm L}\longrightarrow[S(X)]_{\rm R}.
\tag{1.3}
\]

Parallel tags are retained. The resulting bipartite multigraph \(B_S\)
is \(p\)-regular: each necklace contains \(p\) physical owners, and the
same holds for predecessors because \(S\) is a permutation.

Fix a proper edge-colouring

\[
                         \chi:E(B_S)\longrightarrow\mathbb F_p.
\tag{1.4}
\]

For every colour \(c\), its tagged edges form a quotient perfect matching.
The physical lift installs \(\mathcal O_X\) for every tag with
\(\chi(e_X)=c\), producing a translation-invariant exact successor
\(\widetilde S_c\).

Two tags in the same directed orbit \(\mathcal O\) project to parallel
edges with the same two quotient endpoints. Hence a proper colouring gives
them distinct colours. Define

\[
 a_c(\mathcal O)
 =\mathbf1_{\{\exists X:\mathcal O_X=\mathcal O,
                         \ \chi(e_X)=c\}}.
\tag{1.5}
\]

Thus \(a_c(\mathcal O)\in\{0,1\}\). This orbit activity, rather than the
colour of a preferred tag, determines the physical lift.

## 2. The orbit-aware switch identity

For a coloured tagged arc \(e_X\) with \(\chi(e_X)=c\), call its MSW
continuation **preserved** when

\[
                         a_c(\mathcal O_{S(X)})=1.
\tag{2.1}
\]

Otherwise call \(e_X\) an orbit-aware \(c\)-switch. Put

\[
 s_c(\chi)
 =\#\{X:\chi(e_X)=c,\ a_c(\mathcal O_{S(X)})=0\},
 \qquad
 \operatorname {Sw}(\chi)=\sum_cs_c(\chi).
\tag{2.2}
\]

If every directed MSW arc orbit contains only one tag, (2.1) says simply

\[
                         \chi(e_{S(X)})=\chi(e_X),
\]

so (2.2) is the ordinary number of colour exits along the cyclic rows.
With orbit multiplicity, this simpler statistic is wrong.

### Theorem 2.1 (exact quotient-switch/physical-splice identity)

Let \(B_c\) be the set of tails of the **first arcs** in those physical
arc-to-arc transitions of \(\widetilde S_c\) which do not continue the
translated MSW row represented by their selected tag. Then

\[
                         \boxed{|B_c|=p\,s_c(\chi).}
\tag{2.3}
\]

#### Proof

Take the unique colour-\(c\) selected tag \(e_X\) representing one active
orbit. Its lift supplies the \(p\) arcs

\[
 X+t\longrightarrow S(X)+t
 \qquad(t\in\mathbb F_p).
\tag{2.4}
\]

The translated MSW continuation after (2.4) is

\[
 S(X)+t\longrightarrow S^2(X)+t,
\tag{2.5}
\]

which is precisely the translate orbit \(\mathcal O_{S(X)}\). If that
orbit is active in colour \(c\), exact outgoing ownership forces
\(\widetilde S_c\) to use (2.5) at every phase. If it is inactive, none of
the \(p\) transitions uses (2.5).

Distinct selected tags of one colour represent distinct directed arc
orbits, so their \(p\) lifted arcs are disjoint. Every orbit-aware switch
therefore contributes exactly \(p\) distinct physical splice transitions,
and every physical splice arises this way. \(\square\)

This proof also explains the failure of tagged colour-change counting. If
\(e_{S(X)}\) has a different tag colour but another tag in its translation
orbit has colour \(c\), the physical continuation is still preserved.

## 3. Exact H-window dilation

One \(q\)-step every-second Johnson window uses \(2q\) consecutive odd
arcs. It follows one translated MSW row provided the \(2q-1\) internal
arc-to-arc transitions are not in \(B_c\).

Let \(D^-_{c,q}\) and \(D^+_{c,q}\) be the lower- and upper-parity starts
not certified by this inherited-row test. If a splice is marked at the
tail of the first arc whose continuation breaks, then

\[
 \boxed{\begin{aligned}
 D^-_{c,q}
   &=\bigcup_{j=0}^{2q-2}\widetilde S_c^{-j}B_c,\\
 D^+_{c,q}
   &=\bigcup_{j=1}^{2q-1}\widetilde S_c^{-j}B_c
    =\widetilde S_c^{-1}D^-_{c,q}.
 \end{aligned}}
\tag{3.1}
\]

The one-state shift records the two parities of the alternating trace.
These are exact set identities. Therefore

\[
 |D^\pm_{c,q}|\le(2q-1)|B_c|=(2q-1)p\,s_c.
\tag{3.2}
\]

Equality holds exactly when the displayed predecessor translates of
\(B_c\) are disjoint. Clustering of switches can only lower the number of
affected starts.

Every lower start outside \(D^-_{c,q}\), and every upper start outside
\(D^+_{c,q}\), produces the corresponding literal MSW target translated
by one coordinate shift. A start inside the relevant set may accidentally
remain safe; thus these are exact **inheritance-defect** sets and upper
bounds for actual unsafe windows.

Summing (3.2) gives the one-sign bound

\[
 \sum_{q=1}^H|D^\pm_{c,q}|
 \le |B_c|\sum_{q=1}^H(2q-1)
 =H^2|B_c|.
\tag{3.3}
\]

For fused lower and upper signs the conservative ledger is twice (3.3).
This is the exact source of the extra factor \(H\) between maximal-window
control and the all-depth missing-shadow interface.

## 4. Averaging over colours and component cost

Since there are \(p\) colours,

\[
 \min_c s_c\le{\operatorname {Sw}(\chi)\over p}.
\tag{4.1}
\]

Choose such a colour. Theorem 2.1 gives

\[
 |B_c|=p s_c\le\operatorname {Sw}(\chi).
\tag{4.2}
\]

Equations (3.2)--(3.3) now prove (0.4)--(0.5).

There is also a clean component bound. Delete the \(|B_c|\) bad
transitions from the cycles of \(\widetilde S_c\). Every component with no
deleted transition is a translated MSW \(p\)-cycle, so there are at most
\(W/p=T\) such components. Every other component contains a deleted
transition. Hence

\[
 c(\widetilde S_c)\le T+|B_c|,
 \qquad
 c(\widetilde S_c^2)\le2(T+|B_c|).
\tag{4.3}
\]

Thus \(\operatorname {Sw}=O(T)\) makes the component/reset toll
\(O(T)=o(W/H)\) for every \(H=o(p)\).

The window consequences have two different thresholds:

* maximal-depth inheritance defects are \(O(HT)=o(W)\) for \(H=o(p)\);
* the summed two-sign all-depth ledger is \(O(H^2T)\), which is \(o(W)\)
  only under \(H^2=o(p)\).

For the calibrated scale \(H\asymp\sqrt{m\log m}\), an \(O(T)\) switch
theorem would therefore solve the component gate and the single-depth
safety gate, but the crude all-depth ledger would be \(O(W\log m)\), not
\(o(W)\). One would still need switch clustering, direct target reuse, or
a weighted nonuniform depth charge.

## 5. Switches are not missing shadows

Let \(L_{c,q}^\pm(T)\) be the actual target loads of the lifted colour.
Outside the relevant set \(D^\pm_{c,q}\), every occurrence is a
translated genuine MSW occurrence. This proves rank correctness and gives
a known source row for the target. It does not prove that different starts
have different targets.

The exact missing objective remains

\[
 \mathfrak H_{c,q}^\pm
 =\sum_T(1-L_{c,q}^\pm(T))_+.
\tag{5.1}
\]

Even \(D^-_{c,q}=D^+_{c,q}=\varnothing\) does not imply (5.1) is small:
it merely says that the colour is a union of translated complete MSW rows.
The chosen row orbits can have repeated target necklaces. Therefore a successful
low-switch theorem must be paired with a literal quotient target-cover
theorem. Neither endpoint degrees nor the switch statistic contains that
information.

## 6. Exact integer optimization

Introduce binary variables \(x_{X,c}\) for the colour of the tagged edge
\(e_X\). Proper edge-colouring is exactly

\[
\begin{aligned}
 \sum_{X\in O}x_{X,c}&=1
 &&(\text{tail necklace }O,\ c),\\
 \sum_{X:S(X)\in O}x_{X,c}&=1
 &&(\text{head necklace }O,\ c),\\
 \sum_cx_{X,c}&=1
 &&(X\in\Omega).
\end{aligned}
\tag{6.1}
\]

For every directed translation arc orbit \(\mathcal O\), put

\[
 y_{\mathcal O,c}
 =\sum_{X:\mathcal O_X=\mathcal O}x_{X,c}.
\tag{6.2}
\]

The sum is automatically in \(\{0,1\}\), because its terms are parallel
edges at the same quotient endpoints. Add

\[
 z_{X,c}\ge x_{X,c}-y_{\mathcal O_{S(X)},c},
 \qquad z_{X,c}\ge0.
\tag{6.3}
\]

At an integral solution, minimizing \(\sum_{X,c}z_{X,c}\) makes

\[
 \boxed{
 \operatorname {Sw}_{\min}
 =\min\sum_{X,c}z_{X,c}}
\tag{6.4}
\]

subject to (6.1)--(6.3). This is the exact low-switch quotient-colouring
gate. The objective couples the colour of one tagged edge to the full
colour set of the next translation orbit; it is absent from the ordinary
König one-factorization theorem.

An \(O(T)\) proof must exploit additional MSW structure in (6.4), for
example long orbit-compatible row segments or a near-factorization of the
row--necklace incidence hypergraph.  The generic collision estimate says
that almost every coordinate relabelling of one fixed row is
necklace-transversal.  It gives no simultaneous conclusion for all rows
of the naturally labelled MSW factor, and therefore does not provide the
required transition colouring.

## 7. Lower bounds and the limit of regularity

### 7.1 A sharp abstract regularity obstruction

Take \(T\) quotient vertices. At each vertex place \(p\) distinct tagged
loop edges, declared to belong to \(p\) distinct translation-orbit labels,
and order those labels as one reference row. The bipartite tail--head graph
is \(p\)-regular. In every proper \(p\)-edge-colouring, the \(p\) loop
tags at a vertex receive all \(p\) colours.

Since every orbit label occurs once, the orbit-aware condition reduces to
ordinary equality of consecutive colours. The cyclic word is a permutation
of all \(p\) colours, so every one of its \(p\) transitions is a switch.
Summing over the \(T\) vertices gives

\[
                         \boxed{\operatorname {Sw}=pT=W.}
\tag{7.1}
\]

Thus \(p\)-regularity, row length \(p\), and exact one-factorization do not
imply even \(o(W)\) switch cost. This transition system is an abstract
sharp obstruction; it is not claimed to be the projection of the MSW odd
factor.

### 7.2 The physical zero-switch congruence

If \(s_c=0\) for one actual MSW colour, Theorem 2.1 propagates every
selected template around a complete translated MSW row. Hence
\(\widetilde S_c\) is a translation-invariant shortest-wreath factor.
The prime quotient classification then applies.

Because

\[
                         T\equiv2(-1)^m\pmod p,
\tag{7.2}
\]

no such factor exists when \(m\) is odd. Therefore every colour has at
least one orbit-aware switch and

\[
                         \operatorname {Sw}(\chi)\ge p
 \qquad(m\text{ odd}).
\tag{7.3}
\]

When \(m\) is even, a zero-switch colour would have to contain exactly two
AP quotient loops and partition the remaining quotient vertices into
zero-voltage \(p\)-cycles. This is the old integral cycle-hypergraph gate,
not a contradiction. The lower bound (7.3) is negligible compared with
\(T\) and does not kill the low-switch route.

## 8. Certified boundary

Proved:

1. the correct orbit-aware switch statistic;
2. the exact identity \(|B_c|=ps_c\);
3. the exact predecessor-dilation formula for inherited \(q\)-window
   defects;
4. the sharp distinction between maximal-depth and summed all-depth
   switch tolls;
5. the component bound \(c(\widetilde S_c^2)\le2(T+|B_c|)\);
6. the exact integer optimization (6.1)--(6.4);
7. a sharp abstract \(W\)-switch obstruction to any proof from regularity
   alone; and
8. the physical zero-switch Catalan obstruction for odd \(m\).

Not proved:

1. \(\operatorname {Sw}=O(T)\), even for the structural/maximal-depth
   gate, or the sharper raw all-depth estimate
   \(\operatorname {Sw}=o(W/H^2)\), for the actual projected MSW
   transition system;
2. \(o(W)\) all-depth defects at calibrated
   \(H\asymp\sqrt{m\log m}\) from switch count alone;
3. a literal quotient target-cover theorem for the chosen colour; or
4. coefficient one.

The low-switch quotient-colouring route is therefore genuine but has two
separate remaining gates: solve the orbit-aware transition colouring
(6.4), and then solve literal target coverage. Ordinary edge-colouring
solves neither.
