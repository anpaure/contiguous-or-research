# Repaired promotion rings: a direct growing-rank slow-greedy trajectory

Date: 2026-07-26

Scope: constant-one owner packing only. No fixed-uniformity matching
theorem is used.

**Retraction (2026-07-27).** The former unconditional Theorem 0.1 is not
proved. The decreasing buffer \(L_i=L-iJ\) does not control the input
top strip during a checkpoint of length \(K/40=\Theta(m)\). For a top
cluster \(C\), the square generator contains

\[
 \nu_t\sum_g A_C(g)^2+\sum_y\chi_{t,y}P_C(y)^2,
\]

where the second term is the compensation-coin diagonal. This quantity
lies two orders above the recorded top and can be as large as the full
first-moment loss times \(A_C\). The resulting normalized top growth is
\(\exp(\Theta(m))\), whereas a \(J=\Theta(\log m)\) buffer supplies only
\(\exp[-\Theta((\log m)^2)]\) attenuation. The exact audit and the
surviving conditional theorem are in
MATH_AUDIT_REPAIRED_RING_BUFFERED_STOPPED_GENERATOR_ESCAPE_20260727.md.

## 0. Result

Let \(H\) be the least integer for which
\(\binom{2m}{m}/\binom{2m}{m-H}\ge m+H\), and put

\[
 H=(1+o(1))\sqrt{m\log m},\qquad M=m+H,
\tag{0.1}
\]

where \(H\) is the packing-side critical depth. Delete a block of
\(1\le\kappa=o(m)\) consecutive phases from every promotion ring and put

\[
 r=M-\kappa,\qquad K=r+1=(1+o(1))m.
\tag{0.2}
\]

A repaired edge contains one root and \(r\) middle owners. Write

\[
 N=\binom{2m}{m-H},\qquad
 W=\binom{2m}{m},\qquad
 \lambda={W\over N},\qquad
 \rho={r\over\lambda}.
\tag{0.3}
\]

Minimality of \(H\) gives

\[
 1-\rho=O((H+\kappa)/m)=o(1).
\tag{0.4}
\]

In the simple physical catalogue the root and owner degrees are

\[
 D={M!\over\mu_\kappa},\qquad
 D_X=\rho D,\qquad
 \mu_\kappa=2((\kappa-H+1)_+)!.
\tag{0.5}
\]

The representation multiplicity cancels from all ratios below.

### Conditional conclusion 0.1 (requires MDLE)

If the edge-only ADLE+ACLE system stated in
MATH_CROSS_AUDIT_REPAIRED_RING_SLOW_BITE_VS_WBR_DLE_20260727.md
holds along the uncompensated process below (or the corresponding MDLE,
including coin diagonals, holds along the compensated process), then
with probability
\(1-o(1)\) it produces an integral matching missing at most

\[
                 (m^{-1/20}+o(1))N=o(N)
\tag{0.6}
\]

roots. Consequently it leaves

\[
 O\left(\left({H+\kappa\over m}+m^{-1/20}\right)W\right)
 =o(W)
\tag{0.7}
\]

middle owners.

The small parameter in the proof is

\[
 \boxed{
 T\varepsilon_*
 =O\left({K\log m\,(\log m)^8\over m^2z^2}\right)
 =O(m^{-9/10}\log^9m)=o(1),
 \qquad z=m^{-1/20},
 }
\tag{0.8}
\]

where \(T=(K/20)\log m\) is the process time. This is the direct
growing-\(K\) replacement for the invalid fixed-\(K\)
Pippenger--Spencer shortcut.

For the full generator-error expression (4.5), the safe master parameter
is actually

\[
 \bar\varepsilon_*={CL^6\over m^2z^2},\qquad
 T\bar\varepsilon_*=O(m^{-9/10}\log^{13}m)=o(1).
\tag{0.9}
\]

This logarithmic correction does not repair Claim 5.1; it only corrects
the conditional scalar ledger.

## 1. Exact ledgers and reference trajectory

If the matching currently contains \(s\) edges, then, before the
negligible cleaning in Section 6, the surviving root and owner fractions
are exactly

\[
 x=1-{s\over N},\qquad
 u=1-{rs\over W}=1-\rho(1-x).
\tag{1.1}
\]

Put

\[
 q={\rho x\over u}\le1.
\tag{1.2}
\]

The product-density reference degrees are

\[
 \mathcal D_R(x)=Du^r,\qquad
 \mathcal D_O(x)=D_Xxu^{r-1}=q\mathcal D_R(x).
\tag{1.3}
\]

We stop at \(x=z=m^{-1/20}\). Since \(u\ge x\), throughout the run

\[
 \log\mathcal D_R
 \ge \log D+r\log z
 =(19/20+o(1))m\log m.
\tag{1.4}
\]

Thus every reference link is still factorially large. The proof below
does not infer concentration merely from this fact.

The exact packing-side leave is

\[
 W-rN=N(\lambda-r)=O((H+\kappa)N)=o(W).
\tag{1.5}
\]

Hence the required owner conclusion is equivalent to missing \(o(N)\)
roots.

## 2. The infinitesimal slow bite

At time \(t\), give every active physical edge an exponential clock of
instantaneous rate

\[
                  \nu(t)={1\over K\mathcal D_R(x(t))}.
\tag{2.1}
\]

When the first clock rings, select that edge and remove its root and all
its owners. Restart the clocks on the residual catalogue. Simultaneous
rings have probability zero, so the selected edges form a literal
matching. This is uniform random greedy selection with a deterministic
time change.

If all but a negligible root mass have degree
\((1\pm\eta)\mathcal D_R\), then the total jump rate is

\[
 {1\over K\mathcal D_R}\sum_A d(A)
 =(1\pm\eta){Nx\over K},
\tag{2.2}
\]

and therefore

\[
                 {dx\over dt}=-(1\pm\eta){x\over K}.
\tag{2.3}
\]

The target time is

\[
                 T={K\over20}\log m.
\tag{2.4}
\]

The crucial exact jump identity is the following. While an owner \(X\)
is alive, selection of \(e\not\ni X\) removes from its current link
exactly

\[
 a_X(e)=|\{f:X\in f,\ f\cap e\ne\varnothing\}|
\tag{2.5}
\]

options. There are no simultaneous accepted edges, no ganged arcs, and
no inclusion--exclusion error between different selected edges.

## 3. Literal path-mesh hierarchy

The proved width-two estimate is

\[
                 a_X(e)\le(20+o(1)){D_X\over m^2}.
\tag{3.1}
\]

To regenerate it, one must also control paths meeting one protected edge
several times and paths meeting several protected edges. Both are covered
by one witness-counting lemma.

Let \(e_1,\ldots,e_j\) be pairwise vertex-disjoint repaired edges, none
containing \(X\). For positive integers
\(\boldsymbol c=(c_1,\ldots,c_j)\), put \(s=\sum_i c_i\) and define

\[
 B_X^{\boldsymbol c}(e_1,\ldots,e_j)
 =
 \sum_{f\ni X}\prod_{i=1}^j
       \binom{|f\cap e_i|}{c_i},
\tag{3.2}
\]

where the intersections in (3.2) are owner intersections. Thus
\(B^{(1)}_X(e)\) counts intersection witnesses with multiplicity, while

\[
 a_X(e)
 =\sum_{c\ge1}(-1)^{c+1}B_X^{(c)}(e)
\tag{3.3}
\]

is exact binomial inversion.

### Lemma 3.1 (disjoint path-mesh bound)

Uniformly for
\(1\le j\le s\le L:=\lceil100(\log m)^2\rceil\),

\[
 \boxed{
 {B_X^{\boldsymbol c}(e_1,\ldots,e_j)\over D_X}
 \le
 \left({Cs^4\over m^2}\right)^s+m^{-H/5}.
 }
\tag{3.4}
\]

The same estimate holds for a fixed root link. For \(s=1\), the root-link
bound is superpolynomially smaller.

#### Proof

First remove intersections through a root. For a prescribed owner \(X\),
the normalized number of options with a prescribed compatible root is
\(1/\binom mH\). For a prescribed root, the normalized number containing
a prescribed owner is \(r/\binom MH\). Summing over at most \(Lr\)
witnesses makes the total at most \(m^{-H/4}\).

We may therefore choose \(s\) distinct owner witnesses

\[
 Y_{i,1},\ldots,Y_{i,c_i}\in f\cap e_i.
\tag{3.5}
\]

Group a possible witness \(Y\) by \(d=d_J(X,Y)\). If \(d<H/4\), a
repaired promotion path contains at most \(4d+2\) owners on the
\(d\)-sphere about \(X\). If \(d\ge H/4\), the exact owner-pair formula
and the \(r\) possible phases give a total at most \(m^{-H/3}\).
All far-sphere terms are therefore absorbed by \(m^{-H/5}\).

For close witnesses, expose their phase starts by expanding the already
exposed two-sided phase hull. If the next start is separated from that
hull by a gap \(g\ge1\), it fixes \(g\) new leaving coordinates and
\(g\) new entering coordinates. The endpoint-atom factorial quotient is
at most

\[
                 \binom{m-L}{g}^{-2}.
\tag{3.6}
\]

For a fixed exposure step there are at most \(Cs^2(g+1)\) choices of
side, witness, and equal-distance tie with gap \(g\). The sphere and
endpoint sums satisfy

\[
 \sum_{d\ge1}{8d+4\over\binom{m-L}{d}^{\,2}}
 \le {C\over m^2}.
\tag{3.7}
\]

The factor \(2^s(s!)^4\) dominates the remaining orientations, exposure
orders, assignments to the \(e_i\), and choices of the \(c_i\) witnesses
inside each \(e_i\). Since

\[
                 2^s(s!)^4\le(Cs^4)^s,
\tag{3.8}
\]

multiplying the \(s\) endpoint quotients proves (3.4). The common
physical representation multiplicity cancels. \(\square\)

For \(s=1\), this is (3.1). For \(j=1,s=2\), it says that the paths
counted by \(a_X(e)\) which share a second owner with \(e\) have relative
mass \(O((\log m)^8/m^4)\). Thus conditioning \(e\) to survive does not
silently protect a long common segment of a positive fraction of the
link.

### Corollary 3.2 (mesh energies)

The same endpoint exposure, now inside one fixed repaired path \(f\),
gives the internal census

\[
 \sum_e\binom{|e\cap f|}{c}
 \le KD\left({Cc^4\over m^2}\right)^{c-1}
 \qquad(1\le c\le L).
\tag{3.9}
\]

Indeed, the left side is
\(\sum_{S\subseteq f,\ |S|=c}d(S)\); exposing the \(c-1\) starts after
the first gives exactly the preceding endpoint calculation. Iterating
(3.9) over pairwise disjoint \(e_i\) gives, for each pattern
\((j,\boldsymbol c)\),

\[
 \sum_{(e_1,\ldots,e_j)}^{*}
 B_X^{\boldsymbol c}(e_1,\ldots,e_j)
 \le
 D_X(KD)^j
 \left({Cs^4\over m^2}\right)^{s-j}.
\tag{3.10}
\]

The star means pairwise disjointness and avoidance of \(X\). Since
\(m^{-H/5}\le(Cs^4/m^2)^s\) uniformly for \(s\le L\), multiplying
(3.10) by the maximum in (3.4) yields

\[
 \boxed{
 \sum_{(e_1,\ldots,e_j)}^{*}
 \left(B_X^{\boldsymbol c}(e_1,\ldots,e_j)\right)^2
 \le
 (KD)^jD_X^2
 \left({Cs^4\over m^2}\right)^{2s-j}.
 }
\tag{3.11}
\]

This is the exact width-\(2s\) intersection-moment hierarchy. It is
strictly stronger than a maximum pair-codegree estimate.

For every \(h\ge2\) with \(hs\le L\), the same
maximum-times-sum argument gives the power form

\[
 \sum_{(e_1,\ldots,e_j)}^{*}
 \left(B_X^{\boldsymbol c}(e_1,\ldots,e_j)\right)^h
 \le
 (KD)^jD_X^h
 \left({Cs^4\over m^2}\right)^{hs-j}.
\tag{3.12}
\]

We do not monitor every composition \(\boldsymbol c\) as a separate
random variable. For total witness order \(s\), define the aggregated
power energy

\[
 \mathfrak E_{s,h}(X)
 =
 \sum_{j=1}^s{1\over j!}
 \sum_{\substack{c_1+\cdots+c_j=s\\c_i\ge1}}
 {1\over\prod_i c_i!}
 \sum_{(e_1,\ldots,e_j)}^*
 \left(B_X^{\boldsymbol c}(e_1,\ldots,e_j)\right)^h.
\tag{3.13}
\]

Summing (3.12) over the compositions only changes the absolute constant
\(C\): the exponential-generating-function weights have total at most
\(e^s\), already absorbed by \((Cs^4)^s\). Thus only \(O(L^2)\) energies
\(\mathfrak E_{s,h}\), not exponentially many composition types, are
monitored. Binomial inversion acts linearly on these aggregated energies.

## 4. Conditional scale and exact generator

Suppose \(X,e_1,\ldots,e_j\) are still active. A link option counted with
\(s\) owner-intersection witnesses has \(s\) protected owners. Relative
to the unconditioned link its natural scale therefore gains \(u^{-s}\).
Put

\[
             \varepsilon_s(u)={Cs^4\over m^2u}.
\tag{4.1}
\]

For a first moment, the dynamic reference version is obtained by replacing
\((Cs^4/m^2)^s\) with \(\varepsilon_s(u)^s\), \(D\) with
\(\mathcal D_R\), and \(D_X\) with the current resource degree.
For an \(h\)-th power, as in (3.12), as many as \(hs\) distinct
intersection owners may be protected. Since \(h\ge2\) and \(s\ge j\),

\[
                 hs\le2(hs-j).
\tag{4.2}
\]

Thus every power energy is safely controlled by the single master
parameter

\[
        \widehat\varepsilon(u)={CL^4\over m^2u^2}.
\tag{4.3}
\]

This scaling is verified by the generator rather than assumed. Fix a
protected cluster and let \(g\) be the next selected edge. If \(g\)
meets a protected resource, the stopped cluster terminates. Otherwise
the decrement caused by \(g\) is exactly the next disjoint mesh count.
If \(g\) meets a link option in several owners, (3.3) counts that option
once; the terms with two or more witnesses are precisely the
\(s\ge2\) levels of Lemma 3.1.

For an owner link, summing the degrees of the unprotected vertices of a
link option gives the main conflict count

\[
       \bigl(1+(r-1-j)q\bigr)\mathcal D_R.
\tag{4.4}
\]

For a root link it is \((r-j)q\mathcal D_R\). Pair overcounts and
multiple intersections are, by exact binomial inversion, bounded by the
next mesh energies. Their total relative contribution is

\[
                 O(L^2\varepsilon_L(u)+1/(m^2u)).
\tag{4.5}
\]

On the other hand, the owner-cluster reference

\[
 D_Xxu^{r-1}\varepsilon_s(u)^s
\tag{4.6}
\]

has logarithmic derivative

\[
 -{1+(r-1-s)q\over K}.
\tag{4.7}
\]

The difference between \(j\) in (4.4) and \(s\) in (4.7) is exactly
supplied by the \(s-j\) additional protected-owner terms in the
multiplicity hierarchy. Thus (4.4)--(4.7), summed over all
\(\boldsymbol c\), give the exact reference drift up to (4.5).

## 5. Growing-rank martingale lemma

We now state the restriction calculation in the aggregate form actually
needed. A mesh energy means an aggregate \(\mathfrak E_{s,h}\) from
(3.13), not an individual composition or tiny cluster.

### Claim 5.1 (unproved finite-buffer regeneration)

The statement in this subsection is retained only to locate the failed
argument. It does not follow from the finite hierarchy: its moving input
top is uncontrolled. MDLE from the 2026-07-27 audit is a sufficient
replacement.

Let \(u\ge z\), and put

\[
 J=\lceil20\log m\rceil,\qquad
 L=\lceil100(\log m)^2\rceil.
\]

Fix a checkpoint \(i\), put

\[
 L_i=L-iJ,
\]

and suppose that, outside a declared exceptional mass, root and owner
degrees, internal pair sums, and all aggregate mesh energies (3.13) of
total witness order at most \(L_i\) satisfy their reference bounds with
relative error at most \(\eta=m^{-1/10}\). Run for one checkpoint
interval

\[
                 \tau={K\over40},
\]

stopping at the first violation among energies of order at most
\(L_i-J\), or at \(x=z\).
Put

\[
             \varepsilon_*={CL^4\over m^2z^2}.
\tag{5.1}
\]

For every fixed root or owner, and for every normalized aggregate mesh
energy of order at most \(L_i-J\) attached to it, the probability of a
relative error larger than \(\eta\) during this interval is at most

\[
2\exp\left[-{c\eta^2\over T\varepsilon_*}\right]
 +\left({CT\varepsilon_*\over\eta}\right)^J.
\tag{5.2}
\]

The same bound holds for the internal pair energy. The use of the global
time \(T\), rather than \(\tau\), on the right side is a harmless
overestimate.

#### Proof

Consider first a live owner degree \(d(X)\). At a jump caused by \(g\),
its decrement is \(a_X(g)\). By (3.3), (3.11), and the dynamic scaling,

\[
\begin{aligned}
 {d\langle M_X\rangle_t\over dt}
 &= {1\over K\mathcal D_R}
       \sum_g a_X(g)^2 \\
 &\le C\varepsilon_*d(X)^2,
\end{aligned}
\tag{5.3}
\]

for the compensated stopped martingale. No pointwise maximum-jump bound
is assumed after restriction. Instead truncate at normalized jump size

\[
                 b={T\varepsilon_*\over\eta}.
\tag{5.4}
\]

The power energies (3.12) and Markov's inequality show that the
compensator of jumps larger than \(bd(X)\) is at most
\((CT\varepsilon_*/\eta)^J\). On the complementary event, Freedman's
denominator is
\(O(T\varepsilon_*+b\eta)=O(T\varepsilon_*)\), which gives the first
term of (5.2).

For a mesh energy, apply the generator to each square, or more generally
to a power \(A^h\) of a mesh count \(A\). If \(B\) is the decrement
caused by the selected edge, then

\[
 (A-B)^h-A^h
 =\sum_{\ell=1}^h(-1)^\ell\binom h\ell A^{h-\ell}B^\ell.
\tag{5.5}
\]

After summing over the protected disjoint edges and over the selected
edge, every term on the right is exactly a higher mesh energy. If the
selected edge has several owner intersections, binomial inversion (3.3)
places it at the corresponding multiplicity level. Corollary 3.2 bounds
an order increase of \(\ell\) by
\((C\varepsilon_*)^\ell\). The \(\ell=1\) term is the reference drift
computed in Section 4; the sum of the \(\ell\ge2\) terms is
\(O(T\varepsilon_*)\).

There is one bookkeeping point in the outer energy sum. Two protected
tuples appearing in a cross term need not be mutually disjoint. Partition
their union by the connected components of its edge-intersection graph.
Inside each component choose a spanning forest. Reverse counting along a
forest edge costs at most \(K\mathcal D_R\), while merging the two free
edge indices removes exactly one factor \(K\mathcal D_R\) from the
normalization in (3.11). Thus a component merge is no larger than the
corresponding lower-order mesh energy. If the intersection uses several
owners, its extra multiplicity is charged to (3.9). Consequently every
non-disjoint cross term is bounded by the same partition of
(3.11)--(3.12); no unrecorded covariance term remains.

This generator expansion also audits the moving top boundary. Starting
from an asserted energy of order at most \(L_i-J\), a term which exits
the available hierarchy at \(L_i\) must advance by at least \(J\)
witness levels. It therefore contains at least \(J\) factors
\(C\varepsilon_*\), and truncation contributes at most \(\eta^{-J}\).
Its ordered jump times lie in a time simplex of volume at most
\(\tau^J/J!\le T^J/J!\). Hence that checkpoint tail is bounded by

\[
                 (CT\varepsilon_*/\eta)^J.
\tag{5.6}
\]

This estimate controls a chain which advances by \(J\) levels from its
starting order. The moving boundary starts at \(L_i-J\), so every exit
from the recorded hierarchy at \(L_i\) has exactly this property. No
claim is made for the discarded top strip
\(L_i-J<\text{order}\le L_i\).

The predictable quadratic variations of the aggregate energies are
bounded in the same expansion by
\(CT\varepsilon_*\) times the square of their reference values.
Freedman gives (5.2). Repeating the calculation with two protected
vertices gives the internal-pair statement. No constant is exponential
in \(K\); the complete rank dependence is the displayed factor \(K\)
inside \(T\). \(\square\)

### Numerical audit

With \(z=m^{-1/20}\), \(T=(K/20)\log m\),
\(J=20\log m\), and \(L=100(\log m)^2\),

\[
 T\varepsilon_*
 =O(m^{-9/10}\log^9m),
\tag{5.7}
\]

\[
 {\eta^2\over T\varepsilon_*}
 \ge {c m^{7/10}\over\log^9m},
\tag{5.8}
\]

and

\[
 \left({CT\varepsilon_*\over\eta}\right)^J
 \le\exp[-c(\log m)^2].
\tag{5.9}
\]

All estimates are uniform for \(K=r+1\sim m\).

## 6. Exceptional-mass cleaning

There are too many resources for a union bound, and none is used.
Average (5.2) over the transitive root and owner shores and over the
incidence-weighted mesh energies. If \(\delta_m\) denotes the right side
of (5.2), Markov's inequality shows that, with probability \(1-o(1)\),
the bad root fraction and bad owner-incidence fraction at a checkpoint
are at most

\[
 \beta_m=\sqrt{\delta_m}\le\exp[-c(\log m)^2].
\tag{6.1}
\]

The incidence weighting is legitimate because every resource martingale
is stopped at its first boundary crossing. At that instant its degree is
at most \((1+2\eta)\) times the reference degree (raw degrees have only
downward jumps, and the upper reference boundary moves continuously).
Thus averaging the stopped failure indicators already averages their
residual degrees; no uncontrolled original-degree factor is introduced.

The owner assertion means

\[
 \sum_{X\ {\rm bad}}d_t(X)
 \le\beta_m\sum_Xd_t(X)
 =\beta_m rE_t=o(E_t).
\tag{6.2}
\]

Suppress every active edge incident with a bad owner or bad root.
Equation (6.2) and its root analogue show that only \(o(E_t)\) edges are
suppressed, so the total jump rate changes by \(o(1)\).

For the mesh hierarchy, charge a bad cluster \(C\) by its base mass
\(A_C/(K\mathcal D_R)^j\). For each owner, sum these charges before
applying Markov and declare the owner bad only if the aggregate exceeds
the threshold. Thus one tiny bad cluster does not contaminate its owner,
and the declared owner incidence is still bounded by (6.2). This is
weighted RPRN cleaning, not a union of static containment neighborhoods.

Use the checkpoints

\[
 t_i=iK/40,\qquad
 0\le i\le E:=\lceil2\log m\rceil.
\tag{6.3}
\]

Their last time is at least \(T=(K/20)\log m\). Moreover

\[
 L_E\ge100(\log m)^2-(2\log m+1)(20\log m)
      \ge50(\log m)^2
\tag{6.4}
\]

for large \(m\). Thus Lemma 5.1 applies inductively with input order
\(L_i\) and output order \(L_{i+1}\). In particular the degree and
quadratic energies, whose orders are fixed, remain inside the protected
core throughout. The total bad-root count is

\[
 O(\log m)\beta_mN=o(zN),
\tag{6.5}
\]

and the total suppressed edge incidence is \(o(E_t)\) at every
checkpoint. Bad roots are literal root waste. The statement is only
about this random trajectory; it does not assert regeneration for
adversarial reachable residuals.

## 7. Integration and owner leave

Conditional on a valid replacement for Claim 5.1 and on noncascading
weighted cleaning, one obtains

\[
 d(A)=(1\pm\eta)\mathcal D_R(x)
\tag{7.1}
\]

outside \(o(zN)\) roots, uniformly to time \(T\). Equations
(2.2)--(2.3) yield

\[
 {dx\over dt}=-{x\over K}(1+O(\eta))+o(z/K).
\tag{7.2}
\]

Since

\[
                 {T\eta\over K}
 =O(m^{-1/10}\log m)=o(1),
\tag{7.3}
\]

integration gives

\[
 x(T)=\exp(-T/K+o(1))+o(z)
     =m^{-1/20}(1+o(1)).
\tag{7.4}
\]

Every jump selected one actual repaired ring, so this is an integral
matching. If \(s=(z+o(1))N\) roots are missed, the exact owner ledger is

\[
\begin{aligned}
 W-r(N-s)
 &=W-rN+rs\\
 &\le O((H+\kappa)N)+(z+o(1))rN\\
 &=O\left(\left({H+\kappa\over m}+z\right)W\right)
 =o(W).
\end{aligned}
\tag{7.5}
\]

This proves Conditional Conclusion 0.1 once MDLE supplies the valid
replacement for Claim 5.1. The retraction at the top of the note explains
why the finite buffer alone does not do so.

## 8. Audit boundary

Used:

1. exact root and owner degrees and the ledger (1.1);
2. the repaired cyclic-path sphere count;
3. the exact path influence \(a_X(e)=O(D_X/m^2)\);
4. the multiplicity-aware disjoint mesh extension (3.4);
5. exact one-edge jumps of continuous random greedy; and
6. the explicit estimate
   \(T\varepsilon_*=O(m^{-9/10}\log^9m)\).

Not used:

1. Pippenger--Spencer, Gould--Kelly, or any fixed-rank theorem;
2. maximum pair codegree as a surrogate for path influence;
3. an arbitrary-residual regeneration assertion;
4. fractional rounding; or
5. an absorber.

The distinction between (3.1) and (3.4) is essential. The first controls
one degree martingale. The second gives static pure mesh moments.
Turning those moments into a high-probability endogenous trajectory
still requires ADLE/MDLE; Claim 5.1 does not do so.

## 9. Conditional quantitative statement

\[
 \boxed{
 |Q|\ge(1-m^{-1/20}-o(1))N_H,
 }
\tag{9.1}
\]

and

\[
 \boxed{
 W-r|Q|
 =O\left(\left({H+\kappa\over m}+m^{-1/20}\right)W\right)
 =o(W).
 }
\tag{9.2}
\]

The growing-rank concentration ledger is

\[
 \boxed{
 \text{total normalized quadratic variation}
 \le
 T{C(\log m)^8\over m^2z^2}
 =O(m^{-9/10}\log^9m)=o(1).
 }
\tag{9.3}
\]
