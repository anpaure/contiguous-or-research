# Sixth-wave AA: an open-packet linear-frustration no-go

Date: 2026-07-25

Method: pure mathematics only.  No search, experiment, solver, or
computer-assisted enumeration is used.

## 0. Outcome

This note closes the black-box dependent-rounding version of the frozen
rotor-resolution lane.

The input to that lane consists of exact statewise ownership constraints,
open low-run packets, and a fractional assignment of packet occurrences to
prescribed exact colors.  The natural hope is that partition-matroid,
Birkhoff, Beck--Fiala, Banaszczyk, Lovett--Meka, or cycle-canceling rounding
can preserve the exact ownership constraints while adding only a sublinear
number of packet switches.

That assertion is false even in a two-color rank-one partition-matroid
fiber.  For every (g\ge1) there is an explicit instance with

* two prescribed colors, each containing every state exactly once;
* three open packet paths, with no state repeated inside a packet;
* every state occurring in exactly two packet positions;
* zero cost in the standard statewise Birkhoff/local-edge relaxation; and
* exact integral packet variation
  \[
  \boxed{V^*=g}
  \]
  on (6g) occurrence slots.

Moreover each of the two integral colors has at least (g/2) hard runs.
At a native Gaussian radius

\[
d=\lfloor a\sqrt m\rfloor,
\qquad a>0\text{ fixed},
\]

and with (3g=c_d+O(1)), this forces, for **each** color, hard-reset prefix
overhead

\[
2d\,r_c\ge dg
=\left(\frac23a^2e^{-a^2}+o(1)\right)W.
\]

Thus an abstract exact multicover may have a frozen three-packet chronology
whose fractional switch defect and initial packet toll are (o(W)), while
every integral exact color extracted by statewise reconciliation has length
at least

\[
\boxed{
\left(1+\frac23a^2e^{-a^2}+o(1)\right)W.}
\]

The example may be padded by disjoint nested chains so that every color has
the exact Boolean rank histogram and owns every middle and shadow target
exactly once.  What is deliberately **not** asserted is that the three
packet paths embed as paths in the genuine Boolean rotor graph.  Therefore
the theorem is a no-go for every rounding argument using only exact
ownership, nested rank counts, local Birkhoff data, column sparsity, or
partition-matroid structure.  It is not a counterexample to
\(\mathrm{RSCD}_A\).

The next exact statement cannot be an unqualified discrepancy theorem.  It
must use genuine rotor geometry to prove that the actual packet-palette
constraint system has weighted signed frustration (o(W)), or it must
change the chronology globally (for example through the constrained
recursive Hall lift).  In multiplicity two, the required quantity is
exactly a signed-graph frustration index, derived below.

## 1. Two-sheet packet palettes are signed Max-2LIN

Let \(\Omega\) be a finite state set.  There are two target colors
\(0,1\), and both prescribed colors contain every state exactly once.  The
occurrence system contains two slots

\[
\omega^+,\omega^- \qquad(\omega\in\Omega).
\]

The slots are partitioned into open packet paths.  Assume no packet contains
both occurrences of one state.  An exact palette assignment gives the two
slots of every state different colors.  Put

\[
x_\omega=\text{the color on }\omega^+\in\{0,1\}.
\]

Then the color on \(\omega^-\) is \(1-x_\omega\).  Encode a signed slot as
\((\omega,a)\), where (a=0) denotes \(\omega^+\) and (a=1) denotes
\(\omega^-\).  Its color is

\[
x_\omega\oplus a.
\tag{1.1}
\]

For a packet edge

\[
e=((\omega,a),(\eta,b)),
\]

there is no color switch exactly when

\[
x_\omega\oplus x_\eta=a\oplus b.
\tag{1.2}
\]

Let \(G\) be the resulting signed multigraph on \(\Omega\), with parity
label \(a\oplus b\) on this edge.

### Theorem 1.1 -- exact frustration identity

For every two-sheet open-packet instance,

\[
\boxed{
V^*=\min_{x\in\{0,1\}^{\Omega}}
\#\{e=\omega\eta:
x_\omega\oplus x_\eta\ne s_e\}.}
\tag{1.3}
\]

The same identity holds with arbitrary nonnegative edge weights.

#### Proof

Exact statewise ownership makes the color of every slot equal to (1.1) for
one unique vector (x).  By (1.2), the switch indicator of a packet edge is
exactly the violation indicator of its signed parity equation.  Summing
over edges proves (1.3), and inserting edge weights changes nothing.
\(\square\)

Consequently a spanning forest of the signed constraint graph can always be
satisfied: choose one root sign in every tree and propagate (1.2).  Thus, if
\(T\) is any spanning forest,

\[
V^*\le w(E\setminus T).
\tag{1.4}
\]

Conversely every edge-disjoint family of negative signed cycles gives the
corresponding packing lower bound.  The obstruction is signed-cycle
frustration, not linear discrepancy of the ownership equations.

The exact-ownership polytope here is as benign as possible.  For color zero
one chooses exactly one element of each pair
\(\{\omega^+,\omega^-\}\); color one is its complement.  Hence it is a
direct product of bases of (U_{1,2}), equivalently a partition-matroid base
polytope.  The difficulty enters only through the temporal edge objective.

### Theorem 1.2 -- exact two-sheet extraction threshold

Let \(p\) be the number of nonempty open packets, let
\(\operatorname{fr}(G)\) be the signed frustration in (1.3), and let
\(r_0,r_1\) be the numbers of hard monochromatic runs in an optimal exact
palette.  Then

\[
\boxed{r_0+r_1=p+\operatorname{fr}(G)}
\tag{1.5}
\]

and

\[
\boxed{r_0,r_1\ge\frac12\operatorname{fr}(G).}
\tag{1.6}
\]

For a collection of radii with exact prefix weights \(2d\), some one of
the two target colors has total prefix toll at most

\[
\sum_d d\bigl(p_d+\operatorname{fr}(G_d)\bigr),
\tag{1.7}
\]

whereas each target color has toll at least

\[
\sum_d d\,\operatorname{fr}(G_d).
\tag{1.8}
\]

#### Proof

An open binary packet with \(s\) switches has \(s+1\) runs.  Summing over
packets and minimizing gives (1.5).  On one packet, the zero-run and
one-run counts differ by at most one; summing gives
\(|r_0-r_1|\le p\).  Combine this with (1.5) to obtain (1.6).

At radius \(d\), the sum of the two colors' prefix tolls is
\(2d(p_d+\operatorname{fr}(G_d))\).  Averaging the total over the two
colors proves (1.7).  Equation (1.6), multiplied by \(2d\) and summed,
proves (1.8).  \(\square\)

Thus the exact two-sheet frozen-resolution gate is not an \(\ell_\infty\)
discrepancy estimate.  It is the weighted signed-frustration condition

\[
\sum_d d\,\operatorname{fr}(G_d)=o(W),
\tag{1.9}
\]

together with the already small packet baseline.  This statement applies
verbatim when the packet edges are genuine rotor arcs and the two target
colors are genuine integral SCDs.

## 2. The three-path braid

Fix (g\ge1), and take states

\[
\Omega_g=\{X_j,Y_j,Z_j:1\le j\le g\}.
\tag{2.1}
\]

Use the following three open packets, each of length (2g):

\[
\begin{aligned}
A&=(Z_1^-,X_1^+,Z_2^-,X_2^+,\ldots,Z_g^-,X_g^+),\\
B&=(X_1^-,Y_1^+,X_2^-,Y_2^+,\ldots,X_g^-,Y_g^+),\\
C&=(Y_1^-,Z_1^+,Y_2^-,Z_2^+,\ldots,Y_g^-,Z_g^+).
\end{aligned}
\tag{2.2}
\]

Every state occurs exactly twice, once with each sign, and its two
occurrences lie in different packets.  In particular all packets are open
and state-simple.

Write (x_j,y_j,z_j\) for the colors on the plus occurrences.  The three
within-(j) packet edges demand, respectively,

\[
x_j\oplus z_j=1,
\qquad
x_j\oplus y_j=1,
\qquad
y_j\oplus z_j=1.
\tag{2.3}
\]

These three equations are inconsistent: adding them modulo two gives
\(0=1\).  Hence every exact palette has at least one switch among the three
within-(j) edges.  The (g) triples are edge-disjoint, so

\[
V^*\ge g.
\tag{2.4}
\]

This lower bound is exact.  Start with

\[
(x_1,y_1,z_1)=(0,0,1)
\]

and recursively put

\[
x_{j+1}=1-y_j,
\qquad
y_{j+1}=1-z_j,
\qquad
z_{j+1}=1-x_j.
\tag{2.5}
\]

The three connector edges between blocks (j) and (j+1) are

\[
X_j^+Z_{j+1}^-,
\qquad
Y_j^+X_{j+1}^-,
\qquad
Z_j^+Y_{j+1}^-.
\tag{2.6}
\]

By (2.5), their endpoint colors agree, so none is a switch.  Every triple
in (2.5) has exactly two equal coordinates and one different coordinate.
Therefore exactly one equation in (2.3) fails.  This assignment has exactly
one switch per block, proving

\[
\boxed{V^*=g.}
\tag{2.7}
\]

There are (6g-3) packet edges, so the integral violation density tends to
(1/6).

### Corollary 2.1 -- both exact colors have linearly many runs

Let (r_0,r_1) be the total numbers of monochromatic runs of colors zero
and one over the three packets.  Then every exact palette satisfies

\[
r_0+r_1=3+V\ge g+3
\tag{2.8}
\]

and

\[
|r_0-r_1|\le3.
\tag{2.9}
\]

Consequently

\[
\boxed{r_0,r_1\ge g/2.}
\tag{2.10}
\]

#### Proof

A binary word on one nonempty open path with (s) switches has (s+1)
runs, proving (2.8) after summing over the three paths.  Its zero-run and
one-run counts differ by at most one because the runs alternate.  Summing
this inequality over the three packets gives (2.9), and (2.10) follows from
(2.8)--(2.9).  \(\square\)

Thus averaging the two colors does not hide one cheap atom.  Both integral
colors are expensive in the frozen packet chronology.

## 3. Zero fractional defect

Let (u_{v,c}) indicate that packet position (v) receives color (c),
and let (q_{e,c}) be the standard local variable claiming that both ends
of packet edge (e) receive color (c).  The usual statewise/local-edge
relaxation contains

\[
\sum_cu_{v,c}=1,
\qquad
\sum_{v\in\{\omega^+,\omega^-\}}u_{v,c}=1,
\tag{3.1}
\]

and

\[
0\le q_{e,c}\le u_{v,c},u_{w,c}
\qquad(e=vw).
\tag{3.2}
\]

Its switch cost on (e) is

\[
1-\sum_cq_{e,c}.
\tag{3.3}
\]

Set

\[
u_{v,0}=u_{v,1}=\frac12,
\qquad
q_{e,0}=q_{e,1}=\frac12.
\tag{3.4}
\]

Equations (3.1)--(3.2) hold and every edge has cost zero in (3.3).  The same
point also satisfies the usual lower McCormick inequalities

\[
q_{e,c}\ge u_{v,c}+u_{w,c}-1.
\]

Therefore the local LP has value zero while the integral optimum is (g).
The gap persists although the exact-ownership marginal belongs to a product
of partition-matroid base polytopes and every signed state variable has
constraint degree at most four.

This directly excludes a universal estimate of the form

\[
V_{\rm int}
\le C V_{\rm frac}+o(|\Omega|)
\tag{3.5}
\]

for any fixed (C), under hypotheses consisting only of local marginals,
bounded column degree, exact partition-base membership, or negative
correlation.  Conditional expectations can derandomize a supplied global
certificate, but (2.7) shows that no integral certificate of sublinear cost
exists in this instance.

## 3A. Exact obstruction to embedding this braid in a positive-radius rotor

The braid of Section 2 is not merely unembedded; its most direct rotor
embedding is impossible.  This follows from an exact girth invariant of the
genuine rotor graph.

### Lemma 3A.1 -- exact directed girth of the rotor graph

For (d\ge1), every directed cycle in the radius-(d) rotor graph has
length at least (2d+2).  This bound is attained.

#### Proof

Write the singleton word at time (t) as

\[
(z_{t,1},\ldots,z_{t,2d}).
\]

One rotor step has the shift-register law

\[
z_{t+1,1}=x_t,
\qquad
z_{t+1,j+1}=z_{t,j}\qquad(1\le j<2d),
\tag{3A.1}
\]

where (x_t\in L_t).  Track the coordinate (u=z_{0,2d}).  After the
first step, (u\) lies in the residual block (R_1).  It cannot move from
(R) to (L) and from (L) to the first singleton slot in one step,
because the chosen (x_t\) belongs to the old (L_t), whereas the chosen
(y_t\) enters (L_{t+1}) from (R_t).  Hence (u) can enter (L) no
earlier than time (2), and can re-enter singleton position one no earlier
than time (3).  By (3A.1), moving from singleton position one back to
position (2d) then needs another (2d-1) steps.  Thus a return to the
initial state needs at least

\[
3+(2d-1)=2d+2
\]

steps.

For attainment, order the slots of (L) and (R), fix one slot in each,
and repeatedly use the corresponding rotor move.  On ordered slots this is
the cycle

\[
(a_i,q_1,\ldots,q_{2d},b_j)
\]

of length (2d+2).  Its intermediate quotient states are distinct by the
lower bound just proved, and after (2d+2) steps the abstract state returns.
\(\square\)

### Corollary 3A.2 -- the three-path braid cannot be a genuine rotor packet

For every (j), the three within-block packet arcs in (2.2) are

\[
Z_j\longrightarrow X_j,
\qquad
X_j\longrightarrow Y_j,
\qquad
Y_j\longrightarrow Z_j.
\]

They form a directed triangle.  Lemma 3A.1 excludes such a triangle at
every (d\ge1).  Therefore the Section 2 packet system has no literal
positive-radius rotor embedding.

This is the precise point where the formal partition-matroid counterexample
fails to become a genuine Boolean-rotor counterexample.  Subdividing each
triangle to the minimum rotor-cycle scale (2d+2) preserves only one forced
switch per \(\Theta(d)\) states.  At a Gaussian radius this gives weighted
cost of order (c_d=o(W)), not the required order (W).  Hence a genuine
linear-toll obstruction would need a constant-density family of frustrated
constraints in a high-girth rotor subgraph, not a suspension of the local
triangle gadget.

More exactly, \(c_d=\Theta(W/\sqrt m)\) and \(d=\Theta(\sqrt m)\) in a
fixed Gaussian annulus.  Theorem 1.2 says that a genuine two-sheet
reconciliation is cheap precisely only if its frustration is
\(o(c_d)\), once the packet baseline is \(o(c_d)\).  The directed-girth
lemma excludes the present local certificate but does not prove that every
actual rotor signed graph has \(o(c_d)\) frustration: signed cycles may
traverse some packet arcs backwards.  The surviving Boolean statement is
therefore the target-specific assertion

\[
\operatorname{fr}(G_d)=o(c_d)
\quad\text{on every fixed Gaussian annulus,}
\tag{3A.2}
\]

or its weighted multirank sum.  It remains unproved.

## 4. Exact Gaussian toll

Return to the even Boolean rank ledger, but retain only the numerical native
radius counts.  Put

\[
W=\binom{2m}{m},
\qquad
N_d=\binom{2m}{m-d},
\qquad
c_d=N_d-N_{d+1}.
\tag{4.1}
\]

At a native radius (d<m), an exact SCD color has (c_d) radius-(d)
states, and each hard run has exact prefix overhead (2d).  Choose

\[
d=\lfloor a\sqrt m\rfloor,
\qquad
g=\lfloor c_d/3\rfloor.
\tag{4.2}
\]

Use the braid on (3g) states and pad the remaining at most two states in
trivial packet pieces.  Corollary 2.1 gives, for each target color,

\[
\text{radius-}d\text{ prefix overhead}
\ge2d\,(g/2)=dg.
\tag{4.3}
\]

The asymptotics are exact.  First,

\[
\log\frac{N_d}{W}
=\sum_{j=1}^d
\log\frac{m-j+1}{m+j}
=-\frac{d^2}{m}
+O\!\left(\frac{d^3}{m^2}+\frac dm\right),
\tag{4.4}
\]

so (N_d/W=e^{-a^2}+o(1)).  Also

\[
c_d
=N_d\left(1-\frac{m-d}{m+d+1}\right)
=N_d\frac{2d+1}{m+d+1}.
\tag{4.5}
\]

It follows that

\[
\frac{dc_d}{W}\longrightarrow2a^2e^{-a^2},
\qquad
\frac{dg}{W}\longrightarrow\frac23a^2e^{-a^2}.
\tag{4.6}
\]

Hence every exact color extracted from the frozen braid has hard-reset
prefix length at least

\[
\boxed{
W+dg
=\left(1+\frac23a^2e^{-a^2}+o(1)\right)W.}
\tag{4.7}
\]

By contrast, before integral palette reconciliation the braid consists of
only three open packets.  Its hard-start charge at this radius is (6d),
and (6d=o(W)); its local fractional internal-switch charge is zero by
Section 3.  Thus the rounding gap itself, not the packet baseline, creates
the positive-constant loss.

## 5. Exact ownership and nested-rank padding

The construction can be placed in an abstract symmetric-chain ownership
system with the exact Boolean rank numbers.  For each native radius (h),
take (c_h) disjoint formal symmetric chains of length (2h+1).  Their
rank-(m-q) targets number

\[
\sum_{h\ge q}c_h=N_q,
\]

and the total number of chains is

\[
\sum_hc_h=W.
\]

Prescribe two identical exact colors, each containing every formal chain
once.  Each middle target and every target on every nested chain is then
owned exactly once in each color.  At the selected radius (d), use the
three-path braid on (3g) chains and trivial padding on the remaining
chains.  At other radii choose arbitrary low-run abstract packet paths.

Therefore exact one-owner middle constraints, all exact binomial rank
counts, and literal nesting along every chain do not prevent the gap.
Neither does the strongest possible local matroid structure.

The formal chains above are not claimed to be actual chains of subsets
whose cross-chain containment relations agree with the Boolean lattice, and
the packet edges are not claimed to satisfy the genuine rotor transition
formula.  Those two geometric facts are precisely what a surviving theorem
must exploit.

## 6. Consequence for Lane AA

The logarithmic nonaligned-support escape in
`NONALIGNED_REFLECTION_SUPPORT_SEED_ESCAPE_20260725.md` is orthogonal to
this theorem.  That escape shows that a static lower bound obtained by
counting targets invariant under a generated coordinate group can fall
below the FSP scale once a reflection support of order \(\log m\) is
allowed.  No invariant target is counted here, and the braid obstruction
does not depend on a coordinate support.  Conversely, the present formal
braid has not been embedded in the genuine rotor graph, so it does not
repair the invariant-seed argument beyond its nonaligned boundary.  The two
results together leave exactly a geometric travel/synchronization problem,
not another support-size enumeration.

### Proved no-go

There is no target-specific discrepancy or dependent-rounding theorem with
the following black-box hypotheses and conclusion:

1. exact one-owner middle constraints;
2. exact nested rank-shadow ownership and Boolean rank counts;
3. a statewise Birkhoff or partition-matroid fractional point;
4. open state-simple packets and zero local fractional switch cost;
5. bounded signed constraint degree;
6. conclusion: one integral exact color with (o(W)) hard-reset cost.

Sections 2--5 give a family violating the conclusion by the positive
constant in (4.7).  Cycle canceling inside the ownership base polytope,
ordinary discrepancy, vector balancing, partial coloring, and local SDP
rounding all fall inside this black-box scope unless they import an
additional theorem about the genuine rotor packet geometry.

### Exact surviving statement

For every multiplicity-two subinstance of a genuine packet-palette problem,
orient the two occurrences of each state and form the signed graph of
Theorem 1.1.  The exact internal switch cost is its frustration index.  Thus
a necessary target-specific geometric input is

\[
\boxed{
\sum_{d\le H}2d\,\operatorname{fr}(G_d)=o(Q_mW),}
\tag{6.1}
\]

after the actual packet decomposition, target SCD resolution, and all
orientations are chosen.  For higher multiplicity, the exact replacement is
the packet-palette variation (V_d^*), so the full frozen-resolution target
remains

\[
\boxed{
\sum_{d\le H}2d\,V_d^*=o(Q_mW).}
\tag{6.2}

Equations (6.1)--(6.2) are not consequences of generic discrepancy.  A
proof must show that genuine rotor paths exclude a positive-density braid
minor such as (2.2), or must replace the frozen chronology by a globally
re-Eulerized one.  The direct alternative is the constrained recursive Hall
lift with only (o(W/H)) deleted inherited edges.

### Scope

This note does not disprove \(\mathrm{RSCD}_A\), MWB, or the contiguous-OR
theorem.  It proves that exact ownership and nested ranks alone are not the
missing rounding hypothesis.  The remaining issue is a Boolean-rotor
geometric theorem about global signed frustration or a construction that
bypasses frozen palette reconciliation entirely.
