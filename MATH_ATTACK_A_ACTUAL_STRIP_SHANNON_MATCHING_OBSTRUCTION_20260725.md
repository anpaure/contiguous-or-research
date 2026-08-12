# An actual return-free Shannon cut for the protected-strip multicover

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, web input, or
fixed-rank colouring theorem is used.

## 0. Result and scope

Let (Q,ell,H,m) tend through integers such that

\[
 d:=\ell-1,qquad g=d+2Q=\ell+2Q-1,qquad
 4Q\le d,qquad Q\le g\le H-Q,
 \tag{0.1}
\]

and

\[
 m-d\ge 6Q,qquad m+3H-d\le 2m.
 \tag{0.2}
\]

These inequalities hold eventually in the calibrated return-free regime
(Q=o(\ell)), (H=o(m)), (g\le H-Q).

The desired hereditary matching estimate

\[
 \nu({\cal F})\ge (1-o(1/Q)){|{cal F}|\over D}
 \tag{0.3}
\]

is false for rational multicovers of actual return-free protected strips,
even when (D) is the ambient maximum target degree and not a degree
renormalized inside ({\cal F}).

More precisely, for every sufficiently large admissible parameter tuple and
every suitable even integer \(\mu=m^{O(1)}\), there is a rational protected
strip multicover with the following properties.

1. Every path is a literal radius-(Q), return-free rotor chunk on an
   ((m+H))-carrier.
2. Every tag has total rational mass one and every protected target has load
   at most one.
3. Every path type has weight exactly (1/\mu).
4. After clearing denominators by any multiple (D) of \(\mu\), every tag
   and target has degree at most (D), and some targets have degree (D).
5. The cleared multicover contains a submultifamily \({\cal F}\) with

   \[
    |{cal F}|={3D\over2},qquad \nu({\cal F})=1.
    \tag{0.4}
   \]

Thus (0.3) would say (1\ge(3/2)(1-o(1/Q))), which is false.  The
obstruction is the exact Shannon triangle: three tag bundles meet cyclically
in three different middle owners.  Across distinct tags every raw protected
intersection is either empty or a singleton, so the protected nonlinear
width-two moment is identically zero on the obstruction.

This closes the proposed theorem for the **class** of legal protected-strip
multicovers.  It does not prove that the one particular uniform rational
point produced by a previously fixed isolated-pruning outcome contains the
three half-fibres constructed below.  That narrower statement remains open
and is isolated in Section 7.

## 1. The exact protected strip

An oriented length-(g) geodesic parameter on a carrier (U) is a disjoint
decomposition

\[
 U=C\ \dot\cup\ \{a_1,\ldots,a_g\}\ \dot\cup\
   \{b_1,\ldots,b_g\}\ \dot\cup\ R,
 \tag{1.1}
\]

where

\[
 |C|=m-g,qquad |R|=H-g.
\]

Its owner sequence and grid are

\[
 X_t=C\cup\{a_{t+1},\ldots,a_g\}
        \cup\{b_1,\ldots,b_t\},
 \tag{1.2}
\]

\[
 G_{i,j}=C\cup\{a_{i+1},\ldots,a_g\}
          \cup\{b_1,\ldots,b_j\}.
 \tag{1.3}
\]

The physical phase interval is

\[
 I=\{Q,Q+1,\ldots,g-Q\},qquad |I|=\ell.
 \tag{1.4}
\]

The complete raw protected support is

\[
 {\cal S}_Q(P)=
 \{G_{t,t}:t\in I\}
 \cup
 \{G_{t+q,t},G_{t-q,t}:t\in I, 1\le q\le Q\}.
 \tag{1.5}
\]

The two signed cells at depth (q) are, exactly,

\[
 L_q(t)=G_{t+q,t},qquad U_q(t)=G_{t-q,t}.
 \tag{1.6}
\]

A priority-decorated path claims a subset of (1.5), but it always claims
all middle owners (X_t=G_{t,t}).  It will therefore be enough to construct
three raw supports with pairwise intersections equal to three distinct
middle owners.

For completeness, every parameter (1.1) is physical under (0.1).  Initialize
the radius-(Q) queue with (a_1,\ldots,a_Q), put
(C\cup\{a_{Q+1},\ldots,a_g\}) in the lower block, and take the initial
upper queue from (R), possible because (H-g\ge Q).  At transition (t)
use arrival (b_{t+1}).  For (t<g-Q), enqueue (a_{t+Q+1}); in the final
(Q) transitions enqueue unused points of (C).  The scheduled departures
are then (a_1,\ldots,a_g), so the literal owner recurrence is (1.2).
No coordinate returns.

## 2. Three carriers and three long geodesics

Choose mutually disjoint blocks

\[
 |K_0|=m-d,qquad
 |A_{12}|=|A_{23}|=|A_{31}|=d,qquad
 |R_1|=|R_2|=|R_3|=H-d.
 \tag{2.1}
\]

Their union has size (m+3H-d\le2m), so they fit in the Boolean ground
set.  Define

\[
 \begin{aligned}
 U_1&=K_0\cup A_{12}\cup A_{31}\cup R_1,\\
 U_2&=K_0\cup A_{12}\cup A_{23}\cup R_2,\\
 U_3&=K_0\cup A_{23}\cup A_{31}\cup R_3.
 \end{aligned}
 \tag{2.2}
\]

Each (U_i) has size (m+H), and

\[
 U_i\cap U_j=X_{ij}:=K_0\cup A_{ij},qquad |X_{ij}|=m.
 \tag{2.3}
\]

The three (X_{ij}) are distinct.

Choose six mutually disjoint (Q)-sets

\[
 K_i^-,K_i^+\subset K_0qquad(1\le i\le3),
 \tag{2.4}
\]

and disjoint (Q)-sets (R_i^-,R_i^+\subset R_i).  This is possible by
(0.1)--(0.2), since (H-d\ge3Q).  Write

\[
 R_i^0=R_i\setminus(R_i^-\cup R_i^+),qquad |R_i^0|=H-g\ge Q.
 \tag{2.5}
\]

Construct the three oriented paths

\[
 P_1:X_{12}\longrightarrow X_{31},qquad
 P_2:X_{12}\longrightarrow X_{23},qquad
 P_3:X_{23}\longrightarrow X_{31}.
 \tag{2.6}
\]

For (P_i), let \(\alpha_i\) be an order of its starting (d)-block and
\(\beta_i\) an order of its ending (d)-block.  Its complete departure and
arrival orders are

\[
 a^{(i)}=(R_i^-;\alpha_i;K_i^+),qquad
 b^{(i)}=(K_i^-;\beta_i;R_i^+),
 \tag{2.7}
\]

its persistent core is

\[
 C_i=K_0\setminus(K_i^-\cup K_i^+),
 \tag{2.8}
\]

and its unused carrier block is (R_i^0).  The sizes in (1.1) are exact:

\[
 |C_i|=m-d-2Q=m-g,qquad |a^{(i)}|=|b^{(i)}|=g.
\]

At time (Q), the first buffer has exchanged (R_i^-) for (K_i^-), so
the owner is the indicated start (K_0\cup A).  At time (Q+d=g-Q), the
central exchange is complete and the owner is the indicated end
(K_0\cup B).

Choose the central orders so that

\[
 \alpha_1[1,Q]\cap\alpha_2[1,Q]=\varnothing
       \quad\hbox{inside }A_{12},
 \tag{2.9}
\]

\[
 \beta_1[d-Q+1,d]\cap\beta_3[d-Q+1,d]=\varnothing
       \quad\hbox{inside }A_{31},
 \tag{2.10}
\]

and

\[
 \beta_2[d-Q+1,d]\cap\alpha_3[1,Q]=\varnothing
       \quad\hbox{inside }A_{23}.
 \tag{2.11}
\]

Here an interval denotes the underlying set of entries in those positions.
The conditions are possible because (d\ge2Q).

## 3. Exact raw-intersection theorem

### Lemma 3.1 (lower cells which lie in an endpoint)

Consider one path in Section 2, with start (X_A=K_0\cup A), end
(X_B=K_0\cup B), central departure order \(\alpha\), central arrival
order \(\beta\), and post-buffer departure order \(\kappa^+\) on (K^+).

For (1\le q\le Q), the only lower cell contained in (X_A) is

\[
 L_q(Q)=X_A\setminus\alpha[1,q].
 \tag{3.1}
\]

The lower depth-(q) cells contained in (X_B) are indexed by
(0\le r\le q) and are exactly

\[
 L_q(Q+d-r)=
 X_B\setminus
 \bigl(\beta[d-r+1,d]\cup\kappa^+[1,q-r]\bigr).
 \tag{3.2}
\]

#### Proof

After the start phase, every owner contains at least one already arrived
point of (B\setminus X_A).  A lower cell deletes future departure points
and never deletes an arrived point.  Hence only the start phase can give a
lower cell contained in (X_A), and (1.2) gives (3.1).

At phase (Q+d-r), exactly the last (r) entries of \(\beta\) have not yet
arrived and exactly (r) central departure points of (Asetminus X_B)
remain.  The next (q) departures remove all of them if and only if
(r\le q).  The other (q-r) removed points are the first (q-r)
post-buffer entries in (K^+\subset X_B).  This gives (3.2).  If (r>q),
at least one point of (A\setminus X_B) remains, so the lower cell is not
contained in (X_B). \(\square\)

### Theorem 3.2 (literal loose triangle)

The three complete raw supports constructed above satisfy

\[
 \boxed{
 {\cal S}_Q(P_1)\cap{\cal S}_Q(P_2)=\{X_{12}\},\quad
 {\cal S}_Q(P_2)\cap{\cal S}_Q(P_3)=\{X_{23}\},\quad
 {\cal S}_Q(P_3)\cap{\cal S}_Q(P_1)=\{X_{31}\}.}
 \tag{3.3}
\]

#### Proof

Every target of (P_i) is a subset of (U_i).  A common target of
(P_i,P_j) is therefore contained in (U_i\cap U_j=X_{ij}), which has
size (m).  An upper target has rank greater than (m), so cannot be
common.  A common owner has rank (m), and hence must equal (X_{ij}).
Thus it remains only to exclude common lower cells.  Equal lower cells
have equal rank and therefore the same depth (q).

For (P_1,P_2), the common owner is the start (X_{12}) of both paths.
Lemma 3.1 says that the only possible common depth-(q) lower cells are

\[
 X_{12}\setminus\alpha_1[1,q],qquad
 X_{12}\setminus\alpha_2[1,q].
\]

Their deleted sets are nonempty and disjoint by (2.9), so they are unequal.

For (P_1,P_3), the common owner is the end (X_{31}) of both paths.
By (3.2), a possible common depth-(q) lower cell deletes, on each side,
a suffix of length (r\le q) from the corresponding \(\beta\)-order and
a prefix of length (q-r) from the corresponding (K_i^+)-order.  If
both suffixes are nonempty, they lie in the disjoint last-(Q) sets from
(2.10).  If exactly one is nonempty, the two deleted sets have different
(A_{31})-parts.  If both are empty, the two deleted sets are nonempty
prefixes of the disjoint sets (K_1^+,K_3^+).  Equality is impossible in
all cases.

For (P_2,P_3), (X_{23}) is the end of (P_2) and the start of (P_3).
A possible lower cell of (P_2) deletes

\[
 \beta_2[d-r+1,d]\cup\kappa_2^+[1,q-r]
\]

for some (0\le r\le q), whereas the only possible lower cell of (P_3)
deletes \(\alpha_3[1,q]\subset A_{23}\).  If (r<q), the former set has
a nonempty (K_0)-part and the latter does not.  If (r=q), the two
(A_{23})-sets are disjoint by (2.11).  Again equality is impossible.

The three owners in (3.3) themselves occur at the displayed physical
endpoints, so (3.3) follows. \(\square\)

Every priority-decorated version of these paths still claims the three
middle owners.  Since its claimed set is a subset of its raw support,
Theorem 3.2 holds verbatim for claimed targets.  In particular the
construction is independent of where the shallow priority zeros are put.

## 4. Diffuse triangle bundles and fillers

Fix all order entries used in (2.9)--(2.11), and vary only unconstrained
middle entries of one central order in each path.  Reversal is the only
possible second oriented presentation of a simple geodesic support.  Thus
each (P_i) has at least

\[
 {1\over2}(d-2Q)!
 \tag{4.1}
\]

distinct simple variants with the same endpoint data.  The proof of
Theorem 3.2 used only the fixed first/last (Q) entries, so every variant
of one bundle meets every variant of another bundle in exactly the same
anchor (X_{ij}).

Choose an even polynomially bounded integer

\[
 \mu\le(d-2Q)!.
 \tag{4.2}
\]

After decreasing \(\mu\) by a harmless factor two if necessary, take
(\mu/2) distinct triangle variants above each tag (U_i); call this
family \({\cal P}_i\).

We also need (\mu/2) filler variants above each tag.  The following
finite-avoidance observation supplies them.

### Lemma 4.1 (polynomial finite avoidance)

Let (U\in\binom{[2m]}{m+H}), and let \({\cal Z}\) be a family of
(m^{O(1)}) Boolean targets of ranks in ([m-Q,m+Q]).  Then, for all
sufficiently large (m), there are (m^{O(1)}) distinct oriented
length-(g) geodesic supports on (U) whose complete raw protected
supports avoid \({\cal Z}\).

#### Proof

Choose an oriented parameter on (U) uniformly.  At any fixed grid slot
of rank (r), the target is uniform on \(\binom Ur\), by the transitive
action of the symmetric group of (U).  There are at most

\[
 \kappa:=(2Q+1)\ell=m^{O(1)}
 \tag{4.3}
\]

raw protected slots.  Hence

\[
 \Pr({\cal S}_Q(P)\cap{\cal Z}\ne\varnothing)
 \le {\kappa|{\cal Z}|\over
  \min_{|r-m|\le Q}\binom{m+H}{r}}=o(1).
 \tag{4.4}
\]

The denominator is superpolynomial because (H-Q\ge g\to\infty), while
the numerator is polynomial.  The full oriented parameter orbit is
superpolynomial, so the allowed set contains any prescribed polynomial
number of distinct supports. \(\square\)

Apply Lemma 4.1 sequentially.  Above (U_1), choose \(\mu/2\) distinct
fillers avoiding every triangle-variant target.  Above (U_2), also avoid
all targets of the first filler bundle, and above (U_3), avoid both
earlier filler bundles.  Call the resulting families \({\cal F}_i\).
Fillers inside one tag may intersect one another; fillers on different
tags are target-disjoint, and every filler is target-disjoint from every
triangle variant.

## 5. The exact matching-cut violation

Give every path in

\[
 \bigcup_{i=1}^3({\cal P}_i\cup{\cal F}_i)
 \tag{5.1}
\]

rational weight (1/\mu).  There are \(\mu\) paths above each tag, so every
tag has mass one.  At (X_{12}), precisely the two bundles
\({\cal P}_1,{\cal P}_2\) occur, each with mass (1/2); its target load is
one.  The same holds at (X_{23}) and (X_{31}).  Every nonanchor target
belongs to paths from at most one of the six half-mass bundles, and hence
has load at most (1/2).  Thus

\[
 \boxed{\max_v\sum_{P\ni v}x_P=1.}
 \tag{5.2}
\]

Let (D) be any multiple of \(\mu\), and replace every path type by
(D/\mu) labelled copies.  The cleared multihypergraph has tag degree
exactly (D), target degree at most (D), and target degree exactly (D)
at the three anchors.

Let \({\cal Q}\) be the submultifamily consisting of all copies of the
triangle variants and none of the fillers.  Its size is

\[
 |{\cal Q}|=
 3\cdot{\mu\over2}\cdot{D\over\mu}={3D\over2}.
 \tag{5.3}
\]

Two copies from the same \({\cal P}_i\) conflict at their common tag.  Two
copies from different triangle bundles share the corresponding anchor
(X_{ij}), by Theorem 3.2.  Hence \({\cal Q}\) is pairwise conflicting and

\[
 \boxed{\nu({\cal Q})=1.}
 \tag{5.4}
\]

Equations (5.2)--(5.4) prove (0.4), with (D) the ambient maximum target
degree.  They also give the rational matching-cover violation directly:

\[
 x\!\left(\bigcup_i{\cal P}_i\right)={3\over2},
 \qquad
 \max_{M\text{ matching}}
 x\!\left(M\cap\bigcup_i{\cal P}_i\right)={1\over\mu}.
 \tag{5.5}
\]

More invariantly, putting unit test weight on the triangle types gives
dual ratio (3/2) after normalizing by the tag/target capacity scale.

The construction survives protected three-antichain pruning: every
cross-tag triangle intersection is a singleton and every cross-tag filler
intersection is empty.  Same-tag alternatives are never a cross-tag bad
pair and are handled by the tag palette.

## 6. What happened to the projective-plane obstruction

For comparison, let \({\cal L}\) be a pairwise target-intersecting family
of distinct-tag supports of size at most \(\kappa\), and suppose every two
members meet in exactly one target.  If the family has no common target,
then

\[
 |{\cal L}|\le\kappa^2-\kappa+1.
 \tag{6.1}
\]

Indeed, fix (A,B\in{\cal L}) with (A\cap B=\{z\}), and choose
(F\in{\cal L}) avoiding (z).  At most \(\kappa\) members contain (z),
because their intersections with (F) must be distinct.  Every member
avoiding (z) is injected into
((A\setminus\{z\})\times(B\setminus\{z\})), giving at most
((\kappa-1)^2) of them.  This is the sharp projective-plane count.

Thus a pure singleton line system has an exact \(\kappa^2\) ceiling.  It
does not save the simultaneous multicover route.  The actual obstruction
above uses three **tag cliques** of half mass, with singleton intersections
only across different tags.  The three target-capacity inequalities are

\[
 x({\cal P}_1)+x({\cal P}_2)\le1,quad
 x({\cal P}_2)+x({\cal P}_3)\le1,quad
 x({\cal P}_3)+x({\cal P}_1)\le1,
 \tag{6.2}
\]

whose symmetric solution is (x({\cal P}_i)=1/2).  Their sum permits
total mass (3/2), whereas a matching uses at most one bundle.  This is
the first odd matching-polytope cut, already realized by literal strips.

## 7. Exact surviving boundary for the fixed pruning point

The theorem disproves any implication of the form

\[
 \begin{gathered}
 \text{literal return-free strips}+
 \text{tag/target capacities}+\text{width-two census}+\\
 \text{polynomially diffuse atoms}
 \quad\Longrightarrow\quad
 \nu({\cal F})\ge(1-o(1/Q))|{\cal F}|/D
 \end{gathered}
 \tag{7.1}
\]

for all rational points on the catalogue.

It does **not** show that a separately fixed isolated-pruning point assigns
half of each of three fibres to the cyclic bundles.  For that one point,
the minimal missing assertion is the weighted matching-cover inequality

\[
 \boxed{
 \sum_Px_Py_P
 \le(1+o(1/Q))
 \max_{M\text{ matching}}\sum_{P\in M}y_P
 \quad(y_P\ge0).}
 \tag{7.2}
\]

Already its restriction to every physical cyclic triple of tag subfamilies
must give

\[
 x({\cal A}_1)+x({\cal A}_2)+x({\cal A}_3)
 \le1+o(1/Q),
 \tag{7.3}
\]

whenever all cross pairs in \({\cal A}_i,{\cal A}_j\) share the cyclic
anchor (v_{ij}).  Star capacities give only the three pairwise
inequalities (6.2) and cannot imply (7.3).  A proof for the fixed point
must therefore establish an odd-cycle dispersal law using how that point
was chosen; protected-strip geometry and the current overlap moments alone
are insufficient.

## 8. Adversarial audit

1. **Ambient versus local (D).**  The (D) in (5.3) is the degree of the
   full cleared multicover.  It is not redefined after passing to
   \({\cal Q}\).  Tags have degree (D), anchors have degree (D), and no
   target has larger degree.
2. **No heavy-atom loophole.**  Every distinct support has weight
   (1/\mu) and multiplicity (D/\mu).  The obstruction persists for any
   polynomial \(\mu\) allowed by (4.2), including the retained-fibre scales
   used in the protected-strip route.
3. **Exhaustiveness of the intersection proof.**  Carrier intersections
   have size exactly (m), which rules out all common upper cells and
   forces every common owner.  Lemma 3.1 lists every lower cell that can
   lie in either endpoint; conditions (2.9)--(2.11) eliminate them all.
4. **Literal physicality.**  The queue construction after (1.6) realizes
   every displayed geodesic as an actual radius-(Q) return-free rotor
   chunk.  The obstruction is not an abstract target hypergraph.
5. **Pruning compatibility.**  All cross-tag intersections have size at
   most one, so neither a three-antichain rule nor a rectangle rule deletes
   a pair for geometric reasons.
6. **Remaining nonclaim.**  No assertion is made that the particular
   random isolated-pruning outcome already fixed elsewhere retains these
   three half-fibres.  Proving or refuting (7.2) for that fixed point is a
   strictly narrower problem.

The simultaneous multicover-colouring route therefore cannot use (0.3) as
a catalogue-wide theorem.  Its first exact additional requirement is
odd-cycle/weighted matching-cut control for the chosen rational point.
