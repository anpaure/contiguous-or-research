# `k=17` common-DM circuit selector criterion

Date: 2026-08-01  
Lane: serial rooted-flag support `<=2`  
Status: exact necessary common-first filters and exact incremental matching
score.  This is not an induced common-state cycle cover or a `k=17` word.

## 0. Verdict

For a complete static rooted factor, form the bipartite graph whose left
vertices are the 1430 roots, whose right vertices are the 1430 attachment
owners, and whose edge `(p,O)` is present exactly when the unique aligned
state at that incidence has at least one globally literal incoming and one
globally literal outgoing state arc.  A perfect matching in this **both-live
graph** is necessary for any common root/owner occurrence cycle cover.

Let `M` be a maximum matching, let `X` be the roots alternating-reachable
from all `M`-unmatched roots, and put `Y=N(X)`.  If a circuit packet raises
the common matching by `r`, its fully rebuilt graph must satisfy

\[
                         |N'(X)|\ge |Y|+r.                 \tag{0.1}
\]

This is a net distinct-owner condition: new owners reached from `X` must
outnumber old neighbours of `X` lost entirely by at least `r`.  A single
new incidence raises the matching precisely when it joins the DM plus
region to the DM minus region.  For an update that also deletes incidences,
retain the surviving edges of `M` and augment in the updated graph; this is
an exact incremental score.

All incidence changes must be derived from the aggregate final row table.
Per-circuit liveness or matching gains are not additive.

## 1. The common both-live projection

Let `P` and `O` be the root and owner shores, with
`|P|=|O|=n=1430`.  There are nine aligned attachment states at every root
and nine at every owner.  Hence each incidence `(p,O)` has at most one
aligned state, denoted `s(p,O)` when it exists.

For a static factor `F`, let `D_F` be its fully rebuilt loop-free literal
state digraph.  Write

\[
 i_F(s)=|\delta^-_{D_F}(s)|,\qquad
 o_F(s)=|\delta^+_{D_F}(s)|,
\]

with multiplicity or support reference counts retained consistently, and
define

\[
 \lambda_F(s)={\bf1}_{i_F(s)>0}{\bf1}_{o_F(s)>0}.          \tag{1.1}
\]

The common both-live graph is

\[
 G_F=(P,O,E_F),\qquad
 (p,O)\in E_F\iff \lambda_F(s(p,O))=1.                    \tag{1.2}
\]

### Lemma 1.1 (necessary common transversal)

Every occurrence-state cycle cover using one state at each root and each
owner induces a perfect matching in `G_F`.

#### Proof

The selected state at a root has a selected incoming and outgoing arc, so
it is both-live in the full literal state digraph.  Its root and owner give
an edge of `G_F`.  One selected state per root and per owner makes these
edges a perfect matching.  The converse need not hold: the incoming and
outgoing arcs witnessing liveness may use incompatible unselected states or
may fail statewise flow and connectedness.  `square`

Thus

\[
                         m(F):=\nu(G_F)                    \tag{1.3}
\]

is an exact necessary common-first score, not a sufficient chronology
certificate.

## 2. Hall-shore circuit filter

Fix a maximum matching `M` of `G=G_F`, of size `m`.  Orient every
nonmatching edge root-to-owner and every matching edge owner-to-root.  Let
`X` be the roots reachable from all unmatched roots and let `Y` be the
reachable owners.  Standard alternating reachability gives

\[
              Y=N_G(X),\qquad |X|-|Y|=n-m=:\delta.        \tag{2.1}
\]

Let a legal circuit packet `C` produce the aggregate final factor `F_C` and
graph `G_C`.

### Theorem 2.1 (net-shore inequality)

If `m(F_C)>=m+r`, then

\[
                         |N_{G_C}(X)|\ge |Y|+r.            \tag{2.2}
\]

Equivalently, with

\[
 A_X(C)=N_{G_C}(X)\setminus Y,
 \qquad L_X(C)=Y\setminus N_{G_C}(X),
\]

one necessarily has

\[
                         |A_X(C)|-|L_X(C)|\ge r.           \tag{2.3}
\]

The same inequality holds for every old maximum-deficiency shore `Z`, with
`|Z|-|N_G(Z)|=delta`.

#### Proof

For every balanced bipartite graph `H`, Hall's min-max formula is

\[
 \nu(H)=n-\max_{S\subseteq P}
                  \bigl(|S|-|N_H(S)|\bigr).               \tag{2.4}
\]

If `nu(G_C)>=m+r`, the deficiency of every root set, in particular `X`, is
at most `n-m-r=delta-r`.  Using (2.1),

\[
 |X|-|N_{G_C}(X)|\le\delta-r
 \quad\Longrightarrow\quad
 |N_{G_C}(X)|\ge |X|-\delta+r=|Y|+r.
\]

Finally,
`|N_{G_C}(X)|=|Y|-|L_X(C)|+|A_X(C)|`, which gives (2.3).
The identical argument applies to every old shore of deficiency `delta`.
`square`

This is an exact rejection filter, but crossing one certified shore is not
sufficient.  A different old critical shore may remain tight, and deletions
may create a new bottleneck.  The full exact condition is (2.4) applied to
all root sets in the final graph.

## 3. The sharper DM insertion filter

Let `U` be the unmatched roots and `W` the unmatched owners under `M`.
In the alternating orientation above, define

\[
 P^+=\operatorname{Reach}(U)\cap P=X,
 \qquad
 O^-=\{O: O\leadsto W\}.                                  \tag{3.1}
\]

The plus and minus regions are disjoint because `M` is maximum.

### Theorem 3.1 (one-incidence DM criterion)

For a new edge `e=(p,O)` not in `G`,

\[
 \nu(G+e)=m+1
 \quad\Longleftrightarrow\quad
 p\in P^+\ \hbox{and}\ O\in O^-.                         \tag{3.2}
\]

#### Proof

If the two memberships hold, concatenate an old alternating path from an
unmatched root to `p`, the new edge `e`, and an old alternating path from
`O` to an unmatched owner.  This is an `M`-augmenting path, so the matching
increases.  One inserted edge can raise matching size by at most one.

Conversely, any `M`-augmenting path in `G+e` must use `e`, since `M` was
maximum in `G`.  Its prefix and suffix lie in `G`, proving respectively
`p in P+` and `O in O-`.  `square`

For a packet with new incidence set `A_C`, orient every member of `A_C`
root-to-owner and add it to the old alternating digraph.  Then

\[
 \nu(G\cup A_C)>m
 \quad\Longleftrightarrow\quad
 U\leadsto W\text{ in the augmented alternating digraph}.\tag{3.3}
\]

Equivalently, the added arcs must make the DM condensation connect plus to
minus.  A path in (3.3) may use several new incidences.  Therefore testing
each incidence or circuit separately is not a sound packet rejection rule.

If the actual final graph also deletes edges, then
$G_C\subseteq G\cup A_C$.  Consequently (3.3) remains a necessary
**optimistic** filter, but final matching repair is required for an exact
score.

## 4. Nonadditive liveness of a circuit packet

Let `T` be the union of the changed roots of a packet.  Apply every new row
option first, and only then rebuild every transition geometry whose source
or target root lies in `T`.  No other physical geometry can change.

For a state `s`, let `a_C^-(s),d_C^-(s)` be its aggregate added and deleted
incoming arc counts, and let `a_C^+(s),d_C^+(s)` be the corresponding
outgoing counts.  Its exact final liveness is

\[
\lambda_{F_C}(s)=
 {\mathbf 1}_{i_F(s)-d_C^-(s)+a_C^-(s)>0}
 {\mathbf 1}_{o_F(s)-d_C^+(s)+a_C^+(s)>0}.               \tag{4.1}
\]

For a prospective crossing incidence
$(p,O)\in X\times(O\setminus Y)$,
the baseline state is not both-live.  It becomes an edge exactly when every
zero side in (4.1) receives a new supporting arc and every formerly positive
side remains positive after deletions.

There are three separate nonadditivities.

1. A transition between roots changed by two different circuits is tested
   on the pair of final options; it is not the sum of the two one-circuit
   baseline deltas.
2. One circuit may repair the missing incoming side of a state and another
   its missing outgoing side.  Neither circuit creates the edge alone.
3. Hall expansion counts distinct owner neighbours, and maximum matching is
   itself nonlinear.  Several new states with the same owner count only
   once in (2.3).

In particular, a legal support-two circuit need not change a root in `X` in
order to create a crossing incidence: changing the other endpoint of an arc
can change liveness at an unchanged state in `X`.

## 5. Exact incremental common-first scorer

Maintain the active physical geometries, state in/out reference counts,
both-live bits, common adjacency, a maximum matching `M`, and the current DM
shore.  To score one circuit or a root-disjoint packet:

1. install all proposed final row options simultaneously;
2. collect and retest once every geometry incident with a changed root;
3. journal its active/inactive toggles and update the state counts in (4.1);
4. toggle `(root(s),owner(s))` exactly when the both-live bit of `s` changes;
5. maintain `c_O=|{p in X:(p,O) in E}|`; reject a requested gain `r` when
   fewer than `|Y|+r` counters are positive;
6. optionally apply the aggregate DM test (3.3);
7. repair the matching in the fully updated common graph and use its size as
   the exact primary score; and
8. rollback the journal for a rejected candidate.  After acceptance,
   recompute the alternating shore/DM decomposition before the next serial
   round.

The matching repair in step 7 has an exact stopping criterion.

### Theorem 5.1 (surviving-matching update)

Let

\[
 M_0=M\cap E(G_C),\qquad q=m-|M_0|.                       \tag{5.1}
\]

Starting from `M_0`, repeatedly augment in `G_C` until no augmenting path
remains.  If `a` augmentations occur, then

\[
                 \nu(G_C)=m-q+a.                          \tag{5.2}
\]

Hence the common matching gains at least `r` exactly when

\[
                              a\ge q+r.                    \tag{5.3}
\]

#### Proof

`M_0` is a valid matching of size `m-q`.  Each augmentation increases its
size by one.  When no augmenting path remains, Berge's theorem says the
resulting matching is maximum in `G_C`, proving (5.2) and (5.3).  `square`

This update handles simultaneous additions and deletions.  Re-running
Hopcroft--Karp from the surviving matching is a simple exact implementation;
the locality is in the geometry and liveness update, not an unproved local
matching approximation.

A common-first selector should compare, lexicographically,

\[
 (\nu(G_F),\ \hbox{packet matching},\ -\hbox{zero-out},
 \ -\hbox{zero-in}),                                       \tag{5.4}
\]

while retaining an independently rebuilt terminal replay.

## 6. What a no-gain sweep proves

An exhaustive sweep of a catalogue regenerated relative to the **current**
factor, with every legal support-one and support-two circuit evaluated by
the aggregate procedure above, proves only one-circuit local maximality for
that stated score and neighbourhood.

If an implementation tests only adding an unselected circuit or replacing
at most one conflicting selected circuit, while skipping selected-circuit
removals and candidates conflicting with two selected circuits, a no-gain
pass proves local maximality only for that smaller toggle neighbourhood.
Likewise, a catalogue generated relative to an earlier seed does not certify
the freshly regenerated support-two neighbourhood of the final factor.

It does **not** prove any of the following:

* that two or more root-disjoint circuits have no gain;
* that a neutral move cannot expose a later gain or move the Hall shore;
* global optimality or impossibility of a perfect common transversal;
* that common matching `1430` would itself induce a state cycle cover; or
* upper-shadow, residence, voltage, connectedness, opening, or compiler
  feasibility.

The simplest packet countermechanism is exact: one circuit supplies the last
incoming arc of a crossing state and another supplies its last outgoing arc.
Each single-circuit sweep score is unchanged, while the pair creates a new
both-live edge and may complete a plus-to-minus augmenting path.

## 7. `k=17` calibration

For the factor whose loop-free packet matching is `954`, the independently
rebuilt common graph has

```text
both-live incidences / common matching / deficiency    1290 / 718 / 712
alternating Hall root shore / owner neighbourhood        770 / 58
DM minus owners / core owners                              938 / 434.
```

Thus `770-58=712`.  Any candidate gaining `r` common units must leave those
770 roots with at least `58+r` distinct final owner neighbours.  A clean
single-incidence augmenter must start at one of the 770 plus roots and end
at a DM-minus owner; merely landing outside the 58-neighbour shore is not
sufficient.

For the serial round-two reverse factor, whose packet matching is `1178`,
the corresponding audit is

```text
both-live incidences / common matching / deficiency    1741 / 936 / 494
alternating Hall root shore / owner neighbourhood       652 / 158.
```

Again `652-158=494`.  The next gain `r` requires at least `158+r`
neighbours of this new 652-root shore.  The change from `770/58` to
`652/158` is why a selector must rebuild the maximum matching and DM shore
after every accepted serial factor rather than price all rounds against one
frozen cut.

## 8. Exact scope

The both-live graph, Hall filters, DM insertion test, nonlinear liveness
replay, and surviving-matching update above are exact for the stated common
root-owner necessary projection of a complete static factor.  They do not
select compatible incoming and outgoing state arcs, enforce statewise flow,
eliminate subtours, or address upper rows and the downstream compiler.
