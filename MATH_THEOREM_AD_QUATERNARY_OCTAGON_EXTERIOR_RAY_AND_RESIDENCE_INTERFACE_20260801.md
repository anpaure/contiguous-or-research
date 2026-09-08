# The collared quaternary octagon has an eight-ray exterior OR interface

Date: 2026-08-01  
Lane: AD, OR-word guards for the endpoint-bearing quaternary absorber  
Status: exact local union-state and exterior-residence theorem.  This note
does not assert a common-cap compilation or preservation of intervals that
cross the nonlocally reordered donor-path fragments.

## 0. Outcome

Use the quaternary-octagon and rotating-hole notation of
`MATH_THEOREM_AD_ENDPOINT_PATH_BANK_QUATERNARY_OCTAGON_20260801.md`.
After the toggle, the collared long component is

\[
 \mathcal W_h=(A_1,V_1,V_2,\ldots,V_{h+2},V_0,B_3).    \tag{0.1}
\]

It has exactly four distinct prefix-union states, four distinct
suffix-union states, and three union values on intervals of at least three
owners.  All are independent of the collar depth `h` as an alphabet.  In
particular every one-sided exterior crossing belongs to one of eight
nested ray relations.  An interval spanning both exterior shores belongs
to one additional two-sided grid relation whose core is the total union of
the collar.

Thus the answer has two precise parts.

* **Positive structured statement.**  At every width, the long collar has
  an eight-ray plus one-grid exterior interface.  In a band of width at
  most `h+1`, the grid is geometrically impossible, leaving exactly the
  eight rays.  The complete plus packet, including its two residual
  two-owner components, has sixteen directed ray relations and three
  possible full-component grid cores.
* **Sharp limitation.**  At unrestricted width the two-sided grid can
  contain quadratically many distinct last witnesses.  Hence `O(1)` means
  `O(1)` complete ladder/grid certificates, not `O(1)` named target masks.
  No finite collection of one-sided named tickets certifies arbitrary
  exterior contexts.

At residence threshold `h+1`, the collar exports an exact boundary record.
Apart from the ordinary requirement that a short exterior run ending on a
zero at the collar boundary already be closed, the collar-specific debt is
two nested flags, one on each shore.  This closes the two exterior joins
exactly; it does not address the other joins created by a global donor-path
reordering.

## 1. Notation

Let `|S|=m-2`; let `z,a_0,a_1,a_2,a_3` be distinct outside `S`; and put

\[
\begin{aligned}
 A_i&=S\cup\{z,a_i\},
 &B_i&=S\cup\{a_i,a_{i+1}\},\\
 U_i&=S\cup\{z,a_i,a_{i+1}\}.
\end{aligned}                                           \tag{1.1}
\]

Indices on the `a_i` are modulo four.  Choose distinct
`x_0,...,x_{h-1}` in `S` and a private label `y`, and write

\[
 Z=S\cup\{a_0,a_1,z,y\},\qquad
 (z_0,\ldots,z_{h+2})=(a_1,y,z,x_0,\ldots,x_{h-1}),      \tag{1.2}
\]

\[
                         V_i=Z\setminus\{z_i,z_{i+1}\}. \tag{1.3}
\]

Then `V_1=B_0`, `V_0=A_0`, and (0.1) is precisely the long
new component of the quaternary toggle.  Define

\[
             Q=Z\cup\{a_3\},\qquad
             Q^\circ=(Z\setminus\{a_1\})\cup\{a_3\}.   \tag{1.4}
\]

The length of `W_h` is

\[
                              n=h+5.                     \tag{1.5}
\]

## 2. Exact prefix, suffix and internal decks

For a word `X`, let `P(X)`, `S(X)` and `I_>=3(X)` denote respectively its
sets of distinct nonempty prefix unions, suffix unions, and unions of
contiguous intervals having at least three owners.

### Theorem 2.1 (four--four--three normal form)

For every admissible collar depth `1<=h<=m-2` for which the displayed
private label `y` exists,

\[
 \boxed{\mathcal P(\mathcal W_h)=\{A_1,U_0,Z,Q\}},      \tag{2.1}
\]

\[
 \boxed{\mathcal S(\mathcal W_h)=\{B_3,U_3,Q^\circ,Q\}},\tag{2.2}
\]

and

\[
 \boxed{\mathcal I_{\ge3}(\mathcal W_h)
                   =\{Z,Q^\circ,Q\}}.                  \tag{2.3}
\]

The prefix and suffix sets are the following strict nested chains:

\[
 A_1\subset U_0\subset Z\subset Q,qquad
 B_3\subset U_3\subset Q^\circ\subset Q.               \tag{2.4}
\]

The internal set in (2.3) is not asserted to be a chain: `Z` and
`Q^circ` are incomparable.

#### Proof

The first two owners have union

\[
                 A_1\cup V_1=A_1\cup B_0=U_0=Z-y.      \tag{2.5}
\]

The third owner `V_2` supplies `y`, while `A_1` supplies both labels
missing from `V_2`; hence the third prefix already has union `Z`.  No
later rail owner changes it.  The final owner `B_3` supplies the new label
`a_3`, giving `Q`.  This proves (2.1).

From the other end,

\[
                    B_3\cup V_0=B_3\cup A_0=U_3.       \tag{2.6}
\]

The next rail owner is
`V_(h+2)=Z-{x_(h-1),a_1}`; together with `U_3` it gives
`Q^circ`.  The next owner supplies `a_1`, giving `Q`.  This proves (2.2),
including the case `h=1`.

Every interval of at least three owners which avoids `B_3` contains three
consecutive members of the rotating-hole rail, possibly with `A_1` in
place of its first member, and has union `Z`.  An interval of exactly three
owners ending at `B_3` has union `Q^circ`; an interval of at least four
owners ending there has union `Q`.  This proves (2.3).  Strictness follows
from the stipulated distinct labels.  \(\square\)

### Proposition 2.2 (local old-deck dominance)

Treat the old collared cycle and the three other selected old octagon
atoms as separate local components.  The union deck of these local
components is contained in the union deck of the three new components

\[
 \mathcal W_h,\qquad (A_2,B_1),\qquad (A_3,B_2).        \tag{2.7}
\]

#### Proof

The old cycle's single-owner values are retained.  Its edge unions are
the return-rail colours together with `U_0`; all return edges remain and
`U_0=A_1\cup B_0` occurs at the left end of `W_h`.  Every cyclic old
interval of at least three owners has union `Z`, which occurs in (2.3).
The old isolated edge values `U_1,U_2,U_3` occur respectively on
`A_2B_1`, `A_3B_2`, and the right-end edge `A_0B_3` of `W_h`.
\(\square\)

The word **local** is essential.  In the absorber theorem the three old
path atoms can have long donor fragments between them, and the toggle
permutes two of those fragments.  Proposition 2.2 does not certify old
intervals crossing those donor fragments.

## 3. Exact exterior crossing interface

Let a left exterior word `L` end immediately before `A_1`, and let a right
exterior word `R` begin immediately after `B_3`.  Write `Sigma_u` for the
union of the last `u` owners of `L`, and `Pi_v` for the union of the first
`v` owners of `R`.

### Theorem 3.1 (eight rays and one grid)

Every interval of `L W_h R` which meets both `W_h` and an exterior shore
has one of the following values:

\[
\begin{array}{c|c}
\text{geometry}&\text{union value}\\ \hline
\text{enters from the left only}
 &\Sigma_u\cup P,\quad P\in\{A_1,U_0,Z,Q\},\\
\text{exits to the right only}
 &S\cup\Pi_v,\quad S\in\{B_3,U_3,Q^\circ,Q\},\\
\text{spans both shores}
 &\Sigma_u\cup Q\cup\Pi_v.
\end{array}                                             \tag{3.1}
\]

Hence the complete one-sided state consists of eight nested ray families,
independent of `h`.  The two-sided state is one grid relation with fixed
core `Q`.

If intervals have at most `D+1` owners, a two-sided interval exists only
when

\[
                     u+v+n\le D+1.                      \tag{3.2}
\]

Put `R_0=D+1-n`.  When both exteriors are long enough, the number of
positive grid addresses is

\[
       0\quad(R_0\le1),\qquad
       {R_0(R_0-1)\over2}\quad(R_0\ge2).                \tag{3.3}
\]

In particular, if `D<=h`, then `n=h+5>D+1`, so the two-sided grid is
absent.

#### Proof

An interval entering only from the left is a suffix of `L` followed by a
prefix of `W_h`; apply (2.1).  The right case uses (2.2).  An interval
meeting both shores contains all of `W_h`, whose total union is `Q`.
This proves (3.1).  Its length gives (3.2).  Positive integer pairs
`u,v` with `u+v<=R_0` are counted by (3.3).  \(\square\)

### Corollary 3.2 (sixteen-ray full plus packet)

The other two new components have directed decks

\[
\begin{array}{c|c|c|c}
\text{component}&\text{prefix states}&\text{suffix states}&\text{total}\\
\hline
(A_2,B_1)&\{A_2,U_1\}&\{B_1,U_1\}&U_1,\\
(A_3,B_2)&\{A_3,U_2\}&\{B_2,U_2\}&U_2.
\end{array}                                             \tag{3.4}
\]

Thus the full plus packet, with all three components exposed, has sixteen
directed one-sided ray relations and three full-component cores
`Q,U_1,U_2`.  Reversing any component exchanges its prefix and suffix
decks and introduces no new state.

### Corollary 3.3 (bounded structured ticket theorem)

For a prepared gluing in which `W_h` is one contiguous word fragment, it
is sufficient to certify:

1. every target in each of the eight ray relations in (3.1) by a complete
   ladder certificate or an unaffected duplicate;
2. every target in the full-span grid by one complete grid certificate or
   an unaffected duplicate; and
3. the internal local deck, which is already explicit in Theorem 2.1.

Then every interval target meeting this collared fragment is certified at
every width.  For the full three-component packet, use the sixteen rays
and the corresponding fixed-layout grids.

This is a finite **relation-type** theorem.  It is not a finite
targetwise-ticket theorem.

### Proposition 3.4 (the grid has unbounded nested-ray width)

Assume the ground set has size `2m`, so `|Q|=m+3`.  For every integer
`r>=1` satisfying `2r<=m-3`, there are literal rank-`m` Johnson exterior
paths for which the full-span grid contains the product family

\[
 Q\cup\{v_1,\ldots,v_i\}\cup\{w_1,\ldots,w_j\},
                 \qquad 0\le i,j\le r.                 \tag{3.5}
\]

The `(r+1)^2` masks are distinct, and every cover of this family by nested
inclusion chains needs at least `r+1` chains.  Consequently an
arbitrary-width certificate by `O(1)` nested rays, or by `O(1)` named
masks, is false in general.

#### Proof

Choose the two disjoint banks outside `Q`, possible because the complement
of `Q` has size `m-3`.  Fix any `s in S` and put

\[
 T=(A_1-\{s\})\cup\{a_0\},\qquad
 T'=(B_3-\{s\})\cup\{z\}.                              \tag{3.6}
\]

These are rank-`m` subsets of `Q`, with `T` Johnson-adjacent to `A_1` and
`T'` Johnson-adjacent to `B_3`.  Choose distinct removable labels
`u_1,...,u_r` in `T` and `u'_1,...,u'_r` in `T'`.  The sequences

\[
 T_i=(T-\{u_1,\ldots,u_i\})\cup\{v_1,\ldots,v_i\},
\quad
 T'_j=(T'-\{u'_1,\ldots,u'_j\})\cup\{w_1,\ldots,w_j\}
                                                               \tag{3.7}
\]

are simple Johnson paths.  Use `(T_r,...,T_0)` as the left exterior ending
at `A_1`, and `(T'_0,...,T'_r)` as the right exterior beginning at `B_3`.
The two extra endpoint adjacencies are literal by (3.6).  After union with
the intervening total state `Q`, their suffix/prefix unions are exactly
(3.5).

The masks with `i+j=r` are pairwise incomparable.  A nested ray contains
at most one member of this antichain, so at least `r+1` rays are necessary.
\(\square\)

## 4. The full nonlocal donor-path reordering has an additional grid

The topology theorem writes the old donor path as

\[
 P_0,o_1,P_1,o_3,P_2,o_2,P_3,                           \tag{4.1}
\]

where

\[
\begin{aligned}
P_0&:\operatorname{src}\Longrightarrow A_1,&
P_1&:B_1\Longrightarrow A_3,\\
P_2&:B_3\Longrightarrow A_2,&
P_3&:B_2\Longrightarrow\operatorname{snk}.
\end{aligned}                                           \tag{4.2}
\]

After the octagon toggle, the order is

\[
 P_0,n_1,\mathcal R,n_0,P_2,n_2,P_1,n_3,P_3.            \tag{4.3}
\]

Thus `P_1` and `P_2` exchange order.  This is not a one-fragment
replacement, and Theorem 3.1 does not by itself certify it.

### Theorem 4.1 (donor-swap grid is an independent guard)

The old chronology contains the two-sided grid

\[
 \mathcal G^-
  =\{\Sigma_u(P_1)\cup\Pi_v(P_2):u,v\ge1\},             \tag{4.4}
\]

where the selected suffixes end at `A_3` and prefixes begin at `B_3`.
The corresponding new adjacency has the reversed grid

\[
 \mathcal G^+
  =\{\Sigma_u(P_2)\cup\Pi_v(P_1):u,v\ge1\}.             \tag{4.5}
\]

Neither the **local octagon** four-resource identity nor the eight collar
rays implies

\[
                         \mathcal G^-\subseteq
                         \operatorname{Cov}(\text{new word}).           \tag{4.6}
\]

Indeed, for every fixed positive `r,s` and all sufficiently large ambient
ranks there are literal rolling Johnson donor fragments for which `G^-`
has `rs` distinct values that do not occur in the new word.

On a `2m`-point ground set the construction below is available under the
explicit sufficient inequality

\[
                              r+s\le m-4,                \tag{4.7}
\]

because `Omega-Q` has size `m-3` and one of its labels is the already
reserved `a_2`.

#### Proof

The identities (4.4)--(4.5) follow directly from the two orders
(4.1),(4.3).  To see independence, choose disjoint private banks
`ell_1,...,ell_r` and `r_1,...,r_s` outside `Q union {a_2}`; (4.7) gives
them.  For `P_1`, start at `B_1`, replace `a_1` by `ell_1`, and for
`2<=i<=r` replace a distinct temporary label `p_i in S` by `ell_i`.
At the turning step replace `a_2` by `z`; then remove
`ell_r,...,ell_2` while restoring `p_r,...,p_2`, and finally replace
`ell_1` by `a_3`.  This is a simple Johnson path from `B_1` to `A_3`:
all pre-turn owners omit `z`, all post-turn owners contain `z`, and each
half is strictly monotone in its private bank.  Its post-turn suffixes
expose a nested `ell` bank while omitting `a_1`.

For `P_2`, perform the analogous construction from `B_3` to `A_2`:
replace `a_3` by `r_1`, introduce `r_2,...,r_s` using temporary labels
of `S`, replace `a_0` by `z` at the turn, restore the temporary labels,
and finally replace `r_1` by `a_2`.  Its pre-turn prefixes expose the
nested `r` bank and every owner omits `a_1`.  The private banks separate
the two paths from the collar and from each other.

Every selected old crossing target then omits `a_1` and is distinguished
by its pair of private-bank prefixes.  In the new chronology, an interval
containing a private label from each bank must cross from `P_2` through
the owner `B_1` into `P_1`.  Since `a_1 in B_1`, every such new interval
contains `a_1`, and therefore cannot equal an old selected target.  An
interval not spanning both donor fragments misses one of the two private
banks.  The collar contains neither bank.  Thus all `rs` targets are absent
from the new word.  \(\square\)

### Corollary 4.2 (sharp global boundary)

Absent an additional theorem exploiting correlations in the ambient exact
factor, a sound one-cycle/one-path absorber interface must contain both:

1. the constant collar state from Theorem 3.1; and
2. a complete certificate for the donor-swap grid (4.4), or unaffected
   duplicate witnesses for every target in that grid.

Consequently the local collar identity alone gives no `O(1)` nested-ray
theorem for the full nonlocal topology.  There is still an `O(1)` **relation-type**
description—one extra grid—but its occurrence-labelled content can grow
quadratically with the donor-fragment lengths.

The rolling-fan construction proves this local logical independence.  It
is not asserted to be a globally lower/upper-rainbow four-resource factor.
Whether the fixed-`H` exact-factor extension forces repayment of the donor
grid is a separate, still-open correlation question.

## 5. Exact residence state at the two exterior joins

Put

\[
                         K=S\setminus\{x_0,\ldots,x_{h-1}\}. \tag{5.1}
\]

For a coordinate `c`, let `lambda(c)` and `rho(c)` be its leading and
trailing positive-run lengths in `W_h`, with a separate `whole` flag when
it occurs throughout the fragment.  The exact nonzero boundary record is

\[
\begin{array}{c|c|c}
c&\lambda(c)&\rho(c)\\ \hline
K&\text{whole}&\text{whole}\\
a_1&h+2&0\\
z&1&0\\
x_j&j+2&h+1-j\\
a_0&0&h+4\\
a_3&0&1.
\end{array}                                             \tag{5.2}
\]

The coordinate `y` has one internal positive run of length exactly
`h+1`; `z` has a second, internal run of length exactly `h+1`; every other
internal positive run has length at least `h+1`.

Let `tau_L(c)` be the trailing positive-run length of `c` in the left
exterior and `pi_R(c)` its leading positive-run length in the right
exterior.  A boundary run which reaches a global word endpoint is regarded
as clipped and automatically legal.

### Theorem 5.1 (two nested residence flags)

Assume the two exteriors are internally resident at threshold `h+1` and
satisfy the ordinary off-end cleanliness conditions

\[
\begin{aligned}
 c\notin A_1&\Longrightarrow
   \tau_L(c)=0\ \text{or}\ \tau_L(c)\ge h+1
   \quad\text{unless globally clipped},\\
 c\notin B_3&\Longrightarrow
   \pi_R(c)=0\ \text{or}\ \pi_R(c)\ge h+1
   \quad\text{unless globally clipped}.
\end{aligned}                                           \tag{5.3}
\]

Then `L W_h R` is resident across both joins if and only if

\[
\begin{aligned}
 \tau_L(z)&\ge h,&
 \tau_L(x_j)&\ge h-j-1 &&(0\le j<h),\\
 \pi_R(a_3)&\ge h,&
 \pi_R(x_j)&\ge j &&(0\le j<h).                       \tag{5.4}
\end{aligned}
\]

with the same global-clipping convention and vacuous zero right-hand
sides.

Equivalently, reading exterior owners away from the join, the required
label sets are the two nested flags

\[
 \Lambda_t=\{z\}\cup\{x_0,\ldots,x_{h-t-1}\},
 \qquad 1\le t\le h,                                   \tag{5.5}
\]

on the left, and

\[
 P_t=\{a_3\}\cup\{x_t,\ldots,x_{h-1}\},
 \qquad 1\le t\le h,                                   \tag{5.6}
\]

on the right.  Empty indexed ranges are omitted.

#### Proof

Table (5.2) follows directly from the two consecutive missing positions
of every rotating-hole label.  The only short positive run beginning at
the left boundary is the singleton `z` run or the length-`j+2` run of
`x_j`; merging with the exterior gives exactly the first line of (5.4).
The only short positive run ending at the right boundary is the singleton
`a_3` run or the length-`h+1-j` run of `x_j`; this gives the second line.
Every coordinate absent at a collar endpoint is handled exactly by (5.3),
and all remaining runs in (5.2), including whole-fragment runs, are already
long enough.  This proves necessity and sufficiency.

The inequalities in (5.4) say precisely that the owner at exterior
distance `t` contains (5.5) or (5.6), proving the flag form.  \(\square\)

The two flags are `O(1)` **nested families**, not `O(1)` labels: their
union contains the `h` rotating labels.  Without (5.3), no collar-only
residence theorem is possible, because an arbitrary number of coordinates
absent from `A_1` or `B_3` may arrive in short clipped exterior runs and
become internal at the join.

## 6. Exact scope

The proved interface closes the OR-state and residence rows for one
prepared contiguous long component:

\[
 \boxed{8\text{ one-sided rays}+1\text{ two-sided grid}
        +2\text{ nested residence flags}.}              \tag{6.1}
\]

It does **not** prove any of the following.

1. The actual quaternary topology reorders two donor-path fragments.  Old
   intervals crossing those fragments require their own ladder/grid
   certificates; local deck dominance does not supply them.
2. If the two short new components are separately inserted into a word,
   their exterior residence records must also be checked.
3. No common-cap or lower compiler is constructed here.
4. A relation-type certificate may contain linearly or quadratically many
   occurrence-labelled targets; it is not one named ticket.

Thus the rotating-hole depth creates no growing upper-state alphabet, but
arbitrary-width two-sided chronology and global donor-fragment reordering
remain real guards.

## 7. Replay

Run

```text
python3 scratch/audit_ad_quaternary_octagon_exterior_ray_interface_20260801.py
```

The dependency-free replay checks `1<=h<=12`: the exact four prefix and
four suffix states, the three higher internal states, local old-deck
dominance, every internal residence run, and both nested boundary flags.
It reports

```text
PASS_AD_QUATERNARY_OCTAGON_EXTERIOR_RAY_INTERFACE
payload_sha256=6817533dd2e588eb1bf1108e0b8229153277bf936d01c6ad89f12255d2359934
```

The independent adversarial audit
`MATH_AUDIT_AD_QUATERNARY_OCTAGON_EXTERIOR_GUARD_COUNTEREXAMPLE_20260801.md`
rechecks the interface, proves the product-poset ray lower bound, and gives
a literal sixteen-owner lost-mask fixture.  Its companion replay is
`scratch/audit_ad_quaternary_octagon_exterior_guard_counterexample_20260801.py`.
