# All-odd wedge sockets, compiler automaticity, and mixed-duplex separation

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: exact implication and separation theorems; explicit joint all-odd
existence lemmas remain unproved.  The reported `24/24` compilation census is
used only as empirical evidence.

## 0. Verdict

The protected outward-ray route and the mixed-tag duplex route address
different quantifiers.

1. A wedge cut is an **upper-carrier** operation.  The authoritative
   assigned-ray theorem bounds its old upper spill by

   \[
                       b(k-r-1)                     \tag{0.1}
   \]

   for `b` components.  A facet-socket seam recreates every assigned
   fixed-width ray crossing one serviced cut at all depths simultaneously;
   a reciprocal seam can service the left cut of one component and the right
   cut of the next at once.
2. `COMP_d(T)` is a **lower-source** existence statement after the final
   middle path `T` has been chosen.  Positive deadline slack counts short
   physical cells but does not prove the required labels or one common
   source.  Uniform automaticity on protected positive-slack openings remains
   unproved.
3. The double-facet mixed module is a still stronger **typed recursive**
   source statement.  Its source fibre is a subfibre of unrestricted
   `COMP_d(T)` because it retains parent correlations, phase, future collars,
   and the renewable socket.  A direct all-odd compiler may lie outside that
   subfibre.

Consequently a proved positive-slack compiler theorem plus a good protected
wedge/socket opening would bypass the explicit mixed-module construction for
a **terminal all-odd word**.  It would not prove the ported Pascal induction:
the terminal compiler source may violate the typed tag and parent-source
relations needed by the next step.

The `O(bk)` assigned-ray spill also cannot be paid by the lower mixed
compiler.  Short lower cells have rank at most the middle rank, whereas every
upper ray casualty has larger rank.  There are only two valid compositions:

- append the explicit ray list, obtaining `B(k)+O(bk)` terminal length; or
- realize those rays in an upper owner-seam/facet-socket bank under the same
  final carrier, at zero length cost.

The latter adds only `O(bk)` upper equations to the common natural join and
does not create another exponential mixed-lower demand.  It can nevertheless
empty the common source/carrier join, so compatibility must be proved.

For factors with at least two components, a stronger linear object avoids a
separate safe root: open the first component on a left wedge flank, the next
on a right flank, and use one **reciprocal facet socket** to repair both cuts;
later components attach as one-way keyed ears.  For two active components
this reciprocal seam is the exact canonical condition.  The smallest
separated all-odd proof package is therefore:

1. a protected at-most-two-component factor with a legal PWI opening or
   reciprocal-root socket opening; and
2. a compiler source for that **same** opening.

Their coupled form is the exact joint opening-compiler lemma in Section 7.

## 1. Upper support is a carrier invariant

Let `T=(T_0,...,T_(W-1))` be a rank-`r` middle path and let

\[
 Q=(Q_0,\ldots,Q_{W+d-1}),
 \qquad
 T_i=\bigcup_{p=i}^{i+d}Q_p.                       \tag{1.1}
\]

Every `Q_p` is nonempty.  Put

\[
 \operatorname{Up}(T)
 =\left\{\bigcup_{i=a}^{b}T_i:0\le a\le b<W\right\}. \tag{1.2}
\]

### Theorem 1.1 (source/owner upper correspondence)

For every target `Y` with `|Y|>r`,

\[
 Y\in\operatorname{IntOR}(Q)
 \quad\Longleftrightarrow\quad
 Y\in\operatorname{Up}(T).                         \tag{1.3}
\]

More precisely, an owner interval `[a,b]` maps to the source interval
`[a,b+d]`, and an upper source interval `[a,b]` maps to the owner interval
`[a,b-d]`; both maps preserve the union label.

Every strict-lower source witness has at most `d` letters.  Hence upper
support depends only on `T`, while strict-lower support depends on the chosen
source `Q` inside its compiler fibre.

#### Proof

Any source interval of at most `d+1` positions is contained in a full owner
window `[i,i+d]`; if it has exactly `d+1` positions it is one such window.
Its union therefore has rank at most `r`, and rank exactly `r` in the full
window case.  Thus an upper witness `[a,b]` has `b-a+1>=d+2`.  It necessarily
has `a<W` and `b-d>=0`, and

\[
 \bigcup_{i=a}^{b-d}T_i
 =\bigcup_{i=a}^{b-d}\bigcup_{p=i}^{i+d}Q_p
 =\bigcup_{p=a}^{b}Q_p.                             \tag{1.4}
\]

Conversely,

\[
 \bigcup_{p=a}^{b+d}Q_p
 =\bigcup_{i=a}^{b}T_i.                             \tag{1.5}
\]

The same containment argument shows that a strict-lower witness cannot have
`d+1` positions.  \(\square\)

Fix a family of legal final carriers `mathfrak T`.  For `T in mathfrak T`,
let

\[
 u(T)=\#\{Y\subseteq[k]:|Y|>r,\ Y\notin\operatorname{Up}(T)\}       \tag{1.6}
\]

and let `Delta_L(T)` be the exact lower defect minimized over one joined
compiler source fibre, with `+infinity` for an empty fibre.  In the typed
Pascal setting, `Delta_L` is the four-signature functional of the companion
mixed-bulk report.

### Corollary 1.2 (exact carrier/compiler separation)

Assume every `T in mathfrak T` enumerates the middle layer exactly.  Then

\[
 \boxed{
 \nu(k)\le B(k)+
       \min_{T\in\mathfrak T}[u(T)+\Delta_L(T)].}   \tag{1.7}
\]

Relative to a fixed deadline carrier, exact length `B(k)` requires one and
the same `T` with

\[
                          u(T)=0,
 \qquad                   \Delta_L(T)=0.            \tag{1.8}
\]

#### Proof

Choose one source attaining `Delta_L(T)`.  It covers the middle layer, every
upper target in `Up(T)` by Theorem 1.1, and all but `Delta_L(T)` lower masks.
Append each missing upper and lower mask as a literal source letter.  This
gives (1.7).  At exact deadline length no appendage is available, proving
(1.8).  \(\square\)

The appendage is terminal: it need not preserve (1.1), endpoints, residence,
or a renewable port type.

## 2. Assigned outward-ray spill composes only additively

Let a protected fixed-width factor have `b` components.  Assign one
geodesic fixed-width witness to every upper target, choose one wedge flank to
cut in each component, and install a legal final middle path `T`.  Let
`\mathcal C_{\rm ray}(T)` be the distinct assigned outward-ray labels whose old
component-interior witnesses are all destroyed and which are not recreated
by the new seams.

The authoritative assigned-ray theorem gives

\[
 |\mathcal C_{\rm ray}(T)|
 \le b(k-r-1).                                      \tag{2.1}
\]

If a separate depth-two protection condition preserves every rank-`(r+2)`
target, the bound improves to

\[
 |\mathcal C_{\rm ray}(T)|
 \le b\max\{k-r-2,0\}.                             \tag{2.2}
\]

Every upper target outside this explicit list retains an old assigned
witness, so

\[
                         u(T)\le|\mathcal C_{\rm ray}(T)|.           \tag{2.3}
\]

### Theorem 2.1 (terminal assigned-ray completion)

If the final path `T` has a feasible exact lower compiler, then

\[
 \boxed{
 \nu(k)\le B(k)+b(k-r-1),}                         \tag{2.4}
\]

with (2.2) giving the corresponding improvement.  If the mixed-tag FCT
module and the other signature modules close the lower compiler, the same
bound holds for that typed child.

#### Proof

Apply Corollary 1.2 with `Delta_L(T)=0` and (2.3), then append the explicit
unrepaired ray labels.  \(\square\)

This is `B(k)+O(k)` when `b=O(1)`.  It does not establish coefficient one.
The upper ray list cannot use the strict-lower compiler's short cells, by
Theorem 1.1.  Exact zero-cost absorption requires an **upper owner interval**
of `T` for every actual lost ray label.

### Corollary 2.2 (ray-port absorption)

Let `\mathcal J_L` be one joined source relation under which the complete
lower compiler is exact, and fix its final carrier `T`.  Add occurrence-
labelled upper seam/bridge requirements

\[
 \mathcal U_{\rm ray}
 =\{(Y,I_Y):Y\in\mathcal C_{\rm ray}(T),
                   \bigcup_{i\in I_Y}T_i=Y\}.       \tag{2.5}
\]

If every actual ray casualty has such an owner interval and the physical
seam/residence/endpoint relations remain legal, then the deadline child is
upper-complete at zero extra length.  Once `T` is fixed, these are
carrier-only equations and cannot shrink its already-defined source fibre.
If the carrier/opening is still variable in a larger parent/child
construction, however, imposing them before projection may eliminate all
carrier choices and hence empty the combined natural join.

#### Proof

The owner intervals in (2.5) restore every casualty, while all other upper
targets retain their assigned witnesses.  Theorem 1.1 lifts all owner
intervals through every source with the fixed carrier `T`.  \(\square\)

Thus `O(bk)` upper absorption does **not** recreate the exponential
mixed-lower obstruction.  It is a separate `O(bk)` port relation.  It is not
automatic from lower slack or from FCT.

There is a scale warning for Catalan-many upper openings.  For a child of
dimension `k=2r+2`, middle rank `R=r+1`, and
`b=Cat_r=binom(2r,r)/(r+1)`, the blind bound is

\[
 b(k-R-1)=r\operatorname{Cat}_r=\binom{2r}{r-1}.    \tag{2.6}
\]

Relative to `W_child=binom(2r+2,r+1)`, its exact ratio is

\[
 {\binom{2r}{r-1}\over\binom{2r+2}{r+1}}
 ={r\over2(2r+1)}\longrightarrow{1\over4}.         \tag{2.7}
\]

Hence Catalan-many blind ray appendages are `Theta(W)`.  Coefficient one
requires PWI or exact seam rehosting, not merely the assigned-ray count.

## 3. Facet sockets repair every depth simultaneously

Let

\[
 C=(A_0,\ldots,A_{N-1})\subset J(k,r),
 \qquad e_i=A_iA_{i+1}
\]

be a directed simple cycle, with cyclic indices.  Assume `1<=q<N` for every
selected `q`-edge witness.  Suppose `A_i` is a wedge:

\[
 U=A_{i-1}\cup A_i=A_i\cup A_{i+1},qquad |U|=r+1. \tag{3.1}
\]

Cut its right flank `e_i`.  The opened path starts at
`S=A_(i+1)` and ends at `E=A_i`.  Let `B` be the terminal owner of a
preceding opened component and assume

\[
                         B\cup S=U=E\cup S.         \tag{3.2}
\]

### Theorem 3.1 (simultaneous facet-socket ray repair)

Let

\[
 A_s,A_{s+1},\ldots,A_{s+q}
\]

be any selected geodesic `q`-edge witness on `C`.  If its edge span avoids
`e_i`, it remains internal after opening.  If its edge span contains `e_i`,
then it is exactly

\[
 A_i,A_{i+1},\ldots,A_{i+q},                       \tag{3.3}
\]

and the new seam interval

\[
 B,A_{i+1},\ldots,A_{i+q}                          \tag{3.4}
\]

has the same union.  Therefore one facet-socket seam restores every selected
fixed-width outward ray crossing this cut, at every depth.

#### Proof

A geodesic interval containing both wedge flanks would traverse two
transitions with only one net new element: the element inserted on the second
transition is already present at `A_(i-1)`.  Its union would have rank at most
`r+q-1`, a contradiction.  A directed interval with `q<N` containing `e_i`
but not its immediate predecessor `e_(i-1)` must start at `A_i`, proving
(3.3).  Finally, using (3.2),

\[
\begin{aligned}
 B\cup A_{i+1}\cup\cdots\cup A_{i+q}
  &=(B\cup S)\cup A_{i+2}\cup\cdots\cup A_{i+q}\\
  &=(E\cup S)\cup A_{i+2}\cup\cdots\cup A_{i+q}\\
  &=A_i\cup A_{i+1}\cup\cdots\cup A_{i+q}.
\end{aligned}
\]

\(\square\)

The theorem needs only the selected fixed-width witness on its provider
component.  Global fixed-width support suffices after assigning each target
to one such component; componentwise support for every target is not needed.
Also, `q<N` is automatic for a geodesic occurrence: completing one circuit
returns to its initial vertex, so that transition cannot introduce a fresh
coordinate into the interval union.

### Theorem 3.2 (linear reciprocal root and keyed ears)

Let `b>=2`.  Choose an order `a_1,...,a_b` of the components.  On the first
component cut the **left** wedge flank at `i_1`, giving the retained path

\[
 P^-_1=(A^{a_1}_{i_1},A^{a_1}_{i_1+1},\ldots,
        A^{a_1}_{i_1-1}),\quad
 R_1=A^{a_1}_{i_1-1},\quad
 U_1=R_1\cup A^{a_1}_{i_1}.                        \tag{3.5}
\]

On each later component cut a right wedge flank, giving

\[
 P^+_j=(S_j=A^{a_j}_{i_j+1},\ldots,
        E_j=A^{a_j}_{i_j}),\qquad U_j=E_j\cup S_j. \tag{3.6}
\]

If

\[
 R_1\cup S_2=U_1=U_2                              \tag{3.7}
\]

and

\[
 E_j\cup S_{j+1}=U_{j+1}\qquad(2\le j<b),         \tag{3.8}
\]

then concatenating `P^-_1,P^+_2,...,P^+_b` gives a strict linear Johnson
path on exactly the old vertex deck and retains a witness for every target in
the globally assigned fixed-width tower.

#### Proof

Every displayed seam has union rank `r+1`, hence is Johnson.  A selected
geodesic block avoiding its component cut remains internal.  By the wedge
argument in Theorem 3.1, a block crossing the first, left cut cannot cross the
other wedge flank and therefore ends at `A^{a_1}_{i_1}`.  In the concatenated
path its last vertex is replaced by `S_2`; equation (3.7) preserves its union.
For `j>=2`, a block crossing the right cut starts
`E_j,S_j,...`.  Its missing predecessor is replaced by the actual preceding
path endpoint—`R_1` when `j=2` and `E_{j-1}` thereafter—and (3.7) or (3.8)
again preserves its union.  Every replacement has the same `q+1` vertices.
No vertex is added or deleted.  \(\square\)

For a right port put `\kappa=E\setminus S`; then
`U=S\cup\{\kappa\}`.  For any rank-`r` foreign endpoint `B`,

\[
 B\cup S=U
 \quad\Longleftrightarrow\quad
 B\sim S\ \hbox{ and }\ \kappa\in B.             \tag{3.9}
\]

The analogous statement holds for a left port.  Thus (3.7) is a reciprocal
key seam servicing both components, while every seam in (3.8) is a one-way
keyed ear.

Call a port repair **canonical** when a serviced side uses one seam whose
two endpoint union is exactly that port's two-vertex wedge union; equivalently
it replaces only the missing endpoint of each active outward ray as in
Theorem 3.1.  There is an exact signed-path formulation inside this canonical
class when **every chosen component port is active**.  Give an opened port type `O` if its rays need the
outgoing seam and type `I` if they need the incoming seam.  Write its retained
path as `(L_j,...,R_j)` and its wedge union as `U_j`.  A canonical linear
repair exists for a fixed ordered option tuple if and only if the first type
is `O`, the last is `I`, every
seam

\[
                         V_j=R_j\cup L_{j+1}
\]

has rank `r+1`, and

\[
 \epsilon_j=O\Rightarrow V_j=U_j,
 \qquad
 \epsilon_{j+1}=I\Rightarrow V_j=U_{j+1}.         \tag{3.10}
\]

Sufficiency is the endpoint-replacement proof above; necessity inside this
canonical one-endpoint reuse class follows from (3.9).  An `O->I` seam is
reciprocal and forces the two wedge unions equal; an `I->O` seam services
neither side.  The root-and-ears form is necessary for `b=2` and, up to
reversal, for `b=3` when every port is active.  For `b>=4` it is only a clean
sufficient signature; other signed canonical paths, and still more general
multi-state seam grids, may exist.

Equivalently, canonical socket existence is a **colorful directed Hamilton
path** problem in the graph of oriented wedge-flank options, with one vertex
of each component color and arcs defined by (3.10).  This is stronger than
finding an arbitrary directed cycle or a cycle cover.

### Corollary 3.3 (distinguished-safe-root alternative)

Let `C_(a_1),...,C_(a_b)` be ordered right-opened components.  Assume the
assigned witness of every target on the first component survives its cut or
has an explicit final replacement, and for `j=2,...,b` assume

\[
                         E_{j-1}\cup S_j=U_j.       \tag{3.11}
\]

If all new seams, residence conditions, owners, and endpoints are legal,
then the concatenated linear path preserves or recreates every assigned upper
target.

#### Proof

The root targets survive by hypothesis.  Theorem 3.1 repairs every selected
witness crossing a later cut; untouched witnesses remain internal.
\(\square\)

A directed socket cycle through one oriented option from every component
repairs all component cuts and produces an upper-complete **cyclic**
chronology only when every socket is a legal Johnson seam and all cyclic
owner and residence conditions pass.  It does not itself give a linear word:
a subsequent opening still needs Corollary 3.3, an explicit final
replacement, or the reciprocal-root construction of Theorem 3.2.

Finally, `b` cuts remove only `b` old lower-q1 edge occurrences.  Hence at
most `b` lower-q1 labels, and at most `b` multiplicity units, can lose their
last provider.  The socket theorem preserves upper-q1 set coverage, but a
reciprocal seam can replace two equal old wedge-union occurrences by one, so
upper multiplicity is not preserved.  These lower debts belong in the same
pinned `COMP_d`/FCT join; the upper theorem does not discharge them.

## 4. PWI admissibility and Cartesian option banks

Let `Omega_j` be the fully typed local wedge-option bank on component `j`.
Each option records its signed flank, orientation, cut edge, start/end owners,
socket key, and all local dependency collars.  Let `a=(a_j)`, let `gamma`
record order/connector choices not contained locally, and let `Q` be the one
final source.

Form the unprojected relation

\[
\begin{aligned}
 \mathcal J_{\rm wedge}
 ={}&\left(\Join_j\mathcal R_j(a_j)\right)
 \Join\mathcal R_{\rm topology}(a,\gamma)
 \Join\mathcal R_{\rm owner/residence/seam}(a,\gamma)\\
 &\Join\mathcal R_{\rm local\ socket/collar}(a,\gamma)
 \Join\mathcal R_{\rm source/COMP}(T(a,\gamma),Q). \tag{4.1}
\end{aligned}
\]

No shared connector or source variable is projected before this join.  The
exact jointly admissible compiler-supported option atlas is

\[
                         \mathcal A_{\rm comp}
 =\pi_a\mathcal J_{\rm wedge}.                     \tag{4.2}
\]

The local socket/collar relation includes declared endpoint keys, protected
local upper witnesses, and seam collars.  It deliberately excludes both the
global old-witness PWI condition and full upper completeness being tested
below; including either would make the probability criterion circular.

### Theorem 4.1 (exact Cartesian criterion)

The complete local product is jointly admissible if and only if

\[
 \boxed{
 \forall a\in\prod_j\Omega_j\quad
 \exists(\gamma,Q,\mathrm{aux})
       \text{ satisfying }\mathcal J_{\rm wedge}.} \tag{4.3}
\]

A nonempty product subbank `prod_j Omega'_j` is safe if and only if

\[
                         \prod_j\Omega'_j
                         \subseteq\mathcal A_{\rm comp}.             \tag{4.4}
\]

Equivalently, it contains no minimal partial option assignment having no
extension in `\mathcal J_{\rm wedge}`.

#### Proof

Equations (4.3)--(4.4) are precisely the definition of the projection in
(4.2).  A minimal nonextendible partial assignment is a forbidden cylinder;
a product bank is contained in the projection exactly when it contains none
of them.  \(\square\)

Pairwise seam tables suffice only when the relation has a lossless
running-intersection factorization after all shared interface/source
separator variables are retained.  If one deadline window or coordinate run
meets two seams, or two local relations share unfixed source bits, the
higher-arity relation is essential.  For two components, extracting a
Cartesian subbank is exactly finding a complete bipartite subgraph in the
full option-compatibility graph, not merely two nonempty marginal banks.

Wedge deletions on distinct old components commute geometrically.  Their
compiler sources need not commute: the order and seams change the final
chronology, its envelopes, and every crossing lower trace.  Different
hypothetical option tuples may use different sources `Q`, but each actual
tuple must use one source across all components and modules.

Let `B_Y^{\rm old}` be the authoritative old-witness bad box for upper target `Y`.
On a safe product subbank, the product-SPILL formula is valid.  On a
non-Cartesian atlas it is not; one must use an arbitrary distribution `pi`
on `\mathcal A_{\rm comp}` and the general potential

\[
 \Phi_{\mathcal A}(\pi)
 =\sum_{|Y|>r}\pi(B_Y^{\rm old}\cap\mathcal A_{\rm comp}). \tag{4.5}
\]

If (4.5) is below one, some **compiler-feasible** jointly admissible tuple
retains an old witness of every upper target.  PWI is sufficient but not
necessary after rethreading, because Theorem 3.1 may replace a killed old
witness by a facet-socket seam.

If `\pi` may range over every distribution on `\mathcal A_{\rm comp}`, then
the existence of a PWI tuple is equivalent to a point mass with potential
zero.  Thus only a prescribed, structured, or product measure gives a
substantive probabilistic bound.

## 5. Positive slack does not merge the quantifiers

For odd `k=2m+1`, put

\[
 r=m+1,\qquad W=\binom{k}{r},\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},             \tag{5.1}
\]

and

\[
 d=\min\left\{j\in\mathbb Z_{\ge0}:
                 jW+\binom{j+1}{2}\ge\Lambda\right\},
 \qquad
 \sigma=dW+\binom{d+1}{2}-\Lambda.                \tag{5.2}
\]

The slack `sigma` counts excess short interval cells over distinct lower
targets.  It does not specify their labels, source correlations, or central
window hits.  Moreover, by Theorem 1.1 those short cells cannot realize an
upper ray target.

Define the proposed automaticity statement:

> **Protected positive-slack compiler automaticity `PSC(m)` (UNPROVED).**  
> Every legal, linearly `d`-resident, upper-safe opening in the declared
> protected at-most-two-component class, with its exact q1 boundary
> eligibility and every distinct outer-halo pin required by UPMBC clause 4,
> has a feasible pinned `COMP_d(T)` whenever `sigma>0`.

This is a strong sufficient theorem, not a consequence of scalar slack.
The reported `24/24` result proves only that 24 sampled `k=13` openings which
had already passed the upper filter compiled.  It proves neither `PSC(6)`
for all admissible `k=13` openings nor `PSC(m)` uniformly.

For the weakest existential bridge, fix one protected factor `G` and write

\[
\begin{aligned}
 \mathcal A_{\rm good}(G)
   &=\{a:a\text{ is jointly legal, resident, and upper-safe}\},\\
 \mathcal A_{\rm comp}(G)
   &=\{a:\text{the full pinned }\operatorname{COMP}_d(T_a)
              \text{ required by UPMBC clause 4 is feasible}\}.
                                                               \tag{5.3}
\end{aligned}
\]

The exact opening/compiler bridge is only

\[
 \boxed{
 \mathcal A_{\rm good}(G)\cap
 \mathcal A_{\rm comp}(G)\ne\varnothing.}         \tag{5.4}
\]

Statement `PSC(m)` implies (5.4) whenever `A_good` is nonempty, but is
strictly stronger than necessary.  Separate nonemptiness of the two sets in
(5.3) does not imply (5.4).

## 6. Relation to the mixed-tag duplex compiler

For a fixed final Pascal child carrier `T`, let

\[
 \mathcal F_{\rm Pas}(T)\subseteq
 \mathcal F_{\rm unr}(T)                            \tag{6.1}
\]

be, respectively, the **full** typed Pascal source fibre and the unrestricted
`COMP_d(T)` fibre.  Here “full” means that FCT's mixed block, all three
nonmixed blocks, the protected package, and one common natural join are
realized on the same flat carrier and the same `W+d` source positions.  Under
those hypotheses the inclusion holds because the typed system contains all
unrestricted lower-coverage equations and adds parent-source, double-facet,
tag-support, erosion, phase, future-collar, and protected-port relations.  A
local double-facet module by itself does not imply this inclusion.

Therefore:

- full FCT closure with the other three blocks implies an unrestricted
  compiler for its child;
- an unrestricted positive-slack compiler need not export an `FCT` source;
- direct all-odd equality does not imply a reusable Pascal socket; and
- the mixed-bulk obstruction remains valid inside `F_Pas`.

An unrestricted compiler can bypass the explicit mixed-module construction
only by leaving the typed Pascal subfibre—for example by distributing fresh
tag bits outside the canonical sector support.  If it stays inside the
support-separation hypotheses of the mixed-bulk theorem, it must realize the
required bulk labels and cannot contradict the counting bound.

Facet sockets themselves are stable under common-tag suspension.  Indeed,
from `B\cup S=U` one obtains, for every fresh tag set `Z`,

\[
 (B\cup Z)\cup(S\cup Z)=U\cup Z.                  \tag{6.2}
\]

Under the full chain-wide guarded-duplex hypotheses of item 2059, including
the overlapping bridge block, the theorem therefore renews an **existing**
sector socket chain through common-tag suspension.  Equation (6.2) alone
certifies only the returned socket equation: at the intermediate facet stage
the complete guarded bridge triad is still required, and only the
natural-union return restores the original socket type.  Nothing in (6.2)
supplies cross-sector keyed ears or a colorful global socket path.

Suppose full FCT closure has already supplied the lower compiler for one
wedge-opened child.  Theorem 2.1 then gives a terminal `B+O(bk)` word.  To
retain exact deadline and the recursive output type, the same pre-carrier
construction must also select a legal socket path satisfying Theorem 3.2 or
3.3 and absorb its at most `b` lower-q1 seam debts.  These conditions create
no new exponential mixed-lower target family.  Once `T` is fixed, the upper
owner equations do not further restrict `Q`; before `T` is fixed, however,
the socket path, carrier, FCT source, erosion, residence, and lower debts must
all survive one unprojected natural join.

## 7. Exact all-odd implication diagram

For each `m`, use the following statements.

- `PF2(m)`: a `d`-protected, all-depth PBBS/Markov factor with at most two
  components exists.
- `GO_full(m)`: one such factor has a legal, linearly resident, upper-safe
  opening, equivalently an option outside every exact bad set
  `B_Y^{\rm full}` which records both loss of all old witnesses and failure of
  all new seam witnesses.
- `GO_PWI(m)`: one such factor has a legal, linearly resident opening outside
  every old-witness bad set `B_Y^{\rm old}`.
- `GO_sock(m)`: one such factor has a legal, linearly resident, upper-safe
  opening after allowing exact facet-socket replacement witnesses.  It need
  not satisfy `GO_PWI(m)`.
- `PSC(m)`: the strong automaticity statement in Section 5.
- `UPMBC(m)`: the four-clause protected boundary/compiler lemma from the
  authoritative all-odd reduction.
- `FMCC(m)`: some upper-complete middle permutation has feasible unrestricted
  `COMP_d`.

The two proof subclasses are generally incomparable, but

\[
 GO_{\rm PWI}(m)\Longrightarrow GO_{\rm full}(m),
 \qquad
 GO_{\rm sock}(m)\Longrightarrow GO_{\rm full}(m). \tag{7.1}
\]

For `\sigma(m)>0`, the proved direct chain is

\[
\boxed{
 \bigl[GO_{\rm full}(m)+PSC(m)\bigr]
 \Longrightarrow UPMBC(m)
 \Longrightarrow FMCC(m)
 \Longrightarrow \nu(2m+1)=B(2m+1).}              \tag{7.2}
\]

The existential opening in `GO_full` is the opening to which universal `PSC`
is applied.  At zero slack this implication does not follow from the stated
`PSC`; in particular the known `k=9` zero-slack case is a separate base, not
an instance of (7.2).  Both PWI and facet sockets feed this same chain;
authoritative UPMBC clause 3 uses `B_Y^{\rm full}` and therefore permits a
new seam witness.

The same-factor opening decompositions are

\[
 \exists G\in\mathscr P_{m,d}\ 
 \bigl[c(G)\le2\ \land\ \exists a\text{ PWI-good for }G\bigr]
 \Longrightarrow GO_{\rm PWI}(m),
                                                               \tag{7.3}
\]

and the analogous formula with a legal reciprocal-root socket path implies
`GO_sock(m)`.  Marginal existence of some `PF2` factor and of a good opening
on a different factor does not compose.

The weakest coupled sufficient statement is:

> **Odd joint opening-compiler lemma `JOC(m)` (UNPROVED).**  There exist one
> protected factor `G\in\mathscr P_{m,d}` with at most two components, one
> legal choice of cut/orientation per component and (when needed) one seam
> giving a linearly resident and upper-safe opening `a`, and one source in the pinned
> full `COMP_d(T_(G,a))` fibre, with every relation—seams, residence, distinct
> outer-halo pins, upper replay, and compiler equations—satisfied
> simultaneously.

`JOC(m)` is the natural-join restatement of endpoint-form UPMBC and is the
exact coupled wrapper needed for the direct all-odd proof.  Its PWI and
canonical-socket subfamilies are two stronger sufficient proof classes.
Proving `JOC(m)` for every
`m` implies `FMCC(m)` and proves all odd cases.  Positive-slack `PSC(m)` is a
stronger modular route only when `\sigma(m)>0`.

The ported Pascal route is parallel:

\[
\boxed{
 \text{ported base}
 +\text{exact child carrier}
 +\text{three nonmixed blocks}
 +FCT(r,D,d)
 +\text{linear upper socket in the same join}
 \Longrightarrow\text{deadline recursive child}.} \tag{7.4}
\]

For `s\in\mathcal S_{\rm linear}` and
`\omega\in\mathcal J_{\rm FCT}(s)`, let `\delta_{\rm FCT}(s,\omega)` be the
pointwise four-signature residual defect of the companion common-source
theorem after deleting the declared protected demands and occurrences.  The
exact remaining typed socket-existence statement is

\[
 \boxed{
 \exists s\in\mathcal S_{\rm linear}\quad
 \exists\omega\in\mathcal J_{\rm FCT}(s):
          \delta_{\rm FCT}(s,\omega)=0.}            \tag{7.5}
\]

Here `\mathcal S_{\rm linear}` is the colorful canonical signed-path atlas
of (3.10), and the **same** unprojected relation `\mathcal J_{\rm FCT}(s)`
contains path realization, residence, output boundary, the at most `b`
lower-q1 seam debts, erosion, all four tag blocks, protected providers,
future collars, and every protected/compiler occurrence variable.  Residual
lower coverage itself is excluded from the relation and is measured by
`\delta_{\rm FCT}`.  Separate existence of a
socket path and of a source in a differently projected FCT fibre does not
prove (7.5).  This is exact within the declared canonical signed-path atlas
`\mathcal S_{\rm linear}`; it is only sufficient against the broader
noncanonical or multi-state seam grids explicitly left outside Section 3.

There is no current implication between `UPMBC` and `FCT`.  `UPMBC` need not
provide order-one transparency, a full-core redundant position, future
collars, or a typed parent/child source relation.  `FCT` does not construct a
protected odd factor or a legal opening.  An additional typed theorem saying
that a `UPMBC` output exports the next `FCT` input would be needed to join the
two inductions.

For a compiler-supported admissible atlas, one may replace `PSC` by the
following weaker probabilistic sufficient lemma:

\[
 \exists(G,\pi),\quad
 \operatorname{supp}\pi\subseteq\mathcal A_{\rm comp}(G),
 \qquad
 \sum_{|Y|>r}\pi(B_Y^{\rm old}\cap\mathcal A_{\rm comp})<1. \tag{7.6}
\]

The general PWI expectation theorem then produces a compiler-feasible
upper-safe tuple.  Product independence is unnecessary; it is valid only
after Theorem 4.1 certifies a Cartesian subbank.

## 8. Audit and scope boundary

The argument uses the authoritative protected outward-ray theorem.  No
unrestricted three-OR kill-shape claim is used.

The independent audit of the fixed-width facet-socket theorem made four
scope corrections which are incorporated above: geodesicity makes `q<N`
automatic; one global assigned tower suffices; a component-spanning socket
cycle is cyclic rather than a linear word; and socket vertices are oriented
wedge-flank options, so the relevant object is a colorful path/cycle rather
than an uncolored cycle cover.  The reciprocal-root proof in Theorem 3.2
supplies a genuinely linear alternative.  It preserves upper set coverage,
not upper multiplicity, and it leaves at most `b` lower-q1 debts for the
common compiler join.

The decisive quantifier separations are:

\[
 (\exists G\ P(G))\land(\exists G'\ O(G'))
 \not\Rightarrow\exists G\,[P(G)\land O(G)],       \tag{8.1}
\]

\[
 (\exists T\ U(T))\land(\exists T'\ C(T'))
 \not\Rightarrow\exists T\,[U(T)\land C(T)],       \tag{8.2}
\]

and separate signature-source choices do not imply one common compiler
source.  The literal two-state counterexample in the mixed-bulk report proves
the last failure.

The following statements remain unproved and are not inferred from finite
data:

1. growing-`d` existence of a protected at-most-two-component factor;
2. a PWI-good opening or a colorful reciprocal/keyed socket path for that
   same factor, with residence and output boundary;
3. positive-slack compiler automaticity or the weaker same-opening pinned
   join (5.4); and
4. for recursive Pascal closure, cross-sector keyed ears and export of a
   direct all-odd compiler as a typed FCT input in the joint fibre (7.5).

The `24/24` compilation observation is therefore calibration only.  No
finite search, web access, or new certificate computation was used in these
proofs.
