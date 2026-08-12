# Shell-equitable local-minimum quarantine: one entropy charge and the surviving stopped gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver,
probabilistic black box beyond elementary independent priorities, or web
input is used.

Local inputs audited:

- `MATH_THEOREM_MACRO_OVERLAP_QUARANTINE_BY_CONFLICT_THINNING_20260727.md`;
- `MATH_THEOREM_INVERSE_MACRO_THINNING_COVARIANCE_AND_MESOSCOPIC_SURVIVOR_GATE_20260727.md`;
- `MATH_AUDIT_DOMINO_TWIN_SLOW_BITE_TILTED_SPECTRUM_AND_HEREDITY_GATE_20260727.md`; and
- `MATH_THEOREM_DOMINO_TWIN_FACTORIAL_OVERLAP_BOUND_20260727.md`.

## 0. Outcome

Let \({\cal H}\) be the simple domino-twin catalogue, with packet size,
entrance degree, and ground parameters

\[
 K=4m,\qquad n=2m,
\]

\[
 \log D=2m\log m-\beta m+O(\log m),
 \qquad \beta=2+\log2.
\tag{0.1}
\]

For two packets put

\[
                         u(F,G)=K-|F\cap G|.
\tag{0.2}
\]

Assume only the shell hypothesis requested in the question: for fixed
constants \(A,C_I>0\) and \(c<1/2\),

\[
 \boxed{
 N_F(u):=|\{G:u(F,G)=u\}|
 \le e^{C_Im}n^{cu}}
\tag{SH}
\]

for every packet \(F\) and every

\[
                         1\le u\le {Am\over\log m}.
\tag{0.3}
\]

The corresponding cumulative count satisfies

\[
 M_F(u):=|\{G:u(F,G)\le u\}|
 \le u\,e^{C_Im}n^{cu}.
\tag{0.3a}
\]

The additional factor \(u\) is polynomial and will be retained as an
\(O(\log m)\) term; it is not a second entropy charge.

Put \(\delta=1/2-c\).  The exact conclusion has a positive macro part
and a negative stopped part.

### Theorem A (incidence-weighted shell-equitable thinning)

Choose

\[
 u_0=\left\lceil{Bm\over\log m}\right\rceil,
 \qquad B<A,
\tag{0.4}
\]

and join two packets when \(u(F,G)<u_0\).  Give the vertices of this
conflict graph independent continuous priorities and retain a packet
when it is the unique minimum in its closed neighbourhood.  If
\(\Delta\) is the conflict degree and

\[
                         \rho={1\over\Delta+1},
\tag{0.5}
\]

then some priority realization has simultaneously:

1. every entrance degree

   \[
                         d'(X)=(1+o(1))\rho D;
   \tag{0.6}
   \]

2. no retained pair with deficit below \(u_0\); and

3. an exceptional family \({\cal Q}\) of retained incidences
   \((X,F)\), of relative incidence mass

   \[
      { |{\cal Q}|\over\sum_Xd'(X)}
      =O\left({1\over m\log m}\right)=o(1/K),
   \tag{0.7}
   \]

   outside which every exact shell

   \[
    a'_u(X,F)=|\{G\ni X:G\text{ retained},\ u(F,G)=u\}|
   \]

   obeys

   \[
    \boxed{
    a'_u(X,F)\le m^2\rho\,a_u(X,F)}
    \tag{0.8}
   \]

   for all
   \(u_0\le u\le Am/\log m\).  Here \(a_u(X,F)\) is the
   corresponding shell size before thinning.

Thus degrees lose one factor \(\rho\), while every monitored shell loses
the same factor \(\rho\), up to a polynomial slack and an
\(o(1/K)\) weighted quarantine.  In particular, after normalization by
the retained degree, the factor \(\rho\) cancels.  The inverse entropy
in (SH) is not paid a second time.

The proportional assertion is two-sided in joint-retention expectation
and one-sided after deterministic quarantine.  Literal two-sided
pointwise proportionality is impossible for a shell of size one when
\(\rho=o(1)\): its retained size is an integer, not
\((1+o(1))\rho\).  The upper form (0.8) is the form needed by the
survivor kernel.

### Theorem B (macro survivor kernel)

For a nonexceptional retained incidence define

\[
 {\cal K}^{\rm mac}_{X,F}(z)
 ={1\over \rho D}
 \sum_{\substack{G\ni X,\ G\text{ retained}\\
       u_0\le u(F,G)\le Am/\log m}}
 z^{-(|F\cap G|-1)}.
\tag{0.9}
\]

At \(z=m^{-1/2}\), if

\[
 \boxed{
 \delta B>C_I+\beta+\eta}
\tag{0.10}
\]

for some \(\eta>0\), then

\[
 \boxed{
 {\cal K}^{\rm mac}_{X,F}(m^{-1/2})
 \le e^{-(\eta-o(1))m}}
\tag{0.11}
\]

uniformly outside \({\cal Q}\).  The same holds, more strongly, for
\(z=C_\star m^{-1/2}\) with \(C_\star\ge1\).

This is the desired shell-equitable **macro** quarantine.  It uses each
shell bound once, not once to colour and again to estimate the retained
kernel.

### Theorem C (the stopped near-factor implication is false from (SH))

The hypothesis (SH), even together with Theorems A--B, does not imply a
stopped domino-twin near-factor condition.

1. At the literal unit density,

   \[
    \boxed{
    \log\bigl((\rho D)m^{-(K-1)/2}\bigr)
    \le-\beta m+O(\log m),}
   \tag{0.12}
   \]

   so the product-reference entrance degree is exponentially below one
   even before accounting for the thinning loss.

2. The shell hypothesis is silent when

   \[
                 u(F,G)>Am/\log m.
   \tag{0.13}
   \]

   A mesoscopic normalized overlap mass at
   \(|F\cap G|-1=\lfloor\sqrt m\rfloor\) satisfies (SH) vacuously but
   contributes

   \[
                 \exp\bigl((1/2+o(1))\sqrt m\log m\bigr)
   \tag{0.14}
   \]

   to the square-root survivor kernel.

3. Static shell equitability is not hereditary under the stopped
   matching filtration.  It gives no sign or concentration for the
   current-residual shell hazards or their common next-edge columns.

Thus \(c<1/2\) proves exactly the macro endpoint (0.11), but cannot by
itself prove the stopped near-factor.  A corrected square-root route
must use \(z=C_\star m^{-1/2}\) with \(C_\star\) large enough to restore
degree, and must add both a mesoscopic survivor estimate and a
trajectory-specific shell-hazard theorem.

## 1. Conflict graph and marginal degree

Let \(\Gamma\) be the graph on packets in which

\[
                         F\sim G\iff u(F,G)<u_0.
\tag{1.1}
\]

Coordinate transitivity makes \(\Gamma\) regular.  By (SH),

\[
                         \Delta+1
                         \le u_0e^{C_Im}n^{cu_0}.
\tag{1.2}
\]

Give all packets independent uniform priorities in \([0,1]\), and
retain \(F\) precisely when its priority is smaller than the priorities
of all its neighbours.  Every packet is retained with probability

\[
                         \rho={1\over\Delta+1}.
\tag{1.3}
\]

For a fixed entrance target \(X\), its retained degree is a sum of
\(D\) indicators.  Two indicators are independent when their conflict
vertices have graph distance greater than two, so a dependency graph has
maximum degree at most \((\Delta+1)^2\).  Colouring that dependency
graph and applying the elementary Hoeffding inequality inside its colour
classes gives

\[
 \Pr\bigl(|d'(X)-\rho D|>\varepsilon\rho D\bigr)
 \le2\exp\left[-c_0\varepsilon^2
 {D\over(\Delta+1)^4}\right].
\tag{1.4}
\]

Equations (0.1), (1.2), and \(u_0=O(m/\log m)\) make the exponent in
(1.4) factorially large.  It dominates the \(\exp(O(m))\) entrance
targets.  Hence (0.6) holds simultaneously with probability \(1-o(1)\).

The independent-set property gives the second conclusion of Theorem A.

## 2. Joint retention without a second entropy loss

The needed fact is elementary.

### Lemma 2.1 (joint local-minimum bound)

If \(F,G\) are distinct nonadjacent vertices of a \(\Delta\)-regular
graph, then

\[
 \boxed{
 \rho^2\le
 \Pr(F,G\text{ both retained})
 \le {2\over(\Delta+1)(\Delta+2)}
 \le2\rho^2.}
\tag{2.1}
\]

Consequently

\[
 \rho\le
 \Pr(G\text{ retained}\mid F\text{ retained})\le2\rho.
\tag{2.2}
\]

#### Proof

Let \(a\) be the number of common conflict neighbours of \(F,G\).
Conditional on priorities \(x\le y\), all \(\Delta\) neighbours of
\(G\) must exceed \(y\), while the neighbours exclusive to \(F\) must
exceed \(x\).  Hence

\[
 \begin{aligned}
 \Pr(F,G\text{ retained})
 &=2\int_0^1(1-y)^\Delta
       \int_0^y(1-x)^{\Delta-a}\,dx\,dy\\
 &\le2\int_0^1y(1-y)^\Delta\,dy
 ={2\over(\Delta+1)(\Delta+2)}.
 \end{aligned}
\]

The displayed integral is nondecreasing in \(a\).  At \(a=0\) the two
closed neighbourhoods are disjoint and the probability is exactly
\(\rho^2\).  This proves the lower bound.

Divide by \(\Pr(F\text{ retained})=\rho\) to obtain (2.2).
\(\square\)

For a fixed incidence \((X,F)\), conditional on \(F\) being retained,
linearity and (2.2) give

\[
 \rho a_u(X,F)
 \le \mathbb E[a'_u(X,F)\mid F\text{ retained}]
 \le2\rho a_u(X,F).
\tag{2.3}
\]

This conditional estimate is where the colouring loss cancels.  It
would be incorrect to divide the original shell bound by \(\Delta+1\)
and then pay \(\Delta+1\) once more when normalizing the retained
degree.

## 3. Simultaneous shells after an incidence quarantine

Call the retained incidence \((X,F)\) bad at shell \(u\) when

\[
                         a'_u(X,F)>m^2\rho a_u(X,F).
\tag{3.1}
\]

If \(a_u(X,F)=0\), it is never bad.  Otherwise (2.3) and Markov's
inequality give

\[
 \Pr((X,F)\text{ bad at }u\mid F\text{ retained})
 \le {2\over m^2}.
\tag{3.2}
\]

There are at most \(Am/\log m\) monitored shells.  Summing (3.2) over
all entrance incidences and all shells gives expected bad-incidence
mass at most

\[
 O\left({1\over m\log m}\right)
 \mathbb E\sum_Xd'(X).
\tag{3.3}
\]

One more application of Markov's inequality, intersected with the
overwhelming-probability degree event in Section 1, supplies one
priority realization for which the union \({\cal Q}\) of all bad
incidences satisfies (0.7).  Every incidence outside \({\cal Q}\)
satisfies all monitored shell inequalities (0.8) simultaneously.

This is stronger than merely controlling the sum over shells, and the
polynomial factor \(m^2\) contributes only \(O(\log m)\) to a survivor
exponent.  The price is correctly recorded as an incidence-weighted
quarantine rather than an unsupported pointwise assertion at every
packet.

There is also a purely averaged version with no quarantine.  If

\[
 A_u=\sum_X\sum_{F\ni X}a_u(X,F),\qquad
 A'_u=\sum_X\sum_{\substack{F\ni X\\F\text{ retained}}}a'_u(X,F),
\]

then Lemma 2.1 gives

\[
                         \mathbb EA'_u\le2\rho^2A_u.
\tag{3.4}
\]

After division by the retained incidence and degree scales
\(\rho\sum_XD\) and \(\rho D\), the two powers of \(\rho\) cancel
exactly.

## 4. Computing the macro survivor kernel

For a nonexceptional retained incidence, (0.8), (SH), and
\(a_u(X,F)\le N_F(u)\) give

\[
 \begin{aligned}
 {\cal K}^{\rm mac}_{X,F}(z)
 &\le {m^2\over D}
 \sum_{u=u_0}^{\lfloor Am/\log m\rfloor}
 e^{C_Im}n^{cu}z^{-(K-u-1)}.
 \end{aligned}
\tag{4.1}
\]

There is no \(\rho\) on the right side.  This is the promised single
entropy charge.

At \(z=m^{-1/2}\), the logarithm of the \(u\)-summand, including
\(D^{-1}\), is

\[
 \begin{aligned}
 &C_Im+cu\log n+{K-u-1\over2}\log m-\log D+O(\log m)\\
 &\qquad\le
 -\delta u\log m+(C_I+\beta)m+o(m).
 \end{aligned}
\tag{4.2}

It decreases geometrically in \(u\).  At
\(u=u_0=Bm/\log m+O(1)\), condition (0.10) makes (4.2) at most
\(-\eta m+o(m)\).  The number of shells is polynomial, so (0.11)
follows.

The interval in (0.4) exists only if

\[
                         \delta A>C_I+\beta+\eta.
\tag{4.3}
\]

This is the exact quantitative condition on the assumed shell range.
The bare statement \(c<1/2\) is insufficient if the proved range
constant \(A\) is too small relative to the exponential prefactor.

## 5. Degree at the square-root stop

At the unit constant,

\[
 \begin{aligned}
 \log\bigl((\rho D)m^{-(K-1)/2}\bigr)
 &\le\log D-{K-1\over2}\log m\\
 &=-\beta m+O(\log m),
 \end{aligned}
\tag{5.1}

proving (0.12).  Local-minimum thinning can only reduce this degree.
Thus no product-reference slow bite can have a large current link at
literal \(z=m^{-1/2}\).

At

\[
                         z={C_\star\over\sqrt m},
\tag{5.2}
\]

the shell calculation only improves, while (1.2) gives

\[
 \log\bigl((\rho D)z^{K-1}\bigr)
 \ge
 \bigl(4\log C_\star-\beta-C_I-cB-o(1)\bigr)m.
\tag{5.3}
\]

Hence a factorially large stopped reference degree requires

\[
                         4\log C_\star>
                         \beta+C_I+cB.
\tag{5.4}
\]

This still corresponds to leave \(O(N/\sqrt m)\), but it is not the
unit-constant claim.

## 6. Why the full survivor kernel does not follow

The macro shell hypothesis controls overlaps

\[
 |F\cap G|\ge K-{Am\over\log m}.
\tag{6.1}
\]

It says nothing about the mesoscopic range.  The logical separation is
already visible in a normalized overlap law.  Put

\[
                         j_0=\lfloor\sqrt m\rfloor
\]

and give mass

\[
                         \varepsilon_m=e^{-(\log m)^2}
\tag{6.2}
\]

to \(j=|F\cap G|-1=j_0\), with the remaining mass at \(j=0\).  This
law has no pair in (6.1), so it obeys every assumed macro shell bound.
But at \(z=m^{-1/2}\),

\[
 \log\bigl(\varepsilon_mz^{-j_0}\bigr)
 ={1\over2}\sqrt m\log m-(\log m)^2+O(\log m)
 \longrightarrow+\infty.
\tag{6.3}
\]

This is an abstract logical countermodel, not a claim that the law is
realized by the physical domino catalogue.  It proves that (SH) alone
cannot imply the full survivor-kernel estimate.  A physical proof must
add a mesoscopic inverse theorem.

## 7. Why static shell equitability is not stopped regeneration

Let \(N_{u,t}(X,F)\) be the current number of surviving link rows in
shell \(u\), and let \(h_{u,t}\) be their conditional death hazard.
If \(z_t\) is the global residual density and
\(h_t=-\dot z_t/z_t\), the exactly compensated shell variable is

\[
                         Y_{u,t}
 =N_{u,t}z_t^{-u},
\tag{7.1}
\]

or, in overlap coordinates \(j=K-u-1\), the equivalent compensated
variable \(N_{j,t}z_t^{-(K-1-j)}\).  Its logarithmic generator contains

\[
                         h_{u,t}-u h_t.
\tag{7.2}
\]

The static inequalities (0.8) and (0.11) give no sign or integrated
bound for (7.2).  A possible next selected packet can meet primarily
the zero-overlap rows or primarily one monitored shell while both states
have the same time-zero shell census.  Thus current residuals can lose
shell equitability even though the initial thinned catalogue is perfectly
equitable in the incidence-weighted sense proved above.

The missing dynamic input is an incidence-weighted stopped statement of
the form

\[
 \int_0^T|h_{u,t}-u h_t|\,dt=o(1)
\tag{7.3}
\]

on every survivor-relevant shell, together with common next-edge column
moments.  Neither follows from (SH) or from independent-priority
thinning.

## 8. Exact implication boundary

From (SH) with \(c<1/2\), proved:

1. a local-minimum conflict thinning with simultaneous entrance-degree
   preservation;
2. proportional reduction of every monitored overlap shell outside an
   \(o(1/K)\) incidence quarantine;
3. cancellation of the thinning factor in the normalized shell profile;
4. the exact macro survivor estimate (0.11), without double-counting
   entropy; and
5. the quantitative range condition (4.3).

Refuted from (SH) alone:

1. a unit-constant square-root degree corridor;
2. control of the mesoscopic survivor kernel;
3. hereditary shell equitability in the stopped residual; and
4. the stopped domino-twin near-factor condition.

The shell exponent \(c<1/2\) is therefore precisely sufficient for the
static macro-overlap quarantine, but not for the requested stopped
near-factor theorem.  The remaining gates are degree normalization,
mesoscopic inverse control, and trajectory-specific shell hazards—not a
second payment of the macro entropy.
