# Phase-adaptive antipodal rings close the local vortex depth-drop gate

## Status

This note gives an explicit literal packet for the phase choice forced by a
critical balanced vortex.  Let the intrinsic child deadline be `e` and the
ambient deadline be `e+epsilon`, where `epsilon` is zero or one.  The same
common-core antipodal source ring, taken at the ambient owner-window width,
has the following two interpretations:

* for `epsilon=0`, its intrinsic row is already the rank-`q` owner row;
* for `epsilon=1`, its intrinsic row is a rank-`(q-1)` root row and one more
  union derivative is the rank-`q` owner row.

In both cases the ambient owners form a simple biresident Johnson cycle and
both immediate palettes are simple.  Thus the one-level phase gate in
`MATH_THEOREM_BALANCED_VORTEX_DEPTH_PHASE_AND_ZERO_CHARGE_SPLICE_20260806.md`
is locally nonempty and costs no source positions.

This is a packet theorem, not a full balanced-vortex decomposition.  It does
not select disjoint packets covering the whole slice, carry the complete
named lower atlas, or provide a boundary-tensor match to the exterior.

## 1. Parameters and source ring

Let `R` have size

\[
                             |R|=2q-1.                    \tag{1.1}
\]

Let `e` be the intrinsic child deadline and let

\[
 \epsilon\in\{0,1\},\qquad
 h=e+\epsilon+1                                      \tag{1.2}
\]

be the ambient owner-window width.  Assume

\[
                             2\le h\le q-1.               \tag{1.3}
\]

Choose disjoint sets

\[
 K\subset R,\qquad F=\{f_0,\ldots,f_{2h-1}\}\subset R-K,
 \qquad |K|=q-h.                                        \tag{1.4}
\]

There is room because

\[
                   |K|+|F|=q+h\le2q-1.                  \tag{1.5}
\]

On the cyclic period `2h`, use the nonempty source word

\[
                            C_t=K\cup\{f_t\}.             \tag{1.6}
\]

For a cyclic interval of private labels, write

\[
             F[t,t+\ell)=\{f_t,f_{t+1},\ldots,f_{t+\ell-1}\},
                                                               \tag{1.7}
\]

with subscripts modulo `2h`.

## 2. Exact phase-adaptive factor

### Theorem 2.1 (ambient antipodal ring)

The ambient length-`h` source windows are

\[
                         O_t=K\cup F[t,t+h).              \tag{2.1}
\]

They have all of the following properties.

1. The `2h` owners are distinct rank-`q` sets and form a simple Johnson
   cycle.
2. Their immediate lower and upper colours are respectively

   \[
   P_t=K\cup F[t+1,t+h),\qquad
   U_t=K\cup F[t,t+h+1),                                \tag{2.2}
   \]

   and the `2h` values in each row are pairwise distinct.
3. Every private coordinate has one owner run and one owner gap, both of
   length exactly `h`.  Core coordinates are constantly present and the
   unused coordinates are constantly absent.
4. Every cyclic source-union row of width `1<=ell<2h` is pairwise
   distinct.
5. The source ring is a literal one-step de Bruijn circulation; opening it
   at any phase exposes an exact order-`h-1` source state without changing
   its number of positions.

#### Proof

Every length-`h` source interval contains the common core and exactly the
private interval in (2.1), so it has rank `(q-h)+h=q`.  A one-step shift
deletes `f_t` and inserts `f_(t+h)`.  Both labels are different because
`h<2h`, proving Johnson adjacency, and a proper cyclic interval of distinct
labels recovers its start phase, proving owner simplicity.

Intersecting and uniting consecutive owners gives (2.2).  The private
interval lengths `h-1` and `h+1` lie strictly between zero and `2h`, so
their starts are again recoverable.  A private label lies in precisely the
`h` ambient owner windows containing its unique source occurrence and is
absent from the other `h`; this proves biresidence.  At any source width
`ell<2h`, the private part is exactly `F[t,t+ell)`, proving Item 4.
Finally every cyclic word is balanced under the one-letter de Bruijn shift,
and cutting a cyclic word only chooses a state; it inserts no position.
\(\square\)

### Theorem 2.2 (the two intrinsic phases)

Put

\[
                         Z=\mathsf U^e C,                 \tag{2.3}
\]

where `mathsf U` is the adjacent-union derivative.  Then:

* if `epsilon=0`,

  \[
                  Z_t=K\cup F[t,t+h)=O_t               \tag{2.4}
  \]

  is the owner phase;
* if `epsilon=1`,

  \[
                  Z_t=K\cup F[t,t+h-1)                 \tag{2.5}
  \]

  is a simple rank-`(q-1)` root phase and

  \[
                  Z_t\cup Z_{t+1}=O_t.                 \tag{2.6}
  \]

In the second case every private coordinate has a positive run of length
`h-1=e+1` in `Z`, so `C` is already a literal depth-`e` antecedent of the
required root phase.  Hence either value of `epsilon` is realized on the
same `2h` source positions.

#### Proof

By definition, `mathsf U^e C` is the union of `e+1` consecutive source
letters.  If `epsilon=0`, then `e+1=h`, giving (2.4).  If `epsilon=1`, then
`e+1=h-1`, giving (2.5); its rank is

\[
                         (q-h)+(h-1)=q-1.
\]

Adjacent private `(h-1)`-intervals have union the `h`-interval in (2.6).
The run assertion follows from the unique source occurrence of each
private label.  The displayed source word itself witnesses the final
antecedent claim.  \(\square\)

## 3. Lift to the balanced ambient slice

Let `A,B` be disjoint fixed sets of size `a`, let `R` be their complement
in a `(2r-1)`-set, and put `q=r-a`.  Define

\[
                          \widehat C_t=A\cup C_t.          \tag{3.1}
\]

### Corollary 3.1 (literal ambient phase packet)

For either phase in Theorem 2.2, the length-`h` ambient owners are

\[
                    \widehat O_t=A\cup O_t               \tag{3.2}
\]

and belong to the balanced owner slice.  All interval identities, both
immediate palettes, and the source entrance/exit states lift by adjoining
`A`.  Coordinates of `A` are constantly present, coordinates of `B` are
constantly absent, and every moving coordinate retains the biresidence in
Theorem 2.1.

#### Proof

For every source interval `I`,

\[
             \bigcup_{t\in I}(A\cup C_t)
                 =A\cup\bigcup_{t\in I}C_t.
\]

Apply Theorems 2.1--2.2.  \(\square\)

## 4. Symmetric fractional consequence and exact scope

Let the symmetric group of `R` act on all choices `(K,F,cyclic order)` in
Section 1.  It is transitive on each of the owner, lower-root, and
upper-colour shores.  Every packet has `2h` distinct occurrences in each
row.  Since the owner and lower-root shores have the common size

\[
             W_q=\binom{2q-1}{q}=\binom{2q-1}{q-1},       \tag{4.1}
\]

one uniform packet weight saturates both shores simultaneously.  The
upper shore has size

\[
 \binom{2q-1}{q+1}={q-1\over q+1}W_q,                    \tag{4.2}
\]

so the same normalization gives uniform upper load `(q+1)/(q-1)`.
Retaining each upper occurrence with the uniform fractional factor
`(q-1)/(q+1)` closes the immediate-upper row as well.  Thus both intrinsic
phases have an exact fractional owner/lower/upper factor; in particular the
local phase-drop vocabulary has no scalar or orbit obstruction.

This symmetry observation is not a simultaneous integral factor theorem:
upper thinning is not an integral named-occurrence choice, named lower
tickets introduce laminar high-codegree coordinates, and different packets
can collide.  The exact
remaining global statement is:

> select a phase-appropriate disjoint family of antipodal rings covering
> the balanced owner/root slice, carrying the required lower and upper
> occurrence tickets, and exposing one boundary tensor compatible with the
> exterior zero-charge splice.

Thus the ambient deadline mismatch and the local root-phase existence are
closed.  Integral packet cover-down, full decoration, and regenerative
state matching remain open.

## 5. Exact-state splicing is incompatible with a disjoint root leave

The strongest sufficient splice rule in the boundary-tensor theorem is
equality of an entire oriented order-`h-1` source state.  For the present
packet that rule cannot be used against a resource-disjoint exterior
factor.

### Proposition 5.1 (shared-state root collision)

Let an opened ambient source component have a length-`h-1` state

\[
                         (S_0,\ldots,S_{h-2})             \tag{5.1}
\]

whose union has rank `r-1`, and suppose the two adjacent length-`h` owners
at the cut are distinct rank-`r` Johnson neighbours.  In that owner chronology,
that union is the immediate-lower colour at the cut.  Hence two exact
owner/lower factors exposing identical states (5.1) use the same lower
resource.  In particular, an exterior factor which is disjoint from the
balanced vortex on both owner and root shores cannot share a complete
oriented state with the vortex ring.

#### Proof

The owners immediately before and after the cut are

\[
 S_{-1}\cup S_0\cup\cdots\cup S_{h-2},\qquad
 S_0\cup\cdots\cup S_{h-2}\cup S_{h-1}.
\]

Their intersection contains the state union.  Both owners have rank `r`,
are Johnson-adjacent, and the state union already has rank `r-1`; therefore
their intersection is exactly that union.  Identical source states have
the same union and hence the same lower colour.  \(\square\)

For the ring in Section 2 the state union is

\[
                         K\cup F[t,t+h-1),                \tag{5.2}
\]

of rank `q-1`, and after adjoining `A` it is a member of the balanced root
slice.  Proposition 5.1 therefore applies exactly.

Consequently a genuinely disjoint vortex cover-down must use the full
two-cut multiset identity rather than the identical-state corollary, or it
must deliberately coalesce and compensate one lower-root occurrence.
This is a structural boundary obstruction, not an additive-length charge:
the phase-adaptive packet remains zero-length, but its exterior port must
be a nontrivial common-cap tensor.

## 6. A nontrivial zero-charge tensor: pivot absorption

There is a useful sufficient tensor which does not identify either full
boundary state.  Use the cumulative-union notation `L_i(C),R_j(C)` of the
two-cut theorem.

### Theorem 6.1 (absorbed-left pivot splice)

Let `C,E` be two opened source components.  Suppose there is a coordinate
`c` such that for every relevant `i>=1`,

\[
 L_i(C)=J_i(C)\cup\{c\},\qquad
 L_i(E)=J_i(E)\cup\{c\},                                \tag{6.1}
\]

and, for every relevant `i,j>=1`,

\[
 J_i(C)\cup J_i(E)
       \subseteq R_j(C)\cap R_j(E),qquad
 c\notin R_j(C)\cup R_j(E).                             \tag{6.2}
\]

Then the boundary tensor is preserved with the two old cells exchanged:

\[
 \begin{aligned}
 L_i(C)\cup R_j(E)&=L_i(E)\cup R_j(E),\\
 L_i(E)\cup R_j(C)&=L_i(C)\cup R_j(C).                  \tag{6.3}
 \end{aligned}
\]

Consequently the cross-splice is OR-transparent through every width on
which (6.1)--(6.2) hold.  If the paired occurrence tickets are allowed to
exchange components and the two pivot seams pass the capped-age test, the
splice is a literal zero-charge fusion.

#### Proof

By (6.2), adjoining either `J_i(C)` or `J_i(E)` to either right cumulative
union changes nothing.  Since `c` belongs to neither right cumulative
union, all four cells are obtained by adjoining the same one-coordinate
pivot to the appropriate right value.  This gives (6.3), which is exactly
the swapped orientation of the boundary-tensor identity.  The ticket and
residence assertions are the corresponding clauses of the exact two-cut
theorem.  \(\square\)

Unlike complete state equality, Theorem 6.1 does not formally identify the
two left cumulative unions.  However, at the saturated owner/root ranks its
absorption hypothesis still forces a collision on one side.

### Proposition 6.2 (pivot absorption still shares a root)

Assume the width is `h`, both full left states `L_(h-1)(C),L_(h-1)(E)`
and both full right states `R_(h-1)(C),R_(h-1)(E)` have rank `r-1`, and
(6.1)--(6.2) hold through width `h`.  Then either

\[
 L_{h-1}(C)=L_{h-1}(E)
 \quad\hbox{or}\quad
 R_{h-1}(C)=R_{h-1}(E).                                 \tag{6.4}
\]

#### Proof

Because `c` is absent from the right states and each full left state has
rank `r-1`, both `J_(h-1)(C)` and `J_(h-1)(E)` have rank `r-2`.  If they
are equal, the left roots in (6.4) are equal.  Otherwise their union has
rank at least `r-1`.  Taking `i=h-1,j=1` in (6.2), that union lies in both
first right source letters and hence in both full right states.  Those
states have rank `r-1`, so both equal the same union.  \(\square\)

Thus the tempting portal prescription

> plant a common leaving pivot `c`; place all other left-collar labels
> inside a core persistent on both right collars; and pair the boundary
> tickets in the exchanged orientation.

is OR-transparent but cannot be resource-disjoint at the exact lower-q1
level.  It can be used only with one coalesced-and-compensated root.

### Corollary 6.3 (a resource-disjoint fusion needs at least a Boolean C6)

No nontrivial two-edge switch fuses two resource-disjoint exact
owner/lower factors in the middle-levels incidence graph.  The first
possible exact local trade has three old and three new incidence edges,
namely a Boolean `C6`.

#### Proof

A two-edge factor switch would replace

\[
 q_1o_1,\ q_2o_2
 \quad\hbox{by}\quad
 q_1o_2,\ q_2o_1.                                      \tag{6.5}
\]

With four distinct resources, the four displayed incidences form a
`C4`.  The middle-levels incidence graph has no `C4`: two distinct
rank-`r` owners have at most one common rank-`(r-1)` facet.  If resources
are identified, the switch is trivial or has a collision.  Boolean
incidence `C6` trades exist and are therefore the first nontrivial exact
alternative.  \(\square\)

The exact regenerative port target is consequently a **three-way C6
state splice** (or a longer alternating trade) whose complete OR/ticket
boundary tensor and capped ages are preserved.  A two-cut state splice can
still be used after explicitly pricing one repeated root, but it is not an
exact resource-disjoint vortex fusion.
