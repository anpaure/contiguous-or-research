# `k=17`: four-step deletion ladders and refresh slots in the fixed age-type word

Date: 2026-08-01  
Object audited: `scratch/k17_age_type_euler_word_20260801.tsv`  
Object SHA256:
`e55bea5534c80560755dbc34a1f40e5cb9e67bca23e82d72caf902d2a1fd39f8`  
Status: exact local/lag-four audit.  No existence or nonexistence of the
1430-orbit decorated cycle is claimed.

## 0. Verdict

The fixed 1430-position word contains exactly

\[
       139+297=436                                      \tag{0.1}
\]

positions with `c_0=1`.  These positions are not one-slot opportunities to
refresh an old coordinate.  The unique age-zero place is obligatorily
occupied by the coordinate newly inserted on the incoming Johnson edge.
There are therefore

\[
                         c_0-1=0                       \tag{0.2}
\]

retained-coordinate refresh slots at each such position.

This forces a four-step physical identity.  Number the owner states
cyclically and let edge `i` take `T_i` to `T_(i+1)`, deleting `alpha_i` and
inserting `beta_i`.  If position `j` has `c_0(j)=1`, then every literal age
lift must satisfy

\[
 \boxed{\quad \beta_{j-1}=\alpha_{j+3},\quad}          \tag{0.3}
\]

and this coordinate must remain present and unrefreshed through states

\[
                         T_j,T_{j+1},T_{j+2},T_{j+3}. \tag{0.4}
\]

It is inserted into `T_j`, advances successively through ages
`0,1,2,3`, and is deleted on the edge into `T_(j+4)`.  Thus the fixed type
word imposes 436 lag-four insert/delete equalities per quotient traversal.
An equivariant 17-fold physical lift contains `17*436=7412` rotated
instances of them.

Consequently, a quotient Johnson Hamilton cycle whose adjacent type pairs
have the certified counts is not yet a literal age cycle.  It must also
satisfy (0.3)--(0.4), with the appropriate quotient voltages, and the more
general refresh quotas below.  This is an exact obstruction to any proposed
candidate that violates one of these equations.

The conditional decorated-cycle reduction itself remains correct because it
explicitly asks for compatible labelled age partitions on every edge.  The
correction is to any relaxation that replaces those partitions by the type
word and adjacent owner transitions alone.

## 1. Literal transition bookkeeping

Let

\[
 T_i=C_{i,0}\mathbin{\dot\cup}C_{i,1}
          \mathbin{\dot\cup}C_{i,2}
          \mathbin{\dot\cup}C_{i,3},
 \qquad |C_{i,a}|=c_a(i),\qquad C_{i,3}=\{\alpha_i\}. \tag{1.1}
\]

Write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.               \tag{1.2}
\]

For a literal age update, the unrefreshed survivors of old age `a` are

\[
                    C_{i+1,a+1}\subseteq C_{i,a}
                    \qquad(0\le a<3).                 \tag{1.3}
\]

The retained coordinates refreshed on edge `i` form the disjoint union

\[
 \mathcal R_i
   =\mathbin{\dot\bigcup}_{a=0}^{2}
       \bigl(C_{i,a}-C_{i+1,a+1}\bigr).               \tag{1.4}
\]

The new age-zero class is exactly

\[
                  C_{i+1,0}=\{\beta_i\}
                                  \mathbin{\dot\cup}\mathcal R_i. \tag{1.5}
\]

Hence the number of refreshes drawn from old age `a` is not a free
aggregate.  It is the transition-specific integer

\[
             r_{i,a}=c_a(i)-c_{a+1}(i+1),             \tag{1.6}
\]

and

\[
       |\mathcal R_i|=\sum_{a=0}^2r_{i,a}
                     =c_0(i+1)-1.                    \tag{1.7}
\]

Equations (1.2)--(1.7), including the named physical coordinates, are the
exact refresh-slot test for one changing-owner transition.  The type
inequalities `c_(a+1)(i+1)<=c_a(i)` merely say that the three numbers in
(1.6) are nonnegative.

## 2. Exact refresh profiles of the 16 certified transitions

Use the type IDs of the fixed TSV:

```text
0=(1,5,2,1)  1=(1,6,1,1)  2=(2,5,1,1)
3=(3,3,2,1)  4=(3,4,1,1)  5=(4,3,1,1)
6=(5,1,2,1)  7=(5,2,1,1)  8=(6,1,1,1).
```

For an arc `u->v`, the table gives
`(r_0,r_1,r_2)=(c_0(u)-c_1(v),c_1(u)-c_2(v),c_2(u)-c_3(v))`.

| type arc | multiplicity | `(r_0,r_1,r_2)` | retained refreshes |
|---|---:|---:|---:|
| `0->8` | 139 | `(0,4,1)` | 5 |
| `1->6` | 127 | `(0,4,0)` | 4 |
| `1->8` | 170 | `(0,5,0)` | 5 |
| `2->8` | 8 | `(1,4,0)` | 5 |
| `3->7` | 20 | `(1,2,1)` | 4 |
| `4->3` | 20 | `(0,2,0)` | 2 |
| `5->5` | 139 | `(1,2,0)` | 3 |
| `5->8` | 1 | `(3,2,0)` | 5 |
| `6->2` | 8 | `(0,0,1)` | 1 |
| `6->7` | 119 | `(3,0,1)` | 4 |
| `7->0` | 139 | `(0,0,0)` | 0 |
| `7->7` | 98 | `(3,1,0)` | 4 |
| `8->1` | 297 | `(0,0,0)` | 0 |
| `8->4` | 20 | `(2,0,0)` | 2 |
| `8->5` | 1 | `(3,0,0)` | 3 |
| `8->8` | 124 | `(5,0,0)` | 5 |

Thus the 436 zero-refresh transitions are precisely

\[
       7\longrightarrow0\quad(139\text{ times}),
       \qquad
       8\longrightarrow1\quad(297\text{ times}).     \tag{2.1}
\]

On either transition, (1.3) is a pure shift:

\[
 C_{i+1,0}=\{\beta_i\},\qquad
 C_{i+1,1}=C_{i,0},\qquad
 C_{i+1,2}=C_{i,1},\qquad
 C_{i+1,3}=C_{i,2}.                                  \tag{2.2}
\]

The complete distribution by target `c_0` in the fixed word is

| `c_0` | positions | retained refresh slots |
|---:|---:|---:|
| 1 | 436 | 0 |
| 2 | 8 | 8 |
| 3 | 40 | 80 |
| 4 | 140 | 420 |
| 5 | 364 | 1456 |
| 6 | 442 | 2210 |

There are therefore 994 positions with at least one retained refresh slot
and

\[
                 \sum_i(c_0(i)-1)=4174               \tag{2.3}
\]

retained refresh events per quotient period.  These 4174 events are split
by old age according to the table; they are not 4174 independent choices.

## 3. The four-step deletion ladder

Apply the survivor inclusions (1.3) at three successive edges.  For every
position `j`, not only those with `c_0=1`,

\[
 C_{j+3,3}\subseteq C_{j+2,2}
             \subseteq C_{j+1,1}
             \subseteq C_{j,0}.                      \tag{3.1}
\]

The leftmost set is the singleton `C_(j+3,3)={alpha_(j+3)}`.  Hence the
coordinate deleted on edge `j+3` must have entered age zero at position
`j`:

\[
 \alpha_{j+3}\in C_{j,0}
       =\{\beta_{j-1}\}\mathbin{\dot\cup}\mathcal R_{j-1}. \tag{3.2}
\]

It must then avoid the refresh sets on edges `j,j+1,j+2`.  In physical
owner terms,

\[
       \alpha_{j+3}\in T_j\cap T_{j+1}\cap T_{j+2}\cap T_{j+3}. \tag{3.3}
\]

Equation (3.2) is the exact ladder-root/refresh-slot dichotomy:

* if `alpha_(j+3)=beta_(j-1)`, the mandatory newly inserted coordinate is
  the ladder root;
* otherwise `alpha_(j+3)` must be a retained coordinate placed in
  `mathcal R_(j-1)`, consuming one of the `c_0(j)-1` refresh slots.

The remaining refresh slots still have the age-specific quotas (1.6).
Thus (3.2) by itself is necessary but is not a substitute for the full
transition system (1.3)--(1.7).

### Corollary 3.1 (forced ladder at `c_0=1`)

If `c_0(j)=1`, then `mathcal R_(j-1)` is empty.  Both ends of (3.1) are
singletons, so all four sets in the ladder are equal:

\[
 \boxed{
 C_{j,0}=C_{j+1,1}=C_{j+2,2}=C_{j+3,3}
       =\{\beta_{j-1}\}=\{\alpha_{j+3}\}.}           \tag{3.4}
\]

This proves (0.3)--(0.4).  Equality of the endpoint labels alone is not
enough if the coordinate is deleted and reinserted at an intermediate edge;
the continuous-residence and no-refresh requirements are part of (3.4).

## 4. Quotient-voltage form of the forced equation

For a quotient owner order, let arc `i` have voltage `v_i`.  Fix cumulative
phases

\[
                    g_{i+1}=g_i+v_i\pmod {17}.        \tag{4.1}
\]

Let `alpha_i^(0),beta_i^(0)` be the deletion and insertion labels in the
source-representative gauge of quotient arc `i`.  Their labels in the lifted
walk are

\[
       \widetilde\alpha_i=\rho^{g_i}\alpha_i^{(0)},
       \qquad
       \widetilde\beta_i=\rho^{g_i}\beta_i^{(0)}.     \tag{4.2}
\]

At every one of the 436 positions `j` with `c_0(j)=1`, (3.4) becomes the
four-arc voltage equation

\[
 \boxed{
   \rho^{g_{j-1}}\beta_{j-1}^{(0)}
       =\rho^{g_{j+3}}\alpha_{j+3}^{(0)},
   \qquad
   g_{j+3}-g_{j-1}
       =v_{j-1}+v_j+v_{j+1}+v_{j+2}.}                \tag{4.3}
\]

Indices that cross the quotient cut use the total quotient voltage in the
extension of `g`; they must not be reduced modulo 1430 while forgetting the
phase shift.  Equation (4.3) is therefore a constraint on four consecutive
arc labels, not an edge-local predicate on one unlabelled quotient edge.

## 5. Meaning of the 436 singleton positions

A suffix of rank one occurs exactly when `c_0=1`.  Hence these same 436
positions are the 436 rank-one slots in the fractional age certificate.
There is only one `Z_17` orbit of singleton targets.  Any one equivariant
slot already rotates through all 17 physical singleton targets; the other
435 slots are rank-one slack.

They cannot be repurposed as retained-coordinate refresh capacity.  Their
literal source letter is the singleton

\[
                         A_j=C_{j,0}=\{\beta_{j-1}\}. \tag{5.1}
\]

Thus their two meanings are simultaneous:

1. they are redundant rank-one suffix witnesses; and
2. they are rigid no-refresh steps that force the lag-four deletion ladder.

## 6. Exact obstruction and correction

For the fixed `e55bea55...` type word, any of the following refutes a
proposed physical quotient decoration:

1. a transition cannot realize its age-specific refresh vector in Section
   2 on the already chosen labelled partition;
2. for some `j`, the future deletion `alpha_(j+3)` is neither the incoming
   insertion `beta_(j-1)` nor one of the retained refreshes at position `j`;
3. a ladder coordinate is removed or refreshed on one of its three
   survivor edges; or
4. at one of the 436 `c_0=1` positions, the voltage-labelled equality (4.3)
   fails.

These are exact candidate obstructions.  They do not, from the counts
alone, prove that every quotient owner cycle fails.

The safe finite formulation is therefore either:

* retain one labelled age partition at every owner position and enforce the
  survivor inclusions on every selected edge; or
* eliminate the partitions only by an equivalent time-expanded automaton
  carrying the three survivor cohorts, the age-specific refresh quotas, and
  all 436 lag-four equalities.

A search using only the fixed type word, aggregate type-arc counts, and
Johnson adjacency omits a necessary literal row.
