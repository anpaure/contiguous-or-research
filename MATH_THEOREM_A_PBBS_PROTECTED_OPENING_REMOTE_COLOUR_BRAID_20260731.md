# Protected PBBS openings: exact multi-cut survival and the remote-colour braid obstruction

Date: 2026-07-31  
Lane: A, pure mathematics  
Status: unconditional exact opening calculus; unconditional zero-spill
sufficient theorem; unconditional remote-colour obstruction for canonical
wedge repair.  The existence of the required braid in every dimension is
**not** proved, so this note does not prove \(\nu(k)=B(k)\).

## 0. Result and boundary

Let \(F\) be a disjoint union of owner cycles in a Johnson graph.  This
note proves three statements.

1. For arbitrarily many cuts on a component, survival of an old interval
   witness has an exact blocker-clutter description.  After the fragments
   are ordered, every new witness has the exact
   suffix/full-fragments/prefix form.  Thus old survival and seam service
   give an exact, not merely sufficient, hole ledger.
2. A rooted braid which satisfies this ledger, recycles all but one deleted
   lower colour, and passes the exact deadline-staircase inequalities has
   zero opening loss.  This is a dimension-uniform protected-opening
   theorem.
3. Canonical wedge-ray repair has a previously hidden conflict with lower
   colour recycling.  The seam which repairs an active port can never
   recycle that port's own deleted lower colour.  Consequently exact
   \(q=1\) recycling is necessarily a **remote-colour derangement** across
   components.  In particular, two active components cannot be joined by
   one canonical repairing seam with the exact one-hole/no-excess profile
   \(H=1,E=0\).

The third statement is the minimal obstruction to a componentwise
safe-cut proof.  The remaining positive gate is a rooted, option-state
path whose seams simultaneously satisfy the upper key conditions, the
remote lower-colour permutation, and the deadline transducer.  PBBS
all-depth support does not imply that path.

## 1. Occurrence spans and multi-cut blockers

Let \(C\) be a directed cycle and let \({\cal I}_C^+(Y)\) be the
occurrence-labelled cyclic intervals on \(C\) whose union is the upper
target \(Y\).  If

\[
                 I=(X_a,X_{a+1},\ldots,X_b),
\]

write

\[
                 \operatorname{span}(I)
                    =\{X_aX_{a+1},\ldots,X_{b-1}X_b\}.
\tag{1.1}
\]

Length-one occurrences have empty span and can never be destroyed by
cutting edges.  Define the minimal blocker clutter

\[
 {\cal K}^{+}_C(Y)=
 \min_{\subseteq}\Bigl\{K\subseteq E(C):
       K\cap\operatorname{span}(I)\ne\varnothing
       \text{ for every }I\in{\cal I}_C^+(Y)\Bigr\}.
\tag{1.2}
\]

The minimum is under inclusion.  The analogous lower clutter
\({\cal K}^{-}_C(Z)\) is defined from occurrence-labelled intervals whose
intersection is \(Z\).

### Lemma 1.1 (exact multi-cut destruction)

For any cut set \(D_C\subseteq E(C)\), all old component witnesses for
\(Y\) are destroyed if and only if

\[
                    \exists K\in{\cal K}^{+}_C(Y),
                    \qquad K\subseteq D_C .
\tag{1.3}
\]

The identical assertion holds for lower intersection witnesses.

#### Proof

An old occurrence survives precisely when its entire internal edge span
avoids \(D_C\).  Thus all occurrences die precisely when \(D_C\) meets
every span.  Since the cycle is finite, every such transversal contains
an inclusion-minimal transversal, which is an element of (1.2).  The
converse is immediate.  The proof uses only spans, so it applies verbatim
to intersections. \(\square\)

For one cut \(D_C=\{e\}\), (1.3) is exactly the familiar cut-kernel test

\[
 e\in K_C(Y):=\bigcap_{I\in{\cal I}_C^+(Y)}
                       \operatorname{span}(I).
\tag{1.4}
\]

For two or more cuts, the one-edge kernel is not sufficient; the blocker
clutter is the correct invariant.

If

\[
                 \tau_C^\pm(Y)
                    =\min_{K\in{\cal K}_C^\pm(Y)}|K|,
\tag{1.5}
\]

then

\[
              |D_C|<\tau_C^\pm(Y)
              \quad\Longrightarrow\quad
              Y\text{ retains an internal component witness}.
\tag{1.6}
\]

This is exact.  In particular, independently kernel-safe edges need not be
jointly safe: two disjoint witness spans have empty one-edge kernel, while
one cut chosen in each span is a two-edge blocker.

## 2. The exact suffix/full/prefix theorem

Cut every component at least once.  Let
\(Q_1,\ldots,Q_s\) be all resulting nonempty oriented fragments and let
\(\pi\) order them in the linear braid

\[
                 T=Q_{\pi(1)}\Vert\cdots\Vert Q_{\pi(s)}.
\tag{2.1}
\]

For a fragment \(Q=(X_0,\ldots,X_{a-1})\), put

\[
\begin{aligned}
 V(Q)&=\bigcup_{i=0}^{a-1}X_i,&
 I(Q)&=\bigcap_{i=0}^{a-1}X_i,\\
 S_u^+(Q)&=\bigcup_{i=u}^{a-1}X_i,&
 P_v^+(Q)&=\bigcup_{i=0}^{v}X_i,\\
 S_u^-(Q)&=\bigcap_{i=u}^{a-1}X_i,&
 P_v^-(Q)&=\bigcap_{i=0}^{v}X_i.
\end{aligned}
\tag{2.2}
\]

### Theorem 2.1 (complete protected-opening identity)

An upper target \(Y\) occurs as an interval union of \(T\) if and only if
at least one of the following holds.

* Some old cyclic occurrence of \(Y\) has span disjoint from the cuts.
* For some \(a<b\) and valid \(u,v\),

  \[
  Y=S_u^+(Q_{\pi(a)})\cup
       \bigcup_{a<h<b}V(Q_{\pi(h)})\cup
       P_v^+(Q_{\pi(b)}).
  \tag{2.3}
  \]

Likewise, a lower target \(Z\) occurs as an interval intersection of
\(T\) if and only if an old occurrence survives or

\[
  Z=S_u^-(Q_{\pi(a)})\cap
       \bigcap_{a<h<b}I(Q_{\pi(h)})\cap
       P_v^-(Q_{\pi(b)})
\tag{2.4}
\]

for some \(a<b,u,v\).

#### Proof

An interval of \(T\) either lies in one fragment or has a unique first
and last fragment.  In the first case it is an old cyclic interval whose
internal span avoids every cut.  In the second case it consists of a
suffix of its first fragment, every complete intervening fragment, and a
prefix of its last fragment, giving (2.3) or (2.4).  Conversely every
displayed suffix/full/prefix expression is the union or intersection of
that literal interval of \(T\). \(\square\)

For a complete cut/order/orientation choice \(\omega\), let
\(B_Y^*\) be the event that every supporting component cut contains a
blocker from \({\cal K}_C^+(Y)\) and no expression (2.3) equals \(Y\).
Then the exact upper hole count is

\[
                       h^+(\omega)=\sum_Y 1_{B_Y^*}(\omega).
\tag{2.5}
\]

There is an identical formula for lower intersections.  Hence, for any
probability measure \(\mu\) on a **jointly admissible** atlas of physical
cut/order/seam choices,

\[
       \sum_Y\mu(B_Y^*)<1
       \quad\Longrightarrow\quad
       \text{some atlas state has zero upper spill}.
\tag{2.6}
\]

This is the multi-cut SPILL lemma.  The measure must live on jointly legal
states; independent marginal cut banks do not suffice.

### Corollary 2.2 (PBBS one-cut locality)

For a canonical odd PBBS component, site homomesy gives positive but
non-full occupancy for every coordinate.  A fragment obtained by one cut
contains every component vertex, and therefore

\[
                         V(Q)=[k],\qquad I(Q)=\varnothing .
\tag{2.7}
\]

Indeed, for every coordinate \(x\), some PBBS lower edge colour \(C\) in
the component contains \(x\), so both middle endpoints of that edge contain
\(x\).  Some edge colour \(C'\) omits \(x\); its two distinct one-point
extensions cannot both add \(x\), so at least one middle endpoint omits
\(x\).  Thus the middle-owner component really has full union and empty
intersection; this is not being inferred from component size alone.

Consequently every proper upper target and every nonempty lower target
which is newly created by a one-cut-per-component braid crosses exactly
one seam.  Its exact service catalogue is only the adjacent
suffix/prefix grid; no proper target can pass through a complete
intervening PBBS fragment.

### Corollary 2.3 (multi-cut wedge fallback)

Suppose every assigned rank-\((r+q)\) witness is a directed geodesic
\(q\)-edge interval and every selected cut is a designated wedge flank.
Across an arbitrary cut set \(D\), the number of distinct assigned old
casualties over all depths \(q\ge2\) is at most

\[
                              |D|(k-r-1).
\tag{2.8}
\]

Including depth one gives \(|D|(k-r)\).

#### Proof

A fixed-width geodesic cannot contain both flanks of a wedge: the two
wedge transitions enlarge their union by only one, so a \(q\)-edge
interval containing both has rank at most \(r+q-1\).  Hence a geodesic
using a designated cut flank is the unique outward ray on that side.  For
each cut and each depth there is therefore at most one assigned casualty.
There are \(k-r-1\) depths from two through \(k-r\).  Sum over the cuts.
\(\square\)

This is only an additive fallback.  Exact seam service in (2.3) can reduce
the loss, but the scalar bound alone does not imply zero spill or fit the
deadline staircase.

## 3. The lower \(q=1\) ledger

Assume now that the old factor is lower-rainbow: its Johnson edges use
each required rank-\((r-1)\) colour once.  Let \(D\) contain \(b\) cut
edges and hence produce \(b\) fragments.  Let \(j\) of the \(b-1\) new
seams be Johnson edges.  If \(H\) is the number of missing lower colours
and \(E\) is total lower-colour repeat excess, then

\[
                              \boxed{H-E=b-j.}
\tag{3.1}
\]

Indeed, cutting removes \(b\) coloured occurrences and the valid seams add
\(j\).  Comparing the resulting total load with the number of colours
gives (3.1).

In particular, if every seam is Johnson, then \(H-E=1\).  Moreover,

\[
 H=1, E=0
 \quad\Longleftrightarrow\quad
 \{\text{seam colours}\}
   \text{ is a distinct }(b-1)\text{-subset of }
 \{\text{cut colours}\}.
\tag{3.2}
\]

Thus scalar seam count is not the issue.  Exactness is a coloured
restitution problem.

## 4. Canonical wedge service excludes its own cut colour

Let \(w-u\) be a cut wedge flank in \(J(k,r)\), oriented so that an
outward geodesic ray begins

\[
                       w,u,u_2,\ldots,u_q.
\tag{4.1}
\]

Put

\[
       \{\kappa\}=w\setminus u,
       \qquad c=w\cap u.
\tag{4.2}
\]

Here \(\kappa\) is the departure key and \(c\) is the deleted lower
colour.  If the ray union has rank \(r+q\), geodesicity implies that
\(\kappa\) never returns after the first step.  Hence a foreign rank-\(r\)
endpoint \(v\sim u\) replaces \(w\) and reproduces every eligible ray
union if and only if

\[
                               \kappa\in v.
\tag{4.3}
\]

To justify both assertions, a \(q\)-edge interval can enlarge its running
union by at most one at each transition.  Rank \(r+q\) forces equality at
every transition.  If \(\kappa\) reappeared after \(u\), that transition
would insert a coordinate already present at the start and would not
enlarge the union.  Thus, writing
\(U_q=\bigcup_{i=1}^q u_i\), the old union is the disjoint union
\(U_q\mathbin{\dot\cup}\{\kappa\}\).  A neighbour \(v\sim u\) reproduces
it exactly iff it contains \(\kappa\): in that case \(\kappa\) is the
unique element of \(v\setminus u\), so
\(v\subseteq u\cup\{\kappa\}\subseteq U_q\cup\{\kappa\}\).

### Theorem 4.1 (remote-colour exclusion)

If \(v\ne w\) is a foreign endpoint, \(v\sim u\), and (4.3) holds, then

\[
                               v\cap u\ne c.
\tag{4.4}
\]

Thus a canonical seam which services an active wedge port cannot recycle
that port's own deleted lower colour.

#### Proof

Suppose instead that \(v\cap u=c\).  Since \(v\) and \(u\) are Johnson
neighbours, \(v=c\cup\{z\}\) for one \(z\notin u\).  Condition (4.3)
forces \(z=\kappa\).  But then

\[
                         v=c\cup\{\kappa\}=w,
\]

contrary to the endpoint being foreign. \(\square\)

### Corollary 4.2 (remote-colour SDR)

Consider a one-cut-per-component canonical wedge braid.  For each new seam
\(f\), let \(S(f)\subseteq[b]\) be the set of indices of incident active
ports canonically
serviced by \(f\).  Suppose the braid has \(H=1,E=0\).  Since the deleted
cut colours \(c_i\) are distinct, every seam has a unique index
\(\phi(f)\) such that its colour is \(c_{\phi(f)}\), and

\[
 \phi:E(\text{fragment path})\hookrightarrow[b],
 \qquad
 \phi(f)\notin S(f).
\tag{4.5}
\]

Exactly one cut-colour index is omitted from the image.

For two components, if the sole seam services both active ports, (4.5) is
impossible: its colour can be neither deleted colour.  For a three-component
path in which both seams service both incident ports, the only possible
pattern is

\[
          \operatorname{col}(f_{12})=c_3,\qquad
          \operatorname{col}(f_{23})=c_1,
\tag{4.6}
\]

up to reversal; \(c_2\) would be the unique boundary hole.  In fact this
formal pattern is itself physically impossible for three owner-disjoint
components.

More precisely, in the two-component case the foreign seam colour is an
uncut colour of the complete lower palette.  It therefore has final load
two, while both deleted colours have load zero:

\[
                              H=2,\qquad E=1.
\tag{4.7}
\]

### Theorem 4.3 (three-component reciprocal no-go)

There is no owner-disjoint three-component path for which both seams
canonically service both incident active ports and \(H=1,E=0\).

#### Proof

Write each opened component as
\(P_i=(s_i,\ldots,t_i)\), so its deleted edge is \(t_is_i\), its cut
colour is \(c_i=t_i\cap s_i\), and the seams are
\(t_1s_2,t_2s_3\).  By (4.6), their colours are \(c_3,c_1\).

Put

\[
                         s_2=C\cup\{a\},\qquad
                         t_2=C\cup\{b\},
\tag{4.8}
\]

where \(|C|=r-1\).  The first seam services component 2, so its foreign
endpoint \(t_1\) contains \(b=t_2\setminus s_2\).  Hence

\[
                         t_1=s_2-\{x\}+\{b\}
\tag{4.9}
\]

for some \(x\in s_2\).  If \(x=a\), then \(t_1=t_2\), contradicting owner
disjointness.  Thus \(x\in C\), and

\[
                         t_1\cap t_2=(C-\{x\})\cup\{b\}=:D.
\tag{4.10}
\]

The second seam has colour \(c_1\), so \(c_1\subset t_2\); being the cut
colour of component 1, also \(c_1\subset t_1\).  Both \(c_1\) and \(D\)
have rank \(r-1\), whence \(c_1=D\).

Finally, the first seam services component 1.  Its deleted-mate key
\(y=s_1\setminus t_1\) therefore lies in \(s_2\).  Since
\(s_1=c_1\cup\{y\}\), \(y\notin t_1\), and
\(s_2\setminus t_1=\{x\}\), we have \(y=x\).  Therefore

\[
                         s_1=D\cup\{x\}=C\cup\{b\}=t_2,
\]

again contradicting owner disjointness. \(\square\)

For the canonical keyed-ear architecture, the only palette pattern not
excluded by these arguments is the following necessary pattern.  If the
first seam services components 1 and 2 reciprocally while the second is a
one-way keyed ear servicing component 3, exact restitution forces

\[
            \operatorname{col}(f_{12})=c_3,\qquad
            \operatorname{col}(f_{23})=c_2,
\tag{4.11}
\]

leaving \(c_1\) exposed; reversal gives the symmetric pattern.  Indeed the
first equality follows from exclusion at both ends.  The second seam colour
is then \(c_1\) or \(c_2\); the proof above, which did not use service of
component 2 at the second seam, excludes \(c_1\).

This is a genuine global coupling.  Upper-safe choices cannot be made
component by component and followed by local lower-colour repair.

## 5. A zero-loss rooted protected-braid theorem

Assume in this section that \(k=2r-1\) is odd and central, and put

\[
                 W=\binom{k}{r}=\binom{k}{r-1}.
\tag{5.0}
\]

Fix one assigned old witness for every required upper target in a
lower-rainbow all-depth factor.  Cut one edge in each of its \(b\)
components and orient/order the resulting full fragments as

\[
                         Q_1\Vert\cdots\Vert Q_b.
\tag{5.1}
\]

Let \(T\) be the resulting owner chronology, so \(|T|=W\).

### Theorem 5.1 (rooted protected opening)

Assume all of the following.

1. **Safe root.**  The cut in \(Q_1\) avoids the span of every witness
   assigned to its component.
2. **Protected nonroots.**  Write
   \(Q_i=(u_i,\ldots,w_i)\), so the deleted edge is \(w_iu_i\).
   For every \(i\ge2\), each assigned witness destroyed by this cut is an
   outward fixed-width geodesic
   \((w_i,u_i,u_{i,2},\ldots)\), whose retained tail begins in this order
   inside \(Q_i\).  Put \(\kappa_i=w_i\setminus u_i\).  Then

   \[
                         w_{i-1}\sim u_i,\qquad
                         \kappa_i\in w_{i-1}.
   \tag{5.2}
   \]

3. **Remote rainbow restitution.**  All \(b-1\) seams are Johnson and
   their lower colours are precisely \(b-1\) distinct deleted cut
   colours.
4. **Deadline fit.**  Put \(d=B(k)-W\).  There is a nondecreasing integer
   start-threshold vector
   \(0\le G_0\le\cdots\le G_{d-1}\le W\).  Write

   \[
                       g_i=\#\{t:G_t\le i\}.
   \tag{5.3}
   \]

   Its exact run frontiers

   \[
   \rho_j^G=\max\bigl(
     \{a:[a,b]\text{ is an internal coordinate run of }T,
          (b-a+1)+g_{b+1}\le j\}\cup\{0\}\bigr)
          \qquad(1\le j\le d)
   \tag{5.4}
   \]

   give \(H^G_{j-1}=\rho_j^G\), satisfy the chain-alignment inequalities

   \[
       H_t^G\le G_t-\mathbf 1_{\{0<G_t<|T|\}},
   \tag{5.5}
   \]

   and obey

   \[
                  \operatorname{Loss}(G,H^G)
                         \le\operatorname{slack}(k).
   \tag{5.6}
   \]

   Here

   \[
   \begin{aligned}
   \operatorname{Loss}(G,H)
      &=\sum_tH_t+\sum_t(W-G_t)
          +\#\{(t,u):G_t<H_u\},\\
   \operatorname{slack}(k)
      &=dW+\binom{d+1}{2}-\sum_{j=1}^{r-1}\binom{k}{j}.
   \end{aligned}
   \tag{5.7}
   \]

Then opening and braiding causes no upper-target loss, the lower \(q=1\)
ledger is exactly \(H=1,E=0\), and the owner chronology fits a
length-\(B(k)\) chain-aligned deadline staircase.

If, in addition, every required lower owner target has an old surviving
witness or a literal cross-fragment witness of the form (2.4), then the
entire owner lower tower is also preserved.  If the exact common-cap
compiler conditions hold on this same staircase, the protected opening
contributes zero defect to the coefficient-one construction and implies

\[
                              \nu(k)=B(k).
\tag{5.8}
\]

#### Proof

The safe-root clause retains every target assigned to component 1.  For
\(i\ge2\), the protected outward-ray theorem says that every assigned
casualty has the form (4.1).  Replacing its deleted endpoint \(w_i\) by
\(w_{i-1}\) preserves the entire ray union because (5.2) is exactly the
departure-key condition (4.3).  These are literal intervals across the
new seam.  Hence every assigned upper target survives or is exactly
replaced.

Clause 3 and (3.2) give \(H=1,E=0\).  Equations (5.3)--(5.7) are the exact
arbitrary-start residence and scalar-capacity criterion: (5.4) is the
coordinatewise-minimal deadline vector, (5.5) is chain alignment, and
(5.6) is precisely the available staircase budget.  Thus the chronology
fits the required deadline staircase.  Theorem 2.1 gives the stated lower
owner-tower conclusion.  Finally, the exact common-cap hypothesis is the
additional literal lower realization condition; adding it gives a
zero-defect word at the lower bound. \(\square\)

### Corollary 5.2 (cut-colour/key conveyor)

In Theorem 5.1, put \(c_i=w_i\cap u_i\).  The remote-rainbow clause is
automatic if, for every \(i<b\),

\[
          w_i\cap u_{i+1}=c_i,\qquad
          \kappa_{i+1}\in w_i.
\tag{5.9}
\]

The seam after component \(i\) then recycles the source colour \(c_i\)
while its source endpoint carries the departure key which repairs component
\(i+1\).  The seam colours are exactly \(c_1,\ldots,c_{b-1}\), and \(c_b\)
is the unique boundary hole.

This is the simplest positive architecture compatible with Theorem 4.1:
each seam pays backward in lower colour and forward in upper service.

### Corollary 5.3 (local zero-debt collar test)

Suppose every fragment has no internal positive coordinate run shorter
than \(d+1\), and each coordinate is both present and absent somewhere in
every fragment.  At a seam \(P\Vert Q\), let
\(s_x(P)\) and \(p_x(Q)\) be the terminal and initial positive-run lengths,
zero when the corresponding endpoint omits \(x\).  If

\[
                  s_x(P)+p_x(Q)\in\{0\}\cup[d+1,\infty)
                  \qquad(x\in[k])
\tag{5.10}
\]

at every seam, then every internal run of the braid has length at least
\(d+1\).  The flat deadline staircase is therefore feasible with zero
residence debt.

#### Proof

An old internal run stays inside a fragment.  A new run meets a seam and
has length (5.10).  Because no fragment is all-one in any coordinate, one
run cannot cross two seams. \(\square\)

For a one-cut PBBS fragment, the second hypothesis follows from site
homomesy.  The first is a substantive residence condition and is not
supplied by raw PBBS.

## 6. Exact remaining gate and adversarial audit

Define the **remote-colour protected braid condition** \(\mathrm{RCPB}(k)\)
to be the existence of the cuts, orientations, order, target assignment,
remote colour restitution, and deadline data in Theorem 5.1.  This is the
smallest currently isolated opening hypothesis in the canonical
outward-ray architecture.

What PBBS supplies unconditionally is:

* the exact lower-rainbow owner factor;
* complete lower and complementary upper all-depth flag support;
* the outward-ray classification at a wedge cut;
* site homomesy, hence (2.7).

It does **not** supply:

* a root cut outside every assigned blocker;
* an option-state path satisfying all key containments;
* the remote-colour injection (4.5);
* the deadline inequalities and budget (5.3)--(5.6); or
* the final common-cap compiler.

The last bullet now has an exact structural wrapper: co-selectable trace
guards followed by the guarded interval/laminar Rado inequalities give an
integral common-cap compiler.  See
[MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md](MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md).
PBBS does not yet supply those guards or inequalities uniformly, so this
does not make the present opening theorem unconditional.

The strongest unconditional obstruction established here is Theorem 4.1.
It refutes the natural local strategy “repair a component at a wedge seam
and recycle that component's cut colour at the same seam.”  The exact
two-component consequence shows that even perfect upper reciprocal-key
repair may be incompatible with the required lower \(H=1,E=0\) profile.
Three or more components can evade the obstruction only by the remote
derangement (4.5), so the next proof must be global.

The obstruction is deliberately scoped.  A noncanonical expression in
the full suffix/full/prefix grid (2.3) can repair a target without the key
condition (4.3), and multiple cuts can change the blocker clutter.  Thus
Theorem 4.1 is not a no-go for arbitrary PBBS braids and not a
counterexample to \(\nu(k)=B(k)\).  It identifies the minimum extra
structure which any canonical zero-loss braid must prove.

There is also a sharp, separately proved staircase obstruction to the
most literal whole-component implementation.  In the frozen \(k=17\)
11-cycle double-\(q=1\) factor, nine cycles retain an internal run of
length two after every single cut.  Their total length is \(24300\), the
largest has length \(5536\), and therefore every one-cut-per-cycle
whole-block order with terminal omitted starts has

\[
              \rho_2+\rho_3\ge2(24300-5536)+2
                    =37530>7401=\operatorname{slack}(17).
\tag{6.1}
\]

Separately, the run-collar capacity bound already requires at least
\(325\) cuts to eliminate every old run of length two or three, whereas
one cut per cycle supplies only \(11\).  This is an exact no-go for that
frozen factor, those whole blocks, and the canonical-tail start schedule.
It does not exclude arbitrary omitted starts, multi-cut fragments, or
alternating rethreads which change old internal edges.  The proof and
independent payload are in
[MATH_THEOREM_A_K17_PROTECTED_PBBS_OPENING_MAX_POSITION_CUT_CHARGE_20260731.md](MATH_THEOREM_A_K17_PROTECTED_PBBS_OPENING_MAX_POSITION_CUT_CHARGE_20260731.md).

Accordingly, this route has not yet proved the conjecture.  It has reduced
protected opening to the exact, checkable conjunction \(\mathrm{RCPB}(k)\)
and proved that marginal safe cuts, marginal upper service, or marginal
lower-colour balance cannot establish that conjunction separately.
