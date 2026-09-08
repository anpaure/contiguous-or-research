# PBBS connector coboundaries, residence, and the simultaneous hypersimplex lift

Date: 2026-07-28

Status: unconditional local connector and owner-extension theorems, followed by
an exact statement of the remaining global gate.  No PBBS Hamiltonization,
short-residence little-oh estimate, or simultaneous chronology lift is claimed.

## 0. Verdict and scope

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\operatorname {Cat}_m=\frac{W}{2m+1}.
\]

The PBBS odd-graph factor already supplies every canonical descending flag at
every depth.  Its at most `B` projected cycles may be opened and given
depth-`H` collars at cost at most `2HB=o(W)` when `H=O(\sqrt m)`.  Thus pure
Hamiltonization is not an asymptotic gate.

What a useful connector must do is more stringent.  It must either hit the
short-residence witnesses which contribute to the transversal
`nu_H(P_m)`, or realize a common exact owner extension.  Theorems 2.1 and
3.2 below give the exact all-depth flag and residence ledgers for the natural
complement-paired hexagon connector.  Theorem 4.1 shows that exact upper
ownership rules out every nontrivial two-arc switch.  Theorem 6.1 gives an
exact interval-union characterization of trace-two residual extension, and
Proposition 6.3 shows why raw normalized matching is insufficient.

The new hypersimplex theorem removes the last purely rankwise obstruction:
all separately prescribed lower rows can be made hole-free whenever the
coordinate bounds hold.  The exact remaining finite gate is therefore a
**simultaneous hypersimplex lift**: one chronology must realize compatible
rankwise exchanges at all depths, preserve residence and the upper flag
tower, and construct one trace-two skeleton whose eligible interval unions
catalogue all residual targets.  This theorem is unproved.

## 1. Authoritative PBBS inputs and the topology/residence separation

Let `f` be the canonical PBBS successor permutation on the `m`-sets of
`[n]`, and put `g=f^2`.  If

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q
 \tag{1.1}
\]

is a directed `q`-edge `g`-path, call its intersection a correct depth-`q`
flag when it has rank `m-q`.

### Theorem 1.1 (audited complete PBBS flag tower)

For every `1<=q<=m` and every

\[
 S\in\binom{[n]}{m-q},
\]

there is a directed path (1.1) with

\[
 \bigcap_{h=0}^{q}B_h=S.
\]

The number of such canonical PBBS occurrences lies in

\[
 1\le \mu_q(S)\le\binom{2q+1}{q}.
 \tag{1.2}
\]

This is the global-maximum-corridor theorem of Section 21 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, with the load audit in
`MATH_AUDIT_PBBS_ALLQ_CORRIDOR_AND_FIXED_BAND_WORDS_20260726.md`.
Complementing the states identifies this tower with the descending odd-graph
flags in Section 2.6 of
`MATH_K15_COMPLEMENT_ANTIPODAL_MIDDLE_LEVELS_REDUCTION_20260728.md`.

### Theorem 1.2 (audited component and residence ledger)

The projected PBBS factor has at most `B` cycles.  For every `H<m`, the
dominance-staircase construction gives

\[
 L_H\le W+2HB+2(5H-1)\nu_H(P_m),
 \tag{1.3}
\]

where `nu_H(P_m)` is the maximum number of projected-edge-disjoint positive
coordinate residence intervals of length at most `H`.

In particular, for `H=O(\sqrt m)`,

\[
 2HB=O(W/\sqrt m)=o(W).
 \tag{1.4}
\]

Consequently component topology is cheap.  The coefficient-one PBBS gate is
the strict improvement

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)
 =o_A(B\sqrt m)
 \tag{1.5}
\]

for every fixed `A`, or another residence-sharing statement which makes the
last term of (1.3) `o(W)`.  Merely joining cycles does not imply (1.5), since
every untouched internal short-return witness persists.

## 2. The complement-paired hexagon and its exact flag coboundary

Recall the natural paired matchings at the upper vertex
`U_Z=[n] setminus Z`:

\[
 M_0(U_Z)=f^{-1}(Z),\qquad M_1(U_Z)=f(Z).
 \tag{2.0}
\]

Call distinct `m`-sets `t_0,t_1,t_2` a **legal directed star triangle**
when they have a common `(m-1)`-set core and, cyclically,

\[
 f(t_i)\cap t_{i+1}=\varnothing,
 \qquad t_{i+1}\notin\{t_i,f^2(t_i)\}.
\]

These are exactly the incidence and non-fixed-edge conditions for moving
the old `M_1` endpoint `f(t_i)` to the upper slot `U_(t_(i+1))`.  Put

\[
 \tau=(t_0\ t_1\ t_2).
\]

The one-sided alternating Middle Levels hexagon and its complement are
disjoint for `m>=2`: the three star centres have a common nonempty core,
whereas their PBBS predecessors and successors avoid that core.  Hence a
one-sided switch destroys complement antipodality.  Switching the hexagon
and its complement is exactly the odd-graph successor switch

\[
 g_*=f\circ\tau^{-1}.
 \tag{2.1}
\]

Indeed, after the directed hexagon switch the new `M_1` endpoint at
`U_(t_i)` is `f(t_(i-1))=g_*(t_i)`, while all other `M_1` slots are
unchanged.  The complementary switch changes the opposite matching from
`f^{-1}` to

\[
 g_*^{-1}=\tau\circ f^{-1}.
\]

Thus the two toggles are precisely the natural paired matchings encoded by
`g_*`.

If the `t_i` lie in three distinct `f`-cycles, (2.1) merges them into one.
Indeed, open the old cycle immediately after each `t_i` and write the
resulting directed segments as

\[
 S_i=(f(t_i),f^2(t_i),\ldots,t_i),\qquad |S_i|=L_i.
 \tag{2.2}
\]

The new cycle replaces the three old boundaries `S_i|S_i` by the three
boundaries `S_i|S_(i-1)`.

For any successor permutation `h` and `1<=ell<=m+1`, let
`mathcal F_ell(h)` be the multiset of intersections of `ell` consecutive
vertices on every orbit of `h^2`.  The physical paired monodromy may instead
be written `h^(-2)`; reversal of every orbit leaves this intersection
multiset unchanged.  For
`delta in {0,1}` and `a,b>=1`, define

\[
 L_{i,\delta}^{(a)}
 =\bigcap_{h=0}^{a-1}S_i[L_i-2+\delta-2h],
 \qquad
 R_{i,\delta}^{(b)}
 =\bigcap_{h=0}^{b-1}S_i[\delta+2h],
 \tag{2.3}
\]

with indices read in the directed segment.

### Theorem 2.1 (exact all-depth paired-connector coboundary)

Assume that `t_0,t_1,t_2` lie in three distinct `f`-cycles.  Then, for every
`1<=ell<=m+1`,

\[
\boxed{
 \mathcal F_\ell(g_*)-\mathcal F_\ell(f)
 =\sum_{i=0}^{2}\sum_{\delta=0}^{1}
   \sum_{a=1}^{\ell-1}
 \left(
 [L_{i,\delta}^{(a)}\cap R_{i-1,\delta}^{(\ell-a)}]
 -[L_{i,\delta}^{(a)}\cap R_{i,\delta}^{(\ell-a)}]
 \right).}
 \tag{2.4}
\]

#### Proof

Every PBBS `f`-cycle has length at least `2m+1`.  Hence an `ell`-vertex
step-two window with `ell<=m+1` crosses at most one of the three opened
boundaries.  A window crossing no boundary is literally unchanged.  A
crossing window is determined uniquely by

* the segment `S_i` containing its left part;
* its parity `delta` in the original `f`-cycle; and
* the number `a` of its `ell` vertices on the left of the boundary.

Before the switch its intersection is
`L_(i,delta)^(a) intersection R_(i,delta)^(ell-a)`; after the switch it is
`L_(i,delta)^(a) intersection R_(i-1,delta)^(ell-a)`.  Summing the signed
records over the unique triples `(i,delta,a)` proves (2.4).  \(\square\)

If `r_ell(S)` and `n_ell(S)` count the negative and positive occurrences of
a target `S` on the right-hand side of (2.4), then the post-switch load is

\[
 \mu'_\ell(S)=\mu_\ell(S)-r_\ell(S)+n_\ell(S).
 \tag{2.5}
\]

Here `mu_ell` is `mu_(ell-1)` in the edge-depth convention of Theorem 1.1.

Thus complete support through depth `H` is preserved **if and only if**

\[
 \mu_\ell(S)-r_\ell(S)+n_\ell(S)\ge1
 \tag{2.6}
\]

for every `ell<=H+1` and every target of the canonical rank.  Formula (2.6),
not a marginal balance equation, is the exact simultaneous flag condition.
At length `ell`, (2.4) contains `6(ell-1)` removed records and the same
number of inserted records, counted with multiplicity.

For a sequence of connectors, the analogue of (2.5) telescopes exactly in
time.  Collar separation is not needed for that identity.  It is needed only
when one wants to evaluate every connector from its original local context
rather than from the current factor.

### Corollary 2.2 (run-spectrum obstruction to shallow certification)

For a coordinate `x`, let `d_ell(x)` be the number of `ell`-vertex flags
containing `x`.  Let `C_x` be the total length of those step-two cycles on
which `x` is present at every vertex, and let `R` range over all other
cyclic `x`-runs.  Then

\[
 d_\ell(x)=C_x+\sum_R(|R|-\ell+1)_+,
 \tag{2.7}
\]

and therefore

\[
 d_\ell(x)-2d_{\ell+1}(x)+d_{\ell+2}(x)
 =\#\{R:|R|=\ell\}.
 \tag{2.8}
\]

#### Proof

A non-full run of length `r` contains exactly `(r-ell+1)_+` consecutive
`ell`-windows, while an all-`x` cycle contributes its full length for every
allowed `ell`.  Summing gives (2.7).  The constant `C_x` has zero second
difference, and the second finite difference of `(r-ell+1)_+` is one at
`ell=r` and zero elsewhere, proving (2.8).
\(\square\)

Hence point-degree neutrality at one or two depths cannot certify the full
flag tower: the whole tower contains each coordinate's non-full run-length
spectrum (and its all-cycle contribution).

## 3. Exact residence under surgery

Let a directed Johnson word satisfy

\[
 B_{t+1}=B_t-\{d_t\}+\{e_t\}.
 \tag{3.1}
\]

### Lemma 3.1 (deletion-word identity)

For every `ell>=1`,

\[
 \bigcap_{h=0}^{\ell-1}B_{i+h}
 =B_i\setminus\{d_i,d_{i+1},\ldots,d_{i+\ell-2}\}.
 \tag{3.2}
\]

It has canonical rank `m-ell+1` if and only if the displayed deletions are
distinct elements of `B_i`; equivalently,

\[
 e_s\ne d_t
 \qquad(i\le s<t\le i+\ell-2).
 \tag{3.3}
\]

#### Proof

An element of `B_i` lies in every state in the window exactly when it is
never deleted during the window; an element outside `B_i` cannot belong to
the full intersection.  This proves (3.2).  The right-hand side loses
exactly `ell-1` elements precisely under the first condition.  A repeated or
noninitial deletion can occur precisely after that label has been inserted
inside the window, which is exactly the forbidden equality in (3.3).
\(\square\)

With the interleaving

\[
 z_{2t}=e_t,\qquad z_{2t+1}=d_{t+1},
 \tag{3.4}
\]

condition (3.3) is equality avoidance at odd distances with an even start.
Depth-`D` residence is therefore exactly

\[
 z_{2i}\ne z_{2i+2t-1}
 \qquad(1\le t\le D).
 \tag{3.5}
\]

For a general Johnson word this does **not** include the odd-start
comparisons.  In the special odd-length cyclic odd-graph quotient,
multiplication by two permutes the index set and converts (3.5) to the
all-start formulation; that extra reindexing is unavailable here.

### Theorem 3.2 (seam tests and the hitting necessity)

Suppose the retained oriented segments have at least `D` transitions on
each side of one new projected Johnson seam.  The number of
insertion/deletion equalities in (3.3) whose interval crosses the seam and
whose transition distance is at most `D` is

\[
 \sum_{t=1}^{D}(t+1)=\frac{D(D+3)}2.
 \tag{3.6}
\]

Consequently a one-sided three-seam hexagon creates at most
`3D(D+3)/2` new residence tests, while the complement-paired six-seam
connector creates at most

\[
 3D(D+3)
 \tag{3.7}
\]

such tests.

Moreover, every old bad short-return interval lying wholly inside a retained
segment remains bad after the connector.  Thus any surgery producing a
depth-`D` resident factor must cut or modify every old bad witness.  Conversely,
if every retained segment is internally depth-`D` resident and every
cross-seam test (3.5) passes, the rethreaded word is depth-`D` resident.

#### Proof

For a fixed transition distance `t`, there are exactly `t+1` placements of
an ordered insertion/deletion pair with one index on each side of the chosen
seam, in the convention where an endpoint test may use the seam transition.
Summing over `1<=t<=D` gives (3.6).  A retained internal subword has exactly
the same labels, order, and orientation before and after surgery, so each old internal
equality persists.  Finally every residence test is either internal to one
retained segment or crosses a new seam.  The stated two hypotheses cover
these exhaustive cases.  \(\square\)

The last paragraph is the precise reason topology alone is irrelevant to
(1.5): a pure merge need not hit even one short-return witness.

### Proposition 3.3 (legal Johnson-spoke `ell=2` safety does not propagate)

There is a legal local Johnson spoke for which both old and new
two-vertex intersections have canonical rank, but the new three-vertex
intersection does not.  No embedding of this spoke into a PBBS star
connector is asserted.

#### Proof

Take

\[
 R=\{r,s\},\quad c_0=a,\quad c_1=b,\quad\delta_0=r,
\]

and

\[
 Q_0=\{s,a,b\},\quad P_0=\{r,s,a\},\quad
 P_1=\{r,s,b\},\quad L=\{s,b,x\}.
\]

The old word is

\[
 L\xrightarrow{-x,+a}Q_0\xrightarrow{-b,+r}P_0,
\]

and its triple intersection is `{s}`.  The switched spoke is

\[
 Q_0\xrightarrow{-a,+r}P_1.
\]

Both `Q_0 intersection P_0={s,a}` and
`Q_0 intersection P_1={s,b}` have canonical rank two, but

\[
 L\cap Q_0\cap P_1=\{s,b\}
\]

has rank two instead of rank one.  The inserted `a` has been immediately
deleted.  \(\square\)

Thus no `q=2` connector audit can replace the full chronological collar
conditions.

## 4. Exact upper-owner obstruction and connector arity

In the projected paired factor, a Johnson edge `x--y` between `m`-sets has
upper owner colour

\[
 U=x\cup y\in\binom{[n]}{m+1}.
\]

The PBBS upper depth-one owner colours occur exactly once.

### Theorem 4.1 (no exact-owner-preserving two-arc switch)

Let `x->y` and `x'->y'` be two distinct, vertex-disjoint cut arcs with
distinct old owner colours

\[
 U=x\cup y,\qquad V=x'\cup y'.
\]

The nontrivial head swap

\[
 x\to y',\qquad x'\to y
\]

cannot preserve the owner-colour multiset `{U,V}`.

#### Proof

Suppose first that

\[
 x\cup y'=U,\qquad x'\cup y=V.
\]

Then both `y` and `y'` are `m`-subsets of `U intersection V`: each belongs
to one old union and one new union.  Since distinct `(m+1)`-sets have
intersection of size at most `m`, this forces

\[
 y=y'=U\cap V,
\]

contrary to vertex-disjointness.  In the only other matching of the two new
colours,

\[
 x\cup y'=V,\qquad x'\cup y=U,
\]

the same argument puts both `x` and `x'` in `U intersection V` and forces
`x=x'`, again a contradiction.  \(\square\)

Therefore an independently exact-owner-preserving loopless successor
connector of head-swap type has arity at least three.  Indeed, if two cut
arcs are adjacent, their head swap creates a loop; hence every legal
nontrivial two-arc swap has the four distinct endpoints required by Theorem
4.1.  The alternating hexagon has exactly this minimum arity and
preserves its three upper depth-one colours.  This is an exact finite-owner
statement; it is not a lower bound on the asymptotic cost of opening PBBS
components.

For completeness, the paired switch (2.1) is also parity-limited.  A
3-cycle `tau` is even, so `f` and `f\circ\tau^{-1}` have the same sign.
Since

\[
 \operatorname {sgn}(f)=(-1)^{W-c(f)},
\]

the parity of the number `c(f)` of odd-graph cycles is invariant under all
such paired switches.  If `c(f)` is even, these switches alone cannot make
one odd-graph cycle.  Again this obstructs a particular Hamiltonization
architecture, not coefficient one.

## 5. Conditional residence-improving connector theorem

The preceding identities combine without any hidden marginal assumption.

### Theorem 5.1 (exact conditional PBBS connector criterion)

Fix `1<=H<m`.  Start from the PBBS successor `h_0=f`.  At stage `j`, choose a
legal directed star triangle in three distinct current `h_(j-1)`-cycles,
open three segments of length at least `2H+1`, and perform the
complement-paired switch to obtain `h_j`.  Preserve the order and orientation
of every retained segment.  Let `r_(j,ell)(S)` and `n_(j,ell)(S)` be the
removed and inserted multiplicities in the current-context instance of
(2.4).  Assume:

1. every initial bad residence witness of span at most `H` contains a
   transition replaced at some stage;
2. at every stage, every new or subsequently modified seam is rechecked and
   passes all even-start odd-distance tests (3.5) through depth `H`;
3. for every flag length `ell<=H+1` and target `S`,

   \[
    \mu_{0,\ell}(S)-\sum_j r_{j,\ell}(S)
       +\sum_j n_{j,\ell}(S)\ge1;
    \tag{5.1}
   \]
4. the resulting nested owner intervals admit the common owner assignment
   characterized in Theorem 6.1 below.

Then the resulting factor is depth-`H` resident, has complete lower and
upper flag support through depth `H`, and has an exact common owner
extension.

#### Proof

Conditions 1 and 2 imply residence by Theorem 3.2.  Condition 3 and the
telescoped signed multiset identity (2.5) give complete lower support.
Complement equivariance transports the descending lower flags to the
complementary upper union tower.  Condition 4 supplies one owner assignment
for all protected intervals.  \(\square\)

Theorem 5.1 is deliberately conditional.  Neither a connector family
meeting Conditions 1--4 nor the little-oh estimate (1.5) is proved here.

## 6. Trace-two residual extension is a controller-state interval-union problem

The exact finite owner gate can be stated independently of PBBS.

Let `Omega` be a finite ground set and `P` a finite set of chronology
positions.  Each `p in P` has an envelope `E_p subseteq Omega`.  There is a
family `F` of fixed owner labels, each with a prescribed active interval
`I_F subseteq P`; a family `P_0` of already fixed protected pairs `(L,J_L)`
whose union must equal `L`; a set `R` of pairwise distinct residual subset
targets; and a set
`C` of unused cells with intervals `I_c subseteq P`.  Base eligibility is a
bipartite relation `B subseteq R times C`.  An extension is an injective assignment
`phi:R->C` using `B`.  Its actual pointwise owner meet is

\[
 A_p(\phi)=E_p
 \cap\bigcap_{F:p\in I_F}F
 \cap\bigcap_{S:p\in I_{\phi(S)}}S.
 \tag{6.1}
\]

The protected-label requirement is

\[
 A_p(\phi)\ne\varnothing\quad(p\in P),
 \qquad
 \bigcup_{p\in J_L}A_p(\phi)=L\quad((L,J_L)\in P_0),
 \qquad
 \bigcup_{p\in I_{\phi(S)}}A_p(\phi)=S\quad(S\in R).
 \tag{6.2}
\]

Equation (6.2) is exactly the private-hit condition: every point of a
protected label must survive in at least one cell of its interval.  The
fixed protected pairs include the central middle-window equalities; they
need not themselves be active owners.

Call such an extension **trace two** when, at every position `p`, its meet
`A_p(phi)` is already generated, in addition to the envelope `E_p`, by at
most two owner labels active at `p`.

A **trace-two controller skeleton** is a family `alpha=(alpha_p)` in which
`alpha_p` contains at most two prospective owner labels and

\[
 Q_p=E_p\cap\bigcap_{L\in\alpha_p}L.
 \tag{6.3}
\]

For a residual label `S`, put

\[
 P_\alpha(S)=\{p:S\in\alpha_p\}.
\]

Call `alpha` admissible when `Q_p` is nonempty,

\[
 F\in\alpha_p\Longrightarrow p\in I_F,
 \tag{6.3a}
\]

every `Q_p` is contained in every fixed owner `F` with `p in I_F`, and every
equality indexed by `P_0` in (6.2) holds with `Q_p` in place of `A_p`.

For an admissible skeleton and cell `c`, define its skeleton word union

\[
 U_\alpha(c)=\bigcup_{p\in I_c}Q_p.
 \tag{6.4}
\]

Call `c` an eligible realization of `S` when

\[
 (S,c)\in B,\qquad P_\alpha(S)\subseteq I_c,
 \qquad U_\alpha(c)=S.
 \tag{6.5}
\]

The equality automatically implies `Q_p subseteq S` for every `p in I_c`.

### Theorem 6.1 (exact controller-skeleton union-catalogue characterization)

There is a trace-two residual extension satisfying (6.1)--(6.2) if and only
if there is an admissible controller skeleton `alpha` such that

\[
 \text{for every }S\in R\text{ there is a cell }c\in C
 \text{ satisfying (6.5).}
 \tag{6.6}
\]

#### Proof

Suppose first that a trace-two extension exists.  At each position choose at
most two active owner labels whose intersection with `E_p` equals the actual
meet `A_p`; this is the trace-two hypothesis.  Use them as `alpha_p`.  Then
`Q_p=A_p`, so admissibility holds.  For the assigned cell `c=phi(S)`, the
protected equality in (6.2) gives `U_alpha(c)=S`, and activity of every
chosen controller gives `P_alpha(S) subseteq I_c`.  Thus (6.6) follows.

Conversely, choose for each `S` one eligible realizing cell `c_S`.  These
cells are automatically distinct: if `c_S=c_T`, then

\[
 S=U_\alpha(c_S)=U_\alpha(c_T)=T,
\]

and the residual targets are pairwise distinct.  Hence `phi(S)=c_S` is an
injection.  The footprint condition makes every residual controller active
on its assigned interval.  Every active owner contains `Q_p` by
admissibility and `U_alpha(c_S)=S`, while the controllers defining `Q_p` are
among the active owners.  Therefore the intersection of **all** active
owners in (6.1) is exactly `Q_p`.  The protected equalities follow from
admissibility and `U_alpha(c_S)=S`, so `phi` is the required extension.
\(\square\)

### Corollary 6.2 (the apparent Hall graph has right degree at most one)

Define the pre-sharpening graph `G_alpha` by joining `S` to `c` when

\[
 (S,c)\in B,\qquad P_\alpha(S)\subseteq I_c,
 \qquad Q_p\subseteq S\ (p\in I_c),
 \qquad S\subseteq U_\alpha(c).
\]

Then every edge forces

\[
 S=U_\alpha(c).
 \tag{6.7}
\]

Consequently `deg_(G_alpha)(c)<=1` for every cell `c`, and Hall's inequalities
are equivalent merely to `deg_(G_alpha)(S)>=1` for every target `S`.

#### Proof

The pointwise containments give `U_alpha(c) subseteq S`, while the final
containment gives the reverse inclusion.  Thus (6.7) holds.  Distinctness of
the residual subset targets gives right degree at most one.  Neighbourhoods
of distinct targets are therefore disjoint, so all Hall inequalities follow
from the singleton inequalities, and the converse is immediate.  \(\square\)

The quantifier "there is an admissible skeleton" is essential.  Once a
skeleton is fixed, no cross-target matching competition remains.  The whole
residual problem is whether its eligible interval unions catalogue every
target while respecting controller footprints and the central protected
unions.

If repeated labelled copies of the same subset `X` are treated as distinct
residual demands, the graph instead decomposes into independent fibres

\[
 R_X=\{S:\operatorname{value}(S)=X\}
 \quad\longleftrightarrow\quad
 C_X^\alpha=\{c:U_\alpha(c)=X\}.
\]

Exact feasibility is Hall separately inside each such fibre.  If the copies
have identical base eligibility and controller-footprint requirements, this
reduces to the cardinality inequality
`|R_X|<=|C_X^(alpha,eligible)|`; in general one retains the full Hall
inequalities in that fibre.  The Boolean-ideal compiler has one demand per
subset, so Corollary 6.2 applies exactly.

### Proposition 6.3 (raw normalized matching does not imply private hits)

For every `N>=3` there is a trace-two instance whose base option graph is
`K_(N,N)` and hence satisfies every normalized matching inequality, but no
assignment satisfies all residual private-hit requirements.

#### Proof

Take

\[
 \Omega=\{a,e_1,\ldots,e_N\},\qquad
 S_i=\{a,e_i\}\quad(1\le i\le N),
\]

positions `0,1,...,N`, envelopes `E_p=Omega`, and cells

\[
 I_j=\{j-1,j\}\quad(1\le j\le N).
\]

Declare every target eligible for every cell.  Under any bijection, an
internal position belongs to two intervals carrying two distinct targets,
so its meet is `{a}`.  At each endpoint the meet is the unique incident
target.  Only the two targets placed on `I_1` and `I_N` retain their private
markers.  Every target placed on an internal interval has union `{a}` and
loses `e_i`.  Thus `N-2` private-hit requirements fail, although the base
graph is complete and no point meet uses more than two active targets.
\(\square\)

In particular, the private-point condition is not itself a matroid on the
interval family.  On
`{1,2,3}`, the families

\[
 \mathcal A=\{\{1,2,3\}\},\qquad
 \mathcal B=\{\{1\},\{2\}\}
\]

are both irredundant and `|A|<|B|`, but adding either member of `B` to `A`
destroys irredundancy of that singleton.  Thus the exchange axiom fails.
This does not rule out a more elaborate encoding using several matroids.

## 7. Hypersimplex completion and the exact remaining lift

For a depth-`d` resident chronology in `J(k,r)`, let the depth-`q` trace row
have rank `s_q=r-q`, length `W-q`, and let

\[
 e_q=W-q-\binom{k}{s_q}.
\]

The exact transport law prescribes the excess point-degree vector
`gamma_q=(gamma_(q,x))`.  The root theorem
`MATH_HYPERSIMPLEX_MARGINAL_COMPLETION_AND_CHRONOLOGY_GATE_20260728.md`
proves:

### Theorem 7.1 (rankwise hole-free completion)

Assume `e_q>=0`, `gamma_q in Z^k`, and

\[
 \sum_x\gamma_{q,x}=s_qe_q.
 \tag{7.0}
\]

If

\[
 0\le\gamma_{q,x}\le e_q\quad(x\in[k]),
 \tag{7.1}
\]

then there is a hole-free rank-`s_q` multiset with the same size and point
degrees as the actual depth-`q` row.  It is connected to the actual row by
symmetric two-block exchanges.

#### Proof

The checksum is

\[
 \sum_x\gamma_{q,x}=s_qe_q.
\]

Inductively choose an `s_q`-set containing every coordinate currently of
degree `e_q` and otherwise positive-degree coordinates, subtract its
incidence vector, and repeat.  This decomposes `gamma_q` into `e_q` uniform
blocks.  Add those blocks to one copy of every rank-`s_q` target.  Equality
of point degrees gives two binary block-by-coordinate incidence matrices
with the same row and column sums after the blocks are labelled.  The binary
contingency-table interchange lemma says that any two such matrices are
connected by legal `2 by 2` switches.  Applied here, each switch exchanges
one coordinate between two uniform blocks and is exactly a symmetric
two-block exchange.  This lemma is proved by alternating-cycle reduction in
the cited root theorem.  \(\square\)

For the frozen Hall-29 `k=15` carrier, (7.1) holds with

\[
 q=2:\quad 568\le\gamma_{2,x}\le574<1428=e_2,
\]

\[
 q=3:\quad 1138\le\gamma_{3,x}\le1147<3429=e_3.
\]

Thus its depth-two and depth-three holes are not forced by scalar capacity,
point marginals, or the rankwise exchange lattice.

### Open Lemma 7.2 (simultaneous chronology-owner hypersimplex lift)

Let a resident middle chronology and its entire nested trace tower be given.
Assume that, at every required depth, the integrality, checksum, and bound
hypotheses (7.0)--(7.1) hold.  Prove that there exist hole-free multisets in
the corresponding marginal fibres and one modified deletion/insertion word
such that the resulting chronology

1. is again an exact ordering of the prescribed middle layer, with all fixed
   endpoint and boundary data retained;
2. induces those hole-free rows at every depth simultaneously and satisfies

   \[
    L_i^{(q+1)}=L_i^{(q)}\cap L_{i+1}^{(q)}
   \]

   throughout the tower;
3. remains a legal Johnson chronology and satisfies all even-start
   odd-distance residence exclusions (3.5);
4. has complete upper flag support; when the modification is decomposed into
   the connectors of Theorem 2.1, this is exactly the targetwise ledger
   (5.1); and
5. admits one admissible trace-two skeleton satisfying the targetwise
   interval-union condition (6.6), including all central middle-window pairs
   in `P_0`.

No result in the current package proves Open Lemma 7.2.  Separate
hypersimplex decompositions do not synchronize their exchanges, the local
hexagon preserves only its first owner ledger automatically, and raw Hall
matching does not construct the required skeleton word by Proposition 6.3.

## 8. Exact proved/conditional boundary

The following statements are unconditional:

1. PBBS supplies the complete all-depth flag tower with load (1.2).
2. PBBS component collars cost `o(W)` at Gaussian depth; topology alone is
   not the coefficient-one gate.
3. The complement-paired hexagon has the exact all-depth coboundary (2.4).
4. Residence is exactly the deletion-word condition (3.3); old bad witnesses
   must be hit, and new seams require the tests (3.6).
5. Exact upper ownership forbids nontrivial two-arc switches.
6. Trace-two residual extension has the exact skeleton interval-union
   characterization (6.6); after the skeleton is fixed, there is no
   cross-target matching competition for distinct set targets.
7. Every rankwise marginal fibre satisfying (7.0)--(7.1) contains a
   hole-free design.

What remains unproved is different in the two applications:

* For asymptotic coefficient one through PBBS, the smallest audited gate is
  the short-residence little-oh estimate (1.5), or an equivalent
  residence-sharing surgery.  Hamiltonization is unnecessary.
* For the exact finite compiler, the smallest audited gate is Open Lemma
  7.2.  It is a simultaneous chronology/upper-support/owner lift, not a
  rankwise balancing lemma.
