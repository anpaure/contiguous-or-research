# Prospective planting of the twisted `C6` unit pump beside the fixed-`z` seven-ear corridor

**Date:** 2026-08-02  
**Status:** unconditional same-cover Johnson-distance separation, exact
cover-normalizer load bounds, exact
two-aperture/private-edge correction, and an exact conditional ambient
planting theorem.  Post-hoc insertion into an arbitrary completed owner/q1
factor is impossible.  Existence of the final pump-aware rooted corridor,
deeper upper shadows, source binding, and the terminal compiler are not
claimed.

## 0. Result

Let

\[
                         n=2r-1,
\tag{0.1}
\]

let the required history depth be `d>=1`, and put

\[
                         W={n\choose r}={n\choose {r-1}}.
\tag{0.2}
\]

There are two separate ambient questions.

1. **Can the literal pump bank be kept disjoint from the prepared
   seven-ear bank in the same cyclic child cover?**  Yes, but not by an
   arbitrary coordinate conjugation.  Mark the twisted three-run `C6` pump
   by its persistent private edge and by a second planting edge.  Its full
   owner/lower/immediate-upper footprint has size `3n` in each layer.  Fix
   that equivariant pump first and choose the seven-ear anchor `X` outside
   the Johnson balls of radius `2d+4` around its owners.  Such an `X` exists
   whenever

   \[
    3n\sum_{j=0}^{2d+4}{r\choose j}{r-1\choose j}
                         <{2r-2\choose r}.
   \tag{0.3}
   \]

   The opened seven-ear path then has the exact/upper-bound footprint

   \[
        |Q_r|=26d+32,
        \qquad |Q_{r-1}|=26d+31,
        \qquad |Q_{r+1}|\le26d+31.
   \tag{0.4}
   \]

   Together with the already required local label conditions

   \[
          r\ge 3d+4,
          \qquad r\ge 2d+13,
   \tag{0.5}
   \]

   this is an explicit sufficient same-cover planting theorem.  It holds
   for every sufficiently large `r` when `d=O(sqrt(r))`.  Thus collision
   with the prepared seven-ear packet is not an asymptotic obstruction.

2. **Can the pump be added to an arbitrary completed owner/q1 host?**  No.
   A completed factor already gives degree two to every owner and every
   lower facet.  The pump is itself a saturated `3n`-cycle.  Even its first
   incident edge violates the degree row unless an old host edge is removed.
   Moreover its incidence lift has `6n` edges, far beyond the `r-2` range of
   the small protected-factor theorem.  The correct theorem is therefore
   **prospective**: reserve the pump and seven-ear paths first and complete
   the residual host around both of them.

The exact prospective interface is finite.  Open the pump at a planting
edge `e_o` distinct from the persistent private edge `e_*`.  Put the pump
path and the opened seven-ear path into one literal fragment table.  If a
rooted ordered corridor selection satisfies the degree, resource, two-sided
history, exact palette, and zero-background-charge rows in Section 5, then
it expands to one owner/q1-exact resident cycle of absolute voltage `+1` (or
`-1` after global reversal).  The fixed-`z` old/new phases use the same
ambient corridor and hence retain relative displacement zero.  The edge
`e_*` remains physically untouched.

This is the precise sense in which the pump supplies only the **absolute**
child voltage.  It is not asked to cancel the seven-ear phase displacement,
which is already zero.

## 1. The two protected fragments and their exact sizes

### 1.1 The marked pump

Use the `+1` branch of
`MATH_THEOREM_K_TWISTED_THREE_RUN_C6_DYADIC_PUMP_AND_HISTORY_APERTURE_20260802.md`.
Its developed cycle `C_P` has

\[
 \begin{array}{c|ccc}
  \text{resource layer}&r&r-1&r+1\\ \hline
  \text{distinct physical resources}&3n&3n&3n.
 \end{array}
\tag{1.1}
\]

Choose two distinct physical edges:

* `e_*`, the persistent private edge; and
* `e_o:t_o->s_o`, the planting edge.

Delete only `e_o`.  The resulting path

\[
                         P_P=C_P-e_o:s_o\leadsto t_o
\tag{1.2}
\]

has `3n` owners and `3n-1` internal lower and upper edge colours.  We retain
the omitted lower/upper pair of `e_o` in the return-demand record, so the
ported protected footprint is still exactly (1.1).  The edge `e_*` remains
an internal protected edge of `P_P`.

Opening at `e_o` clips, but does not shorten, every run which meets the cut.
Thus the positive and negative internal history bounds of the pump remain
valid.  Its exact exported state is

\[
 \Xi_P=(v=1;z=0,b=0;
        \mathcal R_o^+,\mathcal R_o^-;
        e_*;e_o),
\tag{1.3}
\]

where `e_o` is the reference return and `e_*` is the immutable private
resource.  Complete reversal gives the correlated `-1` state.

This two-edge marking is not an extra combinatorial gadget.  It is one
already proved simple cycle with one edge reserved for recursion and a
different edge used for ambient planting.

### 1.2 The opened seven-ear path

The completed fixed-`z` local cycle has

\[
                         E_A=28d+35
\tag{1.4}
\]

projected Johnson edges.  One exterior ear `Q_j` has `2d+4` edges.  Removing
that ear and its `2d+3` internal owners leaves the protected path

\[
                         P_A^\epsilon:s_A\leadsto t_A,
             \qquad \epsilon\in\{0,1\},
\tag{1.5}
\]

with

\[
 \begin{aligned}
 |E(P_A^\epsilon)|&=(28d+35)-(2d+4)=26d+31,\\
 |V(P_A^\epsilon)|&=26d+32.
 \end{aligned}
\tag{1.6}
\]

The lower facets on this simple path are distinct.  There are `26d+31`
immediate-upper **occurrence tokens**, so the number of distinct physical
caps is at most `26d+31`; no squarefreeness of that cap multiset is needed
for the avoidance bound.  Thus (0.4) follows.  The two phases have the same endpoint owners, canonical
frames, boundary-history sockets, and exposed palette demands, and

\[
                 \lambda(P_A^1)-\lambda(P_A^0)=0.
\tag{1.7}
\]

When the banks are disjoint, the closed-pump/opened-A union has

\[
\begin{array}{c|c}
\text{resource}&\text{count}\\ \hline
\text{owners}&3n+26d+32\\
\text{lower facets}&3n+26d+31\\
\text{upper occurrence tokens}&3n+26d+31\\
\text{incidence edges}&6n+52d+62.
\end{array}
\tag{1.8}
\]

Opening the pump at `e_o` changes only the last count to `6n+52d+60`
and exports its omitted lower/upper return pair.

## 2. Same-cover placement and exact load bounds

### 2.1 Why the full symmetric group is not available

The pump voltage is defined in the fixed cyclic cover generated by
`tau:x->x+1`.  An arbitrary coordinate permutation `g in S_n` changes that
cover to the conjugate cover generated by `g tau g^{-1}`.  Therefore the
uniform `S_n` rank-layer calculation, although correct for an unstructured
physical packet, is **not** a voltage-preserving planting argument.

The normalizer of the cyclic deck group consists of the affine maps

\[
                         x\longmapsto ux+b,
              \qquad u\in\mathbb Z_n^\times.
\tag{2.1}
\]

Such a map sends pump voltage `1` to the unit `u`; translations alone do not
change the developed resource sets.  This normalizer is not transitive on a
Boolean rank layer, so one must keep its orbit strata.

### Lemma 2.1 (cover-preserving orbit-load lemma)

Let `G` be any subgroup of the ambient cover normalizer and let
`Omega_alpha` be its resource orbits, with resource type included in
`alpha`.  If a marked packet contains `m_alpha` resources in
`Omega_alpha`, then in the complete orbit `mathcal O` of distinct marked
packets every `q in Omega_alpha` occurs in exactly

\[
                    {|\mathcal O|m_\alpha\over|\Omega_\alpha|}
\tag{2.2}
\]

members.  Hence a cover-preserving conjugate avoids a forbidden bank `Q`
whenever

\[
             \sum_\alpha
                {m_\alpha|Q\cap\Omega_\alpha|
                         \over|\Omega_\alpha|}<1.
\tag{2.3}
\]

#### Proof

The orbit family is invariant under `G`, so its incidence degree is constant
on each `Omega_alpha`.  Double-counting gives (2.2).  The left side of
(2.3) is the expected collision count of a uniform member of `mathcal O`;
an integer collision count of expectation below one is zero somewhere.
\(\square\)

Equation (2.3) is the exact shared-resource load bound.  It is not implied
by the three aggregate rank-layer sizes.  The two marked edges `e_*` and
`e_o` are part of the object before its orbit is taken.

### 2.2 A deterministic same-cover escape

The cleaner route is to keep the `+1` pump fixed and choose A's local
anchor away from it.  Write `d_J(S,T)=r-|S cap T|` for Johnson distance
between rank-`r` owners.

### Lemma 2.2 (radius of the seven-ear owner bank)

Every owner in the completed seven-ear local cycle, and hence in either
opened path, lies within Johnson distance `2d+3` of its anchor `X`.

#### Proof

Put

\[
              C_0=X-(D^x\cup D^y\cup\{a,b,c\}).
\tag{2.4}
\]

The central packet owners, both monotone ray banks, and every state of every
exterior ear all contain `C_0`.  Since `|C_0|=r-2d-3`, any rank-`r` set
containing it is at Johnson distance at most `2d+3` from `X`. \(\square\)

If an A-facet equals a pump facet, or an A-cap equals a pump cap, an incident
A-owner and pump owner are at Johnson distance at most one.  Thus distance
greater than `2d+4` separates owners, lower facets, upper caps, and
incidences.  It also separates the occurrence-labelled endpoint/history
keys in the fixed A registry because each such key contains its literal
owner or facet.  Bare coordinate names are not capacity-one resources.

### Theorem 2.3 (Johnson-far anchor planting)

Fix the equivariant `+1` pump and the fixed-z label `z`.  If

\[
  3n\sum_{j=0}^{2d+4}{r\choose j}{r-1\choose j}
                         <{2r-2\choose r},
\tag{2.5}
\]

then there is a rank-`r` anchor `X` with `z notin X` and

\[
             d_J(X,T)>2d+4
       \quad\text{for every pump owner }T.
\tag{2.6}
\]

After choosing the seven-ear roles and banks inside and outside this `X`,
the entire local A owner/lower/q1/incidence/history bank is disjoint from the
pump bank.  The pump remains in the original cyclic child cover and retains
voltage `+1`.

#### Proof

There are exactly

\[
                         {n-1\choose r}={2r-2\choose r}
\tag{2.7}
\]

candidate anchors avoiding `z`.  A Johnson ball of radius `R` about one
rank-`r` owner has

\[
                         \sum_{j=0}^{R}{r\choose j}{r-1\choose j}
\tag{2.8}
\]

vertices.  The pump has `3n` owners.  The union bound and (2.5) leave an
anchor satisfying (2.6).

Lemma 2.2 and one triangle inequality exclude owner equality.  Equality of
a lower facet or upper cap would give incident A and pump owners at distance
at most one, contradicting (2.6).  Incidence and the occurrence-labelled
history keys in the protected registry contain one of those physical
owners/facets and are therefore also distinct.  The label inequalities
(0.5) supply the disjoint internal/external A roles after `X` is fixed.
\(\square\)

### Corollary 2.4 (asymptotic range)

For `d=O(sqrt(r))`, condition (2.5) holds for all sufficiently large `r`.

#### Proof

With `R=2d+4=O(sqrt(r))`, the ball in (2.8) is at most

\[
 (R+1)\left({er\over R}\right)^{2R}
                         =\exp(o(r)).
\tag{2.9}
\]

The right side of (2.5) is `exp(Theta(r))`, while the factor `3n` is
polynomial. \(\square\)

This proves disjoint local planting in the selection order

\[
                   \text{pump first, A anchor second}.
\tag{2.10}
\]

It does not plant the pump into a completed spanning factor.  Nor does A's
`Theta(n^7)/O(n^6)` local atlas, by itself, prove the reverse selection
order: the developed pump forbids `Theta(n)` resources, so its crude
deletion bound is of the same order as the whole seven-ear atlas.

## 3. Two universal post-hoc planting no-gos

### Proposition 3.1 (degree saturation)

There is no theorem which adds the pump edge-disjointly to an arbitrary
completed owner/lower-q1 factor while leaving that factor fixed.

#### Proof

Every rank-`r` owner and every rank-`(r-1)` lower facet already has degree
two in the completed incidence factor.  Each pump owner and lower facet has
degree two in the pump cycle.  The union therefore has degree four at every
resource in the pump footprint.  Already one added pump incidence violates
the degree-two row. \(\square\)

Hence the host must be selected around the pump or changed by an exact
alternating rethread.  Resource disjointness from the **prepared bank** does
not mean disjointness from the final spanning owner set.

### Proposition 3.2 (the small protected-factor theorem cannot plant the pump)

The closed pump has `6n` Middle-Levels incidence edges, and the opened pump
has `6n-2`.  For every `r>=1`,

\[
                         6n-2>r-2.
\tag{3.1}
\]

Thus the protected-factor theorem with budget `r-2` does not apply.

#### Proof

Each projected Johnson edge lifts to two incidences.  Substitute
`n=2r-1` in (3.1). \(\square\)

### Proposition 3.3 (why a second planting edge is necessary)

If `e_*` is both the only private edge and the edge at which a saturated
pump component is opened for insertion into a larger component, then that
literal edge cannot remain in the output.  Marking a distinct `e_o` is the
minimal correction: open at `e_o`, keep `e_*` inside `P_P`, and require the
ambient replacement of `e_o` to have zero background charge.

This does not assert that the replacement corridor exists.  It only removes
the formal incompatibility between “join the pump” and “retain the same
private edge.”

### Proposition 3.4 (a transparent two-edge join is impossible)

Let `xy,pq` be two old Johnson edges on four distinct owners and let
`xq,py` be the crossed pair.  If the lower-q1 multisets agree,

\[
       \{x\cap y,p\cap q\}=\{x\cap q,p\cap y\},
\tag{3.2}
\]

then the two old lower colours coincide.  Hence no nondegenerate two-edge
splice can preserve a squarefree exact lower-q1 palette.

#### Proof

There are two possible pairings in (3.2).  If
`x cap q=x cap y=L`, then `y` and `q` both contain the same rank-`(r-1)`
subset `L` of `x`.  The other equality says that `y` and `q` also contain
the same rank-`(r-1)` subset `M` of `p`.  Since distinct rank-`r` sets
`y,q` have intersection of rank `r-1`, both `L` and `M` equal `y cap q`.

In the crossed pairing, `x cap q=p cap q=M` and
`p cap y=x cap y=L`.  Thus both `x` and `p` contain `L union M`.  If
`L!=M`, that union has rank `r`, forcing `x=p`, contrary to distinctness.
Hence again `L=M`. \(\square\)

This is a sharper local incompatibility than mere degree saturation.  The
corrected private-edge-preserving actuator is at least ternary, or else it
must use a global palette backup.

## 4. Exact endpoint compatibility

For an internally depth-`d` resident directed path `P`, write

\[
 D^+(P)=(a_1,\ldots,a_d),
 \qquad I^+(P)=(b_m,\ldots,b_{m-d+1})
\tag{4.1}
\]

for its first `d` deletions and last `d` insertions, newest first on the
right.  Let `D^-(P),I^-(P)` be the dual collars obtained by exchanging
deletions and insertions.

Suppose a Johnson join `e=(a,b)` is placed between paths `P` and `Q`.
The positive history row is exactly

\[
\begin{aligned}
 a&\ne I_i^+(P) &&(1\le i\le d),\\
 b&\ne D_j^+(Q) &&(1\le j\le d),\\
 I_i^+(P)&\ne D_j^+(Q) &&(i+j\le d).
\end{aligned}
\tag{4.2}
\]

The negative row is the same system with the dual collars and the
insertion/deletion roles interchanged.  Equations (4.2) and its dual are
necessary and sufficient; marginal acceptance of the two endpoints is not.

For every selected join one must additionally record

\[
       I(e)=T_{\rm tail}\cap T_{\rm head},
       \qquad U(e)=T_{\rm tail}\cup T_{\rm head},
       \qquad\delta(e),
\tag{4.3}
\]

and its complete occurrence-resource set.  The join is admissible exactly
when:

1. the endpoints are Johnson adjacent;
2. (4.2) and its dual hold;
3. its owner/facet/cap/history resources respect their residual capacities;
4. its labels satisfy the exact lower and upper demand rows; and
5. it avoids the persistent private resource `e_*`.

These five items are the exact endpoint-state compatibility.  In
particular, a direct two-edge splice is not presumed q1-transparent; the
global residual palette rows must certify any compensation.

### Theorem 4.1 (ternary Boolean-hex endpoint interface)

Let three old directed edges be

\[
        O=\{A\to B,C\to D,E\to F\},
\tag{4.4}
\]

where `E->F=e_o` is a nonprivate pump edge and the other two edges lie in
two prepared host components.  Replace them by

\[
        N=\{A\to F,C\to B,E\to D\}.
\tag{4.5}
\]

Assume the six edges form one literal Boolean hex and the three old edges
lie on three distinct directed cycles.  Then the switch merges those cycles
to one and preserves the complete owner, lower-q1, immediate-upper, tail,
and head inventories.  It preserves biresidence exactly when all three new
joins satisfy (4.2) and its dual against their newly paired path collars.
It preserves the pump unit exactly when

\[
 \delta(A,F)+\delta(C,B)+\delta(E,D)
 =\delta(A,B)+\delta(C,D)+\delta(E,F).
\tag{4.6}
\]

Equation (4.6) is automatic for one coherent physical lift of the whole
hex, but not for six independently canonicalized quotient options.  Since
`e_o!=e_*`, the private edge `e_*` remains untouched.

#### Proof

The Boolean-hex identity gives the resource-multiset equality.  Deleting
the three old edges gives three paths, and the new cyclic pairing
concatenates all three into one cycle.  The directed-history collar theorem
is necessary and sufficient at the three changed seams in each polarity.
Finally (4.6) is exactly zero signed switch charge; in one coherent lift it
telescopes because old and new typed tail/head multisets agree. \(\square\)

There is an explicit local supply check.  If a coordinate guard bank `B`
is forbidden, a nonprivate pump edge outside a cyclic radius-`d`
neighbourhood exists whenever

\[
                         3n>6|B|+2d+1.
\tag{4.7}
\]

For a Cartesian Boolean hex through that edge, after deleting forbidden
label sets `B_L,B_R` and at most `lambda_Q` resource options, one remains
whenever

\[
       (r-1-|B_L|)(r-2-|B_R|)>\lambda_Q,
       \qquad \lambda_Q\le |Q|(r-1).
\tag{4.8}
\]

These inequalities prove raw prepared-hex supply only.  They do not put the
two partner edges on distinct residual host components or make their six
history tests hold.

### Theorem 4.2 (exact residual owner/lower-q1 factor gate)

Let `ML_r=(L,R;E)` be the containment graph between rank `r-1` facets and
rank `r` owners.  The closed pump saturates equal-size shores
`F_P subset L` and `O_P subset R`.  Fix any 2-bounded protected seven-ear
bank `Q` disjoint from those shores.  Delete `F_P,O_P` and the already used
edges of `Q`, put

\[
            b(v)=2-d_Q(v),
\tag{4.9}
\]

and call the residual bipartite graph `G`.  Then the pump and `Q` extend to
a spanning owner/lower-q1 two-factor if and only if, for every
`S subseteq L-F_P`,

\[
 \sum_{x\in S}b(x)
 \le
 \sum_{y\in R-O_P}\min\{b(y),d_G(y,S)\}.
\tag{4.10}
\]

#### Proof

After the fixed edges are removed, each residual vertex needs exactly the
degree in (4.9).  The two total demands agree because the pump deletes the
same number of vertices from the two shores and every protected incidence
of `Q` lowers one demand on each shore.  Equation (4.10) is the
Ore--Ryser criterion for the resulting bipartite `b`-factor. \(\square\)

This is an exact, checkable host obstruction.  It proves neither component
fusion nor immediate-upper completion; those require Theorem 4.1 or the
more general fragment master below.

## 5. Prospective pump-aware ambient planting

Fix a table `mathcal F^epsilon` of pairwise resource-disjoint internally
accepting directed fragments which partitions the owner occurrences.  It
contains:

* the pump path `P_P=C_P-e_o`;
* the phase-`epsilon` seven-ear path `P_A^epsilon`; and
* the residual ambient fragments.

All fragments except `P_A^epsilon` are identical in the two fixed-`z`
phases.  Fix one entrance and exit state for every fragment.  Let `x_e` be
the selected literal joins.  Fix one closing join `z->p`, set its variable
to one, and fix an order with `p` first and `z` last.  Every other candidate
join is forward in that order.  Impose:

\[
\begin{aligned}
 &\sum_{e:\operatorname{tail}(e)=F}x_e=1,
   &&\sum_{e:\operatorname{head}(e)=F}x_e=1,
                              &&\text{for every fragment }F;       \tag{5.1}\\
 &\sum_{e:q\in R(e)}x_e\le b_q,
                              &&&\text{for every capacity row }q; \tag{5.2}\\
 &\sum_{e:q\in R(e)}x_e=b_q,
                              &&&\text{for every exact row }q.    \tag{5.3}
\end{aligned}
\]

Here fixed fragment use is subtracted from `b_q`, and the closing join is
handled literally rather than duplicated in (5.1).  Every candidate join
has already passed Section 4.

Let `lambda(F)` be the coherent integer gain of a fragment in the chosen
child section.  Define the background charge relative to the omitted pump
edge by

\[
 \sigma_{\rm bg}=
     \sum_{F\ne P_P}\lambda(F)
       +\sum_e x_e\delta(e)-\delta(e_o).
\tag{5.4}
\]

The equality is imposed coherently in the integer lift; reduction modulo
`n` is enough only for the final component count.

### Theorem 5.1 (unit-pump/seven-ear ambient planting)

Assume:

1. the marked pump is disjoint from the prepared protected bank, for
   example by Theorem 2.3;
2. (5.1)--(5.3) have a solution which uses the same ambient fragments and
   joins in the two fixed-`z` phases;
3. every selected join satisfies the exact endpoint rows of Section 4;
4. the protected private edge `e_*` is retained and no selected resource
   conflicts with it; and
5. `sigma_bg=0` in (5.4).

Then literal expansion gives, in each fixed-`z` phase, one simple directed
spanning cycle with:

* every encoded owner and lower-q1 resource exactly once;
* every immediate-upper resource demanded in (5.3) exactly once;
* positive and negative depth-`d` residence at every internal and join
  boundary;
* the same persistent private physical edge `e_*`;
* absolute voltage `+1`; and
* zero old/new relative displacement.

Using the completely reversed pump branch gives the corresponding `-1`
statement.

#### Proof

The degree rows and the fixed forward order give one spanning directed path
after deleting the closing join: every component is a forward path, and the
unique missing incoming and outgoing roles force a single component.
Adding the closing join gives one cycle.  Expanding the fragments is simple
by resource disjointness and (5.2); (5.3) gives the named exact palettes.
Internal residence is already proved for the pump and seven-ear paths, and
Section 4 proves it at every new join.

The final voltage is

\[
\begin{aligned}
 V
   &=\lambda(P_P)+\sum_{F\ne P_P}\lambda(F)
                         +\sum_e x_e\delta(e)\\
   &=\bigl(\lambda(P_P)+\delta(e_o)\bigr)
                         +\sigma_{\rm bg}\\
   &=1.
\end{aligned}
\tag{5.5}
\]

The opening edge is `e_o`, so `e_*` was never removed.  Finally, every
ambient term is the same in the two fixed-`z` phases, while (1.7) makes the
protected seven-ear contribution equal.  Their signed difference is zero.
\(\square\)

The theorem uses the pump only in the first parenthesis of (5.5).  The
seven-ear packet is already phase-neutral and is not assigned a fictitious
voltage-cancellation task.

### Corollary 5.2 (when ordinary rooted Hall suffices)

Suppose the fixed ordered split graph is capacity-faithful and every perfect
matching has the same background charge.  Then Theorem 5.1 is equivalent to:

1. the rooted split graph satisfies Hall; and
2. its one fixed background charge equals zero.

The second hypothesis holds, in particular, on A's rigid fixed-rail
coboundary face.  It must still be evaluated once: a fixed nonzero residue
cannot be changed by choosing a different Hall matching on that same face.

#### Proof

Capacity faithfulness makes perfect matchings equivalent to
(5.1)--(5.3), and Hall characterizes their existence.  Matching-independent
charge makes (5.4) a single table constant. \(\square\)

Outside that face, the charge row (5.4) is a genuine additional functional
matching constraint.  Separate Hall and voltage witnesses need not be the
same selection.

## 6. Accepted endpoint subatlases and the exact remaining host lemma

Let `mathcal A` be any family of accepted **joint local states**.  A member
may be a cover-preserving affine pump image together with a compatible
seven-ear packet, or it may keep the pump fixed and vary the Johnson-far
seven-ear anchor/ticket.  In every member, the planting-edge endpoints
already belong to accepted incoming/outgoing socket states of one fixed
ambient table.  For a forbidden typed resource `q`, let `Delta_t(q)` be the
number of members of `mathcal A` using `q`.

### Lemma 6.1 (accepted-subatlas avoidance)

An accepted joint state avoiding `Q` exists whenever

\[
             |\mathcal A|>
               \sum_t\sum_{q\in Q_t}\Delta_t(q).
\tag{6.1}
\]

#### Proof

The right side is an upper bound on the number of accepted states
deleted by the forbidden resources. \(\square\)

For a full cover-normalizer orbit, (2.2)--(2.3) give the exact
orbit-stratified loads in (6.1).  Full-rank `S_n` loads are unavailable.
For an endpoint-conditioned joint subatlas there is presently no theorem
giving balanced loads.  This is the first genuinely open correlation row,
not the central supply or the seven-ear collision row.

The weakest remaining all-dimension statement is therefore:

> **Pump-aware rooted host lemma.**  After fixing one opened seven-ear
> packet and its `O(d)` protected owner/q1 bank, there is a compatible
> same-cover marked pump/packet state and one capacity-faithful rooted
> fragment table such that the
> endpoint-accepted subatlas satisfies (6.1), the rooted Hall/common-base
> row is feasible, and its coherent background charge (5.4) is zero.

A proof may replace capacity faithfulness by the exact resource master
(5.1)--(5.3).  It may also use a transparent fusion tree.  What it may not
do is add the pump to a frozen factor, use the small protected-factor
theorem on `6n` pump incidences, or infer endpoint compatibility from the
unconditioned orbit loads.

## 7. Scope

The note proves:

1. exact orbit-stratified resource loads for every cover-preserving marked
   pump orbit;
2. an explicit Johnson-ball inequality which gives disjoint same-cover
   pump/seven-ear local banks for `d=O(sqrt(r))` and all sufficiently large
   `r`;
3. the necessity and sufficiency of a separate planting edge if the
   original private edge is to survive;
4. the literal two-sided endpoint history equations;
5. the exact zero-background charge equation which makes the pump the sole
   absolute-voltage source; and
6. a proof-safe conditional ambient planting theorem.

It does not prove:

1. the pump-aware rooted host lemma of Section 6;
2. arbitrary upper shadows beyond rows explicitly included in (5.3);
3. exterior source/envelope factorization;
4. terminal common-cap/compiler feasibility; or
5. a same-parity `B+O(1)` or exact upper bound.

The corrected architecture is therefore:

\[
 \boxed{
 \text{fix equivariant unit pump}
 \ \longrightarrow\ 
 \text{choose a Johnson-far seven-ear bank}
 \ \longrightarrow\ 
 \text{complete one joint rooted host}
 \ \longrightarrow\ 
 \text{apply only zero-holonomy later repairs}.}
\]
