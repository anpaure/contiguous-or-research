# Closed companion restoration cannot route an interior owner to the boundary

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
 \qquad r=d+H-1.
\tag{0.1}
\]

Assume $H\ge3$ and $d\ge2H+3$, as holds in the calibrated
Gaussian regime for all sufficiently large $m$.

The one-root boundary swap changes a single middle owner, and a
three-top conveyor can change the literal order on a focal top while
preserving the aggregate middle load.  It is therefore natural to try
the following closed-catalyst protocol:

1. use middle-neutral conveyors or moving-hole exchanges to move a
   chosen duplicate occurrence to boundary phase $2$;
2. perform the one-root transfer $e_Y-e_X$; and
3. undo the routing and restore every companion frame exactly.

This protocol does **not** exist for an arbitrary chosen occurrence.
In fact the obstruction is independent of the named move library and
of the number of intermediate moves.

> **Closed-routing obstruction.**  Suppose two legal
> one-configuration-per-top tables agree at every top except one top
> $U$, and their total middle-load difference is $e_Y-e_X$.  If the
> configuration at $U$ is a length-$d$ tight $H$-window path, then
> the removed occurrence $X$ must lie in one of the phase bands
> 
> \[
>       \{1,\ldots,H+1\}\ \cup\
>       \{d-H,\ldots,d\}.
> \tag{0.2}
> \]
> 
> In particular, no occurrence at a phase
> 
> \[
>                    H+2\le i\le d-H-1
> \tag{0.3}
> \]
> 
> can be brought to phase $2$, switched, and returned with all
> companion frames restored.

Only $2H+2$ of the $d=(1-o(1))m$ phases escape this obstruction.
Thus closed companion restoration exposes at most an

\[
                         O(H/m)=o(1)
\tag{0.4}
\]

fraction of the occurrences of one tight path.  The existing boundary
swap is genuinely useful when the chosen occurrence is already at its
certified boundary phase, with $O(H)$ all-depth collateral.  What it
cannot do is manufacture that eligibility by a closed neutral route.

The proof is an exact chronology argument, not a lattice-span or
marginal argument.  A path deck with only one window changed determines
all four letters around that change from the two-sided history unless
the change is within distance $H+1$ of an endpoint.

## 1. Linear tight-window decks

Let

\[
                  w=(w_1,\ldots,w_r)
\tag{1.1}
\]

be an injective word and put

\[
 J_i(w)=\{w_i,w_{i+1},\ldots,w_{i+H-1}\},
 \qquad 1\le i\le d.
\tag{1.2}
\]

Write

\[
              \mathcal J(w)=\{J_1(w),\ldots,J_d(w)\}.
\tag{1.3}
\]

On a fixed top $U$, the corresponding middle-owner deck is

\[
              \mathcal B_U(w)=\{U\setminus J:J\in\mathcal J(w)\}.
\tag{1.4}
\]

All sets in either deck are distinct.  Moreover

\[
 |J_i(w)\cap J_j(w)|=\max\{0,H-|i-j|\}.
\tag{1.5}
\]

Consequently, joining two members of $\mathcal J(w)$ when their
intersection has size $H-1$ recovers the path

\[
                  J_1-J_2-\cdots-J_d
\tag{1.6}
\]

up to reversal.

## 2. One-window replacement is confined to the endpoint bands

### Theorem 2.1 (one-window chronology rigidity)

Let $w,v$ be injective words of length $r=d+H-1$.  Suppose

\[
                  |\mathcal J(w)\triangle\mathcal J(v)|=2.
\tag{2.1}
\]

Let $J_i(w)$ be the unique member of
$\mathcal J(w)\setminus\mathcal J(v)$.  Then

\[
                  i\le H+1\qquad\hbox{or}\qquad i\ge d-H.
\tag{2.2}
\]

#### Proof

The intrinsic intersection-$(H-1)$ graph on either deck is the path
$P_d$.  Removing the unique noncommon vertex from the first deck
leaves paths of orders $i-1$ and $d-i$.  Removing the unique
noncommon vertex from the second deck leaves the same intrinsic graph
on the same $d-1$ common sets.  Hence, after possibly reversing the
indexing of $v$, its missing vertex also has index $i$.

When $1<i<d$, the two components are oriented consistently as
follows.  Among pairs with one member in each component, the facing
pair $J_{i-1},J_{i+1}$ is the unique pair whose intersection has the
maximum size $H-2>0$.  This identifies the endpoints facing the gap;
the path order then identifies every other common set.  At an endpoint
there is only one component and the same conclusion follows after one
global reversal.  We may therefore write

\[
                         J_j(w)=J_j(v)\qquad(j\ne i).
\tag{2.3}
\]

Whenever $t,t+1\ne i$, consecutive-window differences recover the
leaving and entering letters:

\[
 \begin{aligned}
  \{w_t\}&=J_t(w)\setminus J_{t+1}(w),\\
  \{w_{t+H}\}&=J_{t+1}(w)\setminus J_t(w).
 \end{aligned}
\tag{2.4}
\]

The same identities hold for $v$.  Thus

\[
 w_t=v_t,\quad w_{t+H}=v_{t+H}
 \qquad
 \bigl(1\le t\le d-1, t\notin\{i-1,i\}\bigr).
\tag{2.5}
\]

Assume for contradiction that

\[
                         H+2\le i\le d-H-1.
\tag{2.6}
\]

Every word position except possibly

\[
                 i-1,\ i,\ i+H-1,\ i+H
\tag{2.7}
\]

is already fixed by (2.5).  The four displayed positions are fixed by
the other side of the same chronology:

\[
\begin{array}{c|c}
\text{position}&\text{nonexceptional transition which fixes it}\\ \hline
i-1&t=i-H-1\quad\text{(entering)},\\
i&t=i-H\quad\text{(entering)},\\
i+H-1&t=i+H-1\quad\text{(leaving)},\\
i+H&t=i+H\quad\text{(leaving)}.
\end{array}
\tag{2.8}
\]

The bounds in (2.6) put all four transitions in
({1,\ldots,d-1}\setminus\{i-1,i\}).  Hence (2.5) fixes these four
positions as well.  Therefore $w=v$ throughout the length-$r$
segment, so $J_i(w)=J_i(v)$, contradicting (2.1).  This proves
(2.2).  $\square$

### Remark 2.2 (why phase $2$ works)

At $i=2$, the entering history which would separately determine
$w_1,w_2$ does not exist.  Interchanging those two letters keeps
$J_1$ fixed, changes $J_2$, and leaves every $J_j$, $j\ge3$,
fixed.  This is exactly the certified boundary swap.  Theorem 2.1 says
that its missing left history, rather than a hidden lattice freedom, is
the source of the unit transfer.

## 3. Closed-catalyst macros

Call a sequence of table replacements **middle-neutral** if every
replacement preserves the aggregate middle incidence vector.  This
includes the certified complete-frame three-top conveyor and the
squarefree four- and eight-top moving-hole exchanges whenever they are
used in their proved owner-preserving form.

A **closed-companion unit macro** consists of:

1. an arbitrary sequence of middle-neutral replacements;
2. one one-root replacement whose middle derivative is $e_Y-e_X$;
3. another arbitrary sequence of middle-neutral replacements; and
4. exact restoration, at the endpoint, of every selected configuration
   except the selected configuration on one focal top $U$.

No restriction is placed on the number of intermediate moves, their
support, or their all-depth derivatives.

### Theorem 3.1 (closed routing cannot create boundary eligibility)

Let a closed-companion unit macro start and end in legal tables of
linear tight paths.  If its net middle derivative is $e_Y-e_X$, then
the occurrence of $X$ removed from the initial focal path lies in the
endpoint band (0.2).  In particular, the requested macro does not exist
for a chosen occurrence satisfying (0.3), even if an unbounded number
of conveyors and moving-hole exchanges and unbounded intermediate
collateral are allowed.

#### Proof

All nonfocal configurations agree literally at the two endpoints.
Every intermediate middle-neutral move has zero contribution to the
endpoint middle derivative.  Therefore the initial and final focal
owner decks satisfy

\[
 {\mathbf 1}_{\mathcal B_U(v)}-{\mathbf 1}_{\mathcal B_U(w)}=e_Y-e_X.
\tag{3.1}
\]

Complementation inside the fixed top $U$ is a bijection, so their
deleted-window decks have symmetric difference two.  Theorem 2.1
places the removed window, and hence its complementary owner $X$, in
(0.2).  $\square$

### Corollary 3.2 (an occurrence cannot be transported between tops and closed)

Suppose the neutral prefix appears to move the ownership of $X$ from
one top to another before the boundary swap.  If every companion is
restored at the endpoint, then the sole final changed top already
contained $X$ in its initial endpoint-band phases.  Thus the protocol
may choose a different pre-existing boundary occurrence of the same
target, but it cannot turn a specified interior occurrence into a
boundary occurrence.

#### Proof

Apply Theorem 3.1 to the sole final changed top.  Equation (3.1) forces
that top's initial deck to contain $X$.  $\square$

### Corollary 3.3 (an interior repair must remain open)

Any legal endpoint repair which removes a specified occurrence in the
interior range (0.3) and has total middle derivative $e_Y-e_X$ must
leave at least one nonfocal configuration changed.  Equivalently, an
interior repair cannot be a one-top endpoint difference, even if its
intermediate support is arbitrarily large.

#### Proof

If every nonfocal configuration were restored, Theorem 3.1 would put
the removed occurrence in (0.2), contrary to (0.3).  $\square$

## 4. Consequences for constant one

The direct boundary swap remains a valid $O(H)$-collateral primitive:
at each protected signed depth only intervals which contain exactly one
of its two adjacent boundary positions can change.  The failure proved
here is specifically the attempted **closed router** which was meant to
make an arbitrary collision eligible for that primitive.

The exact surviving choices are therefore:

1. prove that $o(W)$ collisions remain after optimizing only over the
   naturally boundary-eligible occurrences;
2. leave a positive number of companion configurations changed, and
   control their aggregate effect by a genuinely open catalytic flow;
3. use at least two nonneutral root replacements whose endpoint changes
   are distributed among several tops, rather than a closed conjugate
   of one boundary swap; or
4. enlarge the configuration catalogue beyond one linear tight path per
   top.

The first option needs a new charged-coverage theorem.  Options 2--3
are exactly the nonclosed moving-hole/conveyor routing problem; the
existing squarefree exchanges do not yet solve it.  What is now ruled
out is the strongest hoped-for local statement:

\[
 \boxed{
 \text{neutral route}\;\longrightarrow\;
 \text{one boundary unit transfer}\;\longrightarrow\;
 \text{exact companion restoration}}
\tag{4.1}
\]

for arbitrary chosen duplicate occurrences.  The obstruction is
statewise and survives arbitrary bounded support, arbitrary polynomial
all-depth collateral, and even arbitrarily long neutral routes.

## 5. Dependencies and scope

The one-root unit transfer and its $O(H)$ vertical locality are in
`MATH_THEOREM_COMMON_CORE_BOUNDARY_SWAP_MARGINAL_ESCAPE_20260727.md`.
The literal middle-neutral conveyor is in
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`.
The squarefree moving-hole exchanges are in
`MATH_THEOREM_PROMOTION_FOUR_TOP_SQUAREFREE_MOVING_HOLE_CUBE_20260726.md`
and
`MATH_THEOREM_PROMOTION_EIGHT_TOP_SQUAREFREE_MOVING_HOLE_EXCHANGE_20260726.md`.

Theorem 3.1 uses none of their internal formulas: it applies to every
middle-neutral routing library.  Its hypotheses are deliberately the
ones in the requested macro--exact endpoint restoration of all
companions and one remaining tight-path configuration.  It does not
rule out an open catalyst bank, several nonneutral endpoint changes, or
a construction which abandons the tight-path catalogue.
