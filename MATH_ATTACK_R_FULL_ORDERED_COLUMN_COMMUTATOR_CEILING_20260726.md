# Full ordered-column commutator ceiling and the exact multi-carrier boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Fix

\[
q=\lfloor A\sqrt m\rfloor,\qquad A>0,
\qquad q<r,
\qquad W=\binom{2m}{m}.
\tag{0.1}
\]

There are two different notions of a multi-carrier construction.

1. A **diagonal first-order bank** changes many carrier slots with
   nonzero individual derivatives. If the changed slots are dispersed,
   \(s=\Theta(r/q)\) slots can be visible on a positive fraction of the
   rooted \(q\)-windows. There is no direction-count invariant forbidding
   this.
2. A **pure commutator** cancels every proper lower-order carrier
   derivative and keeps only the joint interaction of a carrier set
   \(S\). Its ordered-column derivative is supported only on windows which
   meet every carrier in \(S\). In an isometric \(C_{2r}\)-packet this is
   at most a \(q/r\) fraction of the packet, independent of \(|S|\).

The second statement is the exact obstruction requested in this lane.
Adding more entries to one bounded-order commutator does not multiply its
influence.

There is also an immediate correction to the proposed target conclusion.
If \(B_\times\) is the number of actual cross-quartet rooted
depth-\(q\) windows, \(L\) is owner/start leave, and
\(M_{q,\mathrm{hard}}\) is the number of residual holes in the audited
hard target-profile window, then the Gaussian Hall theorem gives

\[
\boxed{
B_\times+L+M_{q,\mathrm{hard}}
\ge(\delta_A-o(1))W.}
\tag{0.2}
\]

Consequently

\[
B_\times+L+M_{q,\mathrm{hard}}=o(W)
\tag{0.3}
\]

is incompatible with the Hall toll when \(B_\times\) has the meaning
used in that theorem. A successful construction instead needs
\(B_\times=\Omega_A(W)\), while \(L+M_{q,\mathrm{hard}}=o(W)\).

The exact changing-frame geometry needed for the first requirement
already exists. The dyadic XOR mosaic of
MATH_THEOREM_O_XOR_HASH_TRANSVERSE_MOSAIC_AND_Q4_HIERARCHY_OBSTRUCTION_20260726.md
has, when \(2m=2^\ell\), after transverse trimming relative to one
prescribed old quartet partition, and under its stated admissible
certified-factor and return-free-depth hypotheses,

\[
L=O(W/m)+e^{-\Omega(m)}W,
\tag{0.4}
\]

and every retained packet axis is cross-quartet. Hence every nontrivial
window is cross-quartet and

\[
B_\times=W-L.
\tag{0.5}
\]

It clears the geometric Hall toll with maximal slack and has no
\(H/r\) loss.

The remaining obstruction is not geometric visibility. Its deterministic
selector-array deployment is target-injective inside each XOR status
cell. Therefore a switch or commutator confined to one such cell has
nonpositive coherence. Positive physical coherence can arise only when
distinct full ordered cell tags are forgotten and coalesce on the same
literal target. Thus the surviving constant-one gate is an exact
**cross-cell** coupling, not another within-cell frame commutator.

The complete proved boundary is:

\[
\boxed{
\begin{array}{l}
\text{bounded pure commutators cannot remove the }H/r\text{ loss};\\
\text{closed pure frame-conjugation cycles cancel exactly};\\
\text{the all-transverse XOR mosaic already clears the geometric toll};\\
\text{only }\Theta(r/q)\text{ nonzero intrinsic first-order transports,}\\
\text{or an equivalent cross-cell physical coalescence, remain viable.}
\end{array}}
\tag{0.6}
\]

No coefficient-one conclusion is claimed.

## 1. Full ordered columns

Let \(P\cong Q_r\) be a physical packet carrying an exact isometric
\(C_{2r}\)-factor. At one fixed signed depth \(q<r\), let
\(\Omega(P)\) be its rooted starts. Thus

\[
|\Omega(P)|=|P|.
\tag{1.1}
\]

For a geodesic rooted window

\[
X_0,X_1,\ldots,X_q,
\tag{1.2}
\]

its full lower and upper ordered columns are

\[
\begin{aligned}
\mathfrak f_q^-
&=\left(
X_0,\,
X_0\cap X_1,\,
\ldots,\,
\bigcap_{i=0}^qX_i
\right),\\
\mathfrak f_q^+
&=\left(
X_0,\,
X_0\cup X_1,\,
\ldots,\,
\bigcup_{i=0}^qX_i
\right).
\end{aligned}
\tag{1.3}
\]

We append every packet, selector, status-cell, active-set, phase, frame,
and chronology label used by the construction. In an orientation cube,
the same information may be encoded by

\[
(\eta;(a_0,\varepsilon_0),\ldots,
       (a_{q-1},\varepsilon_{q-1})),
\tag{1.4}
\]

where \(\eta\) is the complete spectator orientation, the \(a_i\)'s are
the ordered physical swap axes, and \(\varepsilon_i\) records the
selected/removed endpoint when \(a_i\) is first used. Equivalently, one
may retain the complete source owner \(X_0\) and context explicitly.

Let \(\mathcal C_q^{\mathrm{ord}}\) be the resulting ordered-column set.
The terminal literal target is obtained by a projection

\[
\Pi_q:\mathcal C_q^{\mathrm{ord}}\longrightarrow
\binom{[2m]}{m\pm q}
\tag{1.5}
\]

which forgets chronology and auxiliary tags.

This distinction is essential. Ordered columns may be injective while
many of them project to one physical target.

## 2. Legal shore cubes and window locality

Suppose a legal exact-factor cube is indexed by

\[
x=(x_1,\ldots,x_s)\in\{0,1\}^s.
\tag{2.1}
\]

For a root \(\omega\in\Omega(P)\), let \(c_x(\omega)\) be its full ordered
column. Let

\[
I_q(\omega)\subseteq[s]
\tag{2.2}
\]

be the carrier switches physically encountered by its \(q\)-window.
When the encountered set varies with \(x\), \(I_q(\omega)\) means the
union over all shore options; equivalently it is any fixed dependency set
large enough that (2.3) can hold.

### Definition 2.1 (clean window locality)

The shore cube is clean at \(\omega\) if

\[
x|_{I_q(\omega)}=y|_{I_q(\omega)}
\quad\Longrightarrow\quad
c_x(\omega)=c_y(\omega).
\tag{2.3}
\]

Let \(E_{q,\mathrm{hol}}(P)\) count roots where (2.3) fails because of
exterior motion, an unclosed collar, phase holonomy, or another
nonlocal dependency.

Every fixed-exterior literal carrier cube satisfies (2.3). A construction
which does not satisfy it must charge the offending roots explicitly to
\(E_{q,\mathrm{hol}}\).

For \(x\in\{0,1\}^s\), put

\[
F(x)=\bigoplus_{\omega\in\Omega(P)}e_{c_x(\omega)}
\in
\bigoplus_{\omega\in\Omega(P)}
\ell_2(\mathcal C_q^{\mathrm{ord}}),
\tag{2.4}
\]

where the root coordinate is retained. Use normalized Boolean Fourier
coefficients

\[
\widehat F(S)
=2^{-s}\sum_{x\in\{0,1\}^s}
(-1)^{\sum_{i\in S}x_i}F(x).
\tag{2.5}
\]

## 3. Exact ordered-column Fourier locality

### Theorem 3.1 (multi-carrier intersection ceiling)

The Fourier coefficients satisfy

\[
\sum_{S\subseteq[s]}\|\widehat F(S)\|_2^2
=|\Omega(P)|.
\tag{3.1}
\]

If \(S\ne\varnothing\), then outside the holonomy-exceptional roots,

\[
\widehat F(S)|_\omega=0
\qquad\text{unless}\qquad
S\subseteq I_q(\omega).
\tag{3.2}
\]

Consequently

\[
\boxed{
\|\widehat F(S)\|_2^2
\le
\#\{\omega:S\subseteq I_q(\omega)\}
+E_{q,\mathrm{hol}}(P).}
\tag{3.3}
\]

Put

\[
\nu_i(P,q)=\#\{\omega:i\in I_q(\omega)\}.
\tag{3.3a}
\]

Without any synchronization assumption,

\[
\|\widehat F(S)\|_2^2
\le\min_{i\in S}\nu_i(P,q)+E_{q,\mathrm{hol}}(P).
\tag{3.3b}
\]

Suppose now that each \(i\in S\) is attached to one fixed named physical
direction, and that under the common root alignment its two antipodal
phase positions are the same in every shore option and synchronized
cycle. Then

\[
\boxed{
\|\widehat F(S)\|_2^2
\le {q\over r}|P|+E_{q,\mathrm{hol}}(P).}
\tag{3.4}
\]

The right side is independent of \(|S|\).

More generally, if switch \(i\) is attached to a fixed synchronized set
of \(t_i\) physical directions, then

\[
\|\widehat F(S)\|_2^2
\le |P|\min_{i\in S}\min\left\{1,{qt_i\over r}\right\}
+E_{q,\mathrm{hol}}(P).
\tag{3.4a}
\]

#### Proof

For every \(x\), the direct summands indexed by roots are orthogonal and
each contains one unit vector. Hence

\[
\|F(x)\|_2^2=|\Omega(P)|.
\]

Boolean Parseval gives (3.1).

Fix a clean root \(\omega\). If \(i\in S\setminus I_q(\omega)\), then
\(c_x(\omega)\) is independent of \(x_i\). In (2.5), pair every \(x\)
with \(x+e_i\). The two basis vectors agree and their signs are opposite,
so the \(\omega\)-summand cancels. This proves (3.2).

For a fixed root, Parseval bounds the squared norm of any one Fourier
coefficient by the total root energy \(1\). Summing over the permitted
roots and then adding the exceptional roots proves (3.3). Containment in
the roots counted by any one \(i\in S\) gives (3.3b).

Choose one \(i\in S\). On every isometric \(C_{2r}\), direction \(i\)
occurs twice at antipodal positions. Since \(q<r\), the two sets of rooted
length-\(q\) windows containing those occurrences are disjoint and have
size \(q\) each. Thus exactly \(2q\) of the \(2r\) cycle roots meet \(i\).
Summing over the \(|P|/(2r)\) cycles gives

\[
\#\{\omega:i\in I_q(\omega)\}
={q\over r}|P|.
\]

The set of roots meeting every member of \(S\) is contained in this set,
proving (3.4).

For (3.4a), use the union bound over the \(t_i\) directions affected by
one fixed \(i\in S\), cap by all packet roots, and minimize over \(i\).
\(\square\)

If other shore switches move the named direction to different phases,
the union of roots on which \(x_i\) matters can exceed
\((q/r)|P|\). In that case only (3.3b), with the actual \(\nu_i\), is
available.

### Proposition 3.2 (exact cyclic intersection count)

Assume the carrier directions in \(S\) have fixed first-lap positions
\(p_i\in\mathbb Z_r\) on all synchronized cycles. Put

\[
J_i=[p_i-q+1,p_i]\subseteq\mathbb Z_r.
\tag{3.5}
\]

Then the clean support count is exactly

\[
\#\{\omega:S\subseteq I_q(\omega)\}
={|P|\over r}\left|\bigcap_{i\in S}J_i\right|.
\tag{3.6}
\]

In particular it is zero when the positions in \(S\) do not lie in one
cyclic \(q\)-arc.

#### Proof

Modulo the two identical laps, every phase residue in \(\mathbb Z_r\)
occurs at exactly \(|P|/r\) packet roots. A root phase sees direction
\(p_i\) precisely when it belongs to \(J_i\). Intersect these conditions.
\(\square\)

### Corollary 3.3 (physical projection with bounded fibres)

Suppose every physical target in the support of \(\widehat F(S)\) has at
most \(\kappa_q\) relevant ordered-column preimages. Then

\[
\boxed{
\|\Pi_q\widehat F(S)\|_2^2
\le
\kappa_q\left(
{q\over r}|P|+E_{q,\mathrm{hol}}(P)
\right).}
\tag{3.7}
\]

#### Proof

The matrix of \(\Pi_q\) sends each ordered basis vector to one physical
target basis vector. Its squared operator norm on a set with maximum
fibre size \(\kappa_q\) is \(\kappa_q\). Apply (3.4). \(\square\)

Without a bound on \(\kappa_q\), (3.7) gives no physical no-go. Large
tag-forgetting fibres are precisely where positive physical coherence
may be created.

## 4. Pure commutators do not accumulate carrier visibility

For \(S\ne\varnothing\), call an endpoint comparison a **pure
\(S\)-interaction** if its two ordered columns agree at every clean root
whose window misses at least one carrier in \(S\).

Every Boolean Möbius commutator

\[
\partial_Sc(\omega)
=
\sum_{B\subseteq S}
(-1)^{|S|-|B|}e_{c_B(\omega)}
\tag{4.1}
\]

has this support property by the same pairing argument as Theorem 3.1.
However, (4.1) is a signed relation; it is not automatically a legal
two-endpoint exact-factor comparison. Global cancellation of proper
marginals alone also does not imply the pointwise agreement in the
definition. The endpoint theorem below assumes that agreement explicitly.

### Theorem 4.1 (pure-commutator support ceiling)

A pure \(S\)-interaction whose individual carriers are synchronized named
directions as in Theorem 3.1 can change the terminal physical target at no
more than

\[
\boxed{
{q\over r}|P|+E_{q,\mathrm{hol}}(P)}
\tag{4.2}
\]

rooted starts. Adding carriers to \(S\) never multiplies this bound.

For multi-direction frame generators, replace \(q/r\) by the minimum
factor in (3.4a). A generator moving \(\Theta(r)\) directions is not a
bounded carrier; its first-order visibility is already linear.

If their positions do not fit in one cyclic \(q\)-arc, the clean term is
zero.

#### Proof

The endpoint columns agree outside the support described in (3.2).
Projection to physical targets cannot enlarge the number of roots on
which they differ. The root-count argument in the proof of (3.4) gives
(4.2), and (3.6) gives the last statement.
\(\square\)

This is an intersection law. It should be contrasted with a diagonal
first-order bank. If \(D\) is a set of changed direction positions and
the gaps \(g_1,\ldots,g_{2|D|}\) are taken among both antipodal
occurrences on \(\mathbb Z_{2r}\), then the union fraction of roots seeing
at least one changed direction is

\[
\phi_q(D)
={1\over2r}\sum_i\min(g_i,q).
\tag{4.3}
\]

Equivalently, if \(g_1,\ldots,g_{|D|}\) are the cyclic first-lap gaps on
\(\mathbb Z_r\), then

\[
\phi_q(D)={1\over r}\sum_{i=1}^{|D|}\min(g_i,q).
\tag{4.3a}
\]

For \(|D|=\Theta(r/q)\) with dispersed positions, (4.3) is
\(\Theta(1)\). This is a sum of nonzero first-order modes, not one pure
commutator.

## 5. Hall-level obstruction

### Lemma 5.1 (one reassigned start repairs at most one hole)

Let \(f,g:\Omega\to\mathcal T\) be two target maps which differ on at
most \(N\) roots. Then

\[
\bigl||\operatorname{im}f|-|\operatorname{im}g|\bigr|\le N.
\tag{5.1}
\]

The same statement holds after restricting \(\mathcal T\) to any hard
profile window.

#### Proof

Change the images of the exceptional roots one at a time. Reassigning
one root deletes at most one formerly unique image and creates at most
one new image, so image size changes in absolute value by at most one.
\(\square\)

### Theorem 5.2 (bounded commutators cannot repair a Gaussian deficit)

Suppose a baseline exact or partial factor has at least

\[
(\delta_A-o(1))W
\tag{5.2}
\]

holes in one audited hard target-profile window. Apply pure commutator
comparisons made from synchronized one-direction carriers on packets with
total owner mass, counted with multiplicity,

\[
T=\sum_j|P_j|.
\tag{5.3}
\]

Let

\[
E_{\mathrm{hol}}=\sum_jE_{q,\mathrm{hol}}(P_j).
\tag{5.4}
\]

After also adding at most \(L\) omitted starts, the resulting factor still
has at least

\[
\boxed{
(\delta_A-o(1))W
-{q\over r}T
-E_{\mathrm{hol}}
-L}
\tag{5.5}
\]

holes in that window.

In particular, if each owner participates in at most \(c=O(1)\)
commutator rounds, then \(T\le cW\), and

\[
q/r\longrightarrow0,\qquad
E_{\mathrm{hol}}+L=o(W)
\tag{5.6}
\]

leave \((\delta_A-o(1))W\) holes.

#### Proof

Theorem 4.1 bounds the number of reassigned starts by
\((q/r)T+E_{\mathrm{hol}}\). Lemma 5.1 bounds the resulting increase of
hard-profile support by the same number. Each added omitted start covers
at most one further target. Subtract from (5.2). \(\square\)

Thus a bounded number of pure changing-frame commutators cannot repair
the Gaussian Hall deficit. One needs at least one of

\[
T=\Omega_A((r/q)W),\qquad
E_{\mathrm{hol}}=\Omega_A(W),\qquad
L=\Omega_A(W).
\tag{5.7}
\]

Under the stipulated requirement
\(E_{\mathrm{hol}}+L=o(W)\), only the first is a controlled escape within
the clean-locality argument. A separate exterior-moving construction
could instead use linear nonlocal mass, but would have to enlarge the
carrier/collar chart, decode those windows, and prove its full word-cost
ledger rather than leaving them in \(E_{\mathrm{hol}}\).

## 6. Exact coherence identity in ordered and physical target spaces

Let \(K\) range over independently switchable blocks. Let
\(a_K,b_K\) be their old and new target histograms in any chosen target
space and put

\[
\delta_K=b_K-a_K.
\tag{6.1}
\]

Define

\[
\begin{aligned}
C_0&=\sum_t\sum_{K<L}a_K(t)a_L(t),\\
C_1&=\sum_t\sum_{K<L}b_K(t)b_L(t),\\
C_{01}^{\mathrm{off}}
&=\sum_t\sum_{K<L}
\bigl(a_K(t)b_L(t)+b_K(t)a_L(t)\bigr).
\end{aligned}
\tag{6.2}
\]

### Theorem 6.1 (same-shore collision identity)

\[
\boxed{
\Gamma
=
\left\|\sum_K\delta_K\right\|_2^2
-\sum_K\|\delta_K\|_2^2
=2\left(C_0+C_1-C_{01}^{\mathrm{off}}\right).}
\tag{6.3}
\]

If each shore is globally injective in the full ordered-tag space, then

\[
C_0=C_1=0,
\qquad
\boxed{\Gamma_{\mathrm{ord}}\le0.}
\tag{6.4}
\]

For the finest occurrence-tag space used in (2.4), which retains both
the root and \(X_0\), distinct owner blocks are disjoint on opposite
shores as well. Then

\[
C_0=C_1=C_{01}^{\mathrm{off}}=0,
\qquad
\boxed{\Gamma_{\mathrm{root\text{-}ord}}=0.}
\tag{6.4a}
\]

#### Proof

Expand

\[
\Gamma=2\sum_{K<L}\langle b_K-a_K,b_L-a_L\rangle.
\]

The two same-shore terms are \(C_1,C_0\), and the two opposite-shore
terms sum to \(C_{01}^{\mathrm{off}}\), proving (6.3). Under shorewise
injectivity, two distinct blocks never have a common shore target, so
\(C_0=C_1=0\). The remaining term is nonnegative, proving (6.4).
If the root/source identity is retained, distinct blocks cannot share an
opposite-shore tag either, proving (6.4a).
\(\square\)

### Corollary 6.2 (bounded physical collision fibres)

Cancel old/new atoms which agree inside one block. Suppose \(n\) atoms
remain on each shore and every physical target has changed-shore load at
most \(\kappa\) on either shore. Then

\[
\boxed{\Gamma_{\mathrm{phys}}\le2(\kappa-1)n.}
\tag{6.5}
\]

#### Proof

For either shore, all unordered same-target atom pairs number at most

\[
\sum_t\binom{\mu_i(t)}2
\le {(\kappa-1)n\over2}.
\]

The cross-block count \(C_i\) is no larger. Drop the nonnegative
\(C_{01}^{\mathrm{off}}\) from (6.3) and sum the two shore bounds.
\(\square\)

Positive coherence is therefore impossible in the injective ordered
space. It is created only when forgetting tags coalesces distinct
same-shore columns more often than it creates opposite-shore
coalescences. The audited quartet \(C_4\) bank realizes exactly this
mechanism.

## 7. Frame cocycles and zero-monodromy cancellation

Let a frame group act on full ordered columns through a permutation
representation

\[
\rho:G\longrightarrow O(V).
\tag{7.1}
\]

For an ordered-column histogram \(\mu\), define the pure frame derivative

\[
D_g=(\rho(g)-I)\mu.
\tag{7.2}
\]

### Theorem 7.1 (frame-coboundary identities)

For all \(g,h\in G\),

\[
\boxed{D_{gh}=D_g+\rho(g)D_h.}
\tag{7.3}
\]

If \(C=[g,h]\), and \(G_0=\rho(g),H_0=\rho(h)\), then

\[
\boxed{
\rho(C)-I
=
\bigl((G_0-I)(H_0-I)-(H_0-I)(G_0-I)\bigr)
G_0^{-1}H_0^{-1}.}
\tag{7.4}
\]

In particular, disjoint literal carrier-frame changes commute and their
group commutator is exactly zero.

If \(\tau^d=I\), then every closed repetition of a pure frame derivative
cancels:

\[
\boxed{
\sum_{j=0}^{d-1}\rho(\tau)^jD_\tau
=
\bigl(\rho(\tau)^d-I\bigr)\mu
=0.}
\tag{7.5}
\]

#### Proof

Equation (7.3) follows from

\[
\rho(gh)-I
=\rho(g)(\rho(h)-I)+(\rho(g)-I).
\]

For (7.4), observe

\[
\begin{aligned}
&(G_0-I)(H_0-I)-(H_0-I)(G_0-I)\\
&\hspace{30mm}=G_0H_0-H_0G_0.
\end{aligned}
\]

Right multiplication by \(G_0^{-1}H_0^{-1}\) gives
\(\rho(C)-I\). Equation (7.5) is the telescoping identity

\[
(I+\rho(\tau)+\cdots+\rho(\tau)^{d-1})
(\rho(\tau)-I)
=\rho(\tau)^d-I.
\]

This proves every assertion. \(\square\)

Thus a carousel of relabelled copies of one pure frame coboundary cannot
accumulate a target derivative.

### Proposition 7.2 (intrinsic orbit-sum criterion)

Let \(\delta\in V\) be an intrinsic profile derivative, not assumed to be
a coboundary. If \(\tau^d=I\), put

\[
N_\tau\delta=\sum_{j=0}^{d-1}\rho(\tau)^j\delta.
\tag{7.6}
\]

Then

\[
\boxed{
N_\tau\delta
=d\,\Pi_{\operatorname{Fix}(\rho(\tau))}\delta.}
\tag{7.7}
\]

If the \(d\) stage derivatives are treated as independently selectable
blocks, their cross-stage coherence is

\[
\boxed{
\Gamma_{\mathrm{stage}}
=d^2\|\Pi_{\operatorname{Fix}(\rho(\tau))}\delta\|_2^2
-d\|\delta\|_2^2.}
\tag{7.8}
\]

Hence:

* a coboundary has orbit sum zero;
* if the \(d\) ordered translates are orthogonal, then
  \(\Gamma_{\mathrm{stage}}=0\);
* positive cross-stage coherence requires a sufficiently large invariant
  physical projection.

#### Proof

The cyclic averaging operator \(N_\tau/d\) is the orthogonal projection
onto the fixed subspace of the finite-order permutation \(\rho(\tau)\).
This proves (7.7). For the stage blocks,

\[
A=\|N_\tau\delta\|_2^2,\qquad
V=\sum_{j=0}^{d-1}\|\rho(\tau)^j\delta\|_2^2
=d\|\delta\|_2^2.
\]

Subtract to obtain (7.8). \(\square\)

After projection to the three occupancy-profile labels, the symmetric
\(U,V\) aggregate of the audited \(k=3\) quartet cross-profile derivative
is an intrinsic example: swapping \(U\) and \(V\) exchanges its negative
\((4,2)\) and \((2,4)\) profiles and permutes its positive \((3,3)\)
profiles, so that projected aggregate derivative is fixed rather than a
coboundary. Full literal ordered-column invariance would additionally
require equivariant choices of the \(K_{2,2}\) relation, cross matching,
carrier orientation, residual trace tags, and stage chart; it is not
claimed here. The profile calculation nevertheless shows that orbit
algebra alone does not forbid intrinsic transport.

## 8. Fixed-exterior twists cannot hide monodromy

Let \(J\) be a moving port set, \(P\subseteq J\), and \(\tau\) a
permutation of \(J\). Consider slab endpoints

\[
X_L=O_L\cup P,
\qquad
X_R=O_R\cup(J\setminus\tau P),
\tag{8.1}
\]

where the outside coordinates and \(J\) are disjoint and
\(|P|=|J|/2\). Assume also that
\(|O_L|=|O_R|\), so the two endpoints have equal rank. Put

\[
e=|O_L\setminus O_R|.
\tag{8.2}
\]

### Proposition 8.1 (geodesic exterior-motion identity)

If the slab is intended to have geodesic length \(|P|\), then

\[
\boxed{e=|P\setminus\tau P|.}
\tag{8.3}
\]

In particular, a fixed exterior has \(e=0\), and then

\[
\tau P=P.
\tag{8.4}
\]

#### Proof

The Johnson distance is

\[
\begin{aligned}
d_J(X_L,X_R)
&=|X_L\setminus X_R|\\
&=|O_L\setminus O_R|
  +|P\setminus(J\setminus\tau P)|\\
&=e+|P\cap\tau P|.
\end{aligned}
\]

Geodesic length \(|P|\) therefore requires

\[
e=|P|-|P\cap\tau P|
=|P\setminus\tau P|.
\]

If \(e=0\), equal cardinalities give \(\tau P=P\). \(\square\)

A later inverse twist or formal commutator cannot repair a slab which was
already nongeodesic. Every nontrivial serial frame conveyor must therefore
move the exterior by exactly the amount in (8.3) and audit the resulting
crossing collars. Any such crossing starts which are not explicitly
included in an enlarged local carrier/chart and proved covariant belong
to \(E_{q,\mathrm{hol}}\); fully decoded exterior motion is legal and is
not automatically exceptional.

## 9. Application to the exact dyadic XOR changing-frame mosaic

Assume

\[
[2m]=G=\mathbb F_2^\ell.
\tag{9.1}
\]

Fix one prescribed old quartet partition, an admissible certified factor
dimension \(r\) with \(r\log m=o(m)\), and
\(q\le H<r\) inside the factor's stated return-free trace range.

The following inputs are already proved in the cited XOR-mosaic theorem.

1. The owner-dependent hash frame partitions the middle layer exactly
   into equal-or-disjoint variable-dimensional orientation cubes.
2. After trimming and subdivision, every retained \(Q_r\)-packet axis
   crosses any prescribed old quartet decomposition, with leave (0.4).
3. If \(r\log m=o(m)\), the deterministic selector array deploys the
   complete active-set, affine-phase, and direction-order catalogue.
4. Separately at every protected depth and sign, all literal target
   occurrences emitted inside one selected XOR status cell are pairwise
   distinct.

The second item gives (0.5), so this construction already has
positive-density transverse chronology without any carrier-count loss.

The fourth item and Theorem 6.1 give a stronger within-cell conclusion.
For every comparison between two selector-array deployments which both
satisfy the cited target-injectivity conclusion and whose independently
switchable overlay blocks are genuinely legal and all lie in one selected
status cell,

\[
\boxed{\Gamma_{\mathrm{cell}}\le0.}
\tag{9.2}
\]

Indeed each shore is physically target-injective inside the cell, so
\(C_0=C_1=0\) even after forgetting chronology.

If the full status-cell label is retained, different cells are also
ordered-tag orthogonal. Thus positive coherence can occur only under the
physical projection which forgets that label:

\[
\bigoplus_{\text{cells}}\mathcal C_{q,\mathrm{cell}}^{\mathrm{ord}}
\longrightarrow
\binom{[2m]}{m\pm q}.
\tag{9.3}
\]

The unresolved terms are exactly cross-cell same-shore Gram products.
No commutator confined to one cell can create them.

This identifies the correct use of changing frames. They are already
needed, and already available, to destroy every fixed quartet invariant.
They do not themselves generate the negative floor covariance. That
covariance must be engineered between different owner cells after the
frame change.

## 9A. The naive all-carrier tensor has an exponential physical plateau

The commutator theorem does not rule out retaining many nonzero
first-order modes. We now test the most direct exact construction and
show why it is unusable.

Assume \(4\mid m\), put \(b=m/4\), and partition the ground coordinates
into labelled eight-blocks

\[
B_j=U_j\mathbin{\dot\cup}V_j,
\qquad |U_j|=|V_j|=4,
\qquad 1\le j\le b.
\tag{9A.1}
\]

Call a local subset **3-good** when it belongs to

\[
\mathcal U_3
=
\left(\binom{U_j}{3}\times\binom{V_j}{2}\right)
\mathbin{\dot\cup}
\left(\binom{U_j}{2}\times\binom{V_j}{3}\right).
\tag{9A.2}
\]

There are \(48\) such subsets among the \(256\) subsets of \(B_j\).
On \(\mathcal U_3\), use the audited twelve-\(C_4\) resolution between
the internal and cross perfect matchings.

Let \(r\) be an admissible power of two with

\[
r\le {3m\over128},
\qquad q\le r/2.
\tag{9A.3}
\]

For every middle owner having at least \(r\) 3-good blocks, select the
first \(r\). The selected list, its local sector, and its local
\(C_4\)-component are invariant under both matching shores.

### Lemma 9A.1 (exact owner packets and leave)

Products of the selected matching edges partition the good owners
exactly into physical \(Q_r\)-packets on either shore. The bad-owner leave
obeys

\[
\boxed{
L_3\le(2m+1)e^{-3m/512}W.}
\tag{9A.4}
\]

#### Proof

Under independent fair ground bits, the number of 3-good blocks is

\[
\operatorname{Bin}\left(b,{3\over16}\right)
\]

with mean \(3m/64\). Condition (9A.3) places \(r\) at most at half the
mean. The standard multiplicative Chernoff bound gives

\[
\Pr(N_3<r)\le
\Pr\left(N_3<{1\over2}\mathbb EN_3\right)
\le e^{-\mathbb EN_3/8}
=e^{-3m/512}.
\]

The middle layer has probability at least \((2m+1)^{-1}\) under fair
bits, so conditioning costs at most \(2m+1\), proving (9A.4).

On either shore, moving along a chosen matching edge stays in the same
3-good sector and the same alternating \(C_4\). Hence the first-\(r\)
rule is constant on every product packet. Products of the local matching
partitions are therefore disjoint and exhaustive on the good owners.
\(\square\)

Let

\[
F(X)=
\#\{U_j:U_j\subseteq X\}
+\#\{V_j:V_j\subseteq X\}
\tag{9A.5}
\]

be the number of full constituent quartets. It is constant on every
product packet, because a selected 3-good block has profile \((3,2)\) or
\((2,3)\).

Fix \(M>q\) and select a largest residue bank

\[
\mathcal B
=\{X:X\text{ is good and }F(X)\equiv a\pmod M\}.
\tag{9A.6}
\]

It is packet-closed and has mass

\[
\boxed{B_3:=|\mathcal B|\ge{W-L_3\over M}.}
\tag{9A.7}
\]

On \(\mathcal B\), compare the all-internal and all-cross products.
Install the same certified two-sided trace-injective
\(C_{2r}\)-factor in every abstract packet and synchronize abstract bits
with the local \(C_4\) checkerboards. On every good packet outside
\(\mathcal B\), install one identical common shore in both endpoints.

A switchable product trade block is indexed by the frozen exterior, the
first-\(r\) list, and an \(r\)-tuple of local \(C_4\)-components. It has
exactly

\[
4^r
\tag{9A.8}
\]

owners and is the union of \(2^r\) complete \(Q_r\)-packet factors on
each shore. Hence it is a literal exact trade with no seam or port.

At upper depth \(q\), let \(\mu_K^I,\mu_K^X\) be the internal and cross
physical target histograms of the product block \(K\), and put

\[
\delta_K=\mu_K^X-\mu_K^I,\quad
V_q=\sum_K\|\delta_K\|_2^2,\quad
A_q=\left\|\sum_K\delta_K\right\|_2^2,\quad
\Gamma_q=A_q-V_q.
\tag{9A.9}
\]

### Theorem 9A.2 (forced \(2^q\) physical subfibre)

\[
\boxed{
V_q=2B_3,\qquad
\Gamma_q\ge(2^q-1)B_3,\qquad
A_q\ge(2^q+1)B_3.}
\tag{9A.10}
\]

Moreover the internal endpoint already has factorial collision excess

\[
\boxed{
\sum_T\mu^I(T)\bigl(\mu^I(T)-1\bigr)
\ge(2^q-1)B_3.}
\tag{9A.11}
\]

#### Proof

Work first inside one product trade block \(K\). On either shore, an upper
target determines the \(q\) hit local blocks: they have local rank six,
whereas the unhit selected blocks retain rank five. In an internal hit
block, profiles \((4,2)\) and \((2,4)\) determine which internal local
edge was used. In a cross hit block, the two \((3,3)\) unions inside the
fixed local \(C_4\) are distinct. Every unhit local vertex is retained.
The certified trace injection then recovers the start. Thus each shore
map is injective inside \(K\).

The two shore images are physically disjoint. A cross hit has profile
\((3,3)\), so it creates no full constituent quartet and its target has

\[
F(T)\equiv a\pmod M.
\]

Every internal hit has profile \((4,2)\) or \((2,4)\) and creates exactly
one full quartet. Hence its target has

\[
F(T)\equiv a+q\pmod M.
\]

These residues differ because \(M>q\). Therefore

\[
\|\delta_K\|_2^2=2|K|,
\]

and summing gives \(V_q=2B_3\).

Now fix one internal target occurrence and let \(S\) be its \(q\) hit
axes. At each \(i\in S\), its local internal union is either
\(U_i\cup T_i\), shared by exactly the two local \(C_4\)-components with
that \(T_i\), or \(I_i\cup V_i\), shared by exactly the two components
with that \(I_i\). Let \(\rho_i\) be this unique partner involution.

For every \(J\subseteq S\), replace the component at \(i\) by
\(\rho_i\) precisely when \(i\in J\), leaving the exterior and synchronized
abstract trace fixed. The resulting \(2^q\) product trade blocks are
distinct, remain in the same first-\(r\) list and residue bank, and emit
the identical physical internal target. Thus every internal occurrence
has at least \(2^q-1\) same-target partners in other blocks.

Equation (9A.11) follows by counting these ordered partners. The residue
separation makes every cross/internal inner product zero, and all
remaining cross-block products are same-shore and nonnegative. Hence

\[
A_q\ge 2^qB_3+B_3=(2^q+1)B_3.
\]

Subtracting \(V_q=2B_3\) proves the coherence bound. \(\square\)

Taking \(M=H+1\) gives \(B_3\ge(W-L_3)/(H+1)\), but at \(q=H\) the
internal endpoint plateau is already

\[
\Omega\left({2^H\over H}W\right).
\tag{9A.12}
\]

Thus the apparent factor-\(r\) carrier accumulation is not useful
coherence. It is prepaid by an exponentially larger physical endpoint
collision term. Complementing every local eight-block gives the identical
lower-shadow statement from the all-\(k=2\) bank.

The same obstruction has an exact linear-algebra form.

### Proposition 9A.3 (affine changing-frame fibre rank)

Fix one ordered exterior/trace tag and a \(q\)-hit set \(S\). Encode the
two target-sharing partner components at each \(i\in S\) by
\(x_i\in\mathbb F_2\). Let a context-dependent shore schedule be affine:

\[
\sigma_i(x)=b_i+\sum_jA_{ij}x_j,
\tag{9A.13}
\]

where \(\sigma_i=0\) denotes the internal choice. With \(x_{S^c}\) fixed,
the component fibre over a prescribed all-internal target is empty or has
the exact size

\[
\boxed{
2^{\,q-\operatorname{rank}_{\mathbb F_2}A_{S,S}}.}
\tag{9A.14}
\]

For a coordinate-frame permutation

\[
\sigma_i(x)=x_{\tau(i)},
\tag{9A.15}
\]

this becomes

\[
\boxed{2^{|S\setminus\tau(S)|}.}
\tag{9A.16}
\]

#### Proof

The prescribed target conditions are exactly

\[
A_{S,S}x_S
=-b_S-A_{S,S^c}x_{S^c}.
\tag{9A.17}
\]

If consistent, rank-nullity gives (9A.14).

For a permutation matrix, row \(i\in S\) restricts to a nonzero row of
\(A_{S,S}\) exactly when \(\tau(i)\in S\). These nonzero rows have
distinct pivot columns, so

\[
\operatorname{rank}A_{S,S}
=|S\cap\tau^{-1}(S)|
=|S\cap\tau(S)|.
\]

Equation (9A.16) follows. \(\square\)

Forgetting ordered/exterior tags can only merge these fibres. Therefore
\(d\) missing affine ranks force a physical multiplicity \(2^d\). This
exactly classifies the fibre obstruction for affine and permutation
schedules built from the product \(C_4\) atlas; it does not by itself
exclude a schedule whose relevant submatrices have full rank. A
genuinely nonlinear multi-shore Latin primitive also lies outside the
formula.

## 10. Independent audit of the decisive step

The commutator ceiling was checked in three independent forms.

1. **Boolean cancellation.** Pairing \(x\) with \(x+e_i\) proves that a
   pure \(S\)-mode vanishes whenever one carrier in \(S\) is absent.
2. **Cyclic counting.** A named direction belongs to exactly
   \(q|P|/r\) rooted windows of an isometric packet.
3. **Group cocycle.** Closed pure frame derivatives telescope, and
   commuting disjoint frames have zero commutator.

These arguments use different structures and give the same conclusion:
one pure multi-carrier commutator has no \(|S|\) gain.

The coherence identity was also audited independently by direct
expansion:

\[
2\sum_{K<L}
\langle b_K-a_K,b_L-a_L\rangle
=2(C_0+C_1-C_{01}^{\mathrm{off}}).
\tag{10.1}
\]

The sign is decisive. In the finest root/source-tag space all three terms
vanish and coherence is exactly zero. In a coarser shore-injective ordered
space, the positive same-shore terms vanish and only the nonpositive
opposite-shore term remains.

The tensor obstruction has two independent checks. Rank-nullity gives
the affine fibre size (9A.14), while direct application of the commuting
local partner involutions gives \(2^q\) at the all-internal vertex. The
full-quartet residue separates internal and cross physical targets, so
this multiplicity is not an artefact of retaining auxiliary tags.

## 11. Exact surviving constant-one gate

The following are proved.

1. The proposed \(o(W)\) sum in (0.3) contradicts the Gaussian Hall
   inequality.
2. A bounded number of pure multi-carrier commutators repairs only
   \(O((q/r)W)+E_{\mathrm{hol}}\) hard-profile holes.
3. Closed cycles of pure frame conjugations have zero ordered-column
   orbit sum.
4. A fixed-exterior nonidentity twist is nongeodesic unless it fixes the
   port subset.
5. The legal XOR changing-frame mosaic already has all axes transverse
   and negligible leave.
6. Its within-cell target injectivity forces nonpositive within-cell
   coherence.
7. The naive tensor of first-order quartet carriers has physical target
   multiplicity at least \(2^q\) and an
   \(\Omega(2^qW/H)\) endpoint plateau when \(M=H+1\).
8. Every affine or permutation schedule on that tensor obeys the exact
   fibre-rank formula (9A.14); rank deficit \(d\) forces multiplicity
   \(2^d\).

What is not ruled out is a bank of

\[
s=\Theta(r/q)
\tag{11.1}
\]

dispersed **intrinsic**, non-coboundary cross-profile carriers. Its
first-order union can have \(\Theta(W)\) visibility by (4.3). Nor is a
cross-cell physical projection with large, favorably signed same-shore
coalescence ruled out. A nonlinear multi-shore Latin primitive also lies
outside the affine tensor obstruction.

The exact remaining theorem is therefore:

> On the XOR status-cell near-tiling, couple the cellwise selector arrays
> so that \(\Theta(r/q)\) dispersed intrinsic cross-profile marginals
> share one legal chronology, while their cross-cell physical Gram has
> the negative floor covariance required at every depth and sign.

This is strictly stronger than frame mixing, axis dispersion, or a
zero-monodromy commutator. It is the surviving nonabstract HCRT gate.
