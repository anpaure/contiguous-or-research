# Audit: faithful FIFO orbit flow, exact leaves, and the scope of \(s\eta=o(1)\)

Date: 2026-07-27

Method: pure hand mathematics only. No computation, finite search, solver,
or web input is used.

Audited source:
`MATH_THEOREM_R_FIFO_JOINT_CATALOGUE_CODEGREES_AND_FLOW_COLLAPSE_20260727.md`.

## 0. Verdict

Put

\[
 L=2m,\qquad k=m-H,\qquad \ell=m+H,\qquad
 N=\binom{2m}{k},\qquad W=\binom{2m}{m},
\]

\[
 \lambda={W\over N}={k!\ell!\over(m!)^2},\qquad
 r=\lfloor\lambda\rfloor,
\]

and assume

\[
 1\le r\le H,\qquad 2H<m,\qquad \gcd(\ell,r)=1.
\tag{0.1}
\]

The following parts of the source pass the audit.

1. The faithful state graph is one-in/one-out and its components are the
   complete \(L\)-block \(F_r\)-orbits.
2. The joint root-owner edge has exactly \(L\) distinct root vertices and
   \(Lr\) distinct owner vertices.
3. Its exact degrees are

   \[
   D_R=k!\ell!,\qquad D_M=r(m!)^2={r\over\lambda}D_R.
   \tag{0.2}
   \]

4. The root-root, root-owner, and owner-owner codegree formulae in the
   source are correctly normalized. The root-interval displacement bounds
   and the reduced-scale no-complement lemma also pass.
5. At

   \[
   H=\lfloor\sqrt{m\log\log m}\rfloor,
   \qquad r=\log m+O(1),
   \tag{0.3}
   \]

   the full rank \(s=L(r+1)\) and relative codegree \(\eta_m\) satisfy

   \[
   s\eta_m=O\left({r^2H\over m}\right)=o(1).
   \tag{0.4}
   \]

Two scope corrections are required.

* The inequality \(tr\ge2H\) is a necessary condition for the specific
  overlapping-collar recurrence. It does not by itself certify collar
  cancellation. Physical closure here comes from the explicit closed
  ordered \(F_r\)-trajectory, together with its separately verified
  depth-\(H\) legality.
* The independent-thinning statement can and should be made globally
  exact. Below density \(e^{-1}-\Omega(1)\), with high probability no
  complete catalogue column survives at all. This is a procedural
  obstruction to a product-residual nibble, not an obstruction to a
  correlated integral packing.

The source does not prove a near-perfect matching. Conversely, this audit
does not produce a counterexample to a near-perfect matching in the
specific FIFO catalogue.

## 1. Exact orbit-flow rigidity

Let \({\cal S}\) be the fully ordered state set and let

\[
                         \Sigma\longrightarrow F_r\Sigma
\tag{1.1}
\]

be the macro transition. Since the slot permutation of \(F_r\) is an
\(L\)-cycle, every component of (1.1) is a directed \(L\)-cycle.

### Theorem 1.1 (elementary faithful-flow collapse)

Let \(y_\Sigma\) be a real flow on the arcs of (1.1). If it is conserved
at every fully ordered state, then it is constant on every \(F_r\)-orbit.
Consequently every integral capacity-one circulation is a disjoint union
of complete physical orbit columns.

#### Proof

At \(\Sigma\), conservation reads

\[
                         y_{F_r^{-1}\Sigma}=y_\Sigma.
\]

Iteration makes \(y\) constant around the component. Distinct labels make
the first state return occur after exactly \(L\) macros. Thus a Boolean
constant selects the whole orbit or none of it. \(\square\)

There is a useful strengthening which rules out a hidden fixed-rank
reduction by longer chunks.

### Theorem 1.2 (chunk cycles only resegment or multiply a whole orbit)

Fix \(1\le t<L\) and replace the macro arcs by faithful \(t\)-block
chunks

\[
                         \Sigma\longrightarrow F_r^t\Sigma.
\tag{1.2}
\]

Put \(g=\gcd(L,t)\). Every directed cycle of (1.2) has \(L/g\) chunks.
When expanded into elementary macro arcs, it traverses every arc of one
underlying \(F_r\)-orbit exactly \(t/g\) times.

Hence:

* if \(t/g>1\), the expanded cycle repeats every root block and violates
  capacity one;
* if \(t/g=1\), equivalently \(t\mid L\), it is merely a resegmentation
  of the same complete \(L\)-block orbit and has the same root-owner
  support.

Thus faithful subdivision never produces a smaller effective packing
column.

#### Proof

The permutation \(F_r^t\) has \(g\) cycles on an \(F_r\)-orbit, each of
length \(L/g\). Expanding one such cycle gives \((L/g)t\) elementary
macro-arc traversals. Translation invariance around the underlying
\(L\)-cycle gives the same multiplicity on every elementary arc, namely

\[
                         {(L/g)t\over L}={t\over g}.
\]

The two conclusions follow. \(\square\)

The fixed-length theorem is a special case of a stronger statement.
Allow arbitrary positive forward chunks on one deterministic
\(F_r\)-orbit, charge a chunk to every elementary macro arc it
traverses, impose conservation at every fully ordered endpoint state,
and impose capacity one on each elementary macro arc. Every integral
circulation decomposes into chunk cycles. Lifting one chunk cycle to the
universal cover of the directed \(L\)-cycle, the sum of its positive
chunk lengths is \(wL\) for an integer \(w\ge1\). Its expansion
traverses every elementary macro arc exactly \(w\) times. Capacity one
forces \(w=1\) and excludes a second cycle. Hence arbitrary forward
chunks also only resegment one complete orbit. This is Theorem 2.2 of
the audited source.

Any genuine bounded-rank escape must therefore add an exact transition
which changes the ordered queue orbit. A projected root splice is not
enough.

## 2. Exact joint fractional point

Let \({\cal C}_r\) be the catalogue of oriented cyclic coordinate orders,
counted modulo rotation. It has \((L-1)!\) columns. Give every column the
weight

\[
                         x_C={1\over D_R}.
\tag{2.1}
\]

Every root receives load one. Every owner receives load

\[
                         {D_M\over D_R}={r\over\lambda}\le1.
\tag{2.2}
\]

Thus (2.1) is an exact fractional matching saturating the root part, with
total mass \(N/L\). No fractional matching has larger mass because every
column consumes \(L\) roots. In particular, every fractional Hall/LP-dual
cut is satisfied. Any obstruction to the desired packing is integral and
correlated, not scalar or fractional.

## 3. Exact leave invariants

Let \({\cal M}\subseteq{\cal C}_r\) be any integral joint matching and
write

\[
                         c=|{\cal M}|.
\]

Let \(z_R\) and \(z_M\) be the numbers of uncovered roots and owners.

### Theorem 3.1 (cardinality and coordinate-regular leaves)

For every integral joint matching,

\[
 z_R=N-Lc,
 \qquad
 z_M=W-Lrc=(\lambda-r)N+r z_R.
\tag{3.1}
\]

Moreover both leaves are exactly coordinate-regular. For every coordinate
\(x\in[2m]\),

\[
 \#\{A\text{ uncovered root}:x\in A\}
                         ={kz_R\over L},
\tag{3.2}
\]

and

\[
 \#\{U\text{ uncovered owner}:x\in U\}
                         ={z_M\over2}.
\tag{3.3}
\]

In particular

\[
 z_R\equiv N\pmod L,\qquad
 L\mid kz_R,\qquad 2\mid z_M.
\tag{3.4}
\]

#### Proof

Each selected orbit contains \(L\) roots and \(Lr\) owners, proving the
first two expressions in (3.1). Since \(W=\lambda N\), the third follows.

In one root orbit, translating the fixed \(k\)-position template through
all \(L\) starts makes every coordinate occur exactly \(k\) times. Hence
the selected root degree at every coordinate is \(kc\). The complete
root layer has coordinate degree \(kN/L\), which proves (3.2).

For each of the \(r\) owner phases, translating its fixed \(m\)-position
template through all \(L\) starts makes every coordinate occur exactly
\(m\) times. One selected orbit therefore contributes \(rm\) owner
occurrences at every coordinate. The complete middle layer has coordinate
degree \(mW/L=W/2\), proving (3.3). Integrality gives (3.4). \(\square\)

The congruences are not an asymptotic no-go: one may allow an
\(o(N)\)-sized structured leave. They do show that an independently
scattered leave cannot be the endpoint of an exact packing argument.

If \(z_R=o(N)\), then (3.1) gives

\[
 z_M\le N+r z_R=o(W),
\tag{3.5}
\]

because \(N/W=1/\lambda=o(1)\) and \(rN=(1+o(1))W\). Thus a
near-perfect joint matching is quantitatively sufficient for global owner
simplicity.

## 4. What \(s\eta_m=o(1)\) does prove

Let \(D_0=D_M\). The degree ratio satisfies

\[
                         1\le {D_R\over D_0}<1+{1\over r},
\]

so the joint catalogue is \((1+o(1))D_0\)-regular. For a column \(C\),
define

\[
 \sigma(C)={1\over sD_0}
   \sum_{\{u,v\}\subset C}\operatorname{codeg}(u,v).
\tag{4.1}
\]

The maximum relative codegree bound gives

\[
                         \sigma(C)\le{s-1\over2}\eta_m=o(1).
\tag{4.2}
\]

Independently mark every column with probability

\[
                         p={\gamma\over sD_0},
 \qquad 0<\gamma\le1,
\tag{4.3}
\]

and retain a marked column only if it meets no other marked column. The
retained columns form a matching. The standard two-term Bonferroni count,
with (4.2), gives uniformly for every resource

\[
 \Pr(\text{resource is covered})
     ={\gamma e^{-\gamma}+o(1)\over s}.
\tag{4.4}
\]

Therefore some integral bite covers

\[
                         {\gamma e^{-\gamma}+o(1)\over s}
\tag{4.5}

of all joint resources. This argument is uniform in the growing rank.

It is only a one-bite theorem. Reaching an \(o(1)\) leave would require
\(\Theta(s\log(1/\varepsilon))\) regenerated bites. Time-zero pair
codegrees do not prove that the residual catalogue remains regular or
that complete FIFO columns remain available.

The exact product-residual variance calculation in
`MATH_LEMMA_GROWING_UNIFORMITY_REGENERATIVE_NIBBLE_20260726.md` already
shows the methodological limitation:

\[
 s\Delta_2/D=o(1)
 \quad\text{does not imply hereditary residual regeneration.}
\tag{4.6}
\]

No hand proof is presently known which upgrades (0.4), by itself, to a
near-perfect matching for growing \(s\). Equally, the usual projective-
plane example has \(s\Delta_2/D\asymp1\), not \(o(1)\), and therefore is
not a counterexample to such a strengthened statement. One must not claim
either a theorem or a counterexample beyond (4.4)--(4.6).

## 5. Sharp product-residual collapse

Independently retain every root and owner resource with probability
\(0<u<1\). Since a complete column contains \(s\) distinct resources,

\[
 \mathbb E\bigl[\#\text{ surviving complete columns}\bigr]
                         =(L-1)!u^s.
\tag{5.1}
\]

At the reduced scale,

\[
 {\log((L-1)!)\over s}
={\log(2m)+O(1)\over r+1}=1+o(1).
\tag{5.2}
\]

Consequently, for every fixed \(\varepsilon>0\), if

\[
                         u<e^{-1-\varepsilon},
\tag{5.3}
\]

then the right side of (5.1) is \(e^{-\Omega_\varepsilon(s)}\). Markov's
inequality gives

\[
 \Pr(\text{at least one complete FIFO column survives})=o(1).
\tag{5.4}
\]

The same threshold appears locally:

\[
                         D_Ru^{s-1}=e^{-\Omega_\varepsilon(s)}
\tag{5.5}
\]

is the expected surviving degree of a fixed retained root, up to the
smaller owner degree.

Thus a product-like residual stalls at a positive-density plateau. A
successful packing, if it exists, must leave a highly correlated,
coordinate-regular residual of the form forced by Theorem 3.1.

### Theorem 5.1 (singleton-regularity still does not regenerate)

Assume the calibrated scale and the no-complement hypotheses

\[
 H\ge2,\qquad r\ge2,\qquad r(2H-1)<\ell-1.
\tag{5.6}
\]

For every fixed \(\varepsilon>0\), there are, for all sufficiently
large \(m\), positive-density residual families \({\cal R}\) of roots
and \({\cal M}\) of owners satisfying all exact identities (3.1)--(3.4)
for some integer \(c\), with

\[
 {|{\cal M}|\over W}<e^{-1-\varepsilon},
\tag{5.7}
\]

such that the faithful residual catalogue has no column.

#### Proof

Put \(u=e^{-1-2\varepsilon}\) and

\[
 c=\left\lfloor{(1-u)W\over Lr}\right\rfloor,\qquad
 z=N-Lc,\qquad d=W-Lrc.
\tag{5.8}
\]

Then

\[
 z/N=u+O(1/r),\qquad d/W=u+o(1),
\tag{5.9}
\]

so both residual densities are positive and (5.7) holds.

For the coordinate cycle \(\tau=(1\,2\,\cdots\,L)\), all but \(o(N)\)
members of the root layer lie in full \(\tau\)-orbits. Indeed, all
non-full binary necklaces together have at most
\(L2^{L/2}=o(\binom Lk)\) labelled words. Remove any \(c\) full
orbits from the root layer; enough exist because
\[
                         {c\over N/L}
                         =(1-u){\lambda\over r}+o(1)
                         <1-{u\over2}
\]
eventually. Their complement \({\cal R}\) has size
\(z\), and every coordinate has residual degree \(kz/L\).

Partition the owner layer into its \(W/2\) complementary pairs.
The integer \(d\) is even. Choose exactly \(d/2\) complement-pairs.
Their union \({\cal M}\) has size \(d\) and coordinate degree \(d/2\)
at every coordinate. By the no-complement theorem, the \(Lr\) owners
of a faithful column lie in distinct complement-pairs. A uniformly
chosen \(d/2\)-pair family therefore contains the complete owner
support of a fixed column with probability

\[
 { (d/2)_{Lr}\over(W/2)_{Lr}}
 \le(d/W)^{Lr}.
\tag{5.10}
\]

There are \((L-1)!\) columns and

\[
 {\log((L-1)!)\over Lr}=1+o(1).
\tag{5.11}
\]

Thus the expected number of surviving columns is
\(\exp[-\Omega_\varepsilon(Lr)]<1\). Some exact complement-pair
choice has none. The cardinality and singleton equations agree exactly
with (3.1)--(3.4) by construction. \(\square\)

The family just constructed is not proved reachable as the leave of a
partial matching. Therefore Theorem 5.1 is not a counterexample to a
global near-perfect matching. It is, however, a deterministic
counterexample to regeneration from the exact scalar, congruence, and
singleton-marginal state alone.

The stronger Gaussian-profile version also passes. If the \(c\) full
root coordinate-shift orbits and the \(d/2\) owner complement-pairs are
chosen uniformly, then, simultaneously for every
\(1\le q\le H\) and \(T\in\binom{[L]}q\),

\[
\begin{aligned}
 \deg_{\cal R}(T)
   &=\left({|{\cal R}|\over N}+o(1)\right)
      \binom{L-q}{k-q},\\
 \deg_{\cal M}(T)
   &=\left({|{\cal M}|\over W}+o(1)\right)
      \binom{L-q}{m-q}.
\end{aligned}
\tag{5.12}
\]

For sampling \(p\) blocks without replacement with weights in
\([0,b]\), the exposure martingale has differences at most \(b\), so

\[
 \Pr(|X-\mathbb EX|\ge t)
 \le2\exp(-t^2/(2pb^2)).
\tag{5.13}
\]

Apply this with \(b=L\) to root orbits and \(b=1\) to complement-pairs.
At \(q=H\) the complete inclusion degrees are still
\(\exp(\Theta(m))\), while there are at most \(2^L=\exp(O(m))\)
sets \(T\). Relative error \(1/\log m\) therefore gives (5.12)
uniformly with probability \(1-o(1)\). The exceptional non-full root
orbits have total size \(L2^{L/2}\), negligible even relative to the
\(q=H\) degree. Separately, the no-column failure probability is at
most \(\exp[-\Omega_\varepsilon(Lr)]\), so both properties hold for one
choice. Thus unordered inclusion ledgers through the full Gaussian
depth do not regenerate ordered FIFO columns either.

The still stronger conditioned-cylinder statement also passes. Put
\(h=Lr\), \(P=W/2\), \(Q=d/2\), and \(v=Q/P\), and condition the
uniform \(Q\)-pair selection on the event \({\cal D}\) that no FIFO
column survives. With

\[
 v_0=e^{-1-2\varepsilon},\qquad
 \alpha_\varepsilon={1\over4}\min(v_0,1-v_0),
\]

\[
 \kappa_\varepsilon
 =\min\left\{{1\over4},
 {\varepsilon\over4\log(1/\alpha_\varepsilon)}\right\},
\tag{5.14}
\]

every prescribed pattern with \(a\) ones and \(b\) zeros on any
\(j\le\kappa_\varepsilon h\) distinct complement-pair variables obeys

\[
 \Pr(\text{pattern}\mid{\cal D})
 =(1+o(1))v^a(1-v)^b
\tag{5.15}
\]

uniformly. Indeed,

\[
 \Pr({\cal D}^c)
 \le(L-1)!v^h\le e^{-\varepsilon h},
\]

whereas the unconditioned cylinder probability is

\[
 { (Q)_a(P-Q)_b\over(P)_j}
 =(1+o(1))v^a(1-v)^b
 \ge\alpha_\varepsilon^j.
\]

Conditioning changes any event's absolute probability by at most
\(\Pr({\cal D}^c)/(1-\Pr({\cal D}^c))\); division by the last lower
bound gives relative error at most \(2e^{-3\varepsilon h/4}\).
The conditioned law is exactly coordinate-permutation invariant and
every residual in its support is coordinate-regular and dead. Hence
even admissible marginals of a positive linear fraction of the full
owner-bundle rank do not imply regeneration.

For a joint invariant law, take one scalar-compatible
coordinate-regular root residual from Theorem 5.1, apply an independent
uniform coordinate permutation to it, and combine it with the
conditioned owner law. Every realization still has the exact common
scalar and singleton ledgers, and owner-deadness excludes every joint
column.

## 6. Exact remaining theorem

The root-cycle packing problem has been reduced without discarding queue
state to the following integral statement.

> Choose \((1-o(1))N/L\) complete \(F_r\)-orbit columns so that their
> \(L\)-element root supports and \(Lr\)-element owner supports are jointly
> pairwise disjoint.

The exact fractional optimum exists, internal owner collisions are absent,
and pair overlaps satisfy the favorable one-bite condition (0.4). The
faithful flow equations nevertheless leave whole orbit variables, while
independent residual thinning destroys every orbit below density
\(e^{-1}+o(1)\), and Theorem 5.1 shows that even exact
singleton-regular residuals, with all unordered inclusion profiles
through \(H\) asymptotically correct and all admissible cylinders up to
\(\kappa_\varepsilon Lr\) asymptotically Bernoulli, may be empty.
Therefore the unresolved step is a catalogue-specific correlated
rounding/absorption theorem or a literal queue-changing switch.
Neither coefficient one nor the near-perfect packing is claimed here.
