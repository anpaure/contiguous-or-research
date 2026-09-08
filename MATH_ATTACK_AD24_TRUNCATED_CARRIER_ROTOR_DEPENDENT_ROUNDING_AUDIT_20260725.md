# AD24: truncated carrier rotors, coherent diamonds, and the Poisson/throughput boundary

Date: 2026-07-25

Pure mathematics only. No computation, solver, or web input is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

let (H) be the first integer for which

\[
 {W\over N_H}\ge M:=m+H,
\]

and take

\[
 Q=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil,
 \qquad \gamma\to\infty,
 \qquad \gamma=o(\log\log m).
\]

Thus

\[
 H\sim\sqrt{m\log m},\qquad Q=o(H),\qquad
 MN_H=W-o(W),\qquad QN_H=o(W).
\]

The truncated carrier-rotor reduction in
`TRUNCATED_CARRIER_ROTOR_PATH_REDUCTION_20260725.md` is arithmetically and
literally sound.  A path of \(M\) states in every carrier has primary
length \(W+o(W)\), exposes the complete hard flag column through depth
\(Q\), and has the exact symmetric fractional loads.  The outer packet
reservoir, an explicit literal copy of the \(N_H\) upper top masks, and
the two Boolean tails cost \(o(W)\).  This endpoint copy is necessary:
at upper depth \(H\), a full packet has one distinct top target, not \(M\)
distinct targets.

The extra rotor branching does not, by itself, remove the integral gate.
The exact audit gives the following sharper boundary.

1. At a fixed carrier state there are

   \[
    (m-Q)(H-Q)
   \]

   outgoing rotor edges, but all successor flags except the deepest lower
   flag depend only on the chosen (y\in R_U).  After quotienting the
   (m-Q) repeated choices of (x\), the visible branching on the other
   (2Q) hard rows is only (H-Q).  The factor (m-Q) is delayed rotor
   memory, not immediate owner/column branching.

2. Independent stationary path choices retain the exact critical-load
   obstruction.  A fixed middle owner is missed with probability at least

   \[
    (1-\vartheta_0)^{K_0}=e^{-1}+o(1),
   \]

   where

   \[
    \vartheta_0={M\over\binom MH},\qquad
    K_0=\binom mH,\qquad
    K_0\vartheta_0={MN_H\over W}=1-o(1).
   \]

   Hence independent carrier paths have ((e^{-1}+o(1))W) middle holes
   and linear collision excess.  Within-path repetitions only make this
   lower bound worse.

3. There is nevertheless a new exact physical trade.  Two insertions
   (x_1,x_2\in L) may be transposed and then carried through the rotor
   until they leave the queue.  The two resulting path segments rejoin
   after exactly (2Q+2) edges.  Their flag-incidence difference is one
   unit exchange at each of the (2Q+1) ranks

   \[
    m-Q,m-Q+1,\ldots,m+Q,
   \]

   and is zero elsewhere.  Thus its total vertical squared movement is

   \[
    \boxed{2(2Q+1)=o(M).}
   \]

   This is a genuine one-path-per-carrier coherent-column exchange; it
   avoids the doubled-top defect of the full-packet rectangle.

4. Low variance alone is not enough.  For every integral random exchange
   (z),

   \[
    \sum_r\|z_r\|_1\le \sum_r\|z_r\|_2^2.
   \]

   Consequently a statewise mean-reversion identity

   \[
    \mathbb Ez_r=-\kappa_r g_r+e_r,
    \qquad \kappa_r\ge c/N_H,
   \]

   cannot have total variance (o(M)) and normalized bias (o(W)) at
   every state.  There are valid one-path-per-carrier states with
   (|g_0|_1=\Omega(W)); at any such state, variance (o(M)) forces

   \[
    {\|e_0\|_2^2\over\kappa_0^2}=\Omega(W).
   \]

   Therefore the conditional descent implications in the AD22
   low-variance mean-reversion report are algebraically correct, but their
   proposed uniform \(C_m=o(M)\), \(\beta=o(W)\) hypothesis is impossible
   on the full integral state space.  It is not the remaining positive
   theorem.

The carrier diamond is still useful.  What remains is a nonlinear
donor-to-hole theorem for these coherent vertical exchanges, or a global
matching/nibble on complete rotor paths.  Product sampling, a bounded
independent-cluster construction, and an unbiased low-variance martingale
are rigorously insufficient.  No theorem here rules out a genuinely global
path selection exploiting the delayed (x)-memory.

## 1. Audit of the truncated carrier reduction

Write

\[
 a=m-Q,\qquad b=H-Q,\qquad n=2Q.
\]

For a fixed carrier (U\in\binom{[2m]}M), a state is

\[
 \omega=(L;z_1,\ldots,z_n;R_U),
 \qquad |L|=a,\quad |R_U|=b,
\]

and an edge indexed by (x\in L), (y\in R_U) is

\[
 \mathcal R_{x,y}(\omega)
 =
 (L-x+y;\ x,z_1,\ldots,z_{n-1};\ R_U-y+z_n).
\tag{1.1}
\]

The state count and directed degree are exactly

\[
 |\Omega_Q(U)|={M!\over a!b!},\qquad
 d^+(\omega)=d^-(\omega)=ab.
\tag{1.2}
\]

The move is the directed slot cycle carrying (y) from the right block
to the left block, (x) into the first singleton, every singleton one
place to the right, and (z_n) into the right block.  The slot cycles and
the internal symmetric groups on the two unordered blocks generate the
state quotient.  Hence the underlying graph is connected; regularity then
makes the directed graph strongly connected.

The flag column is

\[
 L_q(\omega)=L+z_1+\cdots+z_{Q-q},
 \qquad 0\le q\le Q,
\tag{1.3}
\]

\[
 U_q(\omega)=L+z_1+\cdots+z_{Q+q},
 \qquad 0\le q\le Q.
\tag{1.4}
\]

In particular the middle owner is

\[
 X(\omega)=L+z_1+\cdots+z_Q.
\]

Equation (1.1) gives

\[
 X(\mathcal R_{x,y}\omega)=X(\omega)-z_Q+y.
\tag{1.5}
\]

At a fixed state this has only (b=H-Q) possible next owners, one for
each (y\).  The statement that a uniform edge gives a uniform one of the
(mH) Johnson neighbors is true only after first averaging a uniform
state conditional on its owner: then (z_Q) is uniform in the owner and
(y) is uniform in its complement.  This distinction is essential for a
local nibble.

A path with (s) states initializes in (2Q+2) nonempty letters and then
uses one new core letter per edge.  Its length is therefore

\[
 s+2Q+1.
\tag{1.6}
\]

Taking (s=M) at all (N_H) carriers gives

\[
 MN_H+(2Q+1)N_H=W+o(W).
\tag{1.7}
\]

Uniform initial state followed by uniform rotor edges is stationary because
the directed graph is regular.  Every time marginal is uniform, and hence
every hard-rank flag is uniform among the subsets of that rank inside the
carrier.  Summing over carriers gives the exact fractional target load

\[
 \binom{2m-r}{M-r}{M\over\binom Mr}
 ={MN_H\over\binom{2m}r}.
\tag{1.8}
\]

Thus the counting, integrality, literal chronology, and fractional-load
claims of the reduction pass.  Here a path may be a directed walk; no
simplicity assertion is needed.

There is one endpoint correction to Section 5 of the source reduction.  For
\(Q<q<H\), a uniform full packet hits a fixed proper lower or upper target
with probability \(M/N_q\), and the reservoir sum must include a factor two
for the two signs.  At \(q=H\), the lower target is still proper, but the
upper target is the carrier top itself and is hit with probability
\(1/N_H\), not \(M/N_H\).  Append all \(N_H=O(W/m)=o(W)\) upper top masks
literally.  With this correction the reservoir and tail estimates retain
their claimed \(o(W)\) total cost.

## 2. The exact fixed-state branching quotient

Let

\[
 \omega'=\mathcal R_{x,y}(\omega).
\]

Substitution of (1.1) into (1.3)--(1.4) gives, for (0\le q<Q),

\[
 \boxed{
 L_q(\omega')
 =L+y+z_1+\cdots+z_{Q-q-1},}
\tag{2.1}
\]

while at the deepest lower rank

\[
 \boxed{L_Q(\omega')=L-x+y.}
\tag{2.2}
\]

For every (0\le q\le Q),

\[
 \boxed{
 U_q(\omega')
 =L+y+z_1+\cdots+z_{Q+q-1}.}
\tag{2.3}
\]

Empty sums are omitted.  In (2.1) and (2.3), the inserted (x) cancels
the deleted (x) from the left block.  Therefore:

* the middle owner and all hard flags except (L_Q) depend only on (y);
* the (ab) outgoing edges split into exactly (b) identical projected
  profiles on those (2Q) rows, each with multiplicity (a);
* the full hard column, including (L_Q), distinguishes all (ab)
  pairs ((x,y)).

Thus the extra factor (a=m-Q) is real state entropy, but its immediate
visible effect is confined to the deepest lower row.  It enters the owner
and the other ranks only after the inserted label has travelled through
the rotor.  A one-step coherent-column nibble which counts all (ab)
edges as independent choices overcounts the visible link by exactly the
factor (a).

## 3. The product-path Poisson obstruction

Consider the natural product law: independently for each carrier, choose a
length-(M) stationary rotor path by taking a uniform start state and
uniform successors.

Fix a target (T\in\binom{[2m]}r) and a carrier (U\supset T).  Let

\[
 Y_{U,T}
 =\#\{\text{selected states in the path on }U
           \text{ whose rank-}r\text{ flag is }T\}.
\]

Stationarity and (1.8) give

\[
 \mathbb EY_{U,T}=\vartheta_r,
 \qquad
 \vartheta_r={M\over\binom Mr}.
\tag{3.1}
\]

Hence

\[
 s_r:=\Pr(Y_{U,T}>0)\le\vartheta_r.
\tag{3.2}
\]

The number of carriers containing (T) is

\[
 K_r=\binom{2m-r}{M-r},
\]

and their paths are independent.  Therefore

\[
 \Pr(T\text{ is missed})
 =(1-s_r)^{K_r}
 \ge(1-\vartheta_r)^{K_r}.
\tag{3.3}
\]

At the middle rank,

\[
 \vartheta_0={M\over\binom MH}=o(1),
 \qquad
 K_0\vartheta_0={MN_H\over W}=1-o(1).
\]

Consequently

\[
 \boxed{
 \Pr(T\text{ is missed})\ge e^{-1}-o(1).}
\tag{3.4}
\]

Summing over all (W) owners proves

\[
 \boxed{
 \mathbb E[\text{middle holes}]
 \ge(e^{-1}-o(1))W.}
\tag{3.5}
\]

Since the deterministic slot deficit (W-MN_H) is (o(W)), the expected
middle collision excess is also linear.  This proof uses only first moments
and independence between carriers; it does not assume temporal independence
inside a path.  Repeated visits make (s_r<\vartheta_r) and increase the
void probability.

Thus the polynomial rotor outdegree cannot by itself support an independent
or product-cluster nibble at critical load.  Dependence between carriers is
still indispensable.

## 4. A coherent two-insertion rotor diamond

The rotor does supply a useful exact path exchange which is absent from a
frozen cyclic packet.

### Theorem 4.1 (vertical transposition diamond)

Assume (a\ge2) and (b\ge2).  From every carrier state (omega_0)
there are two directed path segments with the same initial state, the same
terminal state, and exactly (n+2=2Q+2) edges, such that their hard-rank
flag-incidence vectors differ by exactly one unit exchange in every rank

\[
 a,a+1,\ldots,a+n
 =m-Q,m-Q+1,\ldots,m+Q.
\tag{4.1}
\]

At every one of these ranks the two changed targets differ by exchanging
the same two labels (x_1,x_2).  No other hard flag occurrence changes.

#### Proof

Choose distinct (x_1,x_2\in L) and choose (y_1\in R_U).  On side A
take first move ((x_1,y_1)); on side B take first move
((x_2,y_1)).  The right blocks after these moves agree.  Choose a common
legal (y_2) there.  On side A take second deletion (x_2), and on side
B take second deletion (x_1).  Both are legal.  After two moves the two
states have the same left and right blocks, while their singleton queues
are

\[
 (x_2,x_1,z_1,\ldots,z_{n-2})
 \quad\hbox{and}\quad
 (x_1,x_2,z_1,\ldots,z_{n-2}).
\tag{4.2}
\]

Continue with the same choices of (x) and (y) on both sides.  Until
the first of (x_1,x_2) leaves the last queue slot, the two left and right
blocks remain identical.  At the next step their right blocks differ by
exchanging (x_1,x_2); because (b\ge2), choose the following (y) in
their common intersection.  When the second label leaves the queue, the
right blocks agree again.  The queues also agree because both transposed
labels have left them, and the later inserted labels were identical in
the two paths.  The paths therefore rejoin after (n+2) moves.

It remains to compare flags.  After the first move, the two states differ
only in the left block versus the first singleton.  Every nonempty prefix
contains the displaced label and cancels the difference, so only prefix
length zero, of rank (a), changes.

After \(j\) moves, \(2\le j\le n\), the two labels occupy adjacent queue
positions \(j-1,j\).  The two prefix sets agree except at prefix length
\(j-1\), giving one unit exchange (two signed target coordinates) at rank
\(a+j-1\).  After move
(n+1), one transposed label is in the right block and the other is in the
last singleton slot.  Only the full queue prefix changes, at rank (a+n).
After move (n+2) the states are identical.  This accounts once for every
rank in (4.1) and for no other flag.  At each differing prefix the common
core is the same and one side contains (x_1), the other (x_2).
\(\square\)

If (z_r) denotes the load change when one side of the diamond is replaced
by the other, Theorem 4.1 gives

\[
 z_r=e_{A_r}-e_{B_r},\qquad
 \|z_r\|_2^2=2,
\]

at each of the (J=2Q+1) hard ranks.  Hence

\[
 \boxed{
 \sum_{|r-m|\le Q}\|z_r\|_2^2=2J=4Q+2=o(M).}
\tag{4.3}
\]

The middle row occurs exactly once in this list, so the diamond changes
only one middle owner.  It is therefore compatible with an (o(W)) owner
ledger when used (o(W)) times.  Unlike a signed four-order packet
rectangle, it is an actual one-path-for-one-path transition inside one
carrier.

## 5. A discrete variance-throughput obstruction

The low variance (4.3) is not sufficient for the linear mean-reversion
hypothesis proposed in
`MATH_ATTACK_AD22_DEPENDENT_VERTICAL_PHASE_ROUNDING_20260725.md`.

### Theorem 5.1 (integral throughput inequality)

Let (z\in\mathbb Z^N) be any random integral row change.  Suppose

\[
 \mathbb Ez=-\kappa g+e,
 \qquad
 \mathbb E\|z\|_2^2\le C.
\tag{5.1}
\]

Then

\[
 \boxed{
 {\|e\|_2^2\over\kappa^2}
 \ge
 {\bigl(\|g\|_1-C/\kappa\bigr)_+^2\over N}.}
\tag{5.2}
\]

#### Proof

For every integral coordinate (u), (|u|\le u^2).  Hence

\[
 \|\mathbb Ez\|_1
 \le\mathbb E\|z\|_1
 \le\mathbb E\|z\|_2^2
 \le C.
\tag{5.3}
\]

Equation (5.1) and the triangle inequality give

\[
 \|e\|_1\ge\kappa\|g\|_1-C.
\]

Finally (|e|_1\le\sqrt N\|e|_2).  Division by (kappa^2)
proves (5.2).  \(\square\)

### Corollary 5.2 (uniform low-variance mean reversion is impossible)

There are valid one-path-per-carrier configurations whose middle centered
load (g_0) satisfies

\[
 \|g_0\|_1\ge c_0W
\tag{5.4}
\]

for an absolute (c_0>0).

Indeed, by (3.5), under product stationary paths the expected number of
middle holes is at least ((e^{-1}-o(1))W).  Some deterministic outcome has
that many holes.  Each zero load contributes

\[
 {S\over W}=1-o(1)
\]

to the centered (ell^1)-norm, proving (5.4).

Now let (p=N_H=(1+o(1))W/M).  At the state (5.4), suppose

\[
 \kappa\ge {c\over p},\qquad C=o(M).
\]

Then

\[
 {C\over\kappa}=o(W),
\]

and (N=W) in the middle row.  Theorem 5.1 yields

\[
 \boxed{
 {\|e_0\|_2^2\over\kappa^2}=\Omega(W).}
\tag{5.5}
\]

This contradicts any state-uniform normalized-bias bound (o(W)).  The
same argument applies to full cyclic packets, since their product law also
has Poisson-scale middle holes.

Therefore Theorems 5.1 and 5.2 of the AD22 report remain correct as
conditional implications, but the advertised uniform low-variance
hypothesis cannot hold on their stated full state spaces.  At diffuse
critical discrepancy, integral shot noise forces

\[
 C\ge\kappa\|g\|_1-o(M)=\Omega(M)
\]

unless the bias already cancels a linear part of the desired drift.

For a distribution supported on single carrier diamonds, (4.3) gives

\[
 C=O(Q).
\]

At a state satisfying (5.4), unbiased mean reversion can therefore have
rate at most

\[
 \kappa=O(Q/W),
\]

whereas the AD22 descent requires

\[
 1/p=\Theta(M/W).
\]

The shortfall is the diverging factor (M/Q).

## 6. What the diamond can still do

For the balanced factorial potential in one row, a unit transport

\[
 z=e_B-e_A
\]

has the exact increment

\[
 \Delta\Psi=h_B-h_A+1.
\tag{6.1}
\]

For a carrier diamond, orient the notation so that every row removes
(A_r) and adds (B_r).  Its aggregate increment is

\[
 \boxed{
 \Delta\Psi_\Sigma
 =J+\sum_{|r-m|\le Q}(h_r(B_r)-h_r(A_r)).}
\tag{6.2}
\]

Thus the diamond is factorial-energy improving exactly when its aggregate
donor advantage exceeds the unavoidable integer toll (J).  An unbiased
average over diamonds pays this shot-noise toll and cannot create the
postulated low-variance Ornstein--Uhlenbeck drift.

The literal coefficient-one gate is weaker than balanced factorial energy.
At one row, replacing (A) by (B) changes support by

\[
 \Delta|\operatorname{supp}|
 =\mathbf1_{\{h_B=0\}}-\mathbf1_{\{h_A=1\}}.
\tag{6.3}
\]

Hence a nonlinear orientation can be useful whenever it fills more holes
than the singleton targets it destroys, even if (6.2) is not negative.
This is the correct surviving role of the carrier diamond: collision mass
may condense on a small overloaded reservoir, and the construction only
needs aggregate support loss (o(W)), not floor/ceiling balance.

A sufficient new statement would be a **coherent rotor-diamond descent
theorem**: from every path family with non-negligible aggregate support
loss, find a collection of endpoint-compatible diamonds whose orientations
increase total hard-rank support by a quantitatively comparable amount,
while spending (o(W)) path interfaces.  No such theorem is proved here.

## 7. Exact boundary

The audit proves:

1. The truncated carrier state graph, flag columns, literal compiler, and
   fractional loads are valid.  The outer-reservoir ledger is valid after
   restoring the factor two for the two proper signs and appending the
   \(N_H\) upper endpoint tops literally.
2. The raw outdegree (ab) has only (b) immediate profiles on all but
   the deepest lower row.
3. Independent carrier paths retain an (e^{-1})-scale middle void
   probability; the Poisson obstruction survives exactly.
4. The vertical transposition diamond is a new legal physical exchange
   with one unit exchange per hard rank and total squared movement \(2J\).
5. Uniform low-variance mean reversion at rate (1/N_H) is incompatible
   with integral throughput on diffuse critical states.  This corrects the
   claimed scope of the AD22 missing theorem.
6. A nonlinear support-increasing diamond descent or a genuinely global
   complete-path selection remains open.

Thus the extra branching is mathematically meaningful, but it has not yet
produced a coherent-column nibble.  It replaces the frozen-order exchange
obstruction by a sharper nonlinear path-routing gate; it does not remove
the need for global dependence.

The branch-quotient and product-hole calculations, the rotor-diamond
indexing, and the variance-throughput inequality were independently
audited.  A separate full proof of the last obstruction is recorded in
MATH_ATTACK_AD24_LVMR_VARIANCE_THROUGHPUT_AUDIT_20260725.md.
