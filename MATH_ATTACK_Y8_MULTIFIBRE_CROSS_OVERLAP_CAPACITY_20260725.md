# Lane Y8: exact multi-fibre cross-overlap capacity and a support-closed restitution no-go

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
computer algebra, or numerical experiment is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

All genuine-wreath depth statements below assume
\(1\le H\le m-1\).  In the fixed-window application
\(H=\lceil A\sqrt m\rceil\), this holds for every fixed \(A>0\) and all
sufficiently large \(m=m(A)\).  The abstract construction in Sections
4--5 is likewise asserted for all sufficiently large \(m\).

This report does not prove \((\mathrm{SCC}_A)\), \((\mathrm{GCC}_A)\),
MWB, or the constant-one theorem.  It gives the exact theorem which a
positive multi-fibre exchange would have to prove, and a sharp no-go for
deriving that theorem from the audited restitution identities alone.

Let \(F\) be a literal exact middle-wreath factor and stack its complete
coordinate orbit

\[
\mathcal U(F)=\biguplus_{\sigma\in S_n}\sigma F.
\]

Write \(k=n!\).  An arbitrary positive reblocking of \(\mathcal U(F)\)
into exact factors is denoted

\[
\mathscr D=(F_1,\ldots,F_k).
\]

At depth \(q\), let \(X_q(\mathscr D)\) be the total lower-interval
overlap between row copies placed in different factor colours.  There is
an explicit histogram capacity \(X_q^{\max}\), depending only on
\((m,q,k)\), such that the exact identity

\[
\boxed{
\sum_{i=1}^k Q_q(F_i)
=2\bigl(X_q^{\max}-X_q(\mathscr D)\bigr)
}
\tag{Y8.1}
\]

holds for every positive exact reblocking.  Consequently every
multi-fibre exchange obeys

\[
\boxed{
\sum_i\mathcal Q_H(F_i)-
\sum_i\mathcal Q_H(F_i')
=2\sum_{q\le H}\frac{X_q(\mathscr D')-X_q(\mathscr D)}{c_q}.
}
\tag{Y8.2}
\]

There is no floor remainder, parity remainder, or active-pair remainder in
(Y8.2).  Cross-overlap with the other colours is the complete restitution
ledger.  Thus a positive orbit-stack proof is exactly a theorem that
almost saturates all the capacities simultaneously:

\[
\sum_{q\le H}\frac{X_q^{\max}-X_q(\mathscr D)}{c_q}
=o(kW).
\tag{Y8.3}
\]

Condition (Y8.3) is equivalent to the existence of one literal exact
factor with \(\mathcal Q_H=o(W)\).  It is not a weaker fractional or
stationary statement.  In particular, stationarity merely makes the mean
increment in (Y8.2) zero; it supplies no estimate of the distance to
capacity.

The obstruction is not just logical.  Using the independently audited
doubled-\(K_n\) exact-ownership construction, one obtains a finite
support-closed integral model with all of the following simultaneous
properties.

1. Every row owns exactly \(n\) middle symbols and \(n\) actual
   \((m-1)\)-set targets.
2. Every binary middle-exact factor on the row support is one vertex of a
   common-signing cube; there are no hidden supported factors.
3. The uniform row vector \(\tfrac12\mathbf1\) is an exact fractional
   middle factor and has a perfect depth-one \(\{1,2\}\) floor/ceiling
   target profile, with the exact point margins forced at that rank.
4. Nevertheless every positive integral factor on the support satisfies

   \[
   \mathcal C_1\ge2m^2J_*
   =\left(\frac14-o(1)\right)W,
   \]

   and, in the unhalved quadratic normalization,

   \[
   \boxed{
   Q_1\ge4m^2J_*
   =\left(\frac12-o(1)\right)W.}
   \tag{Y8.4}
   \]

5. These inequalities survive stacking any number of its exact factors,
   arbitrary positive row-preserving multi-fibre reblocking, and every
   stationary law on such reblockings.
6. Every constraint pair is exactly the audited scalar restitution normal
   form \(c=1,M=2,r_p=0\).  At a balanced-cut minimizer,
   \(\Gamma=\operatorname{Lock}=0\), while

   \[
   \operatorname{Sync}=I\ge2m^2J_*
   =\left(\frac14-o(1)\right)W.
   \tag{Y8.5}
   \]

The countermodel is literal, positive, integral, exact at the middle
layer, uses the actual depth-one target labels, and has the exact
coordinate point margins.  Its rows are not asserted to be cyclic
interval systems of genuine wreaths.  Therefore it is not a counterexample
to SCC/GCC.  It proves the narrower and decisive impossibility:

\[
\boxed{
\text{the restitution identities, perfect fractional balance, and
arbitrary positive multi-fibre recolouring do not by themselves imply
an }o(W)\text{ integral factor}.}
\tag{Y8.6}
\]

A successful proof must use a genuinely cyclic theorem which forces
near-saturation of (Y8.3), or otherwise rules out the support-closed signed
NAE holonomy exhibited below.

---

## 1. Exact orbit reservoir and floor energy

Let \(\Omega_m\) be the set of unoriented cyclic orders on \([n]\),
modulo rotation and reversal.  For a wreath \(R\in\Omega_m\), let
\(\mathcal I_q(R)\) be its \(n\) cyclic intervals of size \(m-q\).

An exact middle factor \(F\subseteq\Omega_m\) satisfies

\[
\sum_{R\in F}\mathbf1_{\mathcal I_0(R)}
=\mathbf1_{\binom{[n]}m}.
\tag{1.1}
\]

Every exact factor contains exactly \(B\) wreaths.  At depth \(q\), put

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\tag{1.2}
\]

where \(c_q=\lfloor\lambda_q\rfloor\) and
\(0\le\theta_q<1\).  For \(S\in\binom{[n]}{m-q}\), write

\[
\mu_q^F(S)=|\{R\in F:S\in\mathcal I_q(R)\}|.
\tag{1.3}
\]

The unhalved integer-floor energy is

\[
Q_q(F)=\sum_S
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1),
\tag{1.4}
\]

and

\[
\mathcal Q_H(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q}.
\tag{1.5}
\]

Every summand in (1.4) is nonnegative at integral loads and vanishes
exactly at \(c_q,c_q+1\).

The full indexed coordinate orbit has

\[
k=n!
\tag{1.6}
\]

factor colours.  Every uncoloured wreath occurs in it exactly \(2W\)
times, and at every lower target its aggregate load is

\[
T_q:=\sum_{i=1}^k\mu_q^{F_i}(S)
=k\lambda_q.
\tag{1.7}
\]

This is independent of both \(S\) and the exact reblocking.  Since it is
an actual aggregate incidence count, \(T_q\) is an integer.  Write

\[
T_q=kc_q+r_q,
\qquad
r_q=k\theta_q\in\{0,1,\ldots,k-1\}.
\tag{1.8}
\]

No divisibility hypothesis is hidden here.  Alternatively,
\(kW/N_q\in\mathbb Z\) follows directly from
\(n!/N_q=(m-q)!(m+q+1)!\).

---

## 2. The exact cross-overlap capacity identity

For two row copies \(R,D\), define their depth-\(q\) overlap

\[
h_q(R,D)=|\mathcal I_q(R)\cap\mathcal I_q(D)|.
\tag{2.1}
\]

Copies are retained as distinct even when their uncoloured wreath types
coincide.  For a reblocking
\(\mathscr D=(F_1,\ldots,F_k)\), define

\[
X_q(\mathscr D)
=\sum_{1\le i<j\le k}
\sum_{R\in F_i}\sum_{D\in F_j}h_q(R,D).
\tag{2.2}
\]

Equivalently,

\[
X_q(\mathscr D)
=\sum_S\sum_{i<j}
\mu_q^{F_i}(S)\mu_q^{F_j}(S).
\tag{2.3}
\]

For one lower target, define the unrestricted integer-histogram
cross-colour capacity

\[
x_q^{\max}
=\binom{T_q}{2}
-(k-r_q)\binom{c_q}{2}
-r_q\binom{c_q+1}{2},
\tag{2.4}
\]

and put

\[
X_q^{\max}=N_qx_q^{\max}.
\tag{2.5}
\]

The adjective “unrestricted” means that (2.4) optimizes only the colour
histogram at this one target.  It does not assert that all targetwise
capacities can be attained by one wreath reblocking.

### Theorem 2.1 — exact multi-fibre restitution

For every literal positive exact reblocking \(\mathscr D\) of the full
coordinate-orbit reservoir,

\[
\boxed{
\sum_{i=1}^kQ_q(F_i)
=2\bigl(X_q^{\max}-X_q(\mathscr D)\bigr)
}
\tag{2.6}
\]

at every depth \(q\).

#### Proof

Fix a target \(S\) and abbreviate

\[
t_i=\mu_q^{F_i}(S),\qquad
\sum_i t_i=T_q=kc_q+r_q.
\]

The number of same-colour unordered pairs of row occurrences at \(S\) is

\[
I_S=\sum_i\binom{t_i}{2}.
\tag{2.7}
\]

Among integer \(k\)-tuples of this fixed sum, convexity of
\(t\mapsto\binom t2\), or the elementary transfer

\[
\binom a2+\binom b2-
\binom{a-1}2-\binom{b+1}2=a-b-1>0
\]

when \(a\ge b+2\), shows that the minimum is attained exactly when
\(k-r_q\) entries equal \(c_q\) and \(r_q\) entries equal
\(c_q+1\).  Thus

\[
I_S^{\min}
=(k-r_q)\binom{c_q}{2}
+r_q\binom{c_q+1}{2}.
\tag{2.8}
\]

A direct expansion gives

\[
\sum_i(t_i-c_q)(t_i-c_q-1)
=2(I_S-I_S^{\min}).
\tag{2.9}
\]

All unordered pairs of occurrences at \(S\) number
\(\binom{T_q}{2}\).  Therefore its differently coloured pair count is
\(\binom{T_q}{2}-I_S\), while (2.4) is
\(\binom{T_q}{2}-I_S^{\min}\).  Equation (2.9) is consequently twice
the targetwise cross-capacity deficit.  Sum over \(S\) and use (2.3).
\(\square\)

### Corollary 2.2 — the whole exchange gain is cross-overlap gain

For two exact reblockings \(\mathscr D,\mathscr D'\) of the same orbit
reservoir,

\[
\boxed{
\sum_iQ_q(F_i)-\sum_iQ_q(F_i')
=2\bigl(X_q(\mathscr D')-X_q(\mathscr D)\bigr).
}
\tag{2.10}
\]

Hence (Y8.2) holds after weighting and summing over \(q\le H\).

The result permits a move to alter cross-overlaps with every untouched row
of every participating colour.  Those changes are not discarded; their
sum is exactly the right side of (2.10).  Thus the caveat left by
two-owner same-union rigidity is now an equality, not an unmeasured error
term.

### Corollary 2.3 — exact saturation criterion

For a sequence \(H=H(m)\), the following are equivalent:

1. some reblocking satisfies

   \[
   \frac1k\sum_i\mathcal Q_H(F_i)=o(W);
   \]

2. some reblocking satisfies

   \[
   \sum_{q\le H}\frac{X_q^{\max}-X_q(\mathscr D)}{c_q}
   =o(kW);
   \]

3. some literal exact middle-wreath factor \(G\) satisfies

   \[
   \mathcal Q_H(G)=o(W).
   \]

#### Proof

The equivalence of 1 and 2 is Theorem 2.1.  If 1 holds, at least one
nonnegative block energy is no larger than the average, proving 3.

Conversely, the full coordinate orbit of \(G\) has the same uncoloured
row-copy multiset as that of \(F\): every wreath has multiplicity \(2W\).
It is therefore an exact reblocking of \(\mathcal U(F)\), and every one
of its \(k\) blocks is a relabelling of \(G\), with the same energy.
This proves 1. \(\square\)

The corollary is an exact positive-integrality statement.  It also shows
why (Y8.3) cannot be obtained merely by naming a stronger exchange
library: near-saturation is already equivalent to the missing low-factor
theorem.

---

## 3. Stationary laws do not create capacity

Let a Markov chain have as states exact reblockings of one fixed orbit
reservoir and let every transition be a positive row-preserving
multi-fibre exchange.  No reversibility assumption is needed for the
following statement.

### Theorem 3.1 — stationary cross-overlap drift identity

If \(\pi\) is stationary and the chain makes one transition
\(\mathscr D\to\mathscr D'\), then

\[
\mathbb E_\pi
\left[
\sum_{q\le H}\frac{X_q(\mathscr D')-X_q(\mathscr D)}{c_q}
\right]=0,
\tag{3.1}
\]

and equivalently

\[
\mathbb E_\pi
\left[
\sum_i\mathcal Q_H(F_i')-
\sum_i\mathcal Q_H(F_i)
\right]=0.
\tag{3.2}
\]

#### Proof

Under stationarity, \(\mathscr D\) and \(\mathscr D'\) have the same
marginal law.  The expectations of every state function at the two times
are equal.  Apply this to the weighted cross overlap, or use (Y8.2).
\(\square\)

There is also a sharp optimization statement for arbitrary randomized
reblockings.  Choose a block index \(I\) uniformly from \([k]\),
conditionally independently of a random reblocking \(\mathscr D\).  Then

\[
\mathbb E\mathcal Q_H(F_I)
=\mathbb E\left[\frac1k\sum_i\mathcal Q_H(F_i)\right]
\ge\min_{G\text{ exact}}\mathcal Q_H(G).
\tag{3.3}
\]

Equality is attained by the deterministic reblocking consisting of the
full orbit of a minimizing factor.  Hence optimizing over all stationary
or nonstationary laws on positive reblockings has exactly the unknown
one-factor optimum as its floor.  Stationarity is useful only after an
independent theorem controls the capacity deficit.

---

## 4. A support-closed exact-middle countermodel

This section imports the independently audited construction in
`MATH_ATTACK_AA6_EXACT_OWNERSHIP_HOLE_HOLONOMY_NOGO_20260725.md`,
Section 4B, together with its two independent audits.  We make one harmless
modification which turns its fractional barycentre into a uniform row
vector and then prove a new arbitrary-multi-fibre closure statement.

Let

\[
N_1=\binom n{m-1}=\frac m{m+2}W,
\qquad
D=W-N_1=\frac{2W}{m+2}.
\tag{4.1}
\]

The actual depth-one target universe is

\[
\mathcal T=\binom{[n]}{m-1}.
\tag{4.2}
\]

The audited construction supplies a regular family
\(\mathcal U\subseteq\mathcal T\) of size \(D\), a family of disjoint
four-target rectangles avoiding \(\mathcal U\), and

\[
J_*=\min\left\{
\left\lfloor\frac B{2n}\right\rfloor,
\left\lfloor\frac{Q}{\binom n2}\right\rfloor
\right\},
\qquad
Q=\frac W4+O\left(\frac Wn\right).
\tag{4.3}
\]

In particular,

\[
J_*=\left(1+O(n^{-1})\right)\frac B{2n}.
\tag{4.4}
\]

There are \(J_*\) active blocks.  Each block has \(n\) ownership
components.  A component has two rows on each shore.  Its \(2n\) private
middle symbols are split into the four nonempty ownership cells of sizes

\[
\begin{pmatrix}m+1&m\\m&m+1\end{pmatrix}.
\tag{4.5}
\]

Thus its middle-ownership overlay is connected.  Different components use
disjoint middle symbols.

The source has \(B-2nJ_*\) common fixed rows.  Replace each such row by
two distinct formal twin rows, one on each shore, owning exactly the same
private \(n\) middle symbols and the same \(n\) neutral target labels.
This is a connected one-row-per-shore ownership component.  Every exact
factor chooses exactly one twin, and its target load is unaffected by that
choice.

Let \(\mathcal R_m\) be the resulting row universe.

### Theorem 4.1 — complete supported-factor classification

Every binary vector \(x\in\{0,1\}^{\mathcal R_m}\) which covers every
middle symbol exactly once is obtained by choosing one complete shore in
every ownership component.  Conversely every such shore signing is an
exact middle factor of exactly \(B\) rows.

#### Proof

For one middle symbol whose owners are a left row \(L\) and a right row
\(R\), exact coverage is the equation

\[
x_L+x_R=1.
\tag{4.6}
\]

Along a two-edge path in a connected bipartite ownership component, all
left variables agree and all right variables are their complements.
Connectivity of (4.5), and of every twin component, therefore leaves one
binary shore choice per component and no other binary solution.

Choosing one shore covers each component's private middle symbols once.
The active components contribute \(2nJ_*\) selected rows and the twin
components contribute \(B-2nJ_*\), for a total of \(B\). \(\square\)

### Corollary 4.2 — uniform fractional factor and exact quotas

The vector

\[
x^{\mathrm{frac}}=\frac12\mathbf1_{\mathcal R_m}
\tag{4.7}
\]

is an exact fractional middle factor.  Its depth-one target load is exactly

\[
b(S)=
\begin{cases}
2,&S\in\mathcal U,\\
1,&S\notin\mathcal U.
\end{cases}
\tag{4.8}
\]

Thus it is a perfect integral-valued floor/ceiling histogram of total mass
\(W\).  Moreover, every integral factor from Theorem 4.1 has exact point
margin

\[
\sum_{S\ni a}\mu_1(S)=(m-1)B
\qquad(a\in[n]).
\tag{4.9}
\]

#### Proof

Every middle symbol has exactly one owner on each shore, so (4.7) gives it
load one.  The target-load and point-margin claims are the audited
rectangle-cancellation and regular-upper-family identities.  Replacing a
fixed row by twins does not alter either identity because the twins have
identical target incidences. \(\square\)

### Theorem 4.3 — linear integral gap on every supported factor

Every exact factor supported on \(\mathcal R_m\) has at least

\[
h(F)\ge2m^2J_*
\tag{4.10}
\]

zero-load depth-one targets.  All target loads lie in \(\{0,1,2\}\), and
hence

\[
\boxed{
\mathcal C_1(F)=h(F)\ge2m^2J_*,
\qquad
Q_1(F)=2h(F)\ge4m^2J_*.
}
\tag{4.11}
\]

Consequently

\[
\mathcal C_1(F)\ge\left(\frac14-o(1)\right)W,
\qquad
Q_1(F)\ge\left(\frac12-o(1)\right)W.
\tag{4.12}
\]

#### Proof

Inside one active block, two target-pair gadgets are placed on every edge
of \(K_n\).  A gadget has loads \((1,1)\) when its two endpoint component
signs differ and \((2,0)\) or \((0,2)\) when they agree.  A two-colouring
of \(K_{2m+1}\) cuts at most \(m(m+1)\) of its
\(m(2m+1)\) edges.  It therefore has at least exactly \(m^2\)
monochromatic edges.  The two gadgets on every such edge give two holes,
so one block gives at least \(2m^2\) holes.  Sum over the \(J_*\) disjoint
blocks.

The audited neutral assignment makes every target load \(0,1\), or \(2\).
At \(c_1=1\), the corridor cost is one exactly at load zero and zero at
loads one and two.  The unhalved quadratic cost
\((t-1)(t-2)\) is two at zero and zero at one and two.  This proves
(4.11).  Equation (4.12) follows from (4.4), \(W=nB\), and
\(n=2m+1\). \(\square\)

### Theorem 4.4 — arbitrary multi-fibre closure

Take any positive integer \(L\), any \(L\) exact factors supported on
\(\mathcal R_m\), and retain all their row copies.  Repartition any or all
of these copies into \(L\) positive exact middle factors.  Then every
output block still satisfies (4.11).

The same conclusion holds for the stack of all supported exact factors,
for every finite sequence of positive row-preserving multi-fibre
exchanges, and for every probability or stationary law on the reachable
reblockings.

#### Proof

An exact output block cannot contain two copies of one row type, since
they share all of that row's middle symbols and would cover them twice.
After forgetting copy labels, the output is therefore a binary vector on
\(\mathcal R_m\) satisfying the exact middle equations.  Theorem 4.1
makes it one shore signing.  Theorem 4.3 applies to every such signing.

The statement is pointwise for every block, so it survives iteration,
arbitrary randomization, and passage to a stationary law. \(\square\)

This is stronger than a bad local minimum.  It says that the complete
positive factor fibre on the given row support has a linear gap.  No
larger component, nonlocal alternating circuit, correlated signing, or
multi-colour reblocking supported on those rows can escape it.

---

## 5. Exact restitution inside the countermodel

The countermodel realizes the scalar pair normal form used in the audited
restitution identities.

Fix one of the two gadgets on an edge \(uv\) of an active \(K_n\), and
write its target pair as \(p=\{x_p,y_p\}\).  Encode the selected shore of
component \(v\) by \(\varepsilon_v\in\{\pm1\}\).  After possibly reversing
the orientation of the target pair, its loads obey

\[
\mu(x_p)=1+\frac{\varepsilon_u+\varepsilon_v}{2},
\qquad
\mu(y_p)=1-\frac{\varepsilon_u+\varepsilon_v}{2}.
\tag{5.1}
\]

Thus

\[
M_p=2,
\qquad
D_p=\mu(x_p)-\mu(y_p)=\varepsilon_u+\varepsilon_v.
\tag{5.2}
\]

At depth one, \(c=1\), and therefore

\[
b_{1}(M_p)=(2-M_p)_+ +(M_p-4)_+=0.
\tag{5.3}
\]

The exact pair corridor is

\[
h_{1,2}(D_p)=\max\{0,|D_p|-1\}
=\mathbf1_{\{\varepsilon_u=\varepsilon_v\}}.
\tag{5.4}
\]

The two nonzero component coefficients have magnitude one.  Hence

\[
Z_p=1,
\qquad
r_p=\min_{\varepsilon}|\varepsilon_u+\varepsilon_v|=0,
\qquad
\operatorname{Lock}_p=0.
\tag{5.5}
\]

Choose in every active block a balanced \(m\)-versus-\(m+1\) bipartition
of the component signs.  It has exactly \(m^2\) monochromatic edges and
therefore attains the minimum \(2m^2\) gadget cost in that block.  Since
the blocks are disjoint, this is a global minimum of the complete signing
cube.  Consequently the best legal gain from this corner is

\[
\Gamma=0.
\tag{5.6}
\]

Every target pair is individually perfectible, so its independent ideal
cost is zero.  The ideal gain at the corner is exactly its current cost:

\[
I=2m^2J_*.
\tag{5.7}
\]

Substituting (5.5)--(5.7) into the exact restitution identity

\[
\Gamma=I-\operatorname{Lock}-\operatorname{Sync}
\]

gives

\[
\boxed{
\operatorname{Sync}=I=2m^2J_*
=\left(\frac14-o(1)\right)W.
}
\tag{5.8}
\]

The component--target incidence graph contains the doubled complete graphs
\(K_n\).  Every active incidence edge lies on a cycle when \(n\ge3\).
Thus replacing total synchronization support by cyclic support removes
nothing in this example.  The obstruction is genuine global holonomy, not
tree mass, coefficient overshoot, an immutable target, or a parity slice.

The model already permits every supported exact factor, not just the
corners reachable by one parity-preserving involution family.  Hence an
odd-involution enlargement or raw unbundling cannot improve it without
introducing rows outside the support.  Introducing such rows would be new
geometric information, exactly as the scope statement requires.

---

## 6. Capacity theorem boundary

### Proved

1. For the genuine coordinate-orbit reservoir, the weighted floor energy
   of every exact reblocking is exactly twice its all-depth cross-overlap
   capacity deficit, equations (Y8.1)--(Y8.2).
2. An average \(o(W)\) reblocking, an almost capacity-saturating
   reblocking, and one \(o(W)\)-energy exact factor are equivalent.
3. Every stationary positive reblocking law has zero mean cross-overlap
   drift; optimizing over such randomized laws does not lower the unknown
   one-factor minimum.
4. There is a literal positive integral exact-middle support with a
   uniform fractional factor, exact depth-one floor quotas, actual target
   labels, and exact point margins, but with a
   \((1/2-o(1))W\) unhalved quadratic gap in every supported factor.
5. This gap survives arbitrary stacking and arbitrary positive
   multi-fibre reblocking.
6. At a global supported minimum the complete scalar restitution identity
   has zero lock and linear synchronization.  All that synchronization is
   cycle-supported.

### Not proved

1. The abstract countermodel's rows are not proved to be cyclic interval
   systems of actual wreaths.
2. No actual wreath orbit reblocking satisfying (Y8.3) is constructed.
3. No upper bound on the genuine stationary whole-fibre mean is proved.
4. No cyclic theorem ruling out linear signed-NAE holonomy is proved.
5. SCC, GCC, MWB, labelled synchronization, and the constant-one theorem
   remain open.

The surviving positive statement is therefore exact and narrow:

> For genuine wreath rows, prove that some positive integral reblocking of
> the coordinate-orbit reservoir makes the weighted cross-colour lower
> overlap deficit in (Y8.3) equal to \(o(kW)\).  Any proof of this statement
> must use cyclic chronology beyond the audited restitution identities;
> and, once proved, it already contains a literal \(o(W)\)-energy exact
> factor.

---

## 7. Cross-audit of Z7

This section adversarially audits
MATH_ATTACK_Z7_RESTITUTION_GAP_PARITY_AND_CLIPPED_RESIDUES_20260725.md.
Only identities which survive this audit are used below.

### 7.1 Valid clipped and cyclic-restitution identities

The clipped locking theorem is exact.  For each conserved target pair,
the all-old signing and the one-dimensional greedy signing give

\[
r_p\le d_p,\qquad r_p\le Z_p,
\]

and hence

\[
\operatorname{Lock}_\sigma
\le\widehat{\operatorname{Frag}}_\sigma
=I_\sigma-\operatorname{Coh}_\sigma,
\]

\[
\Gamma_\sigma
\ge\operatorname{Coh}_\sigma-\operatorname{Sync}_\sigma.
\tag{Y8.20}
\]

There is no missing factor two.  The cyclic-support rounding is also
valid: after deleting bridges, hyperplane rounding is charged only on
nonbridge edges, and whole-component flips in the contracted bridge forest
satisfy every bridge without changing an internal edge.  Thus

\[
\operatorname{Sync}_\sigma
\le\operatorname{Fr}_\sigma
\le\sqrt{S_\sigma^\circ\delta_\sigma}.
\tag{Y8.21}
\]

For a wreath \(R\), a target
\(S\in\binom{[n]}{m-q}\), and \(1\le q\le m-1\), put

\[
a_{q,S}(R)
=|\{X\in\mathcal I_0(R):S\subseteq X\}|,
\]

\[
\rho_{q,S}(R)
=a_{q,S}(R)
-(q+1)\mathbf1_{\{S\in\mathcal I_q(R)\}}.
\tag{Y8.22}
\]

The complementary-run proof gives the sharp bound

\[
0\le\rho_{q,S}(R)\le q.
\tag{Y8.23}
\]

For an involution bundle \(K\), an oriented moved pair
\(p=\{S,\sigma S\}\), and shore size \(s_K\), the audited identity is

\[
\boxed{
(q+1)z_{pK}
=R_{K,q}(\sigma S)-R_{K,q}(S),
}
\tag{Y8.24}
\]

where \(R_{K,q}(S)=\sum_{R\in K^+}\rho_{q,S}(R)\).  Consequently,

\[
\boxed{
|z_{pK}|
\le\left\lfloor\frac{qs_K}{q+1}\right\rfloor.
}
\tag{Y8.25}
\]

The difference of the two spill sums is bounded by \(qs_K\), not
\(2qs_K\); divisibility by \(q+1\) gives (Y8.25).

### 7.2 Parity-slice scope

For even \(m\), cyclic-order sign is well-defined on unoriented wreaths:
every rotation of the odd cycle is even and every reflection has sign
\((-1)^m=1\).  An involution of type \(1\,2^m\) is even, so a complete
bundled shore replacement preserves the number \(N_-\) of negative rows.
The slice-minimum arguments in Z7 Theorems 6.1--6.4 are valid for that
move family.

The claimed
\(\operatorname{Cat}_{m-3}+1\) realized census values are valid, but the
proof needs the previously audited component-equivariance statement

\[
K^-=\tau K^+
\tag{Y8.26}
\]

for every canonical size-three \(\tau\)-component.  Oddness of \(\tau\)
and side size three would not suffice without (Y8.26).

The implication scope is narrower than “communicating-class obstruction”
may suggest.  Those census values are produced by toggling raw components
of one transposition overlay.  They therefore lie in one original
transposition-heat class.  The parity slices obstruct the bundled even-
\(1\,2^m\) descent family; they are not invariants of the original SCC
heat classes.

Parity is also linearly invisible to restitution.  If
\(\epsilon(R)\) is cyclic-order sign, the audited identities
\(B_r\epsilon=0\) give, target by target,

\[
\boxed{
\sum_R\epsilon(R)\rho_{q,S}(R)
=\sum_{X\supseteq S}(B_m\epsilon)(X)
-(q+1)(B_{m-q}\epsilon)(S)=0.
}
\tag{Y8.26a}
\]

This is a full-wreath-space linear cancellation.  It does not survive
restriction to one exact factor or grouping into ownership components,
and it does not cancel squared, absolute-value, or covariance
restitution.

### 7.3 Odd involution enlargement

For even \(m\), the class \(1^3\,2^{m-1}\) is odd.  Its bundled children
are positive integral exact factors.  The controlled-rank transitivity
proof is valid through \(r=m-1\), and the exact Johnson eigenvalues are

\[
\rho_{2a}=\frac{\binom ma}{\binom n{2a}},
\qquad
\rho_{2a+1}=\frac{2a+1}{m}\rho_{2a}.
\tag{Y8.27}
\]

Thus

\[
0\le\rho_j\le\frac1n
\quad(2\le j\le m-1),
\qquad
\rho_1=\frac1m.
\tag{Y8.28}
\]

Exact centered lower-load vectors have no degree-zero or degree-one part,
so (Y8.28) has the required spectral strength.  The full flip is
\(\sigma F\), and \(N_-(\sigma F)=B-N_-(F)\).

This does not improve SCC or GCC by itself.  Original heat classes are
already \(S_n\)-stable, so the full endpoint is already present and has
the same unlabelled energy.  Membership of proper partial
\(1^3\,2^{m-1}\)-bundle children in an original heat class is not proved.
For odd \(m\), “parity-unified” can refer only to choosing an odd move
class: cyclic-order parity itself is not well-defined on unoriented
wreaths.

\[
\boxed{\text{The clipped spill identities are valid, but parity supplies
no SCC invariant and oddness supplies no energy gain.}}
\tag{Y8.29}
\]

---

## 8. Exact all-depth restitution and positive two-fibre exchange

### Theorem 8.1 — total restitution is the centered load

Put

\[
\kappa_q=\binom{m+q+1}{q},
\qquad
R_q^F(S)=\sum_{R\in F}\rho_{q,S}(R).
\]

For every literal exact factor \(F\), every \(1\le q\le m-1\), and every
\(S\in\binom{[n]}{m-q}\),

\[
\boxed{
R_q^F(S)=\kappa_q-(q+1)\mu_q^F(S).
}
\tag{Y8.30}
\]

If

\[
\bar R_q=\kappa_q-(q+1)\lambda_q,
\qquad
\beta_q=N_q\theta_q(1-\theta_q),
\]

then

\[
\boxed{
Q_q(F)
=\frac{\|R_q^F-\bar R_q\mathbf1\|_2^2}{(q+1)^2}
-\beta_q.
}
\tag{Y8.31}
\]

#### Proof

Exactly \(\kappa_q\) middle \(m\)-sets contain \(S\).  The exact factor
owns each once.  Summing

\[
a_{q,S}(R)
=(q+1)\mathbf1_{\{S\in\mathcal I_q(R)\}}+\rho_{q,S}(R)
\]

over \(R\in F\) proves (Y8.30).  Subtracting the targetwise mean gives

\[
R_q^F-\bar R_q\mathbf1
=-(q+1)(\mu_q^F-\lambda_q\mathbf1).
\]

Since

\[
Q_q(F)
=\|\mu_q^F-\lambda_q\mathbf1\|_2^2-\beta_q,
\]

(Y8.31) follows.  This is an exact floor identity. \(\square\)

Let \(F,G\) be literal exact factors.  Cancel their common rows and let
\(K\) range over the connected components of their middle-ownership
overlay.  Write \(K^+\subset F\), \(K^-\subset G\), and

\[
\Delta_{K,q}
=\mu_q^{K^+}-\mu_q^{K^-}.
\]

For \(\varepsilon\in\{\pm1\}^{\mathcal K}\), let \(H_\varepsilon\)
choose \(K^+\) when \(\varepsilon_K=1\) and \(K^-\) otherwise, together
with the cancelled rows.  Every \(H_\varepsilon\) is a literal positive
integral exact factor, and \(H_{-\varepsilon}\) is its complementary
child.

### Theorem 8.2 — positive complementary two-fibre exchange

Put

\[
b_q=\frac{\mu_q^F+\mu_q^G}{2}-\lambda_q\mathbf1,
\qquad
D_{\varepsilon,q}=\sum_K\varepsilon_K\Delta_{K,q},
\]

\[
\|x\|_H^2=\sum_{q=1}^{H}\frac{\|x_q\|_2^2}{c_q},
\qquad
\mathfrak B_H=\sum_{q=1}^{H}\frac{\beta_q}{c_q}.
\]

Then

\[
\boxed{
\mathcal Q_H(H_\varepsilon)+\mathcal Q_H(H_{-\varepsilon})
=2\|b\|_H^2+\frac12\|D_\varepsilon\|_H^2-2\mathfrak B_H.
}
\tag{Y8.32}
\]

Consequently,

\[
\boxed{
\begin{aligned}
&\mathcal Q_H(F)+\mathcal Q_H(G)
-\mathcal Q_H(H_\varepsilon)
-\mathcal Q_H(H_{-\varepsilon})\\
&\hspace{2cm}
=\frac12\left(
\|\mu^F-\mu^G\|_H^2-\|D_\varepsilon\|_H^2
\right).
\end{aligned}}
\tag{Y8.33}
\]

Thus a signing with
\(\|D_\varepsilon\|_H<\|\mu^F-\mu^G\|_H\)
is a strict positive two-fibre exchange.

#### Proof

The complementary child loads are

\[
\mu_q^{H_{\pm\varepsilon}}
=\frac{\mu_q^F+\mu_q^G}{2}
\pm\frac12D_{\varepsilon,q}.
\]

Apply the exact norm form of \(Q_q\).  The mixed products cancel, proving
(Y8.32).  The original pair is the all-plus antipodal pair, for which
\(D_{\mathbf1,q}=\mu_q^F-\mu_q^G\).  Subtraction proves
(Y8.33). \(\square\)

### Theorem 8.3 — replication does not amplify one overlay

Fix \(r\ge1\).  Retain the row copies in \(rF+rG\), and reblock them
arbitrarily into \(2r\) positive exact factors, using no row type outside
\(F\cup G\).  The minimum possible mean energy is exactly

\[
\boxed{
\frac12\min_\varepsilon
\left(
\mathcal Q_H(H_\varepsilon)+
\mathcal Q_H(H_{-\varepsilon})
\right).
}
\tag{Y8.34}
\]

#### Proof

The restricted-support ownership theorem makes every exact output some
\(H_\varepsilon\).  If \(a_\varepsilon\) outputs have that type and

\[
\nu(\varepsilon)=\frac{a_\varepsilon}{2r},
\]

row-copy conservation on each component shore gives

\[
\mathbb E_\nu\varepsilon_K=0.
\tag{Y8.35}
\]

At the common midpoint, the only energy term odd in \(\varepsilon\) is

\[
\sum_{q\le H}\frac{\langle b_q,D_{\varepsilon,q}\rangle}{c_q},
\]

whose \(\nu\)-mean vanishes.  Therefore

\[
\mathbb E_\nu\mathcal Q_H(H_\varepsilon)
=\mathbb E_\nu
\frac{\mathcal Q_H(H_\varepsilon)+
\mathcal Q_H(H_{-\varepsilon})}{2},
\]

which is at least the right side of (Y8.34).  Repeating \(r\) copies of a
minimizing antipodal pair attains equality. \(\square\)

Thus arbitrarily many fibres, correlated signs, and vector balancing on
one two-support overlay cannot outperform its best ordinary complementary
signing.  This applies equally to an odd
\(1^3\,2^{m-1}\) involution overlay.

---

## 9. Conditional construction of a low stationary factor

The following theorem isolates the exact positive estimate which would
complete the construction.  It is not proved by Z7.

Fix \(A>0\), put

\[
H=H_A=\lceil A\sqrt m\rceil,
\]

and take \(m\ge m_0(A)\) sufficiently large that \(H\le m-1\).

For the parity of the move permutation only, use the odd conjugacy class

\[
\mathcal O_m=
\begin{cases}
1\,2^m,&m\text{ odd},\\
1^3\,2^{m-1},&m\text{ even}.
\end{cases}
\tag{Y8.36}
\]

For odd \(m\), the one-fixed class has

\[
\rho_{2a}=\frac{\binom ma}{\binom n{2a}},
\qquad
\rho_{2a+1}=0.
\tag{Y8.36a}
\]

Indeed, its fixed-subset polynomial is

\[
(1+x)(1+x^2)^m.
\]

The two-row Johnson character numerator is obtained from

\[
(1-x)(1+x)(1+x^2)^m
=(1-x^2)(1+x^2)^m.
\]

All odd coefficients vanish, and factorial simplification of the even
coefficient divided by
\(\binom n{2a}-\binom n{2a-1}\) gives (Y8.36a).  Moreover,

\[
\frac{\rho_{2a+2}}{\rho_{2a}}
=\frac{2a+1}{2m-2a+1}\le1,
\qquad
\rho_2=\frac1n.
\]

Together with (Y8.27), this gives
\(0\le\rho_j\le1/n\) on every exact-load degree \(j\ge2\) in both
parities.

For \(\sigma\in\mathcal O_m\), form its positive integral bundled
ownership cell.  Let

\[
A_\sigma(F)=\|f-\sigma f\|_H^2
\]

and let

\[
V_\sigma(F)=\sum_K\|\Delta_K\|_H^2
\]

be the sum of the squared lower-load effects of its complete bundles.
Uniform independent bundle signs give the exact identity

\[
\boxed{
\mathbb E\!\left[
\mathcal Q_H(F')\mid F,\sigma
\right]
=\mathcal Q_H(F)
+\frac{V_\sigma(F)-A_\sigma(F)}4.
}
\tag{Y8.37}
\]

The spectrum in (Y8.27)--(Y8.28), together with the absence of exact-load
degrees zero and one, gives

\[
\boxed{
\mathbb E_{\sigma\in\mathcal O_m}A_\sigma(F)
\ge
2\left(1-\frac1n\right)
\bigl(\mathcal Q_H(F)+\mathfrak B_H\bigr).
}
\tag{Y8.38}
\]

Define the **fair odd-bundle chain** by choosing
\(\sigma\) uniformly from \(\mathcal O_m\), freshly forming its complete
bundle cell at the current factor, and then choosing every complete-bundle
shore by an independent fair sign.  Every transition remains a literal
positive integral exact factor.

### Unproved odd-restitution gain \(\mathrm{ORG}_A\)

There exist constants \(0<\eta_A\le1\), \(C_A<\infty\), and \(m_0(A)\)
such that, for every \(m\ge m_0(A)\) and every literal exact factor \(F\),

\[
\boxed{
\mathbb E_{\sigma\in\mathcal O_m}
\bigl[V_\sigma(F)-A_\sigma(F)\bigr]
\le
-4\eta_A\mathcal Q_H(F)+4C_AHB.
}
\tag{ORG_A}
\]

### Theorem 9.1 — exact positive consequence of \(\mathrm{ORG}_A\)

If \(\mathrm{ORG}_A\) holds, the fair odd-bundle chain satisfies

\[
\boxed{
\mathbb E[\mathcal Q_H(F_{t+1})\mid F_t]
\le
(1-\eta_A)\mathcal Q_H(F_t)+C_AHB.
}
\tag{Y8.39}
\]

Every stationary class of this enlarged positive exact-factor chain then
has mean energy at most

\[
\boxed{
\frac{C_A}{\eta_A}HB=o(W).
}
\tag{Y8.40}
\]

Moreover, from every state with

\[
\mathcal Q_H(F)>\frac{2C_A}{\eta_A}HB,
\]

some literal cell child has gain at least
\(\eta_A\mathcal Q_H(F)/2\).  Best-child descent therefore constructs an
exact factor with

\[
\mathcal Q_H(F)\le\frac{2C_A}{\eta_A}HB=o(W)
\tag{Y8.41}
\]

after logarithmically many macrosteps.

#### Proof

Average (Y8.37) over \(\sigma\) and apply \(\mathrm{ORG}_A\) to obtain
(Y8.39).  Taking expectations in a stationary law and cancelling the
common mean gives (Y8.40).  The fair mean gain at a state is at least
\(\eta_A\mathcal Q_H(F)-C_AHB\), so one child attains at least that gain.
Above twice the threshold this is at least
\(\eta_A\mathcal Q_H(F)/2\), yielding geometric descent to (Y8.41).
Every visited state is a positive integral exact factor. \(\square\)

The audited Z7 inequalities do not prove \(\mathrm{ORG}_A\).  In a
one-bundle cell,

\[
V_\sigma=A_\sigma,
\]

and the only children are the equal-energy endpoints \(F,\sigma F\).
This geometry satisfies (Y8.25), all divisibility conditions, and
positivity.  What is missing is a theorem forcing positive cross-bundle
Gram mass when \(\mathcal Q_H\) is large:

\[
\mathbb E_\sigma
\sum_{\substack{K,L\\K\ne L}}
\langle\Delta_K,\Delta_L\rangle_H
\ge
4\eta_A\mathcal Q_H(F)-4C_AHB.
\tag{Y8.42}
\]

The double sum in (Y8.42) is ordered; its left side is exactly
\(\mathbb E_\sigma(A_\sigma-V_\sigma)\).  With the unordered convention
\(\sum_{K<L}\), both constants on the right side would be halved.

Equation (Y8.42) is one sufficient adaptive constant-one gate.  The exact
global orbit-reblocking criterion is the capacity saturation (Y8.3).
The latter need not imply the pointwise drift inequality (Y8.42).  Neither
statement is a parity assertion.

---

## 10. Final constant-one boundary

The report proves three unconditional positive integral theorems:

1. orbit-stack energy is exactly twice its multicolour cross-overlap
   capacity deficit;
2. every common signing satisfying the strict discrepancy inequality in
   Theorem 8.2 is a literal positive two-fibre energy-improving exchange;
3. arbitrary replication of one two-support overlay has no advantage over
   its best antipodal signing.

It also gives a complete conditional construction: \(\mathrm{ORG}_A\)
would produce both a stationary exact-factor law and an explicit adaptive
exact factor with energy \(O_A(HB)=o(W)\).

What is not proved is the estimate which makes that construction fire.
Neither clipped restitution, parity escape, odd endpoint spectrum,
replication, nor stationarity controls the cross-bundle Gram term in
(Y8.42).  Accordingly, this report does **not** claim an
\(o(W)\)-energy factor, SCC, GCC, MWB, or the constant-one theorem.

\[
\boxed{
\text{Prove either cyclic-wreath cross-bundle coherence, or directly
prove multicolour capacity saturation, at error }o(W).
}
\tag{Y8.43}
\]
