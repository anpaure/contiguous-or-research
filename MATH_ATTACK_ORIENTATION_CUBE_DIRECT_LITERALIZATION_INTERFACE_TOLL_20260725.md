# Direct literalization of recursive orientation cubes: the Gaussian interface toll

Date: 2026-07-25

Pure mathematics only.  No computation, finite search, or external input is
used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  The recursive half-depth-rainbow orientation-cube
cycles can be literalized directly, with no symmetric-chain decomposition:
after cutting them into \(C\) pieces, the exact independent-reset length is

\[
 W+2HC.
\]

More generally, useful-prefix fusion gives the exact length

\[
 W+2H+\sum_{j<C}(b_j-1),
\]

where \(b_j\) is the shortest positive MTF bridge to the next useful
radius-\(H\) prefix.  Thus a global SCD is not a requirement of the literal
compiler.

This does **not** turn one fixed coordinate pairing into a coefficient-one
central-band word.  There is an exact interface obstruction.  If a literal
word of length \(W+E\) retains one principal endpoint for every middle owner
and all but the boundary endpoints are depth-\(q\) windows inside orientation
cubes of one fixed coordinate pairing, then

\[
 \boxed{
 E+qC\ge D_{m,q}:=\sum_f(T_{f,q}-V_f)_+ .}
 \tag{0.1}
\]

Here \(C\) is the number of fixed-frame pieces,

\[
 T_{f,q}=
 \frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}
 \tag{0.2}
\]

is the number of lower rank-\((m-q)\) targets having \(f\) full pairs, and

\[
 V_f=
 \frac{m!}{f!f!(m-2f)!}\,2^{m-2f}
 \tag{0.3}
\]

is the number of middle starts of the only fixed-pair source type that can
produce them internally.

At Gaussian depth \(q=A\sqrt m+O(1)\),

\[
 \boxed{
 D_{m,q}=(\kappa_A+o(1))W,\qquad
 \kappa_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0 .}
 \tag{0.4}
\]

Consequently:

1. any fixed-frame compiler with \(C=o(W/H)\) has \(E=\Omega_A(W)\);
2. any fixed-frame coefficient-one attempt must have
   \(C\ge(\kappa_A/A+o(1))W/\sqrt m=\Omega_A(W/H)\);
3. cutting at that density and independently resetting the useful prefix
   costs \(2HC=\Omega_A(W)\), so that direct-reset implementation cannot
   have coefficient one.

The obstruction is not a tax on the *name* of a coordinate matching.  The
exact MTF bridge depends only on the two useful ordered prefixes.  A change
of pair frame can therefore have bridge length one when those prefixes are
already aligned.  The precise remaining escape is an owner-dependent,
phase-changing frame selection with

\[
 \sum_j(b_j-1)=o(W)
 \tag{0.5}
\]

and only \(o(W)\) aggregate missing lower and upper shadows through depth
\(H\).  The polynomial mixed-matching reservoir already removes the
fixed-frame bias fractionally, but no integral owner-disjoint selection with
these two properties is presently proved.  Thus the answer is:

> **Local recursive cycles do bypass a global SCD at the compiler level,
> but one fixed pair frame cannot cover a Gaussian band.  It incurs the
> positive interface-service toll (0.1)--(0.4).  A direct coefficient-one
> construction must mix coordinate matchings at mesoscopic density and fuse
> those phase changes with sublinear total useful-prefix toll.**

### 0.1 Exact path-hitting dictionary for the odd wreath factor

The attachment formulation is most naturally stated on

\[
 n=2m+1.
\]

Fix a cyclic order \(\pi\) of \([n]\), and let \(I_\pi(j,r)\) be the set of
the \(r\) consecutive coordinates beginning at cyclic position \(j\).  The
middle factor cycle is exactly

\[
 \boxed{X_j=I_\pi(j,m),\qquad j\in\mathbb Z_n.}
 \tag{PH.1}
\]

For \(0\le q<m\),

\[
 \bigcap_{a=0}^{q}X_{j+a}=I_\pi(j+q,m-q),
 \qquad
 \bigcup_{a=0}^{q}X_{j+a}=I_\pi(j,m+q).
 \tag{PH.2}
\]

For a lower target \(T\in\binom{[n]}{m-q}\), put

\[
 U_T=\left\{X\in\binom{[n]}m:T\subseteq X\right\}.
 \tag{PH.3}
\]

Since the intersection of every consecutive \((q+1)\)-vertex path in
(PH.1) has size exactly \(m-q\), one has the equivalence

\[
 \boxed{
 T\text{ is a lower depth-}q\text{ shadow}
 \iff
 \text{one factor cycle has a consecutive }(q+1)\text{-vertex path in }U_T.}
 \tag{PH.4}
\]

Containment forces equality in (PH.4).  The same criterion applies to a
support-separated orientation-cube segment: its first \(q\) transition
directions are distinct, so its \((q+1)\)-vertex intersection again has
size \(m-q\).

In odd dimension, complementation shifts the depth:

\[
 \binom{[n]}{m+q}
 \stackrel{c}{\longleftrightarrow}
 \binom{[n]}{m-(q-1)}.
 \tag{PH.5}
\]

Thus upper depth \(q\) must be read from the complementary lower
depth-\((q-1)\) path-hitting ledger.  It is not the direct complement of
lower depth \(q\).

This dictionary is used below only as a sufficient construction and as the
coverage test for the designated factor cycles.  Nothing here asserts that
an arbitrary length-\(W+o(W)\) OR word can be converted, at \(o(W)\) cost,
to singleton letters, FIFO interval states, the cycles (PH.1), or a central
near-Ucycle.  That normalization is unsupported.  Every obstruction below
is explicitly conditional on retaining the stated principal endpoints and
fixed-frame internal paths.

## 1. Literal useful-prefix states

For a nonempty set-word \(X_1,\ldots,X_L\), order the nonempty level sets of
the last-occurrence function by decreasing last occurrence.  This gives an
ordered partition

\[
 \Sigma=(C_1,\ldots,C_r).
\]

Appending a nonempty mask \(X\) performs the MTF update

\[
 M_X(\Sigma)=
 (X,C_1\setminus X,\ldots,C_r\setminus X),
 \tag{1.1}
\]

with empty blocks deleted.  Every prefix union of the resulting state is a
literal suffix OR ending at the current word position.  In particular, at
one endpoint there is at most one represented set of each prescribed rank.

A radius-\(H\) useful prefix is an ordered list of disjoint nonempty blocks

\[
 \Lambda=(B_1,\ldots,B_{2H+1}),
 \tag{1.2}
\]

where \(|B_1|=m-H\) and \(B_2,\ldots,B_{2H+1}\) are singletons.  Its prefix
unions have all ranks \(m-H,m-H+1,\ldots,m+H\).  The residual last-occurrence
tail is irrelevant and need not be recoalesced.

For

\[
 U_t=B_1\cup\cdots\cup B_t,
\]

let \(t_*(\Sigma,\Lambda)\) be the least \(t\in\{0,\ldots,2H+1\}\) such
that, after deleting \(U_t\) from every source block, the surviving source
state begins with

\[
 B_{t+1},\ldots,B_{2H+1}.
 \tag{1.3}
\]

The empty suffix makes \(t=2H+1\) always admissible.

### Theorem 1.1 (exact useful-prefix bridge)

The shortest positive MTF word carrying \(\Sigma\) to a state beginning
with \(\Lambda\) has length

\[
 \boxed{b(\Sigma,\Lambda)=\max\{1,t_*(\Sigma,\Lambda)\}.}
 \tag{1.4}
\]

#### Proof

If \(t=t_*>0\), append

\[
 U_t,U_{t-1},\ldots,U_1.
\]

Their new last-occurrence blocks are \(B_1,\ldots,B_t\), and (1.3) supplies
the remaining useful suffix from the old state.  If \(t_*=0\), the one
update \(B_1\) preserves the already present useful prefix.

Conversely, after \(b\) updates, all update-created blocks precede the
surviving source blocks.  If the first \(a\) target blocks were created by
the updates, their union is \(U_a\) and the surviving source must begin with
\(B_{a+1},\ldots,B_{2H+1}\).  Hence \(t_*\le a\le b\).  Positivity gives
\(b\ge1\).  This proves (1.4). \(\square\)

The theorem contains no pair-frame label.  In particular,

\[
 \Sigma\text{ already begins with }\Lambda
 \quad\Longrightarrow\quad b(\Sigma,\Lambda)=1,
 \tag{1.5}
\]

even if the next rotor piece is interpreted using a different coordinate
matching.  Thus there is no universal positive bridge toll caused solely by
changing frames.

## 2. An exact no-SCD compiler

Call a middle-owner piece radius-\(H\) legal if:

1. it has one principal endpoint for each of its distinct middle owners;
2. its first principal endpoint has a useful prefix (1.2);
3. after initialization, each next owner is reached by one nonempty MTF
   update; and
4. at every principal endpoint the prescribed lower and upper flags through
   depth \(H\) are the prefix unions of its useful state.

Long-residence pair-flip rotor paths have exactly this property.  In
particular, the recursive half-depth-rainbow factors from
`ROTOR_SCD_PARITY_CHECK_CYCLE_TILING_20260725.md`, cut into paths, are legal
whenever their active dimension is greater than \(2H\).

Let \({\cal P}_1,\ldots,{\cal P}_C\) be legal pieces partitioning all \(W\)
middle owners.  Let \(b_j\) be the bridge length (1.4) from the terminal
state of piece \(j\) to the useful initial prefix of piece \(j+1\).  For
\(1\le q\le H\), let \(M_q^-\) and \(M_q^+\) be the numbers of lower and
upper rank-\((m\mp q)\) masks not exposed at any principal endpoint.
Equivalently, in the wreath/path model, \(M_q^-\) counts the targets \(T\)
whose up-sets \(U_T\) contain no consecutive \((q+1)\)-vertex principal
path.  In the odd master, \(M_q^+\) is the corresponding complementary
lower depth-\((q-1)\) path-hitting defect, as in (PH.5).

### Theorem 2.1 (direct phase compiler)

There is one nonzero contiguous-OR word covering the complete central band
whose length is at most

\[
 \boxed{
 W+2H+\sum_{j=1}^{C-1}(b_j-1)
 +\sum_{q=1}^{H}(M_q^-+M_q^+).}
 \tag{2.1}
\]

No SCD, common chain colour, or rankwise factorization is used.

#### Proof

Reverse-write the \(2H+1\) useful blocks of the first piece.  A piece with
\(K_j\) owners then needs \(K_j-1\) further principal updates.  Insert a
shortest positive bridge of length \(b_j\) between consecutive pieces.
Since \(\sum_jK_j=W\), the raw length is

\[
 (2H+1)+\sum_j(K_j-1)+\sum_{j<C}b_j
 =W+2H+\sum_{j<C}(b_j-1).
\]

Every advertised flag is a prefix union of a physical last-occurrence state,
hence a literal suffix OR.  Finally append one literal copy of each missing
band mask.  This proves (2.1). \(\square\)

### Corollary 2.2 (exact direct coefficient-one criterion)

For fixed \(A\), the phase pieces give a \(W+o_A(W)\) central-band word if

\[
 \sum_{j<C}(b_j-1)=o_A(W),
 \qquad
 \sum_{q\le H}(M_q^-+M_q^+)=o_A(W).
 \tag{2.2}
\]

This is strictly weaker than first constructing a global SCD.  It asks only
for owner-disjoint legal chronology and aggregate target support.

Using independent useful-prefix initialization at every piece gives
\(b_j\le2H+1\) and the simpler raw bound

\[
 W+2HC.
 \tag{2.3}
\]

The facet--core braid is the depth-one instance of the same compiler: its
overlapping core windows preserve first-band masks without separate reset
letters.  The bridge formula (1.4) is the correct higher-depth interface
ledger.

## 3. The fixed-pair Gaussian capacity deficit

Fix a perfect coordinate matching

\[
 {\cal P}=\{P_1,\ldots,P_m\}
\]

of \([2m]\).  A lower rank-\((m-q)\) target of type \(f\) has \(f\) full
pairs, \(f+q\) empty pairs, and \(m-2f-q\) split pairs.  Its number is
\(T_{f,q}\) from (0.2).

An internal pair-flip depth-\(q\) window producing such a target must start
with the same \(f\) full pairs, \(f\) empty pairs, and \(m-2f\) split pairs.
There are only \(V_f\) such middle owners.  Therefore any collection of
internal fixed-frame windows represents at most

\[
 \sum_f\min\{T_{f,q},V_f\}=N_q-D_{m,q}
 \tag{3.1}
\]

distinct lower targets.  The identical statement holds in the upper rank by
complementation.

The exact capacity ratio is

\[
 \lambda_{f,q}:={V_f\over T_{f,q}}
 =2^q{\binom{f+q}{q}\over\binom{m-2f}{q}}.
 \tag{3.2}
\]

### Theorem 3.1 (positive fixed-frame Gaussian deficit)

If \(q=A\sqrt m+O(1)\), then

\[
 {D_{m,q}\over N_q}
 \longrightarrow
 \Delta(A):=\Phi(A/2)-e^{A^2}\Phi(-3A/2)>0,
 \tag{3.3}
\]

and hence (0.4) holds.

#### Proof

Give \(f\) the target law \(T_{f,q}/N_q\).  Stirling expansion of (0.2)
has saddle

\[
 f_*={ (m-q)^2\over4m}+O(1)
 ={m\over4}-{q\over2}+{q^2\over4m}+O(1),
 \tag{3.4}
\]

and second logarithmic derivative \(-16/m+o(1/m)\).  Thus

\[
 Z_m={4(f-f_*)\over\sqrt m}\Longrightarrow Z\sim N(0,1).
 \tag{3.5}
\]

For bounded \(Z_m\), expand the product in (3.2).  At \(f=f_*\),

\[
 \log\lambda_{f_*,q}=-{q^2\over m}+o(1)=-A^2+o(1).
\]

Also

\[
 {\partial\over\partial f}\log\lambda_{f,q}
 ={8q\over m}+o(m^{-1/2}),
\]

uniformly in the central window, while the quadratic remainder is \(o(1)\).
Consequently

\[
 \log\lambda_{f,q}=-A^2+2AZ_m+o(1).
 \tag{3.6}
\]

Since

\[
 {D_{m,q}\over N_q}
 =\mathbb E(1-\lambda_{f,q})_+,
\]

bounded convergence, with the standard exponentially small tail supplied by
Stirling's formula, gives

\[
 \begin{aligned}
 \Delta(A)
 &=\mathbb E(1-e^{-A^2+2AZ})_+\\
 &=\Phi(A/2)-e^{A^2}\Phi(-3A/2).
 \end{aligned}
\]

The integrand is positive on a set of positive Gaussian measure for every
\(A>0\), so \(\Delta(A)>0\).  Finally

\[
 {N_q\over W}=e^{-A^2+o(1)},
\]

which turns (3.3) into (0.4). \(\square\)

This is the fixed-\(A\) sharpening of the diverging-depth barrier in
`FIXED_PAIR_RESIDUAL_SCD.md` Section 8 and `CUBE_SHADOW_TILING.md`.  It is a
deterministic shortage of physical starts, not a failure of a particular
Gray code or local randomization.

### 3.1 Odd-master form

For direct comparison with (PH.1), let the ground set consist of \(m\)
fixed pairs and one unmatched coordinate \(z\).  Write \(\delta\in\{0,1\}\)
for the indicator of \(z\).  The lower target and middle-source counts are

\[
 T_{f,\delta,q}=
 \frac{m!}{f!(f+q+\delta)!(m-2f-q-\delta)!}
 2^{m-2f-q-\delta},
 \tag{3.7}
\]

\[
 V_{f,\delta}=
 \frac{m!}{f!(f+\delta)!(m-2f-\delta)!}
 2^{m-2f-\delta}.
 \tag{3.8}
\]

Their exact ratio is

\[
 {V_{f,\delta}\over T_{f,\delta,q}}
 =2^q
 {\binom{f+q+\delta}{q}\over
  \binom{m-2f-\delta}{q}}.
 \tag{3.9}
\]

The bounded bit \(\delta\) changes the saddle and the logarithm in (3.6) by
only \(O(m^{-1/2})\).  Summing both \(\delta\)-classes therefore gives

\[
 \sum_{\delta=0}^1\sum_f
 (T_{f,\delta,q}-V_{f,\delta})_+
 =(\kappa_A+o(1))\binom{2m+1}{m}
 \tag{3.10}
\]

for \(q=A\sqrt m+O(1)\), with the same \(\kappa_A\) as (0.4).  Hence the
fixed-frame obstruction applies directly to the odd path-hitting model.

## 4. The interface-service inequality

Consider a literal word of length \(L=W+E\) with \(W\) designated principal
endpoints, one for each middle owner.  Suppose these endpoints are divided
into \(C\) fixed-frame pieces.  At depth \(q\), every principal endpoint
except possibly the last \(q\) endpoints of a piece has its designated lower
flag supplied by an internal pair-flip window.  Thus at most \(qC\)
principal lower endpoints are boundary endpoints.  For upper flags, use the
first \(q\) endpoints of each piece; the same bound holds.

### Theorem 4.1 (exact interface toll)

For each sign separately,

\[
 \boxed{E+qC\ge D_{m,q}.}
 \tag{4.1}
\]

The conclusion permits arbitrary literal bridge words, arbitrary interval
witnesses crossing those bridges, and arbitrary recoding at the
nonprincipal positions.  It is a theorem about this designated
principal-endpoint/fixed-frame architecture; it is **not** a structural
theorem about all near-optimal OR words.

#### Proof

By (3.1), internal fixed-frame principal endpoints represent at most
\(N_q-D_{m,q}\) distinct rank-\((m-q)\) targets.  The boundary principal
endpoints add at most \(qC\) further targets.

At any physical endpoint all interval ORs ending there are the prefix unions
of one last-occurrence state.  They form a strictly nested chain, so one
endpoint represents at most one target of the prescribed rank.  There are
exactly \(E\) nonprincipal positions.  Therefore the complete word
represents at most

\[
 N_q-D_{m,q}+qC+E
\]

distinct lower targets.  Covering all \(N_q\) proves (4.1).  Complementation
gives the upper statement. \(\square\)

The displayed theorem uses the even master.  In the odd path-hitting master,
replace \(D_{m,q}\) by the two-\(\delta\) deficit in (3.10) for the lower
rank.  By (PH.5), the corresponding upper depth-\(q\) statement uses the
complementary lower depth \(q-1\), not the same index \(q\).

At \(q=H=A\sqrt m+O(1)\), Theorem 3.1 gives

\[
 E+HC\ge(\kappa_A+o(1))W.
 \tag{4.2}
\]

Thus facets and seam-crossing intervals do help, but one interface can
service at most \(q\) new depth-\(q\) targets.  No facet braid can evade this
endpoint count.

### Corollary 4.2 (reset dichotomy)

For a fixed-frame coefficient-one word, \(E=o(W)\) forces

\[
 C\ge(\kappa_A+o(1)){W\over H}.
 \tag{4.3}
\]

If those pieces are initialized independently, (2.3) has excess at least

\[
 2HC\ge(2\kappa_A+o(1))W.
 \tag{4.4}
\]

Hence a dense fixed-frame cut-and-reset repair is also impossible at
coefficient one.

For useful-prefix fusion, (4.3) and (2.1) instead require

\[
 \sum_{j<C}(b_j-1)=o(W).
 \tag{4.5}
\]

Equivalently, over the necessarily mesoscopic interface family, the average
excess bridge length must be \(o(H)\).  Constant-length bridges are fully
compatible with this requirement; independent \(\Theta(H)\)-length resets
are not.

## 5. Application to the recursive orientation-cube cycles

Choose a power-of-two active dimension \(\ell\) satisfying

\[
 H\ll\ell\ll m.
 \tag{5.1}
\]

In every typical fixed-pair orientation stratum, partition the active
coordinates into \(\ell\)-dimensional fibres and use the recursive cycle
factor

\[
 F_\ell(u,v)=
 \begin{cases}
 (F_{\ell/2}(u),v),&|u|+|v|\equiv0\pmod2,\\
 (u,F_{\ell/2}(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}
 \tag{5.2}
\]

Each cycle has length \(2\ell\), transition word \(\pi\pi\), coordinate
residence \(\ell\), and injective lower and upper shadow maps through depth
\(\ell/2\).  Thus each cut cycle is radius-\(H\) legal and has an exact
literal compiler.

The number of typical cycles is \(O(W/\ell)=o(W/H)\).  Middle owners in
strata with fewer than \(\ell\) split pairs have exponentially small total
mass and can be isolated using \(o(W/H)\) further pieces.  Hence the entire
fixed-frame recursive factor has

\[
 C=o(W/H).
 \tag{5.3}
\]

Independent literalization therefore costs only \(2HC=o(W)\).  Nevertheless,
Theorem 4.1 gives, at depth \(H\),

\[
 E\ge(\kappa_A+o(1))W.
 \tag{5.4}
\]

when the word is completed to all lower or all upper targets.  The pointwise
half-depth rainbow theorem is not contradicted: it prevents collisions
*inside each orientation fibre*, whereas (5.4) compares the total supply of
source pair types with the target pair-type census across all fibres.

This answers the original direct-literalization question for the recursive
cycles.  They compile physically and cheaply, but they do not cover a
Gaussian band inside one fixed frame.  Their cheap component count is in
fact too small to provide the required profile-changing windows.

## 6. Why changing coordinate matchings is the minimal escape

For a fixed target, its pair type changes when the coordinate perfect
matching changes.  Averaging over matchings satisfies the exact size-bias
identity from `MIXED_PAIR_ROUNDING.md`:

\[
 \pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f),
 \qquad \rho_q={N_q\over W}.
 \tag{6.1}
\]

Thus a polynomial reservoir of coordinate matchings carries an almost
perfect fractional typed block system with balanced middle degree, balanced
shadow degree at every \(q\le H\), and weighted relative pair-codegree
\(O(1/m)\).  This proves that (0.4) is a one-frame obstruction, not an
ownerwise obstruction surviving all frames.

However, fractional selection does not give a literal word.  The typed
edges have growing size, and degree plus \(O(1/m)\) relative codegree does
not imply an almost-perfect integral matching in that regime.  The missing
operation is an owner-disjoint choice of phase blocks from different frames.

Theorem 1.1 shows exactly what must also be preserved when those blocks are
ordered: not the full residual state and not the pair-frame name, but only
the useful ordered prefix.  Hence phase-changing frame selection and literal
fusion should be treated as one theorem, not as a block matching followed by
an uncharged concatenation.

## 7. Exact successor theorem

The direct non-SCD route is reduced to the following statement.

The display below uses the even middle layer for consistency with Sections
3--6.  In the odd wreath form, replace it by \(\binom{[2m+1]}m\), use
(PH.4) for lower coverage, and use (PH.5) for the upper ledger.

> **Mixed-frame useful-prefix necklace theorem \(\mathrm{MFUP}_A\).**  For
> \(H=\lceil A\sqrt m\rceil\), select and order radius-\(H\) legal segments
> of recursive orientation-cube cycles, allowing the coordinate matching to
> depend on the segment, so that:
>
> 1. their middle owners partition the relevant middle layer;
> 2. for every lower target \(T\), use (PH.4): failure at depth \(q\) means
>    that no selected factor segment has a consecutive \((q+1)\)-vertex
>    path in \(U_T\).  Let \(M_q^-\) count these failures and let \(M_q^+\)
>    be the complementary shifted lower defect from (PH.5).  Require
>    \[
>      \sum_{q\le H}(M_q^-+M_q^+)=o_A(W);
>    \]
> 3. for the exact useful-prefix bridge lengths in their chosen order,
>    \[
>      \sum_j(b_j-1)=o_A(W).
>    \]

### Corollary 7.1

If \(\mathrm{MFUP}_A\) holds, then there is a literal contiguous-OR word of
length \(W+o_A(W)\) covering every mask in ranks \(m-H,\ldots,m+H\).

#### Proof

Apply Theorem 2.1. \(\square\)

This theorem is weaker than a global SCD: no shadow target is assigned a
common chain colour across depths, and duplicate targets are harmless.  It
is stronger than the existing mixed-frame fractional reservoir because it
requires an integral owner partition, simultaneous aggregate shadow support,
and one physical chronology with paid interfaces.

## 8. Theorem ledger

### Proved

1. Recursive orientation-cube cycles admit a direct literal MTF compiler;
   no global SCD is required for physical realization.
2. The useful-prefix bridge metric is exact, and the raw compiler length is
   \(W+2H+\sum(b_j-1)\).
3. One fixed coordinate pairing has the positive Gaussian pair-type deficit
   (0.4) at every fixed \(A>0\).
4. Arbitrary literal recoding obeys the interface-service inequality
   \(E+qC\ge D_{m,q}\) inside the stated principal-endpoint architecture.
5. Long fixed-frame recursive cycles have too few interfaces; dense
   independent reset has linear excess.
6. Frame changes themselves have no intrinsic MTF label toll.  Only useful
   prefix incompatibility is charged.
7. Wreath shadow coverage is exactly the Johnson up-set path-hitting
   condition (PH.4), with the odd upper/lower shift (PH.5).

### Not proved

1. \(\mathrm{MFUP}_A\), or any equivalent integral mixed-frame necklace
   selection.
2. A phase ordering with \(o(W)\) total useful-prefix bridge excess.
3. The coefficient-one contiguous-OR theorem.
4. Any reduction of arbitrary near-optimal OR words to singleton
   near-Ucycles.

The minimal escape from the no-go is therefore exact: mix coordinate
matchings owner-dependently, at enough spatial resolution to remove the
fixed-frame type deficit, while keeping average bridge excess \(o(H)\) and
aggregate shadow defect \(o(W)\).  Resolving a global SCD is one sufficient
way to impose that coherence, but it is not logically necessary.
