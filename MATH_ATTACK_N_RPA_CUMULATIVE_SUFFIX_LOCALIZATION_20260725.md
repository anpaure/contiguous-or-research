# Lane N: cumulative-suffix localization for Gaussian PBBS returns

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2r+1,
 \qquad B=\operatorname{Cat}_r,
 \qquad H_A=\lceil A\sqrt r\rceil,
\]

where \(A>0\) is fixed.  Let \(\tau=\phi^2\) be the normalized
step-two PBBS permutation.  For a zero-winding return at step-two time
\(s\), write

\[
 D_j=\tau^jD_0=P_j1R_j0S_j,
 \qquad 0\le j\le s,
\tag{0.1}
\]

using the canonical first-maximum factorization.  Since \(S_j\) is Dyck,
write

\[
 \sigma_j=\frac{|S_j|}{2}
\tag{0.2}
\]

for its semilength, and define the cumulative terminal-suffix mass

\[
 \Sigma(D_0,s)=\sum_{j=0}^{s-1}\sigma_j.
\tag{0.3}
\]

For an arbitrary return, let \(a\ge0\) be its two-step winding.  The exact
return equation is

\[
 \boxed{s+2\Sigma(D_0,s)=\delta(D_s)+aN.}
\tag{0.4}
\]

Here \(\delta(D_s)\) is the first position at which \(D_s\) reaches its
global maximum.  Zero winding is the case \(a=0\).

This note proves a quantitative localization which strictly extends the
previous persistent-unit-deficit estimate.

> **Cumulative-suffix localization.**  There is an absolute constant
> \(K_0>0\) such that, for every fixed \(A>0\), all but
> \(o_A(B/N)\) return starts of arbitrary winding with \(s\le H_A\)
> satisfy
> \[
>  \boxed{
>  \Sigma(D_0,s)\ge
>       \frac{r}{8K_0(\log r)^2}.}
> \tag{0.5}
> \]
> Consequently at least one quotient edge of the return has
> \[
>  \boxed{
>   \sigma_j\ge
>   \frac{\sqrt r}{16K_0(A+1)(\log r)^2},
>  }
> \tag{0.6}
> \]
> and hence canonical deficit
> \[
>  d(D_j)=|S_j|+1=2\sigma_j+1
>  \ge
>  \frac{\sqrt r}{8K_0(A+1)(\log r)^2}+1.
> \tag{0.7}
> \]

Thus every potentially critical Gaussian predecessor passage
must traverse a mesoscopic terminal-sector spike.  Persistent unit deficit,
bounded total suffix mass, and indeed total suffix mass
\(O(r/(\log r)^2)\) with a sufficiently small absolute constant are all
negligible at the full quotient target scale \(B/N\).

This proves neither \((\mathrm{CP}_A)\) nor the stronger
\((\mathrm{RP}_A)\).  A mesoscopic spike is not itself rare enough under
Catalan measure to close the packing estimate.  The exact remaining gate
is nevertheless narrower: bounded-slot predecessor passages in the Pascal
saddle must also carry the spike (0.6), and their dynamically compatible
weighted density is still unproved.

## 1. Exact winding identity

For a Dyck root \(D\), the first-maximum factorization

\[
 D=P1R0S
\tag{1.1}
\]

has

\[
 d(D)=|S|+1,
 \qquad
 \delta(D)=|P|+1,
 \qquad
 \tau D=S1P0R.
\tag{1.2}
\]

If \(D_0\) returns after \(2s+1\) ordinary PBBS steps with winding \(a\),
the exact quotient equation is

\[
 \sum_{j=0}^{s-1}d(D_j)=\delta(D_s)+aN.
\tag{1.3}
\]

Using \(d(D_j)=2\sigma_j+1\) in (1.3) gives (0.4).  No static-sector
transport or converse from \(d(D_0)=1\) is used here.  In particular this
argument is unaffected by the counterexample to the proposed primitive
zero-winding converse.

## 2. Early first maxima

Let \(M_{r,t}\) be the number of semilength-\(r\) Dyck paths whose first
visit to their global maximum occurs at step \(t\).  The audited
prefix/spectral theorem in
`PBBS_PERSISTENT_PRIMITIVE_RETURN_BOUND_20260725.md` gives absolute
constants \(c,C>0\) such that

\[
 \boxed{
 M_{r,t}\le Cr^2 4^r
       \exp\!\left[-c\sqrt{\frac rt}\right]}
 \qquad(1\le t\le r).
\tag{2.1}
\]

The next theorem converts this endpoint estimate into a complete
trajectory estimate.  It is important that the price is only the explicit
\(HT\) union factor; no independence of the intermediate suffixes is
assumed.

### Theorem 2.1 (uniform thin-trajectory count)

For integers \(1\le H,T\le r\), let

\[
 \mathcal Z_r(H,T)
 =\left\{D_0:\begin{array}{l}
   D_0\text{ starts a zero-winding return at some step-two time }s,\\
   1\le s\le H,\quad \delta(\tau^sD_0)\le T
  \end{array}\right\}.
\tag{2.2}
\]

Then

\[
 \boxed{
 |\mathcal Z_r(H,T)|
 \le CHTr^2 4^r
       \exp\!\left[-c\sqrt{\frac rT}\right].}
\tag{2.3}
\]

#### Proof

Fix \(s\le H\) and \(t\le T\).  Since \(\tau\) is a permutation of
\(\mathcal D_r\), the map

\[
 D_0\longmapsto D_s=\tau^sD_0
\tag{2.4}
\]

is injective.  Every image under consideration has first global maximum at
step \(t\), so there are at most \(M_{r,t}\) such starts.  Sum this bound
over the at most \(HT\) pairs \((s,t)\).  Since the right side of (2.1) is
increasing in \(t\), it is at most its value at \(T\) throughout the sum.
This proves (2.3).  Notice that a start counted for more than one pair only
makes the union bound larger.  \(\square\)

## 3. The full (B/N)-scale localization

Choose an absolute constant \(K_0\) so large that

\[
 \boxed{c\sqrt{K_0}>7,}
\tag{3.1}
\]

where \(c\) is the absolute constant in (2.1), and put

\[
 T_r=\left\lfloor\frac{r}{K_0(\log r)^2}\right\rfloor.
\tag{3.2}
\]

### Theorem 3.1 (negligibility of low cumulative suffix mass)

For every fixed \(A>0\),

\[
 \boxed{
 |\mathcal Z_r(H_A,T_r)|=o_A(B/N).}
\tag{3.3}
\]

#### Proof

For all sufficiently large \(r\), \(T_r\ge1\), and

\[
 H_A\le(A+1)\sqrt r,
 \qquad
 T_r\le r,
 \qquad
 \sqrt{r/T_r}\ge\sqrt{K_0}\log r.
\tag{3.4}
\]

Theorem 2.1 therefore gives

\[
 |\mathcal Z_r(H_A,T_r)|
 \le C_A r^{7/2}4^r r^{-c\sqrt{K_0}}.
\tag{3.5}
\]

The Catalan estimate

\[
 B/N\asymp 4^r r^{-5/2}
\tag{3.6}
\]

turns the ratio of (3.5) to (B/N) into

\[
 O_A\!\left(r^{6-c\sqrt{K_0}}\right)=o_A(1)
\tag{3.7}
\]

by (3.1).  This proves (3.3).  \(\square\)

### Corollary 3.2 (mesoscopic spike)

Outside the exceptional set in (3.3), every zero-winding return with
\(s\le H_A\) satisfies (0.5)--(0.7).

#### Proof

Such a return has

\[
 \delta(D_s)=s+2\Sigma(D_0,s)>T_r.
\tag{3.8}
\]

Since \(T_r/H_A\to\infty\), for all sufficiently large \(r\),

\[
 s\le H_A\le T_r/2.
\tag{3.9}
\]

Thus

\[
 \Sigma(D_0,s)>{T_r-s\over2}\ge {T_r\over4}.
\tag{3.10}
\]

Also \(T_r\ge r/[2K_0(\log r)^2]\) eventually, proving (0.5).  Since
\(s\le(A+1)\sqrt r\), at least one summand in (0.3) is at least

\[
 {\Sigma(D_0,s)\over s}
 \ge {\sqrt r\over16K_0(A+1)(\log r)^2}.
\tag{3.11}
\]

This is (0.6), and \(d(D_j)=2\sigma_j+1\) gives (0.7).  \(\square\)

### Corollary 3.3 (all-winding localization)

Outside the same \(o_A(B/N)\) exceptional set, every return of arbitrary
winding with \(s\le H_A\) satisfies (0.5)--(0.7).

#### Proof

The zero-winding case is Corollary 3.2.  If \(a\ge1\), the general return
equation (0.4) gives

\[
 s+2\Sigma(D_0,s)=\delta(D_s)+aN\ge N+1.
\tag{3.12}
\]

Consequently

\[
 \Sigma(D_0,s)\ge\frac{N+1-s}{2}.
\tag{3.13}
\]

For \(s\le H_A=O_A(\sqrt r)\), the right side is at least \(r/2\) for
all sufficiently large \(r\), which is stronger than (0.5).  Dividing by
\(s\le(A+1)\sqrt r\) also gives a suffix spike stronger than (0.6), and
(0.7) follows as before.  Thus only the zero-winding thin class contributes
to the exceptional set.  \(\square\)

### Corollary 3.4 (exact suffix-volume packing inequality)

Let \(\mathcal P\) be a pairwise quotient-edge-disjoint family of
nonwrapping return intervals with \(s(I)\le H_A\), and put

\[
 \mathscr S_r=\sum_{D\in\mathcal D_r}\frac{|S(D)|}{2}
 =\frac12\left(\sum_{D\in\mathcal D_r}d(D)-B\right).
\tag{3.14}
\]

Then

\[
 \boxed{
 |\mathcal P|
 \le o_A(B/N)+
 \frac{8K_0(\log r)^2}{r}\,\mathscr S_r.}
\tag{3.15}
\]

#### Proof

At most \(o_A(B/N)\) selected starts lie in the exceptional set of
Theorem 3.1.  Every other selected interval has cumulative suffix mass at
least \(r/[8K_0(\log r)^2]\) by Corollary 3.3.  For each selected
interval, its \(s\) deficit-carrying roots
\(D_0,\ldots,D_{s-1}\) form a subtrace of the full residence interval.
Because the quotient-edge traces in \(\mathcal P\) are disjoint, these
deficit subtraces are disjoint too.  Hence every root
\(D\in\mathcal D_r\) contributes its suffix semilength to at most one
selected interval.
Therefore

\[
 \frac{r}{8K_0(\log r)^2}
 \left(|\mathcal P|-o_A(B/N)\right)
 \le\mathscr S_r,
\tag{3.16}
\]

which is (3.15).  \(\square\)

The nonwrapping qualification costs nothing in the fixed Gaussian window:
the total number of quotient edges on cycles of length at most \(H_A+1\)
is \(\exp(o_A(r))=o(B/N)\).  Inequality (3.15) is a genuine dynamic
upper bound, but its unconditioned right side is much too large for
\((\mathrm{CP}_A)\), and hence also for \((\mathrm{RP}_A)\).  The proved
lower moment
\(\sum_Dd(D)\ge c\sqrt r\,B\) shows that the scalar global suffix-volume
resource lives far above the \(B/N\) scale.  A completion must exploit
where that mass occurs relative to the bounded-slot predecessor passages,
not merely its total.

## 4. Relation to the recursive Pascal passage gate

Peak deletion sends a physical return to a reduced adjacent-particle
passage, and the exact parent lift fixes the final Pascal slot

\[
 z={n_{-1}(g)-1\over2}.
\tag{4.1}
\]

The existing saddle localization already shows, outside \(o(B/N)\) outer
mass, that the first pruned rank lies in the Pascal saddle tube and
\(z=O(\log r)\).  Theorem 3.1 and Corollaries 3.2--3.3 give an independent,
chronology-level restriction on the same potentially critical returns:

\[
 \boxed{
 \begin{array}{c}
 \text{bounded logarithmic prescribed slot}\\[1mm]
 \text{and}\\[1mm]
 \text{an outer }\tau\text{-trajectory carrying total suffix mass}
        \Omega\!\left(r/(\log r)^2\right),
 \end{array}}
\tag{4.2}
\]

with at least one individual suffix of semilength
\(\Omega_A(\sqrt r/(\log r)^2)\).

These restrictions are simultaneous because each was obtained by deleting
only \(o(B/N)\) outer starts.  Neither one implies the other: a bounded
Pascal slot concerns the physical spacing of the final adjacent particles
in the inverse-pruning fibre, while \(\sigma_j\) measures the canonical
terminal suffix at an outer quotient time.

This gives a precise surviving theorem target.

> **Spike-compatible CP passage gate (unproved).**  In every positive-mass
> Pascal saddle tube, the exact binomial weight of Gaussian-short
> predecessor passages which have \(z=O(\log r)\) and whose outer orbit
> satisfies (4.2) is \(O_A(r^{-1/2})\) of the tube mass.

The \(O_A(r^{-1/2})\) density is the audited scale needed for the
Catalan-order packing gate \((\mathrm{CP}_A)\) after quotient interval
packing and the \(N\)-deck lift.  Replacing big-oh by
\(o_A(r^{-1/2})\) gives the stronger \((\mathrm{RP}_A)\) passage target.
The present report proves the spike condition in these statements; it
does not prove either passage-density estimate.

## 5. Caveats and audited boundary

1. The early-maximum count in Theorem 3.1 is needed only for zero winding.
   Positive winding has \(a\ge1\) in (0.4) and therefore forces the much
   stronger linear lower bound (3.13) directly.
2. No implication \(d(D_0)=1\Rightarrow\) return is used.  The retracted
   static first-deepest-sector recursion plays no role.
3. The estimate counts all qualifying starts, so it automatically bounds
   their quotient packing.  It does not assert that the complementary
   high-suffix family has small packing.
4. The constants are explicit relative to the absolute spectral constant
   \(c\) in (2.1): any \(K_0>(7/c)^2\) works.  The exponent comparison only
   needs \(c\sqrt{K_0}>6\); the displayed choice leaves one full power of
   slack.
5. The cumulative mass in (0.5) is measured in **tree edges**.  In literal
   binary word length it is twice as large.  This convention is why
   \(d(D_j)=2\sigma_j+1\).
6. An independent audit checked the \(HT\) union factor, the exponent
   \(r^{6-c\sqrt{K_0}}\), the floor in \(T_r\), the positive-winding
   extension, and the disjoint suffix-volume charge in (3.15).  It found
   no substantive error; the displayed notation and the subtrace
   qualification incorporate its minor corrections.

The proved/conditional boundary is therefore

\[
 \boxed{
 \begin{aligned}
 &\text{low cumulative suffix mass at Gaussian return, any winding:}
   &&o_A(B/N),\\
 &\text{mesoscopic suffix spike for every remaining return:}
   &&\text{proved},\\
 &\text{weighted bounded-slot passage density on the spike class:}
   &&\text{open},\\
 &\text{full }(\mathrm{CP}_A):
   &&\text{open},\\
 &\text{full }(\mathrm{RP}_A):
   &&\text{open}.
 \end{aligned}}
\tag{5.1}
\]
