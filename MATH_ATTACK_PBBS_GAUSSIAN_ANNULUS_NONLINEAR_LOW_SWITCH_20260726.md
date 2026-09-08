# PBBS Gaussian annulus by nonlinear low-switch rethreading

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad H=\lceil A\sqrt m\rceil .
\tag{0.1}
\]

Fix a Gaussian annulus

\[
 I_{a,b}=\{q:\lceil a\sqrt m\rceil\le q\le
                    \lfloor b\sqrt m\rfloor\},
 \qquad 0<a<b\le A.
\tag{0.2}
\]

There are two exact conclusions.

1. A separately appended annulus word cannot have cost \(o(W)\).  Already
   one boundary rank is an antichain of size

   \[
      \binom{2m+1}{m-q}=(e^{-q^2/m+o(1)})W=\Theta_{a,b}(W).
   \tag{0.3}
   \]

   Thus an economical annulus construction must reuse the PBBS baseline
   positions as witness endpoints.  This is a theorem, not an artefact of
   the product-SCD tail estimate.

2. The correct nonlinear scale is nevertheless compatible with coefficient
   one.  One physically safe seam has exactly \(q\) crossing windows of
   depth \(q\), for each sign.  They form nested flags as \(q\) varies.
   Hence one seam supplies

   \[
      2\sum_{q\in I_{a,b}}q
        =\bigl(b^2-a^2+o(1)\bigr)m
   \tag{0.4}
   \]

   valid signed annulus occurrences.  The whole annulus has
   \(\Theta_{a,b}(W\sqrt m)\) targets.  Therefore

   \[
      \boxed{s=\Theta_{a,b}(W/\sqrt m)}
   \tag{0.5}
   \]

   safe seams have exactly the right incidence capacity.  Since
   \(s=o(W)\), the number of colour switches is harmless.  What is fatal is
   charging every switch as a new radius-\(H\) run start: that costs
   \(Hs=\Theta(W)\).

The positive mechanism is therefore a **soft-switch rethreading**.  Cut the
PBBS owner factor into internally safe segments, reassign their successors,
and use every selected seam as part of the final physical chronology.  If
the rethreaded segments form \(c\) cycles, only those \(c\) cyclic openings
are hard starts.  The exact literal ledger is

\[
 \boxed{L\le W+2Hc+\mathsf H_{\rm ann}+\mathsf H_{\rm core},}
\tag{0.6}
\]

where \(\mathsf H_{\rm ann}\) is the aggregate annulus hole count of the
new chronology and \(\mathsf H_{\rm core}\) is the number of formerly
covered inner targets lost at the selected cuts.  Thus

\[
 c=o(W/H),\qquad
 \mathsf H_{\rm ann}=o(W),\qquad
 \mathsf H_{\rm core}=o(W)
\tag{0.7}
\]

give an \(o(W)\)-cost annulus extension in place.

This note does not construct the required PBBS rethreading.  It identifies
its exact integral discrepancy.  In the isolated-seam regime, the problem
is a simultaneous all-depth bundle matching.  A permanent argument proves
near-coverage if every missing target has a growing number of options from
every tail port.  However the exact incidence census shows that at the
critical isolated scale the average such degree is only \(\Theta(1)\).
Random or independently chosen seam matchings therefore cannot prove the
little-oh.

Trying to gain logarithmic degree forces more than \(W/H\) seams, so the
average colour run is shorter than \(H\).  Then an \(H\)-window crosses
several seams and its target depends on the whole colour cylinder, not on
one tail--head edge.  The surviving gate is precisely a nonlinear,
stateful cylinder near-resolution:

\[
 \boxed{
  \mathbb E_\mu \mathsf H_{\rm ann}=o(W),\qquad
  H\,\mathbb E_\mu c=o(W)
 }
\tag{0.8}
\]

for a law \(\mu\) supported on owner-valid, globally \(H\)-safe PBBS
rethreadings.  Equation (0.8), together with the inner-loss condition in
(0.7), is sufficient by averaging.  A positive-density family of targets
which every such cylinder law misses is the exact obstruction.

The point of (0.8) is not to rename the original problem.  Sections 2--6
prove the literal compiler, the exact simultaneous seam service, the sharp
switch lower bound, the permanent theorem in the edge-local regime, and
the precise place where that regime breaks.  Consequently the remaining
object is an all-order colour-cylinder resolution, not another marginal or
pair-covariance estimate.

## 1. The antichain forces in-place reuse

For the paired odd-dimensional ranks put

\[
 \mathcal T_q^-=\binom{[2m+1]}{m-q},\qquad
 \mathcal T_q^+=\binom{[2m+1]}{m+1+q},
\tag{1.1}
\]

so both have cardinality

\[
 N_q=\binom{2m+1}{m-q}.
\tag{1.2}
\]

The local Johnson calculations below are stated around one fixed owner
rank \(k\), and hence produce the natural ranks \(k-q\) and \(k+q\) at
depth \(q\).  In the odd PBBS application the two complementary parity
projections give (1.1); one of the two natural depth parameters is shifted
by one.  Thus an exact paired statement replaces \(q\) by \(q+1\) on that
side.  All seam counts below are then \(q\) or \(q+1\), and every displayed
Gaussian estimate and little-oh criterion is unchanged.  We suppress this
one-rank endpoint shift after recording it here.

### Lemma 1.1 (one word endpoint per antichain member)

If a literal word of length \(L\) represents every member of an antichain
\(\mathcal A\), then \(L\ge |\mathcal A|\).

#### Proof

Choose one witnessing interval for each target and map the target to the
right endpoint of its interval.  The unions of intervals with one common
right endpoint are nested as the left endpoint moves.  Two different
members of an antichain therefore cannot have the same right endpoint.
The endpoint map is injective. \(\square\)

Uniformly for \(q=O(\sqrt m)\),

\[
 {N_q\over W}
 =\prod_{j=0}^{q-1}{m-j\over m+2+j},
\tag{1.3}
\]

and Taylor expansion gives

\[
 \log {N_q\over W}
 =-{q(q+1)\over m}
   +O\!\left({q^3\over m^2}+{q\over m}\right).
\tag{1.4}
\]

Consequently, if \(q=x\sqrt m+O(1)\),

\[
 N_q=(e^{-x^2}+o(1))W.
\tag{1.5}
\]

### Corollary 1.2 (no separate Gaussian annulus)

For fixed \(a>0\), every separate word covering even one rank in
\(I_{a,b}\) has length \(\Omega_{a,b}(W)\).  In particular no separately
appended block covering the whole annulus has length \(o(W)\).

The total two-sign annulus mass is, by the Riemann-sum form of (1.4),

\[
 \sum_{q\in I_{a,b}}2N_q
 =\left(2\int_a^b e^{-x^2}\,dx+o(1)\right)W\sqrt m.
\tag{1.6}
\]

Thus the annulus contains \(\Theta(W\sqrt m)\) targets even though any
coefficient-one word has only \(W+o(W)\) positions.  Almost every position
must serve a nested family of ranks.  Separate-tail concatenation discards
exactly this endpoint reuse.

## 2. A cyclic safe chronology has a one-letter-per-owner compiler

The next lemma is independent of PBBS.  It is the literal engine used after
a successful rethreading.

Let

\[
 X_{t+1}=X_t-\{a_t\}+\{b_t\},\qquad |X_t|=k,
\tag{2.1}
\]

be a cyclic Johnson chronology of length \(M\).  Its transition support is

\[
 \sigma_t=\{a_t,b_t\}.
\tag{2.2}
\]

Call the chronology **strongly \(H\)-safe** if any two transition supports
whose cyclic edge distance is at most \(H+1\) are disjoint.  The harmless
extra one in this definition guarantees that every positive coordinate run
contains at least \(H+1\) owner states.  It also implies the usual two-sided
rank safety for every window of at most \(H\) edges.

Define the erosion letters

\[
 D_i=\bigcap_{r=0}^{H}X_{i+r}.
\tag{2.3}
\]

### Theorem 2.1 (exact cyclic erosion compiler)

For every \(0\le q\le H\),

\[
 \boxed{
 \bigcap_{r=0}^{q}X_{t+r}
 =\bigcup_{i=t+q-H}^{t}D_i,}
\tag{2.4}
\]

and

\[
 \boxed{
 \bigcup_{r=0}^{q}X_{t+r}
 =\bigcup_{i=t-H}^{t+q}D_i.}
\tag{2.5}
\]

The lower and upper sets have ranks \(k-q\) and \(k+q\), respectively.
If \(H<k\), all \(D_i\) are nonempty.  Hence the linear word

\[
 D_0,D_1,\ldots,D_{M-1},D_0,D_1,\ldots,D_{2H-1}
\tag{2.6}
\]

has length exactly \(M+2H\) and represents every lower and upper window
target through depth \(H\).

#### Proof

For an index \(i\in[t+q-H,t]\), the owner interval
\([i,i+H]\) contains \([t,t+q]\).  Therefore
\(D_i\subseteq\bigcap_{r=0}^qX_{t+r}\).

Conversely, fix a coordinate \(x\) present throughout
\([t,t+q]\).  The maximal positive owner run of \(x\) containing this
interval has at least \(H+1\) states: otherwise its insertion and removal
support edges would occur within cyclic distance at most \(H+1\).  Every
subinterval of at most \(H+1\) states inside an interval of at least
\(H+1\) states extends to an \((H+1)\)-state interval inside the same
positive run.  Thus for some

\[
 i\in[t+q-H,t]
\]

the coordinate \(x\) belongs to every owner in \([i,i+H]\), and hence to
\(D_i\).  This proves (2.4).

For (2.5), every interval \([i,i+H]\), with
\(i\in[t-H,t+q]\), meets \([t,t+q]\).  Therefore every coordinate of
\(D_i\) lies in the displayed upper union.  Conversely, if
\(x\in X_s\) for some \(s\in[t,t+q]\), extend the singleton owner
\([s,s]\) to an \((H+1)\)-state interval in its positive run.  Its start
lies in \([s-H,s]\subseteq[t-H,t+q]\), so the corresponding \(D_i\)
contains \(x\).  This proves (2.5).

In a \(q\)-edge window the supports are pairwise disjoint.  Each removal
deletes a new initial coordinate and each insertion adds a new coordinate,
giving ranks \(k-q\) and \(k+q\).  Equation (2.3) gives
\(|D_i|=k-H>0\).  Finally the longest interval on the right of (2.4)--(2.5)
has \(2H+1\) letters, so repeating the first \(2H\) cyclic letters gives
the exact linearization (2.6). \(\square\)

For several output cycles, apply (2.6) separately.  If their total owner
mass is \(M\) and their number is \(c\), the exact compiled length is

\[
                         M+2Hc.
\tag{2.7}
\]

This is the decisive distinction between a soft colour switch and a hard
run start.  A switch lying inside a strongly safe output cycle has no
separate literal charge.

## 3. Every safe seam carries a triangular annulus fan

Consider one distinguished seam edge between \(X_0\) and \(X_1\) in a
strongly \(H\)-safe chronology.  A \(q\)-edge window crosses this seam
exactly when its first edge is \(-j\), where

\[
                         0\le j\le q-1.
\tag{3.1}
\]

Thus there are exactly \(q\) crossing windows.

### Theorem 3.1 (exact seam fan)

For \(0\le j<q\le H\), put

\[
 L_{j,q}=\bigcap_{r=0}^{q}X_{-j+r},\qquad
 U_{j,q}=\bigcup_{r=0}^{q}X_{-j+r}.
\tag{3.2}
\]

Then

\[
 L_{j,q}=X_{-j}\setminus
      \{a_{-j},a_{-j+1},\ldots,a_{q-j-1}\},
\tag{3.3}
\]

\[
 U_{j,q}=X_{-j}\cup
      \{b_{-j},b_{-j+1},\ldots,b_{q-j-1}\}.
\tag{3.4}
\]

At fixed \(q\), the \(q\) lower targets are distinct and the \(q\) upper
targets are distinct.  At fixed \(j\), as \(q\) increases the lower sets
form a strictly decreasing flag and the upper sets form a strictly
increasing flag.

#### Proof

Pairwise disjointness of the support pairs says that every removal in the
window deletes a different member of its first owner and no inserted
coordinate is removed in the same window.  This proves (3.3).  The dual
argument proves (3.4).

Compare the windows starting at consecutive positions \(t,t+1\).  The
lower target from the second contains \(b_t\), whereas the first does not;
the upper target from the first contains \(a_t\), whereas the second does
not.  Hence adjacent starts give different targets, and therefore all
starts at one rank are distinct.  Increasing \(q\) deletes the next fresh
\(a\)-coordinate in (3.3) and adds the next fresh \(b\)-coordinate in
(3.4), proving strict nesting. \(\square\)

Consequently one seam supplies, in the annulus (0.2), exactly

\[
 \sum_{q\in I_{a,b}}q
 ={b^2-a^2\over2}m+O(\sqrt m)
\tag{3.5}
\]

valid targets per sign.  These are not independent rank-by-rank coupons:
they are a triangular collection of coherently nested flags.  This is the
cross-rank economy that a separate tail loses.

There is one essential caveat.  If an \(H\)-window contains several colour
switches, it belongs to the fan of each seam it crosses.  Formula (3.5) is
then an incidence count, not a count of different physical windows.  The
universal bound at depth \(q\) is

\[
 \#\{\text{windows crossing at least one of }s\text{ seams}\}
 \le \min\{M,qs\}.
\tag{3.6}
\]

This overlap is exactly why dense switching is a nonlinear cylinder
problem.

## 4. Sharp switch-capacity lower bound

Cut a cyclic owner chronology at \(s\) places.  At signed depth \(q\), let
\(\mathcal B_q^\pm\) be the targets supplied by windows wholly inside the
resulting open segments, and put

\[
 D_q^\pm=|\mathcal T_q^\pm\setminus\mathcal B_q^\pm|.
\tag{4.1}
\]

Reconnect the segments in an arbitrary new chronology.  Let \(z_q^\pm\)
be the number of remaining depth-\(q\) targets appended literally.

### Theorem 4.1 (seam-capacity inequality)

Every rethreading satisfies

\[
 \boxed{D_q^\pm\le qs+z_q^\pm.}
\tag{4.2}
\]

Consequently

\[
 \boxed{
 \sum_{q\in I_{a,b}}(D_q^-+D_q^+)
 \le 2s\sum_{q\in I_{a,b}}q
       +\sum_{q\in I_{a,b}}(z_q^-+z_q^+).}
\tag{4.3}
\]

#### Proof

Every window wholly inside one old segment is unchanged.  Thus every new
target outside \(\mathcal B_q^\pm\) must be witnessed either by a window
crossing a selected seam or by one of the \(z_q^\pm\) literal repairs.
There are at most \(qs\) crossing starts by (3.6), and one window supplies
at most one target at a fixed signed rank.  This proves (4.2); summing gives
(4.3). \(\square\)

If \(D_q^\pm\ge\delta W\) at one depth \(q=\Theta(\sqrt m)\) and
\(z_q^\pm=o(W)\), then

\[
                         s=\Omega(W/\sqrt m).
\tag{4.4}
\]

The same conclusion follows if the left side of (4.3) is
\(\Omega(W\sqrt m)\).  Therefore a positive-density Gaussian annulus
cannot be repaired by \(o(W/H)\) sparse seams.  On the other hand the
necessary \(\Theta(W/H)\) seams are still \(o(W)\).  They become expensive
only if each one is declared a hard reset.

This proves the exact economic target:

* \(\Theta(W/H)\) or slightly more **soft** switches;
* only \(o(W/H)\) hard cyclic openings; and
* the crossing windows themselves must cover a positive-density annulus.

## 5. Exact nonlinear rethreading formulation

Let \(P_1,\ldots,P_s\) be open owner segments which partition the middle
owner occurrences used by the PBBS baseline.  They may be tagged by their
old PBBS cycle and phase.  A rethreading \(\pi\) assigns every segment tail
to one segment head, using every head once.  It therefore makes a
permutation of the segments and decomposes them into \(c(\pi)\) cyclic
components.

Let \(\mathfrak P_H\) be the set of those permutations for which

1. every new tail--head step is a literal Johnson step;
2. the complete cyclic chronology, not merely every adjacent pair of
   segments, is strongly \(H\)-safe; and
3. every owner occurrence remains in exactly one output component.

The second condition is stateful.  If some segment is shorter than \(H\),
an \(H\)-window can meet several new seams, and pairwise legality of
adjacent joins is not sufficient.

For \(\pi\in\mathfrak P_H\), let \(\mathsf H_{\rm ann}(\pi)\) be the
aggregate number of targets in the chosen paired annulus which are absent
from all lower and upper windows of the rethreaded chronology.  Let
\(\mathsf H_{\rm core}(\pi)\) be the analogous number in the already
serviced inner PBBS band.

### Theorem 5.1 (in-place nonlinear low-switch compiler)

Every \(\pi\in\mathfrak P_H\) gives a literal word of length

\[
 \boxed{
 L(\pi)\le W+2Hc(\pi)
       +\mathsf H_{\rm ann}(\pi)
       +\mathsf H_{\rm core}(\pi).}
\tag{5.1}
\]

In particular, (0.7) implies \(L(\pi)=W+o(W)\).

#### Proof

Apply Theorem 2.1 separately to every output cycle.  All cycles together
use exactly the original \(W\) owner occurrences, and their cyclic
linearization costs exactly \(2Hc(\pi)\).  The resulting word represents
every target which occurs as a window in the new chronology.  Append every
remaining inner or annulus target as one literal letter.  This gives
(5.1). \(\square\)

There is a useful crude inner-band audit.  Suppose the old PBBS target map
covered every target through depth \(h\), and cut it at \(s\) positions.
Only the \(qs\) old depth-\(q\) windows crossing cuts can disappear.
Therefore, without using any favourable new crossing target,

\[
 \boxed{
 \mathsf H_{\rm core}(\pi)
 \le 2s\sum_{q=1}^{h}q=s h(h+1).}
\tag{5.2}
\]

Thus \(sh^2=o(W)\) is a sufficient provenance bound for retaining a slowly
growing inner PBBS band.  This bound is deliberately one-sided: duplicate
old witnesses and useful new windows can only improve it.

Theorem 5.1 explains the word “nonlinear.”  The old run-start objective
would charge \(2Hs\).  The correct objective charges \(2Hc(\pi)\), while
the benefit of a switch is included nonlinearly through the union of all
target sets of all windows.  A switch can simultaneously help every rank
in (3.5).

## 6. What an edge-local random matching can and cannot prove

First impose the isolated-seam hypothesis: every open segment has at least
\(2H\) edges.  Then a depth-\(H\) window crosses at most one new seam, and
legality and target service may be assigned to individual tail--head
edges.

Let \(G\) be the bipartite graph of legal tail--head joins.  For a target
\(T\) missing from the internal windows, let

\[
 E_T\subseteq E(G)
\tag{6.1}
\]

be the joins whose seam fan contains \(T\).  A perfect matching \(M\) of
\(G\) misses \(T\) exactly when \(M\cap E_T=\varnothing\).  If \(G\) is
viewed as a zero--one matrix, then for a uniformly random perfect matching

\[
 \boxed{
 \Pr(T\text{ is missed})
 ={\operatorname {per}(G-E_T)\over\operatorname {per}(G)}.}
\tag{6.2}
\]

Consequently

\[
 \boxed{
 \mathbb E\mathsf H_{\rm ann}
 =\sum_T{\operatorname {per}(G-E_T)
                    \over\operatorname {per}(G)}.}
\tag{6.3}
\]

This is the exact all-target permanent gate in the edge-local regime.

The complete compatibility case has a useful sufficient theorem.

### Lemma 6.1 (permanent avoidance bound)

Let \(\pi\) be uniform in \(S_s\).  For each row \(i\), let
\(A_i\subseteq[s]\) have cardinality at least \(d\).  If
\(d=o(s/\log s)\), then

\[
 \Pr\bigl(\pi(i)\notin A_i\text{ for every }i\bigr)
 \le \exp\bigl(-(1-o(1))d\bigr).
\tag{6.4}
\]

#### Proof

Retain exactly \(d\) permitted cells in every row and let \(B\) be the
zero--one matrix complementary these retained cells.  Every row sum of
\(B\) is \(s-d\).  Br\'{e}gman's permanent theorem gives

\[
 \operatorname {per}B
 \le ((s-d)!)^{s/(s-d)}.
\tag{6.5}
\]

Divide by \(s!\).  Stirling's formula, uniformly for \(d=o(s)\), gives

\[
 \begin{aligned}
 \log {((s-d)!)^{s/(s-d)}\over s!}
 &=s\log(1-d/s)\\
 &\quad+O\!\left({d\log s\over s}+{1\over s}\right)\\
 &=-d+O\!\left({d^2\over s}+{d\log s\over s}+{1\over s}\right).
 \end{aligned}
\tag{6.6}
\]

The error is \(o(d)\), proving (6.4). \(\square\)

### Corollary 6.2 (complete-port random rethreading)

Assume every tail may legally join every head, and all segments have length
at least \(2H\).  Suppose that, outside an exceptional family of aggregate
size \(o(W)\), every missing annulus target belongs to \(E_T\) in at least
\(d\) columns of every tail row, where

\[
                         d\ge4\log m.
\tag{6.7}
\]

Then some rethreading has aggregate annulus holes \(o(W)\) and

\[
                         c(\pi)=O(\log s).
\tag{6.8}
\]

Its literal cost above the owner baseline is \(o(W)\).

#### Proof

There are at most \(2HW\) target rows in the band.  Lemma 6.1 and (6.7)
give

\[
 \mathbb E\mathsf H_{\rm ann}
 \le o(W)+2HW\exp(-(1-o(1))d)=o(W).
\tag{6.9}
\]

A uniform permutation has expected cycle count

\[
 \mathbb Ec(\pi)=1+{1\over2}+\cdots+{1\over s}=O(\log s).
\tag{6.10}
\]

Therefore

\[
 \mathbb E\bigl(\mathsf H_{\rm ann}+2Hc(\pi)\bigr)=o(W),
\]

because \(H\log s\) is polynomial in \(m\), whereas \(W\) is
exponential.  Some permutation attains at most this expectation.
Theorem 5.1 completes the proof, after adding any \(o(W)\) inner loss.
\(\square\)

This attractive theorem cannot be invoked at the critical isolated scale.
Indeed, at one signed depth \(q\), every one of the \(s^2\) possible joins
has exactly \(q\) crossing windows.  Therefore

\[
 \boxed{
 \sum_{T\in\mathcal T_q^\pm}|E_T|=s^2q.}
\tag{6.11}
\]

If \(d_i(T)\) is the number of heads from tail row \(i\) serving \(T\),
then

\[
 \boxed{
 {1\over N_qs}\sum_{T\in\mathcal T_q^\pm}
             \sum_{i=1}^{s}d_i(T)
 ={sq\over N_q}.}
\tag{6.12}
\]

For \(q=\Theta(H)=\Theta(\sqrt m)\) and
\(s=\Theta(W/H)\), the right side is \(\Theta(1)\).  The same remains
true after restricting to any positive-density family of missing targets,
even if every available incidence is concentrated on that family.  Hence
the growing row degree (6.7) is impossible at critical isolated density.

There is no contradiction with Corollary 6.2.  To make the average degree
\(d\asymp\log m\), one would take

\[
                         s\asymp {W\log m\over H}.
\tag{6.13}
\]

But \(s\) isolated seams require at least \(2Hs\) owner edges, whereas only
\(W\) are available.  Equivalently, the average colour run in (6.13) has
length \(H/\log m<H\).  A typical \(H\)-window then crosses
\(\Theta(\log m)\) seams.  Its target is not determined by one edge
\((i,\pi(i))\), and (6.1)--(6.3) cease to be the correct model.

Thus the edge-local random matching has an exact counterterm:

\[
 \boxed{
 \text{isolated seams give only constant target degree; growing degree
 forces genuinely multi-seam windows.}}
\tag{6.14}

At constant degree, independent/permanental sampling leaves a positive
fraction of targets.  A positive result must either find a deterministic
near-factor in the critical bundle hypergraph, or use the dense multi-seam
cylinders which the edge-local model discards.

## 7. The exact dense-cylinder gate

For dense switches, retain the whole rethreading rather than assigning a
window to one seam.  If \(\pi\in\mathfrak P_H\), write

\[
 F_{t,q}^-(\pi),\qquad F_{t,q}^+(\pi)
\tag{7.1}
\]

for the two physical targets of the \(q\)-window beginning at owner start
\(t\).  These are functions of the complete ordered colour/support cylinder
met by that window.  Define

\[
 \mathsf H_{\rm ann}(\pi)
 =\sum_{q\in I_{a,b}}\sum_{\epsilon\in\{-,+\}}
   \sum_{T\in\mathcal T_q^\epsilon}
   \mathbf1_{\{F_{t,q}^\epsilon(\pi)\ne T\ \forall t\}}.
\tag{7.2}
\]

The product in the last indicator is a high-degree function of the colour
switches.  Pair marginals, one-seam degrees, and Walsh covariances of fixed
order do not determine it.

### Theorem 7.1 (nonlinear cylinder-law criterion)

Suppose there is a probability law \(\mu\) supported on
\(\mathfrak P_H\) such that

\[
 \mathbb E_\mu\mathsf H_{\rm ann}=o(W),
 \qquad
 H\mathbb E_\mu c(\pi)=o(W),
 \qquad
 \mathbb E_\mu\mathsf H_{\rm core}=o(W).
\tag{7.3}
\]

Then one deterministic rethreading gives a word of length \(W+o(W)\)
covering the old PBBS core and the whole annulus.

#### Proof

Take expectations in (5.1).  The expected excess is \(o(W)\), so at least
one member of the support of \(\mu\) has excess \(o(W)\). \(\square\)

The exact obstruction is the negation of (7.3).  For example, a family
\(\mathcal A\) of annulus targets and a constant \(\delta>0\) such that

\[
 \bigl|\mathcal A\setminus
   \{F_{t,q}^\epsilon(\pi):t,q,\epsilon\}\bigr|
 \ge\delta W
\tag{7.4}
\]

for every owner-valid \(\pi\in\mathfrak P_H\) with
\(c(\pi)=o(W/H)\) is a literal positive-density cross-parent cut.  No such
cut is presently proved.

Conversely, checking only the expected multiplicity of every target is not
enough.  If \(Z_T(\pi)\) is its number of realizing windows, the relevant
quantity is

\[
 \boxed{
 \sum_T\Pr_\mu(Z_T=0),}
\tag{7.5}
\]

not \(\sum_T\mathbb E Z_T\), nor any fixed finite list of moments.  In the
isolated regime (7.5) becomes the permanent ratio (6.3).  In the dense
regime it is the corresponding all-order colour-cylinder avoidance
functional.

This is the precise nonlinear low-switch target.  It permits
\(s\asymp W\log m/H=o(W)\) colour switches, with a typical \(H\)-window
reading \(\Theta(\log m)\) successive colours, while requiring only
\(o(W/H)\) hard output components.  Such a law would exploit the very
cross-seam windows which sparse-seam quarantine throws away.

## 8. PBBS-specific audit and remaining theorem

The PBBS owner factor supplies the right raw resources:

1. its owner occurrences already have total mass \(W\);
2. cutting at the relevant short residences is the established source of
   internally safe one-sided pieces (the strong two-sided condition of
   Section 2 remains part of the rethreading gate);
3. the all-depth PBBS support theorem supplies the correct target values
   before literalization; and
4. the unconditional sub-Gaussian compiler gives an inner band which can
   absorb the crude loss (5.2) whenever \(sh^2=o(W)\).

What it does not currently supply is the rethreading law in Theorem 7.1.
In particular, equality of normalized packet ports is insufficient.  Those
ports omit the two cores and the boundary owners, so equality does not imply
a literal Johnson successor.  If the carrier and actual successor are added
to the port, the resulting fixed-carrier maximal-run interface has no
nontrivial joins.  Thus the complete-port hypothesis of Corollary 6.2 is a
genuine missing owner-support substitution, not an already proved PBBS
fact.

There is a second, independent issue.  In the dense regime a legality test
on one proposed seam does not control a window which crosses several
seams.  The controller state must retain the last \(H\) physical supports
with their ages.  Any proposed colouring which checks only adjacent colour
pairs is therefore incomplete.

The portal-tree Johnson walk does not bypass this issue.  It does make
every PBBS target window consecutive with only \(O(HB)\) repeated owner
steps, but its forward/backward portal excursions immediately retrace
support pairs.  Hence it violates strong \(H\)-safety and the erosion
identities (2.4)--(2.5).  It is a chronology theorem, not a literal OR
compiler.  The present rethreading gate explicitly retains the missing
delay-\(H\) condition.

The exact surviving PBBS assertion is the following.

> **Gaussian-annulus nonlinear rethreading theorem — unproved.**  For every
> fixed \(0<a<b<A\), cut and rethread the complete PBBS middle-owner
> occurrence factor so that:
>
> 1. all owners remain exact and the output chronology is globally strongly
>    \(H\)-safe;
> 2. the number of colour switches is \(o(W)\), while the number of output
>    cycles is \(o(W/H)\);
> 3. the aggregate number of missing targets in the paired annulus
>    \(I_{a,b}\) is \(o(W)\); and
> 4. for a slowly growing inner cutoff \(h\), either \(sh^2=o(W)\) or a
>    chain-aligned reserve restores the affected inner targets at \(o(W)\)
>    cost.

Theorem 5.1 would then give the annulus at \(o(W)\) incremental cost over
the PBBS baseline.  Proving the assertion for successive fixed annuli and
diagonalizing the outer radius to infinity would meet the factor-blind
product-SCD tail where its cost becomes \(o(W)\).

The alternative negative result is now equally explicit: exhibit a
positive-density target family satisfying (7.4), or prove that every
owner-valid stateful colour-cylinder law has either

\[
 H\mathbb E c=\Omega(W)
 \quad\text{or}\quad
 \sum_T\Pr(Z_T=0)=\Omega(W).
\tag{8.1}
\]

Neither the boundary antichain nor the old \(Hs\) seam ledger proves
(8.1).  The antichain forces reuse; the seam-fan calculation shows that
reuse has exactly enough capacity.  The remaining question is the integral
alignment of those triangular fans under the actual PBBS owner and
\(H\)-memory constraints.

## 9. Logical boundary

The proved chain is

\[
 \boxed{
 \begin{gathered}
 \text{owner-valid globally safe rethreading}\\
 +\ \mathsf H_{\rm ann}=o(W)\\
 +\ c=o(W/H)\\
 +\ \mathsf H_{\rm core}=o(W)
 \end{gathered}
 \Longrightarrow
 L=W+o(W).}
\tag{9.1}
\]

The exact quantitative constraints are

\[
 \boxed{s=\Omega(W/H)\quad\text{if the annulus has positive-density
 internal deficit},}
\tag{9.2}
\]

and

\[
 \boxed{
 \text{one safe seam supplies }q\text{ targets at depth }q
 \text{ and }\Theta(H^2)\text{ over a Gaussian annulus}.}
\tag{9.3}
\]

Thus the viable coefficient-one regime is neither a separate tail nor a
sparse-seam colouring.  It is a nonlinear rethreading with
\(\Theta(W/H)\) soft switches, few hard components, and target-useful
cross-seam cylinders.  The exact remaining discrepancy is the all-order
PBBS cylinder avoidance sum (7.5), together with owner-valid stateful
realizability.
