# ST terminal sector: an actual singleton-phase critical family

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Result

This note concerns the surviving zero-winding PBBS sector

\[
 p,q,b\asymp \sqrt r,\qquad y_p=1,
 \qquad b=2q-p+1,
\]

and the transported phase sets above its one-defect terminal rotor.

There is an infinite family of **actual canonical PBBS roots** for which

1. \(q=b=p-1\), so the terminal rotor period is the outer return
   duration \(s=2p-1\);
2. the root has a first zero-winding return of duration \(s\), terminal
   curvature \(y_p=1\), and positive endpoint excess exactly \(2p\);
3. among a whole terminal-rotor period, phase zero is the only phase which
   starts the outer duration-\(s\) return;
4. phase zero is a genuine positive-boundary run exit, created by a
   nonempty external dual shoulder \(T_s\);
5. on each quotient orbit, every constructed start has at most two
   conflicting constructed neighbours; hence at least one third of all
   corresponding return intervals can be retained pairwise
   quotient-edge-disjointly.

Consequently the transported-union and rightmost-exit masses are exactly
the start mass, while the actual packing loses at most a factor three:

\[
 U=S=\#\{\hbox{fillers}\},\qquad
 {S\over3}\le\operatorname {Pack}\le S.
\]

In particular a literal projected-edge-disjoint subfamily of at least one
third this cardinality is a lower bound for the quotient packing number
\(\overline\nu_H(P_r)\) whenever \(H\ge s+1\).

For every fixed Gaussian window large enough to contain the chosen
critical ratio, one can choose the filler height so that the family has

\[
 \#\{\hbox{fillers}\}\ge c_A\frac{4^M}{M^2},
\]

where its ambient semilength is

\[
 r=M+3p-1=M+\Theta_A(\sqrt M).
\]

Thus this family is still
\(\exp[-\Theta_A(\sqrt r)]\) below the coefficient-one critical scale
\(4^r/r^2\).  It does **not** refute \(\mathrm{ST}_A\) or the aggregate
transported-union estimate.  It does rigorously rule out every proof which
tries to obtain the missing little-oh from a pointwise lower bound on
phase multiplicity, from the terminal rotor, from positivity of the first
external shoulder, or from edge-disjointness alone.  A successful proof
must use the global rarity of these singleton-phase contexts or a
cross-context incidence theorem.

## 1. The family

Let \(p\ge3\), and put

\[
 h=p-2,\qquad s=2p-1,\qquad q=s-p=p-1,
 \qquad b=2q-p+1=p-1.
 \tag{1.1}
\]

Let \(F\) be any Dyck word of semilength \(M\) and exact height \(h\).
Define

\[
 \boxed{
 D(F)=1^p0^p1^{2p-1}0^{p+1}F0^{p-2}.}
 \tag{1.2}
\]

Its semilength is

\[
 r=M+3p-1.                                         \tag{1.3}
\]

The word in (1.2) is the specialization

\[
 1^{s-p+1}0^p1^{2p-1}0^{s-h}F0^h
\]

of the audited buffered critical-return family, at the extremal values
\(s=2p-1\) and \(h=p-2\).  The earlier word calculation therefore gives
a genuine first zero-winding PBBS return of duration \(s\) at phase zero.
For completeness, the exact facts needed below are recorded and then used
without any capacity-envelope interpretation.

Simultaneous peak deletion gives

\[
 \partial^{p-1}D(F)=10\,1^p0^p.                  \tag{1.4}
\]

One further deletion gives \(M_q=1^q0^q\), where \(q=p-1\).  Hence the
first mountain depth is \(p\).  At the last three profile ranks,

\[
 r_{p-1}=q+2,\qquad r_p=q,\qquad r_{p+1}=q-1,
\]

so

\[
 \boxed{y_p=r_{p-1}-2r_p+r_{p+1}=1.}             \tag{1.5}
\]

The terminal state in (1.4) is the rotor state \(A_0\).  The one-defect
mountain rotor has period

\[
 2q+1=2p-1=s.                                     \tag{1.6}
\]

A top start requires \(p\) consecutive good terminal starts.  Starting
from \(A_0\), exactly the phases

\[
 I=\{0,1,\ldots,p-2\}                             \tag{1.7}
\]

avoid the unique bad rotor state.  Thus every phase outside \(I\) is
already invalid at the terminal level.

## 2. Exact exclusion of every other admissible phase

Write

\[
 a_k=\delta(\tau^kD(F)).
\]

The direct first-maximum calculation for the buffered family gives

\[
 a_k=s+2p\qquad(0\le k\le h=p-2).                \tag{2.1}
\]

Its internal dual staircase array has exactly one nonempty block before
the endpoint:

\[
 |T_{p-2}|=2p.                                    \tag{2.2}
\]

Let \(\delta_F\) be the first position at which \(F\) reaches height
\(h\).  At the first excluded continuation a new external dual block is
created at index \(s\), with

\[
 |T_s|=2M+h-\delta_F.                             \tag{2.3}
\]

After its first height-\(h\) visit, \(F\) has at least \(h\) down-steps
remaining.  Therefore

\[
 \delta_F\le2M-h,
 \qquad |T_s|\ge2h>0.                             \tag{2.4}
\]

For an actual PBBS orbit, define the exact zero-winding cocycle

\[
 \mathcal F_s(k)
 =a_k-s-\sum_{i=k}^{k+s-1}|T_i|.                 \tag{2.5}
\]

A phase \(k\) starts the duration-\(s\) zero-winding return if and only if
\(\mathcal F_s(k)=0\).  At phase zero, the window contains (2.2) and
does not contain (2.3), so

\[
 \mathcal F_s(0)=(s+2p)-s-2p=0.                 \tag{2.6}
\]

Now let \(1\le k\le p-2\).  The interval
\([k,k+s-1]\) contains both indices \(p-2\) and \(s\).  All omitted
dual-block lengths in (2.5) are nonnegative.  Equations (2.1)--(2.3)
therefore give the strict bound

\[
 \begin{aligned}
 \mathcal F_s(k)
 &\le (s+2p)-s-|T_{p-2}|-|T_s|\\
 &=-|T_s|<0.                                      \tag{2.7}
 \end{aligned}
\]

Thus no phase in \(I\setminus\{0\}\) starts the outer return.  Every
phase in \(\{p-1,\ldots,s-1\}\) is terminally invalid by (1.7).  We have
proved the exact singleton statement

\[
 \boxed{
 \{0\le k<s:\tau^kD(F)\text{ starts the duration-}s
                    \text{ zero-winding return}\}=\{0\}.}
 \tag{2.8}
\]

In particular \(D(F)\) is a run exit: it starts, whereas \(\tau D(F)\)
does not.

## 3. Positive endpoint boundary and the external shoulder

The endpoint first-maximum positions are

\[
 a_0=s+2p,
 \qquad a_s=2M+s+2p.                             \tag{3.1}
\]

Using \(r=M+s+p\), which agrees with (1.3), the endpoint excess is

\[
 \boxed{
 a_0+a_s-2r=2p>0.}                               \tag{3.2}
\]

The failure at the next phase is not a terminal-rotor artefact: (2.3) is
the literal external dual shoulder, and

\[
 d(\phi\tau^sD(F))=|T_s|+1\ge2h+1\ge3.          \tag{3.3}
\]

Hence these are actual members of the positive-boundary rightmost-exit
sector used in the transported-union reduction.

For a constructed root viewed in its transported reference fibre, let
\(\mu(D(F))\) be the number of admissible top phases.  Equation (2.8)
gives

\[
 \boxed{\mu(D(F))=1.}                             \tag{3.4}
\]

Therefore, on this family, phase membership mass, transported-union mass,
and rightmost-exit mass are identical.

## 4. The conflict graph has degree at most two

Let \(F\ne F'\), and suppose that \(D(F)\) and \(D(F')\) lie on the same
quotient orbit.  Peak deletion commutes with \(\tau\), so the full pruning
profile is constant along an orbit.  If the forward cyclic distance from
\(D(F)\) to \(D(F')\) were an integer \(k\) with \(1\le k<s\), then
\(\tau^kD(F)=D(F')\) would start the duration-\(s\) return.  This
contradicts (2.8).  Applying the same argument with \(F,F'\) reversed
excludes a backward cyclic distance below \(s\).

Thus distinct constructed starts on one quotient cycle have cyclic
separation at least \(s\) in both directions.  A duration-\(s\) positive
residence has a full trace of \(s+2\) quotient edges, so starts at exact
separation \(s\) can share two boundary edges.  The preceding argument
does not prove that the whole family is edge-disjoint.

All constructed roots have the same terminal state \(A_0\), whose exact
rotor period is \(s\).  Hence two constructed starts on one quotient orbit
are separated by an integral multiple of \(s\).  Intervals separated by
at least \(2s\) are disjoint because \(s+2\le2s\) for \(s\ge2\).  Each
constructed interval can therefore conflict only with the immediately
preceding and immediately following constructed starts.  The conflict
graph has maximum degree at most two.  Greedy three-colouring, separately
on every quotient orbit, gives

\[
 \boxed{
 \operatorname {Pack}\{I(F):\operatorname{ht}(F)=h\}
 \ge {1\over3}\#\{F:|F|=2M,\operatorname{ht}(F)=h\}.}        \tag{4.1}
\]

Thus the general phase-union packing comparison loses only an absolute
constant on this family.  No factor-one assertion is made.

## 5. A critical exact-height shell

Let \(C_a(M)\) be the number of semilength-\(M\) Dyck paths of height at
most \(a\), and put

\[
 E_{M,h}=C_h(M)-C_{h-1}(M).                       \tag{5.1}
\]

We recall an elementary consequence of the path-graph spectral formula.

### Lemma 5.1 (one large Gaussian height shell)

For every fixed \(0<\alpha<\beta<\infty\), there is
\(c_{\alpha,\beta}>0\) such that, for all sufficiently large \(M\), some
integer

\[
 \alpha\sqrt M\le h\le\beta\sqrt M
\]

satisfies

\[
 \boxed{E_{M,h}\ge c_{\alpha,\beta}\,4^M/M^2.}  \tag{5.2}
\]

#### Proof

The exact bounded-height formula is

\[
 C_a(M)=\frac{2}{a+2}\sum_{j=1}^{a+1}
 \sin^2\!\frac{\pi j}{a+2}
 \left(2\cos\frac{\pi j}{a+2}\right)^{2M}.       \tag{5.3}
\]

Pairing the two ends of the spectrum and using dominated convergence
shows that, for every fixed \(c>0\),

\[
 \frac{C_{\lfloor c\sqrt M\rfloor}(M)}{\operatorname {Cat}_M}
 \longrightarrow
 \Psi(c):=\frac{4\pi^{5/2}}{c^3}
       \sum_{j\ge1}j^2e^{-\pi^2j^2/c^2}.          \tag{5.4}
\]

The function \(\Psi\) is analytic and nondecreasing on \((0,\infty)\),
with limits zero and one at the two ends.  Hence it is strictly increasing:
equality at two distinct points would make it constant on an interval,
and analyticity would then make it constant everywhere.  Therefore

\[
 C_{\lfloor\beta\sqrt M\rfloor}(M)
 -C_{\lceil\alpha\sqrt M\rceil-1}(M)
 \ge c'_{\alpha,\beta}\operatorname {Cat}_M      \tag{5.5}
\]

for large \(M\).  The left side is the sum of at most
\((\beta-\alpha)\sqrt M+2\) quantities \(E_{M,h}\).  Pigeonhole and
\(\operatorname {Cat}_M\asymp4^M/M^{3/2}\) prove (5.2). \(\square\)

Fix \(A>0\), and choose

\[
 0<\alpha<\beta<A/2.                              \tag{5.6}
\]

For the shell supplied by Lemma 5.1, set \(p=h+2\) and use (1.2).  Then

\[
 p,q,b\asymp_{A,\alpha,\beta}\sqrt r,
 \qquad s+1\le H=\lceil A\sqrt r\rceil           \tag{5.7}
\]

for all sufficiently large \(M\), and (4.1)--(5.2) give an actual
edge-disjoint lower bound

\[
 \boxed{
 \operatorname {Pack}\ge c_{A,\alpha,\beta}\frac{4^M}{M^2}.}
 \tag{5.8}
\]

Equivalently, with \(H=\lceil A\sqrt r\rceil\),

\[
 \overline\nu_H(P_r)
 \ge c_{A,\alpha,\beta}\frac{4^M}{M^2}.           \tag{5.8a}
\]

Since \(r-M=3p-1=\Theta(\sqrt r)\), this is

\[
 \frac{4^M}{M^2}
 =\frac{4^r}{r^2}\exp[-\Theta_{A,\alpha,\beta}(\sqrt r)].
 \tag{5.9}
\]

Thus (5.8) is not a coefficient-one obstruction, but it is an actual
PBBS obstruction at every local gate named in Sections 1--4.

## 6. Exact implication boundary

The theorem proves:

1. terminal curvature one and a \(\Theta(\sqrt r)\)-phase rotor do not
   force more than one lifted outer phase;
2. positive endpoint boundary, even of critical size \(2p\), does not
   force phase persistence;
3. the external-shoulder exit injection can be exactly one-to-one;
4. cyclic interval selection costs at most an absolute factor three;
5. these four statements hold simultaneously in actual canonical PBBS
   chronology, not only in a capacity envelope.

What remains open is aggregate.  The deterministic active collar in
(1.2) has semilength \(3p-1\), producing the factor
\(4^{-(3p-1)}=\exp[-\Theta(\sqrt r)]\) in (5.9).  Therefore the family
does not show that singleton-phase contexts have critical total mass.
The weighted transported-union estimate can now be proved only by one of
the following genuinely global statements:

- a theorem that every singleton-phase context pays a global
  \(\exp[-\omega(1)]\) or other vanishing context-density penalty;
- a cross-context incidence theorem forcing critical-mass contexts to
  share charged canonical edges; or
- a direct count of positive-boundary exits which uses data outside the
  terminal rotor, the first external shoulder, and the individual orbit.

No such aggregate theorem is proved here.  Accordingly
\(\mathrm{ST}_A\), the weighted transported-union estimate, and the
constant-one theorem remain open.

## 7. Adversarial audit

1. **Actual roots, not capacity tuples.**  Every object is the literal
   word (1.2).  The proof uses the already verified PBBS rotation and
   staircase formulas for that word; no arbitrary weak-composition tuple
   is declared realizable.

2. **Later dual blocks are harmless in the correct direction.**  For
   \(k>0\), the cocycle window can contain blocks after \(T_s\) which were
   not listed explicitly.  They enter (2.5) with a minus sign.  Inequality
   (2.7), rather than an equality, deliberately retains them and therefore
   remains valid.

3. **The terminal interval is exact.**  Here
   \(\partial^{p-1}D=A_0\), the rotor period is \(s=2p-1\), and a block of
   \(p\) good terminal starts avoids \(B_0\) exactly for starting phases
   \(0,\ldots,p-2\).  No phase outside that interval is silently assigned
   an upper-level failure.

4. **Cyclic conflict control uses both directions.**  On a common orbit,
   (2.8) applied first to \(D(F)\) and then to \(D(F')\) makes both cyclic
   gaps at least \(s\).  Together with the exact terminal-rotor period,
   this gives degree at most two, not whole-family disjointness.

5. **No asymptotic overclaim.**  The exact-height shell is of order
   \(4^M/M^2\), whereas the ambient rank is \(M+3p-1\).  The missing
   factor \(4^{3p-1}\) is retained explicitly; it is precisely why the
   construction is a local obstruction and not a counterexample to
   \(\mathrm{ST}_A\).
