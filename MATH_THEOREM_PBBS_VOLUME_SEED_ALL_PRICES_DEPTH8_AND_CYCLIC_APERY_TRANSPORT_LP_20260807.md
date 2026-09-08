# The volume seed controls every depth-eight min-plus price; cyclic Apéry repair is an exact finite transport LP

**Date:** 2026-08-07  
**Status:** unconditional all-price theorem for the terminal even
depth-eight parent/child pair, plus an unconditional finite primal/dual
formulation of the cross-residue gate at every fixed depth.  No
all-depth feasibility theorem is claimed.

## 1. The general cyclic transport LP

Fix a minimum-density denomination $h$.  After subtracting its linear
slope, write

\[
                         e_i=p_i-{i\over h}p_h\ge0
                         \quad(1\le i<h).
 \tag{1.1}
\]

Suppose a volume-balanced signed price functional has positive
coefficients $s_i$ at the first representatives $1\le i<h$ and negative
coefficients thereafter.  Aggregate its negative mass by residue:

\[
 d_i=-\sum_{j\ge1}\mu_{i+jh},
 \qquad
 S_i=s_i-d_i,
 \qquad
 \Delta_i=(-S_i)_+,
 \qquad
 c_i=(S_i)_+.
 \tag{1.2}
\]

There is an exact uncompressed configuration LP behind the argument.  For
each negative length $L$, let

\[
 \mathcal C_L=\left\{x\in\mathbb Z_{\ge0}^{h-1}:
 \sum_{i=1}^{h-1}ix_i\le L,
 \quad \sum_{i=1}^{h-1}ix_i\equiv L\pmod h\right\}.
 \tag{1.2a}
\]

The unused length is filled with zero-reduced-cost size-$h$ pieces.  With
$d_L=-\mu_L$, the exact fractional transport system is

\[
 \sum_{x\in\mathcal C_L}z_{L,x}=d_L,
 \qquad
 \sum_L\sum_{x\in\mathcal C_L}x_i z_{L,x}\le s_i,
 \qquad z_{L,x}\ge0.
 \tag{1.2b}
\]

Its Farkas dual is

\[
 \boxed{
 \sum_{i=1}^{h-1}s_i y_i
 \ge\sum_Ld_L\min_{x\in\mathcal C_L}x\cdot y
 \quad\text{for every }y\in\mathbb R_{\ge0}^{h-1}.}
 \tag{1.2c}
\]

Thus feasibility of (1.2b) proves the all-price inequality for critical
denomination $h$.  It is also necessary for the stronger test against
every nonnegative reduced edge-cost vector $y$.

For explicit proofs, compress (1.2b) by residue: cover as much as possible
with one direct piece, and route only the remaining deficits through a
common alternative partition of the first post-$h$ length.

For a deficit residue $a$, let

\[
 \mathcal X_a=\left\{x\in\mathbb Z_{\ge0}^{h-1}:
 \sum_{i=1}^{h-1}ix_i=h+a,
 \quad x_i=0\text{ whenever }S_i<0\right\}.
 \tag{1.3}
\]

Every $x\in\mathcal X_a$ is an alternative partition of the first
post-$h$ length in residue $a$.  It also partitions every later length
$a+jh$ after appending $j-1$ free size-$h$ pieces.

### Theorem 1.1 (compressed cyclic Apéry criterion)

If there are nonnegative numbers $z_{a,x}$ satisfying

\[
 \sum_{x\in\mathcal X_a}z_{a,x}=\Delta_a
 \quad(S_a<0),
 \tag{1.4}
\]

and

\[
 \sum_{a:S_a<0}\sum_{x\in\mathcal X_a}x_i z_{a,x}
 \le c_i
 \quad(1\le i<h),
 \tag{1.5}
\]

then the signed functional is nonnegative on every min-plus price having
$h$ as a minimum-density denomination.

#### Proof

Let $\delta(L)=\psi(L)-Lp_h/h$.  Direct use of one size-$i$ piece and
free size-$h$ pieces gives $\delta(i+jh)\le e_i$.  A configuration
$x\in\mathcal X_a$ gives $\delta(a+jh)\le x\cdot e$.  Cover $s_a$ of a
deficit residue directly and distribute its remaining mass $\Delta_a$
according to $z_{a,x}$.  Cover every nondeficit residue directly.  The
remaining coefficient of $e_i$ is at least the left-over capacity in
(1.5), hence is nonnegative.  Multiples of $h$ have zero reduced cost,
and volume balance cancels the linear slope. \(\square\)

This compressed finite LP has the exact Farkas dual

\[
 \boxed{
 \sum_{i=1}^{h-1}c_i y_i
 \ge
 \sum_{a:S_a<0}\Delta_a
       \min_{x\in\mathcal X_a}x\cdot y
 \quad\text{for every }y\in\mathbb R_{\ge0}^{h-1}.}
 \tag{1.6}
\]

Thus the remaining all-depth claim has a finite cyclic shortest-path
certificate, not an infinite fan problem.

There is also an exact structural warning.  With several deficit
residues, configurations consume several shared piece capacities, so
(1.4)--(1.5) is generally a fractional hypergraph packing LP, not an
ordinary one-commodity network matrix.  Max-flow interval cuts are not
automatically sufficient.  A genuine all-depth proof must exploit the
special binomial surplus vector, or prove that a restricted interval or
circulant family of configurations is sufficient.

## 2. Terminal depth-eight coefficients

Take

\[
 D=8,\qquad n=182,\qquad n-2=180.
 \tag{2.1}
\]

The child and parent volume margins are

\[
\begin{aligned}
 V_{180,8}&=7356343286129994643216806714860540274994091985142713,\\
 V_{182,8}&=12423084930913947280067439600320949405814529411407249.
\end{aligned}
 \tag{2.2}
\]

Define the integer-scaled coefficient measure

\[
 \widehat\mu_L=
 V_{180,8}\nu_{182,8}(L)-V_{182,8}\nu_{180,8}(L),
 \tag{2.3}
\]

where

\[
 \nu_{n,D}(L)=
 \mathbf1_{L\le D}H_{n/2-D+L}^{(n)}
 -\widetilde H_{n/2-D-L}^{(n)}.
 \tag{2.4}
\]

Then

\[
 V_{180,8}
 \left(M_{182,8}(\psi)-{V_{182,8}\over V_{180,8}}M_{180,8}(\psi)\right)
 =\sum_L\widehat\mu_L\psi(L).
 \tag{2.5}
\]

The coefficients have the one-sign-change pattern

\[
 \widehat\mu_1,\ldots,\widehat\mu_7>0,
 \qquad
 \widehat\mu_L<0\quad(8\le L\le82).
 \tag{2.6}
\]

The exact short-rank certificate is

\[
\begin{aligned}
 \min_{1\le L\le7}\widehat\mu_L
 &=10462856962231059480488815422829203848805469455092102651039990596851366772343617064253438464676677796660,\\
 \widehat\mu_8
 &=-12061843420083108997571399172266789838463118659895440651879793885637632054923218640093105585444899627580.
\end{aligned}
 \tag{2.7}

For $9\le L\le80$, put $s=83-L$, so $3\le s\le74$.  The ratio identity

\[
 {H_s^{(182)}\over H_{s-1}^{(180)}}
 ={32942\over s(183-s)}
 \ge {16471\over4033}>4
 >{V_{182,8}\over V_{180,8}}
 \tag{2.8}
\]

proves the negative tail sign.  At $L=81$, the modified child rank-one
term is dominated because

\[
 -H_2^{(182)}+{V_{182,8}\over V_{180,8}}\,180
 <-16289+2\cdot180<0,
 \tag{2.9}
\]

and at $L=82$ only the negative parent rank-one term remains.

## 3. Minimum-density denominations below eight

For $2\le h\le7$, put

\[
                         S_{h,a}=\sum_{j\ge0}
                         \widehat\mu_{a+jh}.
 \tag{3.1}
\]

The exact minimum nonzero-residue totals are

\[
\begin{array}{c|c|r}
h&\operatorname*{argmin}_{1\le a<h}S_{h,a}
 &\min_{1\le a<h}S_{h,a}\\ \hline
2&1&67880889997754011755214328987123387863720870125570966503198984309338928413342093280483989191002958151662\\
3&2&43882677902359315476492328478855374565581775200522693734085060057626037648419882586431557202842908033157\\
4&1&29669546669735170963961966768061328356391356570838808874208038187493977754992110092123306417941004227015\\
5&4&19242720842002644880693142621904066013058738721594543591911850465957748672209731770714151736097378060225\\
6&2&15614625317201390764205356802242966588071868105865584948823293605705116878686610658134473456257524532657\\
7&1& 2666773637059922966686366327235082605709724921714248576374739403149199654228900963897719563912257757315
\end{array}
 \tag{3.2}
\]

The one-sign-change pattern makes every prefix on each nonzero residue
nonnegative.  The residue-prefix lemma proves the all-price inequality for
every minimum-density denomination $h\le7$; $h=1$ is the tight linear
case.

## 4. The critical denomination eight

At $h=8$, the residue totals $S_i$ for $1\le i\le7$ are

\[
\begin{array}{c|r}
i&S_i\\ \hline
1&-4967552137855314253589907967671092425703711595604551421317830545958499042941268802025743379365611947705\\
2&15475689079241129686990613960937242771239142942980061514680843572533243532403804181473118870086319057378\\
3&29657079131821006229407234090126035243451680214771173555989970373867351726305771597311010949910180756997\\
4&36241338468523228612563961588818678452434811652636569937087817805369446670646897658432537635473575377648\\
5&34637098807590485217551874735732420782095068166443360295525868733452476797933378894149049797306616174720\\
6&25069860890631428313723512474576918707354188409822842604076726133602002015153219893948099437812889276100\\
7& 8554264196197834561845128128936024263877833339960984073000975747977598932044211591049671823151773167650
\end{array}
 \tag{4.1}
\]

Only residue one is deficient.  Write

\[
 \Delta=4967552137855314253589907967671092425703711595604551421317830545958499042941268802025743379365611947705.
 \tag{4.2}
\]

Use the alternative partition

\[
                         9=2+7.
 \tag{4.3}
\]

The exact remaining capacities are

\[
\begin{aligned}
 S_2-\Delta
 &=10508136941385815433400705993266150345535431347375510093363013026574744489462535379447375490720707109673,\\
 S_7-\Delta
 &=3586712058342520308255220161264931838174121744356432651683145202019099889102942789023928443786161219945.
\end{aligned}
 \tag{4.4}
\]

They are positive, so Theorem 1.1 applies with the single route
$1\mapsto2+7$.

## 5. Exact depth-eight theorem

### Theorem 5.1 (all depth-eight prices)

For every closed depth-eight piece table and its complete min-plus
closure,

\[
 \boxed{
 M_{182,8}(\psi)
 -{V_{182,8}\over V_{180,8}}M_{180,8}(\psi)\ge0.}
 \tag{5.1}
\]

Equivalently, the exact minimum central weight for a unit distance-one
pair is

\[
 \boxed{
 \rho^{\rm vol}_8
 =2-{V_{182,8}\over V_{180,8}}
 ={2289601641346042006366173829400131144173654558878177
   \over7356343286129994643216806714860540274994091985142713}.}
 \tag{5.2}
\]

The linear price is tight, and every depth-eight min-plus fan ray is
nonnegative at this weight.  Its Pascal convolution orbit is therefore an
exact nonnegative weighted invariant cone.

## 6. What the transport formulation does and does not give

At depths seven and eight, the cyclic LP has one deficit and a one-route
solution:

\[
                         1\mapsto2+(h-1).
 \tag{6.1}
\]

At larger depths several deficits eventually appear, and a route can
consume two or more shared surplus coordinates.  The exact universal
claim is feasibility of (1.4)--(1.5).  Total surplus alone is not a
generic sufficient condition for that hypergraph packing LP; any proof
that only quotes a one-commodity max-flow theorem would leave a real gap.
The promising additional input is the total positivity and unimodality of
the binomial surplus vector $S_i$, which may force a small balanced route
set to satisfy every Farkas inequality (1.6).
