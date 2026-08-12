# Pair-stratum census, the fixed-frame obstruction, and the multiframe rotor gate

Date: 2026-07-25

This note continues `ROTOR_SCD_PARITY_CHECK_CYCLE_TILING_20260725.md`,
especially Theorem 4.1.  It answers the next question in three parts.

1.  The split/full/empty census forced by a fixed-pair rotor realization of
    one Boolean SCD is exact and elementary.
2.  That census gives a positive Gaussian capacity deficit in every single
    coordinate-pair frame.  Consequently the nonlinear two-sided-rainbow
    factors of Theorem 4.1 cannot be glued inside one fixed frame with
    (o(W)) **weighted** run-start toll.
3.  Mixing coordinate frames removes this obstruction at the exact
    fractional level.  Coordinate conjugates of the nonlinear cycles give
    both an exact fractional band SCD and a weaker fractional direct-compiler
    cover with toll \(O(HW/\ell)=o(W)\).  For coefficient one, the primary
    remaining gate is the weaker \(\mathrm{MFUP}_A\) rounding problem:
    exact middle-owner partition, aggregate shadow holes \(o(W)\), and
    useful-prefix bridge excess \(o(W)\).  Exact mask-disjoint SCD ownership
    is sufficient but unnecessary.  The intermediate decorated-SCD gate
    \((\mathrm{EP}_A)\) asks for a bridge-one path cover with
    \(o(W/H)\) components; its rigid tag-\(H\) class contains an explicit
    induced matching obstruction derived in Section 7.

Throughout,

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad N_{m+1}=0.
\tag{0.1}
\]

For a band \(0\le q\le H\), put

\[
 c_d=N_d-N_{d+1}\quad(0\le d<H),\qquad c_H=N_H.
\tag{0.2}
\]

Thus an SCD clipped at depth \(H\) has exactly \(c_d\) middle owners of
clipped radius \(d\), and

\[
 \sum_{d=q}^Hc_d=N_q.
\tag{0.3}
\]

The conservative rotor component toll is

\[
 \Phi=\sum_{d=0}^H(2d+1)p_d
     =P_0+2\sum_{q=1}^HP_q,
 \qquad P_q=\sum_{d=q}^Hp_d,
\tag{0.4}
\]

where \(p_d\) is the number of radius-\(d\) path components.  The hard-prefix
version replaces \(2d+1\) by \(2d\); both have the same \(o(W)\) threshold.

## 1. Exact split/full/empty census

Fix a perfect matching

\[
 \mathcal P=\{P_1,\ldots,P_m\}
\tag{1.1}
\]

of the \(2m\) Boolean coordinates.  A middle mask has

\[
 f\text{ full pairs},\qquad f\text{ empty pairs},\qquad
 s=m-2f\text{ split pairs}.
\tag{1.2}
\]

After the full, empty, and split index sets are fixed, the orientations of
the split pairs form a cube \(Q_s\).  The number of all middle masks of type
\(f\) is

\[
 \boxed{
 V_f=\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.}
\tag{1.3}
\]

A rank-\(m-q\) mask of lower type \(f\) has

\[
 f\text{ full},\qquad f+q\text{ empty},\qquad
 m-2f-q\text{ split pairs},
\tag{1.4}
\]

and hence the exact number of such masks is

\[
 \boxed{
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.}
\tag{1.5}
\]

By complementation, \(T_{f,q}\) also counts rank-\(m+q\) masks with \(f\)
empty, \(f+q\) full, and \(m-2f-q\) split pairs.  In particular,

\[
 \sum_fV_f=W,\qquad \sum_fT_{f,q}=N_q.
\tag{1.6}
\]

The following is the exact pair-stratum census relevant to Theorem 4.1.

### Theorem 1.1 (forced fixed-frame census)

Suppose a clipped Boolean SCD is realized in the frame \(\mathcal P\) in
the following strong sense: whenever a middle owner has radius at least
\(q\), its depth-\(q\) lower member is obtained by making \(q\) of its split
pairs empty, and its depth-\(q\) upper member is obtained by making \(q\) of
its split pairs full.  Then for every \(f,q\),

\[
 \boxed{
 \#\{\text{type-}f\text{ owners of radius at least }q\}=T_{f,q}.}
\tag{1.7}
\]

Consequently the number of type-(f) owners of exact clipped radius (d)
would have to be

\[
 T_{f,d}-T_{f,d+1}\quad(d<H),\qquad T_{f,H}\quad(d=H).
\tag{1.8}
\]

#### Proof

A pair-flip lower shadow never changes a full pair.  It sends a type-\(f\)
middle owner to a rank-\(m-q\) mask having exactly the pair data in (1.4).
Because an SCD contains every rank-\(m-q\) mask exactly once, this map from
the active type-\(f\) owners must be a bijection onto the \(T_{f,q}\) masks
of lower type \(f\).  This proves (1.7).  Subtract consecutive nested
counts to obtain (1.8).  The upper census is the complementary copy of the
same argument. \(\square\)

There is also a fine, labelled version.  Let \(F,E\subseteq[m]\) be disjoint,

\[
 |F|=f,\qquad |E|=f+q,
\tag{1.9}
\]

and fix an orientation \(\eta\) on the remaining \(m-2f-q\) split pairs.
The lower target \((F,E,\eta)\) has candidate source strata

\[
 (F,E\setminus D),\qquad D\in\binom Eq,
\tag{1.10}
\]

and two orientations on every pair in \(D\).  Exact ownership says that
among all those candidates exactly one active owner has forward deletion
set \(D\) and residual orientation \(\eta\).  Dually, every upper target has
exactly one reverse-deletion owner.  These are the cross-stratum equations
which are absent from the intrastatum injectivity in Theorem 4.1.

### Corollary 1.2 (literal fixed-frame gluing is impossible)

For the counts in (1.7) to be nested, it is necessary that
\(T_{f,q+1}\le T_{f,q}\).  But

\[
 \boxed{
 \frac{T_{f,q+1}}{T_{f,q}}
 =\frac{m-2f-q}{2(f+q+1)}.}
\tag{1.11}
\]

Thus \(T_{f,q+1}>T_{f,q}\) whenever

\[
 m-4f-3q-2>0.
\tag{1.12}
\]

In particular, for (m>2), no exact Boolean SCD can have all of its
positive-depth flags realized by pair flips in one fixed frame.

#### Proof

The active-owner sets ({r\ge q}) are nested in (q), so their counts
cannot increase.  Formula (1.11) follows directly from (1.5).  Taking
\(f=q=0\) gives \(T_{0,1}/T_{0,0}=m/2>1\). \(\square\)

This finite obstruction does not yet imply a linear toll: the offending
small-(f) types at bounded (q) can have small total mass.  The Gaussian
form below is the quantitative obstruction relevant to coefficient one.

## 2. The Gaussian fixed-frame deficit

Define the positive type-capacity deficit

\[
 \boxed{
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.}
\tag{2.1}
\]

It has two equivalent meanings.  It is the number of lower targets that
cannot be supplied even if every type-(f) middle owner is used once as a
pure fixed-frame depth-(q) start; and it is the amount by which the forced
census (1.7) exceeds the available middle census (1.3).

### Theorem 2.1 (fixed-frame run-boundary inequality)

Let one exact clipped SCD be equipped, in every radius class, with a
spanning rotor path forest all of whose selected arcs flip pairs of the same
global frame \(\mathcal P\).  Then for every (1\le q\le H),

\[
 \boxed{qP_q\ge D_{m,q}.}
\tag{2.2}
\]

More generally, if (s_q) selected arcs among radii (d\ge q) are not
\(\mathcal P\)-pair flips, then

\[
 \boxed{q(P_q+s_q)\ge D_{m,q}.}
\tag{2.3}
\]

#### Proof

There are (N_q) active radius-(ge q) owners.  A path component on (t)
owners contains ((t-q)_+ge t-q) starts followed by (q) selected arcs.
Consequently all the forests together contain at least

\[
 N_q-qP_q
\tag{2.4}
\]

pure length-(q) starts.  Such a window empties (q) distinct split pairs
of \(\mathcal P\), so it preserves the source full-pair count (f).  Its
lower mask is distinct from that of every other start because all lower
members belong to one SCD.  Type (f) can therefore contribute at most

\[
 \min\{V_f,T_{f,q}\}
\tag{2.5}
\]

starts.  Summing (2.5) gives (N_q-D_{m,q}); comparison with (2.4) proves
(2.2).

An exceptional arc belongs to at most (q) length-(q) windows.  Deleting
all windows containing one of the (s_q) exceptional arcs leaves at least
(N_q-qP_q-qs_q) pure starts.  The same count proves (2.3). \(\square\)

For completeness, the deficit has an explicit Gaussian limit.  Let
(\Phi_{\rm G}) be the standard normal distribution function and put

\[
 \Delta(x)=\Phi_{\rm G}(x/2)
 -e^{x^2}\Phi_{\rm G}(-3x/2).
\tag{2.6}
\]

### Theorem 2.2 (positive Gaussian capacity deficit)

If (q=x\sqrt m+o(\sqrt m)), with (x>0) fixed, then

\[
 \boxed{
 \frac{D_{m,q}}W\longrightarrow
 e^{-x^2}\Delta(x)>0.}
\tag{2.7}
\]

The convergence is uniform when (x) ranges over a fixed compact
subinterval of ((0,\infty)).

#### Proof

Under the source weights (V_f/W),

\[
 X_m=\frac{f-m/4}{\sqrt m}
 \Longrightarrow N(0,1/16).
\tag{2.8}
\]

Under the target weights (T_{f,q}/N_q), the corresponding limit is

\[
 X_m\Longrightarrow N(-x/2,1/16).
\tag{2.9}
\]

Both statements, uniformly for bounded (X_m) and compact (x)-ranges,
follow by applying Stirling's formula with uniform remainder to (1.3) and
(1.5).  The exact likelihood ratio is

\[
 \frac{T_{f,q}}{V_f}
 =\prod_{i=0}^{q-1}
 \frac{m-2f-i}{2(f+1+i)}.
\tag{2.10}
\]

For bounded (X_m), its logarithm is

\[
 \log\frac{T_{f,q}}{V_f}
 =-8xX_m-3x^2+o(1),
\tag{2.11}
\]

uniformly on the same compact ranges.  Since (2.10) decreases in (f), it
crosses one at

\[
 X_m=-3x/8+o(1).
\tag{2.12}
\]

Finally (N_q/W\to e^{-x^2}).  Splitting the positive part at (2.12) and
using (2.8)--(2.9) yields

\[
 \begin{aligned}
 \frac{D_{m,q}}W
 &\longrightarrow
 e^{-x^2}\Phi_{\rm G}(x/2)-\Phi_{\rm G}(-3x/2)\\
 &=e^{-x^2}\Delta(x).
 \end{aligned}
\tag{2.13}
\]

Strict positivity follows already from the fact that the two limiting
measures are distinct and (2.1) is their positive total-variation part;
it also follows directly from (2.6). \(\square\)

### Corollary 2.3 (exact obstruction to one-frame coefficient one)

Let (H=\lceil A\sqrt m\rceil), where (A>0) is fixed.  Every pure
fixed-frame construction in Theorem 2.1 satisfies

\[
 \boxed{
 \liminf_{m\to\infty}\frac{\Phi}{W}
 \ge\kappa_A,
 \qquad
 \kappa_A=2\int_0^A
 \frac{e^{-x^2}\Delta(x)}x\,dx>0.}
\tag{2.14}
\]

Hence the nonlinear orientation-cube factors of Theorem 4.1 cannot be
glued, inside one global coordinate matching, into one SCD with (o(W))
weighted run-start toll.

#### Proof

By (0.4) and (2.2),

\[
 \Phi\ge2\sum_{q=1}^H\frac{D_{m,q}}q.
\tag{2.15}
\]

First sum over (a\sqrt m\le q\le A\sqrt m), use the compact-uniform form
of (2.7), and pass to a Riemann integral.  Then let (a\downarrow0).  The
integrand has finite positive limit (sqrt{2/\pi}) at zero. \(\square\)

There is an important scope distinction.  At one Gaussian depth,
(2.2) gives only

\[
 P_q=\Omega_A(W/\sqrt m)=o(W).
\tag{2.16}
\]

Thus the theorem does **not** rule out (o(W)) unweighted components.  It
rules out the (o(W)) radius-weighted toll required by the constant-one
rotor--SCD route.  Likewise, (2.3) shows that a low-toll repair must use

\[
 s_q=\Omega_A(W/\sqrt m)
\tag{2.17}
\]

off-frame arcs, contaminating (Omega_A(W)) Gaussian depth-(q) starts.
This is exactly why owner-dependent or phase-changing coordinate frames are
mandatory.  If each such arc incurred a fresh (\Theta(H)) initialization,
(2.17) would again cost (Omega_A(W)); the changes must instead be
entry-neutral, or be grouped into long differently framed packets.

## 3. Entry-neutral sliding frames are locally possible

The fixed-frame obstruction does not imply that changing a frame must
change the physical word.  The following elementary lemma separates the
certificate from the chronology.

### Lemma 3.1 (sliding matching-frame lemma)

Let (e_0,e_1,\ldots) be two-element coordinate supports such that every

\[
 M_t=\{e_t,e_{t+1},\ldots,e_{t+H-1}\}
\tag{3.1}
\]

is a matching.  There are perfect matchings \(\mathcal P_t\) of the (2m)
coordinates satisfying

\[
 M_t\subseteq\mathcal P_t
\tag{3.2}
\]

and such that \(\mathcal P_{t+1}\) is obtained from \(\mathcal P_t\) by at
most one matching two-switch.  In particular,

\[
 |\mathcal P_t\mathbin\triangle\mathcal P_{t+1}|\le4.
\tag{3.3}
\]

#### Proof

Extend (M_0) arbitrarily to \(\mathcal P_0\).  Suppose \(\mathcal P_t\)
has been chosen.  The common live matching

\[
 \{e_{t+1},\ldots,e_{t+H-1}\}
\tag{3.4}
\]

already lies in \(\mathcal P_t\), and the new edge (e_{t+H}=\{u,v\}) is
disjoint from it.  If (uv\in\mathcal P_t), keep the frame.  Otherwise
\(\mathcal P_t\) contains edges (uu') and (vv'), neither belonging to
(3.4).  Replace them by (uv) and (u'v').  This preserves (3.4), inserts
the new live edge, and changes four matching edges in the symmetric
difference. \(\square\)

The frames in Lemma 3.1 are certificates for the same physical transition
sequence; changing the unused completion pairs costs no word entry.  This
does not construct an SCD, because the lower and upper masks must still be
owned exactly once.  It does show that a universal positive interface toll
cannot be deduced merely from the fact that the certifying pair frame moves.

### 3.2 Exact path-hitting form of shadow ownership

The cross-frame ownership condition is most transparent as a Johnson
up-set hitting problem.  Let \(X_0,X_1,\ldots\) be a factor cycle in the
middle Johnson graph and, for a rank-\(m-q\) target \(T\), put

\[
 \mathcal U_T
 =\left\{X\in\binom{[n]}m:T\subseteq X\right\}.
\tag{3.5}
\]

Suppose a consecutive segment \(X_j,\ldots,X_{j+q}\) is geodesic.  Thus its
\(q\) transitions delete \(q\) distinct coordinates of \(X_j\) and insert
\(q\) distinct coordinates outside \(X_j\).  Then

\[
 \left|\bigcap_{a=0}^qX_{j+a}\right|=m-q.
\tag{3.6}
\]

Consequently

\[
 \boxed{
 \bigcap_{a=0}^qX_{j+a}=T
 \quad\Longleftrightarrow\quad
 X_j,\ldots,X_{j+q}\in\mathcal U_T.}
\tag{3.7}
\]

Thus a lower target is covered at depth \(q\) exactly when one selected
factor cycle has a consecutive \((q+1)\)-vertex Johnson path wholly inside
its up-set.  Exact SCD ownership requires exactly one such active path for
every target.

For the usual odd wreath convention, take \(n=2m+1\) and

\[
 X_j=I_\pi(j,m).
\tag{3.8}
\]

Directly,

\[
 \bigcap_{a=0}^qX_{j+a}=I_\pi(j+q,m-q),
 \qquad
 \bigcup_{a=0}^qX_{j+a}=I_\pi(j,m+q).
\tag{3.9}
\]

Complementation has the shifted rank identity

\[
 (2m+1)-(m+q)=m-(q-1).
\tag{3.10}
\]

Hence, in this odd convention, upper depth \(q\) is the complemented lower
depth \(q-1\) condition.  The shift must not be suppressed.  In the even
\(n=2m\) band-SCD convention used in Sections 1--2 and 4--6, rank \(m+q\)
instead complements rank \(m-q\), so the numerical depths agree.

For an \(F_\ell\)-cycle, Theorem 4.1 says precisely that the paths in
(3.7) hit no lower up-set twice through \(q\le\ell/2\), and the reverse
paths give the corresponding upper injectivity.  What it does not say is
that the paths from different coordinate-conjugated cycles hit every up-set
exactly once.  That is the integral multiframe gate below.

## 4. Nonlinear cycle atoms

Let \(\ell\) be a power of two with

\[
 2H\le\ell\le m.
\tag{4.1}
\]

Choose a perfect coordinate matching, take \(\ell\) of its pairs as active,
and fix one orientation on every other pair.  A cycle of (F_\ell) from
Theorem 4.1 has (2\ell) middle masks and transition word (\pi\pi).

For a cycle vertex (x), let (L_q(x)) be the mask obtained by making the
next (q) transition pairs empty, and let (U_q(x)) be the mask obtained
by making the previous (q) transition pairs full.  For (0\le d\le H),
define

\[
 \mathcal C_d(x):
 L_d(x)\subset\cdots\subset L_1(x)\subset x
 \subset U_1(x)\subset\cdots\subset U_d(x).
\tag{4.2}
\]

### Proposition 4.1 (nonlinear cycle atom)

For fixed (d\le H), the (2\ell) chains

\[
 \{\mathcal C_d(x):x\text{ on one }F_\ell\text{-cycle}\}
\tag{4.3}
\]

are saturated symmetric chain segments and are pairwise mask-disjoint.
Their middle owners form one radius-(d) rotor cycle.  Call (4.3) a
radius-(d) nonlinear cycle atom.

#### Proof

The next (d) and previous (d) transition directions are disjoint because
the transition word is (\pi\pi) and (2d\le\ell).  Therefore (4.2) adds
one new Boolean coordinate at every step and is a saturated chain from rank
(m-d) to rank (m+d).

At every lower depth \(q\le d\), Theorem 4.1 says that
\(x\mapsto L_q(x)\)
is injective on the entire orientation cube; its restriction to this cycle
is injective.  The reverse statement gives injectivity of
\(x\mapsto U_q(x)\).  Different depths lie at different ranks.  Hence all
segments in (4.3) are pairwise mask-disjoint.  The transition word
(\pi\pi) is exactly the pair-flip rotor chronology, up to reversing the
chosen orientation of the cycle. \(\square\)

The atom uses one fixed pair frame internally, but its arbitrary coordinate
conjugates use different frames.  This is the basic multiframe packet.

## 5. Exact fractional multiframe gluing

Let \(\Omega_d\) be the set of distinct images of one radius-(d) atom under
the full coordinate permutation group \(S_{2m}\).  The group is transitive
on every Boolean rank.

### Theorem 5.1 (exact fractional multiframe band SCD)

Assign every atom in \(\Omega_d\) the common weight

\[
 \boxed{
 \alpha_d=\frac{c_d}{2\ell\,|\Omega_d|}.}
\tag{5.1}
\]

Then every Boolean mask at every rank (m-H,\ldots,m+H) has total incident
weight exactly one.  The weighted number of middle owners assigned radius
(d) is exactly (c_d).  Thus (5.1) is an exact fractional decomposition
of the central band into nonlinear two-sided-rainbow cycle atoms with the
radius census of one Boolean SCD.

Its fractional component counts and conservative toll are

\[
 p_d^{\rm frac}=\frac{c_d}{2\ell},
\tag{5.2}
\]

\[
 \boxed{
 \Phi_{\rm frac}
 =\frac1{2\ell}\sum_{d=0}^H(2d+1)c_d
 =\frac{W+2\sum_{q=1}^HN_q}{2\ell}.}
\tag{5.3}
\]

The exact hard-prefix toll is

\[
 \boxed{
 \widehat\Phi_{\rm frac}
 =\frac1\ell\sum_{q=1}^HN_q.}
\tag{5.4}
\]

In particular, if

\[
 H/\ell\longrightarrow0,
\tag{5.5}
\]

then both tolls are (o(W)).

#### Proof

Fix (q\le H) and one lower mask (Y) of rank (m-q).  In every
radius-(d) atom with (d\ge q), exactly (2\ell) lower masks occur at
that rank.  Coordinate transitivity implies that the total incidence weight
at (Y) is independent of (Y).  The total weighted number of lower
incidences at rank (m-q) is

\[
 \sum_{d=q}^H
 |\Omega_d|\alpha_d(2\ell)
 =\sum_{d=q}^Hc_d=N_q.
\tag{5.6}
\]

There are (N_q) masks at that rank, so every one has weight one.  The same
argument applies to the upper rank.  At (q=0), it says that every middle
mask has total weight one, while (5.1) assigns total radius-(d) owner
weight (c_d).

Equivalently, by (3.7), the weighted number of active consecutive
\((q+1)\)-vertex paths contained in \(\mathcal U_T\) is exactly one for
every lower target \(T\).  In the odd wreath indexing, the complemented
lower-\((q-1)\) statement gives the upper depth-\(q\) equation.

Every atom is one rotor cycle and becomes one path component after one cut,
which proves (5.2).  Finally,

\[
 \sum_{d=0}^Hc_d=W,
 \qquad
 \sum_{d=0}^Hdc_d=\sum_{q=1}^HN_q.
\tag{5.7}
\]

Substitution gives (5.3)--(5.4), and (N_q\le W) gives the conclusion under
(5.5). \(\square\)

For the coefficient-one Gaussian window (H=A\sqrt m+O(1)), one may take a
power of two

\[
 m^{3/4}\le\ell<2m^{3/4}.
\tag{5.8}
\]

Then

\[
 \Phi_{\rm frac}=O_A(Wm^{-1/4})=o(W).
\tag{5.9}
\]

This theorem is the precise positive answer to the pair-stratum counting
question.  Once frames are mixed, neither the SCD radius census nor the
cost of one interface per long nonlinear packet forces linear loss.  The
single-frame deficit is averaged away by genuine coordinate conjugacy, not
by changing only the order of pairs inside the old frame.

## 6. The exact integral gate

Theorem 5.1 is fractional.  Orbit averaging does not by itself select
pairwise mask-disjoint atoms, and divisibility already prevents an exact
decomposition using only equal (2\ell)-owner atoms in every radius class.
The correct integral target must allow a vanishing residual family.

### Theorem 6.1 (integral packet criterion)

Assume (H=o(\ell)), and suppose there is a collection \(\mathfrak C\) of
coordinate-conjugated nonlinear cycle atoms such that:

1. the atoms in \(\mathfrak C\) are pairwise mask-disjoint;
2. their complement in the central band has a symmetric-chain
   decomposition \(\mathfrak R\);
3. \(\mathfrak R\) has (R=o(W/H)) middle owners; and
4. the union \(\mathfrak C\cup\mathfrak R\) has the exact clipped radius
   counts (c_d).

Then the central band is one integral SCD with a radiuswise rotor path
forest of conservative toll (o(W)).  It extends to a full Boolean SCD.

#### Proof

The nonlinear atoms contribute at most (W/(2\ell)) rotor components.
Charging the maximum conservative weight (2H+1) to each gives

\[
 O(HW/\ell)=o(W).
\tag{6.1}
\]

Use every residual chain as a singleton rotor component.  Its toll is at
most (2H+1), so the residual contribution is

\[
 O(HR)=o(W).
\tag{6.2}
\]

The four hypotheses make the union an exact saturated symmetric-chain
decomposition of the band with counts (0.2).  The standard band-extension
theorem extends it to a full SCD while preserving every band chain as a
contiguous segment. \(\square\)

Thus the remaining theorem is concrete.

> **Multiframe nonlinear-atom rounding gate.**  Round the symmetric
> fractional decomposition of Theorem 5.1 to pairwise mask-disjoint
> coordinate-conjugated atoms leaving an SCD-decomposable residual of
> (o(W/H)) middle owners.

This is stronger than a near-perfect matching on middle owners.  Lower and
upper masks at every depth must be disjoint simultaneously, and the small
residual must itself retain the rank-by-rank symmetric-chain structure.
Theorem 4.1 supplies all intrapacket injectivity; the rounding gate contains
exactly the remaining interpacket ownership constraints.  In the
path-hitting language, the selected cycles must hit every relevant Johnson
up-set exactly once, apart from the \(o(W/H)\)-owner residual.

The exact SCD criterion is sufficient but stronger than the direct literal
compiler requires.  The correct weaker target is the
\(\mathrm{MFUP}_A\) gate from
MATH_ATTACK_ORIENTATION_CUBE_DIRECT_LITERALIZATION_INTERFACE_TOLL_20260725.md.

### Theorem 6.2 (exact fractional MFUP atom cover)

Fix one radius-\(H\) nonlinear cycle atom \(\mathcal A_H\), and let
\(\Omega_H\) be its full \(S_{2m}\)-orbit.  Give every orbit atom weight

\[
 \boxed{
 \beta=\frac{W}{2\ell\,|\Omega_H|}.}
\tag{6.3}
\]

Then:

1. every middle owner has total incident weight exactly one;
2. every lower and every upper target at depth \(q\le H\) has total
   incident weight exactly
   \[
     \boxed{\frac{W}{N_q}=\rho_q^{-1}\ge1;}
     \tag{6.4}
   \]
3. the total fractional number of cycle pieces is \(W/(2\ell)\), so
   independent useful-prefix initialization has excess at most
   \[
     \boxed{\frac{HW}{\ell}=o(W)}
     \tag{6.5}
   \]
   whenever \(H/\ell\to0\).

Thus the mixed-frame orbit has an exact fractional \(\mathrm{MFUP}_A\)
solution with positive coverage slack at every noncentral rank.

#### Proof

Coordinate transitivity makes the middle incidence independent of the
owner.  The total weighted middle incidence is

\[
 |\Omega_H|\beta(2\ell)=W,
\tag{6.6}
\]

so every one of the \(W\) owners has degree one.

At depth \(q\), every atom contributes \(2\ell\) lower flags and
\(2\ell\) upper flags.  Theorem 4.1 makes each of those two lists
internally injective.  Transitivity on the rank-\((m-q)\) and rank-\((m+q)\)
layers therefore gives the common degree

\[
 \frac{|\Omega_H|\beta(2\ell)}{N_q}
 =\frac{W}{N_q}.
\tag{6.7}
\]

Finally, the total atom weight is \(W/(2\ell)\).  The exact useful-prefix
bridge theorem gives bridge excess at most \(2H\) per independently
initialized piece, proving (6.5). \(\square\)

Theorem 6.2 is strictly closer to the direct compiler than Theorem 5.1.
The latter fractionally assigns the exact SCD radius census and load one at
every rank.  The former keeps every owner active through depth \(H\), allows
the unavoidable load \(W/N_q>1\), and asks only for support after integral
rounding.

### Proposition 6.3 (exact hole--duplicate identity)

Let legal mixed-frame pieces partition all \(W\) middle owners.  At one
lower depth \(q\), let \(L_q^-(T)\) be the number of owners whose advertised
lower flag is \(T\), let

\[
 M_q^-=\#\{T:L_q^-(T)=0\},
 \qquad
 R_q^-=\sum_T(L_q^-(T)-1)_+.
\tag{6.8}
\]

Then

\[
 \boxed{M_q^-=R_q^--(W-N_q).}
\tag{6.9}
\]

The same identity holds for the upper loads.  Consequently

\[
 \sum_{q\le H}(M_q^-+M_q^+)=o(W)
\tag{6.10}
\]

is equivalent to saying that the aggregate cross-piece duplicate excess is
only \(o(W)\) above the unavoidable surplus

\[
 2\sum_{q\le H}(W-N_q).
\tag{6.11}
\]

#### Proof

Every owner advertises one lower depth-\(q\) flag, so
\(\sum_TL_q^-(T)=W\).  Splitting targets into zero, unit, and overloaded
loads gives

\[
 W-N_q
 =\sum_T(L_q^-(T)-1)
 =R_q^--M_q^-.
\tag{6.12}
\]

Rearrange.  The upper proof is identical. \(\square\)

Proposition 6.3 is the useful weakening of exact SCD ownership.  Shadow
collisions are permitted, including collisions between different depths
and different pair frames.  Only duplicate mass beyond the forced surplus
creates literal repair cost.

### Theorem 6.4 (MFUP atom-rounding criterion)

Assume \(H=o(\ell)\).  Suppose one can select radius-\(H\) nonlinear cycle
atoms, allowing a different coordinate frame for every atom, together with
legal residual pieces, so that:

1. their middle owners form an exact partition of the middle layer;
2. their total number of pieces is
   \[
     C=O(W/\ell)+o(W/H);
     \tag{6.13}
   \]
3. their lower and upper loads satisfy (6.10).

Then \(\mathrm{MFUP}_A\) holds.  In particular the pieces may be ordered
arbitrarily; no special phase-ordering theorem is needed.

#### Proof

The useful-prefix bridge length always satisfies \(b_j\le2H+1\).  Therefore

\[
 \sum_{j<C}(b_j-1)\le2HC
 =O(HW/\ell)+o(W)=o(W).
\tag{6.14}
\]

Hypothesis 1 is the exact middle-owner clause of \(\mathrm{MFUP}_A\), and
hypothesis 3 is its aggregate shadow-hole clause.  Equation (6.14) supplies
the useful-prefix clause.  Apply the direct phase compiler. \(\square\)

The remaining direct-compiler problem can therefore be stated without SCD
language:

> **MFUP atom rounding gate.**  Round the symmetric fractional atom cover
> of Theorem 6.2 to an exact middle-owner partition satisfying the
> near-minimal aggregate duplicate condition (6.10), using
> \(O(W/\ell)+o(W/H)\) pieces.

This is weaker than the band-SCD gate in Theorem 6.1 in three independent
ways: targets may repeat, targets at different depths need not lie in a
common chain, and the residual need not be SCD-decomposable.

There is nevertheless a real annealed-to-quenched obstruction.  The orbit
average in Theorem 6.2 can be decomposed into conjugates of exact
fixed-frame owner resolutions, but every one such constituent has the
positive Gaussian hole deficit of Section 2.  Selecting one constituent of
that convex combination therefore cannot prove \(\mathrm{MFUP}_A\).
Atoms from different resolutions must be recombined integrally while
preserving exact owner degree one.  Weighted degrees and pair-codegrees
alone do not supply that recombination when the atom size \(2\ell\) grows;
the resolvable necklace geometry must be used.

### Proposition 6.5 (two-resolution all-or-nothing law)

Let \(\mathcal F\) and \(\mathcal G\) be two exact partitions of the middle
owners into whole atoms.  Form the bipartite multigraph \(B(\mathcal F,
\mathcal G)\) with vertex classes \(\mathcal F,\mathcal G\), and with one
edge \(e_X\) for every middle owner \(X\), joining the two atoms which
contain \(X\).

Suppose \(\mathcal H\subseteq\mathcal F\cup\mathcal G\) is an exact owner
partition made by selecting whole atoms from the two resolutions.  Then on
every connected component of \(B(\mathcal F,\mathcal G)\), either
\(\mathcal H\) contains every \(\mathcal F\)-atom and no
\(\mathcal G\)-atom, or it contains every \(\mathcal G\)-atom and no
\(\mathcal F\)-atom.

In particular, if \(B(\mathcal F,\mathcal G)\) is connected, the only exact
whole-atom owner partitions in their union are \(\mathcal F\) and
\(\mathcal G\) themselves.

#### Proof

Give each atom \(A\in\mathcal F\cup\mathcal G\) a selection variable
\(z_A\in\{0,1\}\).  Exact coverage of the owner corresponding to an edge
\(FG\) is the equation

\[
 z_F+z_G=1.
\tag{6.15}
\]

Along a connected bipartite component, these equations force one common
value on all left variables and its complement on all right variables.
There are exactly the two stated choices. \(\square\)

Proposition 6.5 explains why sampling a convex combination or splicing two
resolvable factors atom by atom is not a rounding theorem.  A successful
\(\mathrm{MFUP}_A\) proof must instead use higher-order trades among several
resolutions, deliberately create many useful intersection components, or
cut atoms into legal subsegments.  Any cutting scheme must retain the piece
bound (6.13); otherwise the useful-prefix reset term becomes linear.

## 7. The decorated-SCD bridge-one gate

The exact two-resolution theorem in
ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md gives a second route which
sits between the exact atom-SCD gate and \(\mathrm{MFUP}_A\).

Fix a clipped SCD \(\mathcal D\).  If an owner \(X\) has clipped tag
\(d\), choose one radius-\(H\) collar extension of its tagged state and
write the resulting useful state as

\[
 \widetilde\omega_X
 =(L_X;z^X_1,\ldots,z^X_{2H};R_X).
\tag{7.1}
\]

The collection is a decorated SCD \(\widetilde{\mathcal D}\).  Let
\(\mathcal B(\widetilde{\mathcal D})\) be the directed graph on the \(W\)
owners in which \(X\to Y\) exactly when the useful-prefix bridge from
\(\widetilde\omega_X\) to \(\widetilde\omega_Y\) has length one.

The decorated-SCD gate is

\[
 \boxed{
 (\mathrm{EP}_A):\qquad
 pc\bigl(\mathcal B(\widetilde{\mathcal D})\bigr)
 =o_A(W/H),}
\tag{7.2}
\]

where \(pc\) denotes the minimum number of components in a spanning
directed path forest.  Such a forest has bridge excess at most
\(2H\,pc=o(W)\), while the SCD gives zero designated shadow holes.
Therefore \((\mathrm{EP}_A)\) implies \(\mathrm{MFUP}_A\).

### Proposition 7.1 (exact owner transition induced by a full collar)

Let

\[
 \omega=(L;z_1,\ldots,z_{2H};R)
\tag{7.3}
\]

be a full useful state, and let its middle owner be

\[
 X=L\cup\{z_1,\ldots,z_H\}.
\tag{7.4}
\]

Every bridge-one successor with a distinct middle owner is of exactly one
of the following forms.

1. For \(x\in L\) and \(y\in R\),
   \[
   L'=L-x+y,\qquad
   (z'_1,\ldots,z'_{2H})
   =(x,z_1,\ldots,z_{2H-1}),
   \tag{7.5}
   \]
   and its owner is \(Y=X-z_H+y\).
2. For \(x\in L\) and \(H<j\le2H\),
   \[
   L'=L-x+z_j,\qquad
   (z'_1,\ldots,z'_{2H})
   =(x,z_1,\ldots,\widehat{z_j},\ldots,z_{2H}),
   \tag{7.6}
   \]
   and its owner is \(Y=X-z_H+z_j\).

Thus the possible distinct successor owners are precisely

\[
 \boxed{\{X-z_H+y:y\notin X\},}
\tag{7.7}
\]

although a decorated SCD need not contain the required useful state at any
one of those owners.

#### Proof

The complete bridge-one classification consists of identity, rotor shift,
and singleton promotion.  Identity preserves the owner.  A promotion with
\(j\le H\) also preserves (7.4).  Substitution into the rotor and
\(j>H\) promotion formulas gives (7.5)--(7.7). \(\square\)

For every positive-tag owner define its first-band exit and entry

\[
 a_X=z^X_H\in X,\qquad b_X=z^X_{H+1}\notin X.
\tag{7.8}
\]

Proposition 7.1 gives the necessary first-band condition

\[
 \boxed{
 X\to Y,\ X\ne Y
 \quad\Longrightarrow\quad
 X\setminus Y=\{a_X\}=\{b_Y\}.}
\tag{7.9}
\]

Equivalently,

\[
 L_1(X)=X\cap Y,\qquad U_1(Y)=X\cup Y.
\tag{7.10}
\]

The full ordered-prefix identities (7.5)--(7.6) are stronger than
(7.9); first-band compatibility alone is not a bridge-one arc.

### 7.1 The rigid tag-\(H\) matching

Let

\[
 V_H=\{X:\text{the clipped tag of }X\text{ is }H\},
 \qquad |V_H|=\gamma_H=N_H.
\tag{7.11}
\]

A tag-\(d\) state has

\[
 E_{d,H}=\bigl((m-d)_{H-d}\bigr)^2
\tag{7.12}
\]

radius-\(H\) extensions.  Hence

\[
 E_{H,H}=1.
\tag{7.13}
\]

The useful state of every tag-\(H\) owner is therefore forced by the SCD;
decoration gives no freedom on \(V_H\).

### Theorem 7.2 (top-tag bridge rigidity)

For two distinct states \(X,Y\in V_H\),

\[
 \boxed{
 X\to Y\text{ is bridge one}
 \quad\Longleftrightarrow\quad
 X\to Y\text{ is a genuine radius-}H\text{ rotor arc}.}
\tag{7.14}
\]

#### Proof

Identity cannot join distinct useful states.  In a promotion (7.6), the
full upper endpoint of the target is

\[
 \begin{aligned}
 T_Y
 &=L_X-x+z_j+
   \{x,z^X_1,\ldots,\widehat{z^X_j},\ldots,z^X_{2H}\}\\
 &=L_X+\{z^X_1,\ldots,z^X_{2H}\}
 =T_X.
 \end{aligned}
\tag{7.15}
\]

The tag-\(H\) chains biject with the rank-\((m+H)\) masks, so two distinct
chains cannot share this endpoint.  Promotion is impossible.  The only
remaining bridge-one case is the rotor shift (7.5), and every rotor shift
is bridge one. \(\square\)

Let \(G_H(\mathcal D)\) be the split-copy bipartite graph with a left and a
right copy of \(V_H\), joining \(X_L\) to \(Y_R\) when the two forced
tag-\(H\) states satisfy the rotor identity (7.5).  Write

\[
 \nu_H=\nu(G_H(\mathcal D)).
\tag{7.16}
\]

### Theorem 7.3 (tag-\(H\) matching obstruction)

Every spanning bridge-one path forest on a decorated SCD has

\[
 \boxed{
 p\ge\bigl(2N_H-W-\nu_H\bigr)_+.}
\tag{7.17}
\]

Consequently \((\mathrm{EP}_A)\) requires

\[
 \boxed{
 \nu_H\ge2N_H-W-o_A(W/H).}
\tag{7.18}
\]

Equivalently, if

\[
 \delta_H
 =\max_{\mathcal S\subseteq V_{H,L}}
 \bigl(|\mathcal S|-|\Gamma_H(\mathcal S)|\bigr)
\tag{7.19}
\]

is the split-copy Hall deficiency, then

\[
 \nu_H=N_H-\delta_H,
 \qquad
 p\ge N_H-W+\delta_H,
\tag{7.20}
\]

and \((\mathrm{EP}_A)\) requires

\[
 \boxed{\delta_H\le W-N_H+o_A(W/H).}
\tag{7.21}
\]

When \(H=A\sqrt m+O(1)\),

\[
 \frac{N_H}{W}\longrightarrow e^{-A^2}.
\tag{7.22}
\]

Thus for every \(A<\sqrt{\log2}\), the rigid tag-\(H\) graph must contain a
matching of size

\[
 \boxed{
 \bigl(2e^{-A^2}-1-o(1)\bigr)W.}
\tag{7.23}
\]

#### Proof

A spanning path forest has \(W-p\) arcs.  Arcs whose tail lies outside
\(V_H\) number at most \(W-N_H\).  Among arcs whose tail lies in \(V_H\),
at most \(W-N_H\) can have their head outside \(V_H\), by the indegree-one
condition.  Every remaining arc is a tag-\(H\)-to-tag-\(H\) edge, and these
edges form a matching in the split-copy graph \(G_H(\mathcal D)\).
Therefore

\[
 W-p\le2(W-N_H)+\nu_H.
\tag{7.24}
\]

Rearrangement proves (7.17).  Equations (7.18)--(7.23) follow from
\((\mathrm{EP}_A)\) and the standard central-binomial ratio. \(\square\)

There is a coarser necessary balance condition visible before the full
ordered-prefix constraints.  Put

\[
 s_c=\#\{X\in V_H:a_X=c\},\qquad
 t_c=\#\{Y\in V_H:b_Y=c\}.
\tag{7.25}
\]

Every tag-\(H\) bridge-one edge stays inside one coordinate class \(c\) by
(7.9).  Hence

\[
 \nu_H
 \le\sum_{c=1}^{2m}\min(s_c,t_c)
 =N_H-\frac12\sum_{c=1}^{2m}|s_c-t_c|.
\tag{7.26}
\]

Combining (7.18) and (7.26), \((\mathrm{EP}_A)\) necessarily implies

\[
 \boxed{
 \frac12\sum_{c=1}^{2m}|s_c-t_c|
 \le W-N_H+o_A(W/H).}
\tag{7.27}
\]

Even perfect coordinate marginals do not prove (7.18), because the
restricted inclusion graphs inside the coordinate classes must also satisfy
Hall, and then the complete word identities (7.5)--(7.6) must hold.
Moreover, a large split-copy matching is only necessary: after projecting
back to owners it may contain many directed cycles.  Producing
\(o(W/H)\) paths requires an acyclic selection and compatible connections
to the lower-tag classes as well.

### 7.2 Exact common-base continuation

The outer chains can be chosen recursively, but retaining one inherited
rotor edge prescribes both endpoint matchings.

Suppose \(h\ge1\) and an SCD of the depth-\(h\) band has active states

\[
 v=(L_v;z_1(v),\ldots,z_{2h}(v);R_v).
\tag{7.28}
\]

Choose a continuation set \(C\) of exactly \(N_{h+1}\) active states.  A
lower continuation is a perfect matching

\[
 P^-:C\longrightarrow\binom{[2m]}{m-h-1},
 \qquad P^-(v)\subset L_v,
\tag{7.29}
\]

and, using complements of the upper endpoints, an upper continuation is a
perfect matching

\[
 P^+:C\longrightarrow\binom{[2m]}{m-h-1},
 \qquad P^+(v)\subset R_v.
\tag{7.30}
\]

For an inherited rotor edge \(e:v\to w\), write its rotor parameters as
\(x_e\in L_v\), \(y_e\in R_v\), and put

\[
 \lambda(e)=L_v-\{x_e\},
 \qquad
 \rho(e)=R_v-\{y_e\}.
\tag{7.31}
\]

### Theorem 7.4 (forced partial-matching extension)

Let \(F\) be a directed path forest of inherited rotor edges with all
vertices in \(C\).  There is an integral one-layer SCD extension which
continues exactly \(C\) and retains every edge of \(F\) if and only if:

1. the values \(\lambda(e)\), over the outgoing edges of \(F\), are
   distinct;
2. the values \(\rho(e)\), over the incoming edges of \(F\), are distinct;
3. the forced partial map
   \[
     P^-(v)=\lambda(v\to w)
     \tag{7.32}
   \]
   extends to a perfect matching of (7.29); and
4. the forced partial map
   \[
     P^+(w)=\rho(v\to w)
     \tag{7.33}
   \]
   extends to a perfect matching of (7.30).

Equivalently, after deleting the forced domain and image vertices, both
residual Boolean inclusion graphs satisfy Hall.

#### Proof

Extending \(v\) downward chooses one element \(\ell_v\in L_v\), with new
lower endpoint \(L_v-\ell_v\).  Extending \(w\) upward chooses one element
of \(R_w\) to remove from the upper complement.  The exact rotor-shift
identity forces

\[
 \ell_v=x_e,\qquad
 R_w-\{z_{2h}(v)\}=R_v-\{y_e\}.
\tag{7.34}
\]

These are precisely (7.32)--(7.33).  Distinctness is necessary because
\(P^-\) and \(P^+\) are matchings.  If the two forced partial maps extend,
use the completed matchings to attach all new lower and upper boundary
masks.  The prescribed edges then lift simultaneously, while every other
continued state receives its unmatched attachments.  This is a saturated
symmetric one-layer extension. \(\square\)

Within one recursive \(F_\ell\)-packet, both forced-color lists in
Theorem 7.4 are injective through every layer by the two-sided rainbow
property.  Across packets there are two independent possible losses:

\[
 \begin{array}{ll}
 \text{forced-color loss:}&
 \lambda\text{ or }\rho\text{ collides between packets},\\
 \text{completion loss:}&
 \text{the collision-free partial maps fail residual Hall}.
 \end{array}
\tag{7.35}
\]

Mixed pair frames remove the fixed-frame census shortage and provide every
individual prescribed chain column.  They do not remove either joint loss
in (7.35): the lower and upper matchings must use one common continuation
set \(C\), and the choices must be compatible through all \(H\) layers.

### Corollary 7.5 (exact constructive criterion for the rigid matching)

After constructing the first band separately, suppose one can choose nested
continuation sets and path forests

\[
 F_1\supseteq F_2\supseteq\cdots\supseteq F_H
\tag{7.36}
\]

so that Theorem 7.4 applies at every layer, the final vertex set has size
\(N_H\), and

\[
 |E(F_H)|\ge2N_H-W-o(W/H).
\tag{7.37}
\]

Then the resulting clipped SCD satisfies the necessary tag-\(H\) matching
bound (7.18), with \(\nu_H\ge|E(F_H)|\).

If instead \(F_H\) is a union of \(o(W/H)\) directed paths covering all
but \(o(W/H)\) tag-\(H\) owners, then the tag-\(H\) class already has the
path-cover scale required by \((\mathrm{EP}_A)\).

#### Proof

Iterate Theorem 7.4.  Every edge of \(F_H\) becomes a genuine
radius-\(H\) rotor edge between two top-tag chains, hence an edge of
\(G_H(\mathcal D)\) by Theorem 7.2.  The split copies of a path forest form
a matching, proving the first claim.  The second is immediate by inserting
the exceptional owners as singleton paths. \(\square\)

There are two sharp restrictions on this construction.

* Holding a lower base \(L\) stationary leaves no top-tag rotor edge.
  Holding the full upper endpoint \(T=L+\{z_1,\ldots,z_{2H}\}\) stationary
  also leaves no edge, by Theorem 7.2.  Both extremal bases must move
  coherently.
* Confining all packets to one coordinate pairing misses at least
  \[
    D_{m,H}
    =\sum_f(T_{f,H}-V_f)_+
    =\bigl(e^{-A^2}\Delta(A)+o(1)\bigr)W
    \tag{7.38}
  \]
  lower boundary masks.  Therefore no one-frame choice can even form the
  complete tag-\(H\) boundary class.

The complete mixed-frame orbit gives a perfectly balanced fractional and
scaled integral multicover of all the prescriptions in Theorem 7.4.
However, uniform common-base marginals do not imply a low-boundary common
base: even two transversal matroids can have only the two alternating bases
of an even cycle.  Thus the orbit average does not yield the one-fold,
recursively compatible selection in Corollary 7.5.

At present this is a sharp obstruction rather than a construction theorem:
no fixed-frame or stationary-base continuation can work, while the exact
mixed-frame common-base selection with loss \(o(W/H)\) remains unproved.

For the rigid matching bound alone, full \(2\ell\)-cycles are stronger than
necessary.

### Proposition 7.6 (bounded packet length suffices for \(\nu_H\))

Assume \(0<A<\sqrt{\log2}\), put

\[
 \theta=e^{-A^2},
\tag{7.39}
\]

and choose a fixed integer

\[
 \boxed{
 L_A>\frac{\theta}{1-\theta}
 =\frac1{e^{A^2}-1}.}
\tag{7.40}
\]

Suppose the tag-\(H\) class of one SCD, apart from \(r=o(W/H)\) owners, is
partitioned into directed radius-\(H\) rotor paths, each having \(L_A\)
owners except possibly one shorter terminal path.  Then

\[
 \boxed{
 \nu_H\ge2N_H-W+\Omega_A(W),}
\tag{7.41}
\]

and in particular the necessary matching estimate (7.18) holds with room
to spare.

#### Proof

Cutting the paths only at their ends retains at least

\[
 (N_H-r)-\frac{N_H-r}{L_A}-1
 =\left(1-\frac1{L_A}\right)N_H-o(W/H)
\tag{7.42}
\]

rotor edges.  By (7.22), divided by \(W\), the difference between the main
term in (7.42) and \(2N_H-W\) tends to

\[
 \theta\left(1-\frac1{L_A}\right)-(2\theta-1)
 =1-\theta-\frac{\theta}{L_A}>0
\tag{7.43}
\]

by (7.40).  These path edges form a split-copy matching in \(G_H\).
\(\square\)

For each fixed \(A\), the length \(L_A\) is constant in \(m\).  A
one-layer resolved \(L_A\)-path uses only a bounded number of state,
lower-color, and upper-color slots.  Thus fixed-uniformity matching tools
are not excluded at one layer.  What remains nonlocal is that the same
bounded paths must survive the common-base extension theorem through all
\(H\) layers.  Independent one-layer matchings do not provide the nested
sequence (7.36).

### 7.3 Can the two-stage owner partition be converted?

There are three distinct statements.

1. **The hypothetical exact atom-SCD packing does convert.**  Suppose the
   strong packet criterion of Theorem 6.1 holds, and decorate every chain by
   the full radius-\(H\) collar from its underlying \(F_\ell\)-cycle.  The
   useful states in each atom form one bridge-one rotor cycle.  Cutting each
   cycle once and treating the \(R=o(W/H)\) residual owners as singletons
   gives
   \[
     p\le\frac{W}{2\ell}+R=o(W/H)
     \tag{7.44}
   \]
   whenever \(H/\ell\to0\).  Hence this stronger construction implies
   \((\mathrm{EP}_A)\).
2. **The proved exact two-resolution identity does not automatically
   convert.**  It gives an exact SCD owner partition and an exact packet
   resolution of the same state multiset, but the statewise bijection may
   fragment every packet among different SCD colors.  Choosing collars for
   tags \(d<H\) cannot repair a deficit in \(G_H(\mathcal D)\), because
   tag-\(H\) collars are unique by (7.13).  The missing assertion is exactly
   the matching/path-cover estimate (7.18), followed by its analogues across
   all tags.
3. **An MFUP owner partition need not convert.**  Theorem 6.4 permits
   repeated shadows and does not assign the owners to chains of one SCD.
   It can prove the direct compiler without producing any decorated SCD.

Thus \((\mathrm{EP}_A)\) is a genuine intermediate gate: weaker than exact
packet preservation inside one SCD, stronger than \(\mathrm{MFUP}_A\), and
not a formal consequence of the currently proved two-resolution
factorization.

## 8. Final conclusion

The attempted same-frame gluing has an exact obstruction, not merely a
missing construction detail:

\[
 \text{one fixed pair frame}
 \Longrightarrow qP_q\ge D_{m,q}
 \Longrightarrow \Phi\ge(\kappa_A-o(1))W
\tag{7.1}
\]

for (H=A\sqrt m).  Varying only the nonlinear coordinate order inside
that frame cannot change (7.1).

The necessary escape is genuine frame mixing.  It is arithmetically and
geometrically viable:

* live frames can slide by one two-switch without changing the physical
  chronology (Lemma 3.1);
* one nonlinear \(F_\ell\)-cycle is already a two-sided-rainbow symmetric
  chain packet (Proposition 4.1); and
* all coordinate conjugates have both an exact fractional SCD mixture
  (Theorem 5.1) and the weaker exact fractional MFUP cover with target load
  \(W/N_q\) and \(o(W)\) interface mass (Theorem 6.2).

The primary remaining target is now the MFUP atom rounding gate, not the
stronger exact band-SCD gate.  It asks for exact middle-owner degree one and
aggregate duplicate excess only \(o(W)\) above the forced surplus; shadow
targets may repeat and need not be organized into common chains.  For
mesoscopic atoms \(H\ll\ell\), arbitrary useful-prefix resets already cost
only \(O(HW/\ell)=o(W)\), so phase ordering is automatic once the piece
count is controlled.  Proposition 6.5 records the residual integrality
barrier: two connected owner resolutions cannot be mixed by choosing whole
atoms.  Higher-order trades or controlled legal cuts are still unproved.

If one chooses to retain exact SCD ownership, the cleanest remaining target
is \((\mathrm{EP}_A)\).  Its radius-\(H\), tag-\(H\) states have no collar
freedom, and Theorem 7.3 forces a matching of size
\((2N_H-W)_+-o(W/H)\) in their induced bridge-one graph.  The hypothetical
exact atom-SCD packing supplies that matching and converts to
\((\mathrm{EP}_A)\); the proved statewise two-resolution identity does not.

Accordingly, Theorem 4.1 plus pair-stratum gluing does not yet prove the
constant-one theorem.  It does reduce the direct route to the exact,
strictly weaker condition in Theorem 6.4, without requiring an integral
SCD.

Finally, none of the arguments above assumes that every near-optimal OR word
can be converted to singleton entries or to a central near-universal cycle.
Equations (3.7)--(3.9) are exact for the selected Johnson/wreath/rotor
skeleton and give a sufficient coefficient-one route.  A general OR word
has ordered-partition states and may use essential nonsingleton letters; no
\(o(W)\)-cost reduction from that general class to singleton near-Ucycles is
known.  The fixed-frame obstruction and the multiframe rounding gate are
therefore scoped to the rotor--SCD route, not asserted as universal
characterizations of all near-optimal OR words.
