# ST_A through the Dyck quotient: the exact predecessor-port container and its harmonic obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil .                 \tag{0.1}
\]

The quotient form of the surviving linear-seam gate is

\[
 \boxed{\overline\nu_H=o_A(B_r/\sqrt r).}          \tag{QST_A}
\]

This note builds the exact dynamic container suggested by the
predecessor-child theorem.  It removes the formerly untracked
outer-fibre multiplicity, but it does **not** prove \((QST_A)\).
Instead it gives a sharp obstruction to obtaining the required little-oh
from the harmonic Pascal kernel alone.

At one inverse peak-deletion step, let the reduced core have rank \(d\)
and let \(y\) free leaves be distributed among its \(2d+1\) slots.  Put

\[
 P(d,y)=\binom{y+2d}{2d},\qquad
 K_z(d,y)=\binom{y-z+2d-1}{2d-1}.                 \tag{0.2}
\]

A terminal-slot value \(z\) produces \(z+1\) ordered, pairwise
edge-disjoint predecessor-child returns.  Split one unit of parent mass
equally among their ports \(i=0,\ldots,z\).  The exact load of port \(i\)
over the complete outer fibre is

\[
 C_i(d,y)=\sum_{z=i}^{y}\frac{K_z(d,y)}{z+1}.     \tag{0.3}
\]

Then

\[
 \boxed{
 C_i(d,y)\le C_0(d,y)=\rho(d,y)P(d,y),\qquad
 \sum_{i=0}^{y}C_i(d,y)=P(d,y),}                 \tag{0.4}
\]

where

\[
 \boxed{
 \rho(d,y)=\frac{2d}{y+1}
       \bigl(H_{y+2d}-H_{2d-1}\bigr).}           \tag{0.5}
\]

Thus \(\rho\) is an exact maximum-column contraction, while the whole
port operator has \(\ell^1\)-norm one.  The missing mass has not
disappeared: it occupies the other child ports.

The same statement remains exact on the physical outer sheets.  Above a
reduced quotient cycle the inverse fibres form cyclic covers of total
degree \(P(d,y)\).  After retaining the outer-sheet label, a decorated
\((z,i)\)-port has precisely \(K_z/(z+1)\) units of fractional sheet
load.  Summing over \(z\) gives (0.3); summing over \(i\) gives the full
cover degree \(P\).  Hence there is neither a hidden exponential loss nor
a hidden contraction in the projection.

On a fixed pruning profile \(\mathbf r=(r_0,r_1,\ldots)\), define

\[
 d_j=r_{j+1},\qquad
 y_j=r_j-2r_{j+1}+r_{j+2}.                        \tag{0.6}
\]

The serial container has maximum fixed-port-history density at most

\[
                         \prod_{j<L}\rho(d_j,y_j),              \tag{0.7}
\]

and total mass exactly one.  On the critical harmonic profile

\[
                         r_j=\frac R{j+1},                       \tag{0.8}
\]

one has

\[
 \frac{y_j}{2d_j}=\frac1{(j+1)(j+3)}                            \tag{0.9}
\]

and the completely exact estimate

\[
 \boxed{
 \prod_{j=0}^{L-1}\rho(d_j,y_j)
 \ge
 \prod_{j=0}^{L-1}
 \left(1-\frac1{2(j+1)(j+3)}\right)
 \ge\frac58.}                                      \tag{0.10}
\]

For fixed \(j\), as the integer scale \(R\to\infty\),

\[
 \rho(d_j,y_j)\longrightarrow
 (j+1)(j+3)
 \log\left(1+\frac1{(j+1)(j+3)}\right).          \tag{0.11}
\]

In particular its first factor is the advertised

\[
                         3\log(4/3)<1,                            \tag{0.12}
\]

but all later deficits are summable.  The first strict contraction does
not iterate to a vanishing factor.

Consequently the dynamic harmonic container, even with exact
outer-fibre congestion, can at most improve the constant in the existing

\[
                         O_A(B_r/\sqrt r)                         \tag{0.13}
\]

height-trace bound.  It cannot by itself turn (0.13) into a little-oh.
This is a no-go for the proposed proof mechanism, not a counterexample to
\((QST_A)\): the harmonic inverse fibres are actual Dyck-tree fibres,
but it is not proved that a positive fraction of them carry compatible
PBBS predecessor passages at every displayed level.

The exact surviving positive input is now one of the following.

1. **Dynamic eligibility loss:** actual predecessor itineraries must omit
   enough terminal values that their restricted port kernels have a
   vanishing fixed-history product on the critical Pascal mass, together
   with a bound preventing the lost mass from escaping into too many
   other histories.
2. **Port coalescence/non-reuse:** after physical phase transport, the
   union of active child-port sheets must have \(o(1)\) of the complete
   outer-cover degree.
3. **A non-harmonic passage theorem:** every critical actual passage tower
   must leave the harmonic profile often enough that the accumulated
   kernel deficit diverges.

No one of these statements follows from ranks, prescribed slots, the
\(z+1\) child count, or levelwise trace capacities.

## 1. Removing the reduced-wrap boundary

Let \(D\in\mathcal D_r\), and put

\[
                         d=|\partial D|.
\]

Since peak deletion removes every peak,

\[
                         d=r-\operatorname {pk}(D).              \tag{1.1}
\]

The number of roots with first-pruned rank \(d\) is therefore the
Narayana number

\[
 \mathsf N_r(d)
 =\frac1r\binom rd\binom r{d+1}.                 \tag{1.2}
\]

For \(d\le H=O_A(\sqrt r)\),

\[
\begin{aligned}
 \sum_{d\le H}\mathsf N_r(d)
 &\le (H+1)\binom rH\binom r{H+1}\\
 &\le\exp\bigl(O_A(\sqrt r\log r)\bigr)
 =o(B_r/\sqrt r).                                 \tag{1.3}
\end{aligned}
\]

If a parent gap obeys \(g\le2H-1\) and \(d>H\), then

\[
                         g<2d+1.                                  \tag{1.4}
\]

Thus every predecessor-child passage outside the negligible set (1.3)
is nonwrapping in the reduced quotient, exactly the hypothesis needed by
the \(z+1\) disjoint-child theorem.  Reduced wrap cannot account for the
failure below.

## 2. The one-level predecessor-port operator

Fix a reduced core of rank \(d\ge2\).  Its inverse fibre is the set

\[
 \mathcal W_{d,y}
 =\{(n_0,\ldots,n_{2d})\in\mathbb Z_{\ge0}^{2d+1}:
                         \sum_an_a=y\}.            \tag{2.1}
\]

Its cardinality is \(P(d,y)\).  Take \(n_{2d}\) to be the terminal root
slot and write

\[
                         z=n_{2d}.                                 \tag{2.2}
\]

There are exactly \(K_z(d,y)\) vectors with this value.

For a dynamically realized predecessor passage with terminal value \(z\),
Theorem 6.1 of the growing-gap audit supplies ordered child ports

\[
                         i=0,1,\ldots,z,                           \tag{2.3}
\]

whose residence intervals are pairwise edge-disjoint.  Define the
fractional port operator

\[
 T_{d,y}(\mathbf n,i)=
 \begin{cases}
 1/(z+1),&0\le i\le z=n_{2d},\\
 0,&i>z.
 \end{cases}                                      \tag{2.4}
\]

Every row of \(T_{d,y}\) sums to one.

### Theorem 2.1 (exact port-column ledger)

For every \(0\le i\le y\), the full-fibre column load is (0.3).  Moreover
(0.4) holds.

#### Proof

A vector of terminal value \(z\) contributes to port \(i\) precisely when
\(z\ge i\), and then contributes \(1/(z+1)\).  Summing the \(K_z\)
vectors proves (0.3).  Since all terms are nonnegative,

\[
                         C_i\le C_0.                              \tag{2.5}
\]

The harmonic Pascal identity gives

\[
 \frac{C_0}{P}
 =\frac1P\sum_{z=0}^{y}\frac{K_z}{z+1}
 =\frac{2d}{y+1}
   (H_{y+2d}-H_{2d-1}),                          \tag{2.6}
\]

which is (0.5).  Finally interchange the two finite sums:

\[
\begin{aligned}
 \sum_{i=0}^{y}C_i
 &=\sum_{i=0}^{y}\sum_{z=i}^{y}\frac{K_z}{z+1}\\
 &=\sum_{z=0}^{y}\frac{K_z}{z+1}
                         |\{0,\ldots,z\}|\\
 &=\sum_{z=0}^{y}K_z=P.
\end{aligned}                                      \tag{2.7}
\]

The last equality is the partition of the weak-composition simplex by
its terminal coordinate. \(\square\)

Equation (2.7) is the essential audit correction.  The factor \(\rho<1\)
does not reduce the total parent mass.  It says that no one **decorated
child port** receives more than \(\rho P\) mass.  There are enough other
ports to carry the complement.

### Actual passage values

For one reduced core and horizon \(H\), let

\[
 \mathcal Z_H(E)
 =\{z:\text{some nonwrapping predecessor passage of }E
       \text{ within the horizon prescribes }z\}.               \tag{2.8}
\]

The actual restricted loads are

\[
 C_i(E,H)
 =\sum_{\substack{z\in\mathcal Z_H(E)\\z\ge i}}
    \frac{K_z(d,y)}{z+1}.                         \tag{2.9}
\]

Put

\[
 A(E,H)=\sum_{z\in\mathcal Z_H(E)}K_z(d,y),
 \qquad
 \alpha(E,H)=\frac{A(E,H)}{P(d,y)}.               \tag{2.10}
\]

Because distinct terminal values occupy disjoint weak-composition
hyperplanes, \(A(E,H)\) is the exact number of active outer sheets at one
parent phase, not a union bound.

They obey

\[
 \sum_iC_i(E,H)
 =A(E,H),                                          \tag{2.11}
\]

and

\[
 C_i(E,H)\le C_0(E,H)\le\rho(d,y)P(d,y).          \tag{2.12}
\]

Thus actual quotient dynamics can improve the full kernel only through
the set \(\mathcal Z_H(E)\) and the phase geometry of its child ports.
The algebraic full-fibre value (0.5) is merely the sharp universal
container.

## 3. Exact outer-sheet congestion

Let \(C\) be a cycle of the reduced step-two PBBS quotient, and fix one
inverse-fibre cell with parameters \((d,y)\).  Peak deletion is a
semiconjugacy.  Hence every outer quotient cycle over \(C\) is a cyclic
cover

\[
                         \widetilde C_\alpha\longrightarrow C
\]

of some integral degree \(a_\alpha\), and exact fibre counting gives

\[
                         \sum_\alpha a_\alpha=P(d,y).            \tag{3.1}
\]

Identify all phase fibres with one reference fibre using the outer PBBS
transport.  This transport is bijective; it neither creates nor deletes a
slot vector.

### Theorem 3.1 (decorated sheet ledger)

Retain in a child state:

1. the reference outer sheet;
2. the prescribed terminal value \(z\);
3. the ordered child-port index \(i\); and
4. the reduced child occurrence and phase.

Then a fixed \((z,i)\) port has exact fractional sheet mass

\[
                         \frac{K_z(d,y)}{z+1},                    \tag{3.2}
\]

the union over terminal values has mass \(C_i(d,y)\), and the union over
all ports has total mass \(P(d,y)\).

#### Proof

There are exactly \(K_z\) outer sheets with terminal value \(z\) at the
parent phase.  Bijection of the phase fibres transports those sheets to
the indicated child occurrence without changing their number.  Each
sheet sends mass \(1/(z+1)\) to port \(i\), proving (3.2).  Summing first
over \(z\) and then over \(i\) is exactly Theorem 2.1. \(\square\)

For a pairwise top-edge-disjoint family, two different selected parent
intervals cannot use the same outer edge occurrence.  Therefore the
decorated sheet capacity in Theorem 3.1 is a genuine physical capacity,
not a formal multiplicity.  Erasing the sheet, terminal, or port labels
can merge columns, but it cannot lower their aggregate load.  In
particular:

\[
 \boxed{
 \text{retain the port label: maximum column factor }\rho;
 \qquad
 \text{erase all ports: total factor }1.}          \tag{3.3}
\]

This is the exact outer-fibre congestion dichotomy.  The exponentially
many lifts formerly observed above a single reduced trace are precisely
the \(P\) sheets in (3.1).  They have now been accounted for, but their
mass has not become small.

## 4. Serial composition on a fixed pruning profile

Fix ranks

\[
                         r_0>r_1>\cdots>r_{L+1}>0                \tag{4.1}
\]

with

\[
 y_j=r_j-2r_{j+1}+r_{j+2}\ge0.                  \tag{4.2}
\]

After fixing a bottom core and the complete rank profile, the successive
inverse peak-deletion fibres form a Cartesian product.  Put

\[
 P_j=P(r_{j+1},y_j),\qquad
 M_L=\prod_{j=0}^{L-1}P_j.                        \tag{4.3}
\]

The number \(M_L\) is the exact outer-sheet multiplicity of this profile
above the fixed bottom core.

Compose the port operators (2.4), retaining the full port history

\[
                         \mathbf i=(i_0,\ldots,i_{L-1}).          \tag{4.4}
\]

### Theorem 4.1 (dynamic profile container)

The serial operator is row-stochastic.  Its total mass on all terminal
port histories is \(M_L\), and every fixed history has load at most

\[
                         M_L\prod_{j=0}^{L-1}\rho(r_{j+1},y_j). \tag{4.5}
\]

In the unrestricted maximal container, the all-zero port history has
exactly the load

\[
                         M_L\prod_{j=0}^{L-1}\rho(r_{j+1},y_j). \tag{4.6}
\]

#### Proof

Every one-level row sums to one, so their serial product is row-stochastic
and preserves the total number \(M_L\) of outer sheets.  The maximum
one-level column sum is \(\rho_jP_j\) by Theorem 2.1.  Cartesian
factorization of the inverse choices multiplies these column bounds,
proving (4.5).

At one level, port zero is present for every terminal value and its exact
column sum is \(C_0=\rho_jP_j\).  Hence the Cartesian all-zero history has
the product load in (4.6). \(\square\)

Theorem 4.1 is the strongest conclusion available from the full harmonic
kernel without further PBBS restrictions.  It is an \(\ell^\infty\)
statement.  Its \(\ell^1\) statement is exact conservation.

## 5. Harmonic critical profiles do not contract

Fix \(L\).  Choose \(R\) divisible by

\[
                         \operatorname {lcm}(1,2,\ldots,L+2),   \tag{5.1}
\]

and put

\[
                         r_j=\frac R{j+1}
 \qquad(0\le j\le L+1).                          \tag{5.2}
\]

Then

\[
 d_j=r_{j+1}=\frac R{j+2},                        \tag{5.3}
\]

and

\[
 y_j
 =\frac{2R}{(j+1)(j+2)(j+3)}.                  \tag{5.4}
\]

Consequently

\[
                         t_j:=\frac{y_j}{2d_j}
 =\frac1{(j+1)(j+3)}.                             \tag{5.5}
\]

The harmonic kernel has the elementary average form

\[
\begin{aligned}
 \rho(d,y)
 &=\frac{2d}{y+1}
   \sum_{a=0}^{y}\frac1{2d+a}\\
 &=\frac1{y+1}\sum_{a=0}^{y}\frac{2d}{2d+a}.     \tag{5.6}
\end{aligned}
\]

### Theorem 5.1 (uniform positive harmonic product)

For every integer harmonic profile (5.2),

\[
                         \prod_{j=0}^{L-1}\rho(d_j,y_j)\ge5/8. \tag{5.7}
\]

#### Proof

From (5.6),

\[
\begin{aligned}
 1-\rho(d,y)
 &=\frac1{y+1}\sum_{a=0}^{y}\frac{a}{2d+a}\\
 &\le\frac1{y+1}\sum_{a=0}^{y}\frac a{2d}
 =\frac y{4d}.                                    \tag{5.8}
\end{aligned}
\]

Equations (5.5)--(5.8) give

\[
 \rho(d_j,y_j)
 \ge1-\frac1{2(j+1)(j+3)}.                       \tag{5.9}
\]

For numbers \(0\le x_j\le1\), finite induction gives

\[
                         \prod_j(1-x_j)\ge1-\sum_jx_j.          \tag{5.10}
\]

Finally,

\[
\begin{aligned}
 \sum_{j=0}^{\infty}\frac1{2(j+1)(j+3)}
 &=\frac14\sum_{j=0}^{\infty}
   \left(\frac1{j+1}-\frac1{j+3}\right)\\
 &=\frac38.                                        \tag{5.11}
\end{aligned}
\]

Substitution in (5.10) proves (5.7). \(\square\)

For fixed \(j\), the Riemann-sum form (5.6) gives

\[
 \rho(d_j,y_j)
 \longrightarrow
 \int_0^1\frac{1}{1+t_jx}\,dx
 =\frac{\log(1+t_j)}{t_j},                        \tag{5.12}
\]

which is (0.11).  At \(j=0\), \(t_0=1/3\), proving (0.12).

The ranks (5.2) occur in nonempty actual Dyck-tree inverse fibres.  One
may extend the successive leaf-count profile beyond level \(L+1\) by a
constant tail and realize it with an ordered collection of root paths;
equivalently, every nonincreasing finite leaf-count sequence is the
pruning profile of a plane tree.  Thus (5.7) is not an obstruction caused
by nonintegral or unrealizable ranks.

What remains unproved is passage compatibility: the maximal port
container permits every terminal value at every level, whereas an actual
PBBS core supplies only the dynamically realized set (2.8).  Any positive
use of exact quotient dynamics must enter precisely through this
difference.

## 6. Consequence for the ST_A target

Let \(b_{r,h}\) be the number of rank-\(r\) Dyck roots of height \(h\).
The height-gap theorem and quotient-edge disjointness give

\[
 \overline\nu_H
 \le\sum_{h\le H-1}\frac{b_{r,h}}{h+2}
 =O_A(B_r/\sqrt r).                                \tag{6.1}
\]

To deduce \((QST_A)\) from a dynamic container, its normalized retained
capacity on every critical height/profile sector, or on all but
\(o(B_r/\sqrt r)\) of their aggregate packing mass, must tend to zero.

Theorems 4.1 and 5.1 show that the unrestricted predecessor-port kernel
does not have this property.  Even through arbitrarily many integral
harmonic levels, one port-history column retains at least \(5/8\) of the
complete profile-fibre normalization, while total port mass remains one.
Consequently inserting (0.7) into (6.1) changes only its implicit
constant.  It supplies no function \(\eta(r)\to0\), and therefore no
little-oh.

There is a second way to see the same obstruction.  The local deficit
obeys

\[
                         1-\rho(d_j,y_j)=O(j^{-2}),              \tag{6.2}
\]

so

\[
                         \sum_j(1-\rho(d_j,y_j))<\infty.        \tag{6.3}
\]

A multiplicative container can vanish only if the accumulated logarithmic
deficit diverges.  The critical Pascal dynamics lies on the opposite side
of that boundary.

## 7. The exact remaining dynamic discrepancy

For an actual core \(E\) at level \(j+1\), define its restricted kernel

\[
 \rho_H^{\rm act}(E;y_j)
 =\frac1{P_j}
   \sum_{z\in\mathcal Z_H(E)}\frac{K_{j,z}}{z+1}. \tag{7.1}
\]

This records only the largest actual port column.  The complete restricted
port ledger is (2.9)--(2.12), while \(\alpha(E,H)\) is the exact
one-phase active-sheet fraction.  The physical support is further coupled
by phase transport on the cyclic covers.

A genuine fixed-history improvement over the harmonic container would be
an aggregate theorem asserting that on every critical passage tower,
outside \(o(B_r/\sqrt r)\) packing mass,

\[
 \sum_{j<L}
 \left(1-\frac{\rho_H^{\rm act}(E_{j+1};y_j)}
                  {\rho(d_j,y_j)}\right)
 \longrightarrow\infty.                           \tag{7.2}
\]

Equation (7.2) is the exact dynamic eligibility loss missing from the
maximal container.  It is not sufficient alone: the port operator is
mass-preserving, so mass may escape into a growing set of other histories.
To prove \((QST_A)\), (7.2) must be paired with a subcritical support
bound for those histories.  The direct alternative is a theorem that the
transported union of all active \((z,i)\)-sheets has \(o(1)\) of the full
cover degree; that is the exact non-reuse form.  At one phase its
untransported size is exactly \(\alpha(E,H)P\), so the genuinely new issue
is how these active hyperplanes overlap after transport across many parent
phases.

Ranks and horizon restrictions do not imply (7.2).  On the harmonic
profile the mean terminal occupancy is already \(O(j^{-2})\), and the
value \(z=0\) has dominant Pascal mass.  The gap-seven orbit proves that
\(z=0\) predecessor passages can be phase-dense on individual reduced
orbits, although that particular sector is exponentially negligible
globally.  Therefore any proof of (7.2) must use the joint distribution of
peak type, selected-label itinerary, and transported outer sheets across
the critical Pascal saddle.

## 8. Certified boundary

Proved:

1. small first-pruned ranks are negligible at the \(B_r/\sqrt r\) scale;
2. the exact stochastic predecessor-port operator (2.4);
3. its maximum-column harmonic factor and exact mass-conservation identity
   (0.4);
4. exact accounting of all outer cyclic-cover sheets;
5. exact serial composition on a fixed pruning profile;
6. the uniform positive lower bound \(5/8\) for the critical harmonic
   product; and
7. the precise actual-dynamics discrepancy (7.1)--(7.2).

Not proved:

1. an aggregate loss for actual predecessor-eligible values;
2. a vanishing active-sheet union theorem;
3. exclusion of harmonic profiles for actual critical passage towers; or
4. \((QST_A)\).

The value \(3\log(4/3)<1\) is therefore a correct and useful one-level
fact, but it is not a contracting Lyapunov exponent.  Once outer-fibre
congestion is recorded exactly, the harmonic deficits are summable and
the proposed dynamic container stops at the already known
\(O_A(B_r/\sqrt r)\) scale.
