# Mathematical attack J: rotor--SCD low-switch resolution

Date: 2026-07-24

## Verdict

This line does **not** prove the contiguous-OR width conjecture.

It does give a sharp structural answer to the proposed multicover-coloring
route.  After all physical cuts are charged, the optimum cost of coloring the
exact rotor multicover by genuine integral SCD colors, measured by the
weighted extraction run-start toll, is exactly

\[
 Q_m\min_{\mathcal D}\widehat\Phi_H(\mathcal D)
\]

on every fixed band.  The separate physical master-circuit initialization is
bounded within a constant factor and hence has the same \(o(Q_mW)\)
threshold; no exact equality for the sum of the two ledgers is claimed.  Thus
Euler-tour interleaving, Birkhoff decomposition,
multicolor discrepancy, and averaging do not provide an independent escape
from the one-SCD rotor path-forest lemma.  Any full low-switch coloring already
contains a single low-toll integral SCD.

There are four additional unconditional advances.

1. The uniform fractional SCD and the uniform fractional rotor circulation
   both have zero fractional path defect, and both marginals are separately
   integrally decomposable.  Therefore every argument using only these two
   projections is vacuous for the required common integral selector.
2. The odd-cut rotor skeleton can be orbited and Eulerized into an **exact**
   low-run coloring of the whole master occurrence multiset by pseudo-colors.
   These pseudo-colors have the correct chain histogram but need not be SCDs.
3. Resolving those pseudo-colors into prescribed genuine SCD colors is exactly
   a product of statewise bijection, or permutation-synchronization, problems.
   This gives precise sparse-repair and block-permutation sufficient criteria.
4. Legal two-color SCD exchanges are exactly unions of connected components
   of the ownership overlay.  Moreover, any successful SCD must contain
   \(\omega(\sqrt m)\)-long rotor runs through almost all of every
   positive-density typical-radius annulus.

The smallest unproved lemma remains the fixed-window integral rotor--SCD
path-forest lemma \(\mathrm{RSCD}_A\), stated in Section 8.  The
partial-packing statement in Section 6 is strictly weaker than saturating all
\(Q_m\) colors, but its averaging conclusion still contains the same good
integral SCD atom.

## 1. Exact band master and the run ledger

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_d=\binom{2m}{m-d},\qquad Q_m=(2m-1)(2m)!.
\]

Set \(N_{m+1}=0\) and \(c_d=N_d-N_{d+1}\) for \(0\le d\le m\).
Fix \(H\le m-2\).  For a clipped band define

\[
 \gamma_d=
 \begin{cases}
 N_d-N_{d+1},&0\le d<H,\\
 N_H,&d=H.
 \end{cases}
\]

Then

\[
 \sum_{d=0}^H\gamma_d=W,
 \qquad
 \sum_{d=q}^H\gamma_d=N_q\quad(0\le q\le H).
 \tag{1.1}
\]

Also,

\[
 W\ge\frac{4^m}{2m+1},
 \tag{1.1a}
\]

because \(W\) is the largest of the \(2m+1\) binomial coefficients whose
sum is \(4^m\).  In particular every fixed polynomial in \(m\) is \(o(W)\).

A labelled radius-\(d\) symmetric chain has state

\[
 \omega=(L;z_1,\ldots,z_{2d};R),
 \qquad |L|=|R|=r=m-d.
\]

For \(d\ge1\), its directed rotor successors are

\[
 (L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}),
 \qquad x\in L,\ y\in R.
 \tag{1.2}
\]

At \(d=0\), (1.2) is replaced by the ordinary swap

\[
 (L;\ ;R)\longmapsto(L-x+y;\ ;R-y+x).
 \tag{1.3}
\]

Write \(\Omega_d\) for the state set and \(G_d\) for this directed rotor
graph.  If \(G=(2m)!\), then

\[
 |\Omega_d|=\frac{G}{r!^2},
 \qquad \deg^+=\deg^-=r^2.
 \tag{1.4}
\]

Let \(s=2m-1\).  The exact radius-\(d\) master has

\[
 a_d=s\gamma_d(r-1)!^2
 \tag{1.5}
\]

copies of every directed rotor arc.  Hence every state occurs as a transition
head

\[
 a_dr^2=s\gamma_dr!^2
       =\frac{Q_m\gamma_d}{|\Omega_d|}
 \tag{1.6}
\]

times, and the total number of transition heads is \(Q_mW\).

The mask count is exact as well.  A fixed mask of rank \(m\pm q\) is contained
in \(|\Omega_d|/N_q\) radius-\(d\) states for every \(d\ge q\).  By (1.1) and
(1.6), its total designated occurrence count is

\[
 \sum_{d=q}^H
 \frac{|\Omega_d|}{N_q}\frac{Q_m\gamma_d}{|\Omega_d|}
 =\frac{Q_m}{N_q}\sum_{d=q}^H\gamma_d
 =Q_m.
 \tag{1.7}
\]

Let \(\mathcal D\) be a full SCD, clipped to the band.  Its radius-\(d\)
class \(\mathcal D_d\) has \(\gamma_d\) states.  Define

\[
 p_d^*(\mathcal D)=
 \min\{p(F):F\text{ is a spanning vertex-disjoint directed path forest in }
 G_d[\mathcal D_d]\}
 \tag{1.8}
\]

and define the exact prefix-extraction toll and a convenient conservative
reset toll by

\[
 \widehat\Phi_H(\mathcal D)=\sum_{d=0}^H2d\,p_d^*(\mathcal D),
 \qquad
 \Phi_H(\mathcal D)=\sum_{d=0}^H(2d+1)p_d^*(\mathcal D).
 \tag{1.9}
\]

For a full SCD, \(p_0^*\le c_0=W/(m+1)\), and hence

\[
 \widehat\Phi_H\le\Phi_H
 \le\frac32\widehat\Phi_H+\frac{W}{m+1}.
 \tag{1.9a}
\]

A directed run through \(t\) radius-\(d\) states is materialized by a literal
MTF word of length

\[
 (2d+1)+(t-1)=t+2d.
 \tag{1.10}
\]

Indeed, write the singleton blocks \(z_{2d},\ldots,z_1\) followed by the
lower block \(L\); the residual block need not be written.  Thus \(2d\) is
the exact hard-reset prefix-extraction overhead of one run.  Writing the
residual as well gives the stronger canonical-reset overhead \(2d+1\) used
by \(\Phi_H\).  This is distinct from the cost of first materializing an
abstract master circuit: the latter is at most \(2d+2\) per physical
circuit.  Since

\[
 2d+2\le2(2d+1),
 \tag{1.11}
\]

an \(o(Q_mW)\) conservative run toll also gives \(o(Q_mW)\) physical
initialization.
Abstract Euler closure does not restore the complete physical MTF state, so
every actual circuit cut is declared a hard run start throughout this report.
In particular, the construction below has combined run and master-circuit
initialization charge at most \(3Q_m\Phi_H\), while its exact prefix run
ledger is \(Q_m\widehat\Phi_H\).  By (1.9a), the two tolls have the same
\(o(Q_mW)\) threshold.

## 2. Exact chronology-elimination theorem

### Theorem 2.1 (no averaging or Birkhoff escape)

Let \(H\le m-2\).  Optimize simultaneously over

1. decompositions of the exact master occurrence multiset into \(Q_m\)
   genuine full-SCD colors, clipped to the band; and
2. all Euler/trail chronologies using every master-arc copy exactly once.

Every physical cut is charged as a hard monochromatic run start.  If \(R_H^*\)
is the minimum total weighted run-start toll, then

\[
 \boxed{
 R_H^*=Q_m\min_{\mathcal D\text{ full SCD}}\Phi_H(\mathcal D).
 }
 \tag{2.1}
\]

The upper bound constructs the chronology.  For an arbitrarily frozen Euler
chronology, only the lower bound in (2.1) is asserted.

#### Proof: lower bound

Take any feasible integral resolution and denote its SCD colors by
\(\mathcal D_1,\ldots,\mathcal D_{Q_m}\).  Cut every physical circuit at its
charged hard start.  For one color \(c\) and one radius \(d\), split the
color-\(c\) positions into maximal monochromatic runs.

Consecutive states in each run are related by a directed rotor arc.  Because
\(\mathcal D_c\) is an exact SCD color, each state of
\((\mathcal D_c)_d\) occurs exactly once in that color.  Consequently no run
repeats a vertex, distinct runs are vertex-disjoint, and the runs together
span \((\mathcal D_c)_d\).  They therefore form a spanning directed path
forest.  If \(r_{c,d}\) is the number of runs, then

\[
 r_{c,d}\ge p_d^*(\mathcal D_c).
 \tag{2.2}
\]

A cyclic monochromatic component creates no loophole: its mandatory physical
cut deletes one cyclic adjacency and makes one path component.  Summing (2.2)
gives

\[
 \begin{aligned}
 R_H
 &=\sum_{c=1}^{Q_m}\sum_{d=0}^H(2d+1)r_{c,d}\\
 &\ge\sum_{c=1}^{Q_m}\Phi_H(\mathcal D_c)\\
 &\ge Q_m\min_{\mathcal D}\Phi_H(\mathcal D).
 \end{aligned}
 \tag{2.3}
\]

#### Proof: upper bound

Choose a full SCD \(\mathcal D\) and, in every radius, an optimal forest
\(F_d\) with \(p_d=p_d^*(\mathcal D)\) components.  Index colors by

\[
 (b,\sigma)\in[s]\times S_{2m},
 \tag{2.4}
\]

and let color \((b,\sigma)\) carry \(\sigma\mathcal D\).  A state has
stabilizer \(r!^2\), so this colored orbit uses each state

\[
 s\gamma_dr!^2
 \tag{2.5}
\]

times, exactly the master multiplicity (1.6).

A directed rotor arc has stabilizer \((r-1)!^2\).  The forest \(F_d\) has
\(\gamma_d-p_d\) arcs.  Therefore its complete colored coordinate orbit uses
each directed rotor arc

\[
 s(\gamma_d-p_d)(r-1)!^2
 \tag{2.6}
\]

times.  Subtracting (2.6) from the master multiplicity (1.5) leaves

\[
 sp_d(r-1)!^2
 \tag{2.7}
\]

copies of every arc.  Thus every state has exactly

\[
 sp_d(r-1)!^2r^2=sp_dr!^2
 \tag{2.8}
\]

residual incoming arcs and the same number of residual outgoing arcs.  By
coordinate transitivity, the colored forest orbit also has exactly
\(sp_dr!^2\) path starts and path ends at every state.

At each state, pair the residual incoming arcs bijectively with the colored
paths starting there and prepend the paired connector to the path.  Contract
every resulting connector-plus-path trail.  At a state, the number of
contracted macroedges starting there is its residual outdegree, while the
number ending there is the number of colored path ends; both equal (2.8).
Hence every weak macrocomponent is balanced.  Eulerize each nonempty
macrocomponent and expand its macroedges.

Every master-arc copy is used once, and every selected colored forest path is
consecutive.  Place each physical circuit cut at a path boundary.  There are
at most \(Q_mp_d\) hard radius-\(d\) runs, so

\[
 R_H\le Q_m\sum_{d=0}^H(2d+1)p_d
      =Q_m\Phi_H(\mathcal D).
 \tag{2.9}
\]

The refined-prefix rotor realization makes every finite expanded trail
literal.  Its separate physical-circuit initialization cost is at most

\[
 Q_m\sum_{d=0}^H(2d+2)p_d
 \le2Q_m\Phi_H(\mathcal D).
 \tag{2.10}
\]

Minimizing \(\mathcal D\) proves (2.1).  \(\square\)

### Corollary 2.2 (exact averaging consequence)

A full integral resolution with \(R_H=o(Q_mW)\) exists if and only if one full
integral SCD satisfies \(\Phi_H=o(W)\).  Indeed, the forward implication also
follows directly from

\[
 \min_c\Phi_H(\mathcal D_c)
 \le\frac1{Q_m}\sum_c\Phi_H(\mathcal D_c)
 \le\frac{R_H}{Q_m}.
 \tag{2.11}
\]

Thus an SCD mixture, however cleverly interleaved, cannot have small average
toll unless one of its integral atoms is already good.

### Corollary 2.3 (full-master version)

Let

\[
 \Phi^{<}(\mathcal D)=
 \sum_{d=0}^{m-2}(2d+1)p_d^*(\mathcal D).
 \tag{2.12}
\]

If \(R_{\rm full}^*\) is the optimized full-master toll, then

\[
 Q_m\min_{\mathcal D}\Phi^{<}(\mathcal D)
 \le R_{\rm full}^*
 \le Q_m\min_{\mathcal D}\Phi^{<}(\mathcal D)+O(Q_mm^2).
 \tag{2.13}
\]

For the upper bound, repeat the radiuswise orbit/Euler proof of Theorem 2.1
with the un-clipped multiplicities
\(\gamma_d=c_d\) for \(0\le d\le m-2\); no clipped-band telescoping identity
is needed for that radiuswise construction.  Retain the audited terminal
master circuits but charge every terminal occurrence as a separate run.
Since

\[
 c_{m-1}=N_{m-1}-N_m=2m-1,
 \qquad c_m=1,
 \tag{2.14}
\]

the terminal reset charge is at most \((2m+1)(c_{m-1}+c_m)=O(m^2)\) per
color.  Since \(m^2=o(W)\), (2.13) has the same \(o(Q_mW)\) threshold.

This full-master statement is stronger than the fixed-window rotor route
needed for the conjecture.  One must not replace the audited fixed-window
reduction by an unproved all-radius assertion.

## 3. Why separate fractional and Birkhoff statements are insufficient

### Theorem 3.1 (perfect fractional marginals, zero fractional defect)

On a fixed clipped band set

\[
 x_\omega=\frac{\gamma_d}{|\Omega_d|}
 \qquad(\omega\in\Omega_d).
 \tag{3.1}
\]

Then \(x\) satisfies every band-SCD mask equation.  Indeed, for a fixed mask
\(A\) of rank \(m\pm q\),

\[
 \sum_{\omega\ni A}x_\omega
 =\sum_{d=q}^H
   \frac{|\Omega_d|}{N_q}\frac{\gamma_d}{|\Omega_d|}
 =1
 \tag{3.2}
\]

by (1.1).

The rotor graph \(G_d\) is \(k_d=r^2\)-regular.  Put

\[
 f_e=\frac{\gamma_d}{|\Omega_d|k_d}
 \qquad(e\in E(G_d)).
 \tag{3.3}
\]

At every state \(\omega\),

\[
 \sum_{e\in\delta^+(\omega)}f_e
 =\sum_{e\in\delta^-(\omega)}f_e=x_\omega.
 \tag{3.4}
\]

Moreover,

\[
 \sum_{\omega\in\Omega_d}x_\omega
 -\sum_{e\in E(G_d)}f_e
 =\gamma_d-\gamma_d=0.
 \tag{3.5}
\]

Thus the naive fractional path-start defect is zero at every radius.

This is not an integrality theorem in disguise.  The vector \(x\) is the
barycenter of the complete coordinate orbit of any integral band SCD, and
after multiplication by \(Q_m\), the flow \(f\) is the exact integral rotor
master.  The SCD marginal and circulation marginal are therefore separately
integrally decomposable.  What is missing is a **common** decomposition using
the same color on the SCD state and on its temporal rotor adjacencies.
Equation (3.5) contains no information about that synchronization.

For fixed target SCD colors, ownership alone is a product of Birkhoff
polytopes: occurrences of each state are bijected to the colors containing
that state.  The temporal reward couples two different factors of this
product, and the standard local temporal extension need not remain integral.

### Proposition 3.2 (a transition-augmented Birkhoff gap)

Consider the abstract directed cycle

\[
 X_0\to Y_0\to Z_0\to X_1\to Y_1\to Z_1\to X_0.
 \tag{3.6}
\]

There are two colors, and at each type \(X,Y,Z\), each color must be used once
among the two occurrences.  Every integral coloring has at least two
bichromatic arcs: both colors occur, and a nonconstant cyclic two-color word
has at least two changes.

In the standard fractional relaxation, put

\[
 x_{v,0}=x_{v,1}=\tfrac12
 \tag{3.7}
\]

at every occurrence and put \(y_{e,0}=y_{e,1}=\tfrac12\) on every arc, with
the usual constraints

\[
 y_{e,c}\le x_{u,c},\qquad y_{e,c}\le x_{v,c}
 \quad(e=uv).
 \tag{3.8}
\]

The relaxation declares every arc fully monochromatic, hence has zero switch
cost.  Its integral optimum is at least two.  This is an abstract LP
obstruction, not a rotor/SCD counterexample; it proves that typewise Birkhoff
plus local edge variables does not furnish the required integral selector.

## 4. Exact low-run pseudo-coloring from the odd cut

The preceding theorem is a no-escape result, but the odd-cut skeleton still
gives a useful exact reformulation of the unresolved selector.

Use a known exact odd wreath factor and cut at its distinguished coordinate.
This yields

\[
 B=\operatorname{Cat}_m=\frac{W}{m+1}
 \tag{4.1}
\]

vertex-disjoint complementary Johnson paths

\[
 P=(X_0,\ldots,X_m),\qquad X_m=X_0^c,
 \tag{4.2}
\]

which partition the middle layer.  Write

\[
 a_t=X_t\setminus X_{t+1},\qquad
 b_t=X_{t+1}\setminus X_t,
 \tag{4.3}
\]

and

\[
 w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1}).
 \tag{4.4}
\]

If \(I_w(t,k)\) denotes the cyclic interval of length \(k\) beginning at
position \(t\), then the radius-\(d\) state centered at \(X_t\) is

\[
 \omega_d(t)=
 \left(
 I_w(t+d,m-d);
 w_{t+d-1},\ldots,w_{t-d};
 I_w(t+m,m-d)
 \right).
 \tag{4.5}
\]

For \(d\ge1\), the move \(t\to t+1\) in a constant-radius segment is exactly
the rotor successor (1.2), with

\[
 x=w_{t+d},\qquad y=w_{t+m}.
 \tag{4.6}
\]

For \(d=0\), it is the ordinary swap (1.3).  Hence every constant-radius
segment of a cut path is a literal directed rotor path.

Concatenate the \(B\) paths and assign radius labels \(0,1,\ldots,H\) in
contiguous blocks of sizes \(\gamma_0,\ldots,\gamma_H\).  A block of
\(\gamma_d\) consecutive centers intersects at most

\[
 \frac{\gamma_d}{m+1}+2
 \tag{4.7}
\]

cut paths.  Therefore its radius-\(d\) states form a directed path forest with

\[
 p_d^0\le\frac{\gamma_d}{m+1}+2.
 \tag{4.8}
\]

The telescoping identity

\[
 \begin{aligned}
 U_H
 &:=\sum_{d=0}^H(2d+1)\gamma_d\\
 &=W+2\sum_{q=1}^HN_q
 \end{aligned}
 \tag{4.9}
\]

follows by writing \(2d+1=1+2\sum_{q=1}^d1\) and using (1.1).  Hence, for
\(H=\lceil A\sqrt m\rceil\) with fixed \(A\),

\[
 \begin{aligned}
 \Phi_{\rm cut}
 &:=\sum_{d=0}^H(2d+1)p_d^0\\
 &\le\frac{U_H}{m+1}+2\sum_{d=0}^H(2d+1)\\
 &=\frac{W+2\sum_{q=1}^HN_q}{m+1}+2(H+1)^2\\
 &\le\frac{(2H+1)W}{m+1}+2(H+1)^2\\
 &=O_A(W/\sqrt m)+O_A(m)=o(W).
 \end{aligned}
 \tag{4.10}
\]

The family just constructed is not asserted to be an SCD: its lower and
upper shadows can collide.  Call it one **pseudo-color**.  It nevertheless
contains \(\gamma_d\) distinct legitimate radius-\(d\) chain states and has
the exact required radius histogram.

### Theorem 4.1 (exact pseudo-orbit reduction)

Take \(s\) copies of the complete coordinate orbit of this pseudo-color.  The
resulting \(Q_m=s(2m)!\) pseudo-colors can be embedded into an exact chronology
of the entire band rotor master with total pseudo-color run toll

\[
 R_0\le Q_m\Phi_{\rm cut}=o(Q_mW).
 \tag{4.11}
\]

Furthermore, fix any full SCD \(\mathcal E\), write
\(\mathcal E^{(H)}=\operatorname{clip}_H(\mathcal E)\), and prescribe the
genuine target colors \((b,\sigma)\in[s]\times S_{2m}\), with target color
\((b,\sigma)\) carrying \(\operatorname{clip}_H(\sigma\mathcal E)\).
Recolorings of the same occurrence slots into this prescribed labeled orbit
of clipped exact SCDs are in bijection with independent statewise bijections

\[
 \pi_\omega:P_\omega\longrightarrow A_\omega,
 \tag{4.12}
\]

where \(P_\omega\) is the set of pseudo-occurrence slots having state
\(\omega\), and

\[
 A_\omega=
 \{(b,\sigma):\omega\in\operatorname{clip}_H(\sigma\mathcal E)\}.
 \tag{4.13}
\]

#### Proof

The orbit contains each state exactly \(s\gamma_dr!^2\) times.  The selected
pseudo-forest arcs use every directed rotor arc

\[
 s(\gamma_d-p_d^0)(r-1)!^2
 \tag{4.14}
\]

times.  The residual multiplicity is \(sp_d^0(r-1)!^2\) per arc.  The
connector pairing and balanced-macrograph argument in the proof of Theorem
2.1 therefore Eulerizes the residual arcs while keeping every pseudo-forest
path consecutive.  This proves (4.11).  Notice that the proof used the state
count and orbit transitivity, not the SCD ownership equations.

For the target orbit,

\[
 |A_\omega|=s\gamma_dr!^2=|P_\omega|.
 \tag{4.15}
\]

Choose a bijection (4.12) for each state and give a slot \(v\in P_\omega\)
the target color \(\pi_\omega(v)\).  If a target color \(c\) contains
\(\omega\), then \(c\in A_\omega\) and receives exactly one of the slots in
\(P_\omega\); if it does not contain \(\omega\), it receives none.  Hence
color \(c\) receives exactly the states of its prescribed SCD.  Conversely,
every recoloring into those prescribed target SCDs restricts at each state to
a bijection (4.12).  \(\square\)

For a fixed pseudo chronology, recoloring into this prescribed labeled target
orbit is therefore the following permutation-synchronization objective.
Arbitrary choices of \(Q_m\) target SCDs would add a separate integral
SCD-decomposition variable.  If \(u\to v\) is an internal chronological
adjacency, its switch contribution is

\[
 (2d+1)\,
 \mathbf 1\{\pi_{\omega(u)}(u)\ne\pi_{\omega(v)}(v)\}.
 \tag{4.16}
\]

One also adds \(2d+1\) at every hard sequence start.  The variables at one
state form a Birkhoff factor, but (4.16) couples different factors.  This is
the exact point at which the pseudo-colors must acquire common integral SCD
ownership.

### Proposition 4.2 (pair and long-path capacity obstructions)

For a state \(\omega\), let \(A_\omega\) be its set of admissible target
colors.  If a rotor arc \(e=(\omega,\omega')\) occurs \(a_e\) times among the
internal, non-cut adjacencies of a cut chronology, at most

\[
 B_e=|A_\omega\cap A_{\omega'}|
 \tag{4.17}
\]

copies can be monochromatic.  Indeed, an admissible common color has only one
slot of each state and can support at most one copy of that adjacency.  Thus,
if \(b_d\) is the number of hard radius-\(d\) sequences,

\[
 R_d\ge(2d+1)
 \left[b_d+\sum_e(a_e-B_e)_+\right].
 \tag{4.18}
\]

More generally, among \(k\) occurrence-disjoint copies of a labelled rotor
path \(P=(\omega_1,\ldots,\omega_t)\), at most

\[
 \left|\bigcap_{i=1}^tA_{\omega_i}\right|
 \tag{4.19}
\]

can remain wholly monochromatic.  If a state repeats in \(P\), none can,
because an exact SCD color contains that state only once.  Hence pair
capacities are merely the length-two shadows of the necessary long-range
intersection constraints.

## 5. Two stable repair criteria

The pseudo-orbit theorem permits massive recoloring; Hamming distance itself
is not the correct cost.  The following two deterministic inequalities isolate
repairs that would suffice.

### Lemma 5.1 (sparse repair)

Let \(\lambda_0\) be any coloring of a fixed cut chronology and let
\(\lambda\) be another coloring.  If the two colorings differ on \(E_d\)
radius-\(d\) slots, then

\[
 R(\lambda)
 \le R(\lambda_0)+2\sum_{d=0}^H(2d+1)E_d.
 \tag{5.1}
\]

#### Proof

Changing one slot can alter only the switch indicator on its predecessor and
successor adjacencies.  Each has weight \(2d+1\).  Hard-start charges do not
depend on the slot color.  Summing over changed slots, with possible double
counting only making the bound weaker, proves (5.1).  \(\square\)

Consequently, an exact SCD repair of the pseudo-orbit satisfying

\[
 \sum_d(2d+1)E_d=o(Q_mW)
 \tag{5.2}
\]

would solve the resolution problem.  The existence of such a repair is
**UNPROVED**.

### Lemma 5.2 (block-permutation stability)

Partition every cut chronological sequence into intervals.  Suppose that on
each interval \(B\),

\[
 \lambda(v)=\rho_B(\lambda_0(v))\qquad(v\in B),
 \tag{5.3}
\]

where \(\rho_B\) is a permutation of the full color palette.  Let
\(\partial\mathcal B\) be the set of chronological adjacencies crossing
between intervals.  Then

\[
 R(\lambda)
 \le R(\lambda_0)+
 \sum_{e\in\partial\mathcal B}(2d(e)+1).
 \tag{5.4}
\]

#### Proof

On an adjacency wholly inside one interval, a permutation preserves equality
and inequality of the two colors.  Only a boundary adjacency can acquire a
new switch, and its possible increase is at most its weight.  The hard starts
are unchanged.  This proves (5.4).  \(\square\)

Thus the following is a clean sufficient resolution target.

> **Block-permutation resolution lemma \(\mathrm{BPR}_A\) -- UNPROVED.**  On
> the pseudo chronology of Theorem 4.1, choose intervalwise palette
> permutations satisfying the exact statewise target constraints (4.12), with
> \[
> \sum_{e\in\partial\mathcal B}(2d(e)+1)=o(Q_mW).
> \]

If \(\mathrm{BPR}_A\) holds, (4.11) and (5.4) give a genuine SCD resolution
with \(o(Q_mW)\) run toll.  This target permits \(\Theta(Q_mW)\) slots to
change color; the useful structure is that a large recoloring is constant as
a palette permutation over long chronological blocks.

Theorem 2.1 shows that \(\mathrm{BPR}_A\), if true, must in particular produce
a low-\(\Phi_H\) target SCD.  It is therefore a concrete sufficient repair
lemma, not a proven weakening of the one-SCD structural gate.

## 6. A weaker multicover statement sufficient after averaging

Full saturation by all \(Q_m\) colors is unnecessary for the word bound.

### Proposition 6.1 (partial integral SCD path packing)

Suppose that, for some \(q_m\ge1\), there are full integral SCDs
\(\mathcal D_1,\ldots,\mathcal D_{q_m}\) and spanning directed rotor path
forests \(F_{i,d}\subseteq G_d[(\mathcal D_i)_d]\) such that

1. their selected state and arc occurrences fit injectively within the master
   type and arc capacities; unused master occurrences may be discarded; and
2. writing \(p_{i,d}=p(F_{i,d})\),
   \[
   \frac1{q_m}\sum_{i=1}^{q_m}\sum_{d=0}^H(2d+1)p_{i,d}=o(W).
   \tag{6.1}
   \]

Then one obtains a central-band word of length \(W+o(W)\).

#### Proof

Initialize every selected path separately and use the literal rotor
realization.  For color \(i\), (1.10) gives total length

\[
 W+\Phi_i,
 \qquad
 \Phi_i=\sum_{d=0}^H(2d+1)p_{i,d}.
 \tag{6.2}
\]

By (6.1), some \(i\) has \(\Phi_i=o(W)\).  Discard all other colors and all
unused master occurrences.  The resulting word has length \(W+o(W)\).
\(\square\)

The existence hypothesis of Proposition 6.1 is **UNPROVED**.  It is strictly
weaker as a multicover construction requirement than coloring all \(Q_mW\)
occurrences, because it permits arbitrary unused capacity and requires no
Eulerization of the remainder.  Existentially, however, its average contains
one good integral SCD atom, so it does not evade \(\mathrm{RSCD}_A\).

## 7. Exchange and mesoscopic obstructions

### Theorem 7.1 (exact two-color exchange components)

Let \(\mathcal D,\mathcal E\) be two full SCDs.  Form their bipartite ownership
overlay \(\Gamma(\mathcal D,\mathcal E)\): its left vertices are the chains of
\(\mathcal D\), its right vertices are the chains of \(\mathcal E\), and each
Boolean mask contributes an edge between its two owner chains.

Choose \(X\subseteq\mathcal D\) and \(Y\subseteq\mathcal E\), and exchange
these chain collections between the two colors.  Both resulting colors are
SCDs if and only if \(X\cup Y\) is a union of connected components of
\(\Gamma(\mathcal D,\mathcal E)\).

#### Proof

For an overlay edge joining \(D\in\mathcal D\) and \(E\in\mathcal E\), exact
coverage of its mask in the first new color is

\[
 1-\mathbf1_{D\in X}+\mathbf1_{E\in Y}=1.
 \tag{7.1}
\]

Thus

\[
 \mathbf1_{D\in X}=\mathbf1_{E\in Y}
 \tag{7.2}
\]

on every overlay edge.  Membership is therefore constant throughout every
connected component.  Conversely, if (7.2) holds on all edges, every mask is
owned exactly once in each new color.  \(\square\)

If the overlay is connected, the only exchanges are the empty exchange and
the full exchange, the latter merely renaming the colors.  Thus pairwise
local exchange cannot be a universal repair mechanism; useful exchanges need
disconnected overlays or genuinely higher-color trades.

There is also an exact all-start scale identity.  With prefix-extraction
weights \(\widehat\iota_d=2d\) for \(d<m\) and
\(\widehat\iota_m=2m-1\),

\[
 \sum_{d=0}^m\widehat\iota_dc_d=4^m-W-1.
 \tag{7.3a}
\]

Indeed, using \(c_d=N_d-N_{d+1}\),

\[
 \sum_{d=0}^{m-1}2d\,c_d+(2m-1)c_m
 =2\sum_{q=1}^mN_q-1=4^m-W-1.
\]

The conservative canonical-reset weights in \(\Phi_H\) instead give the
valid upper-ledger identity \(4^m-2\).  Since Stirling's
formula gives \(4^m/W\sim\sqrt{\pi m}\), a toll \(o(Q_mW)\) is an
\(o(m^{-1/2})\) fraction of the all-start weighted ledger.  Very high local
agreement is therefore necessary even before the ownership constraints are
considered.

### Theorem 7.2 (typical radii require mesoscopically long runs)

Fix \(0<a<b<A\), let \(H=\lceil A\sqrt m\rceil\), and suppose a full SCD
\(\mathcal D\) satisfies \(\Phi_H(\mathcal D)=o(W)\).  Then there is a sequence
\(K_m\to\infty\) such that all but \(o(W)\) of the chain states in an optimal
forest with

\[
 a\sqrt m\le d\le b\sqrt m
 \tag{7.3}
\]

belong to directed rotor runs of length at least \(K_m\sqrt m\).

#### Proof

Uniformly for \(d=O(\sqrt m)\),

\[
 \begin{aligned}
 \log\frac{N_d}{W}
 &=\sum_{j=1}^d
 \log\frac{m-j+1}{m+j}\\
 &=-\frac{d^2}{m}+O\!\left(\frac{d^3}{m^2}+\frac d m\right).
 \end{aligned}
 \tag{7.4}
\]

Indeed, expand
\(\log(1-(j-1)/m)-\log(1+j/m)\); its linear term is
\(-(2j-1)/m\), whose sum is \(-d^2/m\), and the quadratic remainders sum to
\(O(d^3/m^2)\).  Therefore the number \(M_I\) of chain states in the annulus
is

\[
 \begin{aligned}
 M_I
 &=N_{\lceil a\sqrt m\rceil}
   -N_{\lfloor b\sqrt m\rfloor+1}\\
 &=\bigl(e^{-a^2}-e^{-b^2}+o(1)\bigr)W
 =\Theta_{a,b}(W).
 \end{aligned}
 \tag{7.5}
\]

Let \(P_I\) be the total number of forest components at these radii.  Since
every relevant weight is at least \(2a\sqrt m+O(1)\),

\[
 P_I=o(W/\sqrt m).
 \tag{7.6}
\]

Choose \(K_m\to\infty\) slowly enough that

\[
 K_m\sqrt m\,P_I=o(W).
 \tag{7.7}
\]

All runs shorter than \(K_m\sqrt m\) together contain at most the left-hand
side of (7.7) states.  Equations (7.5)--(7.7) prove the claim.  \(\square\)

In particular, a construction whose splices or exact exchanges create only
\(O(\sqrt m)\)-length runs has toll \(\Omega(W)\), not \(o(W)\).  This is why
pairwise discrepancy or one-step capacity control is at the wrong correlation
scale.

## 8. Exact remaining lemma and the conditional OR estimate

For fixed \(A>0\), set \(H=\lceil A\sqrt m\rceil\).

> **Rotor path-forest lemma \(\mathrm{RSCD}_A\) -- UNPROVED.**  There exists a
> full integral SCD \(\mathcal D_{m,A}\) of \(B_{2m}\) such that, after
> clipping to radius \(H\),
> \[
> \boxed{
> \Phi_H(\mathcal D_{m,A})
> =\sum_{d=0}^H(2d+1)p_d^*(\mathcal D_{m,A})=o(W).
> }
> \tag{8.1}

This is the smallest unproved lemma for the exact integral rotor-coloring
lane.  The common SCD \(\mathcal D_{m,A}\) lies outside every depthwise
optimization; separate depthwise factors, fractional mixtures, and an
unextendible almost-matching do not satisfy (8.1).

By (1.9a), (8.1) is equivalent to the same statement with the exact prefix
toll \(\widehat\Phi_H\); the conservative weights are retained only because
they also pay the separate master-circuit initialization within a constant
factor.

If (8.1) holds, Theorem 2.1 constructs an exact color resolution with

\[
 Q_mW+O(Q_m\Phi_H)=Q_m(W+o(W))
 \tag{8.2}
\]

total extraction length, so averaging gives one central-band word of length
\(W+o(W)\).  Equivalently, initializing the optimal forest paths of the one
good SCD directly gives

\[
 W+\Phi_H=W+o(W).
 \tag{8.3}
\]

Combining (8.3) with the separately audited outer-tail word gives, for fixed
\(A\),

\[
 \limsup_{m\to\infty}
 \frac{\nu(2m)}{\binom{2m}{m}}
 \le1+O\bigl((1+A^2)e^{-A^2}\bigr).
 \tag{8.4}
\]

If \(\mathrm{RSCD}_A\) is proved for every fixed \(A\), letting
\(A\to\infty\) in (8.4) gives coefficient one in even dimension, and the
standard trimmed one-bit lift gives both parities.  This is a sufficient
rotor route.  It is not asserted to be necessary for overload MWB or for the
conjecture itself.

## 9. Adversarial audit

The strongest claim in this report is Theorem 2.1.  It survives the following
failure tests.

1. **Preselected forests.**  The lower bound uses the optimized quantity
   \(p_d^*(\mathcal D)\), not an arbitrary forest chosen before the coloring.
2. **Frozen chronology.**  The lower bound is valid for every chronology.  The
   upper bound constructs a chronology adapted to the chosen SCD orbit; no
   upper bound for an arbitrary frozen Euler tour is claimed.
3. **Cyclic runs.**  An abstract monochromatic Euler cycle is not a free
   zero-component forest.  Its physical cut is charged and turns it into one
   path.
4. **Literal realization.**  Abstract return need not restore the full MTF
   state.  Equation (2.10) keeps the physical initialization ledger separate
   and bounds it by a constant multiple of the run ledger.
5. **Exceptional radii.**  The exact equality is stated only for
   \(H\le m-2\).  The radius-\(m\) extraction weight is \(2m-1\), not
   \(2m+1\); using \(2m+1\) in Corollary 2.3 is explicitly only an upper
   bound.  The two exceptional classes cost \(O(m^2)=o(W)\) per color.
6. **Radius zero.**  The positive-radius rotor formula is not used at \(d=0\);
   the ordinary swap (1.3) is used.
7. **Pseudo-colors.**  Theorem 4.1 does not call the odd-cut pseudo-colors
   SCDs.  Their exact orbit counts prove an exact multicover statement, while
   (4.12) is the additional integral ownership requirement.
8. **Histograms versus ownership.**  Correct radius counts do not imply an
   SCD.  Already in \(B_2\), let
   \(L_i=(\varnothing,\{i\},\{1,2\})\) and
   \(S_i=(\{i\})\).  The colors \(\{L_1,S_2\}\) and
   \(\{L_2,S_1\}\) are SCDs, whereas the depthwise recoloring
   \(\{L_1,S_1\},\{L_2,S_2\}\) preserves one chain of each radius per
   color but neither color is an SCD.
9. **Fractional perfection.**  The zero defect in (3.5) is deliberately only
   fractional.  Proposition 3.2 exhibits an integrality gap as soon as
   temporal agreement is added.
10. **Long-range compatibility.**  Pair capacities (4.17) do not control the
    common intersections (4.19).  Theorem 7.2 proves that successful typical-
    radius runs must be longer than every fixed multiple of \(\sqrt m\) on
    all but \(o(W)\) states.
11. **Logical scope.**  Theorem 2.1 identifies the exact gate for the full
    integral rotor-coloring lane.  It does not identify a necessary condition
    for the separate overload-MWB route, and no converse from unlabelled
    histogram balance to common labelled SCD ownership is used.

Accordingly, the clean obstruction is now exact: the SCD ownership polytope
and the rotor-circulation polytope have relevant symmetric marginals that
each admit fractional and integral decompositions separately, but those
decompositions do not presently synchronize into common colors with
mesoscopically long monochromatic rotor runs.  The smallest replacement lemma
is \(\mathrm{RSCD}_A\), or,
constructionally, the partial capacity-respecting integral packing in
Proposition 6.1.  Both remain unproved.
