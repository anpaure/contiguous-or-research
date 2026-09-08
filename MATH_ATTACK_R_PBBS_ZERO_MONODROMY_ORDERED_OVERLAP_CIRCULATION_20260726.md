# PBBS root-dependent zero-monodromy braids: ordered-overlap circulation, exact Hamilton cuts, and the unavoidable seam density

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Use the covering-side critical radius

\[
 H=\max\left\{0\le h<m:
 {\binom{2m}{m}\over\binom{2m}{m-h}}\le m+h\right\},
 \qquad M=m+H,
\tag{0.1}
\]

and put

\[
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H}.
\tag{0.2}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 MN_H=W+E_H,\quad 0\le E_H=O(WH/m),\qquad
 N_H=(1+o(1)){W\over m}.
\tag{0.3}
\]

All asymptotics are as \(m\to\infty\).  Every statement using
\(H\ge2\) or \(2H<M\) is asserted for all sufficiently large \(m\).

This report resolves the **uncoloured zero-monodromy layer** exactly and
isolates the remaining coloured integral gate.

1.  An intact PBBS promotion segment has an ordered injective
    \(2H\)-letter word \(w=i(e)d(e)\).  At the unlabelled word-containment
    level, a family of such words can lie in one literal top frame
    precisely when its imposed successor arcs form a partial permutation
    with no proper directed cycle.  After
    contracting the resulting directed paths, authorized joins must form
    a Hamilton cycle.  The binary degree equations, directed subtour
    cuts, the parity cut, and the deck-voltage congruence below are exact;
    they are not merely necessary marginal conditions.

2.  If the imposed word paths pass those cuts, all of their joins can be
    absorbed into **one** cyclic frame.  Thus zero monodromy by itself
    creates no superlinear component toll: one component for each root,
    hence exactly \(N_H\) components, has opening cost at most

    \[
       2HN_H=o(W).
    \tag{0.4}
    \]

3.  There is nevertheless an exact PBBS-provenance lower bound.  A
    same-top inherited PBBS run has at most \(H\) transitions.  Therefore
    the number \(s\) of genuinely non-inherited successor edges in every
    top frame obeys

    \[
       \boxed{s\ge s_0(M,H):=
       \left\lceil {M\over H+1}\right\rceil.}
    \tag{0.5}
    \]

    If a top frame contains \(k\) transition-disjoint intact PBBS
    \(H\)-transition segments, then additionally

    \[
       k\le\left\lfloor {M\over H+1}\right\rfloor
    \tag{0.6}
    \]

    and the number \(b_{\rm out}\) of transitions not internal to those
    full segments obeys

    \[
       \boxed{
       b_{\rm out}\ge b_0(M,H):=
       M-H\left\lfloor {M\over H+1}\right\rfloor.}
    \tag{0.7}
    \]

    The residue in \(b_0\) can be much larger than \(M/H\); it includes
    inherited short tails and must not be called a seam count.  Across
    the \(N_H\) critical roots, the genuine occurrence-level seam bound is

    \[
       \boxed{S_{\rm new}\ge
       N_H\left\lceil {M\over H+1}\right\rceil
       =(1+o(1)){W\over H}.}
    \tag{0.8}
    \]

    Hence a fixed-top, one-frame-per-root PBBS-provenance atlas with only
    \(O(1)\) non-inherited successor occurrences per root is impossible.
    In the exactly \(N_H\)-component model, the average number of such
    occurrences per component is at least

    \[
       (1+o(1)){m\over H}\longrightarrow\infty
    \tag{0.9}
    \]

    non-PBBS joins.  With merely \(C=O(N_H)\), the corresponding average
    lower bound is \(\Omega(m/H)\), with a constant depending on the
    implied component bound.

4.  The common-symmetric-tag all-depth subproblem is an integral,
    coloured, safe-de-Bruijn Hamilton circulation.  Section 6 gives an
    exact binary formulation whose integral solutions are literal
    one-frame-per-root braids in that architecture.
    The complete safe-frame catalogue has an exact symmetric fractional
    solution satisfying every root, Hamilton, parity, monodromy, and
    all-depth target row.  Therefore no linear Hamilton/odd-cut
    obstruction can refute the unrestricted catalogue.  The missing
    theorem is integral simultaneous target rounding in the physically
    authorized PBBS/moving-frame subcatalogue.

Thus coefficient one is **not** proved.  What is proved is the exact
monodromy factor system and the sharp distinction between seam count and
component count.  A fixed-top one-frame-per-root PBBS-provenance atlas
cannot be obtained with only \(O(N_H)\) changed-successor occurrences,
but it is not ruled out that \(\Theta(W/H)\) correlated occurrences
close into only \(N_H\) literal rings.  This count is not a lower bound
on distinct global factor edges or on the number of trade packets.

## Imported audited inputs

The new statements below use three earlier proved packages.

1.  The covering-side calibration (0.1)--(0.3), promotion-frame
    literalization, unit-cost append ledger, and the outer compiler are
    imported from
    MATH_ATTACK_O_PROMOTION_RING_GLOBAL_COMMON_HISTORY_20260726.md and
    its audit.
2.  The PBBS word \(i(e)d(e)\), ordered-overlap identity, top-drift
    formula, and fixed-top inherited-run rank are imported from
    MATH_ATTACK_R_PBBS_CRITICAL_PROMOTION_GLOBAL_CHRONOLOGY_20260726.md
    and its independent audit.
3.  The necessity of \(2H\)-letter memory for simultaneous lower and
    upper traces is imported from
    MATH_THEOREM_PROMOTION_TIGHT_PATH_DEBRUIJN_TU_AND_PORT_PAIRING_OBSTRUCTION_20260726.md.

The partial-permutation theorem, authorized factor cuts, exact seam
rounding, abstract one-component example, Hamilton circulation, and
symmetric fractional point are proved in this report.

## 1. Literal top frames and their flags

Let

\[
 A\in\binom{[2m]}{m-H},\qquad U=A^c,qquad |U|=M.
\tag{1.1}
\]

A cyclic permutation

\[
 c=(c_0,c_1,\ldots,c_{M-1})
\tag{1.2}
\]

of \(U\), with indices read modulo \(M\), defines the literal promotion
frame

\[
 D_t=A\cup\{c_t,c_{t+1},\ldots,c_{t+H-1}\}.
\tag{1.3}
\]

For \(0\le q\le H\), its two signed traces are exactly

\[
 \Phi^-_q(A,c,t)
 =A\cup\{c_{t+q},\ldots,c_{t+H-1}\},
\tag{1.4}
\]

\[
 \Phi^+_q(A,c,t)
 =A\cup\{c_t,\ldots,c_{t+H+q-1}\}.
\tag{1.5}
\]

They have ranks \(m-q\) and \(m+q\).  Because \(2H<M\) for all
sufficiently large \(m\), every length-\(2H\) cyclic block of \(c\) is
injective.  Conversely, a closed sequence of overlapping injective
\(2H\)-blocks whose appended letters exhaust \(U\) exactly once is one
cyclic permutation (1.2), and hence gives (1.3)--(1.5) literally.

Opening one cyclic frame and repeating its first \(2H\) letters exposes
all intervals in (1.4)--(1.5).  Thus one frame per root has total collar
at most \(2HN_H=o(W)\).  Thus \(O(N_H)\) physical components have collar
overhead compatible with coefficient one.  Target holes, collisions,
physical packet legality, and any packet implementation cost remain
separate; the number of in-place internal changes of successor does not
by itself enter this collar cost.

## 2. The PBBS ordered word

For an intact clean PBBS segment of \(H\) Johnson transitions, write

\[
 d(e)=(\delta_0,\ldots,\delta_{H-1}),\qquad
 i(e)=(\eta_0,\ldots,\eta_{H-1}).
\tag{2.1}
\]

Strong geodesicity makes the \(2H\) displayed labels distinct.  The
stationary-top/FIFO identity identifies the departure at phase \(j\)
with the arrival at phase \(j+H\).  Therefore the segment occupies the
ordered block

\[
             \boxed{w(e)=i(e)d(e)}
\tag{2.2}
\]

in the arrival-label word of a final promotion frame.

If two consecutive segment starts in one top are separated by
\(H+g\) phases, \(0\le g\le H\), then their words must satisfy

\[
 \operatorname{suffix}_{H-g}d(e)
 =\operatorname{prefix}_{H-g}i(f).
\tag{2.3}
\]

For a cyclic family of \(k\) disjoint intact segments, with gaps
\(g_1,\ldots,g_k\),

\[
                  \sum_{j=1}^k g_j=M-kH.
\tag{2.4}
\]

These are ordered word identities, not set-overlap identities.

The audited PBBS top-drift formula says that the unique raw continuation
after shifting \(s\) phases has

\[
 d_J(U_t,U_{t+s})=s\qquad(1\le s\le m-H).
\tag{2.5}
\]

In particular the raw continuation with \(g=0\) cannot remain in the
same top.  This fact will be used only in Section 5; the word-completion
theorem in Section 3 is independent of PBBS.

## 3. Exact ordered-word completion

Let \(U\) be any finite set of size \(M\).  Let \(\mathcal W\) be a
family of injective oriented words on \(U\).  Form the directed graph
\(P(\mathcal W)\) on \(U\) by inserting the arc \(x_j\to x_{j+1}\) for
every consecutive pair in every word
\((x_0,x_1,\ldots,x_r)\in\mathcal W\).  Repeated copies of the same arc
are identified.

### Theorem 3.1 (partial-permutation completion)

There is a cyclic permutation of \(U\) containing every word of
\(\mathcal W\) as a consecutive oriented block if and only if exactly
one of the following holds.

1.  \(P(\mathcal W)\) is already one directed Hamilton cycle; or
2.  every vertex of \(P(\mathcal W)\) has indegree and outdegree at most
    one, and \(P(\mathcal W)\) has no directed cycle.

In the second case \(P(\mathcal W)\) is a disjoint union of directed
paths, with isolated vertices counted as paths.  If it has \(p\) path
components, every cyclic completion uses exactly \(p\) new successor
arcs, and

\[
                    p=M-|E(P(\mathcal W))|.
\tag{3.1}
\]

#### Proof

The successor relation of a cyclic permutation has indegree and
outdegree one at every vertex.  Hence two imposed distinct successors or
two imposed distinct predecessors are impossible.  Moreover, a directed
cycle contained in a Hamilton cycle must be the whole Hamilton cycle.
This proves necessity.

Conversely, suppose the second condition holds.  A finite directed graph
with indegree and outdegree at most one is a disjoint union of directed
paths and directed cycles.  By hypothesis only paths occur.  List the
path components as \(Q_1,\ldots,Q_p\), and add an arc from the terminal
vertex of \(Q_j\) to the initial vertex of \(Q_{j+1}\), cyclically in
\(j\).  The result is one directed Hamilton cycle on \(U\), and it
contains every imposed word.

An acyclic partial permutation with \(M\) vertices and \(e\) arcs has
\(M-e\) path components.  A Hamilton cycle has \(M\) arcs, so any
completion adds exactly \(M-e=p\) arcs.  The construction attains this
number. \(\square\)

The theorem exposes the first exact obstruction missed by an overlap
weight or a scalar supply count.  A pair of words may have a long set
overlap and still impose two different successors of the same label.
Conversely, once the imposed arcs form an acyclic partial permutation,
there is no further uncoloured completion obstruction when every path
end may be joined to every path start.

Theorem 3.1 treats \(\mathcal W\) as a set of unlabelled containment
obligations: one occurrence may satisfy two identical obligations.  If
distinct physical PBBS segment copies must occupy distinct phase starts,
introduce copy-to-start assignment variables and their injectivity rows.
Those multiplicity rows, as well as owner-resource rows, are additional
to the successor criterion and are not proved feasible by Theorem 3.1.

## 4. Authorized joins: factor, subtour, parity, and voltage equations

Retain the acyclic case of Theorem 3.1 and let its path components be
\(Q_1,\ldots,Q_p\).  Write \(a_j\) and \(b_j\) for the initial and
terminal coordinate of \(Q_j\).  Suppose a physical catalogue declares
which joins \(b_i\to a_j\) are authorized.  Let \(G\) be the resulting
directed graph on \([p]\), and let \(y_{ij}\in\{0,1\}\) denote a chosen
join.  In Theorem 4.1 the join edges are assumed independently
selectable.  If one physical packet supplies several joins jointly, its
packet variable and all resource/port rows must be added; (4.1)--(4.2)
then remain necessary for the endpoint projection but are not by
themselves sufficient for physical packet legality.

### Theorem 4.1 (exact authorized one-component factor)

The imposed PBBS word paths admit a one-component cyclic completion
using only authorized joins if and only if the binary variables \(y\)
satisfy

\[
 \sum_{j:ij\in E(G)}y_{ij}=1\quad(i\in[p]),
 \qquad
 \sum_{i:ij\in E(G)}y_{ij}=1\quad(j\in[p]),
\tag{4.1}
\]

and, for every nonempty proper \(S\subset[p]\),

\[
 \boxed{
 \sum_{i\in S,\,j\notin S}y_{ij}\ge1.}
\tag{4.2}
\]

Equivalently, (4.1) is a directed one-factor and (4.2) excludes every
proper subtour.

#### Proof

Contract each imposed path \(Q_i\).  A cyclic completion gives every
contracted vertex one chosen outgoing and one chosen incoming join, so
(4.1) holds.  If no chosen arc leaves a nonempty proper \(S\), the
chosen one-factor has a cycle contained in \(S\), contradicting the
one-component requirement.  Thus (4.2) holds.

Conversely, (4.1) makes the selected joins a disjoint union of directed
cycles on \([p]\).  If there were two or more cycles, the vertex set of
one would violate (4.2).  Hence the selected joins form one Hamilton
cycle.  Expanding every contracted path gives the required cyclic
permutation of \(U\). \(\square\)

The Hall inequalities

\[
              |N^+(S)|\ge |S|\qquad(S\subset[p])
\tag{4.3}
\]

are necessary and sufficient for (4.1), because (4.1) is a bipartite
perfect matching between path terminals and path initials.  They are not
sufficient for (4.2): a perfect matching may close several subtours.
This is the precise difference between overlap balance and global
monodromy.

There is also a useful exact odd-cut form.  For
\(\varnothing\ne S\subsetneq U\), let \(p_S\) be the number of imposed
arcs of \(P(\mathcal W)\) crossing the undirected cut \(\delta(S)\), and
let \(y_S\) be the number of added joins crossing it.  Every Hamilton
completion obeys

\[
             p_S+y_S\ge2,
 \qquad      p_S+y_S\equiv0\pmod2.
\tag{4.4}
\]

Consequently

\[
 y_S\ge
 \begin{cases}
 2,&p_S=0,\\
 1,&p_S\text{ is odd},\\
 0,&p_S\ge2\text{ is even}.
 \end{cases}
\tag{4.5}
\]

Equation (4.4) follows because every cycle enters a proper vertex set as
many times as it leaves it.  It is an exact parity obstruction, not an
expectation.  For a partition of the contracted paths into \(r\ge2\)
nonempty classes, summing (4.4) over the classes gives at least \(r\)
chosen joins crossing between classes.

### Deck voltage

Let the PBBS quotient deck have cyclic group \(\mathbb Z/L\mathbb Z\).
Give every imposed path \(Q_i\) its internal voltage \(\omega_i\), and
every authorized join \(i\to j\) voltage \(\omega_{ij}\).  The total
voltage of a selected Hamilton completion is

\[
 \Omega(y)=\sum_{i=1}^p\omega_i
            +\sum_{ij\in E(G)}\omega_{ij}y_{ij}\pmod L.
\tag{4.6}
\]

If deck rotation is \(\rho\), closure on the original top requires

\[
                         \rho^{\Omega(y)}U=U.
\tag{4.7}
\]

For a top with trivial rotational stabilizer this is exactly

\[
                         \boxed{\Omega(y)=0\pmod L.}
\tag{4.8}
\]

Thus (4.1), (4.2), and (4.8) are the exact root-dependent
zero-monodromy equations.  An exact voltage-lift encoding must retain
the one-pass base Hamilton projection.  After anchoring \(g_1=0\),
assign one sheet \(g_i\in\mathbb Z/L\mathbb Z\) to every contracted path
and impose

\[
 g_j\equiv g_i+\omega_i+\omega_{ij}\pmod L
 \qquad\text{whenever }y_{ij}=1.
\tag{4.9}
\]

Following the selected base Hamilton cycle assigns all \(g_i\)
successively, and the assignment closes at \(g_1=0\) if and only if
(4.8) holds.  Equivalently, with lifted binary arc variables
\(\widehat y_{ijg}\), one must impose
\(\sum_g\widehat y_{ijg}=y_{ij}\), lifted flow conservation, and exactly
one selected sheet-copy of each base vertex.  An unrestricted ordinary
circulation in the voltage lift is **not** equivalent: it may traverse a
nonzero-voltage base cycle repeatedly until the accumulated voltage
vanishes.

More generally, if all
admissible connector voltages lie in one coset \(c+K\) of a subgroup
\(K\le\mathbb Z/L\mathbb Z\), a completion using \(p\) connectors is
possible only if

\[
       -\sum_i\omega_i\in pc+K.
\tag{4.10}
\]

This is an exact monodromy obstruction whenever the displayed coset
condition fails.

Assume, as in the audited cyclic PBBS quotient, that \(\rho\) acts as one
regular \(L\)-cycle on the coordinates and that the critical top layer
has size \(2^{L-o(L)}\).  A nonidentity rotation then has at most \(L/2\)
coordinate orbits, so at most \(L2^{L/2}\) subsets are fixed by some
nonidentity rotation.  The stabilized fraction is exponentially small.
It may be quarantined at \(o(W)\) cost whenever the per-top quarantine
cost is \(2^{o(L)}\), in particular for the polynomial promotion-frame
cost used here.  On the remaining tops (4.8), not merely (4.7), is
forced.  If stabilized tops are retained, their exact condition is
(4.7), and imposing (4.8) there would be unnecessarily strong.

### A component lower bound supplied by the factor graph

Let \(r_A\) be the number of strongly connected components of the
authorized connector digraph \(G_A\).  Every directed cycle lies wholly
inside one strongly connected component.  A directed cycle factor covers
every contracted path, so it contains at least one selected cycle in
every strongly connected component.  Therefore every rootwise braid in
the stated catalogue satisfies

\[
                         C\ge\sum_A r_A.
\tag{4.11}
\]

In particular, \(\sum_A r_A\not=O(N_H)\) is an exact obstruction to the
desired component count.  The presently certified PBBS overlap data do
not prove such a bound: absence of a full-overlap edge does not make the
near-overlap graph split into many closed classes.

## 5. The exact fixed-top PBBS-provenance seam lower bound

We now apply only the audited fact that raw full-overlap continuation
leaves the top.

### Theorem 5.1 (exact inherited-run seam lower bound)

In one literal fixed-top frame of length \(M\), call a successor edge
**inherited** if it is the directed successor edge of the audited PBBS
factor occurrence.  Let \(s\) be the number of non-inherited successor
edges.  Then

\[
             \boxed{s\ge
             \left\lceil {M\over H+1}\right\rceil.}
\tag{5.1}
\]

Consequently any one-frame-per-root PBBS-provenance atlas has

\[
 \boxed{S_{\rm new}\ge
 N_H\left\lceil {M\over H+1}\right\rceil
 =(1+o(1)){W\over H}.}
\tag{5.2}
\]

Here \(S_{\rm new}\) counts final root-frame successor **occurrences**
with multiplicity.  If the same abstract factor edge or one compound
trade services several occurrences, it is still counted several times
in (5.2).  Thus (5.2) is not a lower bound on distinct factor edges,
trade variables, or literal letters.

#### Proof

A run of \(a\) consecutive inherited owner occurrences follows one raw
PBBS path.  Strong geodesicity makes its union have rank \(m+a-1\).
If the run lies in a fixed top of rank \(m+H\), then \(a\le H+1\).
Thus every maximal inherited run in the final cyclic frame contains at
most \(H+1\) owners, equivalently at most \(H\) inherited edges.

The whole frame cannot be one inherited run.  Cutting immediately after
each of its \(s\) non-inherited successor edges decomposes the \(M\)
cyclic owner positions into \(s\) maximal inherited runs, with an
isolated position counted as a run of one owner.  Therefore

\[
                         M\le s(H+1),
\tag{5.3}
\]

which proves (5.1).  Sum over the \(N_H\) roots.  Finally,

\[
 N_H\left\lceil {M\over H+1}\right\rceil
 ={MN_H\over H+1}+O(N_H)
 =(1+o(1)){W\over H},
\tag{5.4}
\]

because \(MN_H=W+o(W)\) and
\(N_H=o(W/H)\). \(\square\)

The ceiling in (5.1) is sharp at the provenance-pattern level.  With
\(s_0=\lceil M/(H+1)\rceil\), partition the \(M\) cyclic owner positions
into \(s_0\) nonempty intervals, each of length at most \(H+1\), and put
one non-inherited edge between successive intervals.  This does not
assert that the resulting intervals can all be chosen from the physical
PBBS catalogue.

The full-overlap statement gives the same local boundary in ordered-word
language.  Two intact \(H\)-transition blocks with start separation
\(H\) would share their endpoint owner and impose

\[
                       d(e_j)=i(e_{j+1}).
\tag{5.5}
\]

Exact directed ownership makes the second block the raw continuation of
the first.  It starts \(H\) raw phases later, while (2.5) gives Johnson
top distance \(H\); hence it cannot remain in the same top.  Every full
inherited block must therefore be followed by at least one
non-inherited successor edge.

### Corollary 5.2 (exact full-block residue, not a seam count)

Suppose a fixed-top frame contains \(k\) transition-disjoint intact PBBS
segments of \(H\) transitions.  Then

\[
 k\le\left\lfloor {M\over H+1}\right\rfloor.
\tag{5.6}
\]

If \(b_{\rm out}=M-kH\) is the number of frame transitions outside
those selected full blocks, then

\[
 b_{\rm out}\ge
 b_0(M,H):=M-H\left\lfloor {M\over H+1}\right\rfloor.
\tag{5.7}
\]

Writing

\[
             M=q(H+1)+r,\qquad 0\le r\le H,
\tag{5.8}
\]

gives the exact floor baseline

\[
                         b_0(M,H)=q+r.
\tag{5.9}
\]

#### Proof

The \(H\) inherited edges of a full segment and its required outgoing
non-inherited edge form a package of \(H+1\) frame edges.  These packages
are disjoint for transition-disjoint segments, proving (5.6).  The
definition of \(b_{\rm out}\) then gives (5.7), and substituting (5.8)
gives (5.9). \(\square\)

It is important that \(b_{\rm out}\) is not the seam count \(s\).
Transitions in a shorter inherited tail lie outside every selected full
block but are not new successors.  Moreover the residue \(r\) in (5.9)
can be as large as \(H\), so one may not replace
\(N_Hb_0(M,H)\) by \((1+o(1))W/H\) without an additional congruence
hypothesis.  The exact unconditional occurrence lower bound within the
fixed-top, one-frame-per-root provenance class is (5.2); attainability
is known only for the abstract run-length pattern.

There is an equivalent provenance statement at the critical depth.  An
intact \(H\)-transition segment certifies only its own initial phase as
a completely inherited depth-\(H\) fan.  Therefore the total number of
fully inherited critical starts in all final frames is at most

\[
 N_H\left\lfloor{M\over H+1}\right\rfloor
 =(1+o(1)){W\over H}=o(W).
\tag{5.10}
\]

Thus \(W-o(W)\) critical phase occurrences must have genuinely
cross-segment chronology.  This is not a hole lower bound: those new
chronologies may be exactly the ones which cancel the Gaussian target
deficits.

The distinction from a component bound is essential.  Two consecutive
\(2H\)-words may overlap in \(H-1\) letters while their corresponding
owner segments still have one non-PBBS transition between them.  Many
such joins can form one long directed coordinate path, and one final arc
can close that path.  Consequently (5.2) does not imply
\(\Omega(W/H)\) literal components or \(\Omega(W)\) collar cost.

### Proposition 5.3 (gap density alone has zero component force)

Let \(H\ge2\), let \(M=k(H+1)>2H\), and let
\(c=(c_0,\ldots,c_{M-1})\) be any cyclic permutation.  For
\(0\le j<k\), put

\[
 w_j=(c_{j(H+1)},c_{j(H+1)+1},\ldots,
             c_{j(H+1)+2H-1}),
\tag{5.11}
\]

with indices modulo \(M\).  Then:

1. every \(w_j\) is injective;
2. the directed suffix of \(w_j\) and prefix of \(w_{j+1}\) overlap in
   exactly \(H-1\) ordered letters, so no pair is a full-overlap
   continuation at start distance \(H\); and
3. the union of their imposed coordinate-successor arcs is already the
   Hamilton cycle \(c_0\to c_1\to\cdots\to c_{M-1}\to c_0\).

#### Proof

Injectivity follows from \(2H<M\).  Successive starts differ by \(H+1\),
so the directed suffix of one length-\(2H\) word and prefix of the next
have overlap length \(2H-(H+1)=H-1\).  This is an ordered
suffix--prefix assertion, not a claim about the set intersection of the
two cyclic position intervals; for \(k=2\) that set intersection is
larger.  All start differences are multiples of \(H+1\), and none is
congruent to \(H\) modulo \(M=k(H+1)\), proving the second assertion.

The word \(w_j\) contains every cyclic successor edge whose index lies
from \(j(H+1)\) through \(j(H+1)+2H-2\).  Since
\(2H-1\ge H+1\), these cyclic edge intervals cover all \(M\) successor
edges.  They are all arcs of \(c\), so their union is exactly the one
Hamilton cycle. \(\square\)

This is an abstract ordered-word example, not a claim that the displayed
words occur in the PBBS segment catalogue.  It proves that the audited
facts “one gap per \(H\)-block” and “no full overlap” cannot, by
themselves, imply any component lower bound.  A negative PBBS theorem
must use an actual endpoint Hall deficit, closed overlap class, voltage,
or coloured target invariant.

## 6. The exact common-tag all-depth Hamilton-circulation formulation

This section puts the ordered-overlap, component, middle, and signed
target conditions into one integral system for the common symmetric
nested-tag architecture: at every depth the \(+\) and \(-\) traces use
the same active phase set.  It is not an equivalence to every conceivable
all-depth literal architecture, and it is not a claim of feasibility for
the PBBS physical subcatalogue.  Throughout this section
\(1\le2H<M\), as holds for all sufficiently large \(m\) in (0.1).

For a root \(A\), let \(\mathcal B_A\) be the injective de-Bruijn graph
with

* vertices the injective \((2H-1)\)-words on \(U=A^c\); and
* arcs the injective \(2H\)-words
  \(e=(z_0,z_1,\ldots,z_{2H-1})\), directed from its prefix of length
  \(2H-1\) to its suffix of length \(2H-1\).

An arc emits the exact colours

\[
 \kappa_0(A,e)=A\cup\{z_0,\ldots,z_{H-1}\},
\tag{6.1}
\]

\[
 \kappa_q^-(A,e)=A\cup\{z_q,\ldots,z_{H-1}\},
 \qquad
 \kappa_q^+(A,e)=A\cup\{z_0,\ldots,z_{H+q-1}\}.
\tag{6.2}
\]

These are exactly (1.3)--(1.5).  If physical provenance matters, replace
an arc by provenance-indexed copies \((e,\xi)\); all equations below use
the word projection \(e\), while resource and legality rows use \(\xi\).
This notation does not declare different copies independently
selectable.  If one exact trade or collar simultaneously supplies a set
of arcs, introduce its binary packet variable and impose all incidence,
owner-resource, and port-pairing equations linking that variable to the
corresponding \(z\)'s.  Below, a **specified physical catalogue** means
the resulting globally legal integral selection family, not merely a
list of locally legal individual arcs.

Let \(z_{A,e,\tau}\in\{0,1\}\), where \(0\le\tau\le H\) is a common
nested stopping tag: the phase emits both signed colours through exactly
the depths \(q\le\tau\).  Put

\[
                         z_{A,e}=\sum_{\tau=0}^H z_{A,e,\tau}.
\tag{6.3}
\]

The root-local state equations are

\[
 \sum_{e:t(e)=v}z_{A,e}
 =\sum_{e:h(e)=v}z_{A,e},
 \qquad
 \sum_{e:t(e)=v}z_{A,e}\le1.
\tag{6.4}
\]

Define the coordinate-successor variables

\[
 r^A_{xy}
 =\sum_{e:\,(z_{2H-2},z_{2H-1})=(x,y)}z_{A,e}.
\tag{6.5}
\]

Impose

\[
 \sum_{y\in U}r^A_{xy}=1,\qquad
 \sum_{x\in U}r^A_{xy}=1,
\tag{6.6}
\]

and, for every nonempty proper \(S\subset U\),

\[
                 \sum_{x\in S,\,y\notin S}r^A_{xy}\ge1.
\tag{6.7}
\]

If the chosen arcs carry PBBS deck voltages, impose (4.7).  On
trivial-stabilizer tops this is the zero-voltage row (4.8), equivalently
the one-pass sheet system (4.9).  Stabilized tops must either retain
(4.7) or be quarantined under the preceding exponential census.

For the common tag census, impose

\[
 \sum_{A,e}\sum_{\tau\ge q}z_{A,e,\tau}=N_q
 \qquad(1\le q\le H),
\tag{6.8}
\]

where \(N_q=\binom{2m}{m-q}\).  At depth zero all \(MN_H=W+o(W)\)
phases are retained.  Define the integral target loads

\[
 \mu_{q,T}^{\pm}
 =\sum_{A,e:\,\kappa_q^{\pm}(A,e)=T}
       \sum_{\tau\ge q}z_{A,e,\tau},
\tag{6.9}
\]

and

\[
 \mu_{0,D}
 =\sum_{A,e:\,\kappa_0(A,e)=D}z_{A,e}.
\tag{6.10}
\]

For each sufficiently large \(m\), let \(\mathcal D_m\) denote the
following integral defect.  A sequence of solutions has the literal
constant-one target when \(\mathcal D_m/W\to0\); this is abbreviated by
\(\mathcal D_m=o(W)\):

\[
 \mathcal D_m:=
 \sum_D(1-\mu_{0,D})_+
 +\sum_D(\mu_{0,D}-1)_+
 +\sum_{q=1}^H\sum_{\pm,T}(1-\mu_{q,T}^{\pm})_+
 =o(W).
\tag{6.11}
\]

Because (6.8) equals the number of rank-\(m\pm q\) targets, the signed
hole and repeat totals agree at every \(q\ge1\).  At the middle rank,
repeat excess minus holes is the calibrated quantity
\(MN_H-W=O(WH/m)=o(W)\).

### Theorem 6.1 (common-tag zero-monodromy Hamilton equivalence)

For a specified globally legal physical catalogue in the preceding
sense, integral solutions of (6.3)--(6.10), together with its packet and
resource rows, are equivalent to root-dependent literal promotion frames
with

1. one cyclic coordinate frame for every root;
2. exact ordered overlap through both signed depths \(0\le q\le H\);
3. the specified physical provenance and deck closure; and
4. the common integral stopping tags counted in (6.8).

Every such solution has exactly \(N_H\) cyclic components before
linearization.  Put

\[
 h_0=\sum_D(1-\mu_{0,D})_+,\qquad
 h_q^\pm=\sum_T(1-\mu_{q,T}^\pm)_+.
\]

Let \(K_{\rm phys}\ge0\) be the additional literal length, if any, needed
to implement the selected physical packet variables beyond the chosen
frame words and their ordinary opening collars.  Thus
\(K_{\rm phys}=0\) for a direct literal-frame construction or for
genuinely in-place zero-cost trades.  Using the already audited
promotion-frame literalization and unit-cost hole append lemma, the exact
band-word bound is

\[
 L_{\le H}\le MN_H+2HN_H+h_0+
                \sum_{q=1}^H(h_q^-+h_q^+)+K_{\rm phys}.
\tag{6.12}
\]

For a sequence of solutions with (6.11) and
\(K_{\rm phys}=o(W)\), the already audited outer compiler for ranks
beyond \(H\) then gives a literal contiguous-OR word of length
\(W+o(W)\).

#### Proof

For fixed \(A\), equations (6.4) select vertex-disjoint directed cycles
in the safe de-Bruijn graph.  Equations (6.5)--(6.6) say that their last
coordinate adjacencies form a permutation of \(U\).  Summing either
degree equation in (6.6) gives

\[
                         \sum_e z_{A,e}=M.
\]

Equation (6.7) says the coordinate permutation has no proper cycle,
hence is one Hamilton cycle.  Each selected de-Bruijn component projects
through its last coordinate pairs to a nonempty closed directed trail in
that Hamilton cycle.  The edge set of one simple Hamilton cycle cannot
split into two nonempty closed trails, so there is exactly one selected
de-Bruijn component.  Its successive arcs overlap in \(2H-1\) ordered
labels, and overlap determines them as precisely the cyclic
\(2H\)-windows of the Hamilton coordinate word.  It is therefore one
literal frame (1.2).  The converse selects the cyclic \(2H\)-windows of
a frame and is immediate.

The formulas (6.1)--(6.2) prove the all-depth trace claim.  The single
tag \(\tau\) at a phase makes the two signed activation sets common and
nested, and (6.8) gives their exact census.  The one-pass sheet system
(4.9) returns to its initial physical sheet exactly when (4.8) holds.
For a retained stabilized top, geometric closure is instead the weaker
condition (4.7).

There is one cycle for each of the \(N_H\) roots.  Linearizing them costs
at most \(2HN_H\), and their principal length is \(MN_H\).  Appending
each actually missing middle or signed target once gives (6.12);
collision repetitions are already included in the principal length and
are not charged a second time.  Add \(K_{\rm phys}\) for any physical
implementation length not already present in those words.  Now
\(MN_H=W+o(W)\), \(2HN_H=o(W)\), and (6.11) makes every displayed hole
term \(o(W)\).  Under \(K_{\rm phys}=o(W)\), the calibrated outer
compiler also contributes only \(o(W)\).  Every emitted target is an
actual consecutive intersection or union by (6.1)--(6.2), so the result
is a literal OR word, not a labelled synchronization surrogate.
\(\square\)

### Corollary 6.2 (the \(O(N_H)\)-component relaxation)

Drop the one-Hamilton requirement (6.7), retain (6.4)--(6.6), and let
\(c_A\) be the number of cycles in the resulting coordinate permutation
\(r^A\).  Then the selected safe de-Bruijn arcs over root \(A\) have
exactly \(c_A\) components.  With

\[
                         C=\sum_A c_A,
\]

the exact analogue of (6.12) is

\[
 L_{\le H}\le MN_H+2HC+h_0+
                \sum_{q=1}^H(h_q^-+h_q^+)+K_{\rm phys}.
\tag{6.13}
\]

In particular \(C=O(N_H)\) gives \(2HC=o(W)\).

#### Proof

Every selected safe-state component projects to a nonempty closed trail
in one cycle of \(r^A\).  Conversely, the edge set of one simple cycle
of \(r^A\) cannot split into two nonempty closed trails.  Hence there is
exactly one safe-state component over each coordinate cycle.  Open every
component with its ordinary \(2H\)-collar and repeat the proof of
Theorem 6.1. \(\square\)

This relaxation does not linearize the requirement \(C=O(N_H)\);
cycle-count control is an additional integral side condition.  It does
show that one Hamilton cycle per root is stronger than necessary and
that the exact ordered-state formulation naturally covers the
\(O(N_H)\)-component target in the question.

The diagonal occurrence port is not lost in this formulation: a target
colour is emitted by the same selected ordered arc that carries its
history.  Splitting a target into an ordinary flow node and pairing an
incoming occurrence with an unrelated outgoing occurrence would weaken
(6.9) and is not allowed.

## 7. Fractional feasibility and the exact remaining integer gate

The unrestricted literal safe-frame catalogue has a symmetric
fractional point which passes every cut valid for that unrestricted hull.
No PBBS provenance or voltage restriction is imposed in this section.

### Proposition 7.1 (uniform one-cycle fractional atlas)

Average uniformly over all cyclic permutations of every top \(U\).  At
depth \(H\), choose one uniformly random phase in each root.  Moving
downward from \(H\) to \(1\), extend these active phases, uniformly and
nestedly over the global phase set, until exactly \(N_q\) phases are
active at depth \(q\).  Average also over all such extensions.

The resulting fractional point lies in the convex hull of literal
one-cycle, zero-monodromy frames.  It satisfies (6.3)--(6.8) and every
linear subtour or parity inequality valid for those frames.  Moreover

\[
                    \mu_{q,T}^{\pm}=1
 \qquad(1\le q\le H)
\tag{7.1}
\]

for every target \(T\), while

\[
                    \mu_{0,D}={MN_H\over W}=1+o(1)
\tag{7.2}
\]

for every middle owner \(D\).

#### Proof

Each sampled object consists of one genuine literal Hamilton frame per
root, so all root-local flow, degree, subtour, parity, and geometric
zero-monodromy conditions hold before averaging.  Nested extension is
possible because
\(N_1\ge N_2\ge\cdots\ge N_H\), and it gives (6.8) exactly.

The joint distribution is invariant under every permutation of
\([2m]\).  The symmetric group is transitive on the targets at each
fixed rank.  The total active mass at rank \(m-q\), and separately at
rank \(m+q\), is \(N_q\), equal to the number of targets at that rank;
hence every target has fractional load one.  At depth zero the total mass
is \(MN_H\) and there are \(W\) middle targets, proving (7.2).
\(\square\)

This proposition has two consequences.

* There is no Farkas certificate, Hamilton cut, parity cut, or additive
  monodromy character separating the complete safe-frame catalogue from
  the desired all-depth fractional loads.
* It does not round the common frame choice.  An integral selection must
  realize all ranks with the **same** root frames and the same phase
  tags.  The known determinant-two port minor shows that ordinary
  network total unimodularity cannot supply this rounding.

The first conclusion concerns only inequalities valid for the
unrestricted literal frame hull.  A physical PBBS subcatalogue may still
have a Hall, voltage, or provenance obstruction excluded by that
subcatalogue's additional rows.

For a physically authorized PBBS/moving-frame catalogue, the exact
remaining alternative is now explicit.

### Gate ZMB\(_H\)

Either construct, for all sufficiently large admissible \(m\), a
sequence of integral solutions of (6.3)--(6.10) with
\(\mathcal D_m/W\to0\) and \(K_{\rm phys}/W\to0\), with every
non-PBBS arc implemented by a literal exact-factor trade or by the
resulting literal frame itself, or exhibit one of the following for that
physical catalogue:

1. a Hall-deficient endpoint set (4.3);
2. a violated directed subtour or parity cut (4.2), (4.4);
3. failure of the stabilizer condition (4.7), which is nonzero voltage
   (4.8) on a trivial-stabilizer top, or the coset obstruction (4.10);
4. authorized connector digraphs with
   \(\sum_A\operatorname{scc}(G_A)\not=O(N_H)\); or
5. a common all-depth coloured integer-hull inequality separating
   (6.11), while retaining diagonal occurrence ports.

Within the fixed-top, one-frame-per-root PBBS-provenance class, the
chronology theorem supplies the quantitative restriction (5.2): every
solution has at least \((1+o(1))W/H\) non-inherited successor
occurrences.  It does not presently supply any item 1--5, a lower bound
on distinct global trade edges, or a matching physical upper bound.

## 8. Audited boundary

### Proved here

1.  The exact partial-permutation criterion for ordered PBBS word
    completion, including the exact number of added coordinate arcs.
2.  For independently selectable joins, the authorized-join factor
    formulation, Hall condition, binary subtour characterization, parity
    cut, and cyclic deck-voltage row.
3.  The exact fixed-top PBBS-provenance occurrence bound
    \(N_H\lceil M/(H+1)\rceil=(1+o(1))W/H\), together with the separate
    exact full-block residue
    \(b_0=M-H\lfloor M/(H+1)\rfloor\).
4.  The consequent impossibility of bounded non-inherited successor
    occurrences per root within that compiler class.
5.  An explicit all-\(H\) ordered-word family showing that the same seam
    density can already lie in one Hamilton coordinate component.
6.  The exact common-tag safe-\(2H\)-memory Hamilton/cycle-factor
    circulation, including the identity between coordinate cycles and
    physical safe-state components and the \(2HC\) collar ledger.
7.  The symmetric common-tag fractional point in the unrestricted
    literal safe-frame hull, satisfying every uncoloured factor, cut,
    parity, and geometric monodromy constraint.

### Not proved

1.  A topwise selection of the global PBBS clean-segment bank satisfying
    the authorized Hamilton cuts.
2.  An integral common-frame rounding of Proposition 7.1.
3.  Middle collision excess and aggregate signed holes \(o(W)\) for one
    physical selection.
4.  A physical packet installation with \(K_{\rm phys}=o(W)\).
5.  A PBBS-specific SCC, odd-cut, or voltage lower bound large
    enough to force \(\omega(N_H)\) components.
6.  That common symmetric nested tags are without loss among every
    conceivable literal all-depth architecture.
7.  Coefficient one.

### Independent audit of the decisive count

The PBBS-specific input in Theorem 5.1 is the already audited
fixed-top inherited-run bound: at most \(H+1\) owners, hence at most
\(H\) inherited transitions, occur in one run.  If a cyclic frame has
\(s\) non-inherited successor edges, those edges cut its \(M\) owners
into \(s\) such runs.  Thus \(M\le s(H+1)\) and
\(s\ge\lceil M/(H+1)\rceil\), with no floor ambiguity.  Independently,
packing full \(H\)-transition blocks gives
\(k\le\lfloor M/(H+1)\rfloor\); writing
\(M=q(H+1)+r\) gives the outside-block mass \(b_0=q+r\).  The latter is
not a changed-successor count when a short inherited tail is present.
Theorem 3.1 separately verifies that arbitrarily many changed successors
may occur inside one final Hamilton component.  No step converts (5.2)
into an extra-letter or component lower bound.

The precise boundary is therefore:

> Fixed-top, one-frame-per-root PBBS-provenance braids with bounded
> occurrence seams per root are rigorously closed.  A braid in that
> class with \(N_H\) components remains possible only if it performs at
> least \((1+o(1))W/H\) correlated successor occurrences and solves the
> integral coloured Hamilton circulation ZMB\(_H\).  Monodromy and all
> uncoloured odd cuts alone do not rule it out.
