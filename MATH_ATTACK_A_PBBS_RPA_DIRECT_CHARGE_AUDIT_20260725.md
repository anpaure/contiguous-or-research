# PBBS Gaussian short returns: direct charges, deck obstruction, and the exact remaining scale

Date: 2026-07-25

No computation, finite search, web search, or external result is used.

## 0. Verdict

Put

\[
 N=2r+1,
 \qquad B=\operatorname{Cat}_r,
\]

and let \(\overline\nu_H\) denote the maximum number of pairwise
quotient-edge-disjoint nonwrapping residence intervals on the long
step-two PBBS quotient cycles.  The physical assertion

\[
 \nu_{\lceil A\sqrt r\rceil}(P_r)=o_A(B)
 \tag{RP_A}
\]

is not proved or refuted here.

There are three unconditional conclusions.

1.  A direct height/edge charge gives, uniformly in the cutoff \(H\),

    \[
      \boxed{
      \overline\nu_H
      =O\!\left(B\sqrt{\frac{\log r}{r}}\right).}
      \tag{0.1}
    \]

    This sharpens the previously recorded
    \(O(B\log r/\sqrt r)\) two-scale estimate, but it is still larger
    than the quotient target \(o(B/N)\) by a factor
    \(\Theta(\sqrt{r\log r})\).

2.  If \(R_H\) is the number of quotient roots starting a residence at
    most \(H\), and \(Z_H\) is the number of quotient edges on quotient
    cycles of length at most \(H+1\), then

    \[
      \boxed{
      \nu_H(P_r)\ge
      \frac{N}{2H+1}(R_H-Z_H).}
      \tag{0.2}
    \]

    Consequently \((\mathrm{RP}_A)\) requires

    \[
      \boxed{R_{\lceil A\sqrt r\rceil}
      =o_A(B/\sqrt r).}
      \tag{0.3}
    \]

    Thus even an unquantified statement \(R_H=o(B)\) is insufficient.

3.  Peak deletion gives an exact capacitated passage system, but no
    pointwise fibre contraction.  A gap-seven reduced passage retains a
    positive fraction of its whole Pascal fibre and supports an
    edge-disjoint parent packing of normalized size at least
    \(1/18-o(1)\).  At the two-dimensional Pascal saddle, a positive
    density of bounded-slot Gaussian-short predecessor passages would
    produce \(\Omega_A(B/N)\) quotient packing and hence
    \(\Omega_A(B)\) physical packing.  The remaining theorem must
    therefore be a genuinely aggregate passage/cycle inequality.

The endpoint-capped erosion lemma and its residence-only constant-one
reduction were independently audited.  They pass.  The current source
already contains three earlier citation/numbering repairs; Section 6 records
only one remaining local-hypothesis clarification.  Hence failure to prove
\((\mathrm{RP}_A)\), not a defect in that reduction, is the current boundary.

## 1. A sharper uniform two-scale direct charge

A residence-\(\ell\) return has odd omitted-label gap

\[
 g=2\ell-1
\]

and its quotient interval contains \(\ell+1\) transition edges.  The
height--gap theorem gives

\[
 \operatorname{ht}(D)\le \ell-1
 \tag{1.1}
\]

for its normalized start root \(D\).

### Theorem 1.1 (uniform square-root-log quotient bound)

There is an absolute constant \(C\) such that, for every \(r\ge3\) and
every cutoff \(H\),

\[
 \overline\nu_H
 \le C B\sqrt{\frac{\log r}{r}}.
 \tag{1.2}
\]

#### Proof

It is enough to treat large \(r\).  Put

\[
 L=\left\lfloor
       \frac{\pi}{4}\sqrt{\frac r{\log r}}
    \right\rfloor.
 \tag{1.3}
\]

Split an edge-disjoint quotient family \(\mathcal P\) according as its
residence is at most \(L\) or greater than \(L\).

For the first part, (1.1) says that every start root has height at most
\(L-1\).  The path-graph walk count gives

\[
 \#\{D\in\mathcal D_r:\operatorname{ht}(D)\le L-1\}
 \le
 \left(2\cos\frac{\pi}{L+1}\right)^{2r}.
 \tag{1.4}
\]

Since \(\cos x\le e^{-x^2/2}\), and, for all sufficiently large \(r\),

\[
 L+1\le \frac{\pi}{3}\sqrt{\frac r{\log r}},
\]

the right side of (1.4) is at most

\[
 4^r\exp\!\left(-\frac{\pi^2r}{(L+1)^2}\right)
 \le 4^r r^{-9}.
 \tag{1.5}
\]

There is at most one next-return interval starting at a quotient edge.
Also

\[
 B=\frac1{r+1}\binom{2r}{r}
 \ge \frac{4^r}{(r+1)(2r+1)}.
 \tag{1.6}
\]

Thus the short part has size \(O(B r^{-7})\).

Every interval in the long part contains at least \(L+2\) quotient
edges.  Their traces are pairwise disjoint and the quotient has exactly
\(B\) directed edges, so

\[
 |\mathcal P_{>L}|\le\frac{B}{L+2}
 =O\!\left(B\sqrt{\frac{\log r}{r}}\right).
 \tag{1.7}
\]

Equations (1.5)--(1.7) prove (1.2).  Enlarging \(C\) covers the finitely
many small ranks.  \(\square\)

The proof is an actual deterministic charge: short intervals are injected
into the spectrally small set of low-height roots, while every long
interval is charged uniformly to its own \(L+2\) distinct quotient
edges.

## 2. Deck amplification: the direct enumerative obstruction

### Lemma 2.1 (circular greedy bound)

Let \(C\) be a directed cycle longer than \(K\), and let \(\mathcal A\)
contain at most one directed interval starting at each edge of \(C\),
each interval having length at most \(K\).  Then \(\mathcal A\) has an
edge-disjoint subfamily of size at least

\[
 \frac{|\mathcal A|}{2K-1}.
 \tag{2.1}
\]

#### Proof

An interval of length \(k\le K\) can meet only intervals whose starts
lie among the \(K-1\) preceding edges, its own start, and the \(k-1\)
following edges.  Thus its closed conflict neighbourhood has size at
most \(K+k-1\le2K-1\).  Greedy independent-set selection proves
(2.1).  The argument is circular and has no drawing-seam loss. \(\square\)

### Lemma 2.2 (all deck lifts are disjoint)

Let an interval \(I\) of length \(k\) lie on a quotient PBBS cycle of
length \(d>k\).  Its \(N\) spatial rotations are pairwise disjoint as
physical transition-edge sets.

#### Proof

Let \(C\) be the physical cycle containing one lift and let its
rotation stabilizer have order \(h\).  Rotations outside the stabilizer
place the interval on different physical cycles.  On \(C\), consecutive
stabilizer rotations translate its start by exactly \(d\) transition
edges, because \(C\) has length \(hd\) and its stabilizer quotient is
the displayed quotient cycle.  The \(h\) arcs of length \(k<d\) are
therefore disjoint, including across the cyclic seam. \(\square\)

Disjoint quotient traces have mutually disjoint collections of physical
lifts, since a common physical edge would project to a common quotient
edge.

### Theorem 2.3 (deck-amplification lower bound)

If \(2(H+1)<N\), then

\[
 \nu_H(P_r)\ge\frac{N}{2H+1}(R_H-Z_H).
 \tag{2.2}
\]

#### Proof

Discard starts on quotient cycles of length at most \(H+1\).  Apply
Lemma 2.1 with \(K=H+1\) on every remaining cycle.  This selects at
least \((R_H-Z_H)/(2H+1)\) disjoint quotient intervals.  Lemma 2.2
supplies all \(N\) disjoint lifts of every selected interval. \(\square\)

The voltage-itinerary bound gives

\[
 Z_H\le(2H+2)N^{2H+2}.
 \tag{2.3}
\]

For fixed \(A\) and \(H=\lceil A\sqrt r\rceil\), this is
\(\exp(o(r))=o_A(B/\sqrt r)\).  Rearranging (2.2) proves (0.3).

## 3. The exact capacitated charge and its first failure

Let \(E\in\mathcal D_d\) be a one-step peak-deletion core and put

\[
 k=\operatorname{pk}(E).
\]

Its inverse-tree fibre is the weak-composition simplex of the free leaves
over the \(2d+1\) ordered child slots, and has exact size

\[
 P_r(E)=\binom{r+d-k}{2d}.
 \tag{3.1}
\]

These fibres partition the outer quotient edge set:

\[
 \sum_{d<r}\sum_{E\in\mathcal D_d}P_r(E)=B.
 \tag{3.2}
\]

A reduced predecessor passage at time \(g<N\) prescribes the final root
slot

\[
 z_E(g)=\frac{n_{-1}(g)-1}{2},
\]

and the exact number of permitted parent starts is

\[
 K_r(E,g)
 =\binom{r+d-k-z_E(g)-1}{2d-1}.
 \tag{3.3}
\]

For every edge-disjoint outer family, projection under peak deletion has
the exact capacity constraint

\[
 \sum_a a_e m_a\le P_r(e),
 \tag{3.4}
\]

where \(a\) ranges over reduced passage types, \(a_e\) is the occurrence
multiplicity of reduced edge \(e\) in that ordered trace, and \(m_a\) is
the number of selected parent starts of that type.  Also

\[
 0\le m_a\le K_a.
 \tag{3.5}
\]

Thus the fractional dual

\[
 \begin{aligned}
 \text{minimize }&\quad
   \sum_eP_r(e)w_e+\sum_aK_av_a,\\
 \text{subject to }&\quad
   \sum_ea_ew_e+v_a\ge1,\\
 &w_e,v_a\ge0
 \end{aligned}
 \tag{3.6}
\]

is a rigorous direct-charging mechanism.  An objective
\(o(B/N)\) would prove the quotient form needed for \((\mathrm{RP}_A)\).

Theorem 1.1 is the explicit dual obtained by assigning a uniform edge
weight \(1/(L+2)\) and paying the start slack for the low-height short
types.  Its objective is only
\(O(B\sqrt{\log r/r})\).

No pointwise improvement of the fibre normalization is possible.  For

\[
 E_d=(10)^{d-2}1100
\]

the gap-seven passage has \(k=d-1\), \(z=0\), and

\[
 P_r(E_d)=\binom{r+1}{2d},
 \qquad
 K_r(E_d,7)=\binom r{2d-1},
 \qquad
 \frac{K_r(E_d,7)}{P_r(E_d)}=\frac{2d}{r+1}.
 \tag{3.7}
\]

Taking \(2d-1=r/2+O(1)\) makes the last ratio tend to \(1/2\).  After
discarding short quotient cycles, the five-edge greedy packing retains
at least one ninth of these starts.  Hence one fixed reduced passage has
an edge-disjoint parent packing of normalized size

\[
 \frac1{18}-o(1).
 \tag{3.8}
\]

This refutes bounded-multiplicity child-return charging, an
\(o(1)\)-per-fibre contraction, and every contraction which remembers
only the bounded menu of nested child returns.  It does not refute the
global theorem because this particular fibre has exponentially
sub-Catalan total mass.

There is a stronger orbitwise obstruction.  Put \(p=2d+1\) and

\[
 E_*=E(d-2,1,0)=(10)^{d-2}1100.
\]

The exact defect-one PBBS formulas give a physical component of period
\(3p\) whose omitted-particle itinerary is

\[
 \kappa_{3j}=j,\qquad
 \kappa_{3j+1}=j-3,\qquad
 \kappa_{3j+2}=j-1
 \quad(j\in\mathbb Z_p).
 \tag{3.8a}
\]

Every particle occurs exactly three times, so this word is perfectly
balanced.  Nevertheless every origin \(3j\) is a gap-seven predecessor
passage: the root particle returns at offset five, its predecessor has
already occurred at offset two, and that predecessor is selected again at
offset seven.  At outer rank \(R=4d-1\), the full Pascal fibre has size

\[
 P=\binom{4d}{2d},
\]

the prescribed empty-slot hyperplane has size \(P/2\), and, after the
negligible short parent cycles are removed, the five-edge greedy packing
retains

\[
 (1-o(1))P/18
 \tag{3.8b}
\]

edge-disjoint parent intervals.  The whole three-root reduced orbit has
capacity \(3P\).  Hence every universal local or orbitwise charge of the
form

\[
 \operatorname{pack}(\mathcal O,g)
 \le C\frac gd\sum_{E\in\mathcal O}P_R(E)
 \tag{3.8c}
\]

is false, even with exact Pascal weights and edge-disjointness.

This no-go is globally harmless.  If
\(e(E)=d-\operatorname{pk}(E)\) is the core's own peak defect, then exact
Narayana multiplicities and the Pascal capacities imply that some absolute
\(c,\eta>0\) satisfy

\[
 1+\sum_{e(E)\le cR}P_R(E)
 \le e^{-\eta R}\frac{\operatorname{Cat}_R}{R}.
 \tag{3.8d}
\]

Indeed, for fixed \(d,e\) there are
\(d^{-1}\binom de\binom d{e+1}\) cores and each has capacity
\(\binom{R+e}{2d}\).  If \(d\le5cR\), their combined exponential rate is
at most \((1+11c)\log2\); otherwise \(e/d\le1/4\) and the rate is at most
\((1+c)(h(1/4)+\log2)\).  Both are strictly below \(\log4\) for small
fixed \(c\).  Thus (3.8a)--(3.8c) close local balance-based charging, not
\((\mathrm{RP}_A)\); the surviving mass has linear core defect.

### Proposition 3.1 (high-rank, logarithmic-slot residual)

Outside a family of \(o(B/N)\) quotient start roots, every Gaussian-short
return has

\[
 d=|\partial D|\ge \frac r4,
 \qquad
 z_*(D)<\lceil3\log r\rceil.
 \tag{3.9}
\]

Consequently the predecessor is selected at most
\(6\log r+O(1)\) times before its final passage.

#### Proof

The number of outer roots with first-pruned rank \(d\) is the Narayana
number

\[
 \frac1r\binom rd\binom r{d+1}.
\]

For \(d\le r/4\), monotonicity and the entropy bound give a total
\(\exp(-c r)B=o(B/N)\), because
\(2h(1/4)<\log4\).

Now fix a core \(E\) of rank \(d\ge r/4\), with \(k\) peaks, and put
\(y=r-d-k\).  In its uniform weak-composition fibre, the exact tail of
the distinguished slot is

\[
 \Pr(n_0\ge L)
 =\frac{\binom{y-L+2d}{2d}}{\binom{y+2d}{2d}}
 \le\left(\frac{y}{y+2d}\right)^L
 \le\left(\frac35\right)^L.
 \tag{3.10}
\]

Indeed \(y\le r-d\le3r/4\) and \(2d\ge r/2\).  Sum (3.10) against
the exact fibre partition (3.2), and take
\(L=\lceil3\log r\rceil\).  Since
\(3\log(5/3)>1\), the result is \(o(B/r)=o(B/N)\).
Finally a return passage obeys
\(n_{-1}(g)=2z_*(D)+1\), proving the last assertion. \(\square\)

Thus the unresolved capacity is already confined to high-rank reduced
PBBS cores and bounded-by-logarithmic predecessor multiplicity.  This
does not make it pointwise contractive: the gap-seven example has
\(z=0\).

## 4. The dangerous saddle and the exact counterexample criterion

The outer mass over cores of rank \(d\) with \(k\) peaks is

\[
 \mathsf M_r(d,k)
 =\frac1d\binom dk\binom d{k-1}
  \binom{r+d-k}{2d}.
 \tag{4.1}
\]

Its two-dimensional saddle is

\[
 d=\frac r2,
 \qquad k=\frac r6.
 \tag{4.2}
\]

For \(d=r/2+v\sqrt r\), \(k=r/6+u\sqrt r\), Stirling expansion gives

\[
 \frac{\mathsf M_r(d,k)}B
 =\frac{9\sqrt2}{2\pi r}
   \exp\!\left[-\frac{81u^2-18uv+33v^2}{8}\right]
   (1+o(1))
 \tag{4.3}
\]

uniformly for bounded \(u,v\).  Prescribing any fixed slot \(z\) retains
asymptotic fibre fraction

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}\longrightarrow
 \frac34\,4^{-z}.
 \tag{4.4}
\]

Consequently, fix \(A,a,\eta>0\) and \(z_0\).  If, throughout the tube

\[
 |d-r/2|\le a\sqrt r,
 \qquad k=\lfloor r/6\rfloor,
\]

an \(\eta\)-fraction of the cores admit a predecessor passage of time at
most \(2A\sqrt r+O(1)\) with \(z\le z_0\), then the corresponding outer
start mass is \(\Omega_{A,a,\eta,z_0}(B/\sqrt r)\).  Circular greedy
packing loses only \(O_A(\sqrt r)\), so

\[
 \overline\nu_{\lceil A\sqrt r\rceil}=\Omega(B/r).
 \tag{4.5}
\]

Deck lifting then gives \(\nu_H(P_r)=\Omega(B)\), contradicting
\((\mathrm{RP}_A)\).  Therefore the needed theorem must in particular
prove vanishing bounded-slot predecessor-passage density across every
dangerous Pascal saddle tube.  This vanishing is necessary, but by itself
is not asserted sufficient: the full trace-capacity inequalities (3.4)
remain.

## 5. The exact two-return branching statement and why it still does not contract

For a passage ending at time \(g\), recall that

\[
 n_{-1}(g)=2z+1.
 \tag{5.1}
\]

Here \(n_{-1}(g)\) counts selections at times \(0\le t<g\); the final
selection at time \(g\) is not included.  Hence even when \(z=0\),

\[
 n_{-1}(g)=1,
\]

there is exactly one earlier predecessor selection, and the occurrence at
time \(g\) is its second.  Thus its last earlier occurrence and time \(g\)
always delimit a consecutive child return.  When \(z\ge1\), there are
\(2z+1\ge3\) earlier predecessor selections, but the same conclusion uses
only the last one.

Accordingly every parent return really does contain two child returns: a
return of the distinguished particle before \(g\), and a return of its
predecessor ending at \(g\).  This tempting branching charge is nevertheless
noncontractive.  In the gap-seven family, these are the same ordered
gap-five traces for every parent lift, while (3.8) supplies a constant
fraction of the full parent fibre in an edge-disjoint packing.  Remembering
both child returns therefore still has unbounded, indeed exponential,
projection congestion.  A valid induction must retain the Pascal slot
vector and the lifted trace capacities, rather than only the two child
intervals.

## 6. Independent audit of the endpoint-capped reduction

The substantive content of Lemma 22.1 and Theorem 22.2 in
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md` is correct.

For a coordinate indicator whose internally bounded positive runs have
at least \(H+1\) owners, let

\[
 d_i=\bigwedge_{j=0}^H x_{i+j}.
\]

Then, with constant endpoint extension,

\[
 \bigvee_{a=0}^{t-1}d_{i+a}
 =\bigwedge_{a=t-1}^{H}x_{i+a},
 \qquad1\le t\le H+1,
 \tag{6.1}
\]

and

\[
 \bigvee_{a=0}^{H+s}d_{i+a}
 =\bigvee_{a=H}^{H+s}x_{i+a},
 \qquad0\le s\le H.
 \tag{6.2}
\]

Every crossing cut destroys at most \(q\) lower and \(q\) upper
depth-\(q\) windows.  Thus the exact total central-band length is

\[
 W+2HB+2(H^2+2H)\nu_H(P_r).
 \tag{6.3}
\]

The global standing assumption \(H\le(m+1)/2\) supplies the hypothesis
needed for every erosion letter to be nonempty.  For local readability,
Lemma 22.1 should repeat \(H<m\) explicitly; without either hypothesis its
nonzero-letter conclusion would be false.  Three earlier textual issues are
already repaired in the current source: the transversal is labelled
\((22.7)\), the singleton repairs in \((22.8)\) are correctly credited with
restoring cut windows, and the odd-dimensional conclusion refers to
\((22.6)\).  No correction changes the theorem or its constants.

## 7. Final boundary

No presently valid injection or charge reaches

\[
 \overline\nu_{\lceil A\sqrt r\rceil}=o_A(B/N).
\]

The strongest unconditional direct charge obtained here is (0.1).  The
deck theorem (0.2) simultaneously shows that a direct enumeration must
gain the necessary rare-root estimate (0.3).  Peak deletion then forces
one to retain, at minimum,

* reduced rank and peak count;
* the prescribed Pascal root slot;
* the ordered \(0\cdots0\cdots(-1)\) predecessor-passage condition; and
* the complete reduced trace capacities (3.4).

The smallest theorem which closes this direct-charging lane is an
\(o(B/N)\)-cost feasible dual in (3.6), or an equally strong integral
charge on the lifted slot-vector traces.  Gap seven rules out a pointwise
proof, and (3.8a)--(3.8d) rule out even orbitwise \(O(g/d)\) charging;
the Gaussian saddle criterion in Section 4 shows exactly where an aggregate
proof or a counterexample must occur.
