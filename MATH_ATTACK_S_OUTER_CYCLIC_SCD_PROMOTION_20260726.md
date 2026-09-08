# Outer cyclic SCD promotion: exact quartet recursion and the full-carrier obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 \Omega_m=\binom{[2m]}m,
 \qquad W=|\Omega_m|=\binom{2m}m,
 \qquad N_q=\binom{2m}{m-q}.
\tag{0.1}
\]

For an SCD, let \(\mathcal A_q\subseteq\Omega_m\) be the middle owners
whose chains have radius at least \(q\), so \(|\mathcal A_q|=N_q\).
Write their ordered lower deletion and upper insertion labels as

\[
 \delta_1(X),\delta_2(X),\ldots,
 \qquad
 \eta_1(X),\eta_2(X),\ldots .
\tag{0.2}
\]

The promotion compatible with the first SCD diamond is forced:

\[
 G_1(X)=X-\delta_1(X)+\eta_1(X).
\tag{0.3}
\]

At higher depth put

\[
 G_q(X)=X-\{\delta_1,\ldots,\delta_q\}
          +\{\eta_1,\ldots,\eta_q\}.
\tag{0.4}
\]

The exact shift condition is

\[
 \boxed{G_1(G_tX)=G_{t+1}X,\qquad
        G_tX\in\mathcal A_{q-t}\quad(0\le t<q).}
\tag{0.5}
\]

There are three results.

1. The depth-one cycle criterion needs a correction. A permutation of all
   middle owners extending the forced promotion exists if and only if
   \(G_1:\mathcal A_1\to\Omega_m\) is injective; it need not map
   \(\mathcal A_1\) onto itself. Radius-zero owners may supply exactly
   \(W-N_1=W/(m+1)\) abstract reset transitions. More generally, if

   \[
      \Delta_1=N_1-|G_1(\mathcal A_1)|,
   \tag{0.6}
   \]

   the minimum number of nonforced transitions in an unrestricted
   permutation completion is

   \[
                         \boxed{W-N_1+\Delta_1.}
   \tag{0.7}
   \]

   This is only an abstract owner permutation; making its reset edges
   literal Johnson transitions is an additional Hall problem.
2. There is a positive exact four-child recursion. A round-robin rotor on
   four already coherent child systems is bijective, has trivial ordered
   holonomy, interleaves the child deletion/addition flags exactly, and
   preserves physical antipodal cycles. It constructs a genuine SCD/strip
   kernel on the balanced-center product sector.
3. That sector is asymptotically negligible, and the central quartet seed
   cannot be extended to the full middle layer by sparse seams. Fix
   disjoint quartets and let \(Z(S)\) be the number of full quartets minus
   the number of empty quartets. Every exact SCD has at least

   \[
   \boxed{
    E_m=\left\lceil
      {\lfloor m/2\rfloor(m-2)\over m(2m-1)}\,N_1
         \right\rceil
      =\left({1\over4}+o(1)\right)W}
   \tag{0.8}
   \]

   depth-one diamonds with nonzero \(Z\)-flux. Every pure central
   \(B_4\) rotation has zero flux. Therefore a construction which uses
   the central quartet rotor on \(W-o(W)\) owners cannot be corrected by
   \(o(W)\) reset, off-centre, or cross-quartet seams.

The natural alternating-child recursion also fails at every protected
depth. Exact SCD compatibility forces an average

\[
                         \left({1\over4}+o(1)\right)q
\tag{0.9}
\]

completed sibling-quartet pairs in a depth-\(q\) window, while the
sibling-separated Hamming recursion has none. At the first parent
\(B_8\) scale, already \(12\) of the \(28\) radius-two flags must break
the separated-quartet profile.

Thus the static product/quartet recursion is closed. The sole surviving
bounded-block escape is not a sparse seam atlas: it is a dense,
context-rotating, full-carrier recursion in which a positive density of
transitions use off-centre child profiles, cross-quartet moves, or changing
quartet frames. No such full owner-resolved recursion is proved here.

## 1. Forced promotion and the corrected reset theorem

For \(X\in\mathcal A_q\), let

\[
 D_q(X)=X-\{\delta_1(X),\ldots,\delta_q(X)\},
\qquad
 U_q(X)=X+\{\eta_1(X),\ldots,\eta_q(X)\}.
\tag{1.1}
\]

The two maps \(X\mapsto D_q(X)\) and \(X\mapsto U_q(X)\) are bijections
from \(\mathcal A_q\) to the two rank-\(m\mp q\) layers. The alternative
middle corner of the interval \([D_q(X),U_q(X)]\) is (0.4).

If a middle successor \(P(X)\) has

\[
 X\cap P(X)=D_1(X),\qquad X\cup P(X)=U_1(X),
\tag{1.2}
\]

then the two equations uniquely give \(P(X)=G_1(X)\). Thus the row map is
not an independent choice after the SCD has been fixed.

### Theorem 1.1 (correct depth-one permutation criterion)

There is a permutation \(P\) of \(\Omega_m\) satisfying

\[
                         P(X)=G_1(X)\qquad(X\in\mathcal A_1)
\tag{1.3}
\]

if and only if \(G_1:\mathcal A_1\to\Omega_m\) is injective. When it is
injective, every bijection

\[
 \Omega_m\setminus\mathcal A_1
       \longrightarrow
 \Omega_m\setminus G_1(\mathcal A_1)
\tag{1.4}
\]

completes it, using exactly

\[
                         W-N_1={W\over m+1}
\tag{1.5}
\]

nonforced radius-zero transitions.

#### Proof

A restriction of a permutation is injective, proving necessity. If
\(G_1\) is injective, its domain and image both have size \(N_1\), so the
two complements in (1.4) have equal size \(W-N_1\). Any bijection between
them, together with \(G_1\), is a permutation. \(\square\)

This corrects the stronger and unnecessary requirement
\(G_1(\mathcal A_1)=\mathcal A_1\). A monotone potential can eliminate
all cycles of the forced submap without precluding an \(o(W)\)-seam
permutation closure: the radius-zero owners can close long forced paths.

### Corollary 1.2 (exact unrestricted seam count)

Let

\[
 \Delta_1=N_1-|G_1(\mathcal A_1)|
          =\sum_Y\bigl(|G_1^{-1}(Y)|-1\bigr)_+.
\tag{1.6}
\]

If forced edges may be replaced arbitrarily, the minimum number of
nonforced transitions in a permutation of \(\Omega_m\) is

\[
                         W-N_1+\Delta_1.
\tag{1.7}
\]

#### Proof

At most one source can retain its forced edge over each image, so at most
\(|G_1(\mathcal A_1)|=N_1-\Delta_1\) forced edges survive. Retain one
preimage for each image. The remaining

\[
 W-(N_1-\Delta_1)=W-N_1+\Delta_1
\]

domains and codomains have equal size and may be bijected arbitrarily.
This attains the lower bound. \(\square\)

No Johnson adjacency or literal seam word is asserted in Corollary 1.2.
Those restrictions can only increase the minimum.

### Theorem 1.3 (higher flag cocycle)

Assume \(P\) extends (1.3). Its consecutive windows reproduce all SCD
flags through depth \(H\) if and only if, for every \(X\in\mathcal A_q\),
\(q\le H\), equation (0.5) holds. Equivalently,

\[
 \delta_j(G_tX)=\delta_{t+j}(X),qquad
 \eta_j(G_tX)=\eta_{t+j}(X)qquad(t+j\le q).
\tag{1.8}
\]

#### Proof

If the windows reproduce the flags, after \(t\) moves the middle owner is

\[
 X-\{\delta_1,\ldots,\delta_t\}
   +\{\eta_1,\ldots,\eta_t\}=G_t(X).
\]

Its next forced diamond move must be
\(\delta_{t+1}(X)\mapsto\eta_{t+1}(X)\), proving (0.5) and (1.8).
Conversely, (0.5) inductively identifies \(P^tX=G_tX\); comparing the
unique deleted and inserted coordinates at the next step proves (1.8).
The residual-radius clause ensures that every invoked SCD label exists.
\(\square\)

A cocycle failure at flag offset \(j\) can spoil all rooted windows which
reach it, up to \(H-j\) different roots. Therefore an unweighted count of
one-step failures is not a sufficient aggregate shadow ledger. A safe
sufficient quantity is the actual rooted-flag defect, or the weighted sum

\[
                         \sum_{j=1}^{H-1}(H-j)E_j,
\tag{1.9}
\]

where \(E_j\) counts failures of the \(j\)-th overlap.

### Lemma 1.4 (cycle-length monodromy)

If \(P^LX=X\) and the shift identities hold at \(X\) through depth \(L\),
then \(\rho(X)<L\).

#### Proof

If \(\rho(X)\ge L\), Theorem 1.3 gives

\[
 P^LX=G_L(X)
 =X-\{\delta_1,\ldots,\delta_L\}
    +\{\eta_1,\ldots,\eta_L\}.
\]

The deleted labels are distinct elements of \(X\), and the inserted labels
are distinct elements outside \(X\), so \(G_L(X)\ne X\), a contradiction.
\(\square\)

In particular, a bounded identity-monodromy quartet cycle cannot carry
growing-radius owners. A growing phase carrier is mandatory.

## 2. A positive four-child promotion recursion

The quartet cocycle itself is not inconsistent. The following construction
is an exact positive induction on a restricted product sector.

For \(i\in\mathbb Z_4\), let \(\Omega_i\) carry a permutation \(P_i\), a
phase map

\[
                         c_i:\Omega_i\to\mathbb Z_4,
 \qquad c_i(P_ix)=c_i(x)+1,
\tag{2.1}
\]

and coherent deletion/insertion flags. On
\(\Omega=\prod_{i\in\mathbb Z_4}\Omega_i\), put

\[
                         s(x)=\sum_i c_i(x_i)\pmod4
\tag{2.2}
\]

and define

\[
 R(x_0,x_1,x_2,x_3)
 =(x_0,\ldots,P_{s(x)}x_{s(x)},\ldots,x_3).
\tag{2.3}
\]

### Theorem 2.1 (round-robin quartet rotor)

The map \(R\) is a permutation,

\[
                         s(Rx)=s(x)+1,
 \qquad R^4=P_0\times P_1\times P_2\times P_3.
\tag{2.4}
\]

If the child flags satisfy the promotion cocycle, the parent flag obtained
by round-robin interleaving satisfies it as well. If all four child orbits
have lengths \(L_i\) divisible by four, every parent orbit has length

\[
                         4\operatorname {lcm}(L_0,L_1,L_2,L_3).
\tag{2.5}
\]

#### Proof

At the head \(y=Rx\), the advanced phase is \(s(y)=s(x)+1\). Hence the
active child of the predecessor is \(s(y)-1\), and applying its inverse
recovers \(x\); this proves bijectivity. Four successive moves use the four
children once in cyclic order, proving (2.4). Projecting the parent
deletion and insertion words to a child gives consecutive child words, so
every one-step tail identity is inherited. After \(4k\) moves every child
has advanced \(k\) times. The first return therefore has
\(k=\operatorname {lcm}(L_i)\), proving (2.5); a nonmultiple of four cannot
return because the phase sum changed. \(\square\)

If \(a_i=(i-s(x))\bmod4\in\{0,1,2,3\}\), the largest parent radius
certified directly by the child radii is

\[
                         \rho_R(x)=\min_i\bigl(4\rho_i(x_i)+a_i\bigr).
\tag{2.6}
\]

Indeed, the \((\rho_i+1)\)-st attempted use of child \(i\) occurs at
transition time \(a_i+4\rho_i\).

For parent depth \(q=4d+j\), \(0\le j<4\), the schedule uses \(d+1\)
steps in the \(j\) cyclically consecutive children beginning at \(s(x)\),
and \(d\) in the other children. The four target block ranks identify
these use counts and, when \(j>0\), the starting cyclic interval. If each
child signed shadow map is bijective on its eligible centers, the four
child targets recover all \(x_i\). Thus the parent shadow maps are
bijective onto these balanced-deficit product sectors. The resulting
chain segments form a genuine symmetric saturated-chain decomposition of
their union.

### Proposition 2.2 (physicality is preserved)

Suppose all child cycles have a common length \(L\equiv0\pmod4\), with
deletion word \(z^i_0,\ldots,z^i_{L-1}\), and the child insertion at phase
\(u\) equals \(z^i_{u+L/2}\). Then every parent orbit is a physical
\(C_{4L}\): its insertion at time \(t\) equals its deletion at time
\(t+2L\).

#### Proof

The parent deletion word is the round-robin interleaving of the four child
words and uses all \(4L\) child labels once. After \(2L\) parent moves the
same child is scheduled and has advanced \(L/2\) child phases. The child
antipodal identity gives the claimed parent identity. \(\square\)

### 2.1 Why this does not cover the outer middle layer

Take four disjoint Boolean child blocks of size \(2r\). The static balanced
sector, in which every child is at its middle rank, has

\[
                         \binom{2r}r^4
\tag{2.7}
\]

owners, whereas the full middle layer of their \(8r\)-coordinate product
has \(\binom{8r}{4r}\) owners. Stirling's formula gives

\[
 {\binom{2r}r^4\over\binom{8r}{4r}}
 =\left({2\over\pi^{3/2}}+o(1)\right)r^{-3/2}=o(1).
\tag{2.8}
\]

Starting only from the four active owners of the literal \(B_4\) seed and
iterating four-way gives, on \(n=4^{t+1}\) ground coordinates,

\[
                         M_t=4^{4^t}=2^{n/2}
\tag{2.9}
\]

owners, exponentially fewer than \(\binom n{n/2}=2^{n-o(n)}\).

Thus the local recursion, its holonomy, its cycles, and its shadows are all
exact. Its failure is owner coverage of the off-centre product-chain boxes.
Contextual first-eligible carriers repair middle-owner mass but lose the
global product-sector shadow bijection, returning to the outer matching
problem.

## 3. The quartet-flux invariant

Fix

\[
                         b=\lfloor m/2\rfloor
\tag{3.1}
\]

disjoint four-coordinate blocks \(B_1,\ldots,B_b\); ignore the at most two
unblocked coordinates. For any set \(S\subseteq[2m]\), define

\[
 Z(S)=\#\{i:B_i\subseteq S\}
      -\#\{i:B_i\cap S=\varnothing\}.
\tag{3.2}
\]

### Theorem 3.1 (exact SCD flux at every depth)

For every SCD and every \(q\le m\),

\[
 {1\over N_q}\sum_{X\in\mathcal A_q}
       \bigl(Z(U_q(X))-Z(D_q(X))\bigr)
 =\Delta_{m,q},
\tag{3.3}
\]

where

\[
 \boxed{
 \Delta_{m,q}
 ={2b\bigl((m+q)_{\underline4}-(m-q)_{\underline4}\bigr)
    \over(2m)_{\underline4}}.}
\tag{3.4}
\]

Uniformly for \(q=o(m)\),

\[
                         \Delta_{m,q}=\left({1\over2}+o(1)\right)q.
\tag{3.5}
\]

#### Proof

The SCD maps \(X\mapsto D_q(X)\) and \(X\mapsto U_q(X)\) biject
\(\mathcal A_q\) onto the rank-\(m-q\) and rank-\(m+q\) layers. For a
uniform \(k\)-set, a fixed quartet is full with probability
\((k)_{\underline4}/(2m)_{\underline4}\) and empty with probability
\((2m-k)_{\underline4}/(2m)_{\underline4}\). Summing over the \(b\)
quartets and subtracting the two complementary ranks proves (3.4).

The exact polynomial identity

\[
\begin{aligned}
 &(m+q)_{\underline4}-(m-q)_{\underline4}\\
 &\quad=2q\bigl(4m^3-18m^2+22m-6+(4m-6)q^2\bigr)
\end{aligned}
\tag{3.6}
\]

and \(b=m/2+O(1)\) give (3.5). \(\square\)

At depth one, each SCD owner \(X\in\mathcal A_1\) supplies a diamond

\[
                         D_1(X)\subset X,G_1(X)\subset U_1(X).
\tag{3.7}
\]

Adding the two coordinates of \(U_1\setminus D_1\) can increase \(Z\) by
at most two and can never decrease it. Hence every diamond has flux in
\(\{0,1,2\}\).

### Corollary 3.2 (positive-density noncentral transitions)

At least

\[
 \boxed{
 E_m=\left\lceil
 {b(m-2)\over m(2m-1)}N_1
 \right\rceil}
\tag{3.8}
\]

SCD diamonds have nonzero quartet flux. For even \(m\),

\[
 E_m=\left\lceil{(m-2)N_1\over2(2m-1)}\right\rceil
     =\left({1\over4}+o(1)\right)W.
\tag{3.9}
\]

#### Proof

At \(q=1\),

\[
 (m+1)_{\underline4}-(m-1)_{\underline4}
 =4(m-1)(m-2)(2m-3).
\]

Substitution in (3.4) gives total flux

\[
 N_1{2b(m-2)\over m(2m-1)}.
\]

Each nonzero diamond contributes at most two, proving (3.8)--(3.9).
\(\square\)

For the central quartet cycle

\[
                         14\to12\to23\to34\to14,
\tag{3.10}
\]

the lower local set has rank one and the upper local set has rank three.
Neither is empty or full, so every such transition has zero \(Z\)-flux.
Frozen quartets contribute equally to both endpoints. Corollary 3.2
therefore proves:

> A recursion using pure central \(B_4\) rotations on \(W-o(W)\) owners
> cannot be turned into an exact SCD promotion with only \(o(W)\) changed
> transitions. At least \((1/4-o(1))W\) transitions must be off-centre,
> cross-quartet, or evaluated in a changed quartet frame.

These transitions could be designed as legal promotion edges in a future
dense library. The theorem says they cannot be relegated to a sparse reset
atlas.

### Corollary 3.3 (completed-pair law)

Suppose a depth-\(q\) central-quartet window is geodesic. Let \(d_q(X)\)
be the number of quartets in which both local physical directions occur.
Then

\[
 Z(U_q(X))-Z(D_q(X))=2d_q(X).
\tag{3.11}
\]

If these windows reproduce an exact SCD's depth-\(q\) flags, then

\[
 {1\over N_q}\sum_{X\in\mathcal A_q}d_q(X)
 ={\Delta_{m,q}\over2}
 =\left({1\over4}+o(1)\right)q
 \qquad(q=o(m)).
\tag{3.12}
\]

#### Proof

An untouched quartet contributes equally to both shadows. A quartet with
one varied local direction has lower rank one and upper rank three, hence
zero \(Z\)-difference. A quartet with both directions varied has empty
lower shadow and full upper shadow, hence difference two. Sum over blocks
and use Theorem 3.1. \(\square\)

The alternating sibling-separated recursion has \(d_q(X)=0\) throughout
its protected range, contradicting (3.12). Its exact owner cycles and
intrapacket trace injectivity therefore do not promote to one SCD.

More robustly, suppose only \(B_q\) of the \(N_q\) active depth-\(q\)
windows are allowed to leave the sibling-separated central profile. A
general interval \(D_q(X)\subseteq U_q(X)\) adds \(2q\) coordinates, each
of which increases \(Z\) by at most one. Hence one exceptional window has
flux at most \(2q\), while every regular window has flux zero. Theorem 3.1
therefore forces

\[
 \boxed{
 B_q\ge {N_q\Delta_{m,q}\over2q}
       =\left({1\over4}+o(1)\right)N_q
       \qquad(q=o(m)).}
\tag{3.12a}
\]

Thus the required profile change is positive-density at every protected
depth; it cannot be concentrated into a vanishing collection of special
rooted windows.

### Corollary 3.4 (all fixed bounded central seeds)

Partition the coordinates into fixed even blocks of size \(s\ge4\), and
put \(Z_s=\#\text{full blocks}-\#\text{empty blocks}\). The mean
depth-one SCD flux is

\[
 {2(2m/s)\bigl((m+1)_{\underline s}-(m-1)_{\underline s}\bigr)
  \over(2m)_{\underline s}}
 =2^{3-s}+O_s(m^{-1}).
\tag{3.13}
\]

Every diamond has flux at most two. Hence at least

\[
                         \bigl(2^{2-s}+O_s(m^{-1})\bigr)N_1
\tag{3.14}
\]

transitions have nonzero block flux. A pure central-rank block rotor has
zero flux. Therefore every fixed bounded central seed needs a
positive-density noncentral library. The obstruction tends to zero only
when the physical seed size grows.

## 4. The first exact failed recursion cut

The flux law is already visible when two quartet seeds are combined. Put
\(m=4\), so the ground set has eight coordinates split into two quartets,
and take \(q=2\). There are

\[
                         N_2=\binom82=28
\tag{4.1}
\]

lower targets.

Among rank-two targets, exactly

\[
                         2\binom42=12
\tag{4.2}
\]

put both elements in one quartet; they have \(Z=-1\). The remaining
\(4\cdot4=16\) put one element in each quartet and have \(Z=0\). By
complementation the rank-six targets have \(16\) occurrences at \(Z=0\)
and \(12\) at \(Z=+1\).

Thus at least \(12\) paired depth-two occurrences must change their
\(Z\)-value between lower and upper sides. The alternating two-child
recursion uses one direction in each child, so every one of its windows
has \(Z(D_2)=Z(U_2)\). It supplies none of the required twelve. This is an
exact finite failed cut, not an asymptotic extrapolation.

There is also a direct fixed-priority obstruction. Suppose ordered
quartets are scanned and \(\delta_j\) is supplied by the \(j\)-th eligible
quartet. Let \(B_1\) be the first quartet and put

\[
                         C_m=\binom{2m-4}{m-2}.
\tag{4.3}
\]

At least \(4C_m-(W-N_1)\) positive-radius owners have their first deletion
in \(B_1\), while no forced second deletion uses \(B_1\).

### Theorem 4.1 (flag-pair Hall inequality)

Let

\[
 \lambda_j(X)=(\delta_j(X),\eta_j(X)),
\]

and project these literal pairs to arbitrary types \(z\). Put

\[
 F_j(z)=|\{X\in\mathcal A_j:\lambda_j(X)\text{ has type }z\}|.
\]

If a middle permutation has \(s_j\) failures of

\[
                         \lambda_j(PX)=\lambda_{j+1}(X)
 \qquad(X\in\mathcal A_{j+1}),
\tag{4.4}
\]

then

\[
 \boxed{
 s_j\ge N_{j+1}-\sum_z\min(F_{j+1}(z),F_j(z))
 ={\|F_{j+1}-F_j\|_1-(N_j-N_{j+1})\over2}.}
\tag{4.5}
\]

For every type set \(T\), also

\[
                         s_j\ge F_{j+1}(T)-F_j(T).
\tag{4.6}
\]

#### Proof

Every good source of type \(z\) must map injectively to a distinct head of
the same type. There are at most \(\min(F_{j+1}(z),F_j(z))\) such matches.
Sum over \(z\) and subtract from \(N_{j+1}\). The identity uses
\(\sum_zF_j(z)=N_j\). Restricting the count to a type set proves (4.6).
\(\square\)

Applying (4.6) to whether the deletion coordinate lies outside \(B_1\)
gives

\[
 \boxed{
 s_1\ge4C_m+N_2-W
       =\left({1\over4}-o(1)\right)W.}
\tag{4.7}
\]

Thus the static first-/\(j\)-eligible SCD recursion needs linearly many
depth-two reset seams even before orbit closure. In the completely
unchanged first-eligible packet map the failure is pointwise: rotating the
first eligible block leaves the eligible-index list fixed, so the head's
first child is still \(i_1\), whereas the source's second child is
\(i_2\ne i_1\).

## 5. Exact implication boundary

The following statements are proved.

* Promotion compatible with one SCD is forced by its opposite diamonds.
* Abstract all-owner cycles with only \(W/(m+1)=o(W)\) reset transitions
  exist whenever the forced depth-one map is injective. This statement
  does not make the resets physical.
* The four-child round-robin recursion is an exact promotion, flag, and
  physical-strip construction on balanced-center product sectors.
* One static balanced sector has density
  \(\Theta(m^{-3/2})\), and the literal iterated \(B_4\) seed has
  exponentially small owner density.
* Every exact SCD needs \((1/4+o(1))W\) nonzero-flux quartet diamonds.
  Hence a pure central quartet rotor plus \(o(W)\) seam replacements is
  impossible.
* Exact depth-\(q\) compatibility requires average completed-pair count
  \((1/4+o(1))q\); sibling-separated recursion fails this law.
* The natural fixed-priority scan has \(\Theta(W)\) depth-two cocycle
  failures.

The following remain unproved.

* A dense contextual resolver using the required positive-density
  off-centre/cross-quartet transitions may still exist.
* No theorem here produces a literal Johnson matching for the abstract
  radius-zero permutation completion in Theorem 1.1.
* No theorem here shows that an arbitrary non-product SCD must have
  \(\Delta_1=\Omega(W)\); the depth-one injective-diamond problem remains
  open outside the closed product families.
* The positive round-robin sector does not extend to all off-centre
  product-chain boxes with the Boolean radius census.

Therefore the requested full outer cyclic SCD has not been constructed.
The natural product/quartet induction is rigorously false, and the failure
is stronger than a cycle-count issue: sparse resets cannot supply the
mandatory quartet flux. Any surviving recursion must change its physical
carrier profile on a positive density of transitions and must then solve
the ordered flag cocycle and literal owner matching simultaneously.
