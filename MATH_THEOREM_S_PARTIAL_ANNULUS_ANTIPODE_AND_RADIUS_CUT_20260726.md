# Partial-annulus SCD packets: the endpoint antipode and native-radius cuts

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

and fix

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,\qquad 0<a<b.
\]

For a full SCD \(\mathcal D\), retain the chains of native radius at
least \(q_0\).  The SCD scaffold supplies exactly \(N_{q_0}\) annular
providers and exact target support at every depth \(q_0\le q\le H\).
This note records two exact restrictions on grouping those providers into
literal length-\(2m\) rotor cycles.

First, the lower and upper depth-\(q_0\) endpoints define a canonical
permutation \(\iota\) of the retained chains.  Literal antipodality in a
packet forces

\[
 C_{t+m}=\iota(C_t).
\]

Thus every used provider must lie in a two-cycle of \(\iota\).  With the
floor remainder \(\rho<2m\), all but at most \(\rho\) providers must lie
in such two-cycles.  This is an exact endpoint-monodromy obstruction to
the cycle formulation; it is absent from the weaker long-path compiler.

Second, let \(c_d\) be the number of native-radius-\(d\) SCD chains.  If
\(B_\uparrow\) selected path arcs fail to decrease native radius, then

\[
 p+B_\uparrow\ge\max_{d\ge q_0}c_d.
\]

The exact maximum is

\[
 \max_{d\ge q_0}c_d
 =\bigl(\gamma(a)+o(1)\bigr){W\over\sqrt m},
\]

where

\[
 \gamma(a)=
 \begin{cases}
  \sqrt{2/e},&a\le1/\sqrt2,\\
  2ae^{-a^2},&a\ge1/\sqrt2.
 \end{cases}
\]

Consequently every successful \(p=o(W/H)\) path cover needs
\(\Theta(W/H)\) nondecreasing-radius arcs.  In the cycle formulation the
mean number of such arcs per packet is \(\Theta(H)\), with the exact
leading lower bound

\[
 \bigl(2\gamma(a)e^{a^2}+o(1)\bigr)\sqrt m.
\]

Neither restriction is a universal no-go: one may seek an SCD whose
endpoint permutation is almost entirely involutive and whose decorated
rotor graph contains the required cross-grading arcs.  They do rule out
two tempting shortcuts: an arbitrary SCD followed by cycle closure, and
any recursive packet having only \(O(1)\) radius wraps.

## 1. The depth-\(q_0\) endpoint permutation

Let \(\Omega=\mathcal D_{\ge q_0}\).  For \(C\in\Omega\), write

\[
 D(C)=C_{-q_0}\in\binom{[2m]}{m-q_0},\qquad
 E(C)=C_{q_0}\in\binom{[2m]}{m+q_0}.
\tag{1.1}
\]

Both endpoint maps are bijections onto their ranks.  Define
\(\iota:\Omega\to\Omega\) by

\[
 \boxed{D(\iota C)=E(C)^c.}
\tag{1.2}
\]

This is a permutation: \(C\mapsto E(C)^c\) is a bijection onto the lower
rank, and each lower-rank set belongs to exactly one retained chain.

### Theorem 1.1 (endpoint antipode law)

Suppose a subset \(\Omega'\subseteq\Omega\) is assigned injectively to
the phases of literal directed cyclic-order packets, and every assigned
state reproduces both prescribed SCD endpoints \(D(C),E(C)\) at depth
\(q_0\).  If \(C_t\) is the provider at phase \(t\) of one packet, then

\[
 \boxed{C_{t+m}=\iota(C_t).}
\tag{1.3}
\]

In particular,

\[
 \boxed{\iota^2(C)=C\qquad(C\in\Omega').}
\tag{1.4}
\]

Hence \(\Omega'\) is a union of two-cycles of \(\iota\).  If
\(|\Omega\setminus\Omega'|\le r\), then at most \(r\) vertices of
\(\iota\) may lie outside its two-cycles.

#### Proof

Write the physical cyclic order as

\[
 z_0,z_1,\ldots,z_{2m-1}
\]

with indices modulo \(2m\).  At phase \(t\), the middle owner and the
two depth-\(q_0\) windows are

\[
 X_t=\{z_t,\ldots,z_{t+m-1}\},
\tag{1.5}
\]

\[
 D_t=\{z_{t+q_0},\ldots,z_{t+m-1}\},\qquad
 E_t=\{z_t,\ldots,z_{t+m+q_0-1}\}.
\tag{1.6}
\]

The opposite lower window is

\[
 D_{t+m}
 =\{z_{t+m+q_0},\ldots,z_{t+2m-1}\}
 =E_t^c.
\tag{1.7}
\]

By the prescribed endpoint identities,

\[
 D(C_{t+m})=E(C_t)^c=D(\iota C_t).
\]

Injectivity of the lower endpoint map gives (1.3).  Applying it twice
around the packet gives (1.4).  Therefore every selected vertex belongs
to an \(\iota\)-orbit of length two.  No vertex from any other orbit can
be selected, which proves the final assertion. \(\square\)

There are no fixed points of \(\iota\).  Indeed, \(\iota C=C\) would
give \(D(C)=E(C)^c\).  But \(D(C)\subset E(C)\), whereas \(E(C)^c\) is
disjoint from \(E(C)\); since \(|D(C)|=m-q_0>0\), this is impossible.

### Corollary 1.2 (floor-corrected endpoint obstruction)

Put

\[
 K=\left\lfloor{N_{q_0}\over2m}\right\rfloor,
 \qquad \rho=N_{q_0}-2mK<2m.
\tag{1.8}
\]

If \(2mK\) SCD providers lie in \(K\) literal length-\(2m\) packets,
then the number of vertices of \(\iota\) outside two-cycles is at most
\(\rho\).  Thus an SCD with more than \(\rho\) such vertices cannot
satisfy the requested cycle factor, independently of every deeper collar
choice.

The converse is deliberately limited.  At the depth-\(q_0\) endpoint
level, a physical rank-\((m-q_0)\) interval-cycle factor whose half-turn
is \(\iota\) reproduces both signed endpoint lists.  It still has to
satisfy global middle-owner simplicity, every forced outer SCD tail, and
the common depth-\(q_0,\ldots,H\) history.  An involutive \(\iota\) alone
is therefore not sufficient.

## 2. The exact native-radius histogram

Let \(\mathcal D_d\) be the chains of native radius \(d\), and put

\[
 c_d=|\mathcal D_d|,\qquad
 N_d=\binom{2m}{m-d},\qquad N_{m+1}=0.
\tag{2.1}
\]

Every rank-\((m-d)\) set belongs to a chain of radius at least \(d\), so

\[
 \boxed{
 c_d=N_d-N_{d+1}
 =\frac{2d+1}{m+d+1}\binom{2m}{m-d}.}
\tag{2.2}
\]

The consecutive ratio is

\[
 \boxed{
 {c_{d+1}\over c_d}
 ={(m-d)(2d+3)\over(m+d+2)(2d+1)}.}
\tag{2.3}
\]

It is at least one exactly when

\[
 (d+1)^2\le {m+1\over2}.
\tag{2.4}
\]

Let

\[
 r_m=\left\lfloor\sqrt{{m+1\over2}}\right\rfloor,
 \qquad d_*=\max\{q_0,r_m\}.
\tag{2.5}
\]

Then

\[
 \boxed{\max_{d\ge q_0}c_d=c_{d_*}.}
\tag{2.6}
\]

If \(\sqrt{(m+1)/2}\) is integral, \(r_m-1\) is the second tied
unrestricted maximizer.  This harmless tie does not change (2.6).

### Lemma 2.1 (Gaussian maximum)

For fixed \(a>0\),

\[
 \boxed{
 c_{d_*}=\bigl(\gamma(a)+o(1)\bigr){W\over\sqrt m},}
\tag{2.7}
\]

where

\[
 \gamma(a)=\max_{x\ge a}2xe^{-x^2}
 =
 \begin{cases}
  \sqrt{2/e},&a\le1/\sqrt2,\\
  2ae^{-a^2},&a\ge1/\sqrt2.
 \end{cases}
\tag{2.8}
\]

#### Proof

Uniformly for \(d=O(\sqrt m)\),

\[
 {N_d\over W}
 =\prod_{j=0}^{d-1}{m-j\over m+j+1}
 =\exp\left(-{d^2\over m}+O(m^{-1/2})\right).
\tag{2.9}
\]

Together with (2.2), this gives

\[
 {c_d\over W}
 ={1\over\sqrt m}
 \left(2{d\over\sqrt m}e^{-d^2/m}+o(1)\right)
\tag{2.10}
\]

uniformly on bounded Gaussian scales.  Equations (2.5)--(2.6) reduce the
maximum to that of \(2xe^{-x^2}\) on \([a,\infty)\), proving (2.7)--(2.8).
The ceiling in \(q_0\) changes \(d/\sqrt m\) by \(o(1)\). \(\square\)

## 3. The cross-grading cut

Consider any directed path cover of \(\Omega=\mathcal D_{\ge q_0}\).
Let \(p\) be its number of paths, and let \(B_\uparrow\) count selected
arcs \(C\to C'\) satisfying

\[
 \operatorname{rad}(C')\ge\operatorname{rad}(C).
\tag{3.1}
\]

### Theorem 3.1 (native-radius layer cut)

Every such cover obeys

\[
 \boxed{p+B_\uparrow\ge c_{d_*}.}
\tag{3.2}
\]

Consequently, if \(p=o(W/H)\), then

\[
 \boxed{
 B_\uparrow
 \ge\bigl(\gamma(a)+o(1)\bigr){W\over\sqrt m}
 =\bigl(b\gamma(a)+o(1)\bigr){W\over H}.}
\tag{3.3}
\]

#### Proof

Delete the \(B_\uparrow\) nondecreasing arcs.  The remaining graph is a
cover by \(p+B_\uparrow\) directed paths, and native radius strictly
decreases along every remaining path.  Such a path contains at most one
member of \(\mathcal D_{d_*}\).  Covering all \(c_{d_*}\) members of
that stratum therefore requires at least \(c_{d_*}\) paths.  This proves
(3.2).  Since \(H=(b+o(1))\sqrt m\), Lemma 2.1 gives (3.3). \(\square\)

The bound is sharp using only the radius histogram.  In the complete
transition relaxation, sort the strata by radius and place their vertices
into \(\max c_d\) columns, at most one vertex of each stratum in a column.
Reading every column in decreasing radius gives exactly \(\max c_d\)
paths.  Thus any stronger obstruction must use the physical port graph,
not only the tag counts.

### Corollary 3.2 (cycle form and the per-packet burden)

Suppose \(\Omega'\subseteq\Omega\) omits \(r\) vertices and is
partitioned into directed cycles.  Let \(B_{\rm cyc}\) be the total
number of cycle arcs which do not decrease native radius.  Then

\[
 \boxed{
 B_{\rm cyc}
 \ge\max_d|\Omega'\cap\mathcal D_d|
 \ge c_{d_*}-r.}
\tag{3.4}
\]

#### Proof

Every directed cycle has at least one nondecreasing-radius arc.  Cut one
such arc in each cycle and delete all remaining nondecreasing arcs.  The
result consists of exactly \(B_{\rm cyc}\) strictly decreasing paths.
At least \(\max_d|\Omega'\cap\mathcal D_d|\) such paths are required.
Omitting \(r\) vertices removes at most \(r\) vertices from the largest
original stratum. \(\square\)

For the floor-corrected choice \(r=\rho<2m\), (3.4) and

\[
 K={N_{q_0}\over2m}+O(1)
   =\bigl(e^{-a^2}+o(1)\bigr){W\over2m}
\tag{3.5}
\]

give

\[
 \boxed{
 {B_{\rm cyc}\over K}
 \ge\bigl(2\gamma(a)e^{a^2}+o(1)\bigr)\sqrt m
 =\Theta(H).}
\tag{3.6}
\]

Thus a cycle architecture with only \(O(1)\) radius wraps, phase changes,
or other nondecreasing transitions per packet cannot realize the corrected
partial SCD scaffold.

## 4. Exact boundary

Proved here:

1. the endpoint permutation \(\iota\) and the exact antipodal law
   \(C_{t+m}=\iota(C_t)\);
2. the floor-corrected requirement that all but \(\rho<2m\) providers lie
   in two-cycles of \(\iota\);
3. the exact native-radius histogram and its restricted Gaussian maximum;
4. the cross-grading inequality \(p+B_\uparrow\ge c_{d_*}\); and
5. the \(\Theta(H)\) mean nondecreasing-radius burden per literal packet.

Not proved here:

1. an SCD whose endpoint permutation is almost entirely involutive;
2. a physical interval-cycle factor whose half-turn realizes that
   involution while keeping middle owners disjoint;
3. the required \(\Theta(W/H)\) state-composable cross-grading arcs; or
4. the common forced-tail history through all depths \(q_0,\ldots,H\).

The path compiler in
`MATH_THEOREM_S_PARTIAL_ANNULUS_DIAGONAL_PORT_AND_TAIL_HALL_20260726.md`
shows why these cycle obstructions do not close the RSCD lane: a path
cover with \(o(W/H)\) components may be cut into length-at-most-\(2m\)
pieces at total cost \(W+o(W)\), without antipodal closure.  The decisive
surviving object is therefore the owner-simple, all-port ordered-Hall path
cover, not an arbitrary radius-monotone cycle factor.
