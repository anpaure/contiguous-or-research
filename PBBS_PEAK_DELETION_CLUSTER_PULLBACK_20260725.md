# PBBS peak-deletion pullback for clustered cuts: exact recursion and the tilted-fibre obstruction

Date: 2026-07-25

This note uses only the already audited equality-particle return theorem,
the peak-deletion semiconjugacy, and the clustered dominance seam. Its
purpose is to determine whether short-return clusters at rank \(r\) can be
controlled recursively by clusters in the first-pruned PBBS.

The answer has two parts.

1. There is an exact phase-preserving pullback. Every rank-\(r\) short
   return contains, with the same starting phase, a strictly shorter
   return in the first-pruned PBBS. A clustered cut transversal for the
   reduced returns therefore lifts to a clustered transversal upstairs.
   Covering degrees and cluster spans can be counted exactly.
2. The resulting recursion has coefficient one. Its measure on reduced
   cores is the Pascal-tilted measure

   \[
      \Pr(\partial D=E)=P_r(E)/\operatorname{Cat}_r,
   \]

   not the uniform Catalan measure at the reduced rank. This measure is
   concentrated at \(d=r/2,\ k=r/6\), where \(d=|E|/2\) and
   \(k=\operatorname{pk}(E)\). That peak stratum is exponentially rare
   under the uniform rank-\(d\) Catalan measure. Consequently an
   unweighted lower-rank \(o(\operatorname{Cat}_d)\) clustering theorem
   cannot be inserted into the recursion.

The refined recursion identifies the exact missing object: a union of
transported inverse-fibre slot hyperplanes over each reduced cut cluster.
At the critical saddle a single zero-slot hyperplane already occupies
\(3/4+o(1)\) of its fibre. Iterated zero-slot restrictions also have
Catalan-positive total mass. Thus neither one-step nor iterated scalar
slot counting supplies a strict contraction. A proof still needs a
vanishing density theorem for the **decorated predecessor-passage starts**
inside the Pascal-tilted peak strata, or a direct correlation theorem
showing that their transported fibre unions occupy \(o(1)\) of the sheets.

## 1. The semiconjugate covering of quotient cycles

Let

\[
 \tau_r:\mathcal D_r\longrightarrow\mathcal D_r
\]

be the step-two PBBS permutation on Dyck roots of semilength \(r\). If
\(D\in\mathcal D_r\), let \(\partial D\) be simultaneous peak deletion and
write

\[
d(D)=|\partial D|/2.
\]

The audited semiconjugacy is

\[
\boxed{\partial(\tau_rD)=\tau_{d(D)}(\partial D).}       \tag{1.1}
\]

Fix a \(\tau_d\)-cycle \(C\), choose \(E\in C\), and put

\[
k=\operatorname{pk}(E),\qquad
P_r(C)=P_r(E):=\binom{r+d-k}{2d}.                 \tag{1.2}
\]

The value is constant on \(C\): (1.1) gives bijections between successive
inverse fibres, and (1.2) is the exact inverse peak-deletion count.

### Lemma 1.1 (exact covering degrees)

The \(\tau_r\)-cycles in \(\partial^{-1}(C)\) are cyclic covers

\[
\pi_\alpha:\widetilde C_\alpha\longrightarrow C
\]

of integral degrees \(a_\alpha\), and

\[
\boxed{\sum_\alpha a_\alpha=P_r(C).}             \tag{1.3}
\]

#### Proof

Equation (1.1) makes the restriction of \(\partial\) to every top cycle a
map of cyclic permutations, hence a cyclic cover. If \(|C|=\ell\), a
degree-\(a_\alpha\) cover has length \(a_\alpha\ell\) and contributes
exactly \(a_\alpha\) points above each fixed \(E\in C\). The complete
fibre above \(E\) has size \(P_r(C)\), proving (1.3). \(\square\)

In particular, an interval of span \(S<|C|\) has exactly \(a_\alpha\)
disjoint lifts of the same span to \(\widetilde C_\alpha\). Summed over
all top cycles, it has exactly \(P_r(C)\) lifted copies. No phase loss or
unknown multiplicity occurs here.

## 2. A top return contains a reduced return at the same phase

Consider an odd physical return gap

\[
g=2s+1<2r+1.
\]

The equality-particle theorem says that the particle selected at time zero
is selected again for the first time at an odd time

\[
h=2t+1\le g-2.
\]

In the PBBS whose root is \(E=\partial D\), this is a consecutive
same-particle return. The eventual entry by the immediate predecessor is
extra decoration, but it is not needed for the following transversal
statement.

### Lemma 2.1 (phase-preserving interval containment)

In the step-two quotient, the reduced return interval starts above the
same time-zero edge and has edge support contained in the projection of
the top return interval. Its residence is at most \(H-1\) whenever the
top residence is at most \(H\).

#### Proof

Both systems use the same physical update clock. Times zero and \(h\)
have the same odd separation as times zero and \(g\), so pairing updates
into step-two transitions gives quotient intervals with the same initial
phase. Since \(h\le g-2\), the reduced endpoint occurs at least one
step-two transition earlier. Semiconjugacy (1.1) identifies every
intermediate reduced edge with the projection of the corresponding top
edge. \(\square\)

Consequently, if a reduced cut meets that child return, its lift at the
same time meets the parent return. Notice that this statement remains
valid after replacing a parent return by the minimal simple subreturn from
the simple-return normal form: one simply applies Lemma 2.1 to the new
time-zero edge. No false converse from peak defect is used.

## 3. Exact pullback of clustered cut transversals

For a horizon \(H\), write

\[
q_H(S)=7H+3S-3.                                  \tag{3.1}
\]

This is the audited endpoint-and-seam charge for a cut cluster of span
\(S\), valid when

\[
3H+S\le r+1.                                     \tag{3.2}
\]

Let \(C\) be a reduced quotient cycle. Take a cut transversal \(Q_C\)
for all reduced return intervals of residence at most \(H-1\), and
partition it into clusters \(Q_{C,j}\), each contained in a proper cyclic
arc of span \(S_{C,j}\). Assume (3.2) for every cluster.

### Theorem 3.1 (full-fibre cluster pullback)

Lifting every cut in \(Q_C\) to every cycle above \(C\) gives a transversal
of every rank-\(r\) return whose first-pruned root lies on \(C\). Its exact
cluster charge is at most

\[
\boxed{
  P_r(C)\sum_j q_H(S_{C,j}).}                     \tag{3.3}
\]

#### Proof

Lemma 2.1 gives a child interval \(J(I)\) for every parent interval \(I\).
Some cut of \(Q_C\) lies in \(J(I)\); the corresponding lifted cut lies in
\(I\). Thus the lifted set is a transversal.

On a degree-\(a_\alpha\) cover, every proper base cluster has
\(a_\alpha\) copies of exactly the same span. Each copy is eligible for
the clustered seam by (3.2). Its charge is \(q_H(S_{C,j})\). Sum first
over the copies and then use (1.3). \(\square\)

Define \(\chi_{d,H}^{(r)}(C)\) as the minimum of

\[
\sum_j q_H(S_{C,j})                               \tag{3.4}
\]

over such transversals of the rank-\(d\), residence-\((H-1)\) return
family, with the outer admissibility condition (3.2). Apart from the
exceptional classes treated in Section 4, Theorem 3.1 gives the exact
recursive upper bound

\[
\boxed{
 \mathfrak S_{r,H}
 \le
 \sum_{d=1}^{r-1}\ \sum_{C\subset\mathcal D_d}
      P_r(C)\,\chi_{d,H}^{(r)}(C)+\mathcal E_{r,H}.}
                                                              \tag{3.5}
\]

Here \(C\) ranges over \(\tau_d\)-cycles. If \(d\ge3H\), every cluster
admissible for the native rank-\(d\), horizon-\(H\) seam is also admissible
upstairs. Since residence at most \(H-1\) is a subfamily of residence at
most \(H\), one may use the simpler bound

\[
\chi_{d,H}^{(r)}(C)\le\chi_{d,H}^{(d)}(C).        \tag{3.6}
\]

There is no factor \(H\), no unaccounted deck multiplicity, and no phase
error in (3.5). But there is also no coefficient smaller than one.

## 4. Small reduced ranks and short reduced cycles are exponentially negligible

The exceptional term in (3.5) can be made much smaller than
\(B_r/r\), where \(B_r=\operatorname{Cat}_r\).

First, the number of rank-\(r\) roots with first-pruned rank \(d\) is the
Narayana number

\[
\frac1r\binom rd\binom r{d+1}.                  \tag{4.1}
\]

Thus the total number with \(d<3H=O_A(\sqrt r)\) is

\[
\exp(O_A(\sqrt r\log r))=\exp(o(r)).             \tag{4.2}
\]

Second, the number of reduced roots, over all \(d\le r\), lying on
\(\tau_d\)-cycles of length at most \(3H\) is also

\[
\exp(O_A(\sqrt r\log r))=\exp(o(r)),             \tag{4.3}
\]

by the standard voltage-itinerary bound. For every core \(E\in\mathcal
D_d\),

\[
P_r(E)=\binom{r+d-k(E)}{2d}
      \le\binom{r+d}{2d}
      \le\sum_{j=0}^r\binom{r+j}{2j}
      =F_{2r+1},                                  \tag{4.4}
\]

where \(F_n\) is Fibonacci. Since

\[
F_{2r+1}=\exp((2\log\varphi+o(1))r),
\qquad 2\log\varphi<\log4,                       \tag{4.5}
\]

the complete inverse mass above (4.3) is exponentially small relative to
\(B_r\asymp4^r/r^{3/2}\). Cutting every exceptional root separately costs
only an additional \(O(H)\) per root. Therefore

\[
\boxed{\mathcal E_{r,H}=e^{-c r+o(r)}B_r=o(B_r/r)}              \tag{4.6}
\]

for some absolute \(c>0\) and every fixed \(A\).

Thus exceptional small ranks and short reduced cycles do not obstruct a
summable recursion. The obstruction lies in the main Pascal saddle.

## 5. Why the recursion has coefficient one

The inverse fibres partition \(\mathcal D_r\), so

\[
\boxed{
 \sum_{d=1}^{r-1}\ \sum_{E\in\mathcal D_d}P_r(E)=B_r-1.}
                                                              \tag{5.1}
\]

Equivalently, for a uniformly random nonstar \(D\in\mathcal D_r\),

\[
\Pr(\partial D=E)=\frac{P_r(E)}{B_r-1}.           \tag{5.2}
\]

After normalization, (3.5) is therefore an average with total mass one.
Peak deletion gives localization, but no strict contraction.

More importantly, this is not the uniform Catalan law at rank \(d\). If
\(E\) has \(d\) edges and \(k\) peaks, the exact mass of its cell is

\[
\mathsf M_r(d,k)
=\frac1d\binom dk\binom d{k-1}
 \binom{r+d-k}{2d}.                               \tag{5.3}
\]

Its two-dimensional saddle is

\[
\boxed{d=r/2+O(\sqrt r),\qquad k=r/6+O(\sqrt r).}               \tag{5.4}
\]

The union of every fixed-width Gaussian tube around (5.4) carries a
positive limiting fraction of \(B_r\). By contrast, at \(d=r/2+O(\sqrt
r)\), the same peak stratum has \(k/d=1/3+o(1)\), while a uniform
rank-\(d\) Catalan root has peak density \(1/2+o(1)\). Indeed,

\[
\frac{\frac1d\binom d{d/3}\binom d{d/3-1}}{B_d}
=\exp\left(-d\,[\log4-2\mathsf h(1/3)]+o(d)\right),            \tag{5.5}
\]

and

\[
\log4-2\mathsf h(1/3)>0.                        \tag{5.6}
\]

Hence a set of reduced cores can have size \(o(B_d)\) at every reduced
rank, yet carry a positive fraction of the parent mass in (5.2). This is
the precise reason that an unweighted lower-rank statement such as

\[
\sum_C\chi_{d,H}^{(d)}(C)=o(B_d)                 \tag{5.7}
\]

does not close (3.5). What is needed is (5.7) uniformly in the
Pascal-tilted Narayana cells, with the exact weights (5.3).

The same issue persists after restricting to any fixed Gaussian height
window. Peak deletion lowers height by exactly one, so

\[
\sum_{\substack{E:\operatorname{ht}(E)=h-1}}P_r(E)
=\#\{D\in\mathcal D_r:\operatorname{ht}(D)=h\}.  \tag{5.8}
\]

Thus peak deletion transports the whole critical height mass; it does not
make that mass smaller.

## 6. The exact fibre-union refinement

The full-fibre lift in Theorem 3.1 can overpay. The precise possible gain
can also be stated exactly.

Fix one base cycle \(C=(E_t)_{t\in\mathbb Z/\ell\mathbb Z}\) and identify
all fibres with

\[
\mathcal F=\partial^{-1}(E_0)
\]

by the bijections \(\tau_r^{-t}\). Assign every active parent return to
one reduced cut \(q\) lying in its canonical child interval. Let

\[
\mathcal A_q\subseteq\partial^{-1}(E_q)           \tag{6.1}
\]

be the parent states assigned to \(q\). For a base cut cluster \(J\), put

\[
\boxed{
 \mathcal U_J
  =\bigcup_{q\in J}\tau_r^{-q}\mathcal A_q
  \subseteq\mathcal F.}                           \tag{6.2}
\]

### Proposition 6.1 (selective-sheet cluster lift)

The parent cuts assigned to \(J\) can be covered by lifted clusters of the
same span as \(J\), with total charge at most

\[
\boxed{q_H(\operatorname{span}J)\,|\mathcal U_J|.}             \tag{6.3}
\]

#### Proof

Transporting a parent state at time \(q\) back by \(\tau_r^{-q}\)
identifies the sheet of the cyclic cover on which its lifted cut lies.
For one reference-fibre element, all assigned cuts whose transports equal
that element occur in one lifted copy of the base cluster and are covered
by its one cluster chart. Use one copy for every element of
\(\mathcal U_J\). Duplicate copies lying on the same top cycle can only
reduce the cost. \(\square\)

Formula (6.2), not a scalar inverse-fibre count, is the exact remaining
phase-correlation object. The full pullback takes
\(\mathcal U_J=\mathcal F\) and recovers (3.3). A strict recursive
contraction would follow from a suitably averaged estimate

\[
|\mathcal U_J|=o(P_r(C)),                          \tag{6.4}
\]

or from an equivalent vanishing active-span statement. Neither is a
formal consequence of the predecessor-slot criterion.

For one fixed reduced passage there is, in fact, an exact lower barrier
to such a gain. Fix a passage \((E,g)\) prescribing slot \(z\), and let

\[
\mathcal H_z=\{D\in\partial^{-1}(E):n_0(D)=z\}.     \tag{6.5}
\]

Every \(D\in\mathcal H_z\) is an actual parent return start, by the
predecessor-passage iff theorem. Assign each of these parent returns to
any one cut at offset \(q(D)\) in its common child interval. At that cut
the top state is \(\tau_r^{q(D)}D\); transporting it back as in (6.2)
returns exactly \(D\). Hence, over any partition of the assigned cuts
into clusters,

\[
\boxed{\sum_J|\mathcal U_J|\ge|\mathcal H_z|=K_r(d,k,z).}       \tag{6.6}
\]

The inequality by itself counts cluster copies before possible merging
between different laps of one top covering cycle. Such merging still
cannot create a vanishing gain once the reduced cycle length
\(\ell\) exceeds \(3H\). Indeed, two lifts of the same base start in
consecutive laps are \(\ell\) transitions apart, while their assigned
cuts can shift by at most \(H\). Thus their cyclic separation is at least
\(\ell-H>2H\). A top cluster containing \(t\) of these marked cuts has
span at least

\[
(t-1)(\ell-H)>2H(t-1),
\]

and consequently has charge

\[
q_H(S)\ge7H+6H(t-1)-3\ge6Ht
\]

for all sufficiently large \(H\). Summing over top clusters and top
cycles proves that every selective-sheet pullback of this one passage
costs at least

\[
\boxed{6H\,K_r(d,k,z).}                            \tag{6.7}
\]

Thus clever assignment of the lifts to different child cuts cannot make
the fibre union vanish. It can only share different **base passages**
which already cluster in their reduced chronology.

For one passage prescribing final-root slot \(z\), its active inverse
hyperplane has exact relative size

\[
\frac{K_r(d,k,z)}{P_r(d,k)}
=\frac{2d}{r+d-k}
 \prod_{i=0}^{z-1}
  \frac{r-d-k-i}{r+d-k-1-i}.                     \tag{6.8}
\]

At the saddle (5.4),

\[
\boxed{
 \frac{K_r(d,k,z)}{P_r(d,k)}
 \longrightarrow\frac34\,4^{-z}.}              \tag{6.9}
\]

In particular, a single zero-slot passage already occupies
\(3/4+o(1)\) of the fibre. Taking a union over several cuts can only
increase this fraction. So (6.4) cannot come from one-slot cardinality
alone.

Nor does iteration of zero-slot restrictions force vanishing mass. The
unary-root family

\[
\{\,1E0:E\in\mathcal D_{r-1}\,\}                  \tag{6.10}
\]

has size \(B_{r-1}\sim B_r/4\), is closed under peak deletion until the
core vanishes, and has terminal root slot zero at every active pruning
level. This does not prove that its members satisfy the decorated
predecessor passages. It proves exactly that inverse slots and pruning
profiles alone cannot provide the missing vanishing factor.

There is one stronger audited chronology statistic. If a predecessor
passage prescribes slot \(z\), it contains \(z+1\) pairwise edge-disjoint
child returns. Averaging the reciprocal branch count over a complete
inverse fibre with \(y\) free leaves and a rank-\(d\) core gives the exact
factor

\[
\rho(d,y)
=\frac{2d}{y+1}\bigl(H_{y+2d}-H_{2d-1}\bigr).     \tag{6.11}
\]

At the first saddle, \(d\sim r/2,\ y\sim r/3\), this tends to

\[
3\log(4/3)<1.                                     \tag{6.12}
\]

So predecessor branching gives a genuine one-level contraction. It still
does not iterate to zero on the critical pruning profile. There

\[
d=r_{j+1}\sim\frac r{j+2},\qquad
y=r_j-2r_{j+1}+r_{j+2}
  \sim\frac{2r}{(j+1)(j+2)(j+3)},                 \tag{6.13}
\]

and hence \(y/(2d)\sim((j+1)(j+3))^{-1}\). Expanding (6.8) gives

\[
\rho(r_{j+1},y_j)=1-O(j^{-2}).                    \tag{6.14}
\]

The product of these local chronology contractions can therefore remain
positive. This agrees with the already audited warning that the ordered
child traces, not merely their number, must be controlled in a global
clone/capacity space.

## 7. The surviving recursive target

For fixed \(A\), put \(H=\lceil A\sqrt r\rceil\). The linear one-cut seam
needs only a vanishing improvement over the reciprocal-height packing
scale:

\[
\overline\nu_H=o_A(B_r/\sqrt r).                  \tag{7.1}
\]

The height trace gives the corresponding \(O_A(B_r/\sqrt r)\) bound.
Equations (3.5)--(6.14) show exactly what would make the improvement strict.

Let a **decorated reduced start** mean a root for which the initially
selected equality particle has a short consecutive return and its
immediate predecessor subsequently completes the parent passage within
the horizon. In the critical cell (5.4), let

\[
\eta_{r,H}(d,k)
\]

be the fraction of rank-\(d\), \(k\)-peak cores which are decorated reduced
starts (with the necessary slot layers retained). A sufficient recursive
input is a Pascal-weighted vanishing statement of the form

\[
\boxed{
 \frac1{B_r}
 \sum_{|d-r/2|,|k-r/6|=O(\sqrt r)}
    \mathsf M_r(d,k)\,\eta_{r,H}(d,k)
 \longrightarrow0,}                              \tag{7.2}
\]

with the cluster version replacing \(\eta\) by the normalized fibre-union
cost in (6.2). The already audited saddle lower bound shows that a
positive limiting density throughout this tube saturates the
\(B_r/\sqrt r\) height-trace scale, so vanishing in (7.2) is also the
right qualitative demand.

The first-pruned rank in the tube is \(d\sim r/2\), but its peak density is
\(k/d\sim1/3\), not the uniform Catalan value \(1/2\). The natural
recursively critical feasible profile begins

\[
r_0\sim r,\quad r_1\sim r/2,\quad r_2\sim r/3,\quad\ldots,      \tag{7.3}
\]

and the zero-slot fractions along this profile are

\[
\frac{2r_{j+1}}{r_j+r_{j+2}}
\sim\frac{(j+1)(j+3)}{(j+2)^2}
=1-\frac1{(j+2)^2}.                              \tag{7.4}
\]

Their infinite product is

\[
\prod_{j=0}^{\infty}
\left(1-\frac1{(j+2)^2}\right)=\frac12.         \tag{7.5}
\]

Thus even the formal critical-profile product has a positive limit, in
agreement with the exact unary family. There is no hidden strict
contraction in the Pascal kernels.

The conclusion is therefore sharp: peak deletion pulls every outer short
return into a same-phase, \(O(H)\)-local reduced cluster, with exponentially
small exceptional error. But the exact recursion is mass-preserving and
Pascal-tilted. A coefficient-one proof needs a new vanishing theorem for
decorated predecessor-passage density, or for the transported fibre unions
\(\mathcal U_J\), inside the critical tilted peak strata.

This is the precise obstruction to obtaining a strict contraction from
peak deletion plus clustered-span sharing alone.
