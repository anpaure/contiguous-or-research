# Halo diamonds have abundant phase-adaptive antipodal lifts

## Status

Fix a balanced coordinate vortex and its symmetric constant-radius halo.
Every legal coloured diamond in that halo has an explicit, large family of
literal antipodal-ring lifts.  The owner and root rows of every such lift
remain in the same symmetric halo, its upper row lies in the halo enlarged
by only one `B`-boundary unit, and all of its central suffix tickets are
simple.  The lift is valid in either of the two deadline phases and is
biresident in the phase which is actually compiled.

There is also a shorter `h+2` lift through every diamond.  It has the same
simple owner/root/upper and suffix-ticket rows, but its private-coordinate
zero gaps have length only two (or three in the root phase), so it cannot
replace the antipodal lift when complementary residence is required.

The antipodal period `2h` is not rigid.  Every period `L>=2h` has the same
phase, ticket and halo properties, with run/gap pair `(h,L-h)`.  In
particular the compatible periods `2h` and `2h+1` have identical symmetric
fractional ledgers and remove the previously observed fixed-period
divisibility obstruction at the exact scalar level.

The determinant-two minor in the coloured diamond matrix is completely
sharp locally: its Smith normal form is `diag(1,1,2)`.  Doubling removes
the unique parity obstruction, and for the canonical unit-demand triangle
one additional owner incidence removes it as well.  Moreover every fixed
boundary fibre of the halo contains the
exact ternary Boolean `C6` circuit, which preserves lower, upper, tail and
head resources.  Thus determinant two is not itself an asymptotic upper
defect.  The `C6` can transport topology and integral parity, but, because
it preserves the upper palette, it cannot create a missing upper colour.

The unresolved statement is genuinely global: select the abundant ring
lifts disjointly so that their inter-packet upper repetitions attain the
unavoidable minimum and their occurrence-labelled suffix chains are
simultaneously compatible.  The exact defect-conservation formula at the
end of this note shows that this is the only immediate-upper loss left.

## 1. Halo notation and coloured diamonds

Put

\[
                    n=2r-1.
\]

Fix disjoint coordinate banks `A,B` of size `a`, and let

\[
                    C=[n]\setminus(A\cup B),\qquad |C|=2(r-a)-1.
\]

For any set `X`, write

\[
 \alpha(X)=|A\setminus X|,\qquad \beta(X)=|B\cap X|,
\]

and use the rectangular halo

\[
 {\cal H}^{p,q}_s(A,B)=
 \{X\in\tbinom{[n]}s:\alpha(X)\le p,\ \beta(X)\le q\}.
 \tag{1.1}
\]

A coloured central diamond is a quadruple

\[
 Q\subset O_x=Q+x,\quad Q\subset O_y=Q+y,\quad
 U=Q+\{x,y\},                                      \tag{1.2}
\]

where `|Q|=r-1` and `x,y` are distinct and outside `Q`.  In a central
factor, `Q` is the immediate-lower colour, `O_x,O_y` are the two incident
owners, and `U` is their immediate-upper colour.

Throughout Sections 2--3 let `h` be the ambient owner-window width.  In a
critical vortex it has the form

\[
             h=e+\varepsilon+1,\qquad \varepsilon\in\{0,1\},   \tag{1.3}
\]

where `e` is the intrinsic child deadline.  Thus the compiled intrinsic
row is the owner row when `varepsilon=0` and the root row when
`varepsilon=1`.

## 2. Exact anchored antipodal lift

### Theorem 2.1 (every halo diamond has an antipodal lift)

Assume

\[
 Q,O_x,O_y\in{\cal H}^{p,p}(A,B)                         \tag{2.1}
\]

and

\[
 |Q\cap C|\ge h-1,\qquad |C\setminus U|\ge h-1.          \tag{2.2}
\]

Then the oriented diamond (1.2) has exactly

\[
 \boxed{(|Q\cap C|)_{h-1}(|C\setminus U|)_{h-1}}         \tag{2.3}
\]

anchored antipodal lifts of the following form.

Every owner and every root of the lift belongs to the symmetric
`(p,p)`-halo, and every upper colour belongs to the `(p,p+1)`-halo.  The
distinguished transition has lower, owner and
upper resources exactly `Q,{O_x,O_y},U`.

#### Construction and proof

Choose ordered tuples

\[
 G=(g_1,\ldots,g_{h-1})\in(Q\cap C)_{\neq}^{h-1},\qquad
 Z=(z_1,\ldots,z_{h-1})\in(C\setminus U)_{\neq}^{h-1}.    \tag{2.4}
\]

Put

\[
 K=Q\setminus G
\]

and cyclically order the `2h` private labels as

\[
 F=(x,g_1,\ldots,g_{h-1},y,z_1,\ldots,z_{h-1}).          \tag{2.5}
\]

Use the source ring

\[
                         S_t=K\cup\{f_t\}.               \tag{2.6}
\]

Its length-`h` owners are

\[
                         T_t=K\cup F[t,t+h).              \tag{2.7}
\]

At the distinguished transition,

\[
 T_0=K\cup G\cup\{x\}=Q+x=O_x,
 \qquad
 T_1=K\cup G\cup\{y\}=Q+y=O_y.                         \tag{2.8}
\]

Their intersection and union are `Q` and `U`, respectively.  This proves
the anchoring assertion.  Conversely, an oriented anchored lift of the
displayed form recovers the ordered neutral tuples `G` and `Z`, so (2.3)
is exact.

The only private labels which lie in `A union B` are `x,y`, and they are
antipodal in the `2h`-cycle.  Every `h`-interval therefore contains
exactly one of them; every `(h-1)`-interval contains at most one; and every
`(h+1)`-interval contains at most two.  The fixed core `K` has exactly the
same `A,B` trace as `Q`, because only neutral labels were removed from
`Q`.

If `x` or `y` belongs to `B`, condition (2.1) forces
`beta(Q) <= p-1`.  Hence owners and roots have `beta <= p`, while an upper
interval has `beta <= p+1` even when it contains both `x` and `y`.  Adding
`x` or `y` can only restore a missing `A`-coordinate, so no row has larger
`alpha` than `Q`.  This proves the halo assertions.  All row ranks follow
from

\[
 |K|=r-h
\]

and private interval lengths `h-1,h,h+1`.  Proper cyclic intervals recover
their initial phase, so every one of the three rows is simple. \(\square\)

### Corollary 2.2 (critical vortices always have room)

Put `q=r-a`.  If `Q` lies in the symmetric `p`-halo, then

\[
 |Q\cap C|\ge q-1-p,\qquad |C\setminus U|\ge q-2-p.       \tag{2.9}
\]

Consequently Theorem 2.1 applies whenever

\[
                         h\le q-1-p.                      \tag{2.10}
\]

In particular it applies to the critical choice
`a=O(log(r))`, `h` of order `sqrt(r)`, and fixed `p`, for all sufficiently large
`r`.

#### Proof

Writing `alpha=alpha(Q)` and `beta=beta(Q)`,

\[
 |Q\cap C|=r-1-(a-\alpha)-\beta=q-1+\alpha-\beta
            \ge q-1-p.
\]

Also `|U intersect C| <= |Q intersect C|+2 <= q+1+p`, while `|C|=2q-1`,
which gives the second bound in (2.9).  Condition (2.10) implies both
inequalities in (2.2). \(\square\)

### Proposition 2.3 (exact neutral-coordinate spread)

Choose an anchored lift uniformly from the family in Theorem 2.1.  For
distinct neutral sets

\[
 R_G\subseteq Q\cap C,\qquad R_Z\subseteq C\setminus U,
 \qquad |R_G|=s,\quad |R_Z|=t,
\]

the probability that all labels of `R_G` are used in the moving tuple
`G` and all labels of `R_Z` are used in the return tuple `Z` is

\[
 \boxed{
 { (h-1)_s\over(|Q\cap C|)_s}
 { (h-1)_t\over(|C\setminus U|)_t}.}                    \tag{2.11}
\]

At critical depth this is

\[
                         O_{s,t}((h/q)^{s+t}).            \tag{2.12}
\]

#### Proof

The ordered tuple `G` is uniform among all injective `(h-1)`-tuples from
`Q intersect C`, and `Z` is independently uniform among the corresponding
tuples from `C minus U`.  The probability that a fixed `s`-set occurs in
the first tuple is `(h-1)_s/(|Q intersect C|)_s`, and similarly for the
second.  Corollary 2.2 and `h=o(q)` give (2.12). \(\square\)

This is coordinate spread only.  It does not assert resource or ticket
spread after the common anchored diamond has been fixed.

### Theorem 2.4 (variable-period biresident lift)

Let `L>=2h`, and strengthen (2.2) to

\[
                         |C\setminus U|\ge L-h-1.         \tag{2.13}
\]

Then the same oriented diamond has exactly

\[
 \boxed{(|Q\cap C|)_{h-1}(|C\setminus U|)_{L-h-1}}       \tag{2.14}
\]

anchored lifts of period `L`, owner-window width `h`, and source form
`K+f_t`.  Every owner and root remains in the symmetric `(p,p)`-halo,
every upper remains in the `(p,p+1)`-halo, every proper row is simple,
and every private coordinate has owner run `h` and owner gap `L-h`.

#### Proof

Choose `G` as in (2.4), choose an ordered neutral tuple

\[
 Z=(z_1,\ldots,z_{L-h-1})\in(C\setminus U)_{\neq}^{L-h-1},
\]

and use the cyclic private order

\[
                         F=(x,G,y,Z).                     \tag{2.15}
\]

The distinguished length-`h` windows are still `Q+x,Q+y`.  Since `x,y`
are at cyclic distance `h` and `L>=2h`, an `h`-interval contains at most
one of them, an `(h-1)`-interval contains at most one, and an `(h+1)`
interval contains at most two.  The halo proof of Theorem 2.1 is therefore
unchanged.  All three interval lengths are proper, proving simplicity.
A private label occurs once in period `L`, hence has run `h` and gap
`L-h` in the owner row.  The ordered choices give (2.14). \(\square\)

### Corollary 2.5 (the scalar period obstruction disappears)

Suppose

\[
 h\le q-2-p.                                             \tag{2.16}
\]

Then every halo diamond has lifts of both periods `2h` and `2h+1` with
all the properties of Theorem 2.4.  Moreover every integer

\[
                         N\ge4h^2-2h                     \tag{2.17}
\]

is a nonnegative integral combination of `2h` and `2h+1`.

#### Proof

Corollary 2.2 gives `|C minus U|>=q-2-p>=h`, which supplies the return
tuple for period `2h+1`; period `2h` needs only `h-1` labels.  The two
periods are coprime.  Their Frobenius number is

\[
 (2h)(2h+1)-2h-(2h+1)=4h^2-2h-1,
\]

which proves (2.17). \(\square\)

Thus a cover-down may mix two consecutive biresident periods without
changing the deadline phase or the ticket vocabulary.  The old divisibility
failure `2h does not divide N` is not a scalar obstruction.  What remains
is the existence of a resource-disjoint mixed-period packet cover.

### Theorem 2.6 (all long-gap periods have the same fractional ledger)

Work in the balanced core on a neutral ground set `R` of size `2q-1`.
Fix `h` and any period

\[
                         2h\le L\le q+h-1.               \tag{2.18}
\]

Take the full symmetric orbit of rings

\[
 |K|=q-h,\qquad |F|=L,\qquad S_t=K\cup\{f_t\},           \tag{2.19}
\]

and normalize its uniform weight so that every rank-`q` owner has load
one.  Then:

1. every rank-`(q-1)` root also has load one;
2. every rank-`(q+1)` upper colour has raw load

   \[
                         {q+1\over q-1};                  \tag{2.20}
   \]

3. for every suffix width `1<=ell<h`, every rank-`(q-h+ell)` target has
   ticket load

   \[
       {\binom{2q-1}{q}\over
        \binom{2q-1}{q-h+\ell}};                         \tag{2.21}
   \]

4. all of these loads are independent of `L`.

Consequently any convex mixture of the periods `2h` and `2h+1` preserves
the complete fractional owner/root/upper/ticket ledger.

#### Proof

The symmetric group of `R` is transitive on every named rank shore.  One
ring has `L` distinct owners, roots, uppers, and width-`ell` tickets.
After owner normalization, the total selected occurrence mass in each row
is therefore

\[
                         W_q=\binom{2q-1}{q}.             \tag{2.22}
\]

The root shore also has size `W_q`, proving Item 1.  The upper-shore size
is

\[
             \binom{2q-1}{q+1}={q-1\over q+1}W_q.
\]

Divide (2.22) by this quantity to get (2.20), and divide it by the
width-`ell` ticket-shore size to obtain
(2.21).  The period cancels in every double count. \(\square\)

### Theorem 2.7 (long-gap rings confine every lower ticket to the belt)

Let `S` be a fixed `2a`-coordinate status block, let `C=[n] minus S`, and
write

\[
                         \sigma(X)=|X\cap S|-a.           \tag{2.23}
\]

Suppose a coloured diamond `Q,Q+x,Q+y,U` has its root and both owners in
the status belt `[-p,p]`.  Construct a period-`L>=2h` lift by choosing all
labels of `G` and `Z` in `C`, as in Theorem 2.4.  Then:

1. every owner, root, and every proper suffix ticket of the ring has
   status in `[-p,p]`;
2. every immediate upper has status in `[-p,p+1]`.

Thus this ring vocabulary has no unbounded lower-ticket status excursion.

#### Proof

Put `j=sigma(Q)`.  Since `G` is neutral, the fixed core `K=Q minus G`
has status `j`.  The only private labels which can meet `S` are `x,y`,
and their cyclic distance is `h`.  Every private interval of length at
most `h` therefore contains at most one of them.  Its status is `j` or
`j+1`.

If one of `x,y` belongs to `S`, the corresponding anchored owner has
status `j+1`; the hypothesis therefore forces `j+1<=p`.  Hence all owner,
root, and proper-ticket statuses lie in `[-p,p]`.  An upper interval has
length `h+1` and may contain both `x,y`.  This gives at worst `j+2`; when
both labels lie in `S`, the two anchored owners still force `j<=p-1`, so
`j+2<=p+1`.  The lower status bound never decreases because all added
boundary labels lie in `S`. \(\square\)

For the tunable status belt, the generic `D+2` catalogue can have ticket
excursion `Theta(min(a,D))`.  Theorem 2.7 shows that this excursion is not
forced by the deadline or by the selected diamond: it disappears entirely
when the diamond is lifted with the neutral long-gap vocabulary.  The
remaining question is whether enough such lifts can be selected
simultaneously to realize the belt's fractional coloured factor.

## 3. Phase, tickets and residence

### Theorem 3.1 (the anchored lift is phase-adaptive and biresident)

For any ring in Theorem 2.4 (including Theorem 2.1), let `Uop` denote the
adjacent-union derivative and let `e,h,eps` satisfy (1.3).

1. If `eps=0`, `Uop^e S` is the owner row (2.7).
2. If `eps=1`, `Uop^e S` is the simple root row

   \[
                  K\cup F[t,t+h-1),                      \tag{3.1}
   \]

   and one further derivative is the owner row.
3. At every phase, the proper suffix unions

   \[
       K\cup F[t-\ell+1,t+1),\qquad1\le\ell<h,           \tag{3.2}
   \]

   form one nested ticket.  All tickets in one ring are target-disjoint.
4. In the owner row every private coordinate has one run of length `h` and
   one gap of length `L-h`.  In the root row (3.1) it has one run of
   length `h-1` and one gap of length `L-h+1`.  Thus in the phase actually
   compiled, both nonconstant runs and gaps have length at least `e+1`.

#### Proof

The `e`-th union derivative is the union of `e+1` consecutive source
letters.  Equations (1.3) and (2.6) give Items 1--2.  Equation (3.2) is a
proper private interval; its rank is `r-h+ell`, and its length and start
recover it uniquely.  This proves Item 3.  A private label occurs once in
a period of length `L`, so its membership in sliding windows of lengths
`h` and `h-1` has respectively the run/gap pairs stated in Item 4.
Finally `e+1=h` in the owner phase and `e+1=h-1` in the root phase.
\(\square\)

The oriented source state exported at a cut is explicit: it is an
`(h-1)`-interval of the letters `K+f_t`.  Exact state equality with a
resource-disjoint exterior factor is impossible because its union is the
root at that cut.  Thus Theorem 3.1 closes local phase and residence, but
the exterior splice still requires a nontrivial `C6` (or longer) boundary
tensor.

### Theorem 3.2 (exact recognition of a long-gap factor cycle)

Let

\[
 T_0,T_1,\ldots,T_{L-1},\qquad L\ge2h,
\]

be a cyclic simple Johnson walk of rank-`r` owners.  Write its deletion and
insertion labels as

\[
 T_{t+1}=T_t-\{a_t\}+\{b_t\}.                            \tag{3.3}
\]

It is the owner row of a common-core, one-private-letter source ring of
period `L` and owner-window width `h` if and only if

\[
 \boxed{
 a_0,\ldots,a_{L-1}\text{ are pairwise distinct},
 \qquad b_t=a_{t+h}\quad(t\bmod L).}                     \tag{3.4}
\]

When (3.4) holds, the source ring is uniquely recovered, up to cyclic
phase, as

\[
 K=T_0\cap\cdots\cap T_{L-1},\qquad
 S_t=K\cup\{a_t\},                                      \tag{3.5}
\]

and `|K|=r-h`.

#### Proof

For a ring `T_t=K union F[t,t+h)`, shifting deletes `f_t` and inserts
`f_(t+h)`, so (3.4) is necessary.

Conversely, under (3.4), coordinate `a_s` is inserted at transition
`s-h` and deleted at transition `s`.  It is therefore present in exactly
`h` consecutive owners and absent in the other `L-h`.  No other coordinate
changes.  Thus every owner consists of the common fixed part `K` and one
cyclic `h`-interval of the deletion word `(a_t)`.  It follows that
`|K|=r-h` and that (3.5) has the prescribed owner row.  The deletion word
and common intersection are forced by the given walk, proving uniqueness.
\(\square\)

Theorem 3.2 is the exact reason the uncoloured halo `2`-factor cannot be
lifted formally.  The integral factor theorem controls only degree two; it
does not force a permitted cycle length, distinct deletion labels, or the
long-gap monodromy `b_t=a_(t+h)`.  The antipodal ring is the extremal case
`L=2h`.

## 4. A shorter `h+2` lift and its exact limitation

### Theorem 4.1 (anchored upper-rich lift)

Under the hypotheses of Theorem 2.1, choose an ordered neutral
`(h-1)`-tuple `G` in `Q cap C` and one neutral label
`b in C minus U`.  Put

\[
 K=Q\setminus G,\qquad H=U\cup\{b\},                     \tag{4.1}
\]

and cyclically order `F=H minus K` beginning with

\[
                         x,b,y                           \tag{4.2}
\]

and then the ordered entries of `G`.  The source ring `K+f_t` has period
`h+2`, owner-window width `h`, and one transition whose resources are
exactly `Q,{O_x,O_y},U`.  Hence the number of oriented anchored lifts of
this form is

\[
                 (|Q\cap C|)_{h-1}|C\setminus U|.         \tag{4.3}
\]

All owner, root and upper rows are simple.  They lie in the enlarged
`(p,p+1)` halo.  Every proper suffix chain inside one ring is simple and
target-disjoint.

However, a private coordinate has owner run `h` and gap `2`; in the root
phase it has run `h-1` and gap `3`.  Therefore the packet is positively
resident, but it is not biresident once `h>3`.

#### Proof

With the indexing in which the consecutive triple in (4.2) is
`f_(t-2),f_(t-1),f_t`, the standard two-hole formulas give

\[
 \begin{aligned}
  Q_t&=H-\{x,b,y\}=Q,\\
  U_t&=H-\{b\}=U,\\
  T_t&=H-\{x,b\}=Q+y,\\
  T_{t+1}&=H-\{b,y\}=Q+x.
 \end{aligned}                                           \tag{4.4}
\]

This proves the anchor and the count.  Only `x,y` are nonneutral private
labels.  Unlike the antipodal ring, a window may contain both, but (2.1)
still bounds its `B`-defect by `p+1`; its `A`-defect cannot increase.
Proper private intervals are simple.  The run/gap assertion is immediate
from one occurrence in a cycle of length `h+2`. \(\square\)

Thus the `h+2` packet is the more economical upper-rich local vocabulary,
whereas the `2h` antipodal packet is the phase-safe vocabulary needed for
the balanced-vortex recursion.

## 5. The determinant-two obstruction is exactly one parity bit

Fix a root `Q` and three owner neighbours `Q+x,Q+y,Q+z`.  On the three
owner rows, the three possible diamonds have matrix

\[
 A_3=
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix}.                                          \tag{5.1}
\]

### Theorem 5.1 (sharp local Smith form)

The Smith normal form of `A_3` is

\[
                         \operatorname{diag}(1,1,2).      \tag{5.2}
\]

For an integral desired owner-degree vector `b=(b_x,b_y,b_z)`, the unique
rational solution is

\[
 \begin{aligned}
 z_{xy}&=(b_x+b_y-b_z)/2,\\
 z_{xz}&=(b_x+b_z-b_y)/2,\\
 z_{yz}&=(b_y+b_z-b_x)/2.                                \tag{5.3}
 \end{aligned}
\]

It is nonnegative exactly when the three triangle inequalities hold, and
it is integral exactly when

\[
                         b_x+b_y+b_z\equiv0\pmod2.        \tag{5.4}
\]

In particular, `b=(1,1,1)` has the unique half-integral solution
`(1/2,1/2,1/2)`.  Doubling selects all three diamonds once, covers their
three upper colours once, and gives owner degree two.  Alternatively,
adding one unit to any coordinate of `b` produces an integral two-diamond
solution.

#### Proof

The determinant of (5.1) is `-2`, one entry has gcd one, and a `2 by 2`
minor has determinant one.  This gives (5.2).  Solving the three equations
gives (5.3), from which nonnegativity and (5.4) follow. \(\square\)

The doubled triangle is **not** a one-copy factor: it uses the root `Q`
three times.  Likewise the one-unit correction must obtain that incidence
from another root slot.  Therefore determinant two is cured locally by a
two-cover, but projecting the cover back to one root occurrence is a real
global routing problem.

## 6. Every boundary fibre contains the exact Boolean `C6` circuit

### Theorem 6.1 (halo-internal signed circuit)

Fix any boundary trace `D contained in A union B` satisfying the halo
bounds.  Choose a neutral set `S_C contained in C` so that

\[
                         S=D\cup S_C,qquad |S|=r-2,       \tag{6.1}
\]

and choose four distinct neutral labels `a,b,c,d` outside `S`.  Put

\[
\begin{array}{lll}
 L_a=S+a,&L_b=S+b,&L_c=S+c,\\
 V_a=S+b+c+d,&V_b=S+a+c+d,&V_c=S+a+b+d,
\end{array}                                               \tag{6.2}
\]

and

\[
\begin{array}{lll}
 A_0=S+a+d,&B_0=S+a+c,&C_0=S+c+d,\\
 D_0=S+b+c,&E_0=S+b+d,&F_0=S+a+b.
\end{array}                                               \tag{6.3}
\]

The three old ordered diamonds

\[
 (L_a,V_b,A_0,B_0),\quad
 (L_c,V_a,C_0,D_0),\quad
 (L_b,V_c,E_0,F_0)                                      \tag{6.4}
\]

and the three new ordered diamonds

\[
 (L_a,V_c,A_0,F_0),\quad
 (L_c,V_b,C_0,B_0),\quad
 (L_b,V_a,E_0,D_0)                                      \tag{6.5}
\]

use exactly the same lower, upper, tail and head resources.  All resources
have boundary trace `D`, and hence the complete signed circuit lies inside
one halo fibre.

#### Proof

All active labels are neutral, so every displayed set has boundary trace
`D`.  Direct intersections and unions verify, for example,

\[
 A_0\cap B_0=L_a,qquad A_0\cup B_0=V_b,
\]

and the other five identities follow cyclically.  The lower resources on
both sides are `{L_a,L_b,L_c}`, the upper resources are
`{V_a,V_b,V_c}`, the tails are `{A_0,C_0,E_0}`, and the heads are
`{B_0,D_0,F_0}`. \(\square\)

This circuit is an exact integral rewiring mechanism which is invisible to
the failed TU argument.  In its cycle mode it may merge three physical
cycles into one.  It does not, by itself, project the doubled triangle of
Theorem 5.1 to a one-copy factor.  Moreover its upper multiset is identical
in the two phases.  Therefore no sequence of these circuits changes the
number of missing upper colours.  It repairs topology and transports
already integral choices; it does not solve upper cover-down.

The all-depth lift of (6.4)--(6.5) is also not automatic.  Theorem 2.1
gives many literal ring embeddings of each individual atom, but it does
not say that the six embeddings can be chosen with identical complete
suffix-ticket inventories.  That is a separate flagged-circuit gate.

## 7. Exact upper-defect conservation in the halo

Let a selected owner/root `2`-factor have `N` roots, and let
`R_req` be the required affected upper bank of size `M`.  For
`U in R_req`,
let `mu_U` be its number of selected diamond occurrences.  Put

\[
 \begin{aligned}
 z&=N-\sum_{U\in\mathcal R_{\rm req}}\mu_U,
       &&\text{(occurrences outside the required bank)},\\
 m&=|\{U\in\mathcal R_{\rm req}:\mu_U=0\}|,
       &&\text{(missing required uppers)},\\
 e&=\sum_{U\in\mathcal R_{\rm req}}(\mu_U-1)_+,
       &&\text{(repeat excess inside the bank)}.
 \end{aligned}                                           \tag{7.1}
\]

### Theorem 7.1 (sharp residual formula)

\[
 \boxed{m=e-(N-M)+z.}                                    \tag{7.2}
\]

#### Proof

The total multiplicity inside the required bank is both `N-z` and

\[
                  (M-m)+e.
\]

Equating them gives (7.2). \(\square\)

Thus a bounded upper leave is equivalent to

\[
                  e+z=(N-M)+O(1).                        \tag{7.3}
\]

The term `N-M` is the unavoidable duplicate budget.  Antipodal and `h+2`
rings are internally upper-simple, so `e` in a packet cover is caused only
by collisions between different packets.  Neither the determinant-two
parity correction nor the palette-preserving `C6` changes (7.2).

### Corollary 7.2 (rankwise ticket conservation)

Suppose a disjoint family of antipodal rings has `N` source phases.  Fix a
proper suffix width `ell<h` and a required occurrence-labelled ticket bank
`T_ell` of size `M_ell`.  There are exactly `N` physical suffix tickets of
width `ell`.  Define `z_ell,m_ell,e_ell` exactly as in (7.1), with upper
colours replaced by width-`ell` tickets.  Then

\[
 m_\ell=e_\ell-(N-M_\ell)+z_\ell.                       \tag{7.4}
\]

Consequently the total strict-lower ticket leave is

\[
 \sum_{\ell<h}m_\ell
 =\sum_{\ell<h}\bigl(e_\ell-(N-M_\ell)+z_\ell\bigr).    \tag{7.5}
\]

All `e_ell` terms are inter-ring collisions, because Theorem 3.1 makes
each rank row simple inside one ring.

#### Proof

Apply the counting identity in Theorem 7.1 separately to the `N` tickets
of every fixed suffix width. \(\square\)

## 8. The exact remaining coloured-lift theorem

Form the occurrence-resolved hypergraph whose hyperedges are the
phase-appropriate antipodal rings of Theorem 2.1.  A hyperedge contains:

* its `2h` owners and `2h` roots;
* its `2h` immediate-upper occurrences;
* its `2h` nested suffix-chain tickets; and
* its oriented order-`h-1` entrance and exit states.

Theorems 2.1--3.1 prove all of the following locally and exactly:

1. every halo diamond has many candidate hyperedges;
2. every candidate is owner/root/upper simple;
3. every candidate carries simple complete central tickets;
4. every candidate is valid in either deadline phase; and
5. every candidate is biresident and exports a literal state.

The global theorem still needed is a matching/cover-down in this
hypergraph which covers each halo owner and root once, satisfies (7.3),
has only bounded ticket deficiency, and exposes a bounded `C6`-compatible
boundary tensor.  The local determinant-two obstruction contributes only
the parity bit in (5.4); Theorem 6.1 supplies its exact integral circuit.
The remaining obstruction is the nonnegative correlated cover expressed
by (7.3), together with the occurrence-labelled ticket cuts.

Consequently the uncoloured halo `2`-factor cannot simply be lifted edge by
edge: one ring realizes `2h` diamonds at once.  What the present theorem
does prove is that there is no local phase, residence, aperture, or
determinant-parity obstruction to the coloured lift.  All remaining loss is
global packet disjointness and named-target correlation.
