# The parent-aligned `D_4` hereditary arm and its full collar tensor

Date: 2026-07-26

Method: pure mathematics only.  The explicit path and carrier tables in
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md` are used as exact input.
No search, solver, computation, or web input is used.

## 0. Verdict

The parent-aligned hereditary arm is exact.  It does not, by itself, prove
a hereditary PCap gain.

Cut the local cyclic coordinate word immediately before \(b_1\):

\[
 \widehat q=(b_1,b_2,b_3,b_4,9,a_1,a_2,a_3,a_4).       \tag{0.1}
\]

The first four entries are the exit port \([8]\setminus P\), the last
four are the entrance port \(P\), and \(9\) lies between them.  Thus
(0.1) is the port-compatible linearization of the complete local wreath,
not an artificial phase cut.

In a contiguous parent embedding, every protected target interval which
partially meets this block takes either a prefix or a suffix of length
\(1\le\ell\le8\).  For every fixed interface and \(\ell\), the exterior
part loses one far coordinate when the depth increases.  Consequently
all sixteen boundary profiles are literal hereditary one-deletion chains.

The marked left singleton profile is

\[
 \boxed{\Delta_{1,4}=-4e_2+4e_3-e_4-e_6+2e_7,}        \tag{0.2}
\]

with zero-based starts in the unrotated word
\((a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9)\).  It contains,
for example, the rowwise arms

\[
 P=1345:2\longrightarrow6,
 \qquad P=1256:4\longrightarrow7.                     \tag{0.3}
\]

Thus a single integral factor choice moves these marked occurrences at
every depth \(q=r,\ldots,Q\), with no cross-depth histogram cancellation.

But the legal atom includes fifteen companion profile chains.  Under the
row-common carrier hypothesis their total positive-mass budget is

\[
 \boxed{88\text{ per depth},}                          \tag{0.4}
\]

of which the marked profile (0.2) accounts for only six.  Complementary
interface profiles have the same sign after complementation; they do not
form an opposite cancelling arm.  Exact cancellation occurs only in the
different matched-parent specialization where all nine singleton starts
share one push-forward.

For the standard Catalan boundary preload, the two singleton interfaces
sit on opposite exterior carriers.  On the marked left carrier the clean
intrinsic cap gain is five or six units per depth (away from the single
threshold band); it does not suffer the previously conjectured
\(64/5\)-cutoff.  The opposite singleton and the longer profile chains,
however, remain simultaneous and have uncontrolled physical collision
loads.  Therefore

\[
 \boxed{
 \text{one switch has }\Theta(Q-r)\text{ raw hereditary movement, but
 an }\Omega(Q-r)\text{ PCap gain remains conditional.}}
\]

## 1. The exact parent-block itinerary

Let \(F\) be the canonical `D_4` factor and \(G\) the explicit
noncanonical factor.  For each port \(P\in D_4\), write

\[
 q_H(P)=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9),
 \qquad H\in\{F,G\}.                                  \tag{1.1}
\]

Rotate it as in (0.1), and embed that nine-symbol block contiguously in a
parent cyclic coordinate word.  Let \(R\) be the complementary exterior
arc.  At depth \(q\), a lower target is a cyclic interval of length

\[
                              L_q=m-q.                 \tag{1.2}
\]

Assume throughout the protected window that

\[
                         9\le L_q\le |R|.             \tag{1.2a}
\]

This holds in the intended regime \(Q=o(m)\).  The lower bound excludes
intervals lying properly inside the nine-slot block, and the upper bound
excludes intervals containing the whole exterior arc and both local
interfaces.

For \(1\le\ell\le8\), let

* \(K^-_{q,\ell}\) be the suffix of \(R\) of length \(L_q-\ell\),
  adjoining the left-prefix local segment; and
* \(K^+_{q,\ell}\) be the prefix of \(R\) of length \(L_q-\ell\),
  adjoining the right-suffix local segment.

For a set \(K\) disjoint from the local block, write

\[
                         K\star e_S=e_{K\cup S}.       \tag{1.3}
\]

### Theorem 1.1 (complete hereditary carrier formula)

Assume first that every row uses the same exterior word, the same affine
labelling, and hence the same two carrier sets \(K^\pm_{q,\ell}\).  Then,
for every protected depth,

\[
\boxed{
 D_q=\sum_{\ell=1}^{8}\left(
     K^-_{q,\ell}\star\Delta_{\ell,4}
    +K^+_{q,\ell}\star\Delta_{\ell,,4-\ell}
                            \right),}                  \tag{1.4}
\]

where starts are reduced modulo nine.  Moreover

\[
 K^\pm_{q+1,\ell}
   =K^\pm_{q,\ell}\setminus\{z^\pm_{q,\ell}\}        \tag{1.5}
\]

for the far endpoint \(z^\pm_{q,\ell}\) of the corresponding exterior
interval.  Hence every term in (1.4) is a hereditary one-deletion chain,
and terms belonging to different depths lie in different target ranks.

If the exterior carrier or injection depends on the local row, (1.4) must
be replaced by the row-resolved formula

\[
\begin{aligned}
D_q=\sum_{P\in D_4}\sum_{\ell=1}^{8}\bigl(&
 \Phi^-_{q,P,\ell}d_{P,\ell,4}
 +\Phi^+_{q,P,\ell}d_{P,\ell,,4-\ell}\bigr),         \tag{1.6}
\end{aligned}
\]

where

\[
 d_{P,\ell,j}
  =e_{I_{\ell,j}(q_G(P))}-e_{I_{\ell,j}(q_F(P))}.      \tag{1.7}
\]

#### Proof

A cyclic interval which changes must partially meet the nine-symbol local
block.  Its local intersection is therefore a nonempty proper prefix or
suffix.  For a prefix of length \(\ell\), the unrotated start is \(4\);
for a suffix it is \(4-\ell\) modulo nine.  This gives the sixteen terms
in (1.4).  Intervals disjoint from the block are unchanged, while an
interval containing all nine local symbols sees the same local set on the
two factor sides.

Increasing \(q\) shortens \(L_q\) by one and removes the far exterior
coordinate while retaining the same local prefix or suffix.  This proves
(1.5).  Summing the row atoms gives (1.4) exactly when their carrier maps
are common; without that hypothesis one must retain (1.6). \(\square\)

Thus the parent-atlas construction requirement is precise: it must realize
the port-linearized block (0.1) contiguously.  Port transversality by itself
does not assert that an arbitrary recursive embedding has this itinerary.

## 2. The marked row and all of its interface chains

For \(P=1345\), the rotated old and new blocks are

\[
\begin{aligned}
 \widehat q_F&=(2,8,6,7,9,1,4,5,3),\\
 \widehat q_G&=(6,2,7,8,9,3,1,4,5).
\end{aligned}                                         \tag{2.1}
\]

Their prefixes and suffixes are

\[
\begin{array}{c|c|c|c|c}
\ell&\text{left }F&\text{left }G&\text{right }F&\text{right }G\\ \hline
1&2&6&3&5\\
2&28&26&35&45\\
3&268&267&345&145\\
4&2678&2678&1345&1345\\
5&26789&26789&13459&13459\\
6&126789&236789&134579&134589\\
7&1246789&1236789&1345679&1345789\\
8&12456789&12346789&13456789&12345789.
\end{array}                                           \tag{2.2}
\]

Hence this one row has twelve nontrivial hereditary interface chains;
the four \(\ell=4,5\) chains are fixed by its two complementary ports
(with \(9\) adjoined at length five).  In particular the two singleton
arms are exactly

\[
 K^-_{q,1}\cup\{2\}\longrightarrow K^-_{q,1}\cup\{6\},
\qquad
 K^+_{q,1}\cup\{3\}\longrightarrow K^+_{q,1}\cup\{5\}. \tag{2.3}
\]

The row \(P=1256\) similarly contains

\[
 K^-_{q,1}\cup\{4\}\longrightarrow K^-_{q,1}\cup\{7\}. \tag{2.4}
\]

Equations (1.5), (2.3), and (2.4) prove literal simultaneous movement at
all \(Q-r+1\) depths.  They do not yet apply the cap hinge.

## 3. Full-factor collateral: exact mass and cancellation audit

For a signed profile \(v\) of total mass zero, put

\[
                         m(v)=\frac12\|v\|_1.          \tag{3.1}
\]

The carrier table gives the following positive masses for the two
interfaces in (1.4):

\[
\begin{array}{c|rrrrrrrr}
\ell&1&2&3&4&5&6&7&8\\ \hline
m(\Delta_{\ell,4})
  &6&7&8&0&0&7&9&7\\
m(\Delta_{\ell,4-\ell})
  &7&9&7&0&0&8&7&6\\ \hline
\text{sum}&13&16&15&0&0&15&16&13.
\end{array}                                           \tag{3.2}
\]

Therefore

\[
 \boxed{\sum_{\ell=1}^{8}left[
 m(\Delta_{\ell,4})+m(\Delta_{\ell,4-\ell})
 \right]=88.}                                         \tag{3.3}
\]

The marked \(b_1\) profile has mass six, so the remaining profiles have
triangle-inequality budget eighty-two per depth.  Without row-common
carriers, a safe raw bound is \(14\cdot12=168\) nontrivial row-interface
occurrences per depth.

### Proposition 3.1 (there is no tensor cancellation across the corridor)

The only universal cancellations relevant here are:

1. the selected aggregate profiles at \(\ell=4,5\), which vanish in
   (3.2);
2. the matched-parent identity
   \(\sum_{j=0}^{8}\Delta_{1,j}=0\), which requires all nine starts to
   have one common push-forward; and
3. exact coincidences discovered after applying the physical carrier maps
   in (1.6).

Complement pairing is not cancellation.  The tensor identity

\[
 \Delta_{9-\ell,j+\ell}([9]\setminus S)
                         =\Delta_{\ell,j}(S)            \tag{3.4}
\]

gives the same coefficient sign.  The paired prefix and suffix also have
different exterior carriers.  Finally, profiles at different depths live
in different rank universes, so they cannot cancel as histogram entries.

#### Proof

The first two statements are exact ownership identities from the carrier
table.  Equation (3.4) is its complement law.  Neither complementation nor
adjoining a different exterior set changes a positive coefficient into a
negative one at the same physical target.  Rank distinguishes different
depths. \(\square\)

Thus the literal first matched parent may cancel its complete singleton
profile, but that identity cannot be transported to the two-interface
itinerary (1.4) by summing local labels before their different carriers
are attached.

## 4. Source plateau, destinations, and exact singleton gain

At the marked \(b_1\) interface, the complete old and new fourteen-row
profiles are

\[
\begin{aligned}
 u_F^{b_1}&=5e_2+2e_4+2e_6+5e_8,\\
 u_G^{b_1}&=e_2+4e_3+e_4+e_6+2e_7+5e_8,
\end{aligned}                                         \tag{4.1}
\]

and hence

\[
 \boxed{u_G^{b_1}-u_F^{b_1}
   =-4e_2+4e_3-e_4-e_6+2e_7.}                         \tag{4.2}
\]

For a common exterior core, the source target with local label \(2\) is
drained by four units.  The marked row's nominal destination \(6\) is
also drained by one unit after all rows are included.  The actual receiving
targets are label \(3\), with four units, and label \(7\), with two.

Let

\[
 \phi(x)=(x-p)_+,qquad
 R_h(x)=\phi(x)-\phi(x-h),qquad
 A_h(x)=\phi(x+h)-\phi(x).                             \tag{4.3}
\]

If

\[
 \lambda_{q,x}=\mu_q(K^-_{q,1}\cup\{x\}),             \tag{4.4}
\]

then the exact old-minus-new cap-tail gain from (4.2) is

\[
\boxed{
 G_q^{b_1}
 =R_4(\lambda_{q,2})+R_1(\lambda_{q,4})
  +R_1(\lambda_{q,6})
  -A_4(\lambda_{q,3})-A_2(\lambda_{q,7}).}            \tag{4.5}
\]

In particular \(-6\le G_q^{b_1}\le6\).  It equals six under the robust
separation conditions

\[
\begin{aligned}
&\lambda_{q,2}\ge p+4,quad
 \lambda_{q,4}\ge p+1,quad
 \lambda_{q,6}\ge p+1,\\
&\lambda_{q,3}\le p-4,quad
 \lambda_{q,7}\le p-2.
\end{aligned}                                         \tag{4.6}
\]

### Retracted calculation 4.1 (carrier-conflated intrinsic preloads)

**Retracted.**  The calculation through (4.12) below identifies the
left suffix carrier \(K^-_{q,1}\) with the right prefix carrier
\(K^+_{q,1}\).  They are physically distinct in the hereditary corridor,
so the displayed \(1,2,0\) gain is not valid there.  Proposition 4.2
immediately below gives the corrected authoritative preload.

In the standard first-four-boundary embedding of a size-\(r\) Catalan
plateau, the intrinsic loads on coordinate pairs \(\{1,2\},\{3,4\},
\{5,6\},\{7,8\}\) are, at every transparent ancestor depth,

\[
 d_0=\operatorname {Cat}_r,qquad
 d_1=\operatorname {Cat}_{r-1},qquad
 d_2=2\operatorname {Cat}_{r-2},qquad
 d_3=5\operatorname {Cat}_{r-3}.                      \tag{4.7}
\]

#### Proof

The first-return class at boundary pair \(j\) has multiplicity

\[
 w_j=\operatorname {Cat}_{j-1}operatorname {Cat}_{r+1-j}.
\tag{4.8}
\]

Substituting \(j=1,2,3,4\) gives (4.7).  Adjoining one common exterior
core changes the physical label but not its multiplicity. \(\square\)

Put

\[
 \theta={\operatorname {Cat}_r\over p},                \tag{4.9}
\]

and define the exact thresholds

\[
\begin{aligned}
 \theta_2(r)
 &=\frac{\operatorname {Cat}_r}{2\operatorname {Cat}_{r-2}}
   =\frac{2(2r-3)(2r-1)}{r(r+1)},\\
 \theta_3(r)
 &=\frac{\operatorname {Cat}_r}{5\operatorname {Cat}_{r-3}}
   =\frac{8(2r-5)(2r-3)(2r-1)}{5(r-1)r(r+1)}.
\end{aligned}                                         \tag{4.10}
\]

They tend respectively to \(8\) and \(64/5\).

At the fatal scale \(\theta\ge4\), both \(d_0\) and \(d_1\) exceed
\(p\).  Therefore the four-unit transport \(2\to3\) is cap-neutral, while
the removal at label \(4\) contributes one clean unit.  The removal at
label \(6\) contributes after \(\theta_2(r)\), and the two insertions at
label \(7\) begin to cost at \(\theta_3(r)\).  With no collision load on
the odd destinations, the exact marked-profile gain is

\[
\begin{aligned}
g_{b_1}^{\rm clean}={}&
 R_4(d_0)+R_1(d_1)+R_1(d_2)
 -A_4(d_1)-A_2(d_3).                                  \tag{4.11}
\end{aligned}
\]

Away from the integer threshold bands this is

\[
 g_{b_1}^{\rm clean}=
 \begin{cases}
 1,&4\le\theta<\theta_2(r),\\
 2,&\theta_2(r)<\theta<\theta_3(r),\\
 0,&\theta>\theta_3(r).
 \end{cases}                                          \tag{4.12}
\]

If \(\theta\ge\theta_3(r)\), all four singleton pair classes are already
at cap.  Any equal-mass singleton profile supported on them has
nonnegative new-minus-old hinge change, so the singleton mechanism cannot
produce positive cap descent.  This is an exact singleton no-go; it does
not apply to the length-two and length-three profiles in (1.4).

The loads in (4.7) are only the intrinsic canonical contribution.  Other
contexts can collide with the destinations in (4.5), and the remaining
profiles in (1.4) have their own loads.  Formula (4.5), not (4.12), is
authoritative for the physical factor.

### Proposition 4.2 (correct one-sided parity preload)

Let
\[
 w_j=\operatorname {Cat}_{j-1}\operatorname {Cat}_{r+1-j}.
\]
At every protected depth,
\[
\begin{aligned}
 \mu_q^{\rm par}(K^-_{q,1}\cup\{2j\})&=w_j,&
 \mu_q^{\rm par}(K^-_{q,1}\cup\{2j-1\})&=0,\\
 \mu_q^{\rm par}(K^+_{q,1}\cup\{2j-1\})&=w_j,&
 \mu_q^{\rm par}(K^+_{q,1}\cup\{2j\})&=0.
\end{aligned}                                         \tag{4.13}
\]
Indeed \(b_1=2j\) and \(a_4=2j-1\) have the same first-return
multiplicity \(w_j\), but they lie on the opposite exterior suffix and
prefix carriers.  A nonempty proper prefix of the distinct-symbol
exterior word is not the equal-length proper suffix, and longer local
profiles cannot equal a singleton target.

Thus on the marked \(K^-\)-carrier the clean old loads at
\((2,3,4,6,7)\) are
\[
                         (d_0,0,d_1,d_2,0),
\]
where
\[
 d_0=\operatorname {Cat}_r,\qquad
 d_1=\operatorname {Cat}_{r-1},\qquad
 d_2=2\operatorname {Cat}_{r-2}.
\]
For \(p\ge4\), the corrected collision-free gain is
\[
 \boxed{g_{b_1}^{\rm clean}
   =R_4(d_0)+R_1(d_1)+R_1(d_2).}                     \tag{4.14}
\]
At \(\theta=\operatorname {Cat}_r/p\ge4\), away from the sole threshold
\[
 \theta_2(r)=\frac{\operatorname {Cat}_r}
                   {2\operatorname {Cat}_{r-2}}\longrightarrow8,
\]
this is five below \(\theta_2(r)\) and six above it.  There is no
\(64/5\) cutoff for the left chain.  Foreign collision loads and all
companion profiles remain uncontrolled, so this correction does not
prove positive full-packet PCap gain.

## 5. Multidepth PCap decision

Let

\[
 \mathcal O_q(\mu)=\sum_S(\mu(S)-p)_+,
 \qquad B_q=W-\binom{2m+1}{m-q},                       \tag{5.1}
\]

so the depth-\(q\) PCap summand is

\[
                         P_q(\mu)=[\mathcal O_q(\mu)-B_q]_+.     \tag{5.2}
\]

For the full profile (1.4), the exact cumulative gain of one switch is

\[
\boxed{
 \mathcal G_{r,Q}
 =\sum_{q=r}^{Q}left(
   P_q(\mu_q)-P_q(\mu_q+D_q)
                     \right).}                        \tag{5.3}
\]

Since every profile in (1.4) has total mass zero, the hinge is
one-Lipschitz in positive mass.  Equation (3.3) gives

\[
                 |P_q(\mu_q+D_q)-P_q(\mu_q)|\le88,    \tag{5.4}
\]

and therefore

\[
                         |\mathcal G_{r,Q}|le88(Q-r+1).       \tag{5.5}
\]

The marked profile can contribute at most six per depth; the other
profiles have an eighty-two-unit triangle budget.  The same binary factor
choice multiplies every depth column, so they cannot be optimized
independently.

### Theorem 5.1 (exact conditional boundary)

1. There is no algebraic cross-depth cancellation: the sixteen profile
   families are nested chains in different ranks.
2. If the full physical loads satisfy, on a positive density of depths,
   a uniformly positive version of (4.5) after including all other terms
   of (1.4), and the old PCap summand is on its active branch, then one
   switch has \(\Omega(Q-r)\) PCap gain.
3. The explicit tensor does not prove that sign condition.  It also does
   not force cancellation: the complement partners have the same sign and
   different carriers.
4. If every affected physical target is already at cap, the total-zero
   singleton columns give no positive singleton descent.  Longer local
   profiles remain undecided.

#### Proof

Item 1 is Theorem 1.1.  Summing a positive per-depth gain proves item 2.
Equations (3.2)--(3.4) prove item 3.  For item 4, if every old load is at
least \(p\), additions lie on the linear branch, while a removal crossing
below the hinge can only lose some of its nominal benefit.  Since each
profile has zero total mass, its net old-minus-new gain is nonpositive.
\(\square\)

Thus the answer is neither unconditional linear gain nor chainwise
cancellation.  The tensor proves linear hereditary *capacity*; the actual
cap sign is a load-placement problem.

## 6. Minimal remaining lemma

The exact missing statement is a physical carrier/load theorem, not a new
finite factor:

> **Hereditary `D_4` full-profile drain lemma.**  Realize a
> product-compatible bank of the port-linearized blocks (0.1), and prove
> for their actual collided profiles (1.6) that
> \[
>  \sum_{q=r}^{Q}left[
>   P_q(\mu_q)-P_q(\mu_q+D_q)
>  \right]\ge c(Q-r)                                  \tag{6.1}
> \]
> for some absolute \(c>0\) on a positive-density subbank.

The canonical preload calculation certifies part of the negative-side
saturation in (4.5).  It does not control the odd destinations, the
opposite singleton interface, or the remaining prefix/suffix collars.
Until (6.1) is proved, the `D_4` switch cannot be credited with
\(\Omega(Q-r)\) PCap gain.
