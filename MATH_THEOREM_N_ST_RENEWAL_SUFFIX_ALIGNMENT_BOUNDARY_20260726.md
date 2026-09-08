# PBBS short returns: exact predecessor-suffix summation and the irreducible alignment coordinate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad G=2H-1.
\]

This note pushes the reduced predecessor-passage process through the
strongest scalar global summation available on an actual PBBS orbit.
The result is an exact formula, but it also proves why that summation does
not decide the Gaussian transversal gate.

Fix an augmented rank-\(d\) reduced PBBS orbit \(\mathcal O\), put
\(p=2d+1\), and let \(\kappa_s\in\mathbb Z_p\) be the persistent equality
particle selected at time \(s\).  If

\[
 t_{b,1}<\cdots<t_{b,q}
\]

are the cyclic selection times of particle \(b\), and

\[
 g_{b,i}=t_{b,i+1}-t_{b,i},
\]

then coordinate homomesy gives

\[
 q={|\mathcal O|\over p},\qquad
 \sum_{i=1}^q g_{b,i}=|\mathcal O|,
 \qquad {1\over q}\sum_i g_{b,i}=p.             \tag{0.1}
\]

For \(a=b+1\), a phase \(s\) in the open predecessor block

\[
 t_{b,i-1}<s<t_{b,i}
\]

is predecessor-active through time \(G\) precisely when it is an
\(a\)-visit in the terminal suffix

\[
 I_{b,i}(G)=
 \{s:t_{b,i-1}<s<t_{b,i},\ t_{b,i}-s+g_{b,i}\le G\}. \tag{0.2}
\]

The length of this suffix is exactly

\[
 \boxed{
 \lambda_{b,i}(G)
 =\min\{g_{b,i-1}-1,(G-g_{b,i})_+\}
 =(G-g_{b,i})_+-(G+1-g_{b,i-1}-g_{b,i})_+.}       \tag{0.3}
\]

Consequently the complete one-point active count on the orbit is

\[
 \boxed{
 A_G(\mathcal O)
 =\sum_{b\in\mathbb Z_p}\sum_{i=1}^q
   \#\{s\in I_{b,i}(G):\kappa_s=b+1\}.}          \tag{0.4}
\]

Thus the generalized predecessor decomposition has two coordinates:

1. the adjacent pair of \(b\)-renewal gaps, which determines the suffix
   \(I_{b,i}(G)\); and
2. the placement of successor visits \(b+1\) inside that suffix.

All Kac/homomesy sums, every one-particle gap histogram, and the complete
nilpotent Jordan form determine the first coordinate and omit the second.
This omission is sharp.  Two balanced cyclic selected-particle words can
have the same cyclic gap multiset for every particle and different values
of (0.4), already by one on the even/\(\tau\)-phase subdeck.  The example
is an obstruction to scalar renewal arguments, not a claim that the two
abstract words are PBBS orbits.

There is also a genuine PBBS obstruction at the first nontrivial inverse
lift.  On the exact core orbit

\[
 110100\longmapsto110010\longmapsto101100\longmapsto110100,
\]

the first and third phases are tight gap-five starts, but only the ordered
pair \(101100\to110100\) lifts to a tight gap-seven parent.  The unique
terminal-zero lift above the other tight phase fails.  Hence even in PBBS,
slot occupancy and one-phase activity do not determine the successor
placement in (0.4).

No estimate

\[
 \overline\nu_H=\Omega_A(B_m/H)
 \quad\hbox{or}\quad
 \overline\nu_H=o_A(B_m/H)
\]

follows from the scalar summation.  The exact remaining statistic is the
Pascal-weighted law of the marked suffix occupancies in (0.4), jointly for
successive labels and for even phase shifts up to \(H+1\).

## 1. Actual orbit notation and homomesy

Let \({\cal U}_d\) be the particle-labelled PBBS permutation on

\[
 \Omega_p=\binom{[p]}d,
 \qquad p=2d+1.
\]

The labels are persistent equality-particle identities.  On an orbit

\[
 \mathcal O=(x_0,x_1,\ldots,x_{L-1}),
\]

write \(\kappa_s\) for the selected label at \(x_s\), with indices read
modulo \(L\).  Coordinate homomesy for the labelled PBBS says that every
label occurs the same number of times.  Since exactly one label is selected
at every phase, this common number is

\[
                         q=L/p.                  \tag{1.1}
\]

For fixed \(b\), list its visits cyclically and set

\[
 t_{b,i+q}=t_{b,i}+L,
 \qquad g_{b,i}=t_{b,i+1}-t_{b,i}>0.             \tag{1.2}
\]

Telescoping gives

\[
                         \sum_{i=1}^qg_{b,i}=L.  \tag{1.3}
\]

In particular every particle has exact mean return gap \(p\).  Summing
over all labels gives the two orbitwise scalar identities

\[
 \sum_{b,i}1=L,
 \qquad
 \sum_{b,i}g_{b,i}=pL.                           \tag{1.4}
\]

These identities survive multiplication by any weight constant on the
orbit, in particular the exact inverse-Pascal weight

\[
                         P_m(F)=\binom{m+d-\operatorname {pk}(F)}{2d}.
\]

They are therefore genuine global identities for the weighted reduced
process, not heuristic renewal moments.

## 2. Exact terminal-suffix formula

Fix \(b\), put \(a=b+1\), and take a phase \(s\) with \(\kappa_s=a\).
It lies in a unique open block

\[
                         t_{b,i-1}<s<t_{b,i}.     \tag{2.1}
\]

The first two future selections of \(b\) occur at \(t_{b,i}\) and
\(t_{b,i+1}\).  Therefore the second-predecessor time measured from \(s\)
is

\[
 t_{b,i+1}-s=(t_{b,i}-s)+g_{b,i}.                \tag{2.2}
\]

The phase is active through horizon \(G\) if and only if the right side
of (2.2) is at most \(G\).  This proves the set formula (0.2).

The open block contains \(g_{b,i-1}-1\) integer phases.  The inequality
in (2.2) retains its last \((G-g_{b,i})_+\) phases, truncated by the block
length.  Hence

\[
 |I_{b,i}(G)|
 =\min\{g_{b,i-1}-1,(G-g_{b,i})_+\}.             \tag{2.3}
\]

For nonnegative integers \(u,v\),

\[
 \min\{u,v_+\}=v_+-(v-u)_+.
\]

Substitute \(u=g_{b,i-1}-1\) and \(v=G-g_{b,i}\) to obtain the second
form in (0.3).  The discrete derivative is consequently

\[
 \boxed{
 \lambda_{b,i}(G+1)-\lambda_{b,i}(G)
 =\mathbf1_{\{g_{b,i}\le G<g_{b,i}+g_{b,i-1}-1\}}.} \tag{2.4}
\]

Finally, among the positions in the suffix, precisely those carrying
\(a=b+1\) are predecessor-active.  Summing over the unique block of every
successor phase, and then over \(b\), proves (0.4) without omission or
overcounting.

The elementary enclosure

\[
 0\le A_G(\mathcal O)
 \le\sum_{b,i}\lambda_{b,i}(G)                  \tag{2.5}
\]

is generally sharp at both ends for cyclic words with the same gap data.
Thus replacing the marked count in (0.4) by the suffix volume on its right
loses the decisive information.

## 3. Same-spectrum cyclic-word obstruction

Let \(p\ge4\), let the cyclic time set have length \(2p\), and distinguish
two consecutive labels \(a=b+1\).  Construct a balanced cyclic word \(W\)
by putting

\[
 b\text{ at }0,2p-1,
 \qquad a\text{ at }1,2,                          \tag{3.1}
\]

and placing each of the remaining \(p-2\) labels exactly twice in the
remaining positions, in any order.  Let \(W'\) be the reflected word

\[
                         W'(t)=W(2p-1-t).         \tag{3.2}
\]

Reflection preserves the unordered cyclic gap multiset of every label:
a two-occurrence gap pair \(\{u,2p-u\}\) is merely reversed.  Thus \(W\)
and \(W'\) have

* the same number of visits for every particle;
* the same cyclic one-particle gap multiset for every particle;
* the same mean gap \(p\); and
* the same nilpotent Jordan block multiset for every killed one-particle
  shift.

In \(W'\), the two \(a\)-visits are at

\[
                         2p-3,2p-2.              \tag{3.3}
\]

For every

\[
                         3\le G\le2p-3,          \tag{3.4}
\]

the early \(a\)-visits of \(W\) have their second future \(b\)-visit only
after more than \(G\) steps, so neither is active.  The late visits of
\(W'\) see \(b\) at times \(2p-1\) and \(2p\), at respective second-hit
delays \(3\) and \(2\).  Both are active.  Exactly one late visit has even
time, while the corresponding even visit of \(W\) is inactive.  Therefore
the even-phase active counts differ by one.

This proves:

> The predecessor-active count, even after restricting to the
> \(\tau\)-phase subdeck, is not a function of coordinate homomesy plus the
> complete family of one-particle cyclic gap multisets.

The construction deliberately asserts only a renewal-data obstruction.
It is not asserted that \(W\) or \(W'\) is a PBBS selected-particle word.
Its role is exact: any proof using only the scalar identities (1.4), the
gap histograms, or the Jordan spectra cannot decide the PBBS gate.  A
successful argument must import a PBBS-specific restriction on the marked
successor placements in (0.4).

## 4. Genuine PBBS first-lift obstruction

The abstract freedom in Section 3 has a literal PBBS analogue at the
first nontrivial orientation step.  On the semilength-three \(\tau\)-cycle

\[
 F_0=110100,
 \quad F_1=110010,
 \quad F_2=101100,
 \quad \tau F_i=F_{i+1\pmod3},                   \tag{4.1}
\]

the exact deficit and first-maximum pairs are

\[
 (\delta,d)(F_0)=(2,1),\quad
 (\delta,d)(F_1)=(2,3),\quad
 (\delta,d)(F_2)=(4,1).                          \tag{4.2}
\]

The tight gap-five equation

\[
                         d(F)+d(\tau F)=\delta(\tau^2F)       \tag{4.3}
\]

holds exactly at \(F_0\) and \(F_2\).  Nevertheless the unique
minimal-rank terminal-zero lift above \(F_0\),

\[
                         D_0=1110011000,          \tag{4.4}
\]

has orbit data

\[
 (\delta,d)(D_0),(\delta,d)(\tau D_0),(\delta,d)(\tau^2D_0)
 =(3,1),(3,5),(7,1),                              \tag{4.5}
\]

and fails the return equations at step-two times one, two, and three:

\[
                         1\ne3,\qquad6\ne7,\qquad7\ne3.      \tag{4.6}
\]

The other tight phase has the unique lift

\[
                         D_2=1100111000,          \tag{4.7}
\]

whose cyclic deficits \(1,1,5\) satisfy

\[
                         1+1+5=7=\delta(D_2),     \tag{4.8}
\]

so it starts the tight gap-seven return.  Thus the ordered adjacent pair

\[
                         F_2\longmapsto F_0       \tag{4.9}
\]

closes, while the phase \(F_0\) followed by the inactive \(F_1\) does
not.  Since the inverse fibre at (4.4)--(4.7) has free mass zero, no slot
choice or integral rounding repairs the wrong orientation.

The complete word calculation and the uniqueness of the inverse lifts are
recorded in
`MATH_THEOREM_N_ST_ALL_ZERO_SLOT_ORIENTATION_OBSTRUCTION_20260726.md`.
This example proves inside PBBS that an active one-phase marginal and a
terminal-zero lift do not determine the successor incidence needed by
(0.4).

## 5. Consequence for global summation

Give every augmented orbit its exact inverse-Pascal weight, constant on
that orbit, and divide augmented traces by \(p\).  Equations (1.4) then
sum exactly over all ranks and all orbits.  They determine total visit
mass and total renewal-gap mass.  Equation (0.4), however, becomes

\[
 \sum_{d,\mathcal O}{P_m(\mathcal O)\over2d+1}
 \sum_{b,i}
 \#\{s\in I_{b,i}(G):\kappa_s=b+1\}.             \tag{5.1}
\]

Neither (1.4) nor (2.4) evaluates (5.1).  Even knowledge of every
\(\lambda_{b,i}(G)\) does not do so: one needs the marked occupancy of
each suffix.  The two-point statistic additionally needs the common
alignment of these marked suffix systems for the labels selected at
phases \(s\) and \(s+2u\), \(1\le u\le H+1\).

Accordingly the exact negative criterion remains

\[
 \mathscr R_H\ge\kappa {B_m\over H},
 \qquad
 \mathscr C_H\le M\mathscr R_H                  \tag{5.2}
\]

for fixed \(\kappa>0,M<\infty\), or, more generally, critical
Pascal mass in one bounded active-degree stratum.  Under (5.2), the
audited degree pullback gives

\[
 \overline\nu_H
 \ge
 \left({3\kappa\over8(\lceil4M\rceil+1)}-o(1)\right)
 {B_m\over H}.                                   \tag{5.3}
\]

After the minimal-simple-return reduction this loses at most a further
factor two.  Lifting a quotient family of size \(c_AB_m/H\) through the
physical deck gives, with no lower-direction factor-two loss,

\[
 \nu_H(P_m)
 \ge c_A{NB_m\over H}
 =\left({2c_A\over A}+o(1)\right)B_m\sqrt m.     \tag{5.4}
\]

The present theorem proves neither hypothesis in (5.2).  It proves that
they cannot be obtained from Kac totals, one-particle renewal spectra, or
fixed-depth slot marginals alone.

## 6. Exact proved boundary

Proved:

1. the exact adjacent-two-gap suffix length (0.3), including its horizon
   derivative (2.4);
2. the complete orbitwise predecessor-active summation (0.4);
3. the exact homomesy/Kac totals (1.4) on actual augmented PBBS orbits;
4. a same-spectrum cyclic-word obstruction showing that those totals and
   all one-particle gap spectra omit the marked successor coordinate;
5. a genuine PBBS first-lift obstruction showing that terminal-zero
   capacity and one-phase tightness do not restore that coordinate; and
6. the exact lower deck constant (5.4).

Not proved:

1. a Pascal-saddle lower bound for the marked suffix mass (5.1);
2. boundedness or divergence of its active Palm degree;
3. \(\overline\nu_H=\Omega_A(B_m/H)\) or
   \(\overline\nu_H=o_A(B_m/H)\); or
4. \(ST_A\) or its negation.

The generalized predecessor-passage decomposition is therefore exhausted
at scalar level.  The missing theorem is irreducibly a marked, multi-label,
even-phase alignment theorem for the actual PBBS selected-particle word.
