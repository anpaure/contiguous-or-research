# Predecessor rigidity, an exact different-target ladder, and the reduced-scale seam cut

Date: 2026-07-27

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

## 0. Exact outcome

Let

\[
                         W=\binom{2m}{m}.
\tag{0.1}
\]

This note resolves the local two-letter question and tests the surviving
multi-edge mechanism at the reduced handoff scale.

### The negative theorem

For every two-sided radius-\(H\) safe bridge path

\[
               v_0\longrightarrow v_1\longrightarrow\cdots
               \longrightarrow v_k=w,
               \qquad k\le H,
\tag{0.2}
\]

the target cache contains the \(k\) departures in reverse order.  The
source owner, the target full state, and \(k\) therefore reconstruct the
entire source lower word.  Hence two equal-owner states with distinct
lower roots cannot coalesce at one full target state in at most \(H\)
edges.

Consequently:

1. a two-letter bypass into an unchanged suffix is impossible;
2. every width-\(\le H\) unary seam which changes finitely many initial
   targets and then rejoins the unchanged full suffix is impossible; and
3. a two-letter shortcut to a more distant old suffix state can occur only
   at old offset at least \(2H-2\).

The theorem is insensitive to provider powers and to the promotion/rotor
choice.

### The sharp local escape

The obstruction is sharp for a genuinely different target history.
Suppose two full radius-\(H\) states have one owner and one upper cache,
but their lower words differ by the adjacent transposition in slots
\(q,q+1\), where

\[
                         1\le q<H,\qquad m\ge3H+1.
\tag{0.3}
\]

There are two exact bridge paths which:

1. push the lower transposition to slots \(1,2\);
2. pass through a two-edge Johnson diamond;
3. emerge with an upper-cache transposition in slots \(1,2\);
4. push that transposition through the full cache; and
5. coalesce as identical full states.

Every transition on either route can have a globally fresh support.  The
routes are therefore strictly two-sided \(H\)-safe and their signed
targets are injective along each route.  Their exact common length is

\[
                              K=q+H+1.
\tag{0.4}
\]

For controlled depths \(q\le s\le d\le H\), if
\(\Delta_s^-\) and \(\Delta_s^+\) are the route-to-route lower and upper
target occurrence derivatives, then

\[
 \boxed{
 \sum_{s=q}^{d}
 \left(\|\Delta_s^-\|_1+\|\Delta_s^+\|_1\right)
 =2(d-q+2).}
\tag{0.5}
\]

The middle-owner occurrence derivative has \(L^1\)-norm exactly \(2\).
Thus the first legal local escape has linear, rather than quadratic,
all-depth displacement.

This is an exact ordered-state/path theorem, not yet a theorem about two
fixed global SCDs.  Its initial adjacent transposition extends to a second
full SCD exactly on unions of cycles of an alternate-corner map.  On such
a cycle the endpoint provider powers are exactly \(0,1\).  What is not
proved is simultaneous SCD completion of every intermediate ladder state,
or global collision-free packing of many ladders.

### The reduced-scale decision

Put

\[
 H^2/m=\log\log m+o(1),\qquad H=o(m^{2/3}),
 \qquad r=\Theta(\log m).
\tag{0.6}
\]

Then

\[
 N_H:=\binom{2m}{m-H}
       =(1+o(1))\frac{W}{\log m},
\qquad
 \frac{N_H}{W/H}
       =(1+o(1))\frac{H}{\log m}\longrightarrow\infty.
\tag{0.7}
\]

Assume the reduced handoff has \(P=(1+o(1))N_H\) retained pieces, each of
length \(O(r)<H\), and the goal is \(p=o(W/H)\) final components.

Then:

1. at least \((1-o(1))P\) component fusions are necessary;
2. after crediting the deleted prefix of one receiving piece per fusion,
   a coefficient-one compiler has only \(O(W)\) gross bridge mass, hence
   only \(O(\log m)\) new entries per fusion on average;
3. all but \(o(P)\) of its unary bridges consequently have width at most
   \(H\); and
4. predecessor-root rigidity forbids every such bridge if it rejoins an
   unchanged retained suffix.

Therefore **no independently charged unary exact-suffix seam architecture
can meet coefficient one at the reduced scale**.

In particular, inserting one \(K=\Theta(H)\) ladder independently at
each fusion would cost

\[
                 \Theta(HN_H)
                 =\Theta\!\left(\frac{WH}{\log m}\right)
                 =\omega(W).
\tag{0.8}
\]

An independently paid \(H\)-cost gadget family whose total **gross**
insertion is \(o(W)\) can survive only if its average component reduction
is

\[
                         \omega\!\left(\frac{H}{\log m}\right).
\tag{0.9}
\]

Thus the local ladder does not by itself solve the reduced handoff.  It
can contribute only if its \(H\) transitions are absorbed into retained
path mass, if many defects are pipelined in one global trajectory, or if
an independently paid \(H\)-cost packet has average reduction
\(\omega(H/\log m)\).  Pairwise different-target half-splice
switches are impossible because consecutive-rank containment is
\(C_4\)-free; the first zero-entry algebraic endpoint trade is a
three-tail \(C_6\).

The exact surviving gate is therefore global and multiway, not a longer
independently paid unary seam.

## 1. Full states and exact bridge dynamics

A full radius-\(H\) state is written

\[
 v=(X;\boldsymbol\alpha(v),\boldsymbol\beta(v);
       \mathcal L(v),\mathcal R(v)),
\tag{1.1}
\]

where

\[
 X\in\binom{[2m]}m,
\qquad
 \boldsymbol\alpha(v)
   =(\alpha_1(v),\ldots,\alpha_H(v)),
\tag{1.2}
\]

\[
 \boldsymbol\beta(v)
   =(\beta_1(v),\ldots,\beta_H(v)).
\tag{1.3}
\]

The lower and upper residual blocks are

\[
 \mathcal L(v)
 =X\setminus\{\alpha_1(v),\ldots,\alpha_H(v)\},
\tag{1.4}
\]

\[
 \mathcal R(v)
 =[2m]\setminus
 \left(X\cup\{\beta_1(v),\ldots,\beta_H(v)\}\right).
\tag{1.5}
\]

For \(0\le s\le H\), the native signed targets are

\[
 L_s(v)
 =X\setminus\{\alpha_1(v),\ldots,\alpha_s(v)\},
\tag{1.6}
\]

\[
 U_s(v)
 =X\cup\{\beta_1(v),\ldots,\beta_s(v)\}.
\tag{1.7}
\]

Consider one owner-changing bridge

\[
                         v\longrightarrow v',
\qquad
 X(v')=X(v)-a+b.
\tag{1.8}
\]

The exact FIFO/cache normal form is

\[
                         a=\alpha_1(v),
\tag{1.9}
\]

\[
 \boldsymbol\alpha(v')
 =(\alpha_2(v),\ldots,\alpha_H(v),x),
\qquad x\in\mathcal L(v),
\tag{1.10}
\]

and

\[
 \boldsymbol\beta(v')
 =\bigl(a,\boldsymbol\beta(v)\setminus e\bigr),
\tag{1.11}
\]

with the unaffected cache entries retaining their order.  Here

\[
 e=
 \begin{cases}
 b,&b\in\{\beta_1(v),\ldots,\beta_H(v)\}
       \quad\text{(promotion)},\\
 \beta_H(v),&b\in\mathcal R(v)
       \quad\text{(genuine rotor)}.
 \end{cases}
\tag{1.12}
\]

For a genuine rotor the residual updates are

\[
 \mathcal L(v')=\mathcal L(v)-x+b,
\qquad
 \mathcal R(v')=\mathcal R(v)-b+\beta_H(v).
\tag{1.13}
\]

A transition has support \(\{a,b\}\).  A path is **two-sided safe through
radius \(H\)** when the supports in every interval of at most \(H\)
transitions are pairwise disjoint.  This is equivalent to sharp lower and
upper ranks in every protected interval.  Rank safety alone does not assert
that targets at different starting positions are injective.  If all
transition supports on a path are globally pairwise disjoint, then the
path is two-sided safe through every radius not exceeding its length; the
ladder below proves its stronger target injectivity separately by a fresh
marker.

## 2. Multistep inverse memory

Consider a two-sided radius-\(H\) safe path

\[
                 v_0\longrightarrow v_1\longrightarrow\cdots
                 \longrightarrow v_k=w,
\qquad 1\le k\le H.
\tag{2.1}
\]

Write

\[
 X=X(v_0),\qquad Y=X(w),
\tag{2.2}
\]

and

\[
 X(v_t)=X(v_{t-1})-a_t+b_t.
\tag{2.3}
\]

### Lemma 2.1 (geodesic owner motion)

The \(2k\) coordinates

\[
                         a_1,b_1,\ldots,a_k,b_k
\tag{2.4}
\]

are distinct,

\[
 \{a_1,\ldots,a_k\}\subseteq X,
\qquad
 \{b_1,\ldots,b_k\}\subseteq[2m]\setminus X,
\tag{2.5}
\]

and

\[
 Y=X-\{a_1,\ldots,a_k\}+\{b_1,\ldots,b_k\}.
\tag{2.6}
\]

Consequently

\[
                              d_J(X,Y)=k.
\tag{2.7}
\]

#### Proof

The whole path has at most \(H\) transitions, so safety makes all of its
transition supports pairwise disjoint.  A departure \(a_t\) which was not
in \(X\) would have to be an earlier arrival, repeating a coordinate.  An
arrival \(b_t\) which was in \(X\) would have to be an earlier departure
before it could be absent, again repeating a coordinate.  This proves
(2.5), and telescoping (2.3) gives (2.6).  Both owner differences have
size \(k\), proving (2.7). \(\square\)

### Lemma 2.2 (reverse departure stack)

The first \(k\) entries of the terminal cache are

\[
 \boxed{
 (\beta_1(w),\ldots,\beta_k(w))
 =(a_k,a_{k-1},\ldots,a_1).}
\tag{2.8}
\]

Moreover,

\[
 \alpha_i(v_0)=\beta_{k+1-i}(w)
 \qquad(1\le i\le k),
\tag{2.9}
\]

\[
 \alpha_{k+j}(v_0)=\alpha_j(w)
 \qquad(1\le j\le H-k).
\tag{2.10}
\]

#### Proof

At step \(t\), the departure \(a_t\) is prepended to the cache.  No later
step can remove an earlier \(a_s\): using \(a_s\) as a later arrival would
repeat a transition coordinate inside the protected path.  Since
\(k\le H\), none of these \(k\) prepended entries is evicted from the
length-\(H\) cache.  This proves (2.8).  The FIFO rule (1.10), iterated
\(k\) times, gives (2.9)--(2.10). \(\square\)

For \(0\le s\le H\), define

\[
 D_{s,k}(w)=
 \begin{cases}
 \varnothing,&s=0,\\[1mm]
 \{\beta_{k-s+1}(w),\ldots,\beta_k(w)\},&1\le s\le k,\\[1mm]
 \{\beta_1(w),\ldots,\beta_k(w)\}
 \mathbin{\dot\cup}
 \{\alpha_1(w),\ldots,\alpha_{s-k}(w)\},&k<s\le H.
 \end{cases}
\tag{2.11}
\]

### Theorem 2.3 (all-depth predecessor reconstruction)

For every \(0\le s\le H\),

\[
 \boxed{
                         L_s(v_0)=X\setminus D_{s,k}(w).}
\tag{2.12}
\]

For \(k\le s\le H\), this has the target-set-only form

\[
 \boxed{
 L_s(v_0)
 =L_{s-k}(w)\setminus(Y\setminus X).}
\tag{2.13}
\]

Thus \(X\), \(w\), and \(k\) determine the entire source lower word.

#### Proof

Equations (2.9)--(2.10) reconstruct the ordered source word as

\[
 \boldsymbol\alpha(v_0)
 =
 \bigl(
 \beta_k(w),\beta_{k-1}(w),\ldots,\beta_1(w),
 \alpha_1(w),\ldots,\alpha_{H-k}(w)
 \bigr).
\tag{2.14}
\]

Taking its first \(s\) entries proves (2.11)--(2.12).

For \(s\ge k\), equations (2.6) and (2.10) give

\[
 L_{s-k}(w)
 =L_s(v_0)\mathbin{\dot\cup}\{b_1,\ldots,b_k\}.
\tag{2.15}
\]

The last set is \(Y\setminus X\), proving (2.13). \(\square\)

### Theorem 2.4 (bounded confluence rigidity)

Let \(v,v'\) be two full radius-\(H\) states with the same owner \(X\).
Suppose each has a two-sided radius-\(H\) safe bridge path of length at
most \(H\) to one identical full target state \(w\).  Then the two path
lengths agree and

\[
                         \boldsymbol\alpha(v)
                         =\boldsymbol\alpha(v').
\tag{2.16}
\]

In particular,

\[
                         L_s(v)=L_s(v')
 \qquad(0\le s\le H).
\tag{2.17}
\]

#### Proof

Lemma 2.1 says that either path length equals
\(d_J(X,X(w))\); hence the lengths agree.  Theorem 2.3 reconstructs the
same source word from the same data. \(\square\)

## 3. Exact-suffix seams

Let two SCD collars have common active owner image, and write

\[
 \rho=\mu_1^{-1}\mu_0,
\qquad
 \mu_1(\rho T)=\mu_0(T).
\tag{3.1}
\]

Put

\[
                         v=\omega_0(T),
\qquad
                         u=\omega_1(\rho T).
\tag{3.2}
\]

Then \(v,u\) have the same middle owner, while their lower entrance roots
are \(T,\rho T\).

### Corollary 3.1 (no bounded exact-suffix bypass)

Assume \(T\ne\rho T\).  If an unchanged colour-one suffix goes from
\(u\) to a full state \(w\) in \(k\le H\) transitions, there is no
two-sided radius-\(H\) safe path of any length at most \(H\) from \(v\)
to that same \(w\).

#### Proof

The old and hypothetical new paths start at the same owner and end at the
same owner.  Lemma 2.1 forces both lengths to be the same Johnson
distance.  Theorem 2.4 would then give \(T=\rho T\). \(\square\)

For \(k=1\), this recovers the one-letter predecessor-root obstruction.
For \(k=2\), it rules out the proposed two-letter bypass.  It also rules
out every modification which changes several initial targets but rejoins
one identical full state of the old suffix within \(H\) transitions.

Provider powers do not appear in the proof.  In particular, replacing
every provider by a bounded power of \(\rho\) does not help.

### Proposition 3.2 (far-suffix metric bound)

Suppose the old route from \(u\) to \(w\) has length \(K>H\), every
\(H\)-window on it is safe, and a new safe route from \(v\) to \(w\) has
length \(\ell\le H\).  Then

\[
                              K\ge2H-\ell.
\tag{3.3}
\]

In particular, a two-letter shortcut can first meet an old suffix only at
offset

\[
                              K\ge2H-2.
\tag{3.4}
\]

#### Proof

After the first \(H\) old transitions, Lemma 2.1 puts the current owner at
Johnson distance \(H\) from the common source owner.  Each of the
remaining \(K-H\) transitions can reduce that distance by at most one.
Hence

\[
 d_J(X,X(w))\ge H-(K-H)=2H-K.
\tag{3.5}
\]

The new \(\ell\)-edge safe route is geodesic by Lemma 2.1, so its endpoint
distance is \(\ell\).  Rearranging gives (3.3). \(\square\)

This metric bound does not prove existence at offset \(2H-\ell\).  It
only shows that changing to a later old target cannot turn a two-letter
seam into a local repair.

## 4. The exact lower-to-upper defect ladder

We now show that the confluence obstruction becomes false immediately
after one allows a different target history of length greater than the
memory radius.

For \(1\le j<H\), a pair of states is of type \(L_j(a,c)\) if:

1. the two owners agree;
2. the two upper cache words and both residual blocks agree; and
3. for a common prefix \(P\) of length \(j-1\) and a common suffix \(Q\),

\[
 \boldsymbol\alpha^A=(P,a,c,Q),
\qquad
 \boldsymbol\alpha^B=(P,c,a,Q).
\tag{4.1}
\]

It is of type \(U_j(a,c)\) if the owners, lower words, and residual data
agree, while

\[
 \boldsymbol\beta^A=(P,c,a,Q),
\qquad
 \boldsymbol\beta^B=(P,a,c,Q),
\qquad |P|=j-1.
\tag{4.2}
\]

At the outer boundary, type \(U_H(a,c)\) means that the first \(H-1\)
cache entries agree and

\[
 \boldsymbol\beta^A=(P,c),\qquad
 \boldsymbol\beta^B=(P,a),
\tag{4.3}
\]

\[
 \mathcal R^A=\mathcal R_0\cup\{a\},
\qquad
 \mathcal R^B=\mathcal R_0\cup\{c\}.
\tag{4.4}
\]

Thus the exchanged coordinate has crossed from the ordered cache into
the unordered upper residual.

### Lemma 4.1 (lower transport)

For \(2\le j<H\), one common fresh genuine rotor sends an \(L_j\) pair
to an \(L_{j-1}\) pair.

#### Proof

The first lower entry is common, so both routes have the same departure.
Choose one common arrival from the common upper residual and one common
append letter from the common lower residual.  Equations
(1.10)--(1.13) give the same owner, cache, and residual updates on the two
routes, while the lower adjacent transposition shifts one slot to the
left. \(\square\)

### Lemma 4.2 (the two-edge transfer diamond)

An \(L_1(a,c)\) pair admits two two-edge genuine-rotor routes to a
\(U_1(a,c)\) pair.  The two intermediate owners are distinct, but the
intermediate lower and upper targets agree at every positive depth.

#### Proof

Write the common owner as \(Z\), the common initial cache as \(B\), and

\[
 \boldsymbol\alpha^A=(a,c,Q),
\qquad
 \boldsymbol\alpha^B=(c,a,Q).
\tag{4.5}
\]

Choose two common fresh arrivals \(y,z\) in that order and two common
fresh append letters.  Route \(A\) departs \(a,c\), while route \(B\)
departs \(c,a\).  After the first edge,

\[
 X_A=Z-a+y,\qquad
 \boldsymbol\alpha_A=(c,Q,x),
\qquad
 \boldsymbol\beta_A=(a,B^-),
\tag{4.6}
\]

\[
 X_B=Z-c+y,\qquad
 \boldsymbol\alpha_B=(a,Q,x),
\qquad
 \boldsymbol\beta_B=(c,B^-).
\tag{4.7}
\]

For every positive depth \(s\),

\[
 L_s(A)=L_s(B),
\qquad
 U_s(A)=U_s(B).
\tag{4.8}
\]

Indeed the lower target on either side removes both \(a,c\), together
with the same first \(s-1\) entries of \(Q\), and contains \(y\).  The
upper target on either side restores the missing departure \(a\) or \(c\)
at its first cache position and again contains \(y\).

After the second edge, both owners equal

\[
                         Z-\{a,c\}+\{y,z\},
\tag{4.9}
\]

the lower words and residual blocks agree, and

\[
 \boldsymbol\beta^A=(c,a,B^{--}),
\qquad
 \boldsymbol\beta^B=(a,c,B^{--}).
\tag{4.10}
\]

This is \(U_1(a,c)\). \(\square\)

### Lemma 4.3 (upper transport and fresh flush)

For \(1\le j\le H-2\), one common fresh genuine rotor sends a \(U_j\)
pair to a \(U_{j+1}\) pair.  One further common rotor sends
\(U_{H-1}\) to \(U_H\).  From the boundary state (4.3)--(4.4), one common
fresh genuine rotor coalesces the routes as identical full states.

#### Proof

While \(j\le H-2\), the cache tails agree.  Prepending the common departure
shifts the adjacent cache transposition one slot to the right, and dropping
the common last cache entry gives the same residual update.

At \(U_{H-1}\), the exchanged letters occupy the last two cache slots.
The next common rotor drops different last entries.  It leaves the first
\(H-1\) cache entries common and puts the dropped exchanged letters in the
opposite residual blocks, giving (4.3)--(4.4).

Now choose a common fresh arrival \(z\in\mathcal R_0\) and let \(g\) be
the common departure.  The two genuine rotors give

\[
 \boldsymbol\beta'=(g,P),
\tag{4.11}
\]

\[
 \mathcal R'
 =(\mathcal R_0\setminus\{z\})\cup\{a,c\},
\tag{4.12}
\]

\[
 X'=X-g+z
\tag{4.13}
\]

on both routes.  The lower word and lower residual undergo the same
update, so the full states coincide. \(\square\)

### Theorem 4.4 (full-history different-target ladder)

Assume

\[
 H\ge2,\qquad 1\le q<H,\qquad m\ge3H+1.
\tag{4.14}
\]

Every \(L_q(a,c)\) pair admits two full-state paths which coalesce after
exactly

\[
 \boxed{
                         K=(q-1)+2+H=q+H+1}
\tag{4.15}
\]

transitions.  The transition supports on either route may be chosen
globally pairwise disjoint.  Hence:

1. each route is two-sided safe through radius \(H\);
2. all middle owners on one route are distinct; and
3. for every \(1\le s\le H\), the lower and upper depth-\(s\) targets
   are injective along that route.

#### Proof

Use Lemma 4.1 \(q-1\) times, Lemma 4.2 once, and Lemma 4.3 through the
full cache and final flush.  This gives (4.15).

For an explicit supply count, let \(K=q+H+1\le2H\).  Choose:

1. the \(H\) initial lower-word letters and \(K\) future append letters
   distinctly in the initial owner;
2. the \(H\) initial cache letters and all required fresh arrivals
   distinctly outside the initial owner.

Both initial residual blocks have size \(m-H\ge2H+1\), so these choices
are possible.  Use common append and arrival schedules on the two routes.
At the diamond, only the order of the two departures \(a,c\) differs.
Every transition coordinate on either route is then used exactly once.

Let \(\mathcal Y\) be the set of scheduled arrival letters.  After \(t\)
edges, exactly the first \(t\) arrivals lie in the current owner; none is
ever a departure or a cache letter.  Therefore, at every fixed positive
depth \(s\),

\[
 |X(v_t)\cap\mathcal Y|
 =|L_s(v_t)\cap\mathcal Y|
 =|U_s(v_t)\cap\mathcal Y|
 =t.
\tag{4.16}
\]

This strictly increasing marker proves owner and signed-target
injectivity along each route. \(\square\)

The theorem constructs legal refined-state paths.  It does not assert
that all these refined states already occur in two prescribed full SCDs.

## 5. Exact target derivative of the ladder

Let

\[
 \mathcal P_A=(v^A_0,\ldots,v^A_K),
\qquad
 \mathcal P_B=(v^B_0,\ldots,v^B_K)
\tag{5.1}
\]

be the two routes of Theorem 4.4.  For a signed depth \(s\), define the
occurrence histograms

\[
 h_s^-(\mathcal P)
 =\sum_{t=0}^{K} e_{L_s(v_t)},
\qquad
 h_s^+(\mathcal P)
 =\sum_{t=0}^{K} e_{U_s(v_t)},
\tag{5.2}
\]

and

\[
 \Delta_s^\pm
 =h_s^\pm(\mathcal P_A)-h_s^\pm(\mathcal P_B).
\tag{5.3}
\]

### Lemma 5.1 (one-depth support of an ordered transposition)

At an \(L_j\) pair, all upper targets agree and the lower targets differ
only at depth \(j\).  At a \(U_j\) pair, all lower targets agree and the
upper targets differ only at depth \(j\).  At the intermediate state of
the transfer diamond, every positive-depth signed target agrees.

#### Proof

An adjacent transposition changes exactly the one prefix which contains
its first letter but not its second.  This proves the \(L_j\) and \(U_j\)
statements.  The diamond statement is (4.8). \(\square\)

### Theorem 5.2 (exact controlled displacement)

For \(q\le d\le H\),

\[
 \boxed{
 \sum_{s=q}^{d}
 \left(\|\Delta_s^-\|_1+\|\Delta_s^+\|_1\right)
 =2(d-q+2).}
\tag{5.4}
\]

Across all depths \(1\le s\le d\),

\[
 \boxed{
 \sum_{s=1}^{d}
 \left(\|\Delta_s^-\|_1+\|\Delta_s^+\|_1\right)
 =2(q+d).}
\tag{5.5}
\]

The middle-owner occurrence derivative has \(L^1\)-norm exactly \(2\).

#### Proof

Before the transfer diamond, the paired states have types

\[
                         L_q,L_{q-1},\ldots,L_1.
\tag{5.6}
\]

After it, they have types

\[
                         U_1,U_2,\ldots,U_H,
\tag{5.7}
\]

followed by their common endpoint.  Lemma 5.1 shows that the controlled
range \(q,\ldots,d\) sees exactly:

1. one differing lower occurrence, at the initial \(L_q\); and
2. one differing upper occurrence at each of
   \(U_q,U_{q+1},\ldots,U_d\).

There are \(d-q+2\) such occurrence pairs.  Each replacement of one target
by a distinct target has \(L^1\)-norm two.  The marker (4.16) prevents a
target from one time cancelling a target from another time, proving
(5.4).  Over all depths through \(d\), the \(q\) lower and \(d\) upper
occurrences give (5.5).

The owners agree at every paired time except the first diamond
intermediate.  Those two owners are distinct, so the owner derivative is
one positive and one negative unit. \(\square\)

Equations (5.4)--(5.5) are assigned-column displacement identities, not
missing-hole lower bounds.  In a global packet, derivatives from different
ladders may cancel or land in deliberately vacated columns.

## 6. Exact endpoint completion in a second SCD

The initial \(L_q\) pair has a clean global SCD interpretation.

Fix a full SCD \(\mathscr D_0\).  For every chain of radius at least
\(q+1\), write its three consecutive lower vertices around depth \(q\) as

\[
 R\subset T\subset P,
\tag{6.1}
\]

where

\[
 |R|=m-q-1,\qquad |T|=m-q,\qquad |P|=m-q+1.
\tag{6.2}
\]

There are distinct coordinates \(a,c\) such that

\[
                         T=R+c,
\qquad
                         P=R+\{a,c\}.
\tag{6.3}
\]

Define the partial alternate-corner map

\[
 \boxed{
                         f_q(T)=R+a.}
\tag{6.4}
\]

### Theorem 6.1 (alternate-corner cycle criterion)

Let \(I\) be a family of eligible rank-\((m-q)\) vertices.  Replace
\(T\) by \(f_q(T)\) in the \(\mathscr D_0\)-chain containing \(T\), for
every \(T\in I\), and change no other Boolean vertex.

The resulting chains form a second full SCD \(\mathscr D_1\) if and only
if

\[
                         f_q(I)=I.
\tag{6.5}
\]

Equivalently, \(I\) is a union of directed cycles of the partial
functional graph of \(f_q\).

#### Proof

For each \(T\),

\[
                         R\subset f_q(T)\subset P
\tag{6.6}
\]

are saturated containments, so each modified chain is still a symmetric
chain.  Every rank except \(m-q\) is unchanged.  At rank \(m-q\), the
old selected family \(I\) is replaced by \(f_q(I)\).  The chains still
partition that rank exactly if and only if \(f_q\) restricts to a
permutation of \(I\), which for finite \(I\) is equivalent to (6.5).
\(\square\)

For a full radius-\(H\) application, restrict \(I\) to chains of radius at
least \(H\).

Index both decompositions by their rank-\((m-q)\) entrance roots.  Put

\[
                         \rho=f_q\quad\text{on }I,
\tag{6.7}
\]

and let \(\rho\) be the identity off the trade.  Then

\[
                         \mu_1(\rho T)=\mu_0(T).
\tag{6.8}
\]

### Corollary 6.2 (endpoint provider powers)

On the traded root family,

\[
 \boxed{
 \phi_{q,-}=\operatorname{id}=\rho^0.}
\tag{6.9}
\]

For every native lower depth \(s>q\),

\[
 \boxed{
 \phi_{s,-}=\rho,}
\tag{6.10}
\]

and for every native upper depth,

\[
 \boxed{
 \phi_{s,+}=\rho.}
\tag{6.11}
\]

Thus the endpoint pair has exact provider exponents \(0,1\).

#### Proof

The new chain indexed by \(\rho T=f_q(T)\) is the old chain indexed by
\(T\), with only its depth-\(q\) lower target changed.  Hence the
depth-\(q\) target itself remains its own provider under entrance-root
indexing, while every unchanged target on that old chain is now provided
at root \(\rho T\). \(\square\)

The cycle criterion is exact but does not prove that the functional graph
has positive cycle density.  More importantly, it supplies only the
initial \(L_q\) pairs.  The following remain unproved:

1. simultaneous placement of all intermediate \(L_j,U_j\) states in two
   fixed SCDs;
2. compensation of the one changed intermediate owner;
3. collision-free packing against retained background columns; and
4. an \(O(N_H)\)-sized or denser family of disjoint full histories.

## 7. Pairwise half-splice rigidity and the first multiway trade

The state ladder is unary but long.  A different escape is to permute
whole path tails without inserting intermediate states.

Let

\[
 R_i\in\binom{[2m]}{m-1},
\qquad
 X_j\in\binom{[2m]}m.
\tag{7.1}
\]

A radius-preserving half-splice may attach lower tail \(i\) to middle
head \(j\) only if

\[
                              R_i\subset X_j.
\tag{7.2}
\]

### Lemma 7.1 (consecutive containment is \(C_4\)-free)

There are no distinct \(R_1,R_2\) and distinct \(X_1,X_2\) satisfying

\[
                         R_i\subset X_j
 \qquad(i,j\in\{1,2\}).
\tag{7.3}
\]

#### Proof

Both \(R_1,R_2\) would lie in \(X_1\cap X_2\).  Since the distinct
\(m\)-sets \(X_1,X_2\) have intersection of size at most \(m-1\), that
intersection cannot contain two distinct \((m-1)\)-sets. \(\square\)

Hence two tail assignments cannot be cross-swapped.  Every nontrivial
matching trade moves at least three tails.

The bound is sharp algebraically.  Fix

\[
 K\in\binom{[2m]}{m-2}
\tag{7.4}
\]

and distinct \(a,b,c\notin K\).  Put

\[
 R_a=K+a,\quad R_b=K+b,\quad R_c=K+c,
\tag{7.5}
\]

\[
 X_{ab}=K+a+b,\quad
 X_{bc}=K+b+c,\quad
 X_{ca}=K+c+a.
\tag{7.6}
\]

Then

\[
 R_a-X_{ab}-R_b-X_{bc}-R_c-X_{ca}-R_a
\tag{7.7}
\]

is an alternating \(C_6\).  Its two matchings are

\[
 \mathcal M_0
 =\{R_aX_{ab},R_bX_{bc},R_cX_{ca}\},
\tag{7.8}
\]

\[
 \mathcal M_1
 =\{R_bX_{ab},R_cX_{bc},R_aX_{ca}\}.
\tag{7.9}
\]

If the six participating half-chains have one common radius, either
matching gives a full radius-preserving half-splice.  Relative to common
lower-tail indexing, the lower providers are fixed, while the owners and
upper providers are permuted by the same 3-cycle.  Thus its provider
powers are again \(0,1\).

This \(C_6\) is an exact endpoint assignment trade, not automatically a
physical three-seam packet.  Its new joins still require compatible
\(H\)-collars and globally simple signed target columns.

## 8. The reduced handoff asymptotics

We now specialize to

\[
 H=H_m,\qquad
 H^2/m=\log\log m+o(1),
\qquad H=o(m^{2/3}).
\tag{8.1}
\]

### Lemma 8.1 (exact tail ratio at the reduced scale)

With

\[
                         N_H=\binom{2m}{m-H},
\tag{8.2}
\]

one has

\[
 \boxed{
 \frac{N_H}{W}
 =\exp\left(-\frac{H^2}{m}+o(1)\right)
 =(1+o(1))\frac1{\log m}.}
\tag{8.3}
\]

#### Proof

The exact product is

\[
 \frac{N_H}{W}
 =\prod_{j=0}^{H-1}\frac{m-j}{m+j+1}.
\tag{8.4}
\]

Taking logarithms and expanding uniformly, using \(H=o(m^{2/3})\),

\[
 \begin{aligned}
 \log\frac{N_H}{W}
 &=
 \sum_{j=0}^{H-1}
 \left[
 \log\left(1-\frac jm\right)
 -\log\left(1+\frac{j+1}{m}\right)
 \right]\\
 &=-\frac1m\sum_{j=0}^{H-1}(2j+1)+o(1)\\
 &=-\frac{H^2}{m}+o(1).
 \end{aligned}
\tag{8.5}
\]

Substitute (8.1). \(\square\)

Let the retained pieces have at most \(r\) word positions (hence at most
\(r-1\) internal transitions), where

\[
                         r=O(\log m)
\tag{8.6}
\]

and suppose their number is

\[
                         P=(1+o(1))N_H.
\tag{8.7}
\]

Then

\[
 \frac{P}{W/H}
 =(1+o(1))\frac{H}{\log m}
 \longrightarrow\infty.
\tag{8.8}
\]

Thus a final component count \(p=o(W/H)\) requires average aggregation

\[
 \boxed{
                         \frac{P}{p}
 =\omega\!\left(\frac{H}{\log m}\right).}
\tag{8.9}
\]

This is the stated reduced-handoff component-length gate.

## 9. No affordable unary exact-suffix compiler

We formalize the architecture ruled out by the memory theorem.

A **unary exact-suffix fusion** starts with a duplicate-owner pair

\[
 v=\omega_0(T),\qquad u=\omega_1(\rho T),
\tag{9.0}
\]

where \(T\ne\rho T\), and \(u\) is the head of one previously unconsumed
original retained piece.  It follows a bridge from \(v\) and first meets a
full state reached along the unchanged suffix beginning at \(u\).  Its
width is the number of bridge edges.
In the unary architecture, its internal bridge states are new positions
uniquely charged to that fusion.  If a bridge consumes a third retained
component, overlaps another charged bridge, or shares a reusable corridor,
the whole operation is classified instead as a multiway/shared fusion.
The bridge may replace the old prefix from \(u\) to its meeting state,
but that prefix has at most \(r\) positions.  A width-\(k\) unary bridge
has \(k-1\) uniquely charged internal positions before this prefix credit.

### Theorem 9.1 (reduced-scale unary seam cut)

Assume (8.1), (8.6), and (8.7), with \(r<H\).  Suppose a compiler:

1. starts with \(P\) retained components;
2. ends with \(p=o(W/H)\) components;
3. uses unary exact-suffix fusions;
4. preserves two-sided radius-\(H\) safety; and
5. uniquely charges every new internal bridge state to one fusion, with no
   overlap, reused corridor, or third retained component; and
6. deletes only the replaced prefix of the one receiving piece, of length
   at most \(r\), at each fusion;
7. has initial retained length \(W+o(W)\) and final length \(W+o(W)\).

Then no such compiler exists.

#### Proof

By definition, every unary binary fusion consumes one previously
unconsumed receiver and reduces the number of components by exactly one.
Hence the number of fusions is

\[
 F=P-p=(1-o(1))P
\tag{9.1}
\]

because \(p/P=o((W/H)/N_H)=o(1)\).

Let \(A\) be the total number of newly inserted internal bridge positions
and \(D\) the total number of deleted old-prefix positions.  Unique
charging and the two length assumptions give

\[
                         A-D=o(W).
\tag{9.2}
\]

Every fusion deletes at most \(r\) positions, so

\[
                         D\le Fr\le Pr=O(W).
\tag{9.3}
\]

Hence \(A=O(W)\).  A bridge of width greater than \(H\) has at least
\(H\) internal positions.  Therefore the number \(F_{>H}\) of such
bridges satisfies

\[
 F_{>H}\le\frac{A}{H}=O(W/H)=o(P).
\tag{9.4}
\]

Thus \((1-o(1))P\) required fusions have width at most \(H\).

Every receiving retained piece has length \(r<H\).  Its first meeting
point lies within \(H\) transitions of its alternate equal-owner start.
Corollary 3.1 forbids a safe width-\(\le H\) bridge from the distinct-root
state to that same full target state.  Hence none of the
\((1-o(1))P\) short fusions exists, contradicting (9.1). \(\square\)

The theorem permits \(o(P)\) exceptional long bridges.  There are too few
of them to reduce the component count to \(o(W/H)\).  A corridor shared
by several fusions, or one whose interior is retained mass, is deliberately
outside this unary model and belongs to the surviving multiway/shared
case.

### Corollary 9.2 (independently paid ladders fail)

If one full-flush ladder of Theorem 4.4 is inserted for every binary
fusion, then even after crediting one old receiving prefix of length at
most \(r\), the net number of inserted positions is at least

\[
 (1-o(1))P(H+q-r)
 =\Theta(HN_H)
 =\Theta\!\left(\frac{WH}{\log m}\right)
 =\omega(W).
\tag{9.5}
\]

Therefore the local ladder cannot be paid independently at the reduced
scale.

This conclusion uses physical inserted positions.  It does not turn the
assigned-column derivative (5.4) into a missing-hole lower bound.

## 10. Necessary arity of an \(H\)-cost multiway seam

Unary fusion is not the only possibility.  Let gadget \(j\) consume
\(a_j\) current components, produce \(c_j\ge1\) components, insert
\(b_j\) uniquely charged new positions, and have actual reduction

\[
                         \delta_j=a_j-c_j\le a_j-1.
\tag{10.0}
\]

### Theorem 10.1 (packet arity threshold)

Under the reduced-scale hypotheses, suppose every nontrivial gadget has

\[
                              b_j\ge cH
\tag{10.1}
\]

for one fixed \(c>0\), and the total insertion cost is \(o(W)\).  Then the
average actual component reduction among the paid gadgets, and hence
their average excess arity, satisfy

\[
 \boxed{
 \frac{\sum_j\delta_j}{\#\{j\}}
 =\omega\!\left(\frac{H}{\log m}\right),}
\tag{10.2}
\]

\[
 \boxed{
 \frac{\sum_j(a_j-1)}{\#\{j\}}
 =\omega\!\left(\frac{H}{\log m}\right).}
\tag{10.3}
\]

#### Proof

Equation (10.1) and total cost \(o(W)\) give

\[
                         G:=\#\{j\}=o(W/H).
\tag{10.4}
\]

To pass from \(P\) components to \(p=o(W/H)=o(P)\), the total reduction
telescopes exactly:

\[
                         \sum_j\delta_j=P-p=(1-o(1))P.
\tag{10.5}
\]

Divide (10.5) by (10.4), use (8.8), and then use
\(\delta_j\le a_j-1\). \(\square\)

Thus a bounded-arity \(H\)-cost packet cannot work.  In particular, the
binary lower-to-upper ladder is below the necessary arity by the factor
\(\omega(H/\log m)\).

If one assumes only coefficient-one initial/final length and credits
\(O(W)\) deleted retained mass, then the same gross-mass argument gives
only \(G=O(W/H)\) and the weaker average bound

\[
                         \Omega\!\left(\frac{H}{\log m}\right).
\tag{10.6}
\]

The little-\(o\) conclusion (10.2)--(10.3) uses the stated
\(o(W)\) **gross** insertion hypothesis.

The theorem does **not** obstruct:

1. a zero-entry endpoint permutation such as a physical half-splice
   trade;
2. an \(o(\log m)\)-entry genuinely different-target seam;
3. an \(H\)-step corridor whose states replace retained path mass instead
   of being inserted;
4. many defects pipelined through one already necessary global
   trajectory; or
5. an \(H\)-cost packet which simultaneously fuses
   \(\omega(H/\log m)\) pieces.

These are precisely the architectures not covered by predecessor-root
confluence.

## 11. Precise proved and conditional boundary

### Proved

1. The multistep cache inversion formulas (2.8)--(2.14).
2. Geodesic owner motion for every safe bridge of length at most \(H\).
3. Equal-owner, distinct-root states cannot coalesce at one full state in
   at most \(H\) edges.
4. Every two-letter and every bounded-width exact-suffix bypass is
   impossible.
5. A two-letter far-suffix shortcut must skip at least \(2H-2\) old
   transitions.
6. The exact free-state lower-to-upper ladder of length \(q+H+1\).
7. Strict \(H\)-safety and signed-target injectivity of both ladder routes.
8. Exact controlled target displacement \(2(d-q+2)\) and owner
   displacement \(2\).
9. The alternate-corner cycle criterion for completing the ladder's
   initial endpoint pair to a second full SCD.
10. Exact endpoint provider exponents \(0,1\).
11. Pairwise half-splice rigidity and minimal algebraic \(C_6\) arity.
12. The reduced-scale asymptotic \(N_H=(1+o(1))W/\log m\).
13. Impossibility of every independently charged unary exact-suffix
    compiler with coefficient-one initial/final length at the reduced
    scale.
14. The multiway arity threshold
    \(\omega(H/\log m)\) for independently paid \(H\)-cost gadgets.

### Not proved

1. Positive-density cycles of the alternate-corner map.
2. Completion of all intermediate ladder states inside two fixed SCDs.
3. A common owner partition for \(O(N_H)\) or more ladders.
4. Global cancellation or injective placement of ladder target
   derivatives.
5. A physical \(C_6\) endpoint packet with jointly compatible
   \(H\)-collars.
6. An \(o(\log m)\)-cost genuinely different-target seam at the reduced
   scale.
7. An \(H\)-cost packet of arity
   \(\omega(H/\log m)\).
8. The coefficient-one theorem.

The exact decision is:

\[
 \boxed{
 \begin{minipage}{0.88\textwidth}
 Two letters and, more generally, every independently charged unary
 exact-suffix architecture are impossible.  A legal different-target
 corridor exists locally, but its independently paid \(\Theta(H)\) width
 is too expensive at
 \(H^2/m=\log\log m+o(1)\).  The surviving construction must globally
 permute endpoints, absorb the corridor into retained mass, pipeline
 defects, or obtain average reduction \(\omega(H/\log m)\) in an
 independently paid \(o(W)\)-gross-cost \(H\)-packet family.
 \end{minipage}}
\tag{11.1}
\]
