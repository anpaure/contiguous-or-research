# A low-slack expansion theorem for the marked `K17` rainbow path and residual port flow

Date: 2026-07-31  
Status: exact abstract theorem, exact radius-one scoped obstruction, and
authenticated `OPTIMAL28` marked path plus connected conditioned residual
flow; the nonflat lower-palette target and upper ranks at least `13` are
complete, while residence/exact inversion, upper ranks `10--12`, common cap,
and a `K17` word remain open

## 0. Result

There are two separate facts.

First, after a residence-clean marked component path has been chosen, its
effect on the residual `U`-to-port flow is controlled by an exact cut-loss
functional.  If the path uses `h` pure owners, then it can damage any old
Hall cut by at most `2h`.  Consequently only old cuts of slack strictly
below `2h` need be protected.  For the proposed `106`-component `K17`
bank, `h=105`, so the residual **degree-flow** correlation reduces to the
old cut bank of slack below `210`.  Rainbow path legality, connected
topology, upper/deep palettes, and the common cap remain separate.

Second, this gives a genuine probabilistic/expansion theorem.  Take any
finite family of residence-safe transversal Hamilton paths in the marked
component transition graph, before enforcing distinct `U` labels.  Count

1. pairs of path arcs carrying the same `U` label; and
2. inclusion-minimal arc packets which overload one old Hall cut of slack
   below `2h`.

If the total number of paths containing one of these certificates is less
than the size of the path family, then some path is simultaneously rainbow
and residual-flow extendible.  A cylinder-probability version and an
asymmetric-LLL version follow immediately.  There is also a deterministic
fresh-booster criterion: every partial path cover can be merged whenever
its flow-safe cross-arc bank contains more arcs than all already used labels
can account for.

These results do not finish the current finite instance, but their
clean-bank premise is now met.  The original whole-component closure had six
components with `32` strict internal depth-two runs.  Six explicit
occurrence swaps replace that occurrence selection by one whose marked
closure still has
`106` components, now only `154` macros, and has zero strict internal D2 or
D3 debt.  Global replay confirms that the repaired macro graph is a linear
forest with `5005` components and that its unconditioned port flow is
`10010/10010`.

There is nevertheless an exact pre-LLL obstruction, now known throughout
the complete radius-one occurrence neighbourhood.  The original repaired
fixed-port transition graph has `312` clean directed arcs on `140` labels
and an isolated component `77`.  Of all `1430` one-occurrence alternatives,
`1411` preserve residence and `122` remove every isolated marked component,
but none is connected and none even satisfies the degree necessity for a
Hamilton path.  The minimum forced-leaf count is `21`.  Thus isolation is a
cheap local symptom, while component rank and forced-leaf count are the
first genuinely global occurrence events.  The slack-`<210` path theorem
can be used only after a radius-two (or stronger) occurrence state passes
this deterministic support sieve.

An alternative, larger packet catalogue now closes both of those finite
existence rows.  The authenticated `OPTIMAL28` object gives a literal
residence-clean path through all `106` marked components using `28` optional
components and `133` distinct pure-`U` connectors.  After conditioning on
that path, an exact residual assignment fills all `9744` half-demands and
the complete port graph is one cycle on all `6435` ports.  Thus marked-path
existence and connected conditioned completion are witnessed in this packet
face; the radius-two whole-component question is no longer required for
those two finite rows.  The remaining global gates are residence of the
nonflat zipper (equivalently exact replay after the already nonempty
envelopes), the first three upper ranks, and one exact common-cap/compiler
assignment.  Upper ranks `13--17` are already complete in the literal
interval scan.

## 1. Port-flow notation

Let

\[
  \mathcal T=\binom{\Omega}{r},\qquad
  \mathcal U=\binom{\Omega}{r+1},
\]

and let \(F\) be a linear macro forest on \(\mathcal T\).  Put

\[
                         d_T=2-\deg_F(T).                 \tag{1.1}
\]

Assume the zero-slack identity

\[
                  \sum_{T\in\mathcal T}d_T=2|\mathcal U|. \tag{1.2}
\]

A connector state labelled by `U` uses two distinct facets of `U`, hence
two port incidences.  Let `Q` be a legal marked-component path using a set
`L(Q)` of `h` distinct labels.  Write

\[
 \eta_T(Q)=\#\{\text{incidences of }Q\text{ at }T\},\qquad
 d_T^Q=d_T-\eta_T(Q).                                  \tag{1.3}
\]

Legality includes nonrepeated halfports, so
\(0\le\eta_T(Q)\le d_T\), and

\[
 \sum_T\eta_T(Q)=2h,\qquad
 \sum_Td_T^Q=2|\mathcal U\setminus L(Q)|.              \tag{1.4}
\]

For \(A\subseteq\mathcal U\), put

\[
 n_A(T)=|\{U\in A:T\subset U\}|                         \tag{1.5}
\]

and define the old Hall slack

\[
 \rho(A)=\sum_T\min(d_T,n_A(T))-2|A|.                  \tag{1.6}
\]

The unperturbed port flow is feasible exactly when \(\rho(A)\ge0\) for
every \(A\).

## 2. Exact partial-extension loss

### Theorem 2.1 (cut loss of a fixed marked path)

Let `Q` be a legal rainbow marked path.  It extends to an integral residual
degree flow if and only if, for every
\(A\subseteq\mathcal U\setminus L(Q)\),

\[
                         \rho(A)\ge \ell_Q(A),           \tag{2.1}
\]

where

\[
\begin{aligned}
 \ell_Q(A)
  &=\sum_T\bigl[\min(d_T,n_A(T))
             -\min(d_T-\eta_T(Q),n_A(T))\bigr]\\
  &=\sum_T\min\!\left(\eta_T(Q),
             \bigl(n_A(T)-d_T+\eta_T(Q)\bigr)_+\right).
                                                               \tag{2.2}
\end{aligned}
\]

In particular,

\[
                         0\le\ell_Q(A)\le2h.             \tag{2.3}
\]

#### Proof

After fixing `Q`, use the network

\[
 s\longrightarrow U\longrightarrow T\longrightarrow t,
\]

with source capacity two at every unused `U`, unit containment arcs, and
sink capacity `d_T^Q`.  Max-flow/min-cut gives

\[
 2|A|\le\sum_T\min(d_T-\eta_T(Q),n_A(T))               \tag{2.4}
\]

for every unused-owner set `A`.  Subtracting (2.4) from the definition of
\(\rho(A)\) gives (2.1).  For numbers \(d,n,\eta\) with
\(0\le\eta\le d\),

\[
 \min(d,n)-\min(d-\eta,n)
 =\min\bigl(\eta,(n-d+\eta)_+\bigr),                  \tag{2.5}
\]

which proves (2.2).  Each summand is at most \(\eta_T(Q)\); summing and using
(1.4) proves (2.3).  Integral capacities make the resulting full flow
integral.  \(\square\)

### Corollary 2.2 (the low-slack bank)

For a path of \(h\) connectors, cuts with \(\rho(A)\ge2h\) can never
obstruct.
It is necessary and sufficient to check (2.1) only on

\[
 \mathfrak L_h(Q)=
 \{A\subseteq\mathcal U\setminus L(Q):\rho(A)<2h\}.   \tag{2.6}
\]

For a path family with varying labels, write

\[
 \mathfrak L_h^\circ=\{A\subseteq\mathcal U:\rho(A)<2h\}; \tag{2.7}
\]

the condition `labels avoid A` in Section 3 then selects the appropriate
member of \(\mathfrak L_h(Q)\).

Thus the uniform expansion condition

\[
 \rho(A)\ge2h
 \quad\text{for every relevant residual owner set }A    \tag{2.8}
\]

is sufficient for **every** legal rainbow `h`-connector path to extend.
It is deliberately only sufficient: tight or low-slack cuts may still be
compatible with a specially chosen path.

### Corollary 2.3 (full and one-missing residual stars)

Let \(\mathcal U_Q=\mathcal U\setminus L(Q)\) and
\(N_Q(T)=\{U\in\mathcal U_Q:T\subset U\}\).  For
\(R\subseteq\mathcal U_Q\), define

\[
\begin{aligned}
 F_2(R)&=\{T:d_T^Q=2,\ N_Q(T)\subseteq R\},\\
 F_1(R)&=\{T:d_T^Q=1,\ N_Q(T)\subseteq R\},\\
 A_2(R)&=\{T:d_T^Q=2,\ |N_Q(T)\setminus R|=1\}.
                                                               \tag{2.9}
\end{aligned}
\]

Then residual degree flow exists if and only if

\[
       2|F_2(R)|+|F_1(R)|+|A_2(R)|\le2|R|             \tag{2.10}
\]

for every \(R\).  Indeed, complement
\(A=\mathcal U_Q\setminus R\) in
(2.4), use (1.4), and expand

\[
 \sum_T\bigl(d_T^Q-|N_Q(T)\setminus R|\bigr)_+\le2|R|. \tag{2.11}
\]

Since `d_T^Q<=2`, only a full residual star or a demand-two star missing
one owner contributes.  This is the exact profile-compressed separation
oracle for a proposed path.

## 3. A path-family counting theorem

Let `D` be the directed occurrence-labelled transition catalogue on the
marked components.  An arc `e` records

* its two oriented component endpoints;
* its pure-owner label \(\lambda(e)\in\mathcal U\);
* its two consumed port incidences; and
* acceptance by the exact boundary-run predicate.

Let \(\mathscr H\) be a finite nonempty family of transversal directed
Hamilton paths in `D`: every member visits every marked component once, but
its arc labels are not assumed distinct.  Every path has `h=m-1` arcs.
For an arc set `J`, let

\[
       N(J)=|\{P\in\mathscr H:J\subseteq E(P)\}|.       \tag{3.1}
\]

For \(A\subseteq\mathcal U\), define \(\mathscr W_A\) to be the family of
inclusion-minimal arc sets `J` satisfying all of the following:

1. the arcs in `J` can occur together in a transversal path;
2. their labels are distinct and avoid `A`;
3. their combined port consumption satisfies
   \(\eta_T(J)\le d_T\) for every port `T`; and
4. \(\ell_J(A)>\rho(A)\), with \(\ell_J\) defined by (2.2).

Call these the **minimal active cut packets**.  They are empty whenever
\(\rho(A)\ge2h\).

Let

\[
 \mathscr C=\{\{e,f\}:e\ne f,\ \lambda(e)=\lambda(f)\} \tag{3.2}
\]

be the repeated-label certificates.

### Theorem 3.1 (diverse path-family criterion)

If

\[
 \boxed{
 \sum_{\{e,f\}\in\mathscr C}N(\{e,f\})
 +\sum_{A\in\mathfrak L_h^\circ}\ \sum_{J\in\mathscr W_A}N(J)
 <|\mathscr H|,
 }                                                        \tag{3.3}
\]

then \(\mathscr H\) contains a residence-safe rainbow marked-component path
which has an integral residual degree flow.

#### Proof

A path with a repeated label contains a member of \(\mathscr C\).  If a
rainbow path has no residual flow, Theorem 2.1 supplies a set
\(A\subseteq\mathcal U\setminus L(P)\) with
\(\ell_P(A)>\rho(A)\).  Delete path
arcs from `E(P)` until this inequality is inclusion-minimal.  The remaining
set is a member of \(\mathscr W_A\); by (2.3),
\(A\in\mathfrak L_h^\circ\).

Hence every bad path is counted at least once on the left of (3.3).  If all
paths were bad, that left side would be at least \(|\mathscr H|\), contrary to
(3.3).  \(\square\)

This is an expansion theorem in a literal sense: it asks for sufficiently
many safe Hamilton paths that no union of the repeated-label cylinders and
the low-slack Hall cylinders covers the family.

### Corollary 3.2 (cylinder-probability form)

Choose \(P\) uniformly from \(\mathscr H\).  Suppose that, for every relevant
compatible arc packet `J`,

\[
                    \Pr[J\subseteq E(P)]\le\vartheta^{|J|}. \tag{3.4}
\]

Then it is sufficient that

\[
 \vartheta^2|\mathscr C|
 +\sum_{A\in\mathfrak L_h^\circ}\ \sum_{J\in\mathscr W_A}
       \vartheta^{|J|}<1.                                \tag{3.5}
\]

Every \(J\in\mathscr W_A\) has

\[
                         |J|\ge
       \left\lceil\frac{\rho(A)+1}{2}\right\rceil,       \tag{3.6}
\]

because one connector consumes only two incidences.  Thus positive cut
slack raises the order of the first possible bad cylinder.  Formula (3.5)
is the exact quantitative place where a switching sampler, random walk on
Hamilton paths, or absorbing path family can enter.

### Corollary 3.3 (asymmetric LLL form)

Instead of (3.5), make one bad event for every member of \(\mathscr C\) and
every minimal packet in the second sum of (3.3).  If the chosen path sampler
has a valid lopsided dependency graph and there are numbers `x_B in (0,1)`
such that

\[
             \Pr(B)\le x_B\prod_{B'\sim B}(1-x_{B'}),    \tag{3.7}
\]

then a rainbow residual-flow-extendible path exists.

The dependency hypothesis in this statement is substantive.  A uniformly
random signed permutation is not a product measure on legal paths, and one
may not declare two path cylinders independent merely because their arcs
are disjoint.  A proof must supply either an actual lopsided dependency
graph or a resampling oracle.

## 4. A deterministic fresh-booster expansion lemma

A reversible rainbow path cover \(\mathcal P\) consists of disjoint directed
paths covering the marked components.  Let `p` be its number of paths, so it
uses `m-p` labels.  A **candidate booster** is a transition arc which, after
orienting two cover paths if necessary,

1. joins the end of one path to the start of another;
2. consumes two unused halfports;
3. leaves all inequalities (2.1) valid for the enlarged partial chain; and
4. leaves a reversible path cover (or, in a directed implementation,
   preserves the already chosen orientations of all old path arcs).

Let \(B(\mathcal P)\) be the candidate-booster arc set and let

\[
 \mu(\mathcal P)=\max_{U}
       |\{e\in B(\mathcal P):\lambda(e)=U\}|.           \tag{4.1}
\]

### Theorem 4.1 (fresh-booster expansion)

Assume the zero-connector singleton cover is residual-flow extendible.  If
every reachable flow-extendible reversible rainbow path cover with `p>=2`
satisfies

\[
             |B(\mathcal P)|>\mu(\mathcal P)(m-p),      \tag{4.2}
\]

then there is a residence-safe rainbow Hamilton path with a residual
integral degree flow.

#### Proof

The `m-p` used labels account for at most
\(\mu(\mathcal P)(m-p)\) arcs of \(B(\mathcal P)\).  By (4.2), one booster has a
fresh label, making it a safe booster.  Add it; two cover paths merge, no directed cycle is created,
and the definition of safe booster preserves residual extendibility.
Starting with an extendible singleton cover and iterating `m-1` times gives
one path.  \(\square\)

For the rank-eight/rank-nine Boolean incidence, one `U` has nine rank-eight
facets.  In a catalogue with at most two halfport occurrences per facet
colour and at most one directed arc state per ordered pair of halfport
occurrences, at most `18` halfports can be incident with one `U`; excluding
equal-colour pairs gives the directed multiplicity bound

\[
                         \mu\le18\cdot17-18=288.         \tag{4.3}
\]

Under the same no-parallel-state premise, when every relevant marked
halfport colour occurs once, this improves to

\[
                         \mu\le9\cdot8=72.              \tag{4.4}
\]

If a physical catalogue has parallel states on one ordered halfport pair,
their maximum multiplicity must multiply the right sides of (4.3)--(4.4).
The displayed bounds are only certificates, not claims that (4.2) holds in
the current graph.  Minimum outdegree five by itself cannot imply a Hamilton
path: a disjoint union of directed graphs of order at least six has that
minimum degree and no spanning path.  Nor do many arcs imply rainbow
existence if their labels concentrate.  Endpoint expansion and label
dispersion are both essential.

## 5. Connected residual completion is a second expansion row

The preceding theorems give an integral residual **degree** flow.  They do
not make the completed two-factor connected.

For a fixed good path \(Q\), let \(\mathscr B_Q\) be the finite family of
integral residual flows and let `C_*` be the contracted marked
supercomponent.  For a nonempty union `S` of residual macro components not
containing `C_*`, let `Z_S` be the flows with no selected connector crossing
the cut of `S`.

### Proposition 5.1 (flow-family connectivity criterion)

If

\[
       \sum_{\varnothing\ne S\subseteq
              \pi_0(F_Q)\setminus\{C_*\}}
       |Z_S|<|\mathscr B_Q|,                            \tag{5.1}
\]

then some residual flow completes `Q` to one cycle.

#### Proof

Every disconnected two-factor has a cycle component not containing
`C_*`; the union of its macro components is a nonempty `S` with no crossing
connector.  Thus the sets `Z_S` cover every disconnected flow.  Inequality
(5.1) leaves an uncovered, hence connected, flow.  \(\square\)

The same statement admits cylinder and LLL versions once a distribution on
integral residual flows with proved dependencies is supplied.  Equivalently,
one may use the exact pair-state columns and impose every component subtour
cut.  Ordinary max-flow integrality proves neither (5.1) nor those subtour
rows.  Pair-specific residence or common-cap guards likewise require
pair-state columns unless the allowed relation factors into independent
`U`--port arcs.

## 6. Exact `K17` scope

In the frozen macro forest,

\[
 |\mathcal T|=6435,\quad |E(F)|=1430,\quad
 |\pi_0(F)|=|\mathcal U|=5005.                       \tag{6.1}
\]

Conditional on a clean bank of `m=106` components, a marked path uses

\[
 h=105,\qquad 2h=210,                                \tag{6.2}
\]

and leaves `4900` pure owners and `9800` halfports.  The rebuilt global
macro graph is independently verified to be a linear forest with `5005`
components.  After contraction, a connected residual completion consists of two
bank-boundary owners and a `4898`-edge path through the `4899` unmarked
components.  Opening one of the two boundary edges makes the selected phase
bank and complementary facet bank contiguous with one internal interface.

The original frozen forest did **not** satisfy the clean-bank hypothesis.
Its independently replayed obstruction was:

```text
marked components                         106
whole-component macros                    190
owners                                   3970
strict internal D2 length-two runs          32
bad components                               6
```

Sixteen bad runs used each new-coordinate bit; component reversal could not
remove them, and endpoint `U` owners could not reach them.  The following
six occurrence replacements now remove that obstruction:

```text
z= 9486: (0,4064) -> (0,5826)
z=16502: (0,1781) -> (0,6254)
z= 1675: (0,1997) -> (0,5349)
z= 2829: (0,2849) -> (0,6201)
z=22632: (0,1571) -> (0,4923)
z=26800: (0,2423) -> (0,5775)
```

Their exact repaired ledger is

```text
marked components                         106
required macros                           108
whole-component macros                    154
optional closure macros                    46
owners                                   3815
strict internal D2/D3 debt                0/0
```

Thus `h=105` and the threshold `2h=210` remain unchanged.  The six swaps
do change the port graph.  Independent replay gives its degree profile
`0^4016 1^1978 2^441`, verifies global acyclicity, and finds an
unconditioned `10010/10010` port flow.  The current census certifies the
displayed six-swap witness and marked closure, not an exhaustive theorem
over all six-swap choices.

The repaired fixed-port endpoint catalogue has `412` geometric directed
arcs, of which `312` are residence-clean, on `140` distinct old-U labels.
Component `77`, the singleton required macro `18`, has three geometric
neighbours through two labels and six oriented incidences, but every one is
residence-bad.  Hence it has neither a clean incoming nor a clean outgoing
arc, and no fixed-port marked Hamilton path exists.  This is exactly failure
of the initial path-family/booster premise in Theorems 3.1 and 4.1, not a
residual Hall failure.

### Proposition 6.1 (the repaired fixed-port face is pre-LLL impossible)

In the repaired one-old-U-per-join endpoint catalogue,
\(\mathscr H=\varnothing\).  Consequently no probability measure, LLL, or
expansion argument supported on that catalogue can produce the marked path.
Every extension of this route needs at least one new connector state
incident with component `77`, obtained by changing an endpoint incidence,
inserting a longer socket packet, or otherwise changing its boundary trace.

#### Proof

Every Hamilton path through more than one vertex gives each visited vertex
at least one incident path arc.  Component `77` has no residence-clean
incoming or outgoing arc in either orientation.  Thus no such path exists.
Changing arcs away from component `77` cannot alter this fact.  \(\square\)

### Theorem 6.2 (global support must precede the path LLL)

Let \(\Omega\) be any probability space of occurrence states on the same
`n` marked objects.  For \(\omega\in\Omega\), let \(D_\omega\) be its clean
directed connector catalogue, \(G_\omega\) the undirected projection, and
\(B_\omega\) the bipartite tail--head projection.  Write

\[
 c_\omega=c(G_\omega),\qquad
 l_\omega=|\{v:\deg_{G_\omega}(v)\le1\}|,qquad
 b_\omega=n-1-\nu(B_\omega).                         \tag{6.3}
\]

Every clean directed Hamilton path is supported on a state satisfying

\[
                 c_\omega=1,\qquad l_\omega\le2,
                 \qquad b_\omega\le0.                \tag{6.4}
\]

Fix a marked vertex \(v_0\).  A completely explicit sufficient condition
for the occurrence distribution to contain a state satisfying (6.4) is

\[
\begin{split}
 &\sum_{\substack{\varnothing\ne S\subsetneq V\\v_0\notin S}}
   \Pr\bigl(E(G_\omega;S,V\setminus S)=\varnothing\bigr)\\
 &\quad+
 \sum_{R\in{V\choose3}}
   \Pr\bigl(\deg_{G_\omega}(v)\le1\text{ for every }v\in R\bigr)
 +\Pr\bigl(\nu(B_\omega)<n-1\bigr)<1.               \tag{6.5}
\end{split}
\]

#### Proof

The three conditions in (6.4) are necessary for a directed Hamilton path:
its undirected support is connected, only its two endpoints can have
support degree at most one, and its `n-1` directed arcs have distinct tails
and heads.  If \(G_\omega\) is disconnected, the vertex set of a component
not containing \(v_0\) witnesses one event in the first sum of (6.5).  If
\(l_\omega\ge3\), some triple of low-degree vertices witnesses one event in
the second sum.  The last event is exactly failure of the tail--head
matching necessity.  The union bound proves the sufficient assertion.
\(\square\)

### Corollary 6.2a (support-LLL form)

For every nontrivial component cut `S`, every vertex triple `R`, and every
tail set `Q`, define respectively

\[
\begin{aligned}
 C_S&=\{E(G_\omega;S,V\setminus S)=\varnothing\},\\
 L_R&=\{\deg_{G_\omega}(v)\le1\text{ for every }v\in R\},\\
 M_Q&=\{|N_{B_\omega}(Q)|\le |Q|-2\}.                \tag{6.5a}
\end{aligned}
\]

If this event family has a valid lopsided dependency graph (or resampling
oracle) and numbers \(x_E\in(0,1)\) satisfying

\[
                 \Pr(E)\le x_E\prod_{E'\sim E}(1-x_{E'}),       \tag{6.5b}
\]

then some occurrence state satisfies (6.4).

Indeed, the first two event families exclude disconnectedness and three
forced leaves as above.  By the bipartite deficiency formula

\[
 n-\nu(B_\omega)=\max_{Q\subseteq V}
                   \bigl(|Q|-|N_{B_\omega}(Q)|\bigr),          \tag{6.5c}
\]

avoidance of all \(M_Q\) is equivalent to \(\nu(B_\omega)\ge n-1\).
The lopsided local lemma therefore yields (6.4).  This corollary makes clear
what a genuine occurrence-level LLL must prove; it is not supplied by a
large number of non-isolating moves.

Condition (6.5) is a **global occurrence sieve**, not yet a Hamilton-path
theorem.  In particular, component-cut and three-leaf events may depend on
all occurrence choices.  They cannot be inserted into a local LLL by merely
declaring disjoint-looking connector arcs independent.  A dimension-uniform
LLL proof must provide a product exposure or resampling oracle for these
events.  With only one or two occurrence variables, the honest tool is the
deterministic sieve (6.4), or the union bound (6.5), followed by the path
LLL of Section 3.

### Theorem 6.3 (exact radius-two actuator budget)

Let \(G\) be the clean connector projection of a radius-one frontier state
on a fixed marked-vertex set, and suppose

\[
                        c(G)=3,\qquad l(G)=l.          \tag{6.6}
\]

Let a second occurrence exchange produce a clean catalogue \(G'\).  If
\(G'\) contains a Hamilton path \(P\), then

\[
 |E(P)\setminus E(G)|\ge
 \max\left\{2,\left\lceil{l-2\over2}\right\rceil\right\}.       \tag{6.7}
\]

More precisely, at least \(l-2\) vertices which had degree at most one in
\(G\) are incident in \(P\) with an edge outside \(G\), and the quotient of
those new path edges on the three old weak components is connected.

#### Proof

At most two low-degree vertices of \(G\) can be the endpoints of \(P\).
Every other such vertex needs two path incidences, while \(G\) supplies at
most one, so it is incident with an edge in \(E(P)\setminus E(G)\).  One new
edge can serve at most two of these vertices, giving the second term in
(6.7).  Contracting the three weak components of \(G\), the old edges become
loops.  The new path edges must connect the three contracted vertices, so
at least two are required and their quotient contains a spanning tree.
\(\square\)

For the exact radius-one census, \(l\ge21\); hence every successful second
exchange must supply at least `10` path-usable adjacency units which were
absent from its radius-one frontier graph.  For the high-arc state
`z=21006`, \(l=22\), so at least `20` of its forced leaves must be promoted
and again at least `10` new path adjacencies are required.  At least two of
the new adjacencies must bridge the old `102+2+2` component partition.

This is the requested quantitative answer about two occurrence swaps.
Radius two is **necessary**, because every radius-one state fails (6.4).
It is not yet proved sufficient: a second exchange must be a correlated
ten-unit actuator, not merely another isolation repair.  In particular,
if every second exchange from a frontier state has fewer than ten
path-compatible new adjacency units, or has quotient bridge rank at most
one, that entire radius-two branch is impossible without any path CNF.
When the occurrence exchange changes the marked-component partition rather
than only its connector edges, the invariant version of the same sieve is
to demand directly that the rebuilt graph have \(c=1,l\le2\) and
\(\nu(B)\ge n-1\); the old-leaf incidence refinement then is not asserted.

### Corollary 6.3a (exact persistent-cover certificate)

Assume the marked-vertex identification is fixed, and write `D` and `D'`
for the old and radius-two clean directed catalogues.  A residence-safe
rainbow Hamilton path in `D'` with an integral residual degree flow exists
if and only if there are arc sets `F` and `J` such that

1. one orientation is fixed for every marked component and `F` is a
   spanning directed linear forest in `D intersection D'` under those same
   orientations;
2. `J` is contained in `D' setminus D`, has `c(F)-1` arcs, and, after the
   paths of `F` are contracted, is a consistently oriented Hamilton path;
3. all labels on `F union J` are distinct and all halfport capacities hold;
   and
4. the final consumption vector satisfies
   \(\rho'(A)\ge\ell_{F\cup J}(A)\) for every unused-owner set `A`.

#### Proof

Given the four rows, `F union J` is one directed spanning path; rows 3--4
give rainbow legality and Theorem 2.1 gives the residual integral flow.
Conversely, intersect any successful path `P` with `D`.  Removing its arcs
outside `D` leaves a spanning directed linear forest `F`; the removed arcs
are `J` and linearly order the components of `F`.  The remaining rows are
properties of `P`.  \(\square\)

Consequently a radius-two success from any present frontier needs a
persistent path cover with at least `11` segments and at least `10` new
splicing arcs.  This certificate is the precise finite object to test; the
component/leaf ledger alone is only its first relaxation.

### Lemma 6.3b (low-slack window under occurrence displacement)

Let `d` and `d'` be two nonnegative port-demand vectors with equal total,
and put

\[
 \kappa=\sum_T(d_T-d'_T)_+
       ={1\over2}\lVert d-d'\rVert_1.                \tag{6.7a}
\]

Then, for every owner set `A`,

\[
                       \rho_{d'}(A)\ge\rho_d(A)-\kappa.         \tag{6.7b}
\]

Hence an `h`-connector path in the displaced state can be obstructed only
by old cuts with

\[
                            \rho_d(A)<2h+\kappa.       \tag{6.7c}
\]

#### Proof

For each port,

\[
 \min(d'_T,n_A(T))-min(d_T,n_A(T))
                 \ge -(d_T-d'_T)_+.
\]

Sum this inequality to obtain (6.7b).  If the new residual flow fails,
Theorem 2.1 gives \(\rho_{d'}(A)<\ell(A)\le2h\); (6.7b) then gives
(6.7c).  Equal totals prove the second expression for \(\kappa\).
\(\square\)

For two occurrence exchanges which each move one unit of port demand,
\(\kappa\le2\).  Thus the old six-swap separator bank needed by a
radius-two `K17` path is slack `<212`, not merely `<210`.  Using a
state-specific \(\rho'\) as in Corollary 6.4 remains exact and needs no such
robustness enlargement.

### Corollary 6.4 (radius-two path-family counting theorem)

Let \(\Omega_2^*\) be any finite collection of residence-clean radius-two
states which pass (6.4).  For each \(\omega\in\Omega_2^*\), let
\(\mathscr H_\omega\) be a finite family of clean transversal Hamilton
paths, and define \(N_\omega(J)\), repeated-label pairs
\(\mathscr C_\omega\), and minimal active cut packets
\(\mathscr W_{\omega,A}\) exactly as in Section 3 for that state.  If

\[
\begin{split}
 &\sum_{\omega\in\Omega_2^*}
 \left(
   \sum_{J\in\mathscr C_\omega}N_\omega(J)
  +\sum_{A:\rho_\omega(A)<2h}
       \sum_{J\in\mathscr W_{\omega,A}}N_\omega(J)
 \right)\\
 &\hspace{45mm}<
 \sum_{\omega\in\Omega_2^*}|\mathscr H_\omega|,       \tag{6.8}
\end{split}
\]

then some radius-two state has a residence-safe rainbow marked path with an
integral residual degree flow.

#### Proof

Apply the bad-path covering argument of Theorem 3.1 to the disjoint union
of the path families \(\mathscr H_\omega\).  Every bad pair
\((\omega,P)\) contains a repeated-label certificate or a minimal active
cut packet in its own state.  Inequality (6.8) leaves one uncovered pair.
\(\square\)

Thus the correct probabilistic order is:

1. screen occurrence states by the global conditions (6.4), using (6.5)
   or an exact statewise audit;
2. only on the surviving states apply the cylinder/LLL or booster theorem
   to path choice and low-slack Hall; and
3. finally impose the pair-column connectivity row of Section 5.

For the frozen `K17` instance, the complete radius-one census is

```text
all one-occurrence neighbours                         1430
residence-clean                                        1411
no isolated marked component                           122
connected clean graph                                     0
passing Hamilton-path degree necessity                    0
minimum forced-leaf count                                21
```

The best weak shapes are `102+2+2` and `103+2+2`.  Consequently the live
occurrence search starts at radius two from the `12` three-component
frontier states.  Running path CNFs on the `122` radius-one states cannot
add information to this solver-free no-go.  Numerically, non-isolation has
density `122/1411` (about `8.65%`) inside the residence-clean neighbourhood,
whereas connectedness and path-degree admissibility both have density zero.
The `z=21006` exchange adds six simple projected adjacencies and deletes one
relative to the six-swap graph, yet changes the leaf ledger only from
`23` plus one isolate to `22` leaves.  This is direct evidence that clean-arc
gain is not a surrogate for the correlated leaf-pairing condition (6.7).

### Theorem 6.5 (`OPTIMAL28` realizes the path and connectivity rows)

In the authenticated direct/one-optional packet catalogue there is a fixed
residence-clean path `P` with the following exact ledger:

```text
marked components                                      106
optional forest components                              28
distinct fixed pure-U owners / packet connectors       133
marked owner-word length                              4108
fixed-forest components after P                       4872
remaining pure-U owners                               4872
residual half-demand                                   9744
residual demand profile                   0^691 1^1744 2^4000.
```

There is an integral assignment of two distinct rank-eight facets to every
remaining pure-`U` owner which meets that demand exactly and for which the
union of the macro forest, `P`, and all residual owner edges is a single
cycle on the `6435` rank-eight ports.  This cycle meets the fixed marked
path in exactly two residual edges.  Hence the marked bank is one literal
contiguous interval and the complementary bank is the other.

Literal materialization of that cycle has the sharper ledger

```text
distinct rank-nine owners                            24310
distinct lower-q1 rank-eight colours                 24310
marked bank: objects / owners                      304 / 4108
complement bank: objects / owners                 6131 / 20202
raw marked-owner-bank D2 / D3 bad runs                 0 / 0
raw complement-owner-bank D2 / D3 bad runs         1025 / 547
distinct upper-q1 colours                            17548
upper-q1 holes / excess / maximum load          1900 / 6762 / 6.
```

The exact nonflat two-bank zipper replaces the complementary owner bank by
its complete facet rail.  Its target and maximal-inverse ledger is

```text
D2 target-row length                                  24311
marked rank-nine cells / distinct facet cells    4108 / 20203
marked turn colours / facet colours              4107 / 20203
union of those disjoint lower-colour banks             24310
maximal inverse length / empty envelopes          24313 / 0
strict internal D2 bad / strict internal D3 bad 2392 / 2392
maximal-inverse replay mismatches                       3568
upper interval holes by rank        10:1900, 11:911, 12:128,
                                    13:0, 14:0, 15:0, 16:0, 17:0.
```

#### Proof

The fixed macro and packet edges are acyclic, leaving `4872` components and
the displayed nonnegative demand vector of total `9744`.  The saved
assignment contains one row for every one of the `4872` unused owners; each
row names two distinct facets of that owner.  Its port multiset is exactly
the positive demand multiset.  Therefore the completed port graph is
two-regular.  Independent union--find replay gives one connected component,
so it is one cycle.  The fixed packet path has `304` edges on `305` ports,
with degree profile `1^2 2^303`; only its two endpoints have residual
degree.  Exactly two saved residual edges cross from that vertex set to its
complement, proving contiguity.  The independent literal materializer then
expands the `6435` objects, checks that all `24310` rank-nine owners and all
`24310` lower-q1 colours occur exactly once, locates the two bank
transitions, and scans coordinate runs and upper-q1 unions to obtain the
first displayed defect ledger.  It then forms the `20203`-cell facet rail,
checks that its colours and the `4107` marked turns are disjoint and
partition the entire rank-eight layer, constructs the coordinatewise
maximal inverse, and scans exact replay plus all changing interval unions.
This gives the second ledger.  \(\square\)

This theorem witnesses the **conclusions** of the marked-path existence and
conditioned residual-connectivity rows.  It does not assert that the
probabilistic inequalities (6.5), (6.8), or (5.1) were verified, nor does it
give a dimension-uniform sampler.  Here `h=133`, so the generic old-cut
window would be slack `<266`; the explicit `9744/9744` assignment is a
stronger state-specific certificate and makes that separation unnecessary
for this witness.

The completed object is exact through owner/lower-q1 topology, the immutable
residence-clean marked path, the lower-palette partition of the proposed
nonflat target row, nonempty maximal envelopes, and every upper rank at
least `13` in the linear contiguous-D2 interval model.  It is not yet an
exact nonflat word: the strict internal D2/D3 ledger is `2392/2392` and
maximal inversion misses `3568` target cells.  Envelope nonemptiness is only
one necessary row and does not certify inversion.  The recorded strict-run
counts exclude endpoint-touching and cyclic-closure runs, so those boundary
rows must also remain in any repair theorem.
The only upper holes occur in ranks `10--12`, with counts `1900/911/128`.
Thus the three finite global rows are now concrete: repair nonflat
residence/replay, repair those first three upper shadows, and solve the
common-cap Hall problem, all while freezing the marked bank and its two
exported interfaces.

Therefore the sharp surviving theorem target is:

1. retain the authenticated `OPTIMAL28` marked interval and connected
   owner/lower-q1 factor while eliminating the `2392/2392` strict D2/D3
   defects and the `3568` maximal-inverse replay mismatches, with endpoint
   and cyclic boundary runs checked separately;
2. eliminate the upper-hole vector `(1900,911,128)` in ranks `10,11,12`
   while retaining the already complete ranks `13--17`; and
3. solve the exact common-cap/compiler matching on the same order.

Radius two from the `12` whole-component frontier states remains a useful
structural and dimension-uniform route, but it is no longer a prerequisite
for closing these two finite `K17` rows.

No fixed-port no-go is promoted to a global `K17` obstruction, and no claim
about `nu(17)` follows.

## 7. Frozen dependencies

The fixed-forest obstruction used in Section 6 is independently frozen in

```text
MATH_THEOREM_K17_MARKED_MACRO_COMPONENT_TWO_BANK_OBSTRUCTION_20260731.md
SHA-256 65819b0a7ef73a48729d14b7e20e944072cf7fc8ca1c732c21cd7361f5a9886a

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.audit.json
SHA-256 c4a7e2477186247bdbdace01967426a1cf55db8bcacc99296b679c681451e259

scratch/k17_marked_macro_component_two_bank_obstruction_20260731.independent.json
SHA-256 b668fbc5e75a9ccd25c3571a9c4938f2a6167b0e66ca18d8c35c096afe90bdec

scratch/k17_two_bank_single_occurrence_swaps_20260731.census.json
SHA-256 e9797343a3d6e841195b01b3541814562f8af8c6645f0d8e4795e2f0a9fa1d83

MATH_AUDIT_K17_SIXSWAP_REPAIRED_COMPONENT_PATH_GATE_20260731.md

scratch/audit_k17_sixswap_repaired_component_flow_gate_20260731.py
SHA-256 14b90b013dab73649b9b65097f14def799c2c4bbdb6fe8c0f60d362d8f7bf262

scratch/k17_sixswap_repaired_component_flow_gate_20260731.audit.json
SHA-256 90fbffaf6fc35c159ce81b4730f1d37b503bec49617bdda77cd2f435d92f14d6

scratch/ad_k17_opt28_residual_connected_bflow_20260731.json
SHA-256 b3cbb0663409463cb24a2ed78db154cc88a042b633e979cba3506ba74e610ef6
payload a117a304f277a7746405814786fd3f593dffe5073443431582eb711641e7319a

scratch/audit_ad_k17_opt28_residual_connected_bflow_20260731.py
SHA-256 a6f306a8ac9885cf6556b2746d516f831b53bb1e93e8e8dd4a996a298a0d6c01

scratch/ad_k17_opt28_residual_connected_bflow_20260731.audit.json
SHA-256 95e8b27426d9ac62ccbe490a55c2a1e256e63faa1bc561a5d5a0462380870cfd
payload 05d8685b325abc3311732f032becf2c7f158776a83c6cb36f16fca56d23056f9

scratch/materialize_k17_opt28_connected_owner_cycle_20260731.py
SHA-256 e5434ae453e8dd7a9373d2a5b50379d930554fb22560c37edf1bee04611ee89c

scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa

scratch/k17_opt28_connected_owner_cycle_20260731.audit.json
SHA-256 f28924a629a6e858571119538639adf3ecbd4d186c1014a475e353fe5b719280
payload 6988b37a414a516e4645f81b1dac87618c1949bc636a1190462c5f8520639d7a
```

The radius-one census was extended after the earlier six-swap audit.  Its
byte SHA above is authoritative for the displayed `1430/1411/122/0/0`
counts.  Its embedded payload digest belongs to a live serializer lineage
and does not recompute against the present bytes, so it is intentionally
not cited as an authenticated payload.  The materialized `z=21006` files
were built against the older census lineage; their own byte hashes and
state replay remain valid, but they are an illustration rather than the
canonical first row of the current radius-one sort.

The exact deterministic marked-path/pair-state master is

```text
MATH_THEOREM_R_K17_NONFLAT_COMPONENT_PATH_AND_RESIDUAL_BFLOW_MINMAX_20260731.md
```

The present note adds the low-slack partial-extension algebra, the exact
path-family counting theorem, the cylinder/LLL sufficient conditions, and
the fresh-booster and residual-connectivity expansion criteria.  It does
not rely on a finite search.

## 8. Independent audit

An independent theorem audit accepted Theorems 2.1 and 3.1, the cylinder
and LLL corollaries, and Proposition 5.1 after four corrections now present
in the text:

1. the low-slack family is `Q`-relative in (2.6);
2. minimal cut packets obey the port bound coordinatewise;
3. Theorem 4.1 assumes an initially feasible residual flow and preserves
   reversibility at every booster; and
4. the numerical colour-multiplicity bounds require a no-parallel-state
   catalogue.

The audit also required a global acyclicity replay before using the
`5005`-component topology count.  That replay has since passed; the sharper
finite obstruction is now the complete radius-one support no-go.  A second
independent audit checked the new scope and the radius-two bound:

5. in the census, a leaf means degree exactly one in the **simple
   undirected** projection; orientation, multiplicity, and repeated labels
   are deliberately ignored, so the leaf row is only necessary;
6. `122` means no isolated projected vertex and nothing stronger; all `122`
   graphs are disconnected and none passes the degree sieve;
7. for `z=21006`, `322` directed arcs project to `161` simple adjacencies,
   with weak sizes `102+2+2` and `22` leaves; the exact graph-edit proof
   independently gives the ten-new-adjacency lower bound; and
8. no radius-two state or seventh-state Hall flow has been certified.  This
   remains true for the whole-component occurrence face.  Separately, the
   `OPTIMAL28` packet face now has an authenticated connected conditioned
   residual factor.

The proof of Theorem 6.3 was adversarially checked against deletions: because
only edges in \(E(P)\cap E(G)\) count as persistent, deleting old edges can
only increase, never decrease, the required new-edge set.  Connected graphs
with zero or two leaves may still have articulation obstructions, and a
Hamilton support may still fail rainbow labels or a tight residual Hall cut.
Accordingly (6.4) and (6.7) are explicitly necessary sieves; sufficiency is
the stronger persistent-cover certificate plus (6.8), followed separately
by residual pair-column connectivity.

The `OPTIMAL28` connectivity replay was also checked independently.  Its
payload recomputes, all three input hashes match, every unused owner selects
two distinct literal facets, the selected port multiset equals the exact
demand vector, every one of the `6435` final port degrees is two, and
union--find gives one component.  The fixed packet path is independently a
`304`-edge path and exactly two residual edges cross its vertex boundary.
This audit proves the connected owner/lower-q1 factor and contiguity only;
it deliberately does not inspect complementary residence, upper/deep
shadow support, or common-cap feasibility.

The subsequent literal materialization fills that audit boundary without
changing it: it checks all `24310` owner and lower-q1 labels, the `304/6131`
object bank split, and the exact nonflat zipper.  The raw owner banks have
marked/complementary run debt `0/0` and `1025/547`, respectively.  The
actual mixed-rank D2 target has `2392/2392` strict D2/D3 defects and `3568`
maximal-inverse replay mismatches, although all `24313` inverse envelopes
are nonempty.  The lower-colour partition is exact, and the upper-hole
vector is `(1900,911,128,0,0,0,0,0)` in ranks `10--17`.  These are
authenticated defects of this realized target, not lower bounds for all
connected completions and not evidence of a global `K17` obstruction.

An independent read-only audit recomputed every displayed nonflat count and
all payload hashes.  It also fixes two scope points: the `2392/2392` counts
are internal per-coordinate short runs and exclude endpoint/cyclic closure,
and zero holes in ranks `13--17` means completeness for linear contiguous-D2
interval unions only.  No exact inverse, endpoint residence, common cap, or
word is certified.
