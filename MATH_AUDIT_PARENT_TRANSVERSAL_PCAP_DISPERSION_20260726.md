# Parent-transversal substitution: exact cap-tail and shadow dispersion laws

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let \(p=2m+1\), \(W=\binom{p}{m}\), and let

\[
 \mu_r^F:\binom{[p]}{m-r}\longrightarrow \mathbb Z_{\ge0}
\]

be the depth-\(r\) lower-shadow histogram of an exact middle wreath
factor \(F\). Put

\[
 K_r(F)=\sum_S(\mu_r^F(S)-p)_+,\qquad
 M_r(F)=|\{S:\mu_r^F(S)=0\}|,
\]

\[
 C_r=W-\binom{p}{m-r},\qquad
 \Phi_r(F)=(K_r(F)-C_r)_+ .
\]

Thus \(\Phi_r\) is the depth-\(r\) summand of
\(\operatorname {PCap}_H\).

Fix \(s=r+1\). A \(\mathcal D_s\)-transversal exact local factor on a
size-\(s\) parent hole is a legal context substitute: it fixes every
row's two parent boundary states and preserves the middle-state and
adjacent-union ownership multisets. It does not fix the depth-\(r\)
lower shadows. A single parent replacement can change only the
\(2r\) depth-\(r\) windows per rooted row which meet the open parent
slab. Since the packet has \(\operatorname {Cat}_s\) rooted rows, if

\[
 \Delta=\mu_r^{F'}-\mu_r^F,
\]

then

\[
 \boxed{\frac12\|\Delta\|_1\le 2r\operatorname {Cat}_{r+1}.}
 \tag{0.1}
\]

Write \(a=(-\Delta)_+\), \(c=(\Delta)_+\), and
\(\mu=\mu_r^F\). The exact overload update is

\[
\boxed{K_r(F')=K_r(F)-\mathscr D_{p,\mu}(\Delta),}
\tag{0.2}
\]

where

\[
\boxed{
 \mathscr D_{p,\mu}(\Delta)
 =\sum_S\min\{a(S),(\mu(S)-p)_+\}
  -\sum_S\bigl(c(S)-(p-\mu(S))_+\bigr)_+.}
\tag{0.3}
\]

The exact raw-hole update is

\[
\boxed{
\begin{aligned}
 M_r(F')-M_r(F)
 ={}&|\{S:\mu(S)>0,\ \Delta(S)=-\mu(S)\}|\\
 &-|\{S:\mu(S)=0,\ \Delta(S)>0\}|.
\end{aligned}}
\tag{0.4}
\]

Consequently

\[
 |K_r(F')-K_r(F)|,\ |M_r(F')-M_r(F)|
 \le 2r\operatorname {Cat}_{r+1}.                       \tag{0.5}
\]

If \(\mathscr D_{p,\mu}(\Delta)\ge0\), the exact improvement in the
PCap summand is

\[
\boxed{
 \Phi_r(F)-\Phi_r(F')
 =\min\{\mathscr D_{p,\mu}(\Delta),\Phi_r(F)\}.}
\tag{0.6}
\]

The replacement obeys more conservation than total mass. For every
coordinate \(x\),

\[
 \boxed{\sum_{S\ni x}\Delta(S)=0.}                       \tag{0.7}
\]

For the fixed parent-coordinate set \(J\), the portion of a changed
target outside \(J\) is fixed occurrence by occurrence. Hence for every
exterior carrier \(B\subseteq[p]\setminus J\),

\[
 \boxed{\sum_{S:S\setminus J=B}\Delta(S)=0.}             \tag{0.8}
\]

Thus dispersion of the distinguished child target is not enough. It must
be accompanied by collateral motion satisfying (0.7)--(0.8), and that
motion can restore every unit of cap tail and every hole which the child
arm appears to remove.

The exact library property is therefore full-collar weighted dispersion,
not injectivity of the rooted child-target map. The exact convexified
criterion is Theorem 6.1. It must be supplemented by an \(o(W)\)
convex-to-integral gap. At depth \(r=s-1\), a lower window can meet two
adjacent size-\(s\) parent slabs, so the required signature is in general
a joined two-factor signature.

## 1. Basic identities

Let

\[
 \mathcal V_r=\binom{[p]}{m-r},\qquad N_r=|\mathcal V_r|.
\]

Every exact middle factor has \(\operatorname {Cat}_m=W/p\) wreaths.
Every wreath has \(p\) rooted depth-\(r\) occurrences, so

\[
 \sum_{S\in\mathcal V_r}\mu_r^F(S)=W.                    \tag{1.1}
\]

The cap-tail identity

\[
 K_r(F)=W-\sum_S\min\{\mu_r^F(S),p\}                     \tag{1.2}
\]

shows that cap-tail descent is exactly capped-coverage gain.

For cap one,

\[
\begin{aligned}
 K_{1,r}(F)
 &:=\sum_S(\mu_r^F(S)-1)_+\\
 &=W-|\operatorname {supp}\mu_r^F|
   =W-N_r+M_r(F).
\end{aligned}                                             \tag{1.3}
\]

Thus raw holes are exactly cap-one excess above \(C_r=W-N_r\).

The phase-capacity statement is different. For every assignment of
coordinate-cycle phases to the rows of \(F\), its number \(H'_r\) of
missing depth-\(r\) targets satisfies

\[
 \boxed{H'_r\ge\Phi_r(F)=(K_r(F)-C_r)_+.}                \tag{1.4}
\]

Lowering \(\Phi_r\) lowers this universal obstruction. It does not by
itself upper-bound \(H'_r\), because cross-orbit collisions and legal
phase assignment remain separate.

## 2. Legality and what is held fixed

Put \(s=r+1\). Let \(J\) be the \(2s\) local coordinates of one aligned
size-\(s\) parent hole and let \(\infty\) be its separator coordinate.
The canonical boundary transversal is

\[
 \mathcal D_s\subseteq\binom Js,\qquad
 |\mathcal D_s|=\operatorname {Cat}_s.
\]

Let \(G\) be an exact \(C_{2s+1}\)-factor of
\(KG(J\cup\{\infty\},s)\), with exactly one member of
\(\mathcal D_s\) in every wreath. Root the wreath at its unique
\(P\in\mathcal D_s\). Its states avoiding \(\infty\) form a Johnson
geodesic

\[
 P=X_0^G(P),X_1^G(P),\ldots,X_s^G(P)=J\setminus P.       \tag{2.1}
\]

After ambient substitution, the following are fixed:

1. the rooted row indexed by \(P\);
2. its entrance and exit states \(P\) and \(J\setminus P\), with the
   common exterior coordinates adjoined;
3. every state outside the open parent slab;
4. the packet multiset of middle states inside the slab;
5. the packet multiset of adjacent-union colours inside the slab.

Items 4 and 5 hold because an exact local factor owns every core
\(s\)-set and every core \((s+1)\)-set exactly once. These are exactly
the two context-substitution ledgers, so the ambient result is again an
exact middle factor.

The order of intermediate states is not fixed. Hence every lower window
meeting an intermediate state may change.

The two intrinsic depth-\(r=s-1\) windows are

\[
 \lambda_G^-(P)=\bigcap_{t=0}^{s-1}X_t^G(P),\qquad
 \lambda_G^+(P)=\bigcap_{t=1}^{s}X_t^G(P).               \tag{2.2}
\]

Both are singletons. Along the geodesic, each coordinate of \(P\) is
deleted exactly once and each coordinate of \(J\setminus P\) is inserted
exactly once. Thus \(\lambda_G^-(P)\) is the last deleted coordinate and
\(\lambda_G^+(P)\) the first inserted coordinate.

## 3. The full \(2r\)-offset collar

Index the parent states by \(0,1,\ldots,s\); the open states are
\(1,\ldots,s-1=r\). A depth-\(r\) target is the intersection of
\(r+1\) consecutive middle states. A window starting at relative phase
\(t\) meets an open state precisely when

\[
                         1-r\le t\le r.                  \tag{3.1}
\]

There are \(2r\) such starts. The intrinsic starts are \(t=0,1\); the
other \(2r-2\) form the crossing collar.

For a rooted row \(P\) and such a start \(t\), let
\(T_G(P,t)\in\mathcal V_r\) be the ambient target. Its exterior carrier

\[
 B(P,t)=T_G(P,t)\setminus J                              \tag{3.2}
\]

is independent of \(G\), because all coordinates outside \(J\) are fixed
state by state.

Define the full collar histogram

\[
 h_G(S)=|\{(P,t):P\in\mathcal D_s,\ 1-r\le t\le r,\
                         T_G(P,t)=S\}|.                  \tag{3.3}
\]

If \(G_0\) is the old factor, the full ambient depth-\(r\) change is

\[
 \Delta=h_G-h_{G_0}.                                    \tag{3.4}
\]

Every other rooted window is unchanged.

### Theorem 3.1 (support, carrier, and point conservation)

For one parent replacement,

\[
 \sum_S\Delta(S)=0,\qquad
 \frac12\|\Delta\|_1\le2r\operatorname {Cat}_s,          \tag{3.5}
\]

and, for every exterior carrier \(B\),

\[
 \sum_{S:S\setminus J=B}\Delta(S)=0.                    \tag{3.6}
\]

For every ambient coordinate \(x\),

\[
 \sum_{S\ni x}\Delta(S)=0.                              \tag{3.7}
\]

#### Proof

Both collar histograms count the same
\(2r\operatorname {Cat}_s\) indexed windows. This proves (3.5).
For a fixed indexed window, its exterior carrier (3.2) is unchanged.
Grouping old and new occurrences by carrier proves (3.6).

Put \(k=m-r\). In a single cyclic wreath, exactly \(k\) of the \(p\)
cyclic \(k\)-intervals contain a prescribed coordinate \(x\). There are
\(W/p=\operatorname {Cat}_m\) wreaths, so every exact factor satisfies

\[
 \sum_{S\ni x}\mu_r^F(S)=k\operatorname {Cat}_m.         \tag{3.8}
\]

Subtracting (3.8) for the old and new exact factors proves (3.7).
\(\square\)

Every coordinate-additive weight

\[
 \alpha(S)=c+\sum_{x\in S}w_x                            \tag{3.9}
\]

therefore annihilates \(\Delta\). More strongly, every weight constant
on the carrier slices \(S\setminus J=B\) annihilates it.

## 4. Exact overload and hole changes

### Theorem 4.1 (one-replacement hinge identity)

Let \(\mu\in\mathbb Z_{\ge0}^{\mathcal V_r}\), let
\(\Delta\in\mathbb Z^{\mathcal V_r}\) satisfy
\(\mu+\Delta\ge0\) and \(\sum_S\Delta(S)=0\), and put
\(a=(-\Delta)_+\), \(c=(\Delta)_+\). Then

\[
\begin{aligned}
 K_p(\mu+\Delta)
 =K_p(\mu)
 &-\sum_S\min\{a(S),(\mu(S)-p)_+\}\\
 &+\sum_S\bigl(c(S)-(p-\mu(S))_+\bigr)_+.               \tag{4.1}
\end{aligned}
\]

Also

\[
\begin{aligned}
 M(\mu+\Delta)-M(\mu)
={}&|\{S:\mu(S)>0,\Delta(S)=-\mu(S)\}|\\
 &-|\{S:\mu(S)=0,\Delta(S)>0\}|.                        \tag{4.2}
\end{aligned}
\]

#### Proof

If \(\Delta(S)=-a(S)<0\), deleting \(a(S)\) units lowers the hinge by

\[
 (\mu(S)-p)_+-(\mu(S)-a(S)-p)_+
 =\min\{a(S),(\mu(S)-p)_+\}.                             \tag{4.3}
\]

If \(\Delta(S)=c(S)>0\), inserting \(c(S)\) units raises it by

\[
 (\mu(S)+c(S)-p)_+-(\mu(S)-p)_+
 =\bigl(c(S)-(p-\mu(S))_+\bigr)_+.                       \tag{4.4}
\]

Summation proves (4.1). An old nonhole becomes a hole exactly under the
first event in (4.2), and an old hole is filled exactly under the second.
\(\square\)

The useful removal term minus the collateral overflow term is exactly
\(\mathscr D_{p,\mu}(\Delta)\). Since

\[
 \sum_Sa(S)=\sum_Sc(S)=\frac12\|\Delta\|_1,              \tag{4.5}
\]

(0.5) follows.

### Corollary 4.2 (exact PCap update)

Put \(C=W-N_r\), \(K=K_p(\mu)\), and
\(D=\mathscr D_{p,\mu}(\Delta)\). Then

\[
 \boxed{\Phi_r(\mu+\Delta)=(K-D-C)_+.}                   \tag{4.6}
\]

If \(D\ge0\), then

\[
 \boxed{\Phi_r(\mu)-\Phi_r(\mu+\Delta)
 =\min\{D,\Phi_r(\mu)\}.}                                \tag{4.7}
\]

This follows from \(x_+-(x-D)_+=\min\{D,x_+\}\).

For a sequence of legal replacements, let \(\mu^{j-1}\) be the current
histogram and \(\Delta_j\) the actual next change. No additivity is needed
for

\[
\boxed{
 K_p(\mu^J)=K_p(\mu^0)
       -\sum_{j=1}^J\mathscr D_{p,\mu^{j-1}}(\Delta_j).}
\tag{4.8}
\]

Likewise

\[
\boxed{
 M(\mu^J)=M(\mu^0)
 -\sum_{j=1}^J(\operatorname {Hit}_j-\operatorname {Exhaust}_j),}
\tag{4.9}
\]

where

\[
\begin{aligned}
 \operatorname {Hit}_j
 &=|\{S:\mu^{j-1}(S)=0,\Delta_j(S)>0\}|,\\
 \operatorname {Exhaust}_j
 &=|\{S:\mu^{j-1}(S)>0,\
             \Delta_j(S)=-\mu^{j-1}(S)\}|.
\end{aligned}                                             \tag{4.10}
\]

Thus the exact state-adaptive requirements are

\[
 \sum_j\mathscr D_{p,\mu^{j-1}}(\Delta_j)
 \ge K_p(\mu^0)-C_r-o(W)                                 \tag{4.11}
\]

for \(\Phi_r=o(W)\), and

\[
 \sum_j(\operatorname {Hit}_j-\operatorname {Exhaust}_j)
 \ge M_r(\mu^0)-o(W)                                     \tag{4.12}
\]

for \(M_r=o(W)\).

## 5. Why child-target dispersion alone is false

For \(G\), define the intrinsic histograms

\[
 q_G^\pm(j)=|\{P\in\mathcal D_s:\lambda_G^\pm(P)=\{j\}\}|. \tag{5.1}
\]

For a specified canonical size-\(r\) child fibre
\(\mathcal F\subseteq\mathcal D_s\), put

\[
 q_{G,\mathcal F}^+(j)
 =|\{P\in\mathcal F:\lambda_G^+(P)=\{j\}\}|.             \tag{5.2}
\]

If this fibre has size \(d\), zero background, and is considered alone,
eliminating its cap-\(p\) excess requires

\[
 \max_jq_{G,\mathcal F}^+(j)\le p.                       \tag{5.3}
\]

Thus a fibre of size \(d\ge4p\) must occupy at least four local targets.
This is a genuine necessary test, but it is not sufficient for full
depth-\(r\) descent. The intrinsic offsets account for only
\(2\operatorname {Cat}_s\) of the
\(2r\operatorname {Cat}_s\) collar tokens.

A balanced four-cell example makes the failure exact. Choose local labels
\(\beta,\gamma\) and distinct \((m-r-1)\)-cores \(K,L\) avoiding them.
Put

\[
 A=K\cup\{\beta\},\quad B=K\cup\{\gamma\},\quad
 D=L\cup\{\gamma\},\quad C=L\cup\{\beta\},               \tag{5.4}
\]

\[
 \Delta=-e_A+e_B-e_D+e_C.                               \tag{5.5}
\]

This has zero total mass, zero point margins, and zero mass on each
carrier slice \(K,L\). Take

\[
 \mu(A)=p+1,\qquad\mu(B)=0,\qquad
 \mu(D)=1,\qquad\mu(C)=p.                               \tag{5.6}
\]

The marked arm \(A\to B\) alone lowers cap tail by one and fills the
displayed hole. The full balanced square gives

\[
 (p+1,0,1,p)\longmapsto(p,1,0,p+1),                     \tag{5.7}
\]

so both cap tail and hole count remain one. This is not asserted to be a
new factor circuit. It proves that marked-child dispersion plus all
universal conservation laws cannot imply descent; the actual full collar
must be computed.

There is also a sharp carrier-capacity necessity. For one parent and one
carrier \(B\), let \(\mathcal A_B\) be the union of targets reachable by
its collar tokens, let \(\beta\) be fixed background load, and let \(L_B\)
be the number of such tokens. Every library member satisfies

\[
 \boxed{
 \sum_{S\in\mathcal A_B}(\mu(S)-p)_+
 \ge\bigl(\beta(\mathcal A_B)+L_B-p|\mathcal A_B|\bigr)_+.}
                                                               \tag{5.8}
\]

Indeed all \(L_B\) tokens remain in \(\mathcal A_B\), and
\(\sum_i(x_i-p)_+\ge(\sum_ix_i-p|\mathcal A_B|)_+\).
Spare capacity must therefore occur in the same carrier slice.

## 6. Exact weighted dispersion condition

Let \(\mathscr C\) be phase-disjoint size-\(s\) parent contexts and
\(\mathcal L_s\) a library of \(\mathcal D_s\)-transversal exact local
factors. Assign \(g_C\in\mathcal L_s\) to every \(C\). Every assignment is
middle-exact by context substitution.

Let \(\mathscr A\) be the finite set of legal assignments and
\(\mu^a\) its full depth-\(r\) histogram. Define

\[
 \mathsf K_{p,r}^{\rm int}
 =\min_{a\in\mathscr A}K_p(\mu^a),                       \tag{6.1}
\]

\[
 \mathsf K_{p,r}^{\rm cvx}
 =\min_{\bar\mu\in\operatorname {conv}\{\mu^a:a\in\mathscr A\}}
       K_p(\bar\mu).                                     \tag{6.2}
\]

### Theorem 6.1 (full-collar weighted-cut dual)

\[
\boxed{
 \mathsf K_{p,r}^{\rm cvx}
 =\max_{0\le\alpha\le1}
   \left[
    \min_{a\in\mathscr A}\langle\alpha,\mu^a\rangle
       -p\sum_{S\in\mathcal V_r}\alpha(S)
   \right].}
\tag{6.3}
\]

Hence the exact fractional dispersion condition for removing the
depth-\(r\) PCap obstruction up to \(\varepsilon W\) is

\[
\boxed{
 \min_{a\in\mathscr A}\langle\alpha,\mu^a\rangle
 \le p\sum_S\alpha(S)+C_r+\varepsilon W
 \quad\text{for every }0\le\alpha\le1.}
\tag{6.4}
\]

The exact additional integral requirement is

\[
\boxed{
 \operatorname {IG}_{p,r}(\mathcal L_s)
 :=\mathsf K_{p,r}^{\rm int}-\mathsf K_{p,r}^{\rm cvx}
 =o(W).}
\tag{6.5}
\]

Under (6.4) with \(\varepsilon=o(1)\) and (6.5), some legal assignment
has \(\Phi_r=o(W)\).

#### Proof

For every real vector \(x\),

\[
 K_p(x)=\max_{0\le\alpha\le1}
             \langle\alpha,x-p\mathbf1\rangle.           \tag{6.6}
\]

The convex hull in (6.2) and the cube \(0\le\alpha\le1\) are compact and
convex, and the expression is bilinear. Minimax gives

\[
\begin{aligned}
 \mathsf K_{p,r}^{\rm cvx}
 &=\max_{0\le\alpha\le1}
   \min_{\bar\mu\in\operatorname {conv}\{\mu^a\}}
      \langle\alpha,\bar\mu-p\mathbf1\rangle\\
 &=\max_{0\le\alpha\le1}
   \left[\min_{a\in\mathscr A}\langle\alpha,\mu^a\rangle
       -p\sum_S\alpha(S)\right].
\end{aligned}
\]

This proves (6.3). Its value is at most \(C_r+\varepsilon W\) exactly
when (6.4) holds. Adding (6.5) gives
\(\mathsf K_{p,r}^{\rm int}\le C_r+o(W)\), equivalent to
\(\min_a\Phi_r(\mu^a)=o(W)\). \(\square\)

Condition (6.4) is the exact weighted dispersion property. Indicator
weights test ordinary target cuts, but general fractional weights are
necessary. The minimum is over one joint legal assignment; choosing the
best factor separately for each target is invalid.

The raw-hole analogue is Theorem 6.1 at cap one. By (1.3),

\[
 \boxed{\min_{a\in\mathscr A}M_r(\mu^a)
 =\mathsf K_{1,r}^{\rm int}-C_r.}                        \tag{6.7}
\]

### Separated parents

Call the selected parents \(r\)-separated if no depth-\(r\) window meets
open states from two selected slabs. Then there are nonnegative full
collar histograms \(h_{C,g}\) and a fixed background \(b\) such that

\[
 \mu^{\mathbf g}=b+\sum_{C\in\mathscr C}h_{C,g_C}.       \tag{6.8}
\]

The weighted minimum separates exactly:

\[
\boxed{
 \min_{\mathbf g}\langle\alpha,\mu^{\mathbf g}\rangle
 =\langle\alpha,b\rangle+
   \sum_C\min_{g\in\mathcal L_s}\langle\alpha,h_{C,g}\rangle.}
                                                               \tag{6.9}
\]

This is the simplest finite library test. The objects \(h_{C,g}\) are
the entire \(2r\)-offset collars, not the two maps (5.1).

### A sufficient rounding estimate

Let \(\nu\) be any distribution on legal assignments and put

\[
 \bar\mu=\mathbb E_\nu\mu^a,\qquad
 V(S)=\operatorname {Var}_\nu(\mu^a(S)).
\]

Then

\[
\boxed{
 \mathbb E_\nu K_p(\mu^a)
 \le K_p(\bar\mu)+\frac12\sum_S\sqrt{V(S)}.}
\tag{6.10}
\]

Indeed, write \(\mu^a(S)=\bar\mu(S)+Y_S\). Then

\[
 (\bar\mu(S)+Y_S-p)_+
 \le(\bar\mu(S)-p)_++(Y_S)_+,
\]

and, because \(\mathbb EY_S=0\),

\[
 \mathbb E(Y_S)_+=\frac12\mathbb E|Y_S|
 \le\frac12\sqrt{V(S)}.
\]

Thus \(\sum_S\sqrt{V(S)}=o(W)\) is a concrete sufficient rounding
condition. A margin-sensitive version is

\[
\begin{aligned}
 \mathbb E K_p(\mu^a)
 \le{}&\sum_S(\bar\mu(S)-p)_+\\
 &+\frac12\sum_{\bar\mu(S)>p/2}\sqrt{V(S)}
   +\frac1{2p}\sum_{\bar\mu(S)\le p/2}V(S),              \tag{6.11}
\end{aligned}
\]

using \((y-\gamma)_+\le y^2/(4\gamma)\).

For independent choices in the separated model (6.8), the exact expected
raw-hole count is

\[
\boxed{
 \mathbb E M_r
 =\sum_{S:b(S)=0}
    \prod_{C\in\mathscr C}
       \Pr(h_{C,g_C}(S)=0).}
\tag{6.12}
\]

Thus cap dispersion and hole coverage are distinct even in the additive
case.

## 7. Adjacent parents require joined two-factor profiles

Phase-disjoint substitution guarantees middle exactness but not lower
histogram additivity. A depth-\(r=s-1\) window crossing the boundary of
two consecutive size-\(s\) parent blocks can contain open states from
both, so its target depends jointly on the two factors.

### Lemma 7.1 (at most two parent phases)

A depth-\(r=s-1\) window meets open states from at most two pairwise
disjoint size-\(s\) parent slabs in one row.

#### Proof

The transition starts of distinct size-\(s\) slabs differ by at least
\(s\). The starts of a first and third differ by at least \(2s\). A
state interval of width \(s-1\) cannot meet both their open-state sets.
\(\square\)

Hence the depth-\(r\) occurrences partition into cells indexed by
subsets \(A\subseteq\mathscr C\) with \(|A|\le2\). There are nonnegative
joined histograms \(h_{A,\mathbf g_A}\) with

\[
 \boxed{
 \mu^{\mathbf g}(S)
 =b(S)+\sum_{A:1\le|A|\le2}h_{A,\mathbf g_A}(S).}        \tag{7.1}
\]

The weighted energy in Theorem 6.1 is therefore

\[
 \min_{\mathbf g}\left[
  \langle\alpha,b\rangle
  +\sum_{|A|=1}\langle\alpha,h_{A,g_A}\rangle
  +\sum_{|A|=2}\langle\alpha,h_{A,(g_C,g_D)}\rangle
 \right].                                                \tag{7.2}
\]

It is a pairwise spin optimization and need not split into one-context
minima. This is the exact coupling a local library theorem must control.

## 8. Proved and conditional boundary

The following are proved.

1. A \(\mathcal D_{r+1}\)-transversal local factor is a legal parent
   substitute, fixing rowwise boundaries and both middle ledgers.
2. Its full depth-\(r\) action lies in a
   \(2r\operatorname {Cat}_{r+1}\)-token collar and obeys (3.6)--(3.7).
3. Equations (4.1)--(4.7) give the exact overload and PCap update;
   (4.2) gives the exact raw-hole update.
4. The full-collar weighted-cut condition (6.4), with the integral
   condition (6.5), is necessary and sufficient for this library
   architecture to reach \(K_r\le C_r+o(W)\) at one fixed depth.
5. At the matched scale, adjacent substitutions create two-factor but no
   higher-order lower-shadow interactions.

What is not proved is existence of a useful library. In particular,
\(\mathcal D_{r+1}\)-transversality alone gives no quantitative
dispersion. It implies neither small child-map fibres, spare capacity at
their destinations, harmless collars, nor small joined-table rounding
loss.

The exact next statement is:

> For \(r=\Theta(\log p)\), construct a library of
> \(\mathcal D_{r+1}\)-transversal exact local factors whose full one- and
> two-parent collar tables satisfy (6.4) for every
> \(0\le\alpha\le1\), with total convex-to-integral loss \(o(W)\); or find
> a carrier weight \(\alpha\) for which the left side exceeds
> \(C_r+\Omega(W/r^{3/2})\).

The first alternative removes the depth-\(r\) PCap obstruction. A
separate phase-Hall theorem is still required to convert this into an
upper bound for missing shadows after row powers.

## 9. Cross-audit of the two companion parent reports

This section audits
\(MATH\_THEOREM\_PARENT\_TRANSVERSAL\_RESIDUAL\_CAPACITY\_20260726\)
and
\(MATH\_THEOREM\_PARENT\_TRANSVERSAL\_DISPERSION\_DUAL\_20260726\).

### 9.1 Statements which pass unchanged

The count

\[
                 2r\operatorname {Cat}_{r+1}             \tag{9.1}
\]

is exact as a count of potentially affected rooted slots.  The starts are
\(1-r,\ldots,r\), and they are distinct modulo \(p\) because \(2r<p\).

The residual-background decomposition also passes. Removing the old
collar histogram \(u_{G_0}\) gives a nonnegative background
\(\beta=\mu-u_{G_0}\), and every substitute has literal load
\(\beta+u_G\). Hence

\[
 K_p(\beta+u_G)
 =K_p(\beta)+\sum_S\bigl(u_G(S)-(p-\beta(S))_+\bigr)_+   \tag{9.2}
\]

and the displayed direct-hole identity in that report are exact.

The one-depth minimax dual passes. The multidepth identity also passes:
for \(c\ge0\),

\[
 (K_p(x)-c)_+
 =\max_{0\le\gamma\le1}
 \left(\langle\gamma,x-p\mathbf1\rangle
             -c\|\gamma\|_\infty\right).                \tag{9.3}
\]

Indeed write \(\gamma=\theta\alpha\), where
\(\theta\in[0,1]\), \(0\le\alpha\le1\), and minimize the admissible
\(\theta\) at fixed \(\gamma\), obtaining
\(\theta=\|\gamma\|_\infty\). The negative norm term is concave, so the
stated finite-dimensional minimax interchange is valid. Its common
\(\min_G\sum_q\langle\gamma_q,u_{C,G,q}\rangle\) correctly forces one
factor choice to serve all depths.

The rounding inequalities based on
\(\frac12\sum_{q,S}\sqrt{V_q(S)}\) and on the one-depth square mass
\(\Sigma_q=\sum_SV_q(S)\) also pass. For PCap it is enough to assume
\(K_p(\bar\mu_q)\le C_q+o(W)\); the stronger hypothesis
\(K_p(\bar\mu_q)=o(W)\) printed in one sufficient corollary is not
necessary, although it is not false as a sufficient condition.

### 9.2 Required correction to the parent-scale square estimate

The estimate

\[
 \Sigma_r\le L_r^{\max}\sum_Cw_C                         \tag{9.4}
\]

is valid only when \(C\) indexes independently rounded additive atoms and
\(L_r^{\max}\) is the maximum target multiplicity of one entire such
atom. It is valid in particular for an influence-disjoint atlas of
individual parents.

It is not justified for all phase-disjoint parents by defining
\(L_r^{\max}\) only for one parent. Adjacent parents have joined
depth-\(r\) windows. Grouping the overlap graph into connected components
restores additivity, but a component can contain many parents, and its
target multiplicity need not be bounded by the one-parent
\(L_r^{\max}=O(p)\). Pairwise local interactions can form a long connected
chain.

Therefore the conclusion

\[
 L_r^{\max}=O(p)\quad\Longrightarrow\quad
 \Sigma_r=O(pW/\sqrt r)                                  \tag{9.5}
\]

is proved only for an influence-disjoint atlas, or after separately
proving the same \(O(p)\) multiplicity bound for every whole joint atom.
The formal multidepth dual remains correct after giant-atom grouping, but
that grouping does not supply the local fragmentation needed for
rounding.

### 9.3 Sharp necessity for the distinguished child map

Let \(\mathcal F\subseteq\mathcal D_{r+1}\) be the distinguished
\(\mathcal D_r\) child fibre, \(d=|\mathcal F|=\operatorname {Cat}_r\),
and let

\[
 n_G(S)=|\{P\in\mathcal F:
       \text{the distinguished child target under }G\text{ is }S\}|.
                                                               \tag{9.6}
\]

Against the true residual capacities

\[
 c_\beta(S)=(p-\beta(S))_+,
\]

the full residual defect obeys the sharp necessary lower bound

\[
\boxed{
 E_\beta(G)\ge
 \sum_S(n_G(S)-c_\beta(S))_+
 =d-\sum_S\min\{n_G(S),c_\beta(S)\}.}
\tag{9.7}
\]

This follows simply from \(u_G\ge n_G\) coordinatewise and monotonicity
of the hinge. Thus any factor whose full residual defect is \(o(d)\)
must satisfy

\[
\boxed{
 \sum_S\min\{n_G(S),c_\beta(S)\}=d-o(d).}
\tag{9.8}
\]

This is the exact residual-capacity dispersion requirement on the
distinguished child map. In the most favourable zero-background case,
\(c_\beta(S)=p\), it becomes

\[
 \sum_S(n_G(S)-p)_+=o(d),\qquad
 |\operatorname {supp}n_G|
       \ge {d-o(d)\over p}.                              \tag{9.9}
\]

At the critical choice where \(r\) is minimal with
\(d=\operatorname {Cat}_r\ge4p\), one has \(4\le d/p<16\).
Consequently a useful factor must send almost all distinguished child
tokens into at least

\[
                         \left\lceil{d-o(d)\over p}\right\rceil
                                                               \tag{9.10}
\]

residually available targets in the same carrier slice. Four targets are
only the best-case lower bound; Catalan overshoot can require as many as
sixteen. Condition (9.8) is still merely necessary: the other
\((2r-1)d\)-scale collar population competes for the same capacities and
must satisfy the full weighted dual.
