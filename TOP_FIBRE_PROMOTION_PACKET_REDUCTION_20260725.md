# Top-fibre promotion packets at the critical height

Date: 2026-07-25

## 0. Scope and verdict

This note gives a new exact reduction for coefficient one.  It does not
prove the final packet-selection theorem.

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.
 \tag{0.1}
\]

Choose the least integer $H$ for which

\[
 \lambda_H\ge m+H,
 \qquad M:=m+H.
 \tag{0.2}
\]

Then $H=(1+o(1))\sqrt{m\log m}$.  A rank-$M$ top $U$ supports an
explicit promotion-only MTF cycle of length $M$: choose one cyclic order
of $U$ and take all of its length-$m$ windows.  At every depth $q\le H$,
the physical flags of this cycle are exactly all cyclic intervals of the
same order of lengths $m-q$ and $m+q$.

There are $N_H$ tops, and

\[
 MN_H=W-o(W),\qquad HN_H=o(W).
 \tag{0.3}
\]

Thus one promotion packet per top has total transition length $W-o(W)$
and total independent-reset cost $o(W)$.  Coefficient one is reduced to a
static simultaneous near-covering problem: choose one cyclic order on
every rank-$M$ top so that the aggregate number of missed interval targets
over the central band is $o(W)$.

The packet design has exact, unusually favorable same-rank codegrees.  On
the middle layer its maximum relative codegree is $2/m^2$.  More generally,
on every nontrivial rank inside a top it is

\[
 {a_d\over\binom rd\binom{2m-r}{d}},
 \tag{0.4}
\]

where $a_d$ is the number of relative cyclic shifts producing distance
$d$.  In every rank whose shorter interval side has size at least two,
the maximum is $2/[r(2m-r)]=O(m^{-2})$; the single coatom-of-top rank has
an explicit $O(m^{-1})$ plateau codegree but only $o(W)$ targets.  The uniform
fractional choice is also exact and has only $o(W)$ total unavoidable slot
deficit across the shallow ranks.  What remains unproved is an integral
simultaneous near-parallel-class theorem across all ranks.

## 1. The critical height

### Lemma 1.1 (height tuning)

The integer $H$ defined by (0.2) satisfies

\[
 H=(1+o(1))\sqrt{m\log m},
 \tag{1.1}
\]

and

\[
 1\le {\lambda_H\over M}
 <{M-1\over m-H+1}
 =1+O(H/m).
 \tag{1.2}
\]

Consequently, with

\[
 \rho={M\over\lambda_H}={MN_H\over W},
 \tag{1.3}
\]

one has

\[
 0\le1-\rho=O(H/m)=o(1).
 \tag{1.4}
\]

#### Proof

Uniformly for $q=o(m^{2/3})$,

\[
 \log\lambda_q={q(q+1)\over m}+O(q^3/m^2+q/m).
 \tag{1.5}
\]

The crossing $\lambda_q\asymp m$ therefore occurs at
$q=(1+o(1))\sqrt{m\log m}$, which is itself $o(m^{2/3})$.  This proves
(1.1).

Minimality gives $\lambda_{H-1}<m+H-1=M-1$.  Since

\[
 {\lambda_H\over\lambda_{H-1}}
 ={m+H\over m-H+1}={M\over m-H+1},
 \tag{1.6}
\]

division by $M$ proves (1.2), and (1.3)--(1.4) follow. \(\square\)

### Lemma 1.2 (aggregate slot deficit is negligible)

Put $T=MN_H=\rho W$.  Then

\[
 \sum_{q=0}^{H}(N_q-T)_+=o(W).
 \tag{1.7}
\]

The same assertion holds for the symmetric upper ranks.

#### Proof

By (1.4), write $T=(1-\delta)W$ with
$\delta=O(H/m)$.  Also

\[
 {N_q\over W}\le \exp(-q^2/(2m)).
 \tag{1.8}
\]

The summand in (1.7) vanishes once $q^2/(2m)\ge2\delta$, so only
$q=O(\sqrt{m\delta})=O(\sqrt H)$ contribute.  Each contribution is at
most $\delta W$.  Hence

\[
 \sum_{q=0}^{H}(N_q-T)_+
 =O(W\delta\sqrt H)
 =O\left(W{H^{3/2}\over m}\right)=o(W),
 \tag{1.9}
\]

using (1.1). \(\square\)

### 1.1 The covering-side crossing is cleaner

For a covering theorem there is no need to keep the middle load below one.
Let $H_-$ be the greatest integer satisfying

\[
 \lambda_{H_-}\le m+H_-,
 \qquad M_-=m+H_-.
 \tag{1.10}
\]

Then again $H_-=(1+o(1))\sqrt{m\log m}$, while

\[
 m-H_-<\lambda_{H_-}\le M_-.
 \tag{1.11}
\]

Indeed maximality gives
$\lambda_{H_-+1}>M_-+1$, and

\[
 \lambda_{H_-+1}
 =\lambda_{H_-}{M_-+1\over m-H_-}.
\]

Thus, putting

\[
 T_-=M_-N_{H_-},
 \]

one has

\[
 \boxed{
 1\le {T_-\over W}={M_-\over\lambda_{H_-}}
 <{M_-\over m-H_-}=1+O(H_-/m)=1+o(1).}
 \tag{1.12}
\]

Hence one packet per top has $W+o(W)$, rather than $W-o(W)$, middle
slots.  Repetitions are harmless at this scale, and the uniform fractional
load of every rank-$(m\pm q)$ target is

\[
 {T_-\over N_q}\ge {W\over N_q}=\lambda_q\ge1.
 \tag{1.13}
\]

This covering-side height removes the owner-packing requirement entirely.
All packet, degree, codegree, reset, and tail statements below remain valid
with $(H,M,T)$ replaced by $(H_-,M_-,T_-)$.  The final coefficient-one
transfer needs only $T=W+o(W)$, so either side of the crossing may be used;
the covering side is the sharper formulation of the unresolved vertical
selection theorem.

## 2. Exact promotion packet inside one top

Fix $U\in\binom{[2m]}M$.  A full radius-$H$ state with top $U$ can be
written as

\[
 (A,L,B),
 \tag{2.1}
\]

where

\[
 A=(a_1,\ldots,a_H),\qquad |L|=m-H,qquad
 B=(b_1,\ldots,b_H)
 \tag{2.2}
\]

partition $U$.  Here $A$ is the deletion queue, $B$ is the ordered upper
cache, and the middle owner is $A\cup L$.

A promotion step chooses $x\in L$ and $b\in B$ and performs

\[
 \begin{aligned}
 A'&=(a_2,\ldots,a_H,x),\\
 B'&=(a_1,B\setminus b),\\
 L'&=L-x+b,
 \end{aligned}
 \tag{2.3}
\]

with the inherited order on $B\setminus b$.  It is a bridge-one MTF step
and preserves the top $U$.

### Theorem 2.1 (cyclic orders are promotion cycles)

Choose orderings $L=(l_1,ldots,l_{m-H})$, $A$, and $B$, and form the
cyclic order

\[
 \pi=(a_1,\ldots,a_H,l_1,\ldots,l_{m-H},b_H,\ldots,b_1)
 \tag{2.4}
\]

of $U$.  Repeatedly apply (2.3) with

\[
 x=l_1,\qquad b=b_H,
 \tag{2.5}
\]

where the displayed lists are updated after every step.  Then (2.4)
rotates left by one position at every step.  The resulting $M$ states form
one promotion-only bridge cycle, and their middle owners are exactly the
$M$ cyclic intervals of $\pi$ of length $m$.

At each depth $q\le H$, their lower flags are exactly all cyclic intervals
of $\pi$ of length $m-q$, and their upper flags are exactly all cyclic
intervals of length $m+q$.  For $q<H$ these are $M$ distinct targets; for
$q=H$ every upper flag is the common top $U$.

#### Proof

After (2.3)--(2.5), the concatenated list in (2.4) becomes

\[
 (a_2,\ldots,a_H,l_1,l_2,\ldots,l_{m-H},
 b_H,b_{H-1},\ldots,b_1,a_1),
 \]

which is its left rotation.  The middle owner is the first $m$ entries,
so the owners are precisely the length-$m$ cyclic windows.

The next $q$ removals delete the first $q$ entries of the current window,
giving its terminal length-$(m-q)$ interval.  The upper cache begins with
the entries immediately preceding the current window, in reverse cache
notation, so adjoining its first $q$ entries gives the containing cyclic
interval of length $m+q$.  Rotation supplies every start position.
\(\square\)

Call the cycle in Theorem 2.1 a **top-fibre promotion packet**.

## 3. The packet incidence design

For every top $U$, retain all $(M-1)!$ oriented cyclic orders modulo
rotation as formal packet choices.  For $1\le r<M$, let
$\mathcal V_r=\binom{[2m]}r$.  A packet is incident with the $M$ cyclic
length-$r$ intervals in its order.

### Proposition 3.1 (exact degrees)

A fixed rank-$r$ target belongs to exactly

\[
 \boxed{
D_r=\binom{2m-r}{M-r}\,r!\,(M-r)!}
 \tag{3.1}
\]

Equivalently,

\[
 \boxed{D_r={r!(2m-r)!\over(2m-M)!}.}
 \tag{3.1a}
\]

formal packets.  A fixed top has $(M-1)!$ packet choices.  In particular a
middle target has degree

\[
 \boxed{D_m=\binom mH m!H!.}
 \tag{3.2}
\]

#### Proof

Choose the top containing the target, and then regard the target as one
cyclic block.  Contracting it leaves $M-r+1$ cyclic objects; there are
$(M-r)!$ cyclic arrangements and $r!$ internal orders. \(\square\)

For equal-sized targets $S,T$, write
$d=|S-T|=|T-S|$.  Put

\[
 s_r=\min(r,M-r),
 \tag{3.3}
\]

and let

\[
 a_{r,M}(d)=
 \begin{cases}
 2,&1\le d<s_r,\\
 M-2s_r+1,&d=s_r,\\
 0,&d>s_r.
 \end{cases}
 \tag{3.4}
\]

### Proposition 3.2 (exact same-rank codegrees)

For distinct $S,T\in\mathcal V_r$,

\[
 \boxed{
 {\deg(S,T)\over D_r}
 ={a_{r,M}(d)\over
   \binom rd\binom{2m-r}{d}}.}
 \tag{3.5}
\]

In particular, whenever $s_r\ge2$,

\[
 \max_{S\ne T}{\deg(S,T)\over D_r}
 ={2\over r(2m-r)}=O(m^{-2}),
 \tag{3.6}
\]

while for the upper coatom rank $r=M-1$ it is exactly

\[
 {1\over 2m-M+1}={1\over m-H+1}=O(m^{-1}).
 \tag{3.6a}
\]

That exceptional rank has
$\binom{2m}{M-1}=O(W/m)$ targets and may be repaired literally without
leading cost.  On the middle layer the exact
formula is

\[
 {\deg(X,Y)\over D_m}
 =
 \begin{cases}
 2/\binom md^2,&1\le d<H,\\
 (m-H+1)/\binom mH^2,&d=H,\\
 0,&d>H.
 \end{cases}
 \tag{3.7}
\]

#### Proof

Two cyclic length-$r$ intervals at relative shift $t$ have distance $d$
exactly for the number of shifts recorded in (3.4): use the shorter of an
interval and its complement.  Conditional on $S$ being an interval in a
fixed containing top, symmetry among the
$\binom rd\binom{M-r}d$ targets at distance $d$ gives conditional
probability

\[
 {a_{r,M}(d)\over\binom rd\binom{M-r}d}.
 \tag{3.8}
\]

The ratio of the numbers of tops containing $S\cup T$ and $S$ is

\[
 {\binom{2m-r-d}{M-r-d}\over\binom{2m-r}{M-r}}
 ={\binom{M-r}d\over\binom{2m-r}d}.
 \tag{3.9}
\]

Multiplying (3.8) and (3.9) proves (3.5).  The minimum denominator occurs
at $d=1$, proving (3.6), and $r=m$ gives (3.7). \(\square\)

The vertical codegrees are larger, and this is the exact dependence which
the final selection theorem must exploit rather than ignore.

### Proposition 3.3 (exact nested cross-rank codegree)

Let $S\subset T$ with $|S|=r<|T|=s<M$.  Then

\[
 \boxed{
 \deg(S,T)=D_s\,{s-r+1\over\binom sr}.}
 \tag{3.9a}
\]

In particular, for an adjacent nested pair,

\[
 {\deg(S,T)\over D_s}={2\over s}=\Theta(m^{-1}).
 \tag{3.9b}
\]

#### Proof

Condition on a packet containing $T$.  Inside the cyclic order, the proper
interval $T$ has a uniformly ordered linear interior.  An $r$-subset of
$T$ is also a cyclic interval exactly when it occupies one of the
$s-r+1$ consecutive length-$r$ subblocks of that interior.  Symmetry among
the $\binom sr$ subsets proves the conditional probability in (3.9a).
Multiplication by $D_s$ proves the formula. \(\square\)

Thus same-rank clustering is $O(m^{-2})$, but adjacent vertical clustering
is genuinely $\Theta(m^{-1})$.  Treating the $2H+1$ interval rows as
unrelated vertices loses precisely this nested-column structure.

### Proposition 3.4 (exact uniform fractional selection)

Give every packet over every top weight $1/(M-1)!$.  Then every top has
total choice weight one, while every fixed rank-$r$ target has load

\[
 \boxed{{MN_H\over\binom{2m}r}={T\over\binom{2m}r}.}
 \tag{3.10}
\]

In particular every middle target has load $\rho\le1$, and the total
middle slack is

\[
 W(1-\rho)=W-MN_H=o(W).
 \tag{3.11}
\]

#### Proof

Every top contributes one unit of packet weight, and each packet has $M$
rank-$r$ intervals.  Coordinate transitivity makes the load constant over
the rank, so it is the total incidence $MN_H$ divided by the rank size.
Equation (3.11) is Lemma 1.1. \(\square\)

Thus the one-packet-per-top linear relaxation is exact, has middle capacity
at most one, and has only the aggregate unavoidable deficits in Lemma 1.2.

### Proposition 3.5 (every row rounds integrally on its own)

Fix $1\le r<M$ and put

\[
 \theta_r={T\over\binom{2m}r}.
 \tag{3.12}
\]

There is an integral assignment of exactly $M$ distinct rank-$r$ targets
to every top $U$, all contained in $U$, such that every rank-$r$ target is
assigned either $\lfloor\theta_r\rfloor$ or
$\lceil\theta_r\rceil$ times.  In particular, at $r=m$ every top receives
$M$ distinct middle owners and no middle owner is assigned twice; exactly
$W-T=o(W)$ middle owners remain unassigned.

#### Proof

Use the bipartite inclusion graph between the rank-$M$ tops and the
rank-$r$ targets.  Give every incidence the fractional value

\[
 {M\over\binom Mr}.
 \tag{3.13}
\]

Every top then has total flow $M$.  A fixed rank-$r$ target has
$\binom{2m-r}{M-r}$ containing tops, and the binomial identity gives its
total flow

\[
 \binom{2m-r}{M-r}{M\over\binom Mr}
 ={MN_H\over\binom{2m}r}=\theta_r.
 \tag{3.14}
\]

Put the lower and upper capacity
$[\lfloor\theta_r\rfloor,\lceil\theta_r\rceil]$ at each target, require
flow $M$ out of every top, and use unit capacities on individual
incidences.  The displayed fractional flow is feasible.  Bipartite
network-flow integrality gives an integral feasible flow, proving the
claim.  For $r=m$, one has $0<\theta_m=\rho\le1$, so every used owner has
load one. \(\square\)

Thus top ownership, rowwise divisibility, and rowwise floor/ceiling
balancing all have exact integral solutions.  They can even be obtained
simultaneously as separate tables.  What is missing is one cyclic order on
each top whose interval rows realize compatible choices from all those
tables.

At the covering-side height (1.10), the same proof has
$\theta_r=T_-/\binom{2m}r\ge1$ throughout the central band.  It therefore
assigns every target at least once in every rank, with only
$T_--W=o(W)$ repeated middle slots.  Thus even exact rowwise covering is
integrally feasible; only the requirement that all rows on a top arise
from one common cyclic order remains.

## 3.1 An exact local vertical trade

Let $\pi$ be a cyclic order on $U$, and let $\pi'$ be obtained by swapping
two adjacent symbols $u,v$.

### Proposition 3.6 (adjacent-swap packet trade)

For every $2\le r\le M-2$, the rank-$r$ interval families of $\pi$ and
$\pi'$ differ in at most two deleted and two inserted targets.  At the
occurrence level the only changed windows are

\[
 C_r\cup\{u\},\quad \{v\}\cup D_r
 \tag{3.15}
\]

and they become

\[
 C_r\cup\{v\},\quad \{u\}\cup D_r,
 \tag{3.16}
\]

where $C_r$ is the $r-1$ symbols immediately preceding $u$ and $D_r$ is
the $r-1$ symbols immediately following $v$.  The rank-one and
rank-$(M-1)$ interval families are unchanged as unlabelled families, and
the top is unchanged.

Consequently one adjacent swap changes at most four incidence units in
each controlled rank and at most $O(H)$ units over the entire central
band.  Adjacent swaps connect all cyclic orders on a fixed top.

#### Proof

A cyclic interval which contains both $u,v$ or neither has the same
underlying set after the swap.  The only intervals containing exactly one
of the adjacent symbols are the window ending at $u$ and the window
starting at $v$, giving (3.15)--(3.16).  For $r=1$ these two sets are merely
interchanged; for $r=M-1$ their complements are interchanged.  Adjacent
transpositions generate every permutation, and rotations do not change a
cyclic order. \(\square\)

This is a support-$O(H)$ trade inside the genuine promotion dynamics: no
owner reset or nonliteral state is introduced.  It gives a concrete route
for an absorber, but not yet a proof.  To preserve an owner matching, the
two newly inserted middle windows in (3.16) must be unused or must be
released by coordinated swaps in other tops.  Such alternating swap chains
are the exact local object needed for a vertical correction of the
independent integral tables in Proposition 3.5.

There is no hidden same-top freedom which changes the other rows while
fixing the middle packet.

### Proposition 3.7 (middle-packet rigidity)

Assume $2\le H<M/2$.  For a fixed top $U$, the unlabelled family of the
$M$ length-$m$ windows of a cyclic order determines that cyclic order up to
rotation and reversal.  Consequently it determines every lower and upper
interval row of the promotion packet.

#### Proof

Complement the length-$m$ windows inside $U$.  This gives the family
$\mathcal I_H$ of all length-$H$ cyclic intervals.  Form a graph on
$\mathcal I_H$ by joining two intervals when their intersection has size
$H-1$.  Since $2H<M$, two distinct cyclic $H$-intervals have intersection
$H-1$ exactly when their starts differ by one.  Hence this graph is the
cycle of consecutive windows.

Traversing that cycle, the singleton differences between consecutive
windows recover the successive ground symbols.  Choosing the direction
and the initial window accounts exactly for reversal and rotation.  Every
cyclic interval family is invariant under those two choices, proving the
last assertion. \(\square\)

Thus an owner-only packet matching cannot first be frozen and then repaired
vertically within each top: its shadow rows are already fixed.  A genuine
vertical absorber must be an alternating trade involving several tops and
must change their middle packets while preserving, or almost preserving,
the global middle coverage.

For completeness, changing the top itself has an exact but much larger
support.

### Proposition 3.8 (neighboring-top substitution)

Let $U'=U-u+v$, and obtain a cyclic order $\pi'$ of $U'$ from $\pi$ by
replacing $u$ by $v$ in the same position.  At rank $r<M$, exactly the $r$
cyclic windows of $\pi$ containing that position change; each is obtained
in $\pi'$ by replacing $u$ with $v$.  The other $M-r$ windows are
unchanged.

#### Proof

A cyclic length-$r$ window is unchanged precisely when it avoids the
replaced position.  Every position lies in exactly $r$ of the $M$ cyclic
windows. \(\square\)

At the middle rank two neighboring-top packets therefore share exactly
$H=M-m$ owners and differ on $m$ owners.  Neighboring-top substitution is
not a local owner correction at the critical height; adjacent same-top
swaps are local, but must be linked through a multi-top alternating chain.

## 3.2 Rank-isolating four-order rectangles

Take two disjoint adjacent transpositions $\sigma,\tau$ in a cyclic order
$\pi$, and assume that their two boundary cuts are at cyclic distance
$r$.  They commute.  Put

\[
 \pi_{ij}=\sigma^i\tau^j\pi,
 \qquad i,j\in\{0,1\},
 \tag{3.17}
\]

and let $v_s(\pi)$ be the incidence vector of all cyclic length-$s$
intervals of $\pi$.

### Theorem 3.9 (exact rank isolation)

The mixed rectangle

\[
 \mathcal R_s=
 v_s(\pi_{00})+v_s(\pi_{11})
 -v_s(\pi_{10})-v_s(\pi_{01})
 \tag{3.18}
\]

vanishes for every $s\notin\{r,M-r\}$.  At length $r$ it is one elementary
square

\[
 \boxed{
 e_{K\cup\{a_0,b_0\}}+e_{K\cup\{a_1,b_1\}}
 -e_{K\cup\{a_1,b_0\}}-e_{K\cup\{a_0,b_1\}},}
 \tag{3.19}
\]

up to reversing all signs.  Here $K$ is the set of the $r-2$ symbols
strictly between the two swap boundaries and
$\{a_0,a_1\},\{b_0,b_1\}$ are the swapped pairs.  At length $M-r$ one gets
the complementary square.  If $r=M-r$, both arcs contribute in that one
rank.

#### Proof

A cyclic window notices an adjacent swap exactly when one of its two
boundary cuts passes through the swapped pair.  In the mixed second
difference (3.18), every window which notices at most one of the two swaps
cancels.  A window notices both exactly when its two boundary cuts are the
two distinguished cuts.  The two arcs between those cuts have lengths
$r$ and $M-r$, proving the vanishing assertion.

On the length-$r$ arc, the interior $K$ is fixed and each boundary
contributes one of its two swapped symbols.  The four choices, with the
rectangle signs, give (3.19).  The other arc gives its complement.
\(\square\)

For the critical promotion packet, $3H<m$ for all sufficiently large $m$.
Hence, if

\[
 r=m-q\quad\hbox{or}\quad r=m+q,
 \qquad1\le q\le H,
 \tag{3.20}
\]

the complementary exceptional length $M-r=H+q$ or $H-q$ lies strictly
below the controlled central band.  Thus (3.18) changes exactly one
controlled rank and leaves the middle row fixed.

The signed identity has a positive segment implementation with negligible
overhead.  Fix a hard band

\[
 \mathcal B_Q=\{m-Q,m-Q+1,\ldots,m+Q\},
 \qquad Q\le H.
 \tag{3.21}
\]

For the swap $\sigma$ between cyclic positions $p,p+1$, let

\[
 \mathcal K_Q(\sigma)=
 \bigcup_{s\in\mathcal B_Q}
 \{p+1,\ p-s+1\}\pmod M.
 \tag{3.22}
\]

These are exactly the phase starts whose hard-band interval notices
$\sigma$, and

\[
 |\mathcal K_Q(\sigma)|\le2Q+2.
 \tag{3.23}
\]

Choose phase-start sets $A,B\subseteq\mathbb Z_M$ with

\[
 A\cup B=\mathbb Z_M,
 \qquad A\cap B=\mathcal K_Q(\sigma).
 \tag{3.24}
\]

They may be chosen so that each is a union of at most two cyclic intervals,
because (3.22) has at most two cyclic components.

Define the two positive deployments

\[
 \mathcal D^+
 =\pi_{00}|_A\ \sqcup\ \pi_{11}|_B,
 \qquad
 \mathcal D^-
 =\pi_{10}|_A\ \sqcup\ \pi_{01}|_B,
 \tag{3.25}
\]

where $\pi|_A$ means the promotion states whose phase starts lie in $A$,
cut into its cyclic-interval components.

### Theorem 3.10 (positive segment rectangle)

For every $s\in\mathcal B_Q$, the difference between the rank-$s$
incidence vectors of $\mathcal D^+$ and $\mathcal D^-$ is exactly
$\mathcal R_s$.  Each deployment uses

\[
 M+|\mathcal K_Q(\sigma)|=M+O(Q)
 \tag{3.26}
\]

owner endpoints and at most four promotion paths.  Across all $N_H$ tops,
the duplicated endpoints and independent path initializations cost

\[
 O(QN_H)+O(HN_H)=o(W).
 \tag{3.27}
\]

#### Proof

At a start outside $\mathcal K_Q(\sigma)$, no hard-band window notices
$\sigma$.  If that start lies only in $A$, its contribution cancels between
$\pi_{00}$ and $\pi_{10}$; if it lies only in $B$, it cancels between
$\pi_{11}$ and $\pi_{01}$.  At a start in the intersection, all four
orders occur with the signs in (3.18).  Summing over starts gives the full
rectangle, because its summand is already zero outside the set (3.22).

Equation (3.26) is (3.24).  The component choice following (3.24) gives at
most four paths total.  Finally $Q,H=o(m)$ and
$N_H=(1+o(1))W/m$, proving (3.27). \(\square\)

Thus the direct $0/2$ full-packet idea is unnecessary and, in fact,
wasteful: two diagonal full packets differ at only four middle phase
positions and cover only $M+O(1)$ distinct owners.  The segment deployment
duplicates only the $O(Q)$ starts required for exact cancellation and
retains $M-O(Q)$ distinct phase positions.

### Theorem 3.11 (the rank-$r$ rectangle lattice)

For $2\le r\le M-2$, let $A_r$ be the point-incidence map

\[
 A_r:\mathbb Z^{\binom Ur}\longrightarrow\mathbb Z^U,
 \qquad
 (A_rz)(x)=\sum_{S\ni x}z(S).
 \tag{3.28}
\]

The integer lattice generated by the rank-$r$ rectangles (3.19) is
exactly

\[
 \boxed{\ker_{\mathbb Z}A_r.}
 \tag{3.29}
\]

In particular there is no additional parity or congruence obstruction at
one rank.  Over the reals the two orientations of the positive segment
trade span the full zero-point-marginal subspace.

#### Proof

Every rectangle has zero incidence at every point, so its span is contained
in the displayed kernel.  For the converse, fix $v\in U$.  The total
coefficient of the $r$-sets containing $v$ is zero for every vector in the
kernel.

The Johnson graph on the $(r-1)$-subsets of $U-v$ is connected.  If two
adjacent such subsets are $K+a$ and $K+b$, choose
$c\notin K\cup\{a,b,v\}$; this is possible because $M\ge r+2$.  The
rectangle

\[
 e_{K\cup\{v,a\}}+e_{K\cup\{b,c\}}
 -e_{K\cup\{v,b\}}-e_{K\cup\{a,c\}}
 \tag{3.30}
\]

transfers one unit between the two $v$-containing coordinates while
changing only coordinates which avoid $v$ otherwise.  Along a spanning
tree, use these moves to concentrate all coefficients of $v$-containing
sets at one coordinate; their zero sum then eliminates that last
coefficient.  The remaining vector lies in the corresponding kernel on
$U-v$.  Induction on $M$, with the zero-kernel base $M=r+1$, proves
(3.29).  Every move (3.30) has the form (3.19) and is realized by arranging
its four distinguished symbols at the two swap boundaries. \(\square\)

The lattice theorem and rank isolation show that, at the signed level,
all non-middle central ranks can be balanced sequentially and independently
once their point marginals are fixed.  The remaining difficulty is
positive global deployment: a large collection of prescribed rectangle
coefficients must be packed into $W+o(W)$ promotion segments while keeping
middle coverage.  Theorem 3.10 supplies one exact positive absorber atom;
it does not by itself prove that all coefficients in a decomposition
(3.29) admit a simultaneously sparse positive realization.

There is, however, additional literal splicing freedom which is invisible
in the cyclic-order notation.

### Proposition 3.12 (hidden-interior splice)

At a fixed phase, two cyclic orders encode the same radius-$H$ useful state
whenever they have the same ordered deletion queue $A$, the same ordered
cache $B$, and the same *set* $L$ between them.  In particular an arbitrary
permutation of the $m-H$ symbols in the $L$ block costs no MTF entry and no
reset.

An adjacent swap is invisible at a phase exactly when its two symbols lie
in that unordered $L$ block.  Equivalently, none of the central interval
boundaries of lengths $m-H,ldots,m+H$ cuts that pair at that phase.

#### Proof

The useful state is the ordered partition

\[
 (L;\alpha_H,\ldots,\alpha_1,
       \beta_1,\ldots,\beta_H).
\]

It records $L$ as one block and therefore forgets its internal order.
The second assertion is immediate: a central prefix boundary separates an
adjacent pair precisely when that pair is not wholly inside one useful
block; all blocks other than $L$ are singletons. \(\square\)

Consequently the complementary long portions in the segment rectangle of
Theorem 3.10 may be joined at phase cuts outside the affected-start
neighborhoods of both swaps: the two encoded useful states agree there.
Only the duplicated $O(Q)$ boundary neighborhood needs a separate short
piece.  Thus one rank-isolating positive trade can be implemented with one
long promotion path and $O(1)$ short paths, not with two independently
reset full packets.

More generally, a top-fibre promotion path may reorder its current reserve
block arbitrarily between transitions and then choose any $x\in L$ as the
new queue tail.  This gives $m-H$ transparent continuation choices at every
owner.  Any successful positive realization of the rectangle lattice must
use this hidden-interior freedom to superpose many signed square moves;
deploying one pair of almost-identical full packets per square loses a
factor two in owner capacity.

## 4. Exact coefficient-one transfer

Choose one packet $P_U$ for every top $U$.  For each $q\le H$, let
$M_q^-$ and $M_q^+$ be the numbers of rank-$(m-q)$ and rank-$(m+q)$
targets, respectively, which are not cyclic intervals in any selected
packet.  Count the middle layer only once.

### Theorem 4.1 (top-promotion transfer)

If the packet choices can be made so that

\[
 \boxed{
 M_0+\sum_{q=1}^{H}(M_q^-+M_q^+)=o(W),}
 \tag{TP}
\]

then

\[
 \nu(2m)\le W+o(W).
 \tag{4.1}
\]

#### Proof

Cut and initialize every promotion cycle.  By Theorem 2.1 the resulting
literal word covers all selected cyclic intervals and has length

\[
 MN_H+2HN_H=T+2H{T\over M}=W+o(W),
 \tag{4.2}
\]

using Lemma 1.1 and $H/M=o(1)$.  Append all band holes literally; (TP)
makes this $o(W)$.

Finally append the two outer tails.  From (1.1),

\[
 \sum_{r<m-H}\binom{2m}r
 =O\left(W\sqrt m\,e^{-H^2/m}\right)=o(W).
 \tag{4.3}
\]

The upper tail is symmetric.  This proves (4.1). \(\square\)

The theorem needs no middle-owner partition and no SCD.  Repeated middle
owners merely consume packet slots and are charged automatically as holes
because $T=W-o(W)$.

## 5. The exact remaining selection theorem

The unproved assertion is now purely static.

> **Critical top-packet theorem.**  At the height (0.2), choose one cyclic
> order on every $M$-set $U\subset[2m]$ so that the aggregate number of
> missed cyclic-interval targets in (TP) is $o(W)$.

Propositions 3.1--3.3 prove all marginal, same-rank codegree, capacity, and
fractional statements for this theorem.  They do not prove its integral
simultaneous selection.

Independent choices are quantitatively insufficient.  For a fixed
rank-$(m-1)$ target $S$, the choices belonging to distinct tops are
independent, and its expected load is

\[
 {T\over N_1}=\rho\lambda_1=1-o(1).
 \tag{5.1}
\]

The probability attached to any one top is exponentially small, so its
miss probability tends to $e^{-1}$.  Hence independent packet choices
leave $(e^{-1}+o(1))N_1=\Theta(W)$ first-shadow holes.  The desired theorem
requires a correlated near-parallel class simultaneously in every rank.

The favorable formula (3.6) shows that the obstruction is not same-rank
pair clustering.  The remaining dependence is vertical: one cyclic order
chooses its interval families at all $2H+1$ ranks together.  Proving (TP),
or exhibiting a vertical Hall/absorber theorem which rounds (3.10) with
$o(W)$ aggregate holes, would complete coefficient one through Theorem
4.1.
