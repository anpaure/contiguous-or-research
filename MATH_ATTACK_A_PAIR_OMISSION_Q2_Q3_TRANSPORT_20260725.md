# Pair-omission rows: bounded-degree category capacities and the exact (q=2,q=3) transport gate

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or web use.

## 0. Outcome

The first-avoided-pair construction of
`PAIR_OMISSION_TIGHT_ROW_MULTICOVER_20260725.md`, Section 5, has enough
freedom to remove its **category-total/prefix** obstruction at negligible
cost.  After discarding (o(W/H)) tail owners, one can prescribe exact
rank-two capacities (1+\mathbf 1_{C_2}) with

\[
 \max_{U\in{[n]\choose m-3}}
 |\{T\in C_2:U\subset T\}|=O(\log m),
\]

and with exact capacity equality in every first-avoided-pair category.
Moreover all canonical transitions which lower the category can be
discarded at a further cost (O(W\log ^2m/m)=o(W/H)).

There is nevertheless an exact rigidity statement for the source's
canonical outgoing orientation.  In that canonical column, the capacities
cannot be imposed by moving block cuts, radius starts, or endpoint collars.
For a rank-((m-2)) target (T) of category (h), its physical load is

\[
 \boxed{\mu _2(T)=\lambda_h(T)+\varepsilon_h(T),\qquad
        0\le \varepsilon_h(T)\le2,}
\]

where \(\lambda_h(T)\) is the number of adjacency edges of the chosen
local exact wreath factor (F_h) whose intersection is (T).  At the next
depth there is an analogous identity

\[
 \boxed{\mu _3(U)=\theta_h(U)+\eta_h(U),\qquad
        0\le \eta_h(U)\le2m+5,}
\]

where \(\theta_h(U)\) is the number of actual length-((m-3)) interval
occurrences in (F_h).  The vectors \(\lambda_h\) and \(\theta_h\) are
coupled by the same cyclic start order.  Cuts do not change either vector,
and arbitrary endpoint recollars can change only (O(qJ)) depth-(q)
occurrences, where (J=o(W/H)) is the number of retained path components.

Thus the bounded-codegree cyclic set from
`MATH_ATTACK_A_PROPORTIONAL_Q3_COLOR_SLACK_20260725.md` cannot be inserted
after the physical rows have been selected while retaining the canonical
column.  A two-shadow local-factor design theorem is a sufficient
canonical route.  For the full two-parent Pascal corridor, the more general
remaining object is a row-coherent monotone-path selection inside those
fixed factors.

## 1. Categories and canonical lower flags

Put

\[
 n=2m+1,
 \qquad V_q={ [n]\choose m-q}
 \quad(q\ge1),
 \qquad W={n\choose m}.
\]

Partition (2m) coordinates into ordered disjoint pairs

\[
 P_1,P_2,\ldots,P_m
\]

and leave one coordinate unpaired.  For every set which misses at least
one pair, put

\[
 \kappa(A)=\min\{h:A\cap P_h=\varnothing\}.
\tag{1.1}
\]

Every member of (V_1,V_2,V_3) has a finite category.  For each (h),
let (F_h) be an exact middle wreath factor on

\[
 Q_h=[n]\setminus P_h,
 \qquad |Q_h|=2m-1.
\]

Write a row of (F_h) as a cyclic order

\[
 \pi=(x_0,\ldots,x_{2m-2}),
\]

and put

\[
 S_i=I_\pi(i,m-1),\qquad
 T_i=I_\pi(i,m-2),\qquad
 U_i=I_\pi(i,m-3).
\tag{1.2}
\]

The first-avoided-pair extraction selects (S_i) precisely in phase
(h=\kappa(S_i)), and traverses the corresponding middle owners in the
orientation for which

\[
 T_i=S_i\cap S_{i-1},
 \qquad
 U_i=T_i\cap T_{i-1}.
\tag{1.3}
\]

Consequently every selected (S_i) owns the literal nested flag

\[
 U_i\subset T_i\subset S_i.
\tag{1.4}
\]

In particular,

\[
 \kappa(U_i)\le\kappa(T_i)\le\kappa(S_i).
\tag{1.5}
\]

This monotonicity is independent of the factors and of all cut choices.

## 2. Exact category-capacity constraints

For (r=1,2,3), write

\[
 \mathcal K_h^{(r)}=\{A\in V_r:\kappa(A)=h\},
 \qquad
 K_{\le h}^{(r)}=\bigcup_{j\le h}\mathcal K_j^{(r)}.
\tag{2.1}
\]

### Proposition 2.1 (prefix transport is necessary)

Suppose every (S\in V_1) is assigned a nested physical lower target
(f_q(S)\in V_q), (f_q(S)\subset S), and suppose the depth-(q) load
is exactly

\[
 1+\mathbf 1_{C_q}
\]

on (V_q).  Then, for every (h),

\[
 \boxed{
 |C_q\cap K_{\le h}^{(q)}|
 \ge |K_{\le h}^{(1)}|-|K_{\le h}^{(q)}|.}
\tag{2.2}
\]

#### Proof

By inclusion, (f_q(S)\subset S), so

\[
 \kappa(f_q(S))\le\kappa(S).
\]

Thus all owners in (K_{\le h}^{(1)}) must land in
(K_{\le h}^{(q)}).  The total capacity there is

\[
 |K_{\le h}^{(q)}|+|C_q\cap K_{\le h}^{(q)}|,
\]

which proves (2.2).  \(\square\)

This is a common-owner condition.  A rankwise choice of a high set which
does not satisfy (2.2) cannot be repaired by a later nested flow.

## 3. A bounded-down-degree high set satisfying every category total

Write

\[
 L_h=|\mathcal K_h^{(1)}|,
 \qquad M_h=|\mathcal K_h^{(2)}|.
\tag{3.1}
\]

### Lemma 3.1 (exact adjacent category ratio)

For every (1\le h<m),

\[
 \frac{m+1}{m-1}M_h\le L_h
 \le\frac{m+1}{m-h}M_h.
\tag{3.2}
\]

In particular, with (c_h=L_h-M_h),

\[
 0<c_h,
 \qquad
 \frac{c_h}{M_h}\le\frac{h+1}{m-h}.
\tag{3.3}
\]

#### Proof

Every (T\in\mathcal K_h^{(2)}) has exactly (m+1) supersets in
(\mathcal K_h^{(1)}): add any point of (Q_h\setminus T).  Conversely,
an (S\in\mathcal K_h^{(1)}) has (m-1) facets, and deleting a point can
lower its category only when that point is the unique point of (S) in
one of the (h-1) earlier pairs.  Thus between (m-h) and (m-1) of
its facets remain in category (h).  Double counting the same-category
incidences gives

\[
 (m+1)M_h
 =\sum_{S\in\mathcal K_h^{(1)}}d_h(S),
 \qquad m-h\le d_h(S)\le m-1.
\]

This is (3.2), and subtraction gives (3.3).  \(\square\)

Identify the ground set with \(\mathbb Z_n\) and color every
(T\in V_2) by

\[
 \sigma(T)=\sum_{x\in T}x\pmod n.
\tag{3.4}
\]

### Theorem 3.2 (category-exact logarithmic-codegree capacities)

Let (t=o(m)).  For all sufficiently large (m), there is a set

\[
 C_2^{(t)}\subseteq\bigcup_{h\le t}\mathcal K_h^{(2)}
\]

such that, for every (h\le t),

\[
 \boxed{|C_2^{(t)}\cap\mathcal K_h^{(2)}|=L_h-M_h,}
\tag{3.5}
\]

and

\[
 \boxed{
 \max_{U\in V_3}|\{T\in C_2^{(t)}:U\subset T\}|
 \le
 2\left(\frac{n(t+1)}{m-t}+1\right).}
\tag{3.6}
\]

In particular the maximum down-degree is (O(t)).

#### Proof

For (h\le t), put

\[
 D_h=\left\lceil\frac{n(L_h-M_h)}{M_h}\right\rceil.
\tag{3.7}
\]

By (3.3) and \(h\le t=o(m)\), one has \(D_h\le n\) for all sufficiently
large \(m\), so the following choice of \(D_h\) color classes is legal.
Among the (n) sum-color classes inside
(\mathcal K_h^{(2)}), the union of the (D_h) largest has size at least

\[
 \frac{D_h}{n}M_h\ge L_h-M_h.
\]

Choose exactly (L_h-M_h) targets from that union and call the chosen
set (C_h).  Put (C_2^{(t)}=\bigcup_{h\le t}C_h).  Equation (3.5) is
immediate.

Fix (U\in V_3).  The colors of its supersets (U\cup\{x\}) are

\[
 \sigma(U)+x\pmod n,
\]

and are pairwise distinct.  Also these supersets occupy at most two
categories.  Indeed, if (a=\kappa(U)), then adding a point outside
(P_a) leaves category (a), while adding a point of (P_a) moves to
the next pair missed by (U).  Such a next pair exists because an
((m-3))-set cannot meet all the remaining (m-1) pairs.

It follows that (U) has at most (D_a+D_b) selected supersets, where
(a,b) are those two possible categories and terms exceeding (t) are
omitted.  By (3.3),

\[
 D_h\le \frac{n(h+1)}{m-h}+1,
\]

which proves (3.6).  \(\square\)

The category capacities are exact:

\[
 |\mathcal K_h^{(2)}|
 +|C_2^{(t)}\cap\mathcal K_h^{(2)}|
 =L_h.
\tag{3.8}
\]

Hence every prefix inequality (2.2) is an equality on the retained
categories.  This is stronger than merely matching the global cardinality.
It does **not** yet prove the capacitated Hall inequalities inside one
category, nor does it realize the capacities by a wreath factor.

There is, however, no uncolored Hall obstruction inside one retained
category.

### Proposition 3.3 (exact one-or-two category factor)

If (h\le(m-1)/2), the inclusion graph between
(\mathcal K_h^{(1)}) and (\mathcal K_h^{(2)}) has a spanning integral
subgraph in which every left vertex has degree one and every right vertex
has degree one or two.  Exactly (L_h-M_h) right vertices have degree two.

#### Proof

Write (L=\mathcal K_h^{(1)}), (R=\mathcal K_h^{(2)}), and
(c=|L|-|R|).  Replace every (r\in R) by two clones (r_0,r_1), joining
each original left neighbor to both clones.  Add a dummy set (D) of size

\[
 |D|=2|R|-|L|=|R|-c
\]

and join every dummy vertex to every second clone (r_1).  This number is
nonnegative because (3.2) and (h\le(m-1)/2) give (L_h\le2M_h).  The two sides of the augmented
graph both have size (2|R|).

We verify Hall.  Let a left subset be (A\cup D'), with (A\subseteq L).
If (D'=\varnothing), incidence counting and Lemma 3.1 give

\[
 |N_G(A)|\ge\frac{m-h}{m+1}|A|,
\]

so its two clone neighborhoods have size at least (|A|), because
(2(m-h)\ge m+1).

If (D'\ne\varnothing), its neighborhood contains every second clone and
the first clones of (N_G(A)), hence has size

\[
 |R|+|N_G(A)|.
\]

Put (B=R\setminus N_G(A)).  All (m+1)|B| incidences from (B) land in
(L\setminus A), while every left vertex has at most (m-1) incident
same-category facets.  Therefore

\[
 (m+1)|B|\le(m-1)|L\setminus A|,
\]

and in particular (|B|\le|L\setminus A|).  It follows that

\[
 |N_G(A)|=|R|-|B|
 \ge |A|-(|L|-|R|)=|A|-c.
\]

Since (|D'|\le|D|=|R|-c),

\[
 |R|+|N_G(A)|\ge|A|+|D'|.
\]

Hall gives a perfect matching of the augmented graph.  Every first clone
must be matched to an original left vertex, while dummy vertices use only
second clones.  Projecting the matching back to (G) gives every right
vertex one or two original preimages and every left vertex one image.
Exactly (|L|-|R|=L_h-M_h) second clones are used by original vertices.
\(\square\)

Proposition 3.3 and Theorem 3.2 are deliberately separate.  The former
gives an exact integral category flow with an uncontrolled high set; the
latter gives a logarithmic-codegree capacity set without proving that the
same set supports the flow.  Their simultaneous realization, and then its
realization by cyclic rows, remain genuine requirements.

## 4. The tail and every category-dropping physical transition are cheap

The category estimate in the proof of Theorem 5.1 of the pair-omission
report gives, with

\[
 A_m={2m-1\choose m-1},
\]

an absolute (C) such that

\[
 L_h\le C\sqrt m\,A_m(3/4)^{h-1}.
\tag{4.1}
\]

Choose

\[
 t=\left\lceil\log_{4/3}(H\sqrt m\log m)\right\rceil.
\tag{4.2}
\]

Then (t=O(\log m)) for (H\le m), and

\[
 \sum_{h>t}L_h=O\left(\frac W{H\log m}\right)=o(W/H).
\tag{4.3}
\]

Lemma 3.1 also gives (M_h<L_h), so the rank-two tail has the same
bound.  Thus Theorem 3.2 supplies an exact retained high set with
down-degree (O(\log m)) after only (o(W/H)) tail release.

There is a second, physical source of downward category transport.  In a
row of (F_h), the transition

\[
 S_i\longmapsto T_i=S_i\setminus\{x_{i+m-2}\}
\tag{4.4}
\]

can have \(\kappa(T_i)<h\) only if the departing coordinate is one of the
two points of an earlier pair (P_j), (j<h), and is the unique point of
(S_i) in that pair.  Each coordinate is the departing coordinate at
exactly one cyclic start.  Consequently:

### Lemma 4.1 (cheap category-drop release)

Every row of (F_h) has at most (2(h-1)) selected starts whose canonical
rank-two flag has smaller category.  Through all phases (h\le t), the
number of such starts is at most

\[
 O\left(\frac{Wt^2}{m}\right).
\tag{4.5}
\]

If

\[
 H=o(m/\log ^2m),
\tag{4.6}
\]

then (4.5) is (o(W/H)).

#### Proof

The first assertion follows from (4.4): for each of the (h-1) earlier
pairs, only its two coordinates can cause the drop, and each departs once
per cyclic row.  Every (F_h) has

\[
 \frac1{2m-1}{2m-1\choose m-1}=O(W/m)
\]

rows.  Summing (2(h-1)) over (h\le t) proves (4.5).  Equations
(t=O(\log m)) and (4.6) prove the final claim.  \(\square\)

Deleting these starts creates at most one additional path component per
deletion.  Hence the same estimate bounds the extra initialization cost
by (H\,o(W/H)=o(W)).

Thus monotone category transport is not the surviving obstruction: all
its exceptional physical starts can be released within the established
first-band budget.

The exact totals (3.8) refer to the instance before this release.  After
the category-dropping starts are deleted, the corresponding owner demands
and high-set capacities must be thinned by the same released amount.
No literal exact-capacity claim for the post-deletion instance is being
made without that adjustment.

## 5. Exact canonical-\(q=2\) factor identity

For (T\in V_2) and (h=\kappa(T)), define

\[
 \lambda_h(T)=
 \#\{\hbox{cyclic adjacency edges of }F_h
       \hbox{ whose endpoint intersection is }T\}.
\tag{5.1}
\]

### Theorem 5.1 (canonical rank-two physical-load identity)

For the canonical outgoing column of the first-avoided-pair extraction,

\[
 \boxed{
 \mu_2(T)=\lambda_h(T)+\varepsilon_h(T),
 \qquad 0\le\varepsilon_h(T)\le2.}
\tag{5.2}
\]

The term \(\varepsilon_h(T)\) consists exactly of possible occurrences
owned by one of the two supersets (T\cup\{x\}), (x\in P_h), in later
phases.

#### Proof

The (m+1) supersets

\[
 T\cup\{x\},\qquad x\in Q_h\setminus T,
\]

all have category (h): they still avoid (P_h) and already contain
(T), which meets every earlier pair.  They are precisely the vertices
of the local Johnson clique over (T).  A selected start in phase (h)
has rank-two flag (T) exactly when its outgoing adjacency edge in
(F_h) has intersection (T).  Hence the phase-(h) contribution is
exactly \(\lambda_h(T)\).

Any later-category owner (S\) with rank-two flag (T) is a one-point
extension of (T).  It can cease to avoid (P_h) only by adding one of
the two points of (P_h).  There are therefore at most two such owners,
which gives (5.2).  \(\square\)

An exact balanced rank-two core would have

\[
 \mu_2(T)\in\{1,2\}
\tag{5.3}
\]

away from the released tail.  Therefore (5.2) gives the necessary local
factor condition

\[
 \boxed{\lambda_h(T)\le2\quad\hbox{for every retained }T.}
\tag{5.4}
\]

If \(\lambda_h(T)=0\), at least one of the two later-category spill owners
must point to (T).  Thus even the rank-two high set is a constrained
function of all the (F_h); it is not a free capacity vector.

## 6. The same canonical start order fixes the \(q=3\) transport

For (U\in V_3) and (h=\kappa(U)), define

\[
 \theta_h(U)=
 \#\{\hbox{length-}(m-3)\hbox{ cyclic interval occurrences of }U
       \hbox{ in }F_h\}.
\tag{6.1}
\]

### Theorem 6.1 (canonical rank-three physical-load identity)

For the same canonical extraction,

\[
 \boxed{
 \mu_3(U)=\theta_h(U)+\eta_h(U),
 \qquad 0\le\eta_h(U)\le2m+5.}
\tag{6.2}
\]

Moreover \(\lambda_h\) and \(\theta_h\) are not independent marginals.
If the occurrences of the length-((m-2)) intervals of (F_h) are kept
as distinct vertices, their actual cyclic successor relation is a
directed union of cycles with vertex-label multiplicities \(\lambda_h(T)\),
and the edge from (T_i) to (T_{i-1}) has label

\[
 T_i\cap T_{i-1}=U_i.
\tag{6.3}
\]

The multiplicity of the edge label (U) is \(\theta_h(U)\).

#### Proof

Every occurrence of (U) as a length-((m-3)) interval in (F_h) is
owned by a length-((m-1)) interval (S\subseteq Q_h) containing (U).
Since (U) meets all earlier pairs and avoids (P_h), this (S) has
category (h).  Thus the phase-(h) contribution is exactly
\(\theta_h(U)\).

A later-category owner contributing (U) is an ((m-1))-set obtained by
adding two points to (U) and meeting (P_h).  There are

\[
 2(m+2)+1=2m+5
\]

such supersets: choose exactly one of the two points of (P_h) and one of
the (m+2) points outside (U\cup P_h), or choose both points of (P_h).
This proves (6.2).  Finally (6.3) is the literal interval identity (1.3),
start by start, and proves the common-order assertion.  \(\square\)

Thus, within the canonical column, a Hall flow which first chooses the
loads \(\lambda_h\) and then chooses arbitrary rank-three descendants does
not preserve physical ownership: the descendant is the edge label in the
same cyclic occurrence graph.  A full corridor may choose another
left/right path, but those choices must remain one row-coherent path
through both depths.

## 7. Cuts, collars, and radius placements cannot change canonical vectors

### Proposition 7.1 (bulk rigidity under recutting)

Fix the local factors and the selected middle-owner order.

1. Moving block cuts while retaining the canonical cyclic collars changes
   none of the interval targets in (1.2).
2. If arbitrary legal endpoint collars are allowed on (J) path
   components, then at signed depth (q) only the first or last (q)
   owner positions of each component can depend on those collars.  Hence
   at most (2qJ) depth-(q) occurrences can change.
3. Moving a radius start changes a depth-(q) occurrence only by
   deactivating or activating its owner at that depth.  Thus changing
   (R) owners changes at most (R) occurrences there.
4. Choosing a different left/right monotone path in the full Pascal
   corridor can change bulk descendants.  Such rerouting is not a recut,
   radius move, or endpoint recollar, and is not covered by assertions
   1--3.

#### Proof

The first assertion is immediate because every canonical target is a
fixed interval of the fixed cyclic coordinate order.  For the second,
the lower and upper depth-(q) flags of an owner are respectively the
intersection and union of (q+1) consecutive middle owners.  Once these
owners lie inside the component, the target is forced; only positions
within (q) steps of an endpoint can see an external collar.  The final
assertion in item 3 is tautological from the definition of the active
radius.  Item 4 follows because a fixed middle interval has multiple
left/right interval descendants in its Pascal corridor; choosing another
monotone endpoint path changes those descendants even in the row interior.
\(\square\)

For the extraction of Section 5 of the pair-omission report,

\[
 J=O(W\log ^2m/m)=o(W/H)
\]

under (4.6).  Therefore all three operations together can modify only
(o(W/H)) rank-two or rank-three occurrences unless one releases more
than the permitted number of owners.

In particular, within the canonical-column sublane, the cyclic-sum high
set of the rank-three Hall theorem can be composed with this scaffold only
if the local factors already produce that set, up to the permitted
\(o(W/H)\) boundary changes.  For the full corridor, bulk left/right
rerouting remains an additional possibility and must satisfy one common
row-coherent path system.

## 8. Sufficient canonical theorem and adversarial audit

The results above leave the following sufficient canonical statement.

> **Two-shadow pair-factor theorem (unproved).**  Choose the local exact
> wreath factors (F_h), for (h\le t=O(\log m)), so that after deleting
> (o(W/H)) starts:
> 1. the vectors in (5.2) have values (1) or (2), and their load-two
>    set has bounded (or sufficiently one-sided logarithmic) down-degree;
> 2. the actual successor edge labels in (6.3) give balanced rank-three
>    loads; and
> 3. the same assertions continue through the required Gaussian window.

This theorem would preserve exact common ownership because all flags are
already literal intervals of the selected rows.  It is not implied by
the existence of exact middle wreath factors.  It is stronger than the
full-corridor requirement: the latter may choose noncanonical left/right
paths, whose simultaneous row-coherent selection remains open.

Adversarial checks:

1. The set in Theorem 3.2 satisfies the necessary category totals and a
   maximum down-degree bound.  Proposition 3.3 proves an uncolored
   one-or-two factor, but it does not prove that the prescribed
   bounded-degree high set supports that same factor.
2. The (O(\log m)) constant in (3.6) is not asserted to satisfy the
   sharper one-sided coefficient (D<(1-o(1))\log_2m) from the earlier
   generic rank-three cut lemma.  A further cut argument or a better
   common color choice would be needed for that implication.
3. Equation (5.2) uses edge multiplicity in the actual local factor, not
   merely the number of possible facets.  The later spill bound two is
   exact because a rank-two target needs only one added point.
4. Equation (6.2) has the larger bound (2m+5), and no false constant
   bound is inferred at rank three.
5. Lemma 4.1 bounds category drops by departing coordinates, so it remains
   valid even when the predecessor start is not selected.  The sharper
   one-transition-per-pair statement would be false at component
   boundaries and is not used.
6. Replacing the local factors is genuine new combinatorial work, not an
   endpoint recollar or block recut.  In the canonical sublane this is
   where the proof stops; in the full corridor, row-coherent bulk
   left/right routing is the additional unresolved alternative.
