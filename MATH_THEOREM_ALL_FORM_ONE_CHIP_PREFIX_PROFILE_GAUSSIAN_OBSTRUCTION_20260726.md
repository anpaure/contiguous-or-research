# All-form one-chip packets: exact prefix degrees and the Gaussian literal-compiler obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W=\binom n m,
 \qquad
 T={W\over n}.
 \tag{0.1}
\]

Assume the middle packet hypergraph from
`MATH_THEOREM_ALL_FORM_ONE_CHIP_VOLTAGE_PACKETS_20260726.md` has a
matching covering \(T-o(T)\) odd-central form vertices.  This assumption
solves the middle-owner and component-count layer: the selected unit-voltage
packets lift to a singleton word of core length \(W-o(W)\), use
\(O(W/m^2)\) components, and leave only \(o(W)\) middle owners for literal
repair.

The prefix layer is separate, and it fails for the one-chip atlas itself.
At a fixed Gaussian depth

\[
                         q=A\sqrt m+O(1),
 \qquad A>0,
 \tag{0.2}
\]

the following statements hold before any middle matching is chosen.

1. **Packet phases provide no coverage choice.**  Cyclically shifting a
   selected packet merely permutes its quotient phases.  Changing its
   initial physical voltage phase merely translates every target.  Since
   the unit-voltage lift visits all \(n\) translations, the complete lower
   and upper prefix profiles of a selected packet are invariant.

2. **Almost every lower target has degree zero.**  A rank-
   \((m-q)\) target is reachable from a one-chip packet if and only if its
   cyclic gap composition has a part at least \(q+2\).  For a free target
   with gap word \(g=(g_1,\ldots,g_{m-q})\), its exact weighted degree in
   the full packet-phase atlas is

   \[
      \boxed{
      d_q^-(g)=\sum_i\binom{g_i-2}{q}.}
   \tag{0.3}
   \]

   The reachable fraction of the whole physical target layer is at most

   \[
    \eta^-_{m,q}\le
       {n\binom{2m-q-1}{m}\over\binom{2m+1}{m-q}}
       =o_A(1).
   \tag{0.4}
   \]

3. **The upper side has vanishing total supply.**  In the physical word
   of a parent \(z=(z_1,\ldots,z_m)\), a length-
   \((m+1+q)\) interval has \(m+1+q\) distinct symbols if and only if
   the corresponding \(q\) consecutive parent gaps are all at least two.
   Across **all** parent packets and all quotient phases, the exact number
   of valid upper phases is

   \[
                         A_{m,q}=\binom{2m-q-1}{m-1}.
   \tag{0.5}
   \]

   Even crediting every valid phase with \(n\) distinct physical targets,
   the coverable fraction is at most

   \[
    \boxed{
    \eta^+_{m,q}:=
    {nA_{m,q}\over\binom{2m+1}{m-q}}
    ={(2m-q-1)!(m+q+1)!\over(m-1)!(2m)!}.}
   \tag{0.6}
   \]

   Uniformly for \(q=o(m^{2/3})\),

   \[
    \log\eta^+_{m,q}
      =\log m-(q+1)\log2+{3q^2\over4m}
       +O\!\left({q\over m}+{q^3\over m^2}\right).
   \tag{0.7}
   \]

   Hence \(\eta^+_{m,q}=o_A(1)\) at (0.2), and

   \[
                         \eta^-_{m,q}\le {m-q\over m}\eta^+_{m,q}.
   \tag{0.8}
   \]

Since

\[
 {\binom{2m+1}{m-q}\over W}=e^{-A^2+o(1)},
 \tag{0.9}
\]

every subfamily of one-chip packets, including a hypothetical perfect
middle matching, leaves

\[
 \boxed{
 (1-o_A(1))\binom{2m+1}{m-q}
   =(e^{-A^2}+o_A(1))W}
 \tag{0.10}
\]

lower targets missing and the same number of upper targets missing at
depth \(q\).  The two-sided aggregate leave is therefore

\[
                         (2e^{-A^2}+o_A(1))W.
 \tag{0.11}
\]

Thus the all-form one-chip packet construction is a valid and potentially
near-perfect **middle** packet system, but it cannot be a literal Gaussian
OR compiler.  The obstruction is support-level, not a failure of random
phase selection, codegree control, or scalar supply.  Any positive route
must alter the physical packet word—by cross-packet rethreading, extra
chips, or a different successor—not merely choose phases of the existing
unit-voltage components.

## 1. Middle matching and prefix incidence are different systems

Let \({\cal B}_m\) be the cyclic positive compositions of \(2m\) into
\(m\) parts.  A parent \([z]\in{\cal B}_m\), of least period
\(r(z)\mid m\), supplies one packet of \(r(z)\) odd-central form
vertices.  Its physical lift is one component of length \(nr(z)\).

Let \({\cal M}\subseteq{\cal B}_m\) be a packet matching, and suppose it
covers all but \(L=o(T)\) middle form vertices.  Then

\[
                         \sum_{z\in{\cal M}}r(z)=T-L.
 \tag{1.1}
\]

The complete atlas contains only \(e^{-\Omega(m)}T\) vertices in periodic
parent packets.  Hence every near-perfect matching satisfies

\[
                         |{\cal M}|=(1+o(1)){T\over m}
                         =O(W/m^2).
 \tag{1.2}
\]

Thus linearizing every selected cyclic component with an \((m+H)\)-symbol
collar costs

\[
                         O((m+H)W/m^2)=o(W)
 \tag{1.3}
\]

for every \(H=o(m)\).  The \(nL=o(W)\) uncovered physical middle owners
may also be appended literally.  These statements use only the middle
matching.

Concatenation can create additional seam-crossing windows, but there are
at most \(O((m+H)|{\cal M}|)=O(W/m)=o(W)\) of them.  They cannot repair
the linear prefix deficits proved below.

For a fixed packet, however, all its cyclic positions are used in the
literal word.  Choosing another quotient start sends \(t\) to \(t+c\)
and hence only permutes its prefix occurrences.  Choosing another initial
physical symbol translates every occurrence by the same element of
\(\mathbb Z_n\); the unit voltage subsequently visits every translation.
Therefore:

### Lemma 1.1 (phase invariance)

The multisets of lower and upper target orbits produced by one complete
one-chip packet are independent of its cyclic quotient phase and physical
starting phase.

In particular, after \({\cal M}\) is fixed there is no second phase-choice
hypergraph whose matching could repair prefix holes.  The prefix profile
is a deterministic incidence vector attached to each already selected
packet.

## 2. The physical word and its recurrence

Fix a rooted representative

\[
                         z=(z_1,\ldots,z_m),
 \qquad z_i\ge1,
 \qquad \sum_i z_i=2m.
 \tag{2.1}
\]

Extend \(z\) periodically.  The physical singleton word of its voltage
lift obeys

\[
                         s_{j+1}=s_j+z_{j+1}\pmod n.
 \tag{2.2}
\]

The least-period packet circuit shifts the physical phase by \(2r(z)\),
which is a unit modulo \(n\), so (2.2) traverses all \(nr(z)\) packet
positions.  Since every \(m\) consecutive gaps have sum \(2m=n-1\),

\[
                         \boxed{s_{j+m}=s_j-1\pmod n.}
 \tag{2.3}
\]

Every interval of at most \(m+1\) symbols is therefore a set.  Formula
(2.3) is also the source of both Gaussian obstructions below.

## 3. Exact lower-target degree

Put

\[
                         k=m-q.
 \tag{3.1}
\]

A lower interval of \(k\) symbols beginning at phase \(t\) uses the
first \(k-1\) parent gaps.  Its cyclic gap composition is

\[
 \left(
 z_{t+1},\ldots,z_{t+k-1},
 1+\sum_{j=k}^{m}z_{t+j}
 \right).
 \tag{3.2}
\]

There are \(q+1\) summands in the final term.  Hence that closing gap is
at least \(q+2\).

Conversely, let \(g=(g_1,\ldots,g_k)\) be a rooted positive composition
of \(n\).  If \(g_k\ge q+2\), split \(g_k-1\) into \(q+1\) positive
parts and append those parts to \(g_1,\ldots,g_{k-1}\).  This produces a
parent word \(z\) for which (3.2) is \(g\).  The number of ordered splits
is

\[
                         \binom{g_k-2}{q}.
 \tag{3.3}
\]

Here and below \(\binom aq=0\) when \(a<q\) or \(a<0\).

Let a target translation orbit \(O\) have stabilizer order \(h(O)\), and
write its full cyclic gap word as \(g_1,\ldots,g_k\).  Its weighted atlas
degree is

\[
 d_q^-(O):=\sum_{[z]\in{\cal B}_m}a_{z,q}(O).
 \tag{3.4}
\]

### Theorem 3.1 (exact lower degree and support)

For every lower target orbit,

\[
 \boxed{
 d_q^-(O)={1\over h(O)}
       \sum_{i=1}^{k}\binom{g_i-2}{q}.}
 \tag{3.5}
\]

In particular, \(d_q^-(O)>0\) if and only if

\[
                         \max_i g_i\ge q+2.
 \tag{3.6}
\]

For free targets \(h(O)=1\), (3.5) is (0.3).

#### Proof

Choose a cyclic root of the target.  Equations (3.2)--(3.3) give one
incident rooted parent for every ordered split of the closing gap minus
one, and every incident packet phase arises uniquely this way.  Summing
over the \(k\) cyclic roots gives the numerator in (3.5).  If the target
has stabilizer \(h(O)\), its gap word repeats \(h(O)\) times, so the same
rooted parents are repeated exactly \(h(O)\) times in that sum.  Division
gives (3.5).  The support criterion follows from positivity of the
binomial coefficient. \(\square\)

This exact degree formula already rules out the usual near-regular
hypergraph route: at Gaussian depth almost all right vertices have degree
zero, while the small reachable family carries the entire phase mass.

## 4. Counting the reachable lower support

Choose a uniformly rooted rank-\(k\) target.  Its gap word is a uniform
positive composition of \(n\) into \(k\) parts.  For one fixed part,

\[
 \Pr(g_i\ge q+2)
 ={\binom{n-q-2}{k-1}\over\binom{n-1}{k-1}}.
 \tag{4.1}
\]

The event that some gap is long is rotation invariant, so the same
probability applies to uniformly chosen unrooted physical targets.  The
union bound and Theorem 3.1 give

\[
 {N_q^{-,\mathrm{reachable}}\over\binom n k}
 \le
 k{\binom{n-q-2}{k-1}\over\binom{n-1}{k-1}}
 ={n\binom{2m-q-1}{m}\over\binom{2m+1}{m-q}}.
 \tag{4.2}
\]

The equality follows from \(k=m-q\) and elementary factorial
cancellation.  This proves (0.4).  Section 6 shows that its right side is
\((m-q)/m\) times \(\eta^+_{m,q}\), and hence tends to zero in the
Gaussian window.

The estimate is for the complete one-chip atlas.  Restricting to a
near-perfect middle matching can only decrease the reachable support.

## 5. Exact upper-validity criterion

Consider the \(m+1+q\) positions

\[
                         s_t,s_{t+1},\ldots,s_{t+m+q},
 \qquad 0\le q<m.
 \tag{5.1}
\]

For two positions at distance at most \(m\), the intervening positive gap
sum lies strictly between zero and \(n\), so their symbols are distinct.
For a distance \(m+j\), \(1\le j<m\), the gap sum is

\[
                         n-1+S_j,
 \tag{5.2}
\]

where \(S_j\) is a sum of \(j\) positive parent gaps.  It is less than
\(2n\).  Equality modulo \(n\) occurs exactly when \(S_j=1\), hence
exactly when \(j=1\) and that one parent gap is equal to one.

There are \(q\) possible pairs at distance \(m+1\) inside (5.1).
Periodicity by \(m\) identifies their intervening gaps with
\(z_{t+1},\ldots,z_{t+q}\).  We obtain:

### Theorem 5.1 (upper validity)

The interval (5.1) is a rank-\((m+1+q)\) set if and only if

\[
                         z_{t+1},\ldots,z_{t+q}\ge2.
 \tag{5.3}
\]

Thus its valid quotient-phase count is the number of cyclic length-
\(q\) windows in the parent word containing no part equal to one.

Across all parent classes, summing over their distinct quotient phases is
the same as counting all rooted positive compositions of \(2m\) into
\(m\) parts satisfying (5.3) at the displayed root.  Subtract one from
the first \(q\) parts.  This gives exactly

\[
                         A_{m,q}=\binom{2m-q-1}{m-1},
 \tag{5.4}
\]

including periodic parents with their correct least-period multiplicity.

One valid quotient phase lifts through all \(n\) translations.  It may
hit fewer than \(n\) distinct targets when a target has a stabilizer, and
different phases may collide.  Crediting it with \(n\) distinct targets
is therefore an upper bound.  Equation (5.4) proves (0.6) without any
freeness assumption.

## 6. Gaussian asymptotics and the common obstruction coefficient

Factorial cancellation in (0.6) gives

\[
 \eta^+_{m,q}
 = {\prod_{j=0}^{q+1}(m+j)\over
       \prod_{j=0}^{q}(2m-j)}.
 \tag{6.1}
\]

Taking logarithms and expanding uniformly for \(q=o(m^{2/3})\) yields

\[
 \begin{aligned}
 \log\eta^+_{m,q}
 &=\log m-(q+1)\log2\\
 &\quad+
   \sum_{j=1}^{q+1}\log(1+j/m)
   -\sum_{j=0}^{q}\log(1-j/(2m))\\
 &=\log m-(q+1)\log2+{3q^2\over4m}
   +O\!\left({q\over m}+{q^3\over m^2}\right).
 \end{aligned}
 \tag{6.2}
\]

At \(q=A\sqrt m+O(1)\), the term \(-q\log2\) dominates \(\log m\), so

\[
                         \eta^+_{m,q}
 =\exp\{-A(\log2)\sqrt m+O_A(\log m)\}=o_A(1).
 \tag{6.3}
\]

The lower coefficient in (4.2) uses

\[
 \binom{2m-q-1}{m}
 ={m-q\over m}\binom{2m-q-1}{m-1}.
 \tag{6.4}
\]

Hence it equals \((m-q)\eta^+_{m,q}/m\), proving (0.8).

Finally,

\[
 \log{W\over\binom n{m-q}}
 ={q^2+q\over m}+O(q^3/m^2)
 =A^2+o(1),
 \tag{6.5}
\]

which proves (0.9)--(0.11).

## 7. Incidence and codegree interpretation

For a lower target orbit \(O\), let \({\cal S}_q(O)\) be the multiset of
rooted parent words obtained by choosing a cyclic gap of \(O\), subtracting
one, and splitting the result into \(q+1\) positive parts.  Theorem 3.1
says

\[
                         |{\cal S}_q(O)|=d_q^-(O)
 \tag{7.1}
\]

after quotienting the repeated roots caused by the target stabilizer.
For two target orbits, their exact weighted packet codegree is

\[
 \boxed{
 \lambda_q^-(O,O')
  =\#\{(u,v)\in{\cal S}_q(O)\times{\cal S}_q(O'):
                    [u]=[v]\text{ cyclically}\}.}
 \tag{7.2}
\]

Indeed a pair in (7.2) is exactly a parent packet together with one phase
emitting \(O\) and one phase emitting \(O'\).  This is the literal
codegree, including multiplicities.

No small-codegree theorem can repair the present atlas.  Equations
(3.6) and (4.2) say that \(1-o_A(1)\) of the lower target vertices have
degree zero.  On the upper side, (5.4) says that the total degree of the
entire target layer is already \(o_A(1)\) times its size, even before
collisions are deducted.  The failure therefore precedes Hall expansion,
nibble hypotheses, or phase-discrepancy rounding.

## 8. Exact boundary

The middle and prefix conclusions are now cleanly separated.

* **Middle matching, assumed:** a near-perfect one-chip packet matching
  would give \(W+o(W)\) core plus interface length and only \(o(W)\)
  missing middle owners.
* **Lower Gaussian prefixes, disproved:** almost every target has no
  incident one-chip packet phase because it has no gap of length
  \(q+2\).
* **Upper Gaussian prefixes, disproved:** even the complete packet atlas
  has only \(o(W)\) valid physical occurrences at rank \(m+1+q\).
* **Phase selection, inert:** packet phases permute a fixed incidence
  profile and cannot alter either obstruction.

Thus a near-perfect middle packet matching, if proved, remains valuable as
a component theorem but does not yield a literal Gaussian-annulus OR
compiler.  The physical packet family itself must be enlarged or
rethreaded before a simultaneous all-depth prefix theorem can be true.
