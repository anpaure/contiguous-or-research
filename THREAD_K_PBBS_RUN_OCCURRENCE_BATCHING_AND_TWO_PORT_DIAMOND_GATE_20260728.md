# PBBS run-occurrence batching, the six-owner star, and the two-port diamond gate

Date: 2026-07-28

Status: theorem-level advance, independently audited exact scoped
obstruction, and finite calibration.  The universal assertion that every
canonical PBBS halo is one-mountain is false.  The obstruction proved here
has only polynomial mass, so an aggregate coefficient-one batching theorem
is not disproved.  No coefficient-one conclusion is claimed.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil .
\]

This note resolves four parts of the PBBS-specific batching question.

1.  The single-run hypothesis in the first one-mountain compiler was
    unnecessary.  Split every coordinate word into its maximal positive
    **run occurrences**, and emit the same singleton letter once for each
    occurrence.  If the run-exit sequence is one-mountain, the exact word
    length is still

    \[
       S+w+1,
    \]

    for an `S`-transition path, where
    `w=|X_0\setminus\bigcap_tX_t|`.  Repeated coordinates create repeated
    letters, which are legal because OR is idempotent.  In particular the
    old `S<=m` ceiling applies only to the distinct-coordinate specialization
    and is not a ceiling for literal batching.  More generally, if
    `kappa_H^T(Q)` is the minimum **tower-coherent** occurrence-copy and
    neutral-core excess making all depth-`H` lower and upper rows consecutive
    in their original nested chains, the tower-preserving construction has
    exact length

    \[
                         S+w+\kappa_H^T(Q)+1.
    \]

2.  Every canonical PBBS all-depth corridor packet from Section 21 of
    `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` is an exact FIFO packet.
    A depth-`q` packet has persistent core `m+1-q`, active width `q`, and
    a literal two-sided compiler of length `2q+1`.  Thus PBBS has a large
    supply of root-scale flag-coherent packets.  Their width equals their
    depth, however, so simply replacing `q` by `H^2` does not compress
    `H` seams.

3.  Universal unmodified batching is false.  In the genuine PBBS
    three-root component of length `3n`, after relabelling there are six
    consecutive projected owners

    \[
    \begin{array}{lll}
    K\cup0124,&K\cup014z,&K\cup034z,\\
    K\cup234z,&K\cup123z,&K\cup125z,
    \end{array}
    \tag{0.1}
    \]

    where `z=2m` and `K={6,8,...,2m-2}`.  The indicated positive runs

    \[
       z:[1,5],\qquad 3:[2,4],\qquad
       \text{second }2:[3,5]
    \tag{0.2}
    \]

    form a strict valley `5,4,5`.  Moreover the three correct lower
    three-owner flags are the three-spoke star

    \[
       K\cup\{z,4\},\quad K\cup\{z,3\},\quad
       K\cup\{z,2\}.
    \tag{0.3}
    \]

    The motif starts every three projected transitions.  Hence every
    seven-transition arc of that component contains one, in either global
    orientation.  No nonempty forward `H`-halo on this component is
    one-mountain once `H>=7`.  Even an arbitrary unsplit
    occurrence-faithful order of the canonical run atoms cannot realize
    (0.3), because the unique center atom would need three neighbours in a
    line.  Splitting that center once repairs the local star, so this is a
    unit splitting charge, not an `Omega(H)` local lower bound and not an
    obstruction to unrestricted bundled letters.

4.  The new depth-three transition-system theorem needs a two-sided
    extension before it can preserve the lower and upper flag towers.
    An edge copy incident with an owner `A` has two ports `(x,y)`: the
    lower deleted port `x in A` and upper outside port `y notin A`.
    Pairing copies `(x,y),(x',y')` is rank-safe on both shores exactly when

    \[
                    x\ne x',\qquad y\ne y'.
    \tag{0.4}
    \]

    The cited theorem imposes only the first inequality because its
    displayed depth-three row is the lower row.  A `2x2` opposed port
    rectangle gives two safe old pairs but no two-sided-safe cross-pairing,
    so its component-joining switch cannot be imported verbatim.

The obstruction in (0.1) has only `O(m)` owners and can be handled by the
old collar at cost `O(Hm)=o(W)`.  The still-live theorem is aggregate:
discard a family with total fallback charge `o(W)`, and partition the
remainder into `H`-halos controlled by the split-column compiler, with

\[
 R=O_A\!\left(B+\frac{J}{H}\right),\qquad
 \sum_j\bigl(w_j+\kappa_H^T(Q_j)\bigr)=O_A(HR),
 \tag{0.5}
\]

where `J<=nu_H+B` is a short-residence cut set.  The generalized compiler
would then give

\[
 L_H\le W+O_A(HB+J)+o(W)=W+o(W)
 \tag{0.6}
\]

from the existing critical estimate `nu_H=O_A(BH)`.  Neither (0.5) nor a
Catalan-density obstruction to it is proved here.

## 1. Exact PBBS arc dictionary

Let

\[
 A_0,A_1,\ldots
\]

be an oriented canonical PBBS odd-graph component, and let `lambda_i` be
the coordinate omitted by the edge `A_iA_(i+1)`.  The audited recurrence is

\[
 A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.
 \tag{1.1}
\]

Fix one step-two phase `p` and complement.  For

\[
 X_t=[n]\setminus A_{p+2t}
\]

we have the directed Johnson transition

\[
 \boxed{
 X_{t+1}=X_t-\{d_t\}+\{e_t\},\qquad
 d_t=\lambda_{p+2t},\quad e_t=\lambda_{p+2t+1}.}
 \tag{1.2}
\]

Thus the complete coordinate-run data of a canonical owner arc are read
directly from the alternating deletion/insertion ports of the omitted-label
word.  No Dyck quotient information is lost in (1.2); the quotient is a
compact way to generate this word.

For a linear arc `Q=(X_0,...,X_S)`, put

\[
 K(Q)=\bigcap_{t=0}^{S}X_t,
 \qquad w(Q)=|X_0\setminus K(Q)|.
 \tag{1.3}
\]

Every coordinate indicator on `[0,S]` is a disjoint union of maximal
positive intervals.  Call these intervals **run occurrences**.  Omit the
full intervals `[0,S]`, whose coordinates are precisely `K(Q)`.  For a
remaining occurrence `rho`, write

\[
 x(\rho)\in[n],\qquad I_\rho=[l_\rho,r_\rho].
 \tag{1.4}
\]

The labels `x(rho)` need not be distinct.

### Lemma 1.1 (exact occurrence count)

The number `N(Q)` of noncore run occurrences is

\[
                     \boxed{N(Q)=S+w(Q).}
 \tag{1.5}
\]

#### Proof

Exactly `w(Q)` noncore positive runs are already active at time zero.  At
each of the `S` Johnson transitions exactly one coordinate is inserted, and
that insertion starts exactly one new maximal positive run.  Conversely,
every positive run begins either at time zero or at one of these insertions.
The same coordinate may contribute several runs, but each such run has its
own insertion event.  Hence the count is `w+S`.  \(\square\)

The identity (1.5), not distinctness of the coordinate labels, is the
quantity used by the literal word ledger.

## 2. The generalized run-occurrence compiler

Order the occurrences by nondecreasing start `l_rho`.  Starts after zero
are distinct; the occurrences active at zero may be put in an arbitrary
tie order.  Say that this total order is **one-mountain** if

\[
 \boxed{
   \{i:r_i\ge t\}\text{ is an integer interval for every }t.}
 \tag{2.1}
\]

Equivalently,

\[
 r_j\ge\min(r_i,r_k)\qquad(i<j<k).
 \tag{2.2}
\]

With distinct exit values this is the permutation class avoiding `213`
and `312`.  A strict valley is therefore a hereditary certificate against
the prescribed start order.

### Theorem 2.1 (run-occurrence one-mountain compiler)

Let `Q=(X_0,...,X_S)` be any directed Johnson path with `K(Q) nonempty`.
If its noncore run occurrences admit a one-mountain start order

\[
 \rho_1,\ldots,\rho_N,
\]

then the nonzero word

\[
 K\cup\{x(\rho_1)\},\ldots,
 K\cup\{x(\rho_N)\},K
 \tag{2.3}
\]

represents every consecutive intersection and every consecutive union of
owners in `Q`.  Its exact length is

\[
                    \boxed{S+w(Q)+1.}
 \tag{2.4}
\]

Repeated occurrences of one coordinate give repeated letters in (2.3).

#### Proof

For an owner window `[a,b]`, a run occurrence contributes to the total
intersection exactly when

\[
                      l_\rho\le a,\qquad r_\rho\ge b.
 \tag{2.5}
\]

The first condition is a prefix of the start order and, by (2.1), the
second is an interval.  Their intersection is an interval of occurrence
indices.  OR-ing the corresponding consecutive letters gives `K` together
with exactly the coordinates having a positive run covering `[a,b]`, which
is `intersection_(t=a)^b X_t`.  Two different occurrences of the same
coordinate cannot both cover one connected window, but distinctness is not
needed.

A run occurrence contributes to the total union exactly when it meets the
window, equivalently

\[
                      l_\rho\le b,\qquad r_\rho\ge a.
 \tag{2.6}
\]

Again the selected occurrence indices form a prefix intersected with an
interval.  Several selected occurrences may have the same coordinate
label; idempotence of OR collapses them to that one coordinate, giving
exactly `union_(t=a)^b X_t`.  If the selected occurrence interval is empty,
the final `K` letter supplies the target.  Lemma 1.1 gives (2.4), and every
letter is nonzero because `K` is nonempty.  \(\square\)

### Corollary 2.2 (the old span ceiling is not intrinsic)

The bound `S<=m` in the distinct-coordinate specialization does not hold
for Theorem 2.1.  A coordinate may leave and re-enter many times, producing
several identical singleton atoms; (2.4) still charges only one baseline
letter per transition and only `w` excess letters.  Therefore a root-scale
carrier of arbitrarily large `S` is not excluded by alphabet size.

### 2.3 The occurrence matrix and column splitting

For a depth cutoff `H`, form the binary run-occurrence matrix
`M_H(Q)`.  Its columns are the noncore run occurrences.  For every
`0<=a<=b<=S` with `b-a<=H`, it has the two rows

\[
 \begin{aligned}
 R^-_{a,b}&=\{\rho:[a,b]\subseteq I_\rho\},\\
 R^+_{a,b}&=\{\rho:I_\rho\cap[a,b]\ne\varnothing\}.
 \end{aligned}
 \tag{2.7}
\]

The OR of the labels in these rows, together with `K`, is the corresponding
lower or upper target.

A **label-preserving split** replaces an occurrence column `rho` by one or
more columns carrying the same coordinate label `x(rho)`.  Every row which
used `rho` is assigned to at least one of its copies, while a row which did
not use `rho` is assigned none.  After all assignments, the complete `1`-set
of every split row, not merely a subset of it, must be one interval in the
common column order.  Let
`kappa_H(Q)` be the minimum total number of added copies for which the split
rows have the consecutive-ones property in one common column order.  This is
an integral occurrence-level parameter; it does not identify different run
occurrences merely because their coordinate labels agree.

For every fixed start `a`, the unsplit rows have the two-sided nested chain

\[
 R^-_{a,a+H}\subseteq\cdots\subseteq R^-_{a,a}
 =R^+_{a,a}\subseteq\cdots\subseteq R^+_{a,a+H},
 \tag{2.8}
\]

with the chain truncated at the right endpoint of `Q`.  Call a split
**tower-coherent** only after adjoining `c>=1` neutral core columns, each
carrying the literal letter `K`.  Every row is assigned a nonempty interval
consisting of exactly its assigned occurrence copies together with any
chosen neutral core columns.  These complete intervals must obey every
inclusion in (2.8): whenever a column is assigned to a smaller row, that
same column is assigned to the containing row.  Define

\[
 \kappa_H^T(Q)=
 \min\left\{
   \sum_\rho(c_\rho-1)+(c-1)
 \right\},
 \tag{2.9}
\]

where the minimum is over tower-coherent layouts.  The subtraction of one
charges the first mandatory core column as the same terminal-core baseline
already present in Theorem 2.1.  Deleting all neutral columns from a tower
layout leaves an ordinary split consecutive-ones layout (empty rows are
allowed there), so

\[
                         \kappa_H(Q)\le\kappa_H^T(Q).
 \tag{2.10}
\]

The tower parameter is finite: one may dedicate a separate copy block to
each start, put a neutral `K` column in that block, and realize its finite
set-inclusion chain by adding successive row differences at its ends.  It is
the parameter relevant when a downstream construction needs all depths at
one owner to remain one nested physical occurrence, rather than merely
requiring every target value somewhere in the word.

### Theorem 2.3 (split-column compiler)

For every path with nonempty core there is a literal word representing all
lower and upper windows through depth `H` of length

\[
             \boxed{S+w(Q)+\kappa_H(Q)+1.}
 \tag{2.11}
\]

There is also a word of length

\[
             \boxed{S+w(Q)+\kappa_H^T(Q)+1}
 \tag{2.12}
\]

in which, at each owner start, the representing intervals for the complete
lower/owner/upper depth chain are nested exactly as in (2.8).

#### Proof

Take a minimum split and a consecutive-ones order of its columns.  Emit
`K union {x}` for every ordered copy, followed by `K`.  For each matrix row,
the assigned copies form one interval and their label OR is exactly the
target outside `K`; repeated labels do not change it.  Lemma 1.1 counts the
unsplit columns as `S+w`, and every split contributes one added letter.
For a minimum tower-coherent split, the same construction gives (2.12).
Emit `K union {x}` for each occurrence copy and `K` for each neutral column
in their common order.  Its length is

\[
 (S+w)+\sum_\rho(c_\rho-1)+c
 =S+w+\kappa_H^T+1.
\]

Every assigned interval is nonempty, has the exact target OR, and the
complete interval inclusions make the representing towers nested.  This
proves the last assertion.
\(\square\)

The one-mountain theorem is the support special case `kappa_H=0` witnessed
by the start order.  Its tower cost can still be positive because the
neutral core column has to align all depth chains simultaneously.  The FIFO
corridor of Section 4 has the stronger property `kappa_H^T=0`.  There is
also an exact rigidity fact which is easy to miss.

### Theorem 2.4 (unsplit common order has a FIFO normal form)

Suppose one unsplit order of the run occurrences makes even the singleton
owner rows consecutive.  Then there is an unsplit common order in which the
noncore owner supports are consecutive windows moving one place to the
right at every Johnson transition.  Thus the path has an occurrence-level
FIFO sliding-window normal form.  If `w(Q)>=2`, every witnessing atom order,
after a possible reversal, already has this form.  Conversely, a FIFO order
makes all rows (2.7) consecutive at every depth.

#### Proof

Every owner contains `K` and exactly

\[
                         k-|K|=w(Q)
\]

noncore run occurrences.  Hence its support in the alleged atom order is an
interval of one fixed length `w`.  Consecutive supports have symmetric
difference two, because one run ends and one new run begins.  Two equal-size
intervals with symmetric difference two differ by a unit shift left or
right.

If `w=0`, then `S=0` and the assertion is vacuous.  If `w=1`, singleton
rows place no constraint on the alleged order.  Reorder
the successive run occurrences chronologically; then the one-point support
moves one place to the right and gives the asserted FIFO normal form.
Assume `w>=2`.  The unit-shift direction cannot reverse.  A right shift
followed immediately by a left shift returns to the first interval, so the
occurrence removed at the first step would be active, inactive, active.
That contradicts the definition of one maximal run occurrence.  The other
reversal is symmetric.  Therefore all unit shifts have one direction,
which is exactly FIFO after a possible reversal of the alleged atom line.

Conversely, intersections and unions of consecutive equal-length windows
on one line are again intervals obtained by erosion and dilation.  These are
exactly the rows in (2.7).  \(\square\)

In particular, unsplit one-mountain batching is not a hidden class much
larger than FIFO for fixed-rank Johnson paths.  The genuinely broader
quantities are the support split excess `kappa_H` and its tower-coherent
refinement `kappa_H^T`.

### Corollary 2.5 (global halo composition)

Partition the owner-start indices of a disjoint union of oriented cycles
into consecutive arcs `I_j=[a_j,b_j]` of sizes `s_j`.  Give each arc its
forward `H`-halo

\[
 Q_j=(X_{a_j},\ldots,X_{b_j+H}).
\]

If every halo has nonempty core, then one literal word represents every
lower and upper window of at most `H+1` owners and has length

\[
 \boxed{
 L_H\le W+HR+
       \sum_{j=1}^{R}\bigl(w(Q_j)+\kappa_H(Q_j)\bigr).}
 \tag{2.13}
\]

Replacing `kappa_H` by `kappa_H^T` gives a word preserving the nested
two-sided interval tower at every assigned owner start, of length

\[
 \boxed{
 L_H^T\le W+HR+
       \sum_{j=1}^{R}\bigl(w(Q_j)+\kappa_H^T(Q_j)\bigr).}
 \tag{2.14}
\]

#### Proof

The halo `Q_j` has `S_j=s_j+H-1` transitions.  Theorem 2.3 costs
`s_j+H+w(Q_j)+kappa_H(Q_j)`.  Assign a target window to the unique base arc
containing its start and sum over `j`.  Its tower-coherent version gives
(2.14) by the same sum.  \(\square\)

Equation (2.13) is the target-support ledger.  Equation (2.14) is the
stronger physical flag-tower ledger required in the present PBBS question.

## 3. Exact flag and rank ledger

Theorem 2.1 represents the **actual** intersections and unions.  It does
not say that every owner window has the factorial-floor rank required of a
flag occurrence.  For a rank-`k` path define

\[
 \begin{aligned}
 \epsilon^-_{a,b}
   &=(b-a)-|X_a\setminus\bigcap_{t=a}^{b}X_t|,\\
 \epsilon^+_{a,b}
   &=(b-a)-|\bigcup_{t=a}^{b}X_t\setminus X_a|.
 \end{aligned}
 \tag{3.1}
\]

Then identically

\[
 \boxed{
 \begin{aligned}
 \left|\bigcap_{t=a}^{b}X_t\right|
   &=k-(b-a)+\epsilon^-_{a,b},\\
 \left|\bigcup_{t=a}^{b}X_t\right|
   &=k+(b-a)-\epsilon^+_{a,b}.
 \end{aligned}}
 \tag{3.2}
\]

Both defects are nonnegative.  The lower defect counts deletion events
which do not delete a new coordinate of `X_a`; the upper defect counts
insertion events which do not add a new coordinate to the running union.
When every coordinate has one positive run, `epsilon^+` vanishes and
`epsilon^-` is the number of positive runs born and dying strictly inside
the window.  With recurrent coordinates both defects can be nonzero.

### Proposition 3.1 (support versus tower preservation)

Suppose the PBBS owner cycles themselves are not rethreaded, and every
owner-start index is assigned to a halo as in Corollary 2.5.  The ordinary
split compiler preserves every canonical PBBS window **value** through
depth `H`, so the audited complete-support theorem still covers every lower
and upper target in the band.  The tower-coherent compiler additionally
realizes, for every start, its entire actual lower/owner/upper chain by
nested word intervals.  Hence every canonical correct flag subchain
survives as one aligned physical occurrence.

#### Proof

A canonical occurrence beginning at start `i` is an actual consecutive
owner window.  The base arc assigned to `i` contains its whole forward
window in its `H`-halo, and Theorem 2.3 represents its actual intersection
and union.  Ordinary row-dependent copy assignments need not align the
representing intervals at different depths, so this first conclusion is
target-by-target support only.  Under tower coherence, (2.8) makes those
intervals nested around the same owner occurrence.  In either case, every
designated lower occurrence with `epsilon^-=0` and every designated upper
occurrence with `epsilon^+=0` retains the same value and rank.  The PBBS
support theorem supplies the required designated occurrences target by
target (not necessarily both shores at one common start), so support is
unchanged.  \(\square\)

The proposition is why batching the unchanged factor is cleaner than
rethreading it.  After a reordering, preserving only rankwise multiplicity
vectors or only the depth-one diamond marginals does not preserve the
locations with zero defects in (3.1).

## 4. Every canonical corridor packet is FIFO

Fix `1<=q<=m` and a target

\[
 S\in\binom{[2m+1]}{m-q}.
\]

The audited global-maximum corridor constructs marks

\[
 C_0,\ldots,C_{q-1},\qquad A_0,\ldots,A_{q-1}
\]

and the PBBS path

\[
 B_t=S\cup\{C_0,\ldots,C_{q-t-1}\}
          \cup\{A_0,\ldots,A_{t-1}\},
 \qquad0\le t\le q.
 \tag{4.1}
\]

The shared-coordinate audit proves the stronger implication

\[
                    C_j=A_h\quad\Longrightarrow\quad j+h\ge2q.
 \tag{4.2}
\]

Thus all `2q` marks used in (4.1) are distinct.

### Theorem 4.1 (exact FIFO corridor packet)

Let `X_t=[n]\setminus B_t` and put

\[
 K=[n]\setminus
   \bigl(S\cup\{A_0,\ldots,A_{q-1}\}
            \cup\{C_0,\ldots,C_{q-1}\}\bigr).
 \tag{4.3}
\]

Then

\[
 \boxed{
 X_t=K\cup\{A_t,\ldots,A_{q-1}\}
        \cup\{C_{q-t},\ldots,C_{q-1}\},}
 \tag{4.4}
\]

`|K|=m+1-q`, and

\[
 X_{t+1}=X_t-\{A_t\}+\{C_{q-t-1}\}.
 \tag{4.5}
\]

The packet is FIFO and one-mountain, has
`kappa_q=kappa_q^T=0`, has active width `q`, and has the exact compiler

\[
 \begin{aligned}
 &K\cup\{A_0\},\ldots,K\cup\{A_{q-1}\},\\
 &K,\ K\cup\{C_{q-1}\},\ldots,K\cup\{C_0\},
 \end{aligned}
 \tag{4.6}
\]

of length `2q+1`.  Every subwindow of the owner packet is lower- and
upper-geodesic.

#### Proof

Equation (4.2) makes the selected `A`- and `C`-lists disjoint, so taking
the complement of (4.1) gives (4.4) and the core size.  Equation (4.5) is
immediate.  The run of `A_h` is `[0,h]`, while the run of `C_j` is
`[q-j,q]`.  Order the initial runs as

\[
 A_0,A_1,\ldots,A_{q-1}
\]

and the arriving runs as

\[
 C_{q-1},C_{q-2},\ldots,C_0.
\]

The exit sequence is

\[
                 0,1,\ldots,q-1,q,q,\ldots,q,
\]

which is increasing.  Theorem 2.1 gives the indicated atom order and length.
Every run touches one endpoint of the complete packet, so no subwindow has
an internally completed positive or negative recurrence; equivalently both
defects in (3.1) vanish.  In the atom order of (4.6), the support of `X_t`
is the length-`q` interval of atom positions `[t+1,t+q]`.  Every such
interval meets the cut between
the `A`-bank and `C`-bank.  More exactly, the lower and upper atom supports
for `[a,b]` are

\[
 [b+1,a+q]\quad\text{and}\quad[a+1,b+q],
\]

with the first interval allowed to be empty.  Every nonempty one touches
atom position `q` or `q+1`.  Placing the sole neutral `K` column between
those positions makes every erosion and dilation interval contain it; the
empty full-packet erosion is the `K` column alone.  Thus all two-sided
chains are nested and `kappa_q^T=0`.
\(\square\)

### Corollary 4.2 (a positive-density packet reservoir)

Choose one canonical packet for every rank-`(m-q)` target.  Distinct targets
have distinct oriented starts.  A greedy packing on the projected cycles
selects at least

\[
             \frac{\binom{2m+1}{m-q}}{2q+1}
 \tag{4.7}
\]

pairwise vertex-separated FIFO packets.  If `q=floor(cH)` for fixed `c>1`, using
the first `q-H+1` starts of each packet as a base arc and the last `H`
steps as its halo covers at least

\[
 \frac{q-H+1}{2q+1}\binom{2m+1}{m-q}
 =\left(\frac{c-1}{2c}+o_{A,c}(1)\right)
   e^{-c^2A^2+o_{A,c}(1)}W
 \tag{4.8}
\]

owner-start positions by mutually disjoint flag-coherent blocks.

#### Proof

One oriented start determines its `q`-window intersection, so packets
belonging to different targets cannot have the same start.  A chosen
`q`-edge interval conflicts with at most `2q` possible starts, giving
(4.7).  The binomial ratio is

\[
 \frac{\binom{2m+1}{m-q}}{\binom{2m+1}{m}}
 =\prod_{j=0}^{q-1}\frac{m-j}{m+2+j}
 =\exp\!\left(-\frac{q^2}{m}+o_{A,c}(1)\right),
 \tag{4.9}
\]

which gives (4.8).  Every forward `H`-window beginning in the declared base
arc stays inside its packet.  \(\square\)

This reservoir is structural, not yet economical.  Its packet has
`w=q`, so its excess is comparable with its base span.  At the desired
`b=Theta(H)` seam scale, replacing it by one corridor of depth
`q=Theta(H^2)` pays `Theta(H^2)` width per block and recovers a linear-order
ledger.  The missing operation must fuse packet histories while retaining
only `O(H)` left-boundary runs.

## 5. A hereditary canonical PBBS obstruction

Put `N=2m+1`, `t=m-2`, and assume `m>=4`.  The relevant three-root quotient
orbit is

\[
 \begin{aligned}
 E_0&=(10)^t1100,\\
 E_1&=110(01)^t0,\\
 E_2&=1(10)^t100,
 \end{aligned}
 \tag{5.1}
\]

For completeness, if

\[
 E(a,b,c)=(10)^a1(10)^b0(10)^c,
 \qquad a+b+c=m-1,quad b\ge1,
\]

direct cyclic-parenthesis substitution gives

\[
 phi E(a,b,c)=E(b-1,c+1,a),qquad
 delta(E(a,b,c))=2(a+1).
\]

Thus the cyclic parenthesis map sends `E_0` to `E_1`, `E_1` to `E_2`, and
`E_2` to `E_0`.  With the first maximum used as root, their three voltages
are `N-3,2,2`; hence the omitted-label word is

\[
 \lambda_{3j}=j,\qquad
 \lambda_{3j+1}=j-3,\qquad
 \lambda_{3j+2}=j-1\pmod N.
 \tag{5.2}
\]

The three-root voltage is `N+1`, coprime to `N`, so it lifts to a physical
component of length `3N`; because `3N` is odd, its step-two projection is
again one component of length `3N`.

### Lemma 5.1 (the six-owner normal form)

After choosing a projected origin and relabelling coordinates, six
consecutive complement owners in this component are exactly

\[
 \begin{aligned}
 X_0&=K\cup\{0,1,2,4\},&
 X_1&=K\cup\{0,1,4,z\},\\
 X_2&=K\cup\{0,3,4,z\},&
 X_3&=K\cup\{2,3,4,z\},\\
 X_4&=K\cup\{1,2,3,z\},&
 X_5&=K\cup\{1,2,5,z\},
 \end{aligned}
 \tag{5.3}
\]

where

\[
 z=2m,qquad K=\{6,8,\ldots,2m-2\},\qquad |K|=m-3.
 \tag{5.4}
\]

The transition table is

\[
 \begin{array}{c|ccccc}
 t&0&1&2&3&4\\ \hline
 \text{delete}&2&1&0&4&3\\
 \text{insert}&z&3&2&1&5.
 \end{array}
 \tag{5.5}
\]

There are exactly `N` coordinate translates of this motif in the component,
with projected start indices congruent modulo three.

#### Proof

Substitute (5.2) into the step-two recurrence (1.2) for five transitions.
The normalized rank-`m` state `0E_0`, translated by two coordinates, has
complement

\[
 {0,1,2,4}\cup{6,8,\ldots,2m-2}=X_0.
\]

After adding two to all labels, its first ten physical ports are

\[
                         2,z,1,3,0,2,4,1,3,5.
\]

The even positions are the five deletions and the odd positions the five
insertions, giving (5.5).  The untouched alternating tail of `E_0` is
exactly the fixed core (5.4), and applying (5.5) successively gives (5.3).
Finally

\[
                   \lambda_{t+6}=\lambda_t+2\pmod N.
\]

Three projected moves advance six physical PBBS edges, so shifting the
motif by three projected positions adds two to every coordinate.  Since
`gcd(2,N)=1`, these are `N` distinct translates and exhaust one residue
class of starts in the `3N`-cycle.  \(\square\)

### Theorem 5.2 (one-mountain and three-spoke obstruction)

The path (5.3) is not run-occurrence one-mountain in either orientation.
Its three consecutive three-owner intersections are

\[
 \boxed{
 \begin{aligned}
 X_1\cap X_2\cap X_3&=K\cup\{z,4\},\\
 X_2\cap X_3\cap X_4&=K\cup\{z,3\},\\
 X_3\cap X_4\cap X_5&=K\cup\{z,2\}.
 \end{aligned}}
 \tag{5.6}
\]

No order of the canonical run-occurrence atoms, using one atom per run
occurrence, makes all three displayed occurrence sets contiguous.
Equivalently, this six-owner path has

\[
                         \kappa_2^T\ge\kappa_2\ge1.
 \tag{5.7}
\]

One extra copy of the `z`-column realizes these three rows, so the restricted
three-spoke submatrix has exact split excess one.  No equality for the full
path parameters `kappa_2` or `kappa_2^T` is asserted.

Consequently every projected arc of this component with at least seven
transitions contains a forbidden subarc and is not one-mountain.  The same
holds after reversing the whole component.

#### Proof

In the forward path, the occurrences of `z,3`, and the second occurrence
of `2` have intervals

\[
                    [1,5],\qquad[2,4],\qquad[3,5].
\]

Their starts are strict and their exits are `5,4,5`, violating (2.2).  In
the reversed path, the occurrences of `z,3,4` have intervals

\[
                    [0,4],\qquad[1,3],\qquad[2,5],
\]

and exits `4,3,5`, another strict valley.  Thus neither orientation is
one-mountain.

Equation (5.6) is read directly from (5.3).  Delete the core-only terminal
cell and all fixed `K`-content before passing to the occurrence matrix.
Relative to the common core, the exact row supports are the three pairs

\[
                    \{z,4\},\quad\{z,3\},\quad\{z,2\}.
\]

The relevant `z`-run is one occurrence.  If all three pairs were intervals
in one atom order, that occurrence would have to be adjacent to three
different leaf occurrences, impossible in a line.  This conclusion is
only about the one-copy occurrence-faithful interface.  Unrestricted
bundled letters can emit the three cells `K union {z,4}`, `K union {z,3}`,
and `K union {z,2}` directly, and are not obstructed by this star.

Conversely split the `z` occurrence into `z_L,z_R`.  Put two leaves on the
two sides of `z_L` and put the third adjacent to `z_R`; assign the three
spoke rows to the appropriate center copy.  This proves that the restricted
star submatrix has split excess exactly one, while (5.7) remains only a
lower bound for the full matrix.  More generally a `d`-spoke star with one
center has exact center-column split excess

\[
                         \left\lceil\frac d2\right\rceil-1,
 \tag{5.8}
\]

because one copy of a center column has only two sides, and that many copies
pair all leaves.

By Lemma 5.1, forbidden six-owner motifs start every three transitions.  An
arc with `S>=7` transitions contains `S-4>=3` possible six-owner start
positions, hence one in the required residue class.  Restricting a
one-mountain path to a subarc preserves quasiconcavity.  Indeed, delete
vanished run columns; the surviving set is precisely the meeting row
`R^+_{a,b}`, itself an interval in the alleged one-mountain order.  Replace
every surviving endpoint `r` by
`min(r,b)-a`, and keep the inherited order among the runs whose clipped
start is zero.  The endpoint replacement is a common nondecreasing map and
intersection with the surviving columns preserves every superlevel
interval.  Thus the induced start order is still one-mountain.  Therefore
the larger arc cannot be one-mountain.  The reverse-orientation calculation
above gives the final assertion. \(\square\)

### Corollary 5.3 (universal `Theta(H)` batching is false)

For `H>=7` no nonempty base arc on the component (5.1) has a one-mountain
forward `H`-halo.  In particular its short-residence cuts cannot be grouped
into even one unmodified one-mountain halo, let alone batches of
`Theta(H)` cuts.

The same component has `nu_3>=m` directly.  At the motif starting at
`3j`, the translated label `3+2j` has owner run `[3j+2,3j+4]` and residence
edge interval `[3j+1,3j+4]` (indices are cyclic modulo `3N`).  Consecutive
values of `j` give intervals meeting at their common boundary edge;
nonconsecutive ones are disjoint.  Their conflict graph is the odd cycle
`C_N`, whose independence number is `floor(N/2)=m`.  Nevertheless the
component has only `3N=O(m)` owners.  Applying the old
`O(H)` collar separately at its cuts costs at most `O(Hm)=O(m^(3/2))` in
the Gaussian regime, which is `o(W)`.  Hence Corollary 5.3 refutes the
universal theorem but not an aggregate theorem with an exceptional set.

## 6. The two-port depth-three transition system

The transition-system theorem in
`MATH_DEPTH_THREE_TRANSITION_SYSTEM_AND_COMMON_ORDER_GATE_20260728.md`
correctly treats its displayed lower depth-three row.  Simultaneous
preservation of the upper row requires one more port.

Let `A` be a rank-`s` owner and let an incident Johnson edge copy `e` have
other endpoint

\[
                         A-x+y,
 \qquad x\in A,\quad y\notin A.
\]

Define its two ports at `A` by

\[
 x_A(e)=x=A\setminus c_-(e),
 \qquad
 y_A(e)=y=c_+(e)\setminus A.
 \tag{6.1}
\]

### Lemma 6.1 (exact two-sided transition labels)

If two edge copies `e,f` are paired at `A`, with ports `(x,y)` and
`(x',y')`, their lower and upper three-owner labels are

\[
 \boxed{
 L_A(e,f)=A\setminus\{x,x'\},\qquad
 U_A(e,f)=A\cup\{y,y'\}.}
 \tag{6.2}
\]

They have the required ranks `s-2` and `s+2` exactly when

\[
                         x\ne x',\qquad y\ne y'.
 \tag{6.3}
\]

#### Proof

The lower colours of the two edges are `A-x` and `A-x'`; intersect them.
The upper colours are `A+y` and `A+y'`; union them.  Their ranks are correct
exactly under (6.3).  \(\square\)

Call such a pair **bi-safe**.  Let `h_(A,x,y)` be the number of incident
copies of port type `(x,y)`.  For compatible distinct types introduce
symmetric pair variables

\[
 p_{A;(x,y),(x',y')}\in\mathbb Z_{\ge0}
 \quad\text{only if }x\ne x',\ y\ne y',
 \tag{6.4}
\]

and end-stub variables `u_(A,x,y)`.  The exact local incidence equations
are

\[
 \sum_{(x',y'):\ x'\ne x,\ y'\ne y}
 p_{A;(x,y),(x',y')}+u_{A,x,y}=h_{A,x,y}.
 \tag{6.5}
\]

The two prescribed three-owner rows impose

\[
 \begin{aligned}
 d^-_S
 &=\sum_A\sum_{\{(x,y),(x',y')\}:A-\{x,x'\}=S}p_A,\\
 d^+_T
 &=\sum_A\sum_{\{(x,y),(x',y')\}:A\cup\{y,y'\}=T}p_A.
 \end{aligned}
 \tag{6.6}
\]

Here (6.6) counts the internal three-owner windows; any two boundary flag
chains are fixed separately at the two end stubs, exactly as in the cited
Euler formulation.  Together with two total end stubs and connected
transition graph, these are the exact two-sided replacement for equations
(2.3)--(2.5) of the cited note.

### Theorem 6.2 (two-sided depth-three common-order criterion)

A fixed diamond edge-copy multigraph has one Euler path with prescribed
internal lower and upper three-owner multiplicities if and only if it has
integral variables (6.4)--(6.6), two end stubs, and a realization on
distinguishable copies whose transition graph is connected.  Prescribed end
flags must additionally be compatible with the two selected stubs.

#### Proof

An Euler path pairs its entering and leaving edge copies at each internal
owner.  Lemma 6.1 gives (6.5)--(6.6), and trail order makes the transition
graph one path.  Conversely, realize every integral pair count on the
distinguishable copies.  A connected transition graph with exactly two
degree-one copies is a path through all edge copies, hence reads as an Euler
trail.  Lemma 6.1 gives both prescribed rows.  \(\square\)

For unprescribed pair labels there is a simple local feasibility test.
After removing the chosen stubs, regard each port copy `(x,y)` as an edge of
a bipartite multigraph between the `x`-ports and `y`-ports.  If it has `2p`
edges, a bi-safe pairing exists if and only if its maximum degree is at most
`p`.  Necessity is immediate.  For sufficiency, Koenig edge-colour it with
`p` colours.  If one colour class has size above two, averaging forces a
class below two.  In their two-colour subgraph every alternating component
has edge-count imbalance in `{-1,0,1}`; some component has imbalance `+1`
toward the larger class.  Swapping the two colours on that component moves
one edge from the larger class to the smaller while preserving properness.
Iteration makes all `p` classes have size two.  Each class is a matching
and hence is one compatible pair.  The prescribed projection equations
(6.6) are strictly stronger.

### Proposition 6.3 (the opposed rectangle obstruction)

Let four port copies at one owner have types

\[
                    (a,c),(b,d),(a,d),(b,c),
 \qquad a\ne b,\ c\ne d.
 \tag{6.7}
\]

Pair the first two and the last two.  Both old pairs are bi-safe.  Deleting
these pairing edges gives two possible cross-pairings: one pairs equal
`x`-ports, and the other pairs equal `y`-ports.  Hence neither is bi-safe.

#### Proof

One cross-pairing contains `(a,c)`--`(a,d)` and
`(b,d)`--`(b,c)`.  The other contains `(a,c)`--`(b,c)` and
`(b,d)`--`(a,d)`.  Apply (6.3).  \(\square\)

Thus the lower-safe cross-pair switch from the cited component-joining
theorem is not automatically a two-sided flag-safe switch.  Lower-row
redundancy alone also does not protect the two upper labels changed by a
bi-safe switch.

### Proposition 6.4 (fixed PBBS diamond rigidity)

If every entry of the canonical PBBS diamond table `z_(R,U)` is preserved,
then the projected Johnson edge-copy multigraph is fixed.  Since it is a
simple two-factor, the transition pairing at every owner is forced.
Consequently the only common orders preserving that exact table are the
existing component orders, up to rotation and reversal; no hidden
transition-system rethreading removes the obstruction of Section 5.

#### Proof

For `R subset U` with `|U\setminus R|=2`, there is exactly one Johnson edge:
its endpoints are the two rank-`s` sets strictly between `R` and `U`.
Therefore the complete table fixes every edge copy.  Every PBBS owner has
degree two, so its two incident copies have only one pairing.  Reading the
resulting transition components gives the original cycles.  \(\square\)

Preserving only the row and column sums of the diamond table permits a new
edge multigraph, but then (6.4)--(6.6), the rectangle obstruction, residence,
and all higher flag rows must be solved together.  Through depth `H`, local
pair equations are not enough: one needs the corresponding boundary-corrected
length-`H` transition/de Bruijn constraints on the same path.

## 7. Finite calibration

The exact diagnostic

`scratch/calibrate_pbbs_one_mountain.py`

constructs the canonical PBBS permutation from cyclic parenthesis matching,
takes its complement-projected step-two cycles, decomposes every tested arc
into maximal positive run occurrences, exhausts the left-boundary tie orders,
and directly verifies all represented lower and upper OR values through
depth three.  It also brute-forces an arbitrary common order whenever there
are at most nine run atoms.  The script is a calibration, not part of the
asymptotic proof.

For a depth-three halo and a base arc of `s` owner starts, the tested path
has `S=s+2` transitions.  The table records

\[
 \#\{\text{nonempty-core, run-occurrence one-mountain arcs}\}/W.
\]

\[
\begin{array}{c|ccccc}
m\backslash s&1&2&3&4&5\\ \hline
3&35/35&14/35&7/35&0/35&-\\
4&126/126&126/126&45/126&27/126&18/126\\
5&462/462&462/462&396/462&176/462&121/462
\end{array}
\tag{7.1}
\]

The dash is the case where the requested transition span equals the length
of a seven-owner component, so the finite linear-arc diagnostic excludes it.

The first symbolic obstruction is (5.3).  At base size three the full-layer
census sees three-spoke occurrences at `7,18,33` starts for `m=3,4,5`; for
`m=4,5` the displayed core is nonempty.  The separate exact diagnostic

`scratch/calibrate_pbbs_three_root_component.py`

starts from (5.3), generates only its PBBS orbit, and checks the cyclic
five-transition formula.  For every `m=3,...,8` it finds exactly `N` formula
hits, at projected starts `0 mod 3`, and exactly `N` stars on the
five-transition arcs.  There are `2N` generalized one-mountain failures in
either orientation at that span; the formula/star family is one residue class,
not the set of all valleys.  Every six- and seven-transition arc tested in
that component fails in both orientations.  The last statement is finite
calibration only; the uniform theorem above uses the proved safe threshold
of seven transitions.

The full summary runs gave no direct compiler-verification failure whenever
a one-mountain order was found.  The arbitrary common-order test was
exhaustive only on arcs having at most nine run atoms.  For example, at
`m=4,s=3` it tested `81` of `126` arcs (`45` pass and `36` fail), and at
`m=5,s=3` it tested `198` arcs (`132` pass and `66` fail), leaving `264`
untested.  Its first tested failure is the same three-spoke motif.  The
parameter-specific hashes are as follows:

\[
\begin{array}{c|c|c}
\text{diagnostic}&\text{file SHA-256}&\text{output-content SHA-256}\\ \hline
\texttt{calibrate\_pbbs\_one\_mountain.py}
 &\texttt{181db5334b294a35d014d0543c649eed61ae56a78c4301d22df9c904a0b73894}
 &\texttt{f638a7c08101461d342da3d0b41a984751a0d7e10657c187ecbdfe4bc82e0f6}\\
\texttt{calibrate\_pbbs\_three\_root\_component.py}
 &\texttt{603ddbae020c4ba3fc4b7dec50b7197f06bdf177a02a3c2083bc04ce62b56d21}
 &\texttt{5f8704f9b8ca599d1f14ab97119c68a0ee0be4c5085f049480243e22cbb20c34}
\end{array}
\tag{7.2}
\]

The first output hash is for
`--min-m 3 --max-m 5 --depth 3 --max-base 5 --brute-limit 9 --summary`;
the second is for
`--min-r 3 --max-r 8 --spans 5 6 7 --summary`.  These finite numbers are
not used to extrapolate a density statement.

## 8. The exact aggregate batching theorem still needed

Let `J<=nu_H(P_m)+c(P_m)<=nu_H(P_m)+B` be a circular-interval residence
cut set.  Suppose the canonical owner starts can be divided into a regular
part and an exceptional part, which partition all `W` starts, with the
following properties.

1. If the exceptional part has size `E`, it has an independently literal
   fallback word of total length `E+o_A(W)` covering every lower and upper
   window through depth `H` whose start is exceptional, with its required
   two-sided nested flag chains aligned.
2. The regular starts are the disjoint union of `R` consecutive base arcs;
   their final forward `H`-halos have nonempty persistent core and use the
   tower-coherent split-column compiler.
3. Their cores obey

   \[
      R=O_A\!\left(B+\frac JH\right),\qquad
      \sum_{j=1}^{R}
      \bigl(w(Q_j)+\kappa_H^T(Q_j)\bigr)=O_A(HR).
      \tag{8.1}
   \]

### Theorem 8.1 (conditional `Theta(H)` seam batching)

Under these three hypotheses there is a literal two-sided PBBS central-band
word, with the assigned lower/owner/upper flag chains nested, of length

\[
 \boxed{L_H\le W+O_A(HB+J)+o_A(W).}
 \tag{8.2}
\]

In particular, the existing critical estimate `nu_H=O_A(BH)` implies
`L_H=W+o_A(W)`.

#### Proof

Use the supplied fallback on the exceptional part and the tower-coherent
form (2.14) of Corollary 2.5 on the regular arcs.  Their two baseline terms add to
`E+(W-E)=W`.  Equation (8.1) gives

\[
 HR+\sum_j\bigl(w_j+\kappa_H^T(Q_j)\bigr)=O_A(HB+J).
\]

Proposition 3.1 preserves every canonical nested flag occurrence in the
regular part; the fallback hypothesis supplies the exceptional occurrences.
Finally

\[
 HB+J=O_A(BH),\qquad
 W=(2m+1)B=\Theta_A(BH^2),
\]

so the normalized excess is `O_A(1/H)=o_A(1)`.  \(\square\)

Theorem 8.1 is exactly the desired `b=Theta(H)` ledger.  Section 5 proves
that its regularity hypothesis cannot include every canonical component.
It does not show that the exceptional fallback charge must be macroscopic.

There are now two sharply separated ways to finish or close this lane.

* **Positive:** prove (8.1) after deleting an exceptional family whose old
  collars cost `o(W)`.  This is a joint theorem about PBBS persistent-core
  widths and its integral tower-coherent run-column split excess, not a
  consequence of `nu_H` alone.
* **Negative:** prove that every such deletion leaves a run-valley/star
  packing or a two-port rectangle obstruction with total compulsory charge
  `Omega(W)`.  The single component (5.1) supplies only polynomial charge
  and is insufficient.

## 9. Endpoint geometry is not the negative invariant

The two-endpoint relaxation in the preceding batching note is automatically
near-saturated by an actual consecutive-window chronology.  On a linear
owner path, anchor

\[
 L_{i,q}=\bigcap_{t=i}^{i+q}X_t
 \quad\text{by}\quad(\rho,\lambda)=(X_i,X_{i+q}),
\]

and

\[
 U_{i,q}=\bigcup_{t=i}^{i+q}X_t
 \quad\text{by}\quad(\lambda,\rho)=(X_i,X_{i+q}).
\]

At each fixed depth these endpoint pairs are injective and order-preserving;
reuse of the same left role or the same right role is nested as `q` changes.
Opening one cyclic component loses at most `2q` shore occurrences at depth
`q`, hence at most `cH(H+1)` through depth `H`.  Cross-role reuse of one
owner is not a common word endpoint and imposes no nesting condition.

Therefore an integrated `Omega(H)`-per-seam lower bound cannot come from
endpoint order alone.  It must use intervening occurrence content, such as
the run valleys and the scoped three-spoke atom obstruction above, or the
genuinely two-port/all-depth transition constraints.

## 10. Proved boundary

The following statements are proved.

1. Repeated coordinates do not cost extra beyond the baseline transition
   count: the generalized compiler has exact excess `w`.
2. Within the label-preserving occurrence-copy interface, common-order
   failure is measured by the exact additive support parameter `kappa_H`;
   its tower-coherent refinement is `kappa_H^T`, and the unsplit case has a
   FIFO normal form.
3. Canonical PBBS corridor packets are exact FIFO two-sided packets.
4. The unchanged factor contains a hereditary, orientation-independent
   component on which no `H>=7` halo is one-mountain.
5. That component is asymptotically negligible under the old fallback.
6. A two-sided depth-three transition system needs both ports, and the
   ordinary cross-pair joining switch has an exact opposed-rectangle
   obstruction.
7. Fixing the complete PBBS diamond table fixes its component chronology.
8. Endpoint-pair geometry alone is essentially saturated and cannot prove
   the required macroscopic lower bound.

What remains unproved is exactly the aggregate regular/exceptional
decomposition (8.1), or a Catalan-scale lower bound for the aggregate
tower-coherent run-column split/width charge.  Finite calibration and the
explicit three-root component do not decide that density question.
