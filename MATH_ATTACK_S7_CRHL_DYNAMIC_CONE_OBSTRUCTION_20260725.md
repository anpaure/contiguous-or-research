# Lane S7: triangular-cone obstruction to dynamic CRHL fusion

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computer-assisted enumeration is used.

## 0. Outcome and precise scope

This report does not prove \(\mathrm{CRHL}_A\), \(\mathrm{RSCD}_A\), or
the constant-one theorem. It proves a genuinely cross-layer obstruction
which is absent from the one-layer forced-target theorem.

In every no-merger recursive Hall lift, retaining the directed edge from
the state indexed by \(i\) to the state indexed by \(i+1\) forces

\[
 L_{j+1}(i)=L_j(i)\cap L_j(i+1),\qquad
 R_{j+1}(i+1)=R_j(i)\cap R_j(i+1).
 \tag{0.1}
\]

Consequently an uncut triangular cone of inherited adjacencies forces

\[
 L_h(i)=\bigcap_{r=0}^{h}X_{i+r},\qquad
 R_h(i)=\bigcap_{r=0}^{h}X_{i-r}^{\,c}.
 \tag{0.2}
\]

Let \(\delta_h^-\) and \(\delta_h^+\) be the exact duplicate excesses of
these forward and backward intersection maps on the domains on which all
displayed centers survive through depth \(h\). If \(k_q\) inherited edges
are first cut in the lift from depth \(q\) to depth \(q+1\), then every
exact recursive band SCD satisfies

\[
 \boxed{
 \max\{\delta_h^-,\delta_h^+\}
 \le \sum_{q=0}^{h-1}(h-q)k_q .}
 \tag{0.3}
\]

Thus, with \(K_{<h}=\sum_{q<h}k_q\),

\[
 \boxed{
 K_{<h}\ge
 \left\lceil
   \frac{\max\{\delta_h^-,\delta_h^+\}}{h}
 \right\rceil .}
 \tag{0.4}
\]

There is also an exact all-depth form. Every collision pair in (0.2)
supplies a hyperedge equal to the union of its two triangular cut cones.
The set of first-cut events of any recursive realization must be one
integral transversal of all these hyperedges simultaneously. This records
exactly how one early cut may repair several later layers; it does not sum
unrelated layerwise optima.

For the globally contiguous odd-cut order, put

\[
 W=\binom{2m}{m},\qquad
 B=\operatorname{Cat}_m=\frac{W}{m+1}.
\]

If \(\bar\delta_h^\pm\) are the duplicate excesses of the full cyclic
odd-cut pseudo-endpoint maps on all
\(N_h=\binom{2m}{m-h}\) depth-\(h\) survivors, the exact boundary losses
give

\[
 \boxed{
 \begin{aligned}
 (\bar\delta_h^- -hB)_+
   &\le \sum_{q<h}(h-q)k_q,\\
 (\bar\delta_h^+ -hB)_+
   &\le \sum_{q<h}(h-q)k_q.
 \end{aligned}}
 \tag{0.5}
\]

The injective-load floor in the restricted ledger is exactly zero. The
common term \(hB\) is an exact integer worst-case allowance for
cut-path ends in either orientation, not an asymptotic placeholder.

Therefore \(\mathrm{CRHL}_A\), with
\(H=\lceil A\sqrt m\rceil\) and \(K_H=o(W/H)\), necessarily requires
for every integer sequence \(1\le h=h(m)\le H\),

\[
 \bar\delta_h^-
 \le hB+o\!\left(\frac{hW}{H}\right),\qquad
 \bar\delta_h^+
 \le hB+o\!\left(\frac{hW}{H}\right).
 \tag{0.6}
\]

In particular, positive-density duplicate excess at any
\(h=\Theta(\sqrt m)\) rules out that recursive history. No such
positive-density estimate for every admissible odd-cut ordering is proved
here. Equations (0.3)--(0.6) are a sharper obstruction and a new necessary
gate, not a disproof of \(\mathrm{CRHL}_A\).

All objects in the proof are integral.

## 1. Exact recursive setup

Let the initial directed path forest consist of complementary Johnson paths

\[
 P=(X_0,X_1,\ldots,X_m),\qquad X_m=X_0^c,
 \tag{1.1}
\]

which partition the middle layer. Give each middle owner \(v\) a terminal
radius \(\tau(v)\in\{0,\ldots,H\}\), and put

\[
 V_h=\{v:\tau(v)\ge h\}.
 \tag{1.2}
\]

In the exact clipped-radius ledger,

\[
 |V_h|=N_h=\binom{2m}{m-h}.
 \tag{1.3}
\]

A no-merger recursive realization assigns to every \(v\in V_h\) a state

\[
 \omega_h(v)
 =\bigl(L_h(v);z_1(v),\ldots,z_{2h}(v);R_h(v)\bigr).
 \tag{1.4}
\]

Because the realization is one exact saturated band SCD, both maps

\[
 v\longmapsto L_h(v),\qquad v\longmapsto R_h(v)
 \tag{1.5}
\]

are bijections from \(V_h\) onto
\(\binom{[2m]}{m-h}\). The second map labels complements of upper
endpoints.

Every retained forest edge keeps its original path-edge identity. If an
original edge is first not retained in the lift from depth \(q\) to depth
\(q+1\), while both endpoints lie in \(V_{q+1}\), call \((q,e)\) its
first-cut event. This includes a deliberate deletion of an otherwise
liftable edge.
Write

\[
 D_q=\{e:(q,e)\text{ is a first-cut event}\},\qquad
 k_q=|D_q|.
 \tag{1.6}
\]

Viewed as original edge identities, the \(D_q\) are disjoint. An edge lost
because one endpoint stops is not charged. It will not occur in the cones
below, because every vertex of such a cone is required to survive to the
final depth under consideration.

## 2. One retained edge forces intersections

### Lemma 2.1

Let the inherited adjacency \(i\to i+1\) be present at depth \(j\), and
suppose it is retained in the lift to depth \(j+1\). Then

\[
 \boxed{
 L_{j+1}(i)=L_j(i)\cap L_j(i+1),\qquad
 R_{j+1}(i+1)=R_j(i)\cap R_j(i+1).}
 \tag{2.1}
\]

This includes \(j=0\).

#### Proof

Write the rotor edge as \(v\to w\), using
\(x\in L_j(v)\) and \(y\in R_j(v)\). Its lower relation is

\[
 L_j(w)=L_j(v)-x+y.
 \tag{2.2}
\]

The exact one-edge lift criterion forces the source lower deletion to be
\(\ell_v=x\). Hence

\[
 L_{j+1}(v)=L_j(v)-x=L_j(v)\cap L_j(w).
 \tag{2.3}
\]

For \(j\ge1\), the residual relation is

\[
 R_j(w)=R_j(v)-y+z_{2j}(v),
 \tag{2.4}
\]

and the lift criterion forces the target residual deletion to be
\(u_w=z_{2j}(v)\). Therefore

\[
 R_{j+1}(w)=R_j(w)-z_{2j}(v)
           =R_j(v)\cap R_j(w).
 \tag{2.5}
\]

At \(j=0\), one has
\(R_0(w)=R_0(v)-y+x\) and the forced deletion is \(u_w=x\), so the same
intersection identity holds. \(\square\)

Thus a clean history propagates by literal set intersection; unforced
endpoint choices disappear from the calculation.

## 3. Triangular causal cones

Fix a path \(P=(X_0,\ldots,X_m)\), an integer \(h\ge1\), and an index
\(t\). A forward window is admissible when

\[
 0\le t\le m-h,\qquad
 X_t,X_{t+1},\ldots,X_{t+h}\in V_h.
 \tag{3.1}
\]

Define

\[
 \Lambda_h(P,t)=\bigcap_{r=0}^{h}X_{t+r}
 \tag{3.2}
\]

and its forward cone

\[
 \mathcal C_h^-(P,t)
 =\{(q,e_{t+r}):0\le q<h,\ 0\le r<h-q\},
 \tag{3.3}
\]

where \(e_s\) is \(X_s\to X_{s+1}\).

A backward window is admissible when

\[
 h\le t\le m,\qquad
 X_{t-h},\ldots,X_t\in V_h.
 \tag{3.4}
\]

Define

\[
 \Pi_h(P,t)=\bigcap_{r=0}^{h}X_{t-r}^{\,c}
 \tag{3.5}
\]

and

\[
 \mathcal C_h^+(P,t)
 =\{(q,e_{t-1-r}):0\le q<h,\ 0\le r<h-q\}.
 \tag{3.6}
\]

On a complementary Johnson path, the sets in (3.2) and (3.5) have size
exactly \(m-h\). Indeed, in a path of \(m\) exchanges from \(X_0\) to
\(X_0^c\), the removed coordinates are the \(m\) distinct coordinates of
\(X_0\).

### Lemma 3.1 (clean-cone rigidity)

If no first-cut event lies in \(\mathcal C_h^-(P,t)\), then

\[
 L_h(X_t)=\Lambda_h(P,t).
 \tag{3.7}
\]

If no first-cut event lies in \(\mathcal C_h^+(P,t)\), then

\[
 R_h(X_t)=\Pi_h(P,t).
 \tag{3.8}
\]

#### Proof

Induct on \(h\). At depth zero,
\(L_0(X_t)=X_t\) and \(R_0(X_t)=X_t^c\).

For the lower assertion, the cone decomposes as

\[
 \mathcal C_h^-(P,t)
 =\mathcal C_{h-1}^-(P,t)
  \cup\mathcal C_{h-1}^-(P,t+1)
  \cup\{(h-1,e_t)\}.
 \tag{3.9}
\]

By induction the two depth-\((h-1)\) lower endpoints are their canonical
intersections. The last event in (3.9) is uncut, so Lemma 2.1 gives

\[
 \begin{aligned}
 L_h(X_t)
 &=L_{h-1}(X_t)\cap L_{h-1}(X_{t+1})\\
 &=\left(\bigcap_{r=0}^{h-1}X_{t+r}\right)
   \cap
   \left(\bigcap_{r=1}^{h}X_{t+r}\right)
 =\bigcap_{r=0}^{h}X_{t+r}.
 \end{aligned}
 \tag{3.10}
\]

The reflected argument and the second identity of Lemma 2.1 prove (3.8).
\(\square\)

## 4. Exact duplicate-excess inequality

Let \(\mathcal I_h^-\) and \(\mathcal I_h^+\) be the admissible forward
and backward window domains. Define

\[
 \mu_h^-(S)
 =|\{a\in\mathcal I_h^-:\Lambda_h(a)=S\}|,\qquad
 \mu_h^+(S)
 =|\{a\in\mathcal I_h^+:\Pi_h(a)=S\}|,
 \tag{4.1}
\]

and

\[
 \delta_h^\pm
 =\sum_{S\in\binom{[2m]}{m-h}}(\mu_h^\pm(S)-1)_+.
 \tag{4.2}
\]

Equivalently,

\[
 \delta_h^-
 =|\mathcal I_h^-|-|\Lambda_h(\mathcal I_h^-)|,\qquad
 \delta_h^+
 =|\mathcal I_h^+|-|\Pi_h(\mathcal I_h^+)|.
 \tag{4.3}
\]

The exact integral floor in this restricted injectivity ledger is zero.

### Theorem 4.1 (triangular-cone duplicate obstruction)

For every exact no-merger recursive band SCD and \(1\le h\le H\),

\[
 \boxed{
 \delta_h^-
 \le\sum_{q=0}^{h-1}(h-q)k_q,\qquad
 \delta_h^+
 \le\sum_{q=0}^{h-1}(h-q)k_q.}
 \tag{4.4}
\]

Consequently,

\[
 \boxed{
 K_{<h}:=\sum_{q=0}^{h-1}k_q
 \ge
 \left\lceil
  \frac{\max\{\delta_h^-,\delta_h^+\}}{h}
 \right\rceil.}
 \tag{4.5}
\]

#### Proof

Call a forward window dirty if its cone contains a first-cut event. Every
clean window has actual lower endpoint equal to its canonical endpoint by
Lemma 3.1. Since the actual map \(v\mapsto L_h(v)\) is injective, at most
one clean window can remain in each fiber of \(\Lambda_h\). A fiber of
size \(\mu\) therefore contains at least \(\mu-1\) dirty windows.
Summing gives at least \(\delta_h^-\) dirty forward windows.

A fixed first-cut event \((q,e_s)\) belongs to the forward cone beginning
at \(t\) only when

\[
 0\le s-t<h-q.
 \tag{4.6}
\]

There are at most \(h-q\) such values of \(t\). Hence

\[
 \#\{\text{dirty forward windows}\}
 \le\sum_{q<h}(h-q)|D_q|.
 \tag{4.7}
\]

This proves the lower inequality. The backward proof is identical: one
level-\(q\) event lies in at most \(h-q\) backward cones, and the actual
residual map is injective.

Finally,

\[
 \sum_{q<h}(h-q)k_q\le h\sum_{q<h}k_q=hK_{<h}.
\]

All quantities are integral, so the ceiling in (4.5) is exact.
\(\square\)

### Corollary 4.2 (nonnegative multidepth dual)

For arbitrary \(a_1,\ldots,a_H\ge0\),

\[
 \sum_{h=1}^H a_h\delta_h^-
 \le
 \sum_{q=0}^{H-1}k_q
      \sum_{h=q+1}^H a_h(h-q),
 \tag{4.8}
\]

and likewise with \(+\) in place of \(-\).

#### Proof

Multiply (4.4) by \(a_h\), sum, and reverse the finite sums. \(\square\)

This charges one early cut by its exact future cone capacity, instead of
adding independent layerwise minima.

## 5. One global integral collision transversal

Let

\[
 \mathcal U_H
 =\{(q,e):0\le q<H,\ e\text{ is an original path edge whose
 endpoints lie in }V_{q+1}\}.
 \tag{5.1}
\]

For every two distinct forward windows \(a,b\in\mathcal I_h^-\) with
\(\Lambda_h(a)=\Lambda_h(b)\), form the hyperedge

\[
 \mathcal C_h^-(a)\cup\mathcal C_h^-(b).
 \tag{5.2}
\]

Do the same for every backward collision and every \(1\le h\le H\).
Let \(\mathscr H_H\) be the resulting hypergraph.

A transversal is history-admissible if it contains at most one event
\((q,e)\) for each original edge \(e\). Define

\[
 \tau_H^{\mathrm{dyn}}
 =\min\{|T|:T\text{ is a history-admissible transversal of }
                  \mathscr H_H\},
 \tag{5.3}
\]

with value \(+\infty\) if no such transversal exists.

### Theorem 5.1 (global dynamic collision transversal)

Every exact no-merger recursive realization satisfies

\[
 \boxed{K_H\ge\tau_H^{\mathrm{dyn}}.}
 \tag{5.4}
\]

#### Proof

If two forward windows with the same canonical endpoint both had clean
cones, Lemma 3.1 would make their actual lower endpoints equal, contrary
to endpoint injectivity. Thus the actual first-cut set meets (5.2). The
same holds for every backward collision at every depth.

An original edge has one first-cut time, so the actual first-cut set is
history-admissible. It has cardinality \(K_H\), proving (5.4).
\(\square\)

A usable fractional dual is legitimate only as a lower bound. If
nonnegative weights \(\alpha_C\) on the collision hyperedges satisfy

\[
 \sum_{C\ni u}\alpha_C\le1\qquad(u\in\mathcal U_H),
 \tag{5.5}
\]

then

\[
 K_H\ge\sum_C\alpha_C.
 \tag{5.6}
\]

Indeed, charge every hyperedge to one selected event which hits it and use
(5.5). No rounding of this fractional dual to an SCD is asserted.

## 6. Exact odd-cut boundary allowances

For an odd-cut path, write its cyclic coordinate word as

\[
 w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1}).
 \tag{6.1}
\]

The canonical radius-\(h\) pseudo-state at \(X_t\) has endpoints

\[
 \bar\Lambda_h(P,t)=I_w(t+h,m-h),\qquad
 \bar\Pi_h(P,t)=I_w(t+m,m-h).
 \tag{6.2}
\]

These maps are defined cyclically for all \(0\le t\le m\), including
centers too close to a cut-path endpoint to possess a full one-sided
window. Restrict them to \(V_h\) and put

\[
 \bar\delta_h^-
 =|V_h|-|\bar\Lambda_h(V_h)|,\qquad
 \bar\delta_h^+
 =|V_h|-|\bar\Pi_h(V_h)|.
 \tag{6.3}
\]

Assume now that the terminal-radius blocks are globally contiguous after
concatenating the \(B\) directed paths. Thus every \(V_h\) is one global
suffix.

### Lemma 6.1 (exact discarded-window counts)

For \(1\le h\le H\le m\),

\[
 |V_h\setminus\mathcal I_h^-|\le hB,\qquad
 |V_h\setminus\mathcal I_h^+|\le hB.
 \tag{6.4}
\]

#### Proof

Put \(\ell_i=|V_h\cap P_i|\). Because \(V_h\) is one global suffix of
the concatenation, \(V_h\cap P_i\) is a suffix run of \(P_i\), possibly
empty. In either orientation, a length-\(h\) window lies wholly inside
that run for exactly \((\ell_i-h)_+\) choices of its indexed endpoint.
Hence the number discarded in either orientation is exactly

\[
 \beta_h:=
 \sum_{i=1}^{B}
 \bigl(\ell_i-(\ell_i-h)_+\bigr)
 =\sum_{i=1}^{B}\min\{h,\ell_i\}
 \le hB.
\]

This count already includes the path containing the unique global suffix
boundary; there is no further \(+h\) loss. \(\square\)

Deleting one argument of a finite map reduces its duplicate excess by at
most one. Therefore

\[
 \delta_h^-\ge(\bar\delta_h^- -\beta_h)_+,\qquad
 \delta_h^+\ge(\bar\delta_h^+ -\beta_h)_+.
 \tag{6.5}
\]

Combining with Theorem 4.1 gives the full cyclic test.

### Corollary 6.2

Every globally contiguous no-merger recursive realization satisfies

\[
 \boxed{
 \begin{aligned}
 (\bar\delta_h^- -\beta_h)_+
 &\le\sum_{q=0}^{h-1}(h-q)k_q,\\
 (\bar\delta_h^+ -\beta_h)_+
 &\le\sum_{q=0}^{h-1}(h-q)k_q.
 \end{aligned}}
 \tag{6.6}
\]

If

\[
 \Delta_h
 =\max\{(\bar\delta_h^- -\beta_h)_+,
          (\bar\delta_h^+ -\beta_h)_+\},
 \tag{6.7}
\]

then

\[
 \boxed{
 K_{<h}\ge\left\lceil\frac{\Delta_h}{h}\right\rceil.}
 \tag{6.8}
\]

The exact common discarded-window baseline is
\(\beta_h=\sum_i\min\{h,\ell_i\}\); its uniform worst-case bound is
\(\beta_h\le hB\).

### Corollary 6.3 (necessary multidepth rigidity)

Fix \(A>0\), let \(H=\lceil A\sqrt m\rceil\), and suppose one recursive
history has

\[
 K_H=o(W/H).
 \tag{6.9}
\]

Then, for every chosen sequence \(1\le h=h(m)\le H\),

\[
 \boxed{
 \bar\delta_h^-
 \le hB+o\!\left(\frac{hW}{H}\right),\qquad
 \bar\delta_h^+
 \le hB+o\!\left(\frac{hW}{H}\right).}
 \tag{6.10}
\]

If \(h=\Omega(\sqrt m)\), both duplicate excesses are \(o(W)\).

#### Proof

The weighted right side of (6.6) is at most \(hK_H\), while
\(\beta_h\le hB\), giving (6.10). Also
\(hB=hW/(m+1)=o(W)\) for \(h\le H=O_A(\sqrt m)\).
For \(h=\Omega(\sqrt m)\), the remaining little-oh term is \(o(W)\).
\(\square\)

Thus a successful ordering must make the cyclic pseudo-endpoint maps
asymptotically injective at every Gaussian depth, after the exact boundary
allowances above.

## 7. Exact Hall failure after a feasible first layer

The next example isolates dynamic matching compatibility itself, before
any rotor reward is imposed.

### Proposition 7.1

In \(B_6\), there is an exact globally contiguous lifetime assignment with

\[
 |V_0|=20,\qquad |V_1|=15,\qquad |V_2|=6
 \tag{7.1}
\]

such that both lower and upper-complement perfect matchings exist in the
first lift, but no lower matching can perform the second lift, regardless
of which first lower matching is chosen.

#### Proof

Write triples without braces. Set

\[
 V_2=\{123,124,125,134,135,145\}
 \tag{7.2}
\]

and

\[
 V_1=\binom{[5]}3
 \cup\{126,136,146,156,236\}.
 \tag{7.3}
\]

Then \(|V_2|=6=\binom61\) and
\(|V_1|=15=\binom62\), exactly the required Boolean rank sizes.

A lower perfect matching from \(V_1\) to all fifteen pairs is

\[
 \begin{array}{c|cccccccccc}
 v&123&124&125&134&135&145&234&235&245&345\\ \hline
 L_1(v)&12&14&15&13&35&45&24&23&25&34
 \end{array}
 \tag{7.4}
\]

and

\[
 \begin{array}{c|ccccc}
 v&126&136&146&156&236\\ \hline
 L_1(v)&16&36&46&56&26.
 \end{array}
 \tag{7.5}
\]

Every displayed pair is contained in its triple, and the fifteen targets
are all the pairs exactly once.

For the upper-complement matching, the residual-root family
\(\{v^c:v\in V_1\}\) is the family of all triples except

\[
 123,124,125,134,135.
\]

The following is a perfect matching of those residual roots to all pairs:

\[
 \begin{array}{c|cccccccccc}
 R_0(v)&146&256&236&246&356&126&136&156&346&456\\ \hline
 R_1(v)&16&26&36&46&56&12&13&15&34&45
 \end{array}
 \tag{7.6}
\]

and

\[
 \begin{array}{c|ccccc}
 R_0(v)&145&234&235&245&345\\ \hline
 R_1(v)&14&24&23&25&35.
 \end{array}
 \tag{7.7}
\]

Again every target is contained in its residual root and all fifteen pairs
occur once. Thus the two first-layer matching systems are simultaneously
feasible and construct an exact depth-one band SCD.

Now take any first-layer lower perfect matching, not necessarily (7.4)--(7.5).
For every \(v\in V_2\), one has

\[
 L_1(v)\subset v\subset[5].
 \tag{7.8}
\]

Any second extension would have
\(L_2(v)\subset L_1(v)\), so every one of its six lower targets would lie
in \(\binom{[5]}1\). It could not cover the required sixth singleton
\(\{6\}\). Hence the second lower Hall system is impossible for every
first-layer history.

Finally,

\[
 |V_0\setminus V_1|=5,\qquad
 |V_1\setminus V_2|=9,\qquad
 |V_2|=6,
 \tag{7.9}
\]

which are exactly \(c_0,c_1,N_2\). Ordering these three displayed classes
consecutively makes \(V_1,V_2\) global suffixes. \(\square\)

This proposition is stronger than a first-layer Hall counterexample: the
entire first layer is integrally feasible on both signs, but the chosen
survivor ancestry makes the next layer impossible. It is still not an
odd-cut-path counterexample, because the arbitrary order in the last
sentence is not asserted to be a concatenation of the prescribed odd-cut
paths.

The general ancestry condition exposed by the proof is immediate. If a
lower flag system exists, then for every \(h\) the containment graph

\[
 V_h\longleftrightarrow\binom{[2m]}{m-h},
 \qquad v\sim T\iff T\subset v
 \tag{7.10}
\]

has a perfect matching. Equivalently, for every target family
\(\mathcal T\subseteq\binom{[2m]}{m-h}\),

\[
 \boxed{
 |\{v\in V_h:\text{ some }T\in\mathcal T\text{ satisfies }T\subset v\}|
 \ge|\mathcal T|.}
 \tag{7.11}
\]

The complementary condition with \(T\subset v^c\) is necessary for upper
flags. These all-depth ancestral Hall inequalities are immune to rotor-edge
deletions. They are not asserted to be sufficient for one nested flag
history.

## 8. Exact two-layer rotor-collision gadget

The following hand-checkable gadget shows that first-layer paired-rainbow
compatibility does not compose automatically.

In \(B_8\), with \(m=4\), take the two vertex-disjoint complementary
Johnson paths

\[
 \begin{aligned}
 P:\quad
 1234&\to1235\to1256\to2567\to5678,\\
 Q:\quad
 1267&\to1268\to1248\to1348\to3458.
 \end{aligned}
 \tag{8.1}
\]

The final set in each row is the complement of the first. On the first
two edges of each row, the four lower forced targets at the first lift are

\[
 123,\quad125,\quad126,\quad128,
 \tag{8.2}
\]

which are distinct. The four upper-complement forced targets, namely the
complements of the four joins, are

\[
 678,\quad478,\quad345,\quad357,
 \tag{8.3}
\]

also distinct. Hence both one-layer forced-label projections, and the
paired-label test on this four-edge gadget, have zero duplicate defect.

At depth two, however,

\[
 1234\cap1235\cap1256
 =12
 =1267\cap1268\cap1248.
 \tag{8.4}
\]

Therefore at least one event in

\[
 \begin{aligned}
 \{&(0,1234\to1235),(0,1235\to1256),
      (1,1234\to1235),\\
   &(0,1267\to1268),(0,1268\to1248),
      (1,1267\to1268)\}
 \end{aligned}
 \tag{8.5}
\]

must be cut. This is precisely one collision hyperedge from Theorem 5.1.

The gadget is local: these ten middle sets do not constitute a full
middle-layer factor. Thus it disproves automatic composition of the local
forced-label test, but is not a counterexample to the existential full
odd-cut \(\mathrm{CRHL}_A\) statement.

## 9. Audit and proved/conditional boundary

The decisive implications were audited as follows.

1. Lemma 2.1 uses the forced source lower deletion and forced target
   residual deletion. The exceptional depth-zero formula is included.
2. At fixed final depth \(h\), a level-\(q\) cut lies in at most \(h-q\)
   forward cones and at most \(h-q\) backward cones. For \(h=1\), the
   capacity is one, verifying the absence of an off-by-one term.
3. First-cut events are counted once. Under no merger/no reintroduction,
   an original adjacency cannot reappear.
4. Stopping edges create no uncharged cone failure: every cone vertex lies
   in \(V_h\subseteq V_{q+1}\).
5. Endpoint injectivity is exact rank ownership in one saturated band SCD,
   not an added hypothesis.
6. The full cyclic losses in both orientations have the exact integer
   upper bound \(hB\). With
   \(\ell_i=|V_h\cap P_i|\), their common exact discarded-window count is
   \(\sum_i\min\{h,\ell_i\}\); the global suffix boundary is already
   included.
7. The collision-transversal number is necessary only. A transversal need
   not support either Boolean perfect matching and need not produce a band
   SCD.

The proved advance is (4.4), its all-depth integral fusion form (5.4), and
the exact odd-cut baseline (6.6).

To close \(\mathrm{CRHL}_A\) negatively by this method, it is enough to
prove that every admissible globally contiguous odd-cut ordering has
\(\bar\delta_h^\pm=\Omega(W)\) at some
\(h=\Theta(\sqrt m)\), or more generally
\(\tau_H^{\mathrm{dyn}}\not=o(W/H)\).

To prove \(\mathrm{CRHL}_A\) positively, it is necessary to choose the
odd-cut order so that (6.10) holds at every depth and then still solve the
two exact forced-target matching systems along one common history.
Near-injectivity is necessary, not sufficient.

No separate layerwise matching, fractional flow, pseudo-state family, or
collision transversal is promoted here to an integral SCD or to a literal
contiguous-OR word.
