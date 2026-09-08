# Pure-mathematical synthesis after the half-period and router advances

**Date:** 2026-08-04
**Status:** proof-status synthesis.  It records unconditional results,
separates the Gaussian/Bellman dual from the literal OR-word construction,
and states the shortest honest remaining all-dimensional theorem.  It does
not claim `nu(k)=B(k)` or `nu(k)<=B(k)+O(1)` beyond the currently verified
finite range.

## 0. Current verdict

The certified finite statement remains

\[
                         \nu(k)=B(k)\qquad(0\le k\le16),
\]

and the first unresolved finite value remains

\[
                         24313=B(17)\le\nu(17)\le25746.
\]

The general additive-constant conjecture is **not proved**.  Two distinct
mathematical programs have nevertheless advanced:

1. the Gaussian Bellman dual has been reduced much further, including one
   new complete six-slot scalar closure and an all-period one-defect
   reduction; and
2. the common-cap router now has exact fixed-state routing, globally
   owner-disjoint preselection, and a quadratic-menu protected-wedge packing
   theorem.  Its remaining premise is no longer an abstract factor or raw
   candidate count, but literal cap activation, typed terminal/product
   capacity, and regeneration in the same child.

Neither program by itself supplies an integral one-copy owner chronology,
all upper witnesses, residence, a terminal compiler, and regeneration in
one child.

## 1. Gaussian/Bellman side

### 1.1 What is completely closed

Every internally superadditive Bellman table of grid size at most five has
strictly positive Rayleigh functional.  At grid six, the least-efficiency
branches `h=2` and `h=6` are also completely positive.  Thus a six-slot
separator, if one exists, must lie in `h=3,4,5`.

The all-grid affine setup-cost family

\[
                         V_m=\alpha m-\beta
                         \left\lceil {m\over h}\right\rceil
\]

is strictly positive throughout its admissible parameter interval.  This
is an arbitrary-grid theorem, but only for that one-parameter family.

### 1.2 The six-slot `h=3` frontier after the new closure

The exact three-chamber reduction remains authoritative.  Its status is now:

* **Chamber III:** closed.  Its two adverse finite pulses cancel jointly,
  leaving the prethreshold repeated-gap train; the new half-period theorem
  proves that train positive on its full domain.
* **Chamber II:** closed.  Strict convexity first eliminates the former
  stationary two-compact strip and reduces the chamber to

  \[
       P_-(P,a)=L_3(P;a,2a)>0.
  \]

  The outer period ranges follow from direct signs.  On the formerly open
  bounded range `4/5<P/A<11/12`, write

  \[
       \kappa(u)={K'(Au)\over2A},\qquad
       T_\rho(s)=\sum_{q\ge0}\kappa(q\rho+s).
  \]

  Exact derivative bounds imply

  \[
       -\kappa(x)-2\kappa(2x)
       >\kappa(\rho+2x)-\kappa(\rho).
  \]

  Subtracting the shift-stationarity equation
  `T_rho(x)+2T_rho(2x)=0` from the period residual leaves this strict
  compact bracket plus Gaussian tails with nonnegative coefficients.
  Therefore shift stationarity forces the period residual to be positive,
  contradicting period stationarity.  The bounded KKT locus is empty and
  the complete chamber is positive.
* **Chamber I:** both lower-period faces are now positive.  Strict convexity
  in the period direction collapses the former endpoint, pure, and late
  stationary exits to one scalar period-minimum gate

  \[
       \mathfrak S(a,b)=\mathcal G(p_*(a,b),a,b).
  \]

  A joint late stationary point must obey
  `p_*<xi<p_*+b<A` and an additional explicit curvature gate.  The sign of
  `mathfrak S` remains open.

The new scalar theorem underlying the Chamber-II/III advance is

\[
 F_{A/2}'(w)<0\qquad(0\le w\le A/3).
\]

It reduces the final boundary to a decreasing function whose minimum is the
arithmetic value `C(A/6)>0`.  This is a genuine positivity theorem, not a
numerical observation.

The complete canonical inert `h=4` branch and the complete canonical
least-density `h=5` branch are now positivity theorems.  For `h=4`, every
inert endpoint generator is literally
redundant: on faces `X,Y,Z` it equals respectively `c_1+c_5`, `c_2+c_4`,
or `2c_3`.  After the exact change of variables

\[
 p=A-P,qquad a=p-u,qquad\delta=v-p,qquad\tau=A+\delta,
\]

all three inert faces reduce to only two one-variable outer gates:

\[
 \mathfrak G_{XY}(\delta)=\mathcal H(\delta)+\mathcal I(\delta)+\mathcal S(\delta),
 \qquad
 \mathfrak G_Z(\delta)=C(\tau/2)+2\mathcal I(\delta).
\]

Every inner minimization is one-dimensional.  A period-uniform theorem
shows that every critical point of `F_tau` on `[0,A/2]` is a strict maximum,
and the complete endpoint/switch/KKT ledger is explicit.  The relaxed gates
are now signed on an explicit initial interval:

\[
 0\le\delta\le\delta_*={43849\over643260}
 \quad\Longrightarrow\quad
 \mathfrak G_{XY},\mathfrak G_Z>0.
\]

But the decoupled relaxation itself is not a viable full proof, because at
the far endpoint

\[
 \mathfrak G_{XY}(A/2)<-{21\over2000},\qquad
 \mathfrak G_Z(A/2)<-{9\over2500}.
\]

Thus the physical `h=4` theorem restores the correlation lost by minimizing
the reflected pairs and singleton separately.  This is a no-go for further
optimization of the decoupled gates, not a negative physical table.

Returning to the literal train restores the missing correlation.  The four
endpoint shifts form one additive rectangle

\[
                         \{0,u,P,P+u\},
\]

with `2tau/3<=P<A` and `0<=u<min(A-P,P/4)`.  The remaining residues satisfy
`y+z<P+u<A`.  Every physical table now obeys the single three-parameter
gate

\[
\begin{aligned}
 \Phi>\mathfrak R={}&C(\tau)+F_\tau(P)+F_\tau(P+u)\\
 &+\min\{C(\tau),F_\tau(u)\}-\Gamma(\delta),
\end{aligned}
\]

where `Gamma<3147/700000`.  At the formal far endpoint the rectangle gate
has the strictly positive margin

\[
                         \mathfrak R(A/2,A,0)>{23453\over700000},
\]

so the old negative endpoint was entirely an artefact of decoupling.  The
complete literal rectangle proof closes both inactive branches with margin
`>21/20000`; the active predecessor covers the switch with margin
`3653/700000`.

For `h=5`, the endpoint-defect polytope is genuinely four-dimensional, but
reflection reduces it to three nested rays.  Nested-ray transport closes
all faces for `delta>=A/15`.  On `0<delta<A/15`, the common endpoint
inequality `A-2m<=delta` forces `m>7A/15`; reflection handles both `m>A/2`
and `v>A/2`, and one three-way `u` split, charging all three theta errors,
gives the uniform margin `656/1000000` without using any `X/Y/Z` face
equality.  The `delta=0` threshold has margin `>163/70000`.  Hence no
canonical least-density `h=5` region remains.

### 1.3 All-grid minimal-counterexample structure

The formal cyclic Apéry clock and the physical Bellman clock agree after a
finite shoulder.  A minimal nonpositive clock must therefore be one of:

1. an endpoint-critical case;
2. a positive formal cyclic clock overturned by a quantified negative
   finite shoulder; or
3. a genuinely nonpositive subthreshold periodic clock.

For an honest cyclic Apéry clock whose gaps have at most one exception, the
only unresolved geometry is a long wrap.  A short first gap is exactly the
already-positive affine setup-cost clock, and an internal lone defect is
impossible.

At exact first carry the remaining long-wrap clock is

\[
 W_{qh+r}=q(A-a)+ra,
 \qquad0\le r<h,
\]

with

\[
 {A\over2(h-1)}<a<{A\over h+1}.
\]

The Euclidean shifted-block theorem absorbs every compact-train term into a
fixed `1/40` margin.  The remaining theta block is a right-endpoint
quadrature of the strictly increasing, zero-half-mean Jacobi reflection
error.  This gives the uniform all-period estimate

\[
 R_h(x)>-{1\over10000},
 \qquad
 S_h(a)>{249\over10000}>0.
\]

Hence **every** exact-first-carry one-defect long wrap is positive for all
`h>=4`; the former cutoff at one thousand is gone.  The only cyclic/physical
alternatives left by this route are now a genuinely multi-defect cyclic
word or a finite shoulder large enough to overturn a positive formal clock.

For a genuinely multi-defect exact-first-carry table, every prefix gap sum
is the minimum cyclic block of its length.  The uniform deficits form a
nonnegative subadditive gauge on the cyclic group.  Endpoint reflection
then reduces the compact loss to the maximum overlap depth `H` of two
ordered ray systems, with theta charge `tau`, and gives the exact lower
bound

\[
 \Phi(W)>{860-360H-\tau\over20000}.
\]

Therefore any remaining nonpositive formal clock must satisfy
`360H+tau>860`; under terminal ray coverage this already forces `H>=3`.
The multidefect obstruction is thus a triple-overlap geometry, not merely
the existence of two exceptional gaps.

The first triple-overlap period is exactly `h=8`.  On its sparsest honest
two-spike face

\[
  (a,a,a,a,b,a,a,t),
\]

the complete endpoint comparison is now positive.  The formerly open
large-spike chamber has the uniform margin

\[
                         {2283\over140000}.
\]

Moreover every arbitrary period-eight depth-three word has an honest
depth-three two-spike representative with the same first gap `a` and
period `P`.  This is only a geometric compression of the constraints.  The
corresponding functional compression is now disproved sharply: for
`a=A/15`,

\[
 (a,a,a,a+\varepsilon,4a-\varepsilon,a,a,4a)
\]

is honest with `H=3` and, for small positive `epsilon`, has strictly
smaller endpoint and literal Bellman functional than every same-`(a,P)`
canonical two-spike representative.  It remains positive, so it is not a
counterexample to Bellman positivity.

The failed compression is no longer needed.  Prefix-minimality makes every
terminal `i`-gap suffix a maximum cyclic `i`-block.  At period eight this
forces

\[
                         Y_2>{1\over4},
 \qquad                  Y_3>{3\over8}.
\]

Only the first reflected pair can therefore lie wholly before the quarter
point.  One coarse pre-quarter bound and two sharp post-quarter bounds give

\[
                         \Phi(W)>{859\over210000}>0
\]

for **every** honest exact-first-carry period-eight `H=3` clock.  Combined
with the previous `H<=2` closure, the complete exact-first-carry period-eight
branch is positive.

Period nine is now closed as well.  Here `H=3` forces exactly three rays.
The new analytic anchor is

\[
 f'(u)<0\quad(2/9\le u\le1/2),
 \qquad
 f(2/9)<{13\over250}.
\]

Terminal suffix maximality gives `Y_2>2/9` and `Y_3>1/3`; one unrestricted
pair, one two-ninth pair, one quarter pair, and the retained positive middle
train yield

\[
                         \Phi(W)>{367\over420000}>0.
\]

Together with `H<=2`, this closes every honest exact-first-carry period-nine
clock.

The suffix-max argument is now uniform in the period.  If `R_i` is the
terminal suffix of `i` gaps and `Y_i=alpha+R_i/A`, then exact-first-carry
prefix minimality gives

\[
 R_i\ge {iP\over h},\qquad
 Y_i\ge\alpha+{i\over h}(1-\alpha),\qquad
 Y_{i+1}-Y_i\ge\alpha.
\]

Consequently every terminal ray with `i>=h/4` lies strictly beyond the
quarter point, and at most `ceil(h/4)-1` rays can lie before it.  This is a
structural cutoff, not by itself a positivity proof; the small-period
closures also use sharper train and overlap estimates.

Period ten is now completely closed, including the first possible
four-overlap chamber.  The analytic anchors are

\[
 f'(u)<0\quad(1/5\le u\le1/2),\qquad
 f(1/5)<{101\over2000},\qquad
 \sup_{[0,1/2]}f<{27\over500}.
\]

Terminal suffix maximality gives `Y_2>1/5`, `Y_3>3/10`, and `Y_4>2/5`.
The new chambers have the strict margins

\[
 (u,H)=(3,3):\quad {3937\over420000},
 \qquad
 (u,H)=(4,3),(4,4):\quad {527\over420000}.
\]

Together with the previous `H<=2` closure, every honest
exact-first-carry period-ten clock is positive.

Periods eleven and twelve are now closed by one common ledger.  The
period-ten proof actually gives the sharper global bound

\[
                         \sup_{[0,1/2]}f<{1079\over20000},
\]

while the sharp quarter certificate gives `f(1/4)<1129/25000`.  For both
periods, terminal maximality puts every ray from the third onward strictly
past the quarter point.  Pricing only the first two pairs globally and all
later pairs at the quarter gives the exhaustive margins

\[
 u=3:\ {6753\over700000},\qquad
 u=4:\ {3641\over700000},\qquad
 u=5:\ {529\over700000}.
\]

The last chamber occurs only at period twelve.  Combined with the prior
`H<=2` theorem, all honest exact-first-carry clocks through period twelve
are positive.

Period thirteen is closed as well.  The key strengthening is the uniform
compact-train floor

\[
                         f(x)>{5503\over125000}
                         \qquad(0\le x\le1/4),
\]

obtained because every interior critical point is a strict maximum, so the
minimum on the quarter interval lies at an endpoint.  Now `Y_3>3/13>1/5`
and `Y_4,Y_5>1/4`.  Pricing the first two pairs globally, the third at the
one-fifth anchor, and the last two at the quarter gives the worst new
margin

\[
                         {1903\over125000}>0.
\]

The `u=3,4` margins are larger.  Period fourteen uses the same promoted
floor: `Y_3>3/14>1/5` and every ray from the fourth onward is post-quarter.
The new `u=6` chamber has margin

\[
                         {1761\over125000}>0.
\]

Together with `H<=2`, every honest exact-first-carry clock through period
fourteen is positive.

The promoted floor/global/one-fifth/quarter ledger continues through
period twenty.  Exhausting the maximal ray chambers gives

\[
\begin{array}{c|c}
h&\text{worst strict margin}\\ \hline
15&1761/125000\\
16&4751/500000\\
17&257/62500\\
18,19&93/31250\\
20&23/12500.
\end{array}
\]

Thus every honest exact-first-carry clock through period twenty is
positive.  At period twenty-one the old ledger first breaks at `(h,u)=(21,5)`,
but a new rational anchor

\[
                         f(4/21)<{5127\over100000}
\]

closes all chambers through eight rays.  The final nine-ray chamber is
closed by the far-ray certificate

\[
                         f(2/7)<{4083\over100000}.
\]

If `X_6<1/4`, the sixth pair gains `433/100000` over the quarter price,
exceeding the residual deficit `432/100000` by exactly `1/100000`.  If
`X_6>=1/4`, ordered early rays put pairs six through nine entirely in the
decreasing quarter interval, making them all positive.  Thus every honest
exact-first-carry clock through period twenty-one is positive.  The middle
train is not needed in the final proof.

Period twenty-two is closed by two further anchors,

\[
 f(2/11)<{513\over10000},\qquad
 f(3/11)<{107\over2500},
\]

and a nested `X_6/X_7` case split.  If either early endpoint has crossed
the quarter point, ordering makes every later pair free; otherwise the
corresponding far anchor pays.  The worst ten-ray chamber has margin

\[
                         {301\over250000}>0.
\]

Hence every honest exact-first-carry clock through period twenty-two is
positive.  The current finite anchor set first breaks at period twenty-three;
this is again a method frontier, not a negative clock.

The finite arguments now have one audited all-period ledger.  Given any
monotone anchor grid `t_j` with certified upper values `V_j`, every ray uses
the best eligible **clipped** price

\[
 \min\{0,L-V_j-\varepsilon\}\quad(t_j<1/4),
 \qquad
 \min\{0,L-V_j\}\quad(t_j\ge1/4).
\]

Terminal maximality makes an anchor eligible whenever `t_j<=i/h`.  Thus
the ray-only problem reduces to the one-dimensional discrete quadrature

\[
 L-\varepsilon+
 \sum_{i=1}^u\min\{0,L-B(i/h)\}>0,
\]

where `B` is the best theta-priced decreasing majorant supplied by the
anchors.  Positive raw anchor credit, such as the `2/7` gain at period
twenty-one, requires the separately recorded ordered-`X` case split; the
unconditional grid price is correctly clipped at zero.  The all-period
Bellman target is therefore a uniform Riemann-sum/overlap inequality for
one majorant `B`, not an endless list of unrelated finite chambers.

The finite shoulder is now also an exact scalar rather than a loose count.
For deficits `Delta_m=W_m-V_m` and edge slacks `sigma_(m,j)`, one has

\[
 \Delta_m=\min_j\{\sigma_{m,j}+\Delta_{m-j}\},
 \qquad \sigma_{m,j}\ge0.
\]

Along any critical denomination, the deficits form nonincreasing finite
chains.  A layer-cake decomposition gives

\[
 \Phi(V)=\Phi(W)-\mathfrak S_h(V\mid W),
\]

where `mathfrak S_h` is an explicit integral of finite derivative-prefix
trains.  Thus a positive formal clock is overturned exactly when this net
shoulder debt reaches its formal margin.  Critical-chain monotonicity alone
cannot rule that out; the remaining proof must use the full
cross-denomination min-plus coupling.

That coupling now has an exact tropical form.  Every derivative-prefix
train satisfies a strict-boundary min-plus recursion and an exact Pareto
minimum; along an attaining edge it splits into a boundary prefix plus a
literal translate of a lower-budget predecessor train.  For uniform clocks
the path cost is just the sum of seed deficits.  For the affine and
one-defect long-wrap clocks the only extra charge is respectively a
failed-coalescence count or a residue-carry count.  Above one charge quantum,
an active budget `m` forces at least `(m-1)/2` earlier budgets to be active
at half height.  Thus the free shoulder geometry is gone; the remaining
analytic issue is that the forced translates cross the sign change of
`K'`, so this spreading theorem does not yet bound the Gaussian shoulder
debt by the formal margin.

### 1.4 What Bellman positivity would and would not prove

A proof of the universal Bellman inequality would close the smooth
fractional configuration dual.  It would rule out every fractional
Rayleigh separator and validate the critical Gaussian coefficient.  It
would **not** automatically round the fractional object to one copy of each
named owner, one connected chronology, literal residence, upper witnesses,
or a common-cap compiler.  These are separate integral occurrence-labelled
gates.

## 2. Literal construction and common-cap router

### 2.1 Exact conditional factor theorem

Fix one materialized cap/guard/phase/occurrence state and one compensation
linkage.  If a literal incidence factor is left-`h`-regular and
right-at-most-`h`, every incidence has a private claim-to-port prefix, and
all active ports have one simultaneous typed suffix linkage to distinct
unused sinks, then weighting every prefix/suffix concatenation by `1/h`
gives a value-`|G|` fractional flow.  Integral max flow links every gain.

The abstract Middle-Levels two-factor supplies only the degree factor.  It
does not supply the physical occurrence injection, the private prefixes,
or the suffix linkage.

### 2.2 Two exact sufficient suffix-router interfaces

There are now two proof-safe ways to close the suffix row once a literal
fixed-state interface is exposed.

**Small Boolean port bank.**  If the active ports have distinct rank-`s`
Boolean values, each has at least `L` legal typed one-coordinate extensions,
the forbidden sink-value bank has size at most `L-1`, and `|P|<=L`, Hall's
theorem gives a full one-step private router.  In the intended regime

\[
 |P|=O(d(k)),\qquad |F|=O(d(k)),\qquad L=\Theta(k),
\]

the inequalities hold for all sufficiently large `k`.

**Large literal candidate atlas.**  Form the cross-list conflict graph of
whole typed suffix paths in one fixed state.  If every list has size at
least `L` and the **total** cross-list degree of every candidate is at most
`Delta`, Haxell's theorem gives a conflict-free transversal under

\[
                         L\ge2\Delta.
\]

A self-contained Lovasz-local-lemma proof gives the weaker sufficient row
`L>=2e Delta`.  Hence literal catalogues with

\[
                         L=\Omega(n^2),
 \qquad                  \Delta=O(n d(n)),
 \qquad                  d(n)=\Theta(\sqrt n)
\]

have a simultaneous suffix router for all large `n`.

**Matched-port reduction.**  A left-`h`-regular/right-at-most-`h` factor
already has a matching saturating its gain shore.  If the matched ports
have distinct rank-`s` Boolean values, then it is enough to route those
`|G|` ports, rather than the full active neighbourhood.  Incidence-specific
typed one-step menus still have pairwise overlap at most one, so Hall gives
distinct sinks whenever

\[
                         |G|\le L,
 \qquad                  |F|\le L-1.
\]

This removes unused factor ports and their type-compatibility obligations.
It does not create the matched literal prefixes or the sink occurrences.

The same Hall argument survives bounded value multiplicity.  If selected
occurrence ports have value multiplicity at most `rho`, meet `T` distinct
values, and every menu has size at least `L`, then the simple sufficient
row is

\[
                         T\le L-\rho,
 \qquad                  |F|\le L-\rho.
\]

Consequently two coordinatewise value-distinct banks (`rho=2`) admit one
**joint** suffix matching, including all cross-coordinate sink collisions,
when `T,|F|<=L-2`.  The prefixes and all shared capacities must be priced
in that same Hall instance, and any additional nonseparable ticket-pair
compatibility must already be encoded in the menus.

The degree `Delta` is global across all other lists.  An `O(nd)` bound per
other task, raw hexagon abundance, or individual path existence is not
enough.  All higher-order acceptance conditions must first be materialized
as capacities, typed identity gadgets, or pairwise conflicts.

### 2.3 Exact remaining router premise

The private prefix and suffix choices now coinstantiate in one fixed state.
For a rank-`s` gain `X_g`, call

\[
                 X_g\longrightarrow U\longrightarrow Y
\]

a good Boolean diamond when both direct occurrence arcs, the typed sink,
and all three unit capacities are already active in the same residual
cap/guard/phase state.  If every gain has at least `L_0` candidate ports
and every candidate incidence has at least `L_1` typed sinks, then two
successive pair-overlap Hall matchings select pairwise private diamonds.
For `p` gains and forbidden banks `f_0,f_1`, the exact sufficient rows are

\[
 p(L_i-1)-{p\choose2}-f_i\ge0,
 \qquad f_i\le L_i-1\quad(i=0,1).
\]

Thus `p,f_i=O(d)=O(\sqrt m)` and `L_i=Theta(m)` are more than sufficient.
Both arcs have empty interior, so endpoint injectivity is literal path
privacy; no later gammoid activation is hidden.  The two-coordinate
version first makes the port banks globally disjoint and then uses one
common sink matching.

This removes the former *separate* private-prefix and suffix-router gates
on any genuinely rich fixed-state face.  Prefix-rich and suffix-rich ports
in disjoint banks give a sharp counterexample, so marginal abundance in
separate states is not enough.

The canonical serialized factor face is not such a rich face.  Once a
factor is fixed, a lower source occurrence has exactly two certified factor
halfports, an owner has at most two adjacent certified q1 sinks, and an
own-turn incidence has exactly one.  Thus `L_0<=2`, `L_1<=2`, and
`L_1^{own}<=1`; the prospective quadratic wedge menu collapses to one
wedge at a fixed lower turn.  Consequently linear static-diamond abundance
is an alternative enriched-cap interface, not a theorem target supported
by the present factor state.

On the actual face, selected turn branches have an exact one-dimensional
activation law: two routes collide precisely when consecutive selected
turns use side pattern `1->0`.  A selected path-run is feasible iff no
forced one precedes a forced zero; a full component is feasible iff all
allowed-side sets share one bit.  For source-flexible tasks, more than
`3(p-1)` active candidate turn occurrences per gain give a private
nonconsecutive transversal greedily.  Fixed-source tasks do not have that
menu.  Their weakest remaining row is therefore the **protected-wedge
activation lemma**: choose the prospective wedge bank, its factor
completion, and one cap state jointly so that one typed branch of every
wedge survives.  Two-coordinate use still needs two physical source units
and the corresponding owner/terminal product capacity.

The former “arbitrary factor may choose the wrong ports” quantifier is now
removed abstractly.  On a Middle-Levels shore, first use the same
pair-overlap Hall argument to preselect one eligible incidence per gain (or
two sequential coordinate matchings), protect those exact edges, and only
then apply the small protected-factor theorem.  For two coordinates the
union is 2-bounded with exactly `2|I|` edges, so an `O(d)` bank embeds once
the total protected bank has at most `m-2` edges.  The joint matched-port
Hall theorem then routes only those protected ports.

Factor serialization also closes two formerly physical-looking rows.  An
oriented factor gives every protected incidence a unique
`(component,turn,side)` halfport address, its exact lower and owner values,
the singleton containment label, and a one-step prefix with empty interior.
The forced collision ledger is exactly lower-source load `d_P(L)`,
owner-cell alias load `d_P(U)`, and halfport load one.  Requested binary
roles obey one parity bit per component.  Opening loss is exactly

\[
 \sum_C\min_{L\in C}d_P(L)
 \le\left\lfloor{|P|\over3}\right\rfloor,
\]

and lossless opening is equivalent to a protected-degree-zero lower cut in
every component.  Distinct halfports can still alias one physical owner
cell, so common-cap activation and capacity identity remain external.

On the canonical turn-diamond face, the one-coordinate alias is now solved
exactly.  A factor turn `L_j` has the two literal chains

\[
 L_j\longrightarrow U_j\longrightarrow Z_j,
 \qquad
 L_j\longrightarrow U_{j+1}\longrightarrow Z_j,
\]

where `Z_j` is its occurrence-labelled upper q1 union.  Choosing the left
chain at every turn of a component, or the right chain at every turn, uses
each lower source, owner cell, and `Z_j` exactly once.  These are the only
full adjacent-owner/own-`Z_j` unit routings: a cyclic binary choice with no
owner collision has no `1->0` transition and is therefore constant.

Thus one claim per lower turn needs neither private formal halfports nor a
full-port suffix-rank theorem on this face.  The sharp product boundary is
also exact: two claims per turn cannot cross one unit owner shore, since
`2ell` demands meet a cut of capacity `ell`.  A two-coordinate construction
must use globally owner-disjoint selected banks, capacity-two/product
layers, or a physical coordinate split; it also needs distinct source and
terminal capacities.

The first of those repairs is now available abstractly.  Sequentially
preselecting coordinate banks while deleting **all** previously selected
upper owners gives a globally owner-disjoint family.  If coordinate `q`
has menu floor `L_q`, the fixed forbidden bank has size `f`, and there are
`p` gains, Hall reduces exactly to

\[
 f+qp\le L_q-1,
 \qquad
 p(L_q-1)-{p\choose2}-f-qp\ge0.
\]

The simpler sufficient row is `p<=L_q` and `f+qp<=L_q-1`.  Hence any fixed
number of `O(d(k))` coordinate banks with linear Boolean menus can be made
owner-disjoint for all large `k`.  For two coordinates the selected-bank
loads are now lower source two, upper owner at most one, and halfport one.
This removes the owner alias, but not the two source units, cap activation,
distinct typed terminals, or product closure.

A stronger correlated preselection is also available when one needs a
complete protected turn rather than one incidence.  At a lower turn `L`, a
full wedge chooses two outside coordinates `{a,b}`, protects both owners
`L+a,L+b`, and fixes the q1 terminal `L+a+b`.  A fixed wedge conflicts with
at most `m-1` wedges in another menu through each owner and at most one
through its terminal, for the exact bound `2m-1`.  Hence menus of size

\[
                         Q>(p-1)(2m-1)
\]

admit a greedy choice of `p` wedges with all `2p` owners and all `p` q1
terminal values distinct.  The selected bank has lower degree two, upper
degree one, and `2p` edges, so it extends inside one Middle-Levels
two-factor whenever the protected edge-count and compatibility rows hold.
Because full menus have quadratic size while `p=O(d)=O(sqrt m)`, this
packing has asymptotic room.  Literal activation, typing, conjunctive
source/terminal multiplicity, and product closure remain external.

The topology quantifier is now exact.  Fix a tree-compatible pull host `H`
of a factor containing the protected wedge bank `D`, and delete every pull
whose occurrence support meets `D`.  A wedge-preserving Hamiltonization
exists exactly when the residual host `H_D` is connected; if a prescribed
pull bank must also survive, it must be a graphic forest in `H_D`.  If one
protected wedge blocks at most `2lambda` host edges, then

\[
                         |E(H)-E(H_D)|\le2p\lambda,
\]

so `kappa(H)>2p lambda` is sufficient.

This does **not** let one freeze the factor first.  A fixed factor supports
exactly one wedge at each lower turn, while a prospective menu of
`binom(m,2)-1` wedges can omit precisely that one.  Hence quadratic wedge
abundance and static-host connectivity do not commute.  The remaining
topology theorem must choose the wedge bank and the factor/pull host jointly,
or prove the protected-pull cut for an adaptive completion.

The adaptive completion problem now has an exact rank formula.  All
two-factor completions containing a protected bank `D` and avoiding a fixed
bank `Z` lie in one exchange class under `D`-transparent alternating closed
trails.  Define `rho(D,Z)` as the maximum size of a graphic forest `R` for
which `D union R` is degree at most two and has zero exact guarded
Ore--Ryser extension deficiency.  If `N` is the Middle-Levels vertex count,
then

\[
 \min_F |\operatorname{Comp}(F)|=N-\rho(D,Z).
\]

Thus Hamiltonicity is exactly `rho=N-1`, and at most `c` components is
exactly `rho>=N-c`.  This is the joint factor/forest condition; the
extendable-forest family is not asserted to be a matroid.

Even a disconnected static protected-pull host has a useful rescue.  A
maximal forest of its residual host leaves at most

\[
                         1+|D|\lambda=1+2p\lambda
\]

factor components for `p` wedges of pull load `lambda`.  This is `O(1)`
when task birth and pull load are bounded, but only `O(d)` for `p=O(d)`.
Crucially, a bounded number of cycles alone is not yet an additive-constant
word: two literal history states can require `Theta(d)` reset letters.  The
next exact bridge is a completed-hinge zero-cost fusion or a globally
`O(1)` guarded overlap tour, together with bounded compiler deficiency.

For the common-core ring, the exact topology target is now sharper than
either host connectivity or a component-count bound.  Let `H_D` be a
tree-compatible pull host after deleting every pull touching the protected
bank, and call a factor cycle **rooted** when it contains a ring hinge.
Switching a maximal forest in each component of `H_D` leaves exactly one
factor cycle for every rootless host component.  Therefore

\[
 F'\setminus S\text{ is a forest}
 \quad\Longleftrightarrow\quad
 \text{every component of }H_D\text{ contains a rooted factor cycle}.
\]

Equivalently, every nonempty root-free component set has a transparent pull
leaving it.  After fixing one perfect matching, the second matching is a
successor-permutation cycle cover and the same condition says that every
permutation cycle meets the root set; the nonroot arcs must be graphic
independent.  Thus ordinary Hall/factor extension is not enough.

The special ring geometry further collapses root placement to one
panchromatic-core condition.  A size-`m` ring hits all factor components iff
there are at most `m` components and their lower shores have a common
rank-`m-2` subset.  A union-bound shadow inequality is an exact sufficient
condition, and the complete-permutation benchmark has expected
`m-1` such cores.  But no transfer to the sparse protected successor graph
is known.  Two forced, mutually Johnson-separated incidence hexagons give
an explicit obstruction: even a factor with at most `m` components need
not admit any common-core ring transversal.  Hence factor, ring, and
transparent-pull host must be chosen jointly.  Forest complement also does
not by itself certify that the ring's fixed cyclic head shift induces one
cycle on the resulting path pieces.

That bridge now has an exact min--max formulation.  Choose one jointly
completed occurrence-labelled hinge `a_i->h_i` from each residual factor
component.  Put an arc `i->j` in the component compatibility digraph when
role `i` may replace its head by `h_j` with every owner, lower, residence,
upper-witness, cap, and compiler ticket unchanged.  Reassigning heads by a
permutation produces exactly the permutation's cycle count.  Therefore
zero-extra fusion is equivalent to a directed Hamilton cycle in this
completed-hinge digraph; a strict two-switch cut expansion is a finite
sufficient certificate.

Without completed hinges, the exact alternative is a minimum guarded
overlap tour.  For bare order-`d` histories its edge cost is

\[
                         \delta_d(u,v)=d-\operatorname{ov}(u,v).
\]

An all-pairs connector of cost at most `K` exists exactly when every exit
ends and every entry begins with one common literal core of length `d-K`.
This criterion must hold for the **complete** regenerative signature, not
just the raw history word.  The obstruction is sharp: `x^d` and `y^d`
already cost `d`, and equal histories with incompatible invariant cap flags
have infinite guarded cost.  Thus the new supply target is precise: produce
completed hinges with a common length-`d-O(1)` core or prove Hamiltonicity
of their compatibility digraph, while keeping final compiler damage
bounded.

The current Pascal/turn-diamond and promotion/common-core machinery does
**not** prove that supply.  The turn projection forgets order-`d` histories
and every cap/compiler guard, so independent component tags preserve all
owner/q1/wedge statements while leaving only compatibility loops.  The
promotion `2H`-core `Q_U` is a coordinate-containment core; its retained
central words lie in `U\setminus Q_U` and are ordered separately in each
top.  Thus `H/d\to\infty` supplies local aperture, not one common literal
history.

For one proposed full regenerative state `xi`, let `S_xi` be its
occurrence bank.  The exact component-hitting deficiency is

\[
 \eta(D,Z;\xi)=\min_F\beta(F\setminus S_\xi).
\]

It counts precisely the factor components missing that state.  Hence the
Common-Core Component Transversal is the single graphic condition
`F\setminus S_xi` is a forest.  On the fixed-edge Middle-Levels face this
has an exact guarded Ore--Ryser forest-extension criterion.  Jointly
completed `S_xi` then gives zero-cost fusion; a common guarded `K`-router
with bounded components gives constant cost.  The missing state is therefore
an actual ordered `d-K` core together with orientation, residence, upper
witnesses, occurrence/cap state, bounded compiler damage, joint hinge
semantics, and the forest-complement row.

An explicit local supply now exists.  For every fixed `c>=3`, choose one
rank-`(r-2)` set `B`, partition it into the same ordered `d` nonempty source
letters, and surround that common history by a cyclic family of two-letter
screens.  The resulting `c` hinges have distinct owners, pointwise-fixed
lower q1 colours, cyclically permuted upper q1 colours, and one literal
common order-`d` history.  The cyclic head shift fuses `c` components with
zero added positions and preserves, as an occurrence multiset, **every**
interval-OR value of width at most `d`.  In fact every strict-lower interval
value of arbitrary width is preserved: any interval meeting both screens
already contains a rank-`r` owner.  Thus the entire strict-lower compiler
transports with zero deletion.  Its `2c` protected incidence edges have
maximum degree two, so the small protected-factor theorem unconditionally
plants the ring in a spanning owner/lower-q1 two-factor whenever
`2c<=m-2`; the cyclic replacement remains a two-factor.  A separate
two-component `K_(2,2)` switch has the same common history and short-deck
invariance, with at most four local immediate-palette casualties.  Any old
upper target that can be lost by the cyclic ring lies in one of the `c`
upper cones above its rank-`(r+1)` seam bases, a family of size at most
`c*2^(k-r-1)`.  Therefore the history word, owner/lower-q1 planting, and
strict-lower compiler are no longer missing.  The exact residual theorem is
global: choose protected upper witnesses outside those cones' changed hinge
edges while distributing one compatible ring across the residual factor
components and one common cap state.

The full-size specialization `c=m` now also has an explicit covariant upper
reservoir.  All seam bases share the rank-`(m-1)` core `K=B+b`; every
possible damaged target is `K union T`, where the external trace `T`
contains a cyclic ring edge.  A family of `m` top geodesics witnesses every
cyclic-interval trace, and private trace paths witness every remaining
trace.  The complete bank uses `O(m2^m)=o(W)` incidences and has no repeated
owner, immediate-lower colour, or immediate-upper colour.  With the first
`K` deletion chosen as `b`, the `m` ring hinges are literally the first
top-path edges, not extra occurrences.  Under the cyclic rethread, every
top prefix union is cyclically transported and every private path is
unchanged.  Thus, **after the joint bank is planted**, every arbitrary-width
upper target survives as well.

Planting is the remaining nontrivial row.  Sublinear size and degree two do
not suffice: an explicit `6m-8`-edge one-cone bank violates a singleton
residual Ore--Ryser cut.  For a protected bank `P`, the exact cut slack is
the weighted boundary

\[
 m\sigma(A)=(m-2)n_1(A)+2b_{\ge2}(A),
\]

and extension is equivalent to charging every protected loss against this
quantity for every lower-shore cut `A`.  Even after factor completion, the
`m` distinguished hinges must still be placed on distinct components (or
an equivalent forest-complement condition proved), and the private paths
must be co-instantiated with residence and the cap.  The former vague
upper-witness selector has therefore collapsed to an explicit bank plus
one exact all-cut factor/forest problem.

The local residence row of that bank is now also closed asymptotically.
For trace size `q<=m-d-1`, shorten the fixed-trace path to `q` consecutive
windows; every internal positive `K`-run then has length `m-q>=d+1`.
The remaining top tail contains only `2^{o(m)}` targets and admits
pairwise owner/lower/upper-disjoint monotone geodesics, selected by a
uniform central-binomial reservoir.  Every coordinate on such a geodesic
has only an initial, terminal, or full run.  Hence the complete protected
bank is internally `d`-clipped resident and remains so after the cyclic
ring rethread.  Endpoint collars and global cyclic residence remain part
of the eventual host theorem.

The all-cut factor row has likewise been localized exactly.  With
`s(A)=|N(A)|-|A|` and
`b(A)=sum_{2<=a_U<=m-1}(m-a_U)`, one has

\[
 (m-1)\sigma(A)=(m-2)s(A)+b(A),
\]

while the protected loss is crossing incidence minus the one-neighbour
rebate.  Every failed cut for a bank with `e` edges therefore satisfies

\[
 \min\{|A|,W-|A|\}< {m(m-1)\over2m-1},e.
\]

For the common-core reservoir this is `O(m^2 2^m)=o(W)`.  Equality in the
shadow bound is classified completely: `A` is a disjoint union of
`binom(S_i,m-1)` with pairwise support intersections at most `m-3`.
Thus arbitrary global cuts are no longer the extension obstacle; the
remaining theorem is a cut-thin choice on this small/co-small,
near-clique-closed family.

That residual family has now been reduced further.  Every private target
trace admits a geodesic-minimum `q`-owner witness.  A balanced triple rule
closes every singleton Ore row, every cut with complementary shore at most
`m-2` is automatic, and the resident high tail can be packed while
preserving those singleton inequalities.  Alternatively, independent
trace spreading gives absolute singleton and private-endpoint load at most
ten and hence

\[
                         \lambda_P(A)\le15|A|+2m.
\]

For this spread bank every zero-clique-defect cut and every principal
up-star is safe.  A stronger constrained version retains the common
triple window `G_2` and still closes all `b(A)=0` cuts; its exact Hamming
Lipschitz estimate also closes explicit positive-defect neighbourhoods.
The original broad endpoint-spread claim was corrected: the fixed top
bank has `m` endpoints above `K`, so those top endpoints are priced by the
separate `2m` term rather than hidden in the constant private load.

Protected deficiency is componentwise on the lower Johnson graph.  Both
`sigma` and `lambda_P` split exactly over induced Johnson components, so a
failed cut always has a connected failed component.  Connected
`t`-vertex candidates have the elementary entropy bound
`W[m(m-1)]^{2(t-1)}`.  After all preceding closures, the exact unresolved
Ore family is therefore Johnson-connected, small or co-small,
positive-`b`, low-expansion, outside the principal-star and certified
Hamming-stability regions.

The positive-defect geometry is now substantially sharper.  Hamming
distance to the zero-`b` class has the optimal general scale
`Theta(m sigma)`, and no polynomial multiple of `b` controls that distance.
The replacement is an exact block-gluing identity: the protected Ore
margin of a union of complete support blocks equals the sum of their
individual margins minus an explicit cross-owner penalty.  This closes
two-block overlaps and their `Theta(m)` Hamming neighbourhoods, together
with a broad low-fibre singleton-margin regime.

For the constant-spread reservoir, every canonical two-sided Boolean
interval is now closed.  If

\[
 \mathcal A(C,S)=\{L:C\subseteq L\subseteq S,\ |L|=m-1\},
\]

its exact normalized slack is

\[
 u-2+{2(m-u)\over m-c},
\]

and its protected loss splits into one core-exit current and one saturated
support-boundary current.  The core current has at most two crossings per
resident path.  Combining this with the absolute singleton cap, the exact
singleton block-gluing identity, and a uniform binomial separation proves
that **every** such `A(C,S)` passes protected Ore for all sufficiently large
`m`, in one common physical bank.  Thus the canonical interpolation between
complete supports and principal stars is no longer open.

Ordinary isoperimetry cannot finish what remains.  Under complementation,
`sigma` is exactly a two-capped lower-shadow excess; coordinate compression
never increases it.  There are connected shifted two-level colex families
in the localized size range with `sigma/|A|<6`.  They are explicitly unions
of two Hamming-adjacent principal stars.  Low slack does, however, force a
dense Johnson neighbourhood on more than half the members once
`m>=144, |A|>=2m`.  The exact residual Ore theorem is therefore an
erosion/protected-crossing theorem for shifted partial-colex or multi-centre
families, not a stronger scalar shadow bound.

The explicit adjacent-star obstruction is now closed, and the closure is
substantially broader.  For a monotone union of `h` arbitrary-rank principal
stars, the owner fibres and cross-owner current have an exact
inclusion--exclusion formula.  On the same constant-spread physical bank,
the resulting protected Ore inequality holds uniformly whenever

\[
                       4^h(h+\log m)=o(m).
\]

In particular it holds for every
`h <= (1/2-epsilon) log_2 m`.  This includes the adjacent pair and every
fixed-width shifted/colex star union.  A naive decomposition into a
logarithmic head plus a Hamming-paid geometric tail is nevertheless false:
already for singleton stars its next-shell/tail ratio is
`Theta(m^2/h)`.  Thus the remaining cut theorem concerns genuinely
growing-width shifted/Macaulay structure outside this DNF regime; it cannot
be obtained by charging the discarded tail to ordinary Hamming distance.

Initial colex families now have an exact erosion normal form.  If

\[
 |F|=\sum_{j=s}^m{c_j\choose j},
 \qquad \rho_j=c_j-j+1,
\]

then the complement of `F` is simultaneously a disjoint union of
two-sided Boolean intervals and the monotone DNF of their principal-star
cores.  Cross-block shadows are triangular: every shared owner has one
unique terminal internal block, and all earlier blocks contribute boundary
singletons.  In fact every shared facet belongs to exactly two blocks, so
the total triangular charge is the exact sum
`sum_j(m-j)binom(c_j,j)`.  The six-row protected-current table shows complete
cancellation at protected degree two and identifies the entire remaining
tax at degrees zero and one.

For any safe high-index head, the audited erosion inequality is

\[
 \mu_P(A)\ge\mu_P(A^{\rm head})+
 \sum_{j\le r}\left({j\over\rho_j}-12\right){c_j\choose j}.
\]

Hence every tail with nonnegative aggregate aperture credit is safe; in
particular, `rho_j<=j/12` is a termwise sufficient condition.  The broad
terms `rho_j>j/12` are the only negative contributors in this singleton
certificate.  A stronger whole-block reduction leaves intrinsic
nonpositive credit only when `rho_j>=j` (apart from one zero singleton
endpoint).  A two-level example proves why merely declaring each
interval safe cannot finish the argument: its literal pivot current can
equal the whole smaller block.

Maximal constant-`rho` runs now supply precisely that first grouping.
Their cores are `R+{p_j}` for one common root, so the entire run is

\[
 \{L:R\subseteq L,\ L\cap X\ne\varnothing\},
\]

equivalently one principal star with a two-sided interval removed.  Its
loss is exactly one root-deletion current plus one unique-hit current, with
a path bound linear in `|X|`.  The localized size theorem forces
`rho<m/2`, and every intrinsically nonpositive run (`j<=rho`) then passes:
small `rho` follows from the all-cut margin, while the remaining range has
a uniform entropy gap over the path catalogue.  The strict-jump interaction
has now also been closed.  If the top aperture is at most `m/10`, the
owner-fibre cap gives a uniform linear margin; between `m/10` and `m/2`,
the top Macaulay term has an exponential entropy advantage over all lower
negative credit and the complete protected catalogue.  The aperture-one
tail has total debt at most `66`, while its pure common-root face has exact
slack `h(m-2)` and loss at most `10h+binom(h,2)`.  Hence **every localized
initial-colex cut passes protected Ore** for the same constant-spread bank.
This theorem has an independent audit.  Initial colex is no longer an open
subcase; transfer from an arbitrary failed cut into that class remains
open.

That transfer now has an exact flow formulation.  Delete the protected
incidences and give every lower vertex and owner residual degree `2-d_P`.
For every lower shore `A`,

\[
 \mu_P(A)=\sigma(A)-\lambda_P(A)
 =\sum_U\min\{2-d_P(U),d_{G-P}(U,A)\}
  -\sum_{x\in A}(2-d_P(x)).
\]

Thus `mu_P` is submodular and its negative is exactly the capacitated Hall
deficiency.  Maximum-deficiency shores form the full
Dulmage--Mendelsohn min-cut lattice, with unique minimal and maximal
members.  The minimal shore contains no protected-degree-two lower vertex;
for the constant-spread bank every nonexceptional member has at least
`2m-32` neighbours inside its induced Johnson graph.

The correction to the naive compression route is important.  Forced
members of the minimal DM shore cannot be exchanged away at zero cost.
After contracting residual-network SCCs, add an implication arc
`[x]->[y]` whenever `y` is an elementary downward coordinate shift of
`x`.  A shifted maximum-deficiency shore exists exactly when the sink SCC
is not reachable from the source SCC in this augmented digraph; the source
successor-closure is then the unique minimal shifted mincut.  The remaining
arbitrary-cut factor gate is therefore two exact statements: exclude that
implication path for some coordinate order, and classify the resulting
shifted capacity-closed shore (or classify the irreducible DM core
directly).  DM closure alone is not asserted to force colex.

The co-small half has a separate exact normal form.  For an incidence-lift
path bank, let `Z_P` be its protected lower q1 palette.  The minimal DM
shore forces `Z_P` into its complement `C`; writing `C=Z_P dotcup B`,
failure is exactly

\[
 \Omega_P(C)>2|B|,
\]

where `Omega_P` counts only residual capacity on fully filled owners and
unprotected owners missing one facet, with forced gaps from `Z_P` priced
explicitly.  A sufficient all-`B` certificate is the pointwise harmonic
bound

\[
 \Gamma(x)=\sum_{U\supset x}
 {2-d_P(U)\over m-|N(U)\cap Z_P|}\le2.
\]

Its exact mean is already two.  Hence aggregate random spread cannot prove
it: the co-small route needs a perfectly balanced q1 design or a less
pointwise argument exploiting correlations between optional vertices.
The forced base itself is now constructively safe.  Forbidding the
polynomial family of q1 facets lying under owners with at most two
`K`-coordinates does not affect the low paths and is absorbed by the high
greedy supply.  The resulting forced palette has positive gap at every
owner, and gap one only at protected degree two, so
`Omega_P(Z_P)=0` exactly.  Only the optional bank `B` and its correlated
harmonic allocation remain on the co-small side.

There is also a factor-first alternative, but its minimum-component form is
now refuted.  Decompose owners by their exact
external trace `T`.  The saturating-cycle theorem gives, in every
nonempty damage slice `1<=|T|<=m-2`, a deterministic minimum-component
path cover with one component whose owner union is `K union T`.  Thus the
exponential bulk of damage targets is witnessed automatically.  After
contracting those slice paths, completing the Middle-Levels factor is
exactly one physical endpoint matching; its rank-prefix scalar surplus is
`binom(m-1,q)^2`, and the ring hinges are literal endpoint-connector
switches.  Exact endpoint conservation forces

\[
                         e_q=2{m-1\choose q}^2
\]

cross-trace incidences at every rank.  The minimum-component forests fail
this already at `q=2` for every `m>=4`.  The least raw repair splits
`(1/2+o(1))W` additional path components.  This costs no word positions,
but radically changes the architecture and still leaves occurrence Hall,
the co-singleton distinct-edge rule, quotient-cycle fusion, residence, and
the cap.  The factor-first route is therefore a secondary `Theta(W)`-split
architecture, not a current bypass of protected Ore.

The topology row now has an exact adaptive formulation.  In a transparent
pull host, maximal forest switching leaves exactly one defect in each host
component not met by a selected hinge root.  Equivalently, the protected
ring extends precisely when every host component is root-bearing.  In the
fixed-matching form, every successor-permutation cycle must meet the root
set.  A common-core ring can be placed across all components exactly when
there are at most `m` components and their lower shadows share one
panchromatic rank-`(m-2)` core.  Two forced disjoint six-cycles show that
component count alone does not imply that core.

For a fixed canonical pull family, the obstruction is sharper: one lower
root sees at most four accessible wedges, common-label support averages
exactly two, and the union over canonical pull phases averages at most
eight, while a full ring needs all `binom(m,2)` wedge choices.  Thus no
factor frozen before the ring can be a universal host.  The surviving
quantifier order is joint.  Given a protected reservoir phase cover,
Hamilton extension is equivalent to connectivity of the residual
contracted pull quotient (with the analogous exact rooted path-cover
criterion).  The remaining topology lemma is to choose the ring/reservoir
and factor together so that the induced `m`-state predecessor arcs form one
Hamilton cycle with globally consistent pull labels and the residual
quotient is connected or root-covered.

The cap-side wedge combinatorics has also collapsed to an exact threshold.
For `p` sources, `q` already selected protected wedges forbid at most

\[
 B_q={m\choose2}-{m-q\choose2},
\]

and this is sharp; the cross-menu cost of one selected wedge is `m-1`, not
`2m-1`.  Menus larger than `B_{p-1}` therefore admit globally distinct
owner/q1-terminal wedges.  Those distinct owner sets make their factor
turns automatically nonconsecutive, so one active typed branch per wedge
routes privately.  The remaining issue is activation in one cap state,
not routing interference.

There is now a precise gammoid bypass for that activation.  Let `P_0` be
the union of the `m`-owner stars of the required lower turns and let
`Gamma` be the completion-stable typed suffix gammoid.  If

\[
 |P_0|-r_\Gamma(P_0)\le m-p,
\]

then every basis meets each star in at least `p` owners, its supported
wedge menu exceeds `B_{p-1}`, and the preceding packing plus gammoid
heredity routes all claims.  More generally it is enough to find one
independent set meeting every source star in `p` owners.  The bound is
sharp at corank `m-p+1`; a common-owner-star example also proves that many
individually active wedges do not imply joint owner capacity.  The exact
remaining cap premise is therefore an occurrence-level proof of this
near-full rank bound (or the corresponding factor-restricted Rado cuts),
after pricing the fixed compensation linkage and prefix interiors.

At the Boolean-value level, even that raw rank premise is now constructed.
For arbitrary distinct lower turns

\[
 p\le\left\lfloor{m+2\over4}\right\rfloor,
\]

the union of all `p` complete owner stars has a simultaneous one-step
linkage to distinct rank-`(m+1)` terminals.  The proof processes the stars
sequentially.  Terminals chosen at each earlier star lie on one Hamilton
cycle of its `K_m` terminal graph; hence an adjacent new source loses at
most two candidate edges to that entire earlier source, while a distance-
two source loses at most one.  After `i-1` stages the current `K_m` has
minimum degree at least `m-2i+1>=m/2`, so another Hamilton cycle exists.
Shared owner ports are deduplicated.  This yields a literal full linkage of
the entire port union, not merely a fractional or all-cut certificate.

Consequently a priced deletion bank hitting `h` of these disjoint paths
leaves suffix-gammoid corank at most `h`.  For bounded `p`, the near-full
wedge theorem closes as soon as `h<=m-p`.  The cap row is therefore no
longer abstract owner-port rank: it is the physical materialization and
typing of the selected rank-`(m+1)` occurrences, plus a linear or smaller
deletion footprint.  Endpoint-factorized activation has two additional
quantitative forms: bounded rank-layer crossings give zero defect, while a
linear total owner/terminal footprint gives only `O(1)` wedge casualties
for `p=O(sqrt(m))`, even if one compensation path snakes through many
owners.

The current parent/reference construction has not been proved to activate
these canonical skeleton prefixes inside the same residual common-cap
network, retain the typed sink occurrences, and resolve owner-cell aliases
and source multiplicity.  The smallest currently visible literal statement
is one
of:

1. a gain-saturating incidence matching whose selected distinct Boolean
   ports have linearly many incidence-typed one-step extensions and only
   `O(d)` forbidden sink values; or
2. two such coordinatewise banks whose union has multiplicity at most two,
   with globally private prefixes and one joint physical sink bank; or
3. distinct Boolean occurrences for the whole active port bank with the
   same one-step extension row; or
4. whole typed path lists of quadratic size with total cross-list conflict
   degree `O(nd)`.

Without one of these literal occurrence interfaces, the exact boundary
remains the factor-restricted typed suffix Rado rank, or equivalently every
residual trapped-menu cut.  Abstract eligible-port preselection and
two-factor completion are no longer the missing combinatorial step.

### 2.4 The two-coordinate type mismatch is now sharp

The canonical folded-C8 terminal pair is an incomparable Boolean diamond:
its ray values `X,Y` have meet `C` and join `U`.  The native first-exit or
q1/q2 terminal bank is a nested Hasse pair `R<V`.  No two-native-cell
literal conversion can preserve both target identities; an injective
lattice map preserves incomparability.

At socket level, the exact minimal repair is one polarity bit:

\[
 C\mapsto(R,0),\quad X\mapsto(R,1),\quad
 Y\mapsto(V,0),\quad U\mapsto(V,1).
\]

The existing occurrence-coordinate/role field can supply this bit without
a new stored state, but only when the exact `X,Y` witnesses remain upstream
inside one deterministic complete bundle and one cap accepts the product
type.  Alternatively both roles may coalesce on one existing join-envelope
cell only when its literal value is exactly `U`, both complete source-free
routes exist, and dual-role acceptance is explicit.  Thus the missing
two-coordinate theorem is no longer an abstract socket count: it is the
materialization of a background-compatible **polarized complete bundle**.

## 3. The shortest honest all-dimensional implication

Within the current regenerative architecture, the shortest sufficient
theorem is still a **uniform co-instantiated bounded-charge reset spine**.
There must exist one compatible infinite odd spine, with an even terminal
tap at every stage, such that each complete terminal certificate has total
charge at most one absolute constant.  Every local witness must occur in the
same materialized child.

The per-transition content can now be stated in four rows.

1. **Integral host and chronology.**  Round the fractional owner/trace
   circulation to one copy of every named owner, with connected or
   serializable topology, residence, and the complete upper deck.
2. **One-child packet bank.**  Plant every source/helper/reset module with
   its occurrence, guard, endpoint, and compiler tickets in that same
   child.
3. **Literal service.**  Supply private claim-to-port prefixes and close the
   common-cap suffix row by one of the two router interfaces above; account
   for the complete background/compiler damage in the same state.  For the
   two folded-C8 coordinates, retain the exact ray witnesses and materialize
   either a polarized native socket bundle or an exact accepted join-envelope
   coalescence.
4. **Regeneration and terminal charge.**  Export a literal next auxiliary
   state while keeping the odd and even terminal repair charges uniformly
   bounded.

These rows imply

\[
                         \nu(k)\le B(k)+O(1)
\]

because terminal damage is paid only once at the requested dimension.  The
statement is conditional because no theorem currently co-instantiates all
four rows along one infinite spine.

## 4. Exact mathematical frontier

The present proof effort has three sharply separated targets.

### Analytic target

Chamber II is completely closed, every honest exact-first-carry clock
through period twenty-six is positive, and the complete canonical
six-slot inert `h=4` and least-density `h=5` branches are closed.  On the
`h=4` residual rectangle the closed active-`Gamma` side has margin
`3653/700000`; one common low/upper bank signs the entire inactive side by
`21/20000`.  For `h=5`, nested-ray transport closes `delta>=A/15`, while
the all-face reflected endpoint argument closes `0<delta<A/15` with margin
`656/1000000`; the threshold handles `delta=0`.

At period twenty-six, the sharpened global estimate closes every overlap
depth at most four.  Ordered anchors reduce all remaining geometry to two
residual chambers, and a middle anchor closes both for reflected depth
`6<=u<=10`.  The remaining near-half depths `u=11,12` are now closed by
the exact global compact price `f(x)<1053/20000`: repricing precisely the
first three far rows contributes `1950/1000000`, leaving strict residual
margins `68/1000000` and `302/1000000`.  Thus period twenty-six is a
complete theorem, independently checked with rational certificates.  The
all-period exact-first-carry target is now a uniform continuation of the
certified one-dimensional anchor-grid quadrature, not an unresolved
period-twenty-six terminal geometry.
A separate uniform theorem must still prevent a finite
physical shoulder from overturning a positive formal clock; the exact
tropical Pareto/cocycle reduction for that row is available.

### Integral-rounding target

Turn the exact fractional triangular chain factor and stationary literal
trace circulation into a one-owner-once, one-target-once connected Euler
chronology with bounded sidecar.  Fractional feasibility has no remaining
rank-marginal separator; the obstruction is named integral colouring and
component fusion.

### Regenerative common-cap target

In one child, expose the physical port injection and a typed suffix atlas
satisfying either the small-Boolean Hall conditions or the Haxell global
load condition, while retaining the background matching, upper witnesses,
residence, and the next-state boundary.

The additive conjecture is therefore no longer blocked by an unspecified
scalar count or an abstract common-basis problem.  It is blocked by one
integral co-instantiation theorem: an owner-exact regenerative chronology
whose literal service interface satisfies a capacity-faithful router
certificate.

## 4.1 Latest correlation, rigidity, and residual-cut refinements

The cap-side Boolean rank and occurrence-existence rows now correlate
exactly.  For arbitrary distinct lower turns

\[
 p\le\left\lfloor{m+2\over4}\right\rfloor,
\]

the sequential Dirac cycles used by the full owner-star linkage each have
an edge whose two owner endpoints are new.  Selecting that edge as the
protected wedge forces the linked terminal to be the wedge's literal q1
turn occurrence after factor completion.  Thus the remaining cap premise
is no longer existence of an occurrence carrying the Boolean edge; it is
typed survival of that occurrence in one complete cap state and
nonaccumulating regeneration.

The companion owner-area theorem removes path monotonicity from the damage
ledger.  An arbitrary background whose distinct owner projection has size
`f` and whose terminal-only exception bank has size `e` has q1 projection
at most

\[
                         (m-1)f+e.
\]

Consequently `O(m)` owner area and `O(m^2)` terminal/hidden area leave only
`O(1)` protected-turn casualties for `p=O(sqrt(m))`.  The exact unresolved
cap statement is a factor-independent, selection-stable typed deletion
summary with those two layer-area bounds, exported afresh at every lift.

On the factor side, the proposed generalized optional charging LP does not
close the last co-small cuts: total-mass equality forces it to be exactly
the fractional residual `b`-matching polytope, hence by integrality it is
equivalent to the desired two-factor extension.  This circular route is
discarded.  A wider forbidden q1 bank does give a genuine localization:
every optional gap has width at least `d-2`, and any positive minimal
optional obstruction is a three-supported near-clique bootstrap core with
size at least `3d-11` and induced Johnson minimum degree at least
`3(d-4)`.  The remaining noncircular factor target is to compress or rule
out this bootstrap core; a lex-min obstruction can persist only through an
explicit locked threshold-majorization inversion.

The most economical Hamilton-first ring surgery has also been closed
negatively.  Directly cutting a known Hamilton cycle at all ring roots and
ring owners and then rematching exposed endpoints works only when the cycle
already contains an entire ring phase.  Therefore the topology row cannot
be solved by one-layer endpoint matching.  It must use either additional
Boolean-diamond transport of external pairs or a genuinely joint
factor/ring selection.  This is a useful reduction: the apparent ordinary
Hall subproblem was illusory.

The bare `c=3` ring-topology row is now closed by a stronger construction.
The two ring phases are the two perfect matchings of one coherent incidence
hexagon, with the three unchanged lower-factor stubs sharing the same added
label.  Start from the rotational middle-levels factor and choose a standard
nonloop pull carrying this hexagon.  A fresh coordinate `q`, absent from the
fixed ring support, separates that pull from a transformed lollipop pull
spanning tree whose gluing vertices all contain `q`.  Replacing one edge on
the corresponding auxiliary-tree path by the ring pull gives a new spanning
tree.  Toggling every other tree pull leaves exactly two factor cycles and
preserves the old ring phase; toggling the ring hexagon then joins those two
cycles into one Hamilton cycle and installs the new ring phase.  This works
for every `m>=5`, costs no physical position, and is independently audited.

Thus the former six-open-hex component-hypertree problem is not load-bearing
for the three-ring.  Its exact complement calculation remains useful as a
boundary theorem: for the 18-edge bank the component--hex incidence
multigraph has cyclomatic number `13-c(F_0)`, so strictness is equivalent to
`c(F_0)=13`; arbitrary protected completions need not satisfy this.  The
single-pull construction bypasses the strictness requirement rather than
proving it.

This closes only bare owner/factor topology.  It does not yet place the same
Hamilton factor in one global state carrying residence, arbitrary-width
upper witnesses, the background lower compiler, the typed common cap, and a
regenerative export.  Those compatibility rows are still correlated with
factor selection.

After these refinements, the shortest honest additive-constant target has
two principal correlated rows, plus their simultaneous realization with the
now-explicit topology gadget:

1. rule out the localized optional bootstrap core, or construct the
   guarded residual factor directly while retaining the coherent ring pull;
2. retain the now-materialized q1 paths in one typed cap state with
   `O(m)` owner and `O(m^2)` terminal/hidden regenerative area.

Neither combined statement is currently proved, so the general
additive-constant conclusion is not claimed.

## 5. Frozen new dependencies

| result | SHA-256 |
|---|---|
| initial Chamber-I exact-clock/unique-stationary reduction | `adcbced9bf28374e1df96466552dbe70704c720d4af81c2212978efd8e86895d` |
| initial independent Chamber-I audit | `e41b4da738c00d1b105db5ee93b2d91746a76a8ee9854c2c02f6cbd68b617f28` |
| Chamber-II stationary-strip elimination and one-curve reduction | `f5dbde2a817c6ab23ade7de5c0f0d691d80db4d4bb23865f9643959efa79c91b` |
| independent Chamber-II audit | `3900b98672355272cf866659b4a5046f60b581604e18c91282e78e29d5f53d65` |
| corrected Chamber-I boundary/single-period scalar reduction | `4a80c1bdf2e23d5b495799d41b7b30755d6500df509078cc2ec7bfdc8a134af9` |
| independent corrected Chamber-I audit | `238adbe6df505b3fc991efcad228ff0e231bb91f6e864b7627efa369787d7679` |
| prethreshold two-variable half-period reduction | `c7479855908547c4d18ccc139d0df6880bb73905f93b7b9ba26683a841636286` |
| half-period monotonicity and repeated-gap closure | `c35a9db78b5dc317fa319dd150c3abe0521b3043b9dc22d7066b2d14ae2afd4a` |
| independent combined prethreshold audit | `1b42db42d688c57d375a04f1c2663764f6f624147614eb4392c5b7bda57dff87` |
| long-wrap Euclidean/theta reduction | `7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738` |
| independent long-wrap audit | `7dbb73b27234df23cc04bac16e1e9afaba15dac90bc03d40345087f69d9cf34a` |
| theta half-interval monotonicity and half-root anchors | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
| independent theta audit | `d54a01bc22960a1f7d9ec36cb7740f95cdd850d938589b5a9badcf27a3117b4e` |
| all-period monotone-quadrature long-wrap closure | `24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd` |
| independent all-period long-wrap audit | `ab249d01d769f42e9ca26cf17d4170397b021fe5d0714e3e20127d57a614a85b` |
| finite-shoulder critical-chain layer-cake reduction | `0e0df7a4d691bc6e73e0fba481fdeeceb43668f0fb8d1a69c02f7fc699cdc2e1` |
| independent finite-shoulder audit | `5152407757cfd64d4963591aba5139aed21ee0f000ba93ea4e9f0a95a631d637` |
| folded-C8/nested-terminal invariant and polarized socket | `a6dba7ab6eab0e14e47552ab52ce00a2962969a6168f08972946720c6224fe53` |
| independent polarized-socket audit | `731f7b7df0814aab3c686ad98dec8ffad7436d72fdda1c95db8adf895cb0ec5e` |
| multidefect prefix-minimum/reflected-ray-depth reduction | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| independent multidefect audit | `afcbe9eb2bf84c609e7654df49e8a90b6895f4e72fa9aea8b5b1be851a962f8d` |
| Chamber-II outer-period closure and compact KKT core | `c60b69aadd89815605be134162ade2c2355008ae9f34ee39d45bb3c5cef139b3` |
| independent outer-period audit | `4f230c0615122794d71e65523d4b55a8bbe9f2b6c63de66b9b6bed48c41bc4da` |
| complete Chamber-II residual incompatibility and closure | `52ec7f4ac4dbe9f0a32e5eed063cf5bf8419c535575a631b16d8c98d31e40a68` |
| independent complete Chamber-II audit | `fda3429412100f11be6491171ee7827c7ec56cc924a744bea0d1a2027b0f6cb0` |
| six-slot `h=4` redundant-endpoint/two-gate reduction | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| independent `h=4` two-gate audit | `f92d2d444c23cbc7366820d367935a9db5bbd304faafcd73e53f445963a5ee0e` |
| corrected `h=4` local-sign/relaxation-obstruction theorem | `badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af` |
| independent corrected `h=4` final-GO audit | `5781c83357c77dd8216ecbb24ab4739e779d0c65751c7f8aecce1ef43b6ae46c` |
| corrected literal-rectangle correlated `h=4` gate | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |
| independent literal-rectangle final-GO audit | `a23d9ac8fac44e26183e0b265599e084c4f5dc00202abf410cec47703fbd5e2f` |
| corrected `h=4` upper-band convexity/KKT pruning | `6f8daaba40de9d40c17d429fa4925d4d985d3374fa00d89a5d05651b2529aa11` |
| independent convexity/KKT final-GO audit | `41420c97aa68a7d7fc2f297a8e0c1b06056e5a9be8ea9f3d4b04e0df7909617a` |
| complete active-`Gamma` `h=4` positivity/boundary collapse | `3259e9c0c8a3f74839f5ed1cf73646395b8bebb17ea871d1d7e95e74360e2953` |
| independent active-`Gamma` final-GO audit | `3336f44dd086c09a4430c2d7c14c5f385d48a4bfc0ea1a74ad86cc5c40dfc872` |
| complete literal correlated six-slot inert `h=4` positivity | `34b4c57f4f917fed9dbed8c455f0b8bf279183dfdee8f66073ccd16b7dc6dfba` |
| independent complete `h=4` final-GO audit | `194fe89c87492da3eaad26be626bab9857b0ebd3053c42865d429c0297afd105` |
| `h=5` endpoint-defect polytope and correlated-gate reduction | `4a751598067165d88cd1e01e0406c3dce09c941cbba7fa0dd95487d0ff3e4b59` |
| independent `h=5` reduction final-GO audit | `1e4fe3bde5c60cb6263d9ff42616d06bd631e022c5472199d6328dfd1e0ec0a3` |
| `h=5` reflected-three-ray scalar-gate reduction | `2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef` |
| independent reflected-three-ray final-GO audit | `0659d01f929fc7f9524e3cfe1f8b4f16bf9b595c438a7ec253f27a965258b570` |
| `h=5` nested-ray large-`delta` closure | `34dfb968b14876fdd190183eef29723475ca2c6c537faac8b807c641dd4fba1a` |
| independent large-`delta` final-GO audit | `da8b93dc93ec9db2368b419d66de94f26d5019ee6c1073d3eeff861d302b2801` |
| complete canonical least-density `h=5` positivity | `59551dcca1dcd923e1d05fda17d7b491f2ff37f8a37ddd6ab8faf5dd0522854d` |
| independent complete `h=5` final-GO audit | `5c0cd324b2f1422dcfd0806dc72c3db7bf0624e9801290cc9de39e9199452fa5` |
| period-eight two-spike closure and canonical geometric compression | `76f1ced69d953d0ed0d6f1b4dd20566fcf5d6a657158c4b6de5b349e155e8e27` |
| independent period-eight audit | `ed3ba018742e88c7473fa8d8b7f0ea043912c0f5c8b1a09ebc4864700279c0fb` |
| period-eight functional-compression no-go | `4656324a6f1c016e1a4409241c58e5a4c751e52f4ce89361b7643939b4feeb21` |
| independent compression-no-go audit | `75dbaf2cacee209ad4c2438f1f561bef177f812585208eb460d5c76fbde58423` |
| complete period-eight `H=3` direct quarter closure | `93f40df626f7356ccb5dd890818fd9214f3db3f65cce9f649ca1db4270603815` |
| independent complete period-eight audit | `4ddd05cd74136a8016320e7dacb3aa611a4ae3c3ea687375f80ceeccec4a1de3` |
| complete period-nine `H=3`/all-clock closure | `65dddbe77a805cfa5b0308f3e555801234437a383ca18ce9bbb92d5ec5b716d7` |
| independent complete period-nine audit | `971520239060c755278f3d6c8b1d38d183ec13bf30958a74d77adbd54942cc8f` |
| terminal suffix maximum and quarter-cutoff lemma | `6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639` |
| independent terminal-suffix cross-audit | `1a1051b344ef9357f785871f4d6ee8d02712f9979a4244c8250faeeb6a4b79cd` |
| complete period-ten `H=3,4`/all-clock closure | `1697def0ed72f30c6972a706a968a3efed68e470ebe511b813c7eedc7259095e` |
| independent complete period-ten audit | `afc8590f5dbdaca0f34eff68a53bdae5f4ed97ee9882fc37ff458db53d0aa7e5` |
| complete period-eleven/twelve all-clock closure | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| independent period-eleven/twelve audit | `41d5d32a55907c6f3ba925b038944d52775e8011fee18d25957c00e8bb9b6169` |
| complete period-thirteen all-clock closure | `236a857ccddb8cc0490902f9afc909b047180fcd54cf355e2c3c88fb88e2fb9f` |
| independent period-thirteen cross-audit | `2749693bb04c21f2edb7846ec58d021f2fd091573fd0749844cbc8cc5699a011` |
| complete period-fourteen all-clock closure | `662ce674cd921d94567382033ff2f7a42eaf0e726dc8d8b990a32b7df6ebbe17` |
| independent period-fourteen cross-audit | `363b30d33cbd2767f0175bdb4fc08f0935bd3ee49fa2621127e506428dfe43a5` |
| complete period-fifteen-through-twenty closure | `876c12340cad4755c5c0e571525fdf48456fe1c31bc934894d9e451abf4f0e3b` |
| independent period-fifteen-through-twenty audit | `a99f4f69c05e099759f12eaf1a80e941d5de3ef6f13034b0ae0f3a831011f75e` |
| complete period-twenty-one far-ray closure | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| independent period-twenty-one audit | `27e1d896178b3648d4e24f4860dc3fdc51c7993f8990901e1bb536f795ac2650` |
| complete period-twenty-two nested far-ray closure | `455adc5d9558e6bebff177decac1df601a0e60f848aa58c81972f6b34d09e954` |
| independent period-twenty-two audit | `df03c3aabc1a100ea627193340f56b233165751451baf0d1ab028e04570efdb5` |
| complete period-twenty-three four/six-twenty-thirds closure | `2f8078d67c08ec37529351d57defe0e73a67779550dec31456806bcaa5c1c46f` |
| independent period-twenty-three final-GO audit | `b96be1598f7dad2d310f356c22de0dec8b232393a5629b0375686ee47ddf3e6f` |
| complete period-twenty-four threshold-ray closure | `0c3e35f6880f0903cbe44bfed543dcdc65be4f4dea8c8032b6b57b0a7713d5ec` |
| independent period-twenty-four final-GO audit | `0ae893a941184f22d51b93adec71b862ae06c7e6f9b4aed81a65138bb40c12e6` |
| complete period-twenty-five sharp-global-price/threshold closure | `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a` |
| independent period-twenty-five final-GO audit | `7cf04a46443f6e1e7eae815da0d29fc0580929a0b48874412f07fdf9e7e33d41` |
| period-twenty-six sharp-depth/two-residual-chamber reduction | `15777eb5978671af4ce685f9760fc1c2a1cef25e424cafe7deda8bc004cdee2f` |
| independent period-twenty-six reduction audit | `b3f554f184122e2011b88d2827bd3562424419d62956334e8e2183f524f4a5e5` |
| period-twenty-six residual middle-anchor/high-depth collapse | `b1f3c516683ba0453f62bf76ff7806dc773477adf32587c31c51c304a888fe77` |
| independent residual-collapse final-GO audit | `378c156d4caa7ebdf37817db262f4c5ff86f152ffb53f10ad646c70d7e7526ef` |
| complete period-twenty-six global-price closure | `97182d953e89773b6b2c193348ccf9ae3c94c8d7267ddd9731c1a7dd0168e229` |
| independent complete-period-twenty-six final-GO audit | `3aa280e5f20232a0d24071089ee147c46b9e2911be4c573968576f91d8ea3f92` |
| monotone anchor-grid reflected-ray ledger | `2f83517aee645bfacb1b50b8b462cbe0436b5055b0d4c3b5ead05ef598ab2f3f` |
| independent anchor-grid final-GO audit | `f6024388f84466025b39509cc4f59eba8f2ba19b29ccb614e19dc0b87b16c2f7` |
| finite-shoulder Pareto frontier and one-defect cocycle | `a15aff104c48a7e2fb095a06d00131489e2d9e5f0ea0940fc49d6127ab4b3def` |
| independent Pareto/cocycle audit | `3bc1edda09b9df58c5eeb88ecd2566d1fef7eb81c0babc6dff979da4fe9e0176` |
| typed suffix Haxell/LLL factor-router specialization | `2d3b24f7dc0ad85147593f3a6f65bebc95f28d5c1ad1c1179bf0257891fdd6f9` |
| independent typed-router audit | `cce8854fd2946d8305dae2006d3cba8e02f01df6c9bc79e25fe1d02db3f22e6b` |
| matched-port and bounded-multiplicity Boolean router | `732d2c8d4c4318a09dceb00435387df719b691aa3d81d9359887dba8af0e6524` |
| independent matched-port router audit | `a205c6a356e2b0f38e874a4e683e34301081523fdca4b3864aa1b0f5377dc099` |
| state-first Boolean-diamond prefix/suffix coinstantiation | `19611e47ec7c121e6869f27930c1cbd9b74ddc3cfadaba9a6b50588d99ea30d1` |
| symbolic state-first coinstantiation audit | `3883a0657b5b97cba7d6c1d2b36cec844d00d337cde0da90d03c4ae9f085f593` |
| fixed-factor static-diamond no-go and sparse-turn activation | `f190f4904a2c18a012e5dd3fd78eb97953b6ce9f8c68318452294f4961a1b794` |
| symbolic sparse-turn/no-go audit | `3862c20feb6f02a27e75badb8e85fd9985ec7236ece1353dbf4cc462c97e3074` |
| preselect-protect-complete Middle-Levels Boolean router | `13c3c3baea1e2e667f748ba49fafef297f49d6e8771d09043c96e823f8bb72bc` |
| independent preselect-complete audit | `f7c1625f7cb8dfa96ff6e3b01e94a6134d955583f0ce1023d81906b635caa7a4` |
| protected-factor occurrence lift, parity, and opening loss | `a455c5804840e7bf13f90b44b4076fa46339a9d8e2247bb192ed140cb7ccb262` |
| independent occurrence-lift cross-audit | `30818a6918c32d254d7b792e3345f2e5caf8770ba06cbdbabc56cae5e4338ac7` |
| Middle-Levels turn-diamond capacity router | `a7176faaf6cd44768df058423c4f492018fa0f6b256008dd0de80cf3ecf85ef7` |
| independent turn-diamond router audit | `0844c9498048e4eac72d95b8f0c7e8396cab4219a9c6dda07e782ed68d04ad56` |
| global-owner-disjoint multicoordinate preselection | `fab1d624778ddf687867fad2969d5821a3383dd38f8e6da7e5e26d571f4a69f9` |
| independent global-owner-disjoint cross-audit | `befd81026fbcc22ccd50757eab240ed991f683340c2555c1b871fe9b6edd2164` |
| protected turn-diamond wedge packing | `7727963a32eda4aad2b556ec0141dd02ca2c38e80daa563e97e36601cd3332fd` |
| independent wedge-packing audit | `4d7b9fbc8331d476c4cdf3acda6da214a0f4e7eb53950929685f842c536d6af4` |
| protected-wedge static-pull cut and host-lift reduction | `328bf5b1a280a1f926dac07afa478fa6469071b3fa8cb71788702ba17b483791` |
| independent protected-pull/host audit | `b9924dd7f890a60db20318665d73d2d84b3c0cd504c9315221b2bee2eba91f67` |
| protected-factor adaptive rank and bounded-component rescue | `f553f85672445da0fe3ef71c10557eaa72b3c96042b13fcca83c7be5dd6c2b1e` |
| independent adaptive-rank/component audit | `2dc2e5f125fda7bf28cf27445edd9e2840886bd3281fc9d6620363c8f5e927ec` |
| bounded-component completed-hinge/guarded-overlap theorem | `3b8087d7e2fd1bb219d536db0f8e184b10548571546a53171cf6d39455c8f8de` |
| independent completed-hinge/overlap audit | `0250df2335709dfce8f83c70137dc2fe489e6cfa2d5b0399d21a4962103a90ab` |
| turn-diamond common-history supply obstruction and exact regenerative state | `e763749d0d222bb6f9207670431365102ac29f1d832aa5904569f5452fc93c03` |
| independent common-history supply audit | `3446f4913eb260d327590f1a3b139e2cd52b2e9497d1c98959cfe0a57507d4be` |
| common-core cycle-transversal forest-complement reduction | `a9db5e4ad7d5697ba51e5e9042ccb7be4426df2161eaa5e8b3361f5d95369649` |
| independent forest-complement final-GO audit | `0877cf5e24cd3036e2b31dc3facc17f8e4cc646670b6ed3ecc916a0ec524afee` |
| rooted pull transversal, panchromatic core, and fixed-matching obstruction | `5cc02e3ce3fd07a2fd3d7656893a72ef4c4395076dafc19c0769c6834b30668a` |
| independent rooted-topology audit | `d666c54041deae7d7844e5fdd94abb7b0ea0b11cfd3d331a438763e3fbe11972` |
| cyclic common-history hinge ring and short-deck invariance | `96b9f8717c138dfac7df2a4d1c439392de1a3313c9e57114d2e1cd6f145b90ba` |
| independent cyclic-hinge-ring final-GO audit | `512abf6455d69859d1ca3ee6901fccaadefb743fcab7ddc9f00ded3954b08b02` |
| protected Ore weighted-boundary/cut-thinness theorem | `4bb0621bdac66579eefba12c8b270d6334c517468d7f0deba277943f0bfc8891` |
| common-core upper-damage reservoir and covariant full-size ring | `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983` |
| independent Ore/reservoir final-GO audit | `b0080792c16e9fe97afa31481b26181dbe41b6b1b035bdedfec3083a33b19d96` |
| hybrid clipped-resident common-core reservoir | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| independent hybrid-reservoir final-GO audit | `20095bf654c35ac973e72109bd5b57341a76bdb02d67f18001556fd26c96084b` |
| protected Ore near-shadow localization | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| independent near-shadow audit | `798c63035bb5984a883d72fd1c0825f4594b9b6f85e23db27c0ab3b8b0a2f2ee` |
| minimal reservoir/singleton and co-small Ore closure | `bfc9b6cc16c19e06ea8c455d688099e90fd8c80bd476b71fdbbbff1c1f91ae87` |
| independent minimal-reservoir final-GO audit | `85d363aa3bfd8a5c0c26f459d03d49fde88f8d8316a2dc883270f05139e436e2` |
| constant-spread, zero-defect, and principal-star closure | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| constrained-`G_2` complete equality-cut closure | `b07682e2aee1b5d3017e96fc1483b17a91be8d249673a2c4b49433610867eb5e` |
| independent spread/equality audit | `dd71ed0151e7463ffe45e570687cf8996dd7921d411d54899bb74a2e785370e6` |
| Johnson-component Ore reduction | `e8d77dc370839a0ee8fe3bb23d47aef6fa51059f65cae5d51dfb17c0b02bbd7c` |
| independent Johnson-component audit | `1921cf97fda2111a910ba32245bcb37fc64f2f2ff6cd532f3a81513323aa57ea` |
| factor-first trace-slice/Pascal connector reduction, with correction banner | `a05a53ab3a9344c09d471600f503f0aae44d1ddd6508b5cedd4caf983b106ebc` |
| independent factor-first final-GO audit | `46e7fead08de1eed0e3ab3c356131189dbebfd73c58b4458d04dc776b55c85dc` |
| forced square-flow/minimum-slice no-go and sharp raw repair | `1c2cf9c21bca7aa1690ad31da972281ca4cd8ee3c09f47c5a28a5e20fcd33d7d` |
| independent square-flow obstruction audit | `04f65f3e12b88e578bc240d15df9b92d681cc78d5d3e9ff2aa5a1b2ca25347f9` |
| positive-defect block gluing and sharp Hamming stability | `b414ed2dea6a3cc7365a054cbea7e664069ae5c9d84e1bdff1c80d79e6ae0980` |
| independent positive-defect audit | `d2d383b2e77c354fcbde593477a65d8ef3278ecdcf959656103a4dd08f3996b8` |
| exact two-sided-subcube Ore ledger and safe regions | `6499abf7abf9536bdfcf421206ad1e56d3b3f9d2ce05258b92cb8873ddb26dd7` |
| independent two-sided-ledger audit | `49e99350c2c3be085964d055b39ff792f8cc5607ae6dbe5ad7bae2d2c7e1daf7` |
| complete constant-spread closure of every two-sided subcube | `c1bcfa900291760974c167c2c02248c65291d28beaf3ef8e66c095a2301f4817` |
| independent all-subcube closure audit | `437e3b896009d3dae0c32876263a63e0735b7c4faee77a9733e074eadfa8ab02` |
| capped-shadow compression and partial-colex obstruction | `6e138117e2310bcc8087d3cc67cb07bd1702f0674b1ac1369298205b4fc1610f` |
| independent capped-shadow audit | `ba80e42b760b2cba69691a01cfcfaf2ed049125d5adbb47f577b8c800aae4335` |
| adjacent principal-star union protected-crossing closure | `33c60f18e4eded178218a0619b664948b9c8fca5ac67ce13778f2a44cd8014a7` |
| independent adjacent-star closure audit | `2e38962e20b4244d2d30e405b3427679e7b277d9c7c74aacdddbb84c5e8d0e31` |
| bounded/log-width DNF star-union Ore closure | `26dd7101b25bd4b1ddc6bd8daace1620cfb5805b0e58828b5180d1b70967e1e2` |
| independent bounded-DNF closure audit | `a667ea1b877394b6df3d880483f6a9e2f54b17bdc390459e7a2b4caf68c53843` |
| Macaulay interval/DNF erosion and exact triangular current | `77253694d02d6d11c41a21b9875af843ede525d1751bca7d2463ac014b174cec` |
| common-root Macaulay-run current and localized broad-run closure | `83db1a8e67e359025a03b0d704feb5aad81aaaae49a3e4f5339eb948edbfd189` |
| independent Macaulay/run audit | `8ebc6da6b34d322b3861383ea2c7adfb11ac741f0224d470687479d16ee09b12` |
| nested Macaulay multi-run current | `0e63df633f3d89879b05ec076cb0254a5ab74036b5b7ff10d97225f5d236d5de` |
| independent nested multi-run audit | `7b41b40716d088b9133382f3787ece4a0b145b4f3253d67d185e57b4a8e0dcc9` |
| complete localized initial-colex protected Ore theorem | `1c1ca29979c511534bfaf3adfa558be5ba9bfec5d6b93dcc33d6e44451e0c96a` |
| independent localized initial-colex audit | `d022b781dad4714b4f458e852d2345e2a4191a093e4835dd0068466f195e10c4` |
| residual-capacity DM uncrossing, co-small criterion, and shifted-mincut criterion | `fd528c5cb0fa2c50af611271ee3ef1f0bbbcc1849cee7226335ebb88c8dd2bf2` |
| factor-first canonical phase cover and fixed-host obstruction | `ae2a051514ca3cc8d16a17cdc8e5cb2a70468511f4148e65b4bd601dc8194079` |
| independent factor-first phase-cover audit | `6a869c0af338ef740f70fc9a5a3012ae83f843d0d5e7044b352a386f123d4e29` |
| cap-aware protected-wedge exact menu threshold | `ae4ce45555394121fcf1e7df7840c86a0786b840dedcf96ca414ef9d33c7f188` |
| independent cap-aware wedge audit | `2898dde385b6e2c637c40d3e71d9583e1219aeb0e27147ab83c02fc936f6aa2b` |
| near-full owner-gammoid protected-wedge bypass | `4962e57f888848a40bc9b1f6cb8cb871d95bc2f1d777858a609ef9aebe93aadd` |
| independent near-full owner-gammoid audit | `d5800be4e1bcb33a81e7148200dccb7c8a4985ea7392213500cb7617e79b1c65` |
| independent residual-capacity DM V3 audit | `fcabf7fe45956613be6c911c8828eb5312885a605b323db8e950a24e05c3e835` |
| co-small forced-q1 harmonic-gap certificate | `4a5d0993d7c3e2eb54198c2b6278670649308f7aeb3dd1de046b18742db0a85a` |
| co-small base-safe q1 forbiddance | `c17615960cf7a9ff551125d72b69849b97181b41e1cd234d8a3b58820d7faf7a` |
| independent co-small base-safe audit | `73c9e0a00f4cb1a7c0e02a82a5b36b520548c06d40fc74e859275a66d78f1bd6` |
| paired-turn deletion and minimal occurrence lift | `b1852de086db9846d6f4748e7200fe4757d31036e5a50673a68dac78d6262110` |
| independent paired-turn deletion audit | `9989d2833e91f76c0933466354c5f7177c658d8fd7d4d645415838b16e5c03c4` |
| endpoint-only active-wedge margin | `1c443748c354042951c485cf52289b7db5bf349c3b75151ef73b8978d1e13093` |
| independent endpoint-only active-wedge audit | `438e25846ceb31e399fc1d12199b64c37d676919bed36b62a1dd69cddd5500e6` |
| bounded-turn-star one-step full-port linkage | `5899c6f8f40504d58ffa96e94d17a100e4d77fc59fa0a4363489c1528e9392f3` |
| independent bounded-turn-star linkage audit | `fa73a030031928a470852ac662efd296820dbd4ac0a5464e525d9a4b166ed15b` |
| rank-layer crossing cap damage and wedge activation | `46eae57429e3f2939b2032b3fe44783e3a5643af6c53eb7faf53d4fd89fd33eb` |
| independent rank-layer crossing audit | `18776b12cba5c870bc4e03afa4822b249efbf6db4aba019ce2f3cab70e7ed533` |
| linear layer footprint gives bounded wedge defect | `242c752d5344a00658d821f2e0b0b0210e0a3dc3d923903be1a96a2bba1fcd16` |
| independent linear-footprint audit | `d8c8e4691e9e43901725c7ee49a5700057a5827c8eaf30000035090a3448f379` |
| two-layer footprint gives bounded wedge defect | `42b522abb25158fe06ca54a60b10ad6b3a9b7028e55e640c595d4f385b5befe8` |
| independent two-layer footprint audit | `bcaf3bd8a10c0f839fed2d8448e9b9cd52dbe7d88979492bfceab1da7502982b` |

## 6. Latest concentrated three-ring/cap frontier

The bare topology and local upper-loss rows are now closed.  A coherent
three-ring is one standard pull, and a graphic-basis exchange makes it the
last switch from exactly two factor components to one Hamilton component at
zero position cost.  Independently, a clipped-resident reservoir protects
the ring's complete upper-damage cone.  Once this bank is jointly planted in
an already upper-complete carrier, the switch preserves every upper target
without a witness-width restriction.

The actual `Ibc/Ica` pair also has a complete literal local model.  Both
phases admit exact nonempty antecedents, all `d-1` aligned birail ray
pairs occur at explicit distinct addresses, and each ticket has its own
native owner--q1 socket.  Identical ordinary palette service and already
charged bundle service on one address/value/state fact coalesce with unit
load; the remaining bundle footprint must still be deleted in the residual
occurrence bank if that separate router remains active.

Serial safety removes the opposite phase and passive terminal typing from
the weakest **final** compiler theorem.  One terminal phase contains
`2(d-1)` distinct aligned ray targets at `2(d-1)` distinct addresses,
so those facts form a literal forced matching.  The ideal `(d+1)`-slot
containment theorem extends these pins for all sufficiently large `k`.
The maximal-envelope halo theorem now upgrades the local phase antecedent
to a global pinned inverse whenever the complete affected-owner halo is
planted inside a resident flat Johnson carrier.

There is a further exact collapse.  In one fixed literal word every interval
address has one OR value, so its occurrence graph has right degree at most
one.  Forced ray addresses have their forced values and cannot be neighbours
of residual targets.  Therefore forced-edge contraction has zero surcharge,
and terminal Hall is exactly lower-deck coverage.  If `sigma` is the scalar
short-cell slack, the missing-target count is

\[
 M_A^\Pi=D_A^\Pi+Q_A^\Pi+R_A^\Pi-\sigma,
\]

where `D` counts duplicate residual values, `Q` counts extra occurrences of
already forced values, and `R` counts rank-middle short cells.  Thus the
remaining lower gate is neither target count, ideal Hall, guard-pruned Hall,
nor polarized type.  It is one-copy physical chainization extending the pins
with literal waste at most `sigma+O(1)`.  Native sockets remain load-bearing
only if a separate compensation/router or regenerative continuation uses
them.

On the factor side, a surviving optional obstruction is much larger than
the former quadratic bouquet estimate.  A coordinate-section induction
for adjacent Boolean layers, followed by asymmetric density peeling,
forces the sharper bound

\[
 |B^-|\ge \binom{d-2}{\lfloor(d-2)/2\rfloor}
          =\Theta\!\left({2^{d-2}\over\sqrt d}\right)
          =2^{\Omega(\sqrt m)}.
\]

This does not exclude the core.  It says that any counterexample to
protected factor extension is a genuinely mesoscopic Boolean object, not a
localized affine-plane-size defect.  The still sharper
`binom(2D-1,D-1)` threshold would require minimum degree `D` on both
shores; the present hypotheses give only average degree on the lower shore.

For a fixed pairwise-disjoint pull system, joint planting has an exact
criterion.  The protected bank forces a unique pull phase `A_D`; with the
ring pull `g` last, extension exists precisely when

\[
 A_D\cup\{g\}\text{ is a graphic forest}
 \quad\text{and}\quad
 (H-B_D)/(A_D\cup\{g\})\text{ is connected}.
\]

Synchronous conjugation cannot make this automatic: even all cyclic
rotations miss some legal ring wedge from `m>=17`.  The reservoir and
ring must therefore be selected jointly inside the pull phase union, or the
move system must be enlarged.

There is now a conditional but strict simplification of the second pull
condition.  Pin one core coordinate `q` in every physical vertex of the
complete ring-damage reservoir.  Complementing the distinguished
fixed-boundary pull tree puts every one of its completing circuits in the
opposite `q=0` half.  Hence, inside one explicitly compatible
pairwise-support-disjoint host, any accessible phase-consistent protected
bank for which `A_D union {g}` is a graphic forest extends to a last-ring
Hamilton completion automatically.  The residual **physical** cographic
cut is then free.  This does not construct the compatible host, preserve a
typed/global occurrence order, or repair the short `q`-runs created by
pinning; accessibility, graphic independence, and global residence remain.

The regenerative quantifier can also be weakened.  One auxiliary parent
certificate may be copied into independent children: one continuation
child and separate odd/even terminal-readout children.  Therefore the
terminal packet phase, its `Theta(d)` ray facts, its antecedent, and its
literal-waste certificate need not be exported to the next dimension.  In
fact, for each requested horizon it is enough to have a finite continuation
path whose **leaf** has a uniformly bounded readout charge; paths for
different horizons may diverge, and terminalizing a leaf may destroy every
continuation interface.  This is reuse of an existence certificate, not
simultaneous resource duplication.  If the recursion consumes a fixed
literal parent interior rather than an existential boundary class, a
rematerialization or left-totality theorem is still required.

The shortest honest additive-constant target is consequently a forked
one-phase regenerative extension:

1. construct arbitrarily long continuation paths in a complete auxiliary
   state, or one left-total continuation class, without requiring any
   intermediate state to be terminally compilable;
2. at each requested terminal horizon, independently choose an initially
   upper-complete globally resident leaf carrier, coherent ring, pinned
   protected reservoir, and actual `Ibc/Ica` packet;
3. satisfy accessibility and graphic independence in one compatible pull
   host (the coordinate wall then supplies physical cographic completion);
4. choose one terminal phase and construct one global nonempty antecedent
   extending its forced rays with

   \[
      D_A^\Pi+Q_A^\Pi+R_A^\Pi\le\sigma+C;
   \]

   if a separate physical router retains native bundles, additionally
   price its noncoalescible footprint; and
5. obtain both odd and even terminal leaves with one uniform constant `C`.

Separate existence of the ingredients does not imply either fork.
In particular, clipped residence is not global residence, the halo theorem
requires an unclipped compatible owner boundary, fractional rotor balance
does not control one-copy literal waste, the reservoir preserves upper
completeness rather than creating it, and existential boundary cloning
does not justify replacing a fixed parent interior.  The general
`B(k)+O(1)` theorem remains open at the literal-waste terminal leaf and the
continuation/host-extension rows.
