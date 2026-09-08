# PBBS tower-coherent pin batching: exact interval rank, controller framing, and the sole asymptotic lemma

Date: 2026-07-28

Status: theorem-level unconditional compiler theorem, exact PBBS local
counterexample, and one explicitly isolated PBBS-specific asymptotic lemma.
No coefficient-one conclusion is claimed.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{n}{m},
 \qquad B=\frac{W}{n}=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
 \tag{0.1}
\]

where `A>0` is fixed.  The preceding run-occurrence theorem used a
label-preserving split parameter `kappa_H^T`.  That parameter is a useful
named-occurrence interface, but it is not the exact two-sided packet
parameter:

* it restricts physical letters to singleton run labels over one persistent
  core;
* row-dependent copies must obey the complete source-window/owner diamond
  poset, not only rows checked separately; and
* arbitrary nested word intervals need not be the fixed unit-shift windows
  of an erosion controller.

The exact minimal local quantity is the **cut-aware selected, pinned,
diamond-constrained interval Boolean excess**

\[
             \vartheta_H^\Diamond(Q,I;\mathcal F,\mathcal A,\mathscr C).
\]

Here `I` is the set of middle-owner starts credited to the chart,
`mathcal F` is its assigned target family, `mathcal A` is the family of
actual packets surviving in the final cut-aware chronology, and
`mathscr C` contains any required seam, endpoint, core-anchor, or
fixed-frame constraints.  The minimum is over a height-truncated cover by
actual two-sided packet occurrences, arbitrary bundled nonzero source
letters, and physical intervals respecting the entire tower/diamond poset.
Distinct credited middle owners give the intrinsic normalization

\[
 \boxed{\vartheta_H^\Diamond=L_{\min}-|I|\ge0.}
 \tag{0.2}
\]

For a fixed proposed interval layout, the common-pin kernel in Section 2 is
necessary and sufficient; thus this is an exact minimum, not merely a
certificate.  Requiring every available depth at every context start gives
a stronger all-start surrogate `theta_(H,all)^Diamond(Q)`.  If `Q` is the
forward `H`-halo of a base arc `I`, a valid named occurrence-copy
construction gives

\[
 \boxed{
 \vartheta_H^\Diamond(Q,I;\mathcal F,\mathcal A,\mathscr C)
 \le H+\theta_{H,\mathrm{all}}^\Diamond(Q)
 \le H+w(Q)+\kappa_H^\Diamond(Q).}
 \tag{0.3}
\]

The last display is a sufficient named-history construction, not an
identity.  The first minimum may be much smaller because it can choose one
occurrence of a repeated target and bundle several coordinates in one
letter.

If chart-credit sets partition all nonexceptional middle owners and their
assigned target families, together with one fallback, cover the required
depth-`H` band, concatenation gives the unconditional exact ledger

\[
 \boxed{
 L_H^T\le W+
       \sum_{j=1}^{R}\vartheta_{H,j}^\Diamond+f.}
 \tag{0.4}
\]

There is no additional `HR` in (0.4): every uncredited halo owner already
contributes to the chart excess.  Only after applying (0.3) does one obtain
the stronger surrogate

\[
 L_H^T\le W+HR+
       \sum_j\bigl(w(Q_j)+\kappa_H^\Diamond(Q_j)\bigr)+f.
 \tag{0.5}
\]

Consequently a genuinely tower-coherent one-mountain batching with

\[
 R=O_A(B+J/H),
 \qquad
 \sum_j\vartheta_{H,j}^\Diamond=O_A(HR),
 \qquad f=o_A(W),
 \tag{0.6}
\]

has length

\[
 W+O_A(HB+J)+o_A(W).
 \tag{0.7}
\]

In particular it is `W+o(W)` under the already proved numerical estimate
`J<=nu_H+B=O_A(BH)`.  This implication does **not** derive (0.6) from the
scalar seam count; (0.6) is a simultaneous tower-and-pin statement.

There are three exact tests.

1. Every canonical PBBS corridor packet is positive in the strongest
   sense: it has one fixed sliding-window frame, one neutral core cell, and
   is a literal erosion-controller pinning with all lower and upper towers
   nested.
2. Even an ideal FIFO one-mountain path can have linear **all-start**
   diamond-TCIBR.  Thus height-truncated target selection, rather than a
   full depth-`H` tower at every start, is part of the minimal interface.
3. The canonical three-root PBBS component gives a sharper negative test
   for named histories.  A forward `H`-halo containing a base of `2H+1`
   credited starts has occurrence-faithful excess `Omega(H^2)`, while its
   short-return packing is only `Theta(H)`.  The same component is
   impossible as a fixed depth-`H` erosion frame for `H>=3`.

The PBBS lower bound is occurrence-level: it uses private *run-occurrence*
addresses.  Separate runs of the same coordinate may be fused by an
unrestricted bundled chart, so it does not lower-bound
`vartheta_H^Diamond`.  Moreover the component has only `O(m)` owners and
may be put into an `o(W)` fallback.  It closes the named-split subroute
locally without proving an aggregate Catalan-scale obstruction.

After imposing the exact cut-aware occurrence ledger and the common pin
criterion, precisely one PBBS-specific statement remains.  It is
`PBBS--DTCB_A` in Section 7: an aggregate `o(W)` selected-cover bound for
the unrestricted bundled parameter.  No scalar consequence of `nu_H` is
substituted for that lemma.

## 1. The exact selected-cover diamond-TCIBR parameter

Let

\[
 Q=(X_0,X_1,\ldots,X_S),
 \qquad X_i\in\binom{\Omega}{r},
 \tag{1.1}
\]

be the **final** linear Johnson chronology after any cuts and
reconnections under consideration.  Let
`I subseteq {0,...,S}` be a set of credited starts for which the owners
`X_a`, `a in I`, are distinct.  For a source interval
`C=[a,b] subseteq [0,S]`, put

\[
 T_C^- =\bigcap_{t=a}^{b}X_t,
 \qquad
 T_C^+ =\bigcup_{t=a}^{b}X_t.
 \tag{1.2}
\]

A rooted packet occurrence `omega=(a,h)`, where
`0<=h<=min(H,S-a)`, consists of the occurrence-labelled rows

\[
 \{T^-_{[a,a+q]},T^+_{[a,a+q]}:0\le q\le h\}
 \quad\hbox{and}\quad
 \{X_{a},\ldots,X_{a+h}\}.
 \tag{1.3}
\]

Occurrence identity is retained: equal set values at different source
windows are not identified.  Identical occurrence nodes shared by two
selected packets are identified once.

Let `mathcal A` be the actual packet occurrences admissible in this final
chronology, and let `mathcal F` be the family of nonmiddle target values
assigned to the chart.  A **height-truncated tower cover** `Sigma` is a
finite subfamily of `mathcal A` such that

1. the owner row `X_a` is present for every credited `a in I`;
2. every value in `mathcal F` labels at least one row of a selected packet;
3. selecting height `h` retains both shores at every depth `0,...,h` and
   all constituent owner rows in (1.3).

Thus a selected target brings its actual two-sided prefix with it, but a
repeated target does not force every one of its occurrences or an
unneeded continuation to height `H`.

For every selected source interval `C` introduce physical word intervals
`J_C^-` and `J_C^+`, and for every selected owner introduce `J_t^0`.
The **source tower/diamond poset** consists of

\[
 \begin{aligned}
 C\subseteq D&\Longrightarrow
       J_D^-\subseteq J_C^-,\qquad J_C^+\subseteq J_D^+,\\
 t\in C&\Longrightarrow
       J_C^-\subseteq J_t^0\subseteq J_C^+,
 \end{aligned}
 \tag{1.4}
\]

with `J^-_[t,t]=J_t^0=J^+_[t,t]`.  These relations include the usual
same-root chains and every constituent-owner diamond; they also impose the
natural relation between nested source windows belonging to different
selected roots.

Let `mathscr C` be any further finite interval constraint system required
by the proposed literal construction.  It may prescribe fixed endpoints,
cell caps, core anchors, seam labels, or endpoint labels.  A **pinned
diamond chart** of length `L` consists of

* a height-truncated tower cover `Sigma`;
* intervals satisfying (1.4) and `mathscr C`; and
* nonempty letters `A_0,...,A_(L-1) subseteq Omega`

such that

\[
 \bigcup_{p\in J_C^-}A_p=T_C^-,
 \qquad
 \bigcup_{p\in J_t^0}A_p=X_t,
 \qquad
 \bigcup_{p\in J_C^+}A_p=T_C^+,
 \tag{1.5}
\]

and every additional pin in `mathscr C` has its prescribed OR value.
Define the selected, pinned, diamond-constrained interval Boolean rank by

\[
 \operatorname {dtibr}_H^Diamond
       (Q,I;\mathcal F,\mathcal A,\mathscr C)
 =\min L,
 \tag{1.6}
\]

where the minimum is also over the selected cover and interval layout, and
is infinity if no chart exists.  Its exact credited-owner excess is

\[
 \vartheta_H^\Diamond
       (Q,I;\mathcal F,\mathcal A,\mathscr C)
 =\operatorname {dtibr}_H^\Diamond-|I|.
 \tag{1.7}
\]

This is the strongest minimal parameter for the present interface:
"strongest" means that the full selected source poset and all literal pins
are imposed; "minimal" means that packet occurrence, selected height,
interval layout, and arbitrary bundled letters are all optimized.

When every available packet `(a,min(H,S-a))` is forced for every start,
there are no extra constraints, and all records are admissible, write

\[
 \theta_{H,\mathrm{all}}^\Diamond(Q)
 =L_{H,\mathrm{all}}^\Diamond(Q)-(S+1).
 \tag{1.8}
\]

### Lemma 1.1 (nonnegative exact normalization)

Every finite pinned diamond chart satisfies

\[
 \operatorname {dtibr}_H^\Diamond
       (Q,I;\mathcal F,\mathcal A,\mathscr C)\ge |I|.
 \tag{1.9}
\]

Hence `vartheta_H^Diamond>=0`; in particular
`theta_(H,all)^Diamond>=0`.

#### Proof

Choose `J_a^0` for every credited owner.  Two line intervals with a common
left endpoint are nested.  Their OR values are then comparable by
inclusion, so two distinct values of the same cardinality cannot share that
endpoint.  The `|I|` distinct rank-`r` owners require `|I|` distinct left
endpoints.  Thus `L>=|I|`.  The same argument works with right endpoints.
\(\square\)

### Definition 1.2 (history-induced refinement)

There is a stricter occurrence-provenance version.  Give every output cell
`p` one chronological activity interval `R_p subseteq [0,S]`.  For every
source window `C`, require the three physical supports

\[
 \{p:C\subseteq R_p\},\qquad
 \{p:t\in R_p\},\qquad
 \{p:R_p\cap C\ne\varnothing\}
 \tag{1.10}
\]

to be word intervals for the lower row, an owner `t in C`, and the upper
row respectively.  With maximal cell label

\[
                         A_p=\bigcap_{t\in R_p}X_t,
 \tag{1.11}
\]

the common positive-hit conditions of Section 2 decide exact equality.
This **history-DTCIBR** automatically satisfies (1.4) and prevents one
physical copy from switching histories between rows.  It is, however,
strictly stronger than arbitrary diamond-TCIBR.  A named singleton
run-occurrence split is a further restriction.  Consequently

\[
 \operatorname {IBR}
 \ \le\ \operatorname {dtibr}^\Diamond
 \ \le\ \operatorname {dtibr}^{\mathrm{hist}}
 \ \le\ \hbox{any valid named-split construction length}.
 \tag{1.12}
\]

The exact global theorem below uses the first nontrivial quantity in
(1.12), not the occurrence-restricted surrogates.

## 2. One common word: the exact pin criterion

For a proposed finite tower chart, temporarily forget the letters and keep
only a family of labelled intervals

\[
                         \Pi=\{(I_c,S_c)\}_c.
 \tag{2.1}
\]

It includes all intervals in (1.3) and may also include seam, endpoint,
fallback, or protected-occurrence pins.  For every coordinate `x`, define

\[
 Q_x(\Pi)=[0,L-1]\setminus
   \bigcup_{c:\,x\notin S_c}I_c.
 \tag{2.2}
\]

### Theorem 2.1 (arbitrary-frame common-pin criterion)

One nonzero word of length `L` realizes every exact pin in `Pi` if and only
if

\[
 Q_x(\Pi)\cap I_c\ne\varnothing
 \qquad(c,\ x\in S_c),
 \tag{2.3}
\]

and

\[
 \{x:p\in Q_x(\Pi)\}\ne\varnothing
 \qquad(0\le p<L).
 \tag{2.4}
\]

When these conditions hold, the coordinatewise maximal word

\[
                         A_p=\{x:p\in Q_x(\Pi)\}
 \tag{2.5}
\]

realizes all pins simultaneously.

#### Proof

If `x` is absent from `S_c`, it must be absent throughout `I_c`, which gives
the forbidden union in (2.2).  If `x` belongs to `S_c`, it must occur at
least once in `I_c`, giving (2.3).  Nonzero letters give (2.4).

Conversely, (2.5) excludes every negative coordinate from every pin.
Condition (2.3) supplies every positive coordinate somewhere in its pin
interval, and (2.4) makes each source letter nonempty.  Therefore the OR on
`I_c` is exactly `S_c` for every `c`.  \(\square\)

Theorem 2.1 is the common quantifier missing from independent row
consecutive-ones tests.  A family of row-dependent split assignments is
valid only after its complete physical intervals are put into one `Pi` and
pass (2.3)--(2.4).

## 3. Relation to run-occurrence splitting

For the path (1.1), put

\[
 K(Q)=\bigcap_{t=0}^{S}X_t,
 \qquad
 w(Q)=|X_0\setminus K(Q)|.
 \tag{3.1}
\]

Split each coordinate indicator into maximal positive run occurrences.
There are exactly

\[
                         S+w(Q)
 \tag{3.2}
\]

noncore occurrences.  The split parameter `kappa_H^T(Q)` from
`THREAD_K_PBBS_RUN_OCCURRENCE_BATCHING_AND_TWO_PORT_DIAMOND_GATE_20260728.md`
allows repeated columns carrying one named occurrence and neutral columns
carrying `K`.  Its original tower requirement is only the same-root chain.

Define its **diamond refinement** `kappa_H^Diamond(Q)` by additionally
requiring all selected source-window relations in (1.4).  The cost
normalization is unchanged: added named-occurrence copies plus all but the
first neutral core column.  Thus

\[
                 \kappa_H^\Diamond(Q)\ge\kappa_H^T(Q).
 \tag{3.3}
\]

### Theorem 3.1 (named histories upper-bound exact diamond rank)

If `K(Q)` is nonempty, then

\[
 \boxed{
 L_{H,\mathrm{all}}^\Diamond(Q)
 \le S+w(Q)+\kappa_H^\Diamond(Q)+1,\qquad
 \theta_{H,\mathrm{all}}^\Diamond(Q)
 \le w(Q)+\kappa_H^\Diamond(Q).}
 \tag{3.4}
\]

If `Q` is the forward `H`-halo of a base-start set `I`, then every target
assignment covered by the all-start chart satisfies

\[
 \boxed{
 \vartheta_H^\Diamond(Q,I;\mathcal F,\mathcal A,\mathscr C)
 \le H+\theta_{H,\mathrm{all}}^\Diamond(Q)
 \le H+w(Q)+\kappa_H^\Diamond(Q).}
 \tag{3.5}
\]

Here (3.5) assumes that the named split realizes every additional
constraint in `mathscr C` and that its packets are admissible in
`mathcal A`.

#### Proof

Take a minimum diamond-coherent named split.  Emit `K union {x}` for every
copy of a run occurrence of coordinate `x`, and emit `K` for every neutral
column, in their common order.  Every selected row is an interval, contains
exactly its prescribed outside-`K` occurrences, and contains only neutral
extra columns.  Its OR is therefore its label.  The copywise inclusions are
precisely (1.4).

There are `S+w` original occurrence columns.  By the normalization of
`kappa_H^Diamond`, all added occurrence and neutral columns contribute
`kappa_H^Diamond+1`.  This proves the first inequality.  Subtract `S+1` to obtain
the second.  The all-start chart is an admissible selector chart.  A forward
halo has `S+1=|I|+H`, so subtracting the charged baseline `|I|` gives (3.5).
\(\square\)

The inequalities can be strict because `vartheta_H^Diamond` permits
arbitrary bundled letters and optimizes the packet cover.  Conversely, a
finite exact selector excess need not give a small singleton-copy split
parameter.

A run-occurrence one-mountain order proves only the ordinary support fact
`kappa_H=0`.  It does not force `kappa_H^Diamond=0`; neutral-core placement,
tower alignment, and cross-root diamonds remain real constraints.  Thus a
valid named-history sufficient hypothesis is

\[
                         w(Q)+\kappa_H^\Diamond(Q)=O(H),
 \tag{3.6}
\]

or, more sharply, `vartheta_H^Diamond=O(H)`.

### Proposition 3.2 (all-start towers are not the minimal interface)

Let `K` be nonempty, let `a_0,...,a_(S+H-1)` be distinct, and put

\[
 X_i=K\cup\{a_i,a_{i+1},\ldots,a_{i+H-1}\},
 \qquad0\le i\le S,
 \tag{3.7}
\]

where `S>=H`.  This is a FIFO one-mountain Johnson path.  Put

\[
                         N=S-H+1.
 \tag{3.8}
\]

The subsystem consisting, for `0<=i<N`, of the final two lower nodes in
the height-`H` packet has exact unrestricted diamond interval rank

\[
 \boxed{
                 N+\left\lceil\frac N2\right\rceil.}
 \tag{3.9}
\]

Consequently the forced all-start chart obeys

\[
 \boxed{
 \theta_{H,\mathrm{all}}^\Diamond(Q)
 \ge \left\lceil\frac{S-H+1}{2}\right\rceil-H.}
 \tag{3.10}
\]

In particular it is linear in `S` when, for example, `S/H` tends to
infinity, despite perfect FIFO one-mountain support.

#### Proof

For every `0<=i<N`, the depth-`H` lower target is `K`, while the
depth-`H-1` lower target is

\[
                         K\cup\{a_{i+H-1}\}.
 \tag{3.11}
\]

In any realizing word, call a position **core-pure** if its letter is a
subset of `K`.  Each selected `K` interval lies in one maximal core-pure
component.  Its parent interval in (3.11) must reach a position containing
the private coordinate `a_(i+H-1)` without crossing any position containing
a different outside-`K` coordinate.  It therefore uses one of the two
shores of that core-pure component.  One component serves at most two of
the `N` distinct parents.  Moreover the `N` private outside coordinates
need `N` distinct positions.  Hence every realization has at least
`N+ceil(N/2)` positions.

Conversely, pair the parents and use the three-cell blocks

\[
 K\cup\{a_u\},\quad K,\quad K\cup\{a_v\},
 \tag{3.12}
\]

with the evident two nested intervals; use a two-cell block for an unpaired
parent.  This proves (3.9).  Since the full chart has baseline `S+1`, (3.10)
follows.  \(\square\)

The repeated value `K` needs only one selected occurrence when the target
cover, rather than every source start, is the object.  Proposition 3.2 is
therefore an exact reason to minimize over height-truncated packet covers.

## 4. Unconditional global tower-batching theorem

Let `P` be a disjoint union of oriented owner cycles containing all `W`
distinct middle owners.  After rooting the relevant pieces and making any
literal cuts/reconnections, take `R` regular charts.  Chart `j` has final
chronology `Q_j`, a credit set `I_j`, assigned nonmiddle target family
`mathcal F_j`, admissible packet family `mathcal A_j`, and constraint system
`mathscr C_j`.  Require the credit sets to be disjoint.  Let `E` be the set
of uncredited middle owners, so

\[
                    \sum_{j=1}^{R}|I_j|+|E|=W.
 \tag{4.1}
\]

Assume a fallback word of total length `|E|+f` represents every owner in
`E` and its assigned target family with all required tower and pin
constraints.  Assume, finally, that the regular assigned families and the
fallback collectively cover every target value in the required lower and
upper depth-`H` band.  Duplicate target occurrences need not all be kept.

### Theorem 4.1 (exact selected-cover tower batching)

Under these hypotheses there is one nonzero literal word covering every
required target and every middle owner, of length

\[
 \boxed{
 L_H^T(P)\le W+
       \sum_{j=1}^{R}\vartheta_H^\Diamond
        (Q_j,I_j;\mathcal F_j,\mathcal A_j,\mathscr C_j)+f.}
 \tag{4.2}
\]

#### Proof

Choose a minimum pinned diamond chart for each regular index.  Its length is

\[
 |I_j|+\vartheta_H^\Diamond
        (Q_j,I_j;\mathcal F_j,\mathcal A_j,\mathscr C_j).
 \tag{4.3}
\]

Concatenate these words with the fallback word.  Every witness interval is
internal to one constituent chart and is unchanged by concatenation.  The
cover hypothesis supplies every required nonmiddle value; the credit and
fallback sets supply every middle owner.  Summing (4.3), using (4.1), and
adding `|E|+f` gives (4.2).  \(\square\)

The exact ledger (4.2) contains no separate halo term.  A context owner
which is not credited to its chart is physically represented there anyway,
and that duplicate is already included in `vartheta_H^Diamond`.

### Corollary 4.2 (all-start named-history surrogate)

Suppose `I_j` is a consecutive base arc of `s_j` starts and `Q_j` is its
forward `H`-halo, so `Q_j` has `s_j+H` owners.  If a valid named-history
split for `Q_j` has width `w(Q_j)` and diamond split excess
`kappa_H^Diamond(Q_j)`, then

\[
 \boxed{
 L_H^T(P)\le W+HR+
   \sum_{j=1}^{R}\bigl(w(Q_j)+\kappa_H^\Diamond(Q_j)\bigr)+f.}
 \tag{4.4}
\]

#### Proof

Theorem 3.1 gives

\[
 \vartheta_{H,j}^\Diamond
 \le H+w(Q_j)+\kappa_H^\Diamond(Q_j).
\]

Sum this inequality in (4.2).  \(\square\)

### Corollary 4.3 (tower-coherent one-mountain compiler)

Suppose a literal one-mountain atlas has a residence cut set of size `J`, a
batch size `b`, and selected pinned charts satisfying

\[
 R\le C_A\left(B+\frac{J}{b}\right),
 \qquad
 \sum_{j=1}^{R}\vartheta_{H,j}^\Diamond\le C_AHR,
 \qquad f=o_A(W).
 \tag{4.5}
\]

Then

\[
 L_H^T(P_m)
 \le W+O_A\left(HB+\frac{HJ}{b}\right)+o_A(W).
 \tag{4.6}
\]

If `b>=c_AH`, `J<=nu_H(P_m)+B`, and
`nu_H(P_m)=O_A(BH)`, this is `W+o_A(W)`.

#### Proof

Insert (4.5) into Theorem 4.1.  Since

\[
 HR=O_A\left(HB+\frac{HJ}{b}\right),
\]

the first assertion follows.  If `b>=c_AH` and `J=O_A(BH)`, the excess is
`O_A(BH)`.  Finally

\[
 W=(2m+1)B=\Theta_A(BH^2),
\]

so `BH=o_A(W)`.  \(\square\)

Corollary 4.3 is an unconditional implication, not an assertion that
scalar cut indices generate the charts in (4.5).  Ordinary one-mountain
support proves only `kappa_H=0`; the selected full tower poset and common
pin feasibility are additional hypotheses.

## 5. Exact reconciliation with erosion controllers

The tower parameter above allows arbitrary nested intervals.  The exact
erosion-controller normal form is a strict framed specialization.

Let

\[
 T=(T_0,\ldots,T_{v-1})
 \tag{5.1}
\]

be a rank-`r` path, and let `d>=1`.  A **depth-`d` framed chart** has a word

\[
 A=(A_0,\ldots,A_{v+d-1})
\]

whose central intervals are fixed by

\[
 J_i^0=[i,i+d],
 \qquad
 \bigcup_{p=i}^{i+d}A_p=T_i.
 \tag{5.2}
\]

The natural two-sided frames are

\[
 J^-_{i,q}=[i+q,i+d],
 \qquad
 J^+_{i,q}=[i,i+d+q].
 \tag{5.3}
\]

Whenever their labels are exact, these intervals satisfy (1.4).  Moreover,

\[
 \bigcup_{p\in J^+_{i,q}}A_p
 =\bigcup_{h=0}^{q}T_{i+h}
 \tag{5.4}
\]

automatically, while a desired lower equality

\[
 \bigcup_{p\in J^-_{i,q}}A_p
 =\bigcap_{h=0}^{q}T_{i+h}
 \tag{5.5}
\]

is an additional physical pin.

Define the maximal erosion controller

\[
 P_p=\bigcap_{\substack{0\le i<v\\i\le p\le i+d}}T_i,
 \qquad0\le p<v+d.
 \tag{5.6}
\]

### Theorem 5.1 (framed charts are exactly controller pinnings)

For a resident Johnson path `T`, a nonzero framed chart realizing a
specified family of lower, seam, and boundary pins exists if and only if
the corresponding controller-position sets `H_x={p:x in A_p}` satisfy:

1. on each internal maximal `x`-run `[u,v]` in `P`, the endpoints `u,v`
   are selected and consecutive selected positions have gap at most `d+1`,
   with the exact one-sided boundary version;
2. every extra negative and positive pin passes (2.2)--(2.3); and
3. every physical position is selected by at least one coordinate.

Equivalently, these are CP1--CP3 of the erosion-controller formulation.
Every feasible framed chart is a tower chart.  The converse is false in
general.

#### Proof

The central pins (5.2) force `A_p subseteq P_p`.  A selected occurrence of
coordinate `x` at source position `p` covers precisely the middle indices
`[p-d,p]`.  These intervals cover one carrier run exactly when the eroded
controller run contains both endpoint pins and consecutive pins have gap at
most `d+1`; this is CP1.

All additional exact interval labels are pins in the common system of
Theorem 2.1, giving CP2.  Condition (2.4) is CP3.  Conversely CP1 gives all
central equalities, CP2 gives every extra pin, and CP3 gives a nonzero word.
Equations (5.3) then give nested tower intervals.  \(\square\)

The distinction is structural.  Adding an occurrence-copy column to an
arbitrary tower chart can change interval lengths and endpoint increments;
it need not preserve (5.2).  Controller pins choose coordinate membership
inside already fixed source positions and do not carry an additive
one-letter-per-pin cost.  Thus `kappa_H^T`, `theta_H^T`, and controller-pin
feasibility must not be identified numerically.

## 6. Cut-aware occurrence selection and exact PBBS tests

Suppose a decorated braid `Gamma` cuts or reconnects source PBBS pieces.
For a signed target `S`, let `O^sigma(S)` be its recorded old occurrence
family with complete supports, `C_Gamma` the actual disruption set, and
`N_Gamma^sigma(S)` the audited new seam-crossing occurrences.  On the lower
side retain only depths `1<=q<=H`.  The exact surviving-occurrence budget is

\[
 \beta_\Gamma^\sigma(S)=
 \#\{o\in\mathcal O^\sigma(S):
       \operatorname {supp}(o)\cap C_\Gamma=\varnothing\}
 +\#\mathcal N_\Gamma^\sigma(S)-1.
 \tag{6.1}
\]

A multi-seam window is counted once.  The inequality
`beta_Gamma^sigma(S)>=0` says only that at least one final occurrence is
available.  It does not choose occurrences whose physical intervals form
the towers (1.4), and it does not imply the common-pin criterion
(2.3)--(2.4).  A cut-aware tower atlas must therefore:

1. select concrete surviving or new occurrences from (6.1);
2. retain the whole tower at every declared regular start, or explicitly
   charge its missing rows to the fallback; and
3. feed all selected lower, central, seam, and endpoint intervals into one
   pin system.

An overlapping-halo partition of the unchanged chronology is not itself a
physical cut: it destroys no old occurrence, and (6.1) is then unnecessary.
The cut-aware ledger becomes mandatory when cuts, reversals, trimming, or
reconnections are used to reduce the physical block count.

### Proposition 6.1 (positive PBBS corridor test)

For every canonical depth-`q` PBBS corridor packet, put

\[
 X_t=K\cup\{A_t,\ldots,A_{q-1}\}
       \cup\{C_{q-t},\ldots,C_{q-1}\},
 \qquad0\le t\le q.
 \tag{6.2}
\]

The word

\[
 \begin{aligned}
 &K\cup\{A_0\},\ldots,K\cup\{A_{q-1}\},K,\\
 &K\cup\{C_{q-1}\},\ldots,K\cup\{C_0\}
 \end{aligned}
 \tag{6.3}
\]

has length `2q+1`, satisfies `D^qA=(X_0,...,X_q)`, and realizes the complete
two-sided corridor towers in the framed intervals (5.3).  In particular it
is one common controller pinning, not a collection of row-dependent
witnesses.

#### Proof

In the `2q` noncore atom positions, `X_t` occupies the interval
`[t,t+q-1]`.  Insert the neutral `K` cell between atom positions `q-1` and
`q`.  The `q+1`-cell window beginning at `t` is then exactly `X_t`, proving
`D^qA=X`.

For a window `[a,b]` of owners, its lower and upper atom supports are

\[
                         [b,a+q-1],
 \qquad
                         [a,b+q-1],
 \tag{6.4}
\]

with the lower interval allowed to be empty.  Every nonempty support touches
one of the two atom positions adjacent to `K`; adjoining the `K` cell gives
exactly the framed intervals (5.3).  The empty full-packet erosion is the
`K` cell alone.  \(\square\)

### Proposition 6.2 (sharp unmodified-PBBS counterexample)

For every `m>=4`, the canonical PBBS three-root component of length
`3(2m+1)` contains the six consecutive owners

\[
 \begin{array}{lll}
 K\cup0124,&K\cup014z,&K\cup034z,\\
 K\cup234z,&K\cup123z,&K\cup125z,
 \end{array}
 \tag{6.5}
\]

where `z=2m` and `K={6,8,...,2m-2}`.  It has the following two exact
failures.

1. The three depth-two lower rows are

   \[
   K\cup\{z,4\},\qquad K\cup\{z,3\},\qquad
   K\cup\{z,2\}.
   \tag{6.6}
   \]

   Hence the one-copy occurrence interface is the three-spoke star and has
   `kappa_2^T>=kappa_2>=1`.
2. Coordinate `3` has an internal maximal owner run of length exactly
   three, namely owners `2,3,4` in (6.5).  Therefore the unchanged component
   has no framed depth-`d` preimage for any `d>=3`.

The motif occurs in `2m+1` coordinate translates, once every three
projected starts.  Nevertheless the whole component has only `O(m)` owners.

#### Proof

The intersections in (6.6) are read directly from (6.5).  After deleting
the fixed core, their occurrence supports are `{z,4},{z,3},{z,2}`.  One
copy of `z` would need three neighbours in a line, proving the first claim.

In (6.5), coordinate `3` is absent from owners `0,1`, present in owners
`2,3,4`, and absent from owner `5`.  Thus this is an internal maximal run of
length three.  Exact depth-`d` residence requires every internal run to have
length at least `d+1`, so a framed preimage is impossible for `d>=3`.
The translate count is the exact three-root voltage calculation
`lambda_(t+6)=lambda_t+2 mod (2m+1)`.  \(\square\)

Proposition 6.2 is sharp in scope.  It proves that canonical PBBS does not
satisfy a universal zero-split or uncut-controller theorem.  Cutting or
rethreading can expose or merge these runs, and the component's polynomial
mass can be sent to an `o(W)` fallback.  It supplies no Catalan-density lower
bound on `theta_H^T`.

## 7. The single missing PBBS-specific lemma

For a decorated PBBS atlas `Gamma`, define its **tower-coherent batching
cost** by

\[
 \mathfrak A_H(\Gamma)=
 HR_\Gamma+
 \sum_{j=1}^{R_\Gamma}\theta_H^T(Q_j)+f_\Gamma,
 \tag{7.1}
\]

provided that

* every chart uses a concrete cut-aware occurrence selection as in Section
  6;
* all its selected intervals pass the one common pin criterion of Section
  2 (and CP1--CP3 when the framed erosion architecture is claimed); and
* the exceptional/fallback chart has excess `f_Gamma` and supplies every
  occurrence not assigned to a regular chart.

Set the cost to infinity if any condition fails.  Minimize over all literal
PBBS atlases allowed by the chosen unchanged-piece/reconnection lane:

\[
                         \mathfrak A_H(P_m)
 =\min_\Gamma\mathfrak A_H(\Gamma).
 \tag{7.2}
\]

Theorem 4.1 proves unconditionally that the central-band word length is at
most

\[
                         W+\mathfrak A_H(P_m).
 \tag{7.3}
\]

All remaining PBBS content in this lane is exactly the following one lemma.

> **PBBS--TCB_A (cut-aware tower-coherent batching lemma).**  For every
> fixed `A>0`, with `H=ceil(A sqrt(m))`,
> \[
>                         \boxed{\mathfrak A_H(P_m)=o_A(W).}
> \tag{7.4}
> \]
> Equivalently, there are concrete cut-aware PBBS charts for which the
> block-frame charge, exact minimal tower excess, and exceptional fallback
> have aggregate `o_A(W)`, with all selected pins realized by one common
> word in each chart.

In the one-mountain occurrence-copy subroute, a sufficient certificate for
this single lemma is

\[
 R=O_A(B+J/H),
 \qquad
 \sum_j\bigl(w(Q_j)+\kappa_H^T(Q_j)\bigr)=O_A(HR),
 \qquad
 f_\Gamma=o_A(W),
 \tag{7.5}
\]

together with the cut-aware selection and common-pin conditions already
built into (7.1).  Equation (7.5) without those occurrence and pin
conditions is not `PBBS--TCB_A`.

The known scalar facts

\[
 J\le\nu_H(P_m)+B,
 \qquad
 \nu_H(P_m)=O_A(BH)
 \tag{7.6}
\]

control only the possible number of batches.  They do not imply (7.4), do
not choose a protected occurrence, and do not solve one common controller
pinning.  Thus no coefficient-one claim follows here.

## 8. Proved boundary

The following statements are unconditional.

1. `theta_H^T` is the exact minimal unrestricted bundled-letter parameter
   for a complete nested tower chart.
2. The common-pin criterion (2.3)--(2.4) is necessary and sufficient for
   every proposed chart.
3. Tower-coherent occurrence splitting gives the certified upper bound
   (3.3), but is not the exact minimal parameter.
4. Global halo concatenation has the exact ledger (4.3), and the corrected
   one-mountain quantitative implication is Corollary 4.2.
5. Fixed sliding frames specialize to the erosion controller and are
   equivalent to CP1--CP3; arbitrary tower charts need not be framed.
6. Cut-aware occurrence survival and common-word feasibility are separate
   conditions.
7. Canonical PBBS corridor packets pass the framed tower test exactly.
8. The canonical three-root component refutes universal zero-charge and
   uncut framed-controller assertions, but only on polynomial mass.

The report contains exactly one unproved PBBS-specific statement:
`PBBS--TCB_A`, equation (7.4).
