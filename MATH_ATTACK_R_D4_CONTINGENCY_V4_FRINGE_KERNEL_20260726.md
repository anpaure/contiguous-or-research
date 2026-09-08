# Lane R: sharp four-cell contingency and the strict-\(D_4\) fringe kernel

Date: 2026-07-26

Method: pure mathematics only; no search, computation, solver, or web use.

## 0. Exact outcome

There are three logically distinct statements.

1. The abstract two-partition discrepancy problem is completely solved,
   with a stronger constant-order error.  If the two partition block loads
   are at most \(B\), literal integral block bits give

   \[
     \boxed{\left|N_{ab}-{d\over4}\right|\le {3B\over4}}
     \qquad(a,b\in\{0,1\}).                         \tag{0.1}
   \]

   The constant \(3/4\) is optimal, even for arbitrarily many blocks.
   Exceptional mass \(R\) adds at most \(3R/4\) to the upper deviation.

2. The full canonical two-endpoint preload is

   \[
     \boxed{M_s=C_s+2C_{s-1}+C_{s-2}=\rho_sC_s,}
     \qquad
     \rho_s={5s(5s-7)\over4(2s-1)(2s-3)}
             \longrightarrow {25\over16}.            \tag{0.2}
   \]

   Hence four cap-\(p\) cells are statewise possible only if, with
   \(\theta=C_s/p\),

   \[
     \boxed{
     \theta\le\theta_{4,s}:={4\over\rho_s}
       ={16(2s-1)(2s-3)\over5s(5s-7)}
       \longrightarrow {64\over25}.}                 \tag{0.3}
   \]

   This mass condition is not sufficient for the canonical coordinate
   implementation.  The two endpoint coordinate swaps have one Klein-four
   ownership component containing the four root families of sizes

   \[
                         (C_s,C_{s-1},C_{s-1},C_{s-2}). \tag{0.4}
   \]

   A legal coordinate shore merely permutes (0.4), so one cell retains
   load \(C_s\).  Thus the coordinate library fails whenever \(C_s>p\),
   even below (0.3).

3. Two dense, simultaneously legal, raw \(D_4\) fringe partitions with
   fourteen-row blocks can be constructed outside an exponentially small
   set.  They still do not instantiate (0.1).  Every strict fringe packet
   fixes both complementary local ports, while the protected endpoint
   window contains both ports.  Its local intersection is therefore empty,
   before and after the substitution.  Consequently

   \[
     \boxed{\text{every strict }D_4\text{ fringe state has zero action on
     the protected two-endpoint cell, occurrence by occurrence}.}       \tag{0.5}
   \]

   The raw no-fringe exception is exponentially small, but the exception
   to **useful endpoint action** is all of \(M_s\).  Combining strict
   non-coordinate fringe states with the coordinate Klein-four shores still
   leaves maximum cell load at least \(C_s\).

The dense strict-fringe route is therefore closed.  The only surviving
local route is a boundary-active parent atom.  The full
\(H_4\)-conjugated canonical/noncanonical \(D_4\) library contains a real
eight-target coupled endpoint seed on a marked port, but it does not cover
all fourteen ports: one two-root orbit is completely frozen, and no dense
parent-aligned atlas or cross-context residual-capacity theorem is proved.

## 1. The sharp two-partition theorem

Let \((\Omega,\mu)\) be a finite weighted occurrence set, with total mass

\[
                              d=\mu(\Omega).           \tag{1.1}
\]

Let \(\mathcal P,\mathcal Q\) be two partitions of \(\Omega\), and put

\[
 \Delta_P=\max_{P\in\mathcal P}\mu(P),\qquad
 \Delta_Q=\max_{Q\in\mathcal Q}\mu(Q).               \tag{1.2}
\]

Choose one bit \(x_P\in\{0,1\}\) for every \(P\)-block and one bit
\(y_Q\in\{0,1\}\) for every \(Q\)-block.  Let \(N_{ab}\) be the mass of
occurrences whose two block bits are \((a,b)\).

### Theorem 1.1 (sharp bounded-block four-cell contingency)

There are integral block bits for which, simultaneously for all four
cells,

\[
 \boxed{
 \left|N_{ab}-{d\over4}\right|
 \le \Gamma(\Delta_P,\Delta_Q)
 :=\min\left\{{\Delta_P\over4}+{\Delta_Q\over2},
              {\Delta_Q\over4}+{\Delta_P\over2}\right\}.}             \tag{1.3}
\]

Equivalently,

\[
 \Gamma(\Delta_P,\Delta_Q)
 ={\max(\Delta_P,\Delta_Q)\over4}
  +{\min(\Delta_P,\Delta_Q)\over2}.                  \tag{1.4}
\]

In particular, if both block loads are at most \(B\), then

\[
 \boxed{
 \left|N_{ab}-{d\over4}\right|\le{3B\over4}
       \le {3\over4}\sqrt{Bd}.}                      \tag{1.5}
\]

Thus (1.5) proves the requested \(O(\sqrt{Bd})\) statement and is much
stronger when \(d/B\to\infty\).

### Lemma 1.2 (two-dimensional half-rounding)

If \(v_1,\ldots,v_n\in\mathbb R_{\ge0}^2\) and
\(\|v_i\|_1\le D\), then some \(\epsilon_i\in\{0,1\}\) satisfy

\[
 \left\|\sum_i\left(\epsilon_i-\frac12\right)v_i
 \right\|_\infty\le{D\over2}.                       \tag{1.6}
\]

#### Proof

The polytope

\[
 \mathcal K=\left\{z\in[0,1]^n:
      \sum_i z_iv_i={1\over2}\sum_i v_i\right\}      \tag{1.7}
\]

contains \(z_i=1/2\).  At an extreme point of \(\mathcal K\), at most two
coordinates are fractional; otherwise a nonzero perturbation supported on
the fractional coordinates would preserve the two vector equations.

Keep all integral coordinates.  It remains to round
\(p=\alpha u+\beta v\), where \(u,v\ge0\) and
\(\|u\|_1,\|v\|_1\le D\), to one of \(0,u,v,u+v\).  Scale to \(D=1\).
If \(\alpha+\beta\le1\) and \(\|p\|_\infty\le1/2\), choose \(0\).  Otherwise
suppose, by symmetry, \(p_1>1/2\).  If a vector \(t\in\{u,v\}\) is farther
than \(1/2\) from \(p\) in \(\ell_\infty\), then either its first
coordinate is below \(p_1\), or

\[
 t_2>p_2+\frac12,\qquad
 t_1\le1-t_2<\frac12-p_2<p_1.                         \tag{1.8}
\]

If neither \(u\) nor \(v\) were within \(1/2\), then
\(u_1,v_1<p_1\), contradicting
\(p_1=\alpha u_1+\beta v_1\) and \(\alpha+\beta\le1\).
For \(\alpha+\beta\ge1\), apply the first case to
\((1-\alpha)u+(1-\beta)v\) and complement the chosen subset of
\(\{u,v\}\).  Rescaling proves (1.6). \(\square\)

#### Proof of Theorem 1.1

Order the \(\mathcal P\)-blocks arbitrarily and stop when their cumulative
mass first crosses \(d/2\).  One of the two adjacent partial sums is within
\(\Delta_P/2\) of \(d/2\).  Give those blocks bit one.  If their total mass
is \(A\), then

\[
                         \left|A-{d\over2}\right|
                         \le{\Delta_P\over2}.          \tag{1.9}
\]

For each \(Q\in\mathcal Q\), let

\[
 v_Q=(a_Q,b_Q),                                        \tag{1.10}
\]

where \(a_Q\) and \(b_Q\) are the masses of \(Q\) incident respectively
with the selected and unselected \(\mathcal P\)-blocks.  Then
\(a_Q+b_Q=\mu(Q)\le\Delta_Q\).  Lemma 1.2 chooses the \(Q\)-blocks of bit
one so that

\[
 N_{11}={A\over2}+\delta_+,\qquad
 N_{01}={d-A\over2}+\delta_-,\qquad
 |\delta_\pm|\le{\Delta_Q\over2}.                     \tag{1.11}
\]

The other two cells have the opposite errors.  Equations (1.9)--(1.11)
give deviation at most \(\Delta_P/4+\Delta_Q/2\).  Reversing the roles of
the partitions gives the other term in (1.3). \(\square\)

### Proposition 1.3 (optimality)

The constant \(3/4\) in (1.5) cannot be reduced.  Take
\(4k+1\) common blocks for \(\mathcal P=\mathcal Q\), each of mass \(B\).
Every block is indivisible and lies in one joint cell, so some cell contains
at least \((k+1)B\), whereas \(d/4=(k+1/4)B\).  Its deviation is
\(3B/4\). \(\square\)

## 2. Exceptions, integer caps, and fixed background

Suppose a set of mass \(R\) is removed before the block bounds are verified.
Apply Theorem 1.1 to mass \(d-R\), then allow the exceptions to land
adversarially.  One obtains

\[
 \boxed{
 {d\over4}-\Gamma-{R\over4}
 \le N_{ab}\le
 {d\over4}+\Gamma+{3R\over4}.}                       \tag{2.1}
\]

For equal block cap \(B\) and integer masses,

\[
                     N_{ab}
 \le\left\lfloor{d+3B+3R\over4}\right\rfloor.       \tag{2.2}
\]

Thus the exact uniform sufficient condition for integer cell cap \(p\) is

\[
                     \boxed{4p-d\ge3B+3R-3.}          \tag{2.3}
\]

The constants in (2.1)--(2.3) are jointly sharp by putting one common block
of mass \(B\) and all exceptional mass \(R\) in the same cell.

Now let fixed, choice-independent background loads be \(b_{ab}\), with
total \(F=\sum b_{ab}\).  Put

\[
             \beta_+=\max_{a,b}\left(b_{ab}-{F\over4}\right).          \tag{2.4}
\]

If the controllable mass is \(d\), then

\[
 \boxed{
 \max_{a,b}(b_{ab}+N_{ab})
 \le {d+F\over4}+\Gamma+{3R\over4}+\beta_+.}         \tag{2.5}
\]

Equivalently, one may use the literal residual capacities

\[
                         c_{ab}=(p-b_{ab})_+.          \tag{2.6}
\]

Balancing the marked fibre alone proves nothing unless either all
canonical collars are included in \(d\), or their imbalance is charged in
\(\beta_+\).  In particular the mass
\(2C_{s-1}+C_{s-2}=\Theta(C_s)\) is not exceptional.

## 3. The exact canonical preload and cell thresholds

The four two-endpoint root types have multiplicities

\[
                         C_s,quad C_{s-1},quad
                         C_{s-1},quad C_{s-2}.         \tag{3.1}
\]

Their total is \(M_s\) in (0.2).  The exact ratios

\[
 {C_{s-1}\over C_s}={s+1\over2(2s-1)},
 \qquad
 {C_{s-2}\over C_s}={s(s+1)\over4(2s-1)(2s-3)}        \tag{3.2}
\]

give the displayed value of \(\rho_s\).

Even after hypothetical complete fragmentation, four zero-background
cells require \(M_s\le4p\), which is (0.3).  If a future useful
four-cell packet system really has \(B=14\), useful exceptional mass \(R\),
and no other background imbalance, Theorem 1.1 gives the exact sufficient
condition

\[
                         \boxed{4p-M_s\ge39+3R.}       \tag{3.3}
\]

With fixed background, add \(4\beta_+\) to the right side.  Thus even a
valid bounded packet system needs quantitative slack below (0.3); the
mass boundary itself leaves no discrepancy room.

For more than four cells, the zero-background scalar minimum is

\[
                   \boxed{L_s(\theta)=lceil\rho_s\theta\rceil.}         \tag{3.4}
\]

Put \(\theta_j(s)=j/\rho_s\).  In the minimal Catalan-scale interval,

\[
\begin{array}{c|c}
\theta_4(s)<\theta\le\theta_5(s)&5\text{ cells},\\
\theta_5(s)<\theta\le\theta_6(s)&6\text{ cells},\\
\theta_6(s)<\theta<C_s/C_{s-1}&7\text{ cells}.
\end{array}                                             \tag{3.5}
\]

The limiting thresholds are

\[
               \theta_4\to{64\over25},\qquad
               \theta_5\to{16\over5},\qquad
               \theta_6\to{96\over25}.               \tag{3.6}
\]

Moreover \(M_s<7p\) throughout the minimal-scale interval.  Indeed

\[
 7-\rho_s{C_s\over C_{s-1}}
 ={3s^2+21s-42\over2(2s-3)(s+1)}>0
 \qquad(s\ge2).                                       \tag{3.7}
\]

These cell counts ignore any additional background; with background the
correct necessary condition is \(M_s\le\sum_T(p-\beta_T)_+\).

## 4. Why the coordinate partitions do not satisfy Theorem 1.1

Inside the size-\((s+1)\) parent, the four no-interior-return root families
may be written

\[
\begin{aligned}
 \mathcal B_s={}&\{1u0:u\in\mathcal D_s\}
 \mathbin{\dot\cup}\{10\,1v0:v\in\mathcal D_{s-1}\}\\
 &\mathbin{\dot\cup}\{1v0\,10:v\in\mathcal D_{s-1}\}
 \mathbin{\dot\cup}\{10\,1w0\,10:w\in\mathcal D_{s-2}\}.
                                                               \tag{4.1}
\end{aligned}
\]

The left and right endpoint coordinate swaps commute.  Their one-ended
ownership relations join the first family respectively to the second and
third; applying both joins to the fourth.  They preserve every interior
return cut, so (4.1) is exactly one component of the four-factor overlay.

The four shores are coordinate images of one another.  On the distinguished
two-endpoint target they only permute the multiplicity vector (3.1).
Therefore

\[
 \boxed{
 \min_{\text{legal coordinate shores}}
       \max_{a,b}\mu(T_{ab})\ge C_s.}                 \tag{4.2}
\]

The abstract theorem assumes one independently selectable bit for every
block of each partition.  Here the join of the two purported partitions
has fused the complete preload component; selecting a shore is one global
permutation, not two block signings.  Thus Theorem 1.1 is inapplicable,
even when \(M_s\le4p\).

## 5. Two dense raw fringe partitions

Let \(N_4(T)\) be the number of size-four fringe subtrees of an ordered
binary tree \(T\), and define

\[
                 \mathcal T(z,u)=\sum_Tz^{|T|}u^{N_4(T)}.              \tag{5.1}
\]

Root decomposition gives the exact identity

\[
                 \boxed{\mathcal T=1+z\mathcal T^2
                         +14(u-1)z^4.}                 \tag{5.2}
\]

Indeed \(1+z\mathcal T^2\) propagates all fringe occurrences in the two
children, while the fourteen total-size-four trees acquire one additional
root occurrence.

Put \(A_0=[u^0]\mathcal T\) and \(A_1=[u^1]\mathcal T\).  Then

\[
 A_0={1-\sqrt{1-4z+56z^5}\over2z},
 \qquad
 A_1={14z^4\over\sqrt{1-4z+56z^5}}.                  \tag{5.3}
\]

Let

\[
                 e_t=[z^t](A_0+A_1)                  \tag{5.4}
\]

be the number of size-\(t\) trees with fewer than two size-four fringe
roots.  The discriminant in (5.3) is positive at \(z=1/4\), where it is
\(7/128\), and is decreasing but positive on \([0,1/4]\).  Since the
coefficients are nonnegative, Pringsheim's theorem implies that both
series have radius strictly larger than \(1/4\).  Hence, for some
\(\lambda<1\),

\[
                         {e_t\over C_t}=O(t^{3/2}\lambda^t).             \tag{5.5}
\]

For a tree not counted by \(e_t\), choose its first and last size-four
fringe roots in preorder.  They are distinct and cannot be nested, hence
their subtrees are disjoint.  Replacing either selected filling by any of
the fourteen size-four trees leaves the complete set and order of
size-four fringe roots unchanged: the selected root remains size four,
has no proper size-four descendant, and all outside subtree sizes are
unchanged.

Consequently the nonexceptional trees have two exact partitions:

* a left partition obtained by varying the first filling and fixing all
  other data;
* a right partition obtained by varying the last filling and fixing all
  other data.

Every block has exactly fourteen trees.  A left and right block meet in at
most one tree.

### Theorem 5.1 (raw exact-factor product legality)

Replace the canonical local factor at every selected first or last fringe
hole by either the canonical \(D_4\) factor or the certified non-coordinate
\(D_4\) factor.  Arbitrary left-block and right-block states compose to one
literal integral exact factor.

#### Proof

Each local state is a complete fourteen-row complement-path factor: it
enumerates every local \(X\)-state and every adjacent-union \(Y\)-colour
once, and fixes each root/complement port pair.  Hence its substitution has
zero discrepancy in both exact ownership ledgers.

Different blocks within one partition have disjoint row support.  On a row
which receives both choices, the first and last holes are disjoint aligned
subtrees and therefore occupy disjoint open phase slabs.  Each replacement
fixes its slab endpoints.  The two replacements commute, their complete
\(X/Y\) discrepancies add to zero, and the resulting row is still a literal
complement geodesic.  Summing over all blocks proves exactness. \(\square\)

Applied to the four disjoint parent-root families in (4.1), the raw
exceptional occurrence mass is

\[
                         R_s^{\rm raw}
                   =e_s+2e_{s-1}+e_{s-2}
                   =e^{-\Omega(s)}M_s,                \tag{5.6}
\]

and both raw partitions have block size \(B=14\).  This statement uses the
explicit disjoint parent-root realization (4.1).  In any alternative lift
where one physical packet variable is shared by several occurrence tags,
the relevant \(B\) is its aggregate tag load, not fourteen automatically.

## 6. The decisive endpoint-profile kernel

Raw exactness does not make the two fringe states endpoint bits.

Let \(J\) be the eight-coordinate ground set of one packet.  Every local
factor state, canonical or noncanonical, has complementary row ports

\[
                         X_0=P,\qquad X_4=J\setminus P.                 \tag{6.1}
\]

### Lemma 6.1 (swallowed port-factor invariant)

Let a protected intersection window contain the entire local packet slab,
including both states in (6.1).  If \(O\) is its intersection outside
\(J\), then for every exact local port factor \(H\),

\[
                              T_H(W)=O.                \tag{6.2}
\]

The complementary upper target is fixed as well.

#### Proof

The local part of the lower intersection is contained in

\[
                         P\cap(J\setminus P)=\varnothing.              \tag{6.3}
\]

Thus only \(O\) remains.  Dually, the local union contains all of \(J\),
so its complementary contribution is fixed. \(\square\)

For \(s\ge7\), every selected size-four fringe in the central fillings of
(4.1) is proper and lies strictly inside the serviced endpoint window.
Lemma 6.1 applies occurrence by occurrence, regardless of which exact
\(D_4\) factor state or \(H_4\)-conjugate is used.

### Theorem 6.2 (strict-fringe cell indivisibility)

Every factor generated by all raw choices in Theorem 5.1 has the same
protected four-cell vector

\[
                         (C_s,C_{s-1},C_{s-1},C_{s-2}).                 \tag{6.4}
\]

Adding arbitrary coordinate Klein-four shore choices only permutes this
vector.  Hence

\[
 \boxed{
 \min_{\substack{\text{coordinate shores, strict }D_4/H_4\\
                  \text{fringe states}}}
       \max_{a,b}\mu(T_{ab})\ge C_s.}                 \tag{6.5}
\]

#### Proof

The outer root form in (4.1) determines the Boolean cell.  All fringe
states lie strictly in its variable filling and are invisible by Lemma
6.1, so they fix the physical target, including its exterior carrier.
Coordinate shores only rename the four targets. \(\square\)

This identifies the parameter error in applying Theorem 1.1.  For raw
factor packetization, \(B=14\) and \(R=R_s^{\rm raw}\) are correct.  For
**useful endpoint signing**, the supported active set is empty, so the
effective exception is

\[
                              \boxed{R_s^{\rm useful}=M_s.}             \tag{6.6}
\]

The exponentially small raw exception cannot be substituted for (6.6).
This closes the proposed dense strict-fringe realization even throughout
the nominally feasible range \(\theta\le\theta_{4,s}\).

The argument applies to every state in the complete exact local port
fibre.  Merely adding more internal \(D_4\) factors cannot escape; a changed
slab must meet an endpoint of the serviced window.

## 7. Boundary-active \(D_4/H_4\) seeds and their limitation

Let \(F\) be the canonical \(D_4\) factor, \(G\) the certified
non-coordinate factor, and

\[
                         H_4=\langle(2\ 3),(4\ 5),(6\ 7)\rangle.       \tag{7.1}
\]

For \(H\in\{F,G\}\), write the two endpoint tokens of its coordinate word
at port \(P\) as

\[
                         e_H(P)=(a_4^H(P),b_1^H(P)).   \tag{7.2}
\]

After coordinate conjugation and reanchoring at the same port,

\[
                         e_{hH}(P)=h\,e_H(h^{-1}P).    \tag{7.3}
\]

Literal substitution in the two certified coordinate-word tables gives
the following complete orbit-representative palettes:

\[
\begin{array}{c|c|c|c|c}
P&|H_4P|&\{a_4\}&\{b_1\}&\#\{(a_4,b_1)\}\\ \hline
1234&2&\{1\}&\{8\}&1\\
1236&2&\{1,6\}&\{7,8\}&2\\
1245&2&\{1,2,4,5\}&\{3,6,7,8\}&8\\
1246&8&\{1,2,4,6\}&\{3,5,7,8\}&7.
\end{array}                                             \tag{7.4}
\]

Thus no one-endpoint projection has more than four states, and the orbit
\(\{1234,1235\}\) is completely frozen.  More than four physical labels
occur only in the **coupled** two-endpoint profile, on ten of the fourteen
ports.

For example, at \(P=1245\) the eight attainable pairs are

\[
 \boxed{
 \{(1,8),(2,3),(4,3),(5,3),(4,6),(4,7),(5,6),(5,7)\}.}               \tag{7.5}
\]

If a parent-aligned serviced target retains both endpoint tokens and has a
common core disjoint from them, (7.5) gives eight distinct physical target
sets.  This is a genuine finite multi-state seed and has enough scalar
alphabet size for every range in (3.5).

It is not a dense fragmentation theorem:

* a factor state is chosen for all fourteen ports simultaneously;
* two ports are frozen under the entire displayed library;
* the other ports have different, coupled palettes;
* strict-fringe placement erases every palette by Theorem 6.2;
* no parent-aligned bounded-block atlas covers \(M_s-o(M_s)\) occurrences.

Accordingly (7.5) proves finite local possibility above the four-cell
threshold, but not balanced multistate capacity or coefficient one.

## 8. Cross-context separation and residual capacity

Suppose a future boundary-active four-cell atom in context \(C\) has

\[
 T_C^{ab}=K_C\cup\{x_C^a,y_C^b\},
 \qquad a,b\in\{0,1\},                                \tag{8.1}
\]

with its two active coordinate pairs disjoint from each other and from
\(K_C\).

### Lemma 8.1 (collision localization)

If \(T_C^{ab}=T_D^{a'b'}\), then

\[
 K_C\setminus K_D\subseteq\{x_D^{a'},y_D^{b'}\},
 \qquad
 K_D\setminus K_C\subseteq\{x_C^a,y_C^b\}.           \tag{8.2}
\]

In particular,

\[
                         |K_C\triangle K_D|\le4.       \tag{8.3}
\]

#### Proof

An element of \(K_C\setminus K_D\) belongs to the common target but not
to \(K_D\), so it must be one of the two active labels supplied by context
\(D\).  The reverse containment is symmetric. \(\square\)

Thus core distance greater than four is an exact separator.  For
constant-weight \(k\)-cores in an \(n\)-set, the number of cores within
symmetric-difference distance four is at most

\[
                         \sum_{i=0}^2\binom{k}{i}\binom{n-k}{i}.        \tag{8.4}
\]

A greedy separated atlas therefore loses a polynomial factor in general,
not \(o(1)\), and does not prove coefficient one.  No private marker or
bounded weighted collision-degree theorem for the actual aligned contexts
is presently known.

Finally, all cell counts must be tested against the actual carrier-resolved
capacities

\[
                         c_T=(p-\beta(T))_+.           \tag{8.5}
\]

The distinguished first-insertion column of the \(D_4\) table does not
include the other cyclic starts, crossing collars, or loads from other
parent contexts.  A valid construction must enumerate the full affected
histogram \(u(T)\) and prove \(u(T)\le c_T\) (or the corresponding total
hinge bound) for one common integral factor choice at every protected
depth.

## 9. Precise proved and open boundary

The following claims are proved.

1. The abstract two-partition theorem is integral, sharp, and has error
   \(3B/4\), with exact exceptional and background terms.
2. The complete canonical preload and the exact four-, five-, six-, and
   seven-cell scalar thresholds are (0.2)--(0.3) and (3.4)--(3.6).
3. The canonical coordinate overlay cannot implement independent block
   signs; its largest cell remains at least \(C_s\).
4. First/last size-four fringe selection gives two raw fourteen-block
   partitions outside exponentially small mass, and phase-disjoint
   substitutions compose to one exact factor.
5. Every such strict fringe state is in the kernel of the protected
   endpoint statistic.  The useful active mass is zero, so this entire
   dense deployment is definitively ruled out.
6. The parent-aligned \(D_4/H_4\) library has an eight-target coupled seed,
   but also a frozen two-port orbit and no dense full-preload atlas.

The remaining theorem cannot be a refinement of strict fringe packing.  It
must construct bounded, boundary-active parent atoms whose changed slabs
meet the serviced endpoints, whose joint factor states fragment almost all
of the preload, and whose complete carrier profiles satisfy the true
residual capacities with cross-context congestion \(o(W)\).  A recomputed
endpoint overlay after internal \(D_4\) changes is not ruled out, but no
fragmentation theorem for that two-stage route is known.
