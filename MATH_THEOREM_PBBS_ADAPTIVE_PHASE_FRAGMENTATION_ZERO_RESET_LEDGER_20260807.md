# Adaptive SCD phase shifts remove the PBBS theta reset deficit with no new endpoint pieces

**Date:** 2026-08-07
**Method:** rephase one two-piece SCD segment without changing its piece
count, then use the exact SCD start-rank multiplicities
**Status:** unconditional chainization and endpoint-count theorem.  A
positive-density family of top-aligned full pieces can be replaced by two
partial pieces on the same SCD chains, with exactly the same number of
endpoint chains.  Rephasing all chains in one explicit start-rank band
removes more than the complete theta reset deficit.  No added endpoint
position and no growing exported phase state is required at this abstract
level.

This does not construct the common literal PBBS source word.  It changes
the global fragmentation, so the remaining theorem is an owner-compatible
common-history realization of the rephased pieces.

## 1. Parameters and the original ledger

Use the odd merged-PBBS parameters

\[
n=2m+1,\qquad t=m-d,\qquad W=\binom n m.
\]

The deep band is

\[
\mathcal B_{\rm deep}
=\{X\subseteq[n]:d+1\le |X|\le t-1\}.
\tag{1.1}
\]

Fix any SCD of \(B_n\).  Split every intersection with (1.1) from the
top into pieces of at most \(d\) consecutive ranks.  Write

\[
P=P_{n,d}
\]

for the number of pieces and

\[
F=F_{n,d}
\]

for the number of length-\(d\) full pieces.  The merged region has \(g\)
endpoint chains, leaving

\[
S=g-P
\tag{1.2}
\]

unused after assigning one endpoint chain to every piece.  The exact reset
excess is

\[
H:=F-S.
\tag{1.3}
\]

The reset theorem gives

\[
\frac HW\longrightarrow
\theta=4\sum_{a\ge1}e^{-4\pi a^2}>0.
\tag{1.4}
\]

## 2. One-chain phase shift

Consider a deep-band chain segment of length

\[
L=ad+r,\qquad a\ge1,\qquad 1\le r\le d-2.
\tag{2.1}
\]

Its top-aligned fragmentation has piece lengths

\[
\underbrace{d,d,\ldots,d}_{a\ {\rm times}},r.
\tag{2.2}
\]

Thus it contributes \(a+1\) pieces and \(a\) full pieces.

### Lemma 2.1 (one reset removed at zero piece charge)

Replace (2.2) on this same SCD chain by

\[
r+1,
\underbrace{d,d,\ldots,d}_{a-1\ {\rm times}},
d-1.
\tag{2.3}
\]

Then:

1. the two lists in (2.2)--(2.3) have the same total length \(L\);
2. every new piece has length at most \(d\);
3. the number of pieces remains \(a+1\); and
4. the number of full pieces decreases from \(a\) to \(a-1\).

Equivalently, shifting the first cut by the phase

\[
\delta=r+1
\tag{2.4}
\]

removes exactly one private-reset demand without consuming an additional
endpoint chain.

#### Proof

The total length in (2.3) is

\[
(r+1)+(a-1)d+(d-1)=ad+r=L.
\]

Both boundary pieces have lengths in \(\{2,\ldots,d-1\}\).  The remaining
claims follow by inspection. \(\square\)

No target is deleted or duplicated: the new pieces are consecutive
subchains whose union is the original segment.

### Lemma 2.2 (one global one-rank clock shift)

There is an even simpler simultaneous rule.  On every deep-band chain
segment of length \(L\ge d\), make the top piece have length \(d-1\), and
then continue downward in pieces of length \(d\), with a final remainder.

Write \(L=ad+r\), \(0\le r<d\).  Relative to the original top-aligned
fragmentation, the changes in the pair

\[
(\#\hbox{ pieces},\#\hbox{ full pieces})
\]

are

\[
\boxed{
\begin{array}{c|c}
r&(\Delta P,\Delta F)\\ \hline
0&(1,-1)\\
1,\ldots,d-2&(0,-1)\\
d-1&(0,0).
\end{array}}
\tag{2.5}
\]

Segments of length below \(d\) remain one partial piece.

#### Proof

After the first piece of length \(d-1\), the remaining length is

\[
(a-1)d+(r+1).
\]

If \(r=0\), this gives \(a-1\) full pieces and a final singleton, versus
\(a\) original full pieces.  If \(1\le r\le d-2\), it gives \(a-1\)
full pieces and a final piece of length \(r+1\), with the same total
piece count as before.  If \(r=d-1\), the remainder is \(ad\), giving
exactly \(a\) full pieces after the leading partial piece, the same counts
as originally. \(\square\)

Thus a single fixed phase shift of the fragmentation clock, by one rank
from a top length \(d\) to a top length \(d-1\), never increases the total
endpoint demand \(P+F\).  It decreases that demand by one on every chain
whose positive remainder is not \(d-1\).

## 3. An explicit positive-density eligible bank

A symmetric chain starting at rank \(j\le t-1\) crosses rank \(t-1\).
If \(j>d+1\), its deep-band intersection has length

\[
L_j=t-j.
\tag{3.1}
\]

For \(1\le r\le d-2\), put

\[
j_r=t-d-r.
\tag{3.2}
\]

For all sufficiently large parameters, \(j_r>d+1\).  A chain starting at
\(j_r\) therefore has deep length

\[
L_{j_r}=d+r.
\tag{3.3}
\]

It has exactly the two original pieces of lengths \(d,r\), and Lemma 2.1
replaces them by the two partial pieces \(r+1,d-1\).

An SCD has exactly

\[
c_j=\binom n j-\binom n{j-1}
\tag{3.4}
\]

chains starting at rank \(j\).  Hence the number of eligible chains in
the band (3.2) is

\[
\begin{aligned}
E_{n,d}
&=\sum_{r=1}^{d-2}
\left(\binom n{t-d-r}-\binom n{t-d-r-1}\right)\\
&=\binom n{t-d-1}-\binom n{t-2d+1}.
\end{aligned}
\tag{3.5}
\]

### Theorem 3.1 (eligible density exceeds theta)

At the optimal deadline,

\[
\boxed{
\frac{E_{n,d}}W\longrightarrow
e^{-\pi}-e^{-9\pi/4}>\theta.}
\tag{3.6}
\]

Consequently \(E_{n,d}>H\) for every sufficiently large parameter.

#### Proof

The two ranks in (3.5) are

\[
t-d-1=m-2d-1,\qquad
t-2d+1=m-3d+1.
\]

The uniform central-binomial estimate and
\(d^2/n\to\pi/8\) give the limit in (3.6).

For a proof-safe strict comparison, write

\[
e^{-\pi}-e^{-9\pi/4}
=e^{-\pi}(1-e^{-5\pi/4})
>\frac12e^{-\pi}.
\]

Also

\[
\theta
\le\frac{4e^{-4\pi}}{1-e^{-12\pi}}
<8e^{-4\pi}
<\frac12e^{-\pi}.
\]

The last two strict inequalities follow respectively from
\(e^{12\pi}>2\) and \(e^{3\pi}>16\).  Thus the limiting eligible density
is strictly larger than \(\theta\).  Equations (1.4) and (3.6) imply
\(E_{n,d}>H\) eventually. \(\square\)

## 3A. Exact balanced \(Q\)-phase assignment for every \(Q\)

The eligible chains can be distributed almost equally among any prescribed
number \(Q\le d-2\) of integral phases.  No divisibility condition
\(Q\mid d\) is needed.

Write

\[
D=d-2,\qquad
w_r=\binom n{t-d-r}-\binom n{t-d-r-1}
\quad(1\le r\le D).
\tag{3.7}
\]

Thus \(w_r\) is the number of eligible chains with remainder \(r\), and
\(\sum_{r=1}^D w_r=E_{n,d}\).

### Lemma 3A.1 (the eligible remainder weights decrease)

For all sufficiently large parameters,

\[
w_1\ge w_2\ge\cdots\ge w_D.
\tag{3.8}
\]

#### Proof

Put

\[
c_j=\binom n j-\binom n{j-1}
=\binom n j\,\frac{n-2j+1}{n-j+1}.
\]

Direct division gives

\[
\frac{c_{j-1}}{c_j}
=\frac{j(n-2j+3)}
       {(n-j+2)(n-2j+1)}.
\tag{3.9}
\]

Writing \(A=n-2j+1\), the right side is at most one exactly when

\[
A(A+1)\ge2j.
\tag{3.10}
\]

Throughout (3.7), \(j\le t-d-1=m-2d-1\), so \(A\ge4d+4\).
Since \(16d^2/n\to2\pi>1\), inequality (3.10) holds eventually.
Now \(w_{r+1}=c_{t-d-r-1}\le c_{t-d-r}=w_r\). \(\square\)

For \(1\le a\le Q\), define the integral phase offsets

\[
\boxed{
\delta_a=1+\left\lceil\frac{aD}{Q}\right\rceil.}
\tag{3.11}
\]

They satisfy

\[
2\le\delta_1<\cdots\le\delta_Q=d-1
\]

after deleting repeated values if \(Q>D\); under \(Q\le D\) no deletion
is needed, and

\[
\left|\delta_a-\left(1+\frac{aD}{Q}\right)\right|<1.
\tag{3.12}
\]

A remainder-\(r\) chain is eligible for phase \(a\) when
\[
r<\delta_a.
\tag{3.13}
\]

In that phase its two new piece lengths are

\[
\delta_a,\qquad d+r-\delta_a,
\tag{3.14}
\]

both in \(\{1,\ldots,d-1\}\).  Thus it still has two pieces and no full
piece.

### Theorem 3A.2 (balanced integral interlacing)

For every integer \(1\le Q\le d-2\), all \(E_{n,d}\) eligible chains can
be assigned to the \(Q\) phases (3.11) so that:

1. every assigned chain satisfies \(r<\delta_a\);
2. the phase class sizes differ by at most one;
3. every chain retains two pieces and loses its one full piece; and
4. the offsets are within one rank of a uniform arithmetic \(Q\)-grid.

This holds for every \(d\); in particular it does not require \(Q\mid d\).

#### Proof

The phase neighborhoods in the ordered remainder set are nested.  The
first \(a\) phases can use every chain with

\[
r\le k_a:=\left\lceil\frac{aD}{Q}\right\rceil.
\]

Because the weights \(w_r\) decrease, their prefix average is at least
the average over all \(D\) classes.  Hence

\[
\sum_{r=1}^{k_a}w_r
\ge\frac{k_a}{D}E_{n,d}
\ge\frac aQ E_{n,d}.
\tag{3.15}
\]

Give phase \(a\) the quota

\[
h_a=
\left\lfloor\frac{aE_{n,d}}Q\right\rfloor
-\left\lfloor\frac{(a-1)E_{n,d}}Q\right\rfloor.
\tag{3.16}
\]

The quotas sum to \(E_{n,d}\) and differ by at most one.  Their first
\(a\) terms sum to \(\lfloor aE_{n,d}/Q\rfloor\), which is at most the
left side of (3.15).  The nested-neighborhood Hall criterion therefore
assigns all chain copies to the phase slots.  Equations (3.13)--(3.14)
prove the last piece-count assertions, and (3.12) proves the grid
statement. \(\square\)

Theorem 3A.2 is an exact balanced/interlaced global chainization at the
SCD level.  It is stronger than rounding the analytic phase measure:
instead of leaving an \(O(1/d)\) Fourier error, it uses the actual chain
remainders and removes one reset from every eligible chain.

## 4. Exact zero-reset endpoint ledger

### Theorem 4.1 (adaptive-phase reset elimination)

For every sufficiently large parameter, choose any \(H=F-S\) eligible
chains from Section 3 and apply Lemma 2.1 to them.  Let \(P'\) and \(F'\)
be the piece and full-piece counts after rephasing.  Then

\[
\boxed{
P'=P,\qquad F'=F-H=S,\qquad P'+F'=g.}
\tag{4.1}
\]

Thus the rephased chainization assigns one endpoint to every piece and one
private reset to every remaining full piece using exactly the existing
\(g\) endpoint chains.  It adds no endpoint position.

#### Proof

Every application of Lemma 2.1 preserves the number of pieces and removes
one full piece.  Applying it on \(H\) disjoint SCD chains gives

\[
P'=P,\qquad F'=F-H.
\]

By \(H=F-S\), the latter equals \(S\).  Finally \(P+S=g\) by (1.2).
\(\square\)

There is also a selection-free version.  Rephase **all** \(E_{n,d}\)
eligible chains.  Then

\[
P'=P,\qquad F'=F-E_{n,d}<S
\tag{4.2}
\]

eventually, so \(P'+F'<g\).  This leaves unused endpoint capacity and
requires no extra selected/unselected bit inside the eligible band.

### Theorem 4.2 (one fixed phase already clears theta)

Apply the global one-rank clock shift of Lemma 2.2 to every deep-band SCD
chain.  Let \(N_0\) count the affected chain segments whose lengths are
zero modulo \(d\), and let \(N_{\rm mid}\) count those whose remainders
lie in \(1,\ldots,d-2\).  The new counts satisfy

\[
\boxed{
P^\star=P+N_0,\qquad
F^\star=F-N_0-N_{\rm mid},\qquad
P^\star+F^\star=P+F-N_{\rm mid}.}
\tag{4.3}
\]

Moreover,

\[
N_{\rm mid}\ge E_{n,d}>H
\tag{4.4}
\]

for all sufficiently large parameters.  Consequently

\[
\boxed{
P^\star+F^\star<g.}
\tag{4.5}
\]

Thus one fixed global cut phase, not a growing phase bank, gives enough
existing endpoint chains for every piece and every remaining private
reset.

#### Proof

Sum the three exact rows of (2.5) over the SCD chains.  This proves (4.3).
Every chain counted by \(E_{n,d}\) has remainder in
\(1,\ldots,d-2\), so it is counted by \(N_{\rm mid}\).  Theorem 3.1 gives
(4.4).  Finally,

\[
P+F=P+(S+H)=g+H,
\]

and hence (4.3)--(4.4) give

\[
P^\star+F^\star=g+H-N_{\rm mid}<g.
\]

\(\square\)

The increase \(N_0\) in the piece count causes no separate shortage:
\(P^\star\le P^\star+F^\star<g\).  It is paid exactly by the simultaneous
loss of \(N_0\) full-piece resets.

## 5. Target packing remains exact

The rephased pieces are still disjoint saturated subchains of the same
SCD and still partition every target in \(\mathcal B_{\rm deep}\).
Under Theorem 4.1 their number remains \(P\le g\); under the global shift
of Theorem 4.2 it is \(P^\star<g\).  Every piece has at most \(d\)
vertices.  Therefore the endpoint-chain injection from the merged-region
capacity theorem applies in either case:

1. assign every rephased piece a distinct physical endpoint chain;
2. map its targets to increasing suffix lengths within that endpoint;
3. for a piece containing a rank-\((t-1)\) target, use the top-aligned
   interval lengths ending at \(d\).

No marked target collision or scalar address shortage is introduced.
What changes is only which consecutive targets share one endpoint chain.

## 6. Position and exported-state audit

The construction does not form \(d\) separate physical regions.  It
changes cut locations on selected chains of one SCD.

In the strongest version, Theorem 4.2 uses the same top length \(d-1\)
on every chain, so there is only one global cut rule and no phase choice
to export.

For the eligible start rank \(j_r=t-d-r\), the phase is

\[
\delta=r+1=t-d-j_r+1.
\tag{6.1}
\]

Thus it is recovered from the absolute minimum rank of the chain segment,
or equivalently from the two new piece lengths \(r+1,d-1\).  The
selection-free version (4.2) is a deterministic function of this rank.
It needs no \(d\)-valued exported phase register and no coordinate sidecar.

At the abstract chain/endpoint level the construction therefore has:

\[
\boxed{
\text{zero added positions, one global SCD, and \(O(1)\) exported phase
state.}}
\tag{6.2}
\]

This statement does not assert a bounded-state literal PBBS compiler.  It
asserts that the phase itself is intrinsic data, so a growing sidecar is
not forced by the chainization.

## 7. The remaining physical theorem

The fixed top-aligned fragmentation grouped all pieces in a slab by a
common maximum rank.  Rephasing replaces, on an eligible chain,

\[
(d,r)\quad\hbox{by}\quad(r+1,d-1).
\]

Although this preserves every target and every scalar endpoint count, the
two new pieces require a different overlap history in the merged cyclic
region.  The existing two-endpoint and fixed-coordinate theorems do not
serialize these adaptive cuts.

### Theorem 7.1 (the two rephased pieces cannot simply be adjacent)

Let

\[
C_1\subset C_2\subset\cdots\subset C_{d+r},
\qquad 2\le r\le d-2,
\tag{7.1}
\]

be a strict saturated chain.  Put \(h=r+1\).  The one-rank shift splits
it into

\[
\mathcal L=(C_1,\ldots,C_h),
\qquad
\mathcal U=(C_{h+1},\ldots,C_{h+d-1}).
\tag{7.2}
\]

Suppose \(\mathcal U\), which contains the rank-\((t-1)\) target, is
assigned to suffix depths \(2,\ldots,d\) at one endpoint.  Assign
\(\mathcal L\) to any \(h\) consecutive suffix depths

\[
a+1,\ldots,a+h,\qquad 0\le a\le d-h,
\tag{7.3}
\]

at another endpoint.  Then the two endpoints cannot be consecutive in
either temporal order.

#### Proof

First put the lower endpoint at \(e-1\) and the upper endpoint at \(e\).
The assignments read

\[
Z_{e-1,a+k}=C_k\quad(1\le k\le h),
\qquad
Z_{e,j}=C_{h+j-1}\quad(2\le j\le d).
\tag{7.4}
\]

The suffix recurrence is

\[
Z_{e,j}=A_e\cup Z_{e-1,j-1}.
\tag{7.5}
\]

At most the last lower depth equals \(d\), so at least
\(h-1=r\ge2\) consecutive values of \(k\) in (7.4) satisfy
\(a+k\le d-1\).  For two consecutive such values \(k,k+1\), equations
(7.4)--(7.5) require

\[
A_e\cup C_k=C_{h+a+k},
\qquad
A_e\cup C_{k+1}=C_{h+a+k+1}.
\tag{7.6}
\]

The first equality gives \(A_e\subseteq C_{h+a+k}\).  Also
\(C_{k+1}\subseteq C_{h+a+k}\).  Hence the left side of the second
equality is contained in \(C_{h+a+k}\), contradicting the strict next
member \(C_{h+a+k+1}\).

Now put the upper endpoint at \(e-1\) and the lower endpoint at \(e\).
Because \(h\ge3\), the interval (7.3) contains some depth
\(\ell=a+k\) with \(3\le\ell\le d\).  The same recurrence would give

\[
C_k=Z_{e,\ell}
=A_e\cup Z_{e-1,\ell-1}
=A_e\cup C_{h+\ell-2}.
\tag{7.7}
\]

But \(h+\ell-2>k\), so \(C_{h+\ell-2}\supsetneq C_k\), a contradiction.
\(\square\)

Theorem 7.1 is a concrete scope correction.  The full-piece
sliding-Johnson normal form does not supply the needed history: it concerns
consecutive endpoints whose complete depths \(1,\ldots,d\) are full,
whereas the rephased upper piece occupies depths \(2,\ldots,d\).
Furthermore, the most direct attempt to put its companion partial piece
on the adjacent endpoint is impossible.

Nor can one invoke that normal form by filling in the missing depth-one
cell at every rephased upper endpoint.  Such a filling makes the endpoint
full again.  A theta-density family of those completed endpoints is ruled
out at fixed additive overhead by the positive-density full-endpoint
theorem, which forces additive cost \(\Omega(\theta d)\).  The missing
depth-one cell must remain genuinely nonfull and participate in the new
interlaced history.

This obstruction applies to a large enough bank to clear theta.  The
excluded remainder-\(1\) class has size

\[
w_1=\binom n{t-d-1}-\binom n{t-d-2}=O(W/d),
\tag{7.8}
\]

because the adjacent-layer difference at distance \(\Theta(d)\) from the
middle is an \(O(d/n)=O(1/d)\) fraction of that layer.  Hence

\[
\frac{E_{n,d}-w_1}{W}
\longrightarrow e^{-\pi}-e^{-9\pi/4}>\theta.
\tag{7.9}
\]

One may choose all \(H\) chains in Theorem 4.1 with \(r\ge2\), so every
chosen rephased pair obeys Theorem 7.1.

This does not refute zero positional charge.  An intervening endpoint may
carry a piece from another chain, so many rephased pairs could be
interlaced without inserting blank positions.  It proves that such a
global interlacing theorem is genuinely necessary.

### Exact common-history statement

Let \(\mathscr P^\star\) be either rephased piece family from Theorem 4.1
or 4.2.  The remaining assertion is:

> **Adaptive-phase merged PBBS chart theorem.**  Realize the rephased SCD
> pieces by an injection into the existing merged endpoint positions and
> one source word \(A\), so that:
>
> 1. every target assigned to suffix interval \(I\) equals
>    \(\bigcup_{i\in I}A_i\);
> 2. the two pieces of every rephased chain are interlaced with other
>    endpoints as required by Theorem 7.1, without adding positions;
> 3. every coordinate cover-free cut holds;
> 4. every source letter lies in its prescribed PBBS owner envelope; and
> 5. all residence, upper, and compiler rows are preserved.

The coordinatewise content of Item 1 is exact.  For a coordinate \(x\),
let \(\mathcal I_x^+\) be the assigned intervals whose targets contain
\(x\), and let \(\mathcal I_x^-\) be those whose targets omit \(x\).
A support set for \(x\) exists if and only if

\[
\boxed{
I\not\subseteq
\bigcup_{J\in\mathcal I_x^-}J
\qquad(I\in\mathcal I_x^+).}
\tag{7.10}
\]

Indeed, the support must avoid the union on the right and hit every
positive interval; condition (7.10) is necessary and lets one choose one
allowed support point from every positive interval.  Thus (7.10), together
with the owner-envelope restriction on those support points, is the exact
common-history/cover-free gate.

Theorem 4.1 proves that this target has no theta reset deficit, no target
packing deficit, no added endpoint position, and no intrinsic growing
phase state.  Its remaining content is common-history and owner
compatibility.

## 8. Consequence for the uniform \(Q\)-phase proposal

Uniform roots-of-unity phases are sufficient to suppress the Gaussian
theta alias, but they are not necessary.  Adaptive phase shifts exploit
the actual remainder \(L\bmod d\) of each SCD chain segment and remove the
reset demand integrally, before any queue bite.

Hence the shortest surviving route is not to prove that a slowly growing
uniform \(Q\) can be stored.  It is to physicalize the zero-charge
replacement

\[
\boxed{(d,r)\longmapsto(r+1,d-1)}
\]

on a theta-sized, or on the complete selection-free, eligible chain bank.
