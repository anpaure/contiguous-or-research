# Mixed pair frames: exact owner allocation, type transport, and the cycle gate

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is used.

## 0. Verdict

Let

\[
 \mathcal M=\binom{[2m]}m,
 \qquad W=|\mathcal M|,
 \qquad \mathcal L_q=\binom{[2m]}{m-q},
 \qquad N_q=|\mathcal L_q|,
 \qquad \rho_q={N_q\over W}.
 \tag{0.1}
\]

There is a polynomial catalogue of coordinate perfect matchings with the
following exact integral property. Every middle owner can be assigned to
one catalogue frame, and, independently at every certified lower or upper
depth, every target can be assigned to a frame, so that in every
frame--pair-type bin the assigned middle supply is at least the assigned
target demand. Thus the fixed-frame Gaussian deficit disappears completely
at the **integral pair-type marginal** level.

The proof has two ingredients:

1. the exact size-bias identity

   \[
    \pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f);
    \tag{0.2}
   \]

2. total unimodularity of two bipartite allocation networks.

This is not yet a literal pair-flip transport. After the marginal
allocation, targets in a bin must still be matched to compatible assigned
owners. The exact remaining condition is the family of Hall inequalities

\[
 |\Gamma_{j,f,q}(\mathcal Z)\cap A_{j,f}|
       \ge |\mathcal Z\cap B_{j,f,q}|
 \quad\hbox{for every }\mathcal Z\subseteq\mathcal L_{j,f,q}.
 \tag{0.3}
\]

These inequalities are not implied by the bin cardinalities. Still further,
the assigned owners in each frame must be unions of complete isometric
cycles and the depthwise matchings must be prefixes of the same cycle order.

There is also an exact cycle-level congruence. An isometric \(2h\)-cycle in
an \(h\)-cube meets every coordinate star in \(0,h\), or \(2h\) vertices.
Consequently, if full cycles cover all middle owners except a residual set
\(R\), then

\[
 |R\cap\{X:a\in X\}|\equiv {W\over2}\pmod h
 \quad(a\in[2m]).
 \tag{0.4}
\]

In particular, a cycle-only exact cover requires \(2h\mid W\). This gives a
concrete obstruction to promoting the owner allocation mechanically to
whole cycles. It is only a bounded-residual obstruction in the intended
asymptotic compiler, not a renewed coefficient-one obstruction.

The correct conclusion is therefore:

\[
 \boxed{\text{mixed frames solve integral type capacity; the live gate is
 face-Hall plus coherent cycle bundling.}}
 \tag{0.5}
\]

**Subsequent coherence audit.**  The all-depth nested-prefix part has an
exact TU extension once physical targets are assigned to frame copies:
one layered split-node pair-flip network rounds every feasible fractional
solution integrally and is characterized by Hoffman cuts.  The proof and
the coupled model are in
`MATH_THEOREM_MIXED_FRAME_NESTED_FLOW_AND_CYCLE_COUPLING_20260726.md`.
That note also locates two genuine boundaries.  Variable target-frame
certificate rows give a determinant-two, fractionally feasible but
integrally infeasible two-depth instance; complete cycle variables give
an actual fractional exact-cover gap inside `Q_3`.  Thus TU survives
simultaneous depths conditionally on the target-frame partition, but not
the two subsequent coupling decisions.

## 1. Pair-frame incidence

Let

\[
 \mathscr P=(P_1,\ldots,P_J)
 \tag{1.1}
\]

be a catalogue of perfect matchings of \([2m]\). For a mask \(A\) and a
frame \(P_j\), let \(f_j(A)\) be the number of coordinate pairs fully
contained in \(A\).

For a middle owner \(X\), its type in frame \(j\) is

\[
 f_j(X)=f,
 \qquad s=m-2f
 \tag{1.2}
\]

with \(s\) split pairs. For a lower target \(T\in\mathcal L_q\), type \(f\)
means

\[
 f\text{ full pairs},\qquad f+q\text{ empty pairs},
 \qquad m-2f-q\text{ split pairs}.
 \tag{1.3}
\]

The exact source and target orbit sizes in one frame are

\[
 V_f={m!\over f!^2(m-2f)!}\,2^{m-2f},
 \tag{1.4}
\]

\[
 T_{f,q}={m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
 \tag{1.5}
\]

Write

\[
 \lambda_{f,q}:={V_f\over T_{f,q}}
   ={2^q\binom{f+q}{q}\over\binom{m-2f}{q}}.
 \tag{1.6}
\]

For fixed \(j,f,q\), define the literal compatibility graph

\[
 G_{j,f,q}=(\mathcal M_{j,f},\mathcal L_{j,f,q};E_{j,f,q}).
 \tag{1.7}
\]

Here \(\mathcal M_{j,f}=\{X:f_j(X)=f\}\),
\(\mathcal L_{j,f,q}=\{T:f_j(T)=f\}\), and

\[
 T\sim_j X
 \quad\Longleftrightarrow\quad
 T\subset X\quad\hbox{and every element of }X\setminus T
 \hbox{ lies in a split }P_j\hbox{-pair of }X.
 \tag{1.8}
\]

The second condition says exactly that the elements of \(X\setminus T\)
can be deleted by \(q\) distinct pair flips.

### Lemma 1.1 (exact biregular degrees)

The graph \(G_{j,f,q}\) is biregular. Its degrees on the source and target
sides are respectively

\[
 d^{\rm src}_{f,q}=\binom{m-2f}{q},
 \qquad
 d^{\rm tar}_{f,q}=2^q\binom{f+q}{q}.
 \tag{1.9}
\]

Thus

\[
 {d^{\rm tar}_{f,q}\over d^{\rm src}_{f,q}}
       ={V_f\over T_{f,q}}=\lambda_{f,q}.
 \tag{1.10}
\]

#### Proof

From a source \(X\), choose the \(q\) split pairs whose currently selected
elements are deleted. This gives the first degree. From a target \(T\),
choose \(q\) of its \(f+q\) empty pairs and one of the two coordinates in
each chosen pair to adjoin. This gives the second degree. Double-counting
edges gives (1.10). \(\square\)

If the full source and target orbits are retained and \(V_f\ge T_{f,q}\),
biregularity itself proves Hall on the target side: for
\(\mathcal Z\subseteq\mathcal L_{j,f,q}\),

\[
 d^{\rm tar}_{f,q}|\mathcal Z|
 \le d^{\rm src}_{f,q}|\Gamma(\mathcal Z)|,
 \tag{1.11}
\]

so \(|\Gamma(\mathcal Z)|\ge\lambda_{f,q}|\mathcal Z|\ge|\mathcal Z|\).
The fixed-frame obstruction occurs precisely because this fails in the
orbits with \(\lambda_{f,q}<1\).

## 2. The exact full transport problem

The mixed-frame problem can be written without any asymptotic language.
Introduce binary variables

\[
 y_{X,j}\in\{0,1\}
 \tag{2.1}
\]

and, for every certified depth \(q\),

\[
 u^q_{T,X,j}\in\{0,1\}.
 \tag{2.2}
\]

The intended meanings are that owner \(X\) uses frame \(j\), and that the
depth-\(q\) occurrence starting at \(X\) is allocated to \(T\) in that
frame. The exact one-depth transport constraints are

\[
 \sum_jy_{X,j}=1\qquad(X\in\mathcal M),
 \tag{2.3}
\]

\[
 \sum_{X,j}u^q_{T,X,j}=1\qquad(T\in\mathcal L_q),
 \tag{2.4}
\]

\[
 \sum_Tu^q_{T,X,j}\le y_{X,j}
       \qquad(X\in\mathcal M,\ j\in[J]),
 \tag{2.5}
\]

and

\[
 u^q_{T,X,j}=0\quad\hbox{unless }T\sim_jX.
 \tag{2.6}
\]

The same variables with reverse pair flips give the upper equations.

Equations (2.3)--(2.6) still omit two physical conditions.

* **Nested-prefix condition.** For a fixed \((X,j)\), the targets selected
  at depths \(1,\ldots,H\) must be

  \[
    X\setminus\{x_1\},
    X\setminus\{x_1,x_2\},\ldots,
    X\setminus\{x_1,\ldots,x_H\}
    \tag{2.7}
  \]

  for one order of distinct split-pair representatives.

* **Cycle condition.** Owners with frame \(j\) must be grouped into
  complete isometric cycles whose transition orders induce (2.7).

If \(\mathscr C_j\) is the catalogue of allowed isometric cycles in frame
\(j\), both conditions are expressed by cycle variables \(x_C\in\{0,1\}\):

\[
 \sum_{j}\sum_{C\in\mathscr C_j:X\in C}x_C=1
       \qquad(X\in\mathcal M),
 \tag{2.8}
\]

\[
 \sum_j\sum_{C\in\mathscr C_j}
       a^-_{C,q}(T)x_C\ge1
       \qquad(T\in\mathcal L_q, 1\le q\le H),
 \tag{2.9}
\]

with the complementary upper inequalities. Here \(a^-_{C,q}(T)\) is the
number of forward \((q+1)\)-vertex paths of \(C\) whose intersection is
\(T\). For a lower-rainbow factor it is \(0\) or \(1\). In an exact band
SCD, (2.9) is replaced by equality; the displayed inequality is the weaker
coverage gate needed by the direct coefficient-one compiler.

The remainder of the note proves the integral projection of (2.3)--(2.9)
onto the pair-type cardinalities. It does not assert (2.6)--(2.9).

## 3. Size bias and a uniform polynomial catalogue

Let

\[
 \pi_0(f)={V_f\over W},
 \qquad
 \pi_q(f)={T_{f,q}\over N_q}.
 \tag{3.1}
\]

For a uniformly random coordinate perfect matching, these are respectively
the type laws of a fixed middle owner and a fixed depth-\(q\) lower target.
Equation (1.6) gives the pointwise identity

\[
 \boxed{
   \pi_q(f)\lambda_{f,q}=\rho_q^{-1}\pi_0(f).}
 \tag{3.2}
\]

In particular, for every type set \(\mathcal B\),

\[
 \mathbb E_{\pi_q}
   [\lambda_{F,q}{\bf1}_{F\in\mathcal B}]
 =\rho_q^{-1}\Pr_{\pi_0}(F\in\mathcal B).
 \tag{3.3}
\]

Choose a fixed \(A>0\) and put

\[
 \mathcal B=\{f:|f-\mu_0|\le A\sqrt{m\log m}\},
 \qquad
 \tau=\Pr_{\pi_0}(F\notin\mathcal B),
 \tag{3.4}
\]

where \(\mu_0=m(m-1)/(2(2m-1))\). Let

\[
 \alpha=J(1-\tau).
 \tag{3.5}
\]

### Definition 3.1 (uniform mixed-frame catalogue)

The catalogue \(\mathscr P\) is \((\varepsilon,\mathcal B,H)\)-uniform if
the following hold.

For every middle owner \(X\), with

\[
 I(X)=\{j:f_j(X)\in\mathcal B\},
 \qquad a_X=|I(X)|,
 \tag{3.6}
\]

one has

\[
 (1-\varepsilon)\alpha\le a_X\le(1+\varepsilon)\alpha.
 \tag{3.7}
\]

For every \(1\le q\le H\) and every \(T\in\mathcal L_q\), put

\[
 S_{T,q}=\sum_{j:f_j(T)\in\mathcal B}
                   \lambda_{f_j(T),q}.
 \tag{3.8}
\]

Then

\[
 (1-\varepsilon){\alpha\over\rho_q}
 \le S_{T,q}\le
 (1+\varepsilon){\alpha\over\rho_q}.
 \tag{3.9}
\]

### Lemma 3.2 (polynomial catalogues exist)

For \(H\le C\sqrt{m\log m}\) and any fixed \(A,C\), there is a polynomial
\(J=m^{O_{A,C}(1)}\) and an
\((m^{-3},\mathcal B,H)\)-uniform catalogue.

#### Proof

Choose the frames independently and uniformly. For a fixed owner, each
indicator in (3.6) has expectation \(1-\tau\). Chernoff's inequality gives
failure probability \(\exp(-\Omega(\varepsilon^2J))\).

For a fixed target, (3.3) says that each summand in (3.8) has expectation
\((1-\tau)/\rho_q\). On \(\mathcal B\), direct expansion of (1.6) gives

\[
 \lambda_{f,q}\le m^{K(A,C)}.
 \tag{3.10}
\]

Bernstein's inequality therefore gives exponentially small failure in a
fixed positive power of \(m\) once the exponent in \(J\) is sufficiently
large. Increase that exponent so that both failure probabilities are below
\(\exp(-3m)\). There are fewer than \(4^m\) masks in all relevant ranks and
only polynomially many depths. A union bound leaves positive probability
that (3.7) and (3.9) hold simultaneously. \(\square\)

This is the precise role of size bias: an ordinary uniformly chosen frame
gives the wrong target type profile, while weighting its target incidence
by \(\lambda_{f,q}\) converts that profile exactly into the middle type law.

## 4. Integral owner-to-frame allocation

We use the following elementary rounding fact.

### Lemma 4.1 (bipartite degree rounding)

Let \(G=(L,R;E)\) carry nonnegative edge weights \(w_e\) with

\[
 \sum_{e\ni x}w_e=1\qquad(x\in L).
 \tag{4.1}
\]

Write \(d_r=\sum_{e\ni r}w_e\). There is an integral map
\(\phi:L\to R\), using only edges of \(G\), such that

\[
 |\phi^{-1}(r)|\in\{\lfloor d_r\rfloor,\lceil d_r\rceil\}
 \qquad(r\in R).
 \tag{4.2}
\]

#### Proof

Give every left vertex supply one and every right vertex the integer lower
and upper capacities \(\lfloor d_r\rfloor\) and \(\lceil d_r\rceil\).
The weights \(w\) are a feasible fractional flow. The incidence matrix of
a bipartite network is totally unimodular, so the feasible flow polytope has
an integral vertex. At that vertex every left supply travels on one edge,
and (4.2) holds. \(\square\)

For an allowed incidence \((X,j)\), give the edge from \(X\) to the bin
\((j,f_j(X))\) weight

\[
 y_{X,j}={1\over a_X}.
 \tag{4.3}
\]

The weights from every owner sum to one. For \(f\in\mathcal B\), define the
fractional supply in bin \((j,f)\) by

\[
 B_{j,f}=\sum_{X:f_j(X)=f}{1\over a_X}.
 \tag{4.4}
\]

Because the full frame-\(j\), type-\(f\) orbit has size \(V_f\), (3.7)
gives

\[
 {V_f\over(1+\varepsilon)\alpha}
 \le B_{j,f}\le
 {V_f\over(1-\varepsilon)\alpha}.
 \tag{4.5}
\]

Applying Lemma 4.1 gives an integral assignment \(\phi(X)\in I(X)\). Put

\[
 A_{j,f}=\{X:\phi(X)=j, f_j(X)=f\},
 \qquad b_{j,f}=|A_{j,f}|.
 \tag{4.6}
\]

Then

\[
 \boxed{|b_{j,f}-B_{j,f}|<1.}
 \tag{4.7}
\]

Thus all middle owners have been assigned exactly once, and every chosen
frame is balanced for that owner.

## 5. Integral target-to-frame allocation

For a target \(T\in\mathcal L_q\) and an allowed frame \(j\), define

\[
 z^q_{T,j}={\lambda_{f_j(T),q}\over S_{T,q}}.
 \tag{5.1}
\]

These weights sum to one over \(j\). The fractional target demand entering
bin \((j,f)\) is

\[
 D_{j,f,q}
 =\sum_{T:f_j(T)=f}z^q_{T,j}.
 \tag{5.2}
\]

Using the lower bound in (3.9), the orbit count (1.5), and the cancellation
\(T_{f,q}\lambda_{f,q}=V_f\), one gets the exact estimate

\[
 \boxed{
 D_{j,f,q}
 \le {\rho_qV_f\over(1-\varepsilon)\alpha}.}
 \tag{5.3}
\]

On the other hand, (4.5)--(4.7) give

\[
 b_{j,f}\ge {V_f\over(1+\varepsilon)\alpha}-1.
 \tag{5.4}
\]

Since

\[
 \rho_1={m\over m+1}
 \tag{5.5}
\]

and \(\rho_q\) decreases with \(q\), the choice \(\varepsilon=m^{-3}\)
satisfies, uniformly for \(q\ge1\),

\[
 {\rho_q(1+\varepsilon)\over1-\varepsilon}<1.
 \tag{5.6}
\]

For every \(f\in\mathcal B\), Stirling's formula gives

\[
 {V_f\over W}\ge m^{-K'(A)}.
 \tag{5.7}
\]

Because \(J\) is polynomial whereas \(W\) is exponential, the strict gap
in (5.6), multiplied by the lower bound in (4.5), tends to infinity.
More explicitly,

\[
 b_{j,f}-D_{j,f,q}
 \ge {V_f\over\alpha}
 \left({1\over1+\varepsilon}
       -{\rho_q\over1-\varepsilon}\right)-1,
 \tag{5.8}
\]

and the right side tends to infinity uniformly in the displayed range.
Consequently, for all sufficiently large \(m\),

\[
                         D_{j,f,q}\le b_{j,f}
 \tag{5.9}
\]

simultaneously for every \(j,f\in\mathcal B\) and \(1\le q\le H\).

### Theorem 5.1 (integral mixed-frame pair-type allocation)

For all sufficiently large \(m\), there is a polynomial catalogue
\(\mathscr P\), an integral assignment of every middle owner to one frame,
and, for every \(1\le q\le H\), an integral assignment

\[
 \psi_q:\mathcal L_q\longrightarrow[J]
 \tag{5.10}
\]

such that

\[
 f_{\psi_q(T)}(T)\in\mathcal B
 \tag{5.11}
\]

and

\[
 \boxed{
 \#\{T:\psi_q(T)=j, f_j(T)=f\}
       \le |A_{j,f}|=b_{j,f}}
 \tag{5.12}
\]

for every \(j,f,q\). The same assertion holds simultaneously for the upper
targets, using a separate occurrence slot in the reverse direction.

#### Proof

The owner assignment is (4.6). For a fixed \(q\), form the bipartite
network from targets \(T\in\mathcal L_q\) to allowed type bins
\((j,f_j(T))\). Give each target supply one and bin \((j,f)\) capacity
\(b_{j,f}\). The weights (5.1) form a fractional flow saturating every
target, and (5.9) shows that they respect all bin capacities. Integral
max-flow therefore supplies \(\psi_q\). Repeat independently for every
depth. Lower and upper slots of an oriented cycle are distinct, so the
upper allocation can be rounded independently as well. \(\square\)

After (5.12), one may inject the assigned targets in each bin into its
\(b_{j,f}\) abstract depth-\(q\) source slots. Hence Theorem 5.1 is an exact
integral allocation of the complete pair-type occurrence ledger. There are
no fractional owners and no fractional targets.

The theorem also explains why the slack at depth one matters. The target
load in a typical bin is essentially \(\rho_q\) times its source supply.
The smallest relative reserve is

\[
 1-\rho_1={1\over m+1}.
 \tag{5.13}
\]

Uniform catalogue accuracy must therefore be \(o(1/m)\), not merely
unparameterized \(o(1)\). Polynomial sampling supplies this accuracy.

## 6. What remains: exact face Hall

The injection after Theorem 5.1 ignores which source slots are physically
compatible with which targets. For fixed assigned sets

\[
 A_{j,f}\subseteq\mathcal M_{j,f},
 \qquad
 B_{j,f,q}=\{T:\psi_q(T)=j, f_j(T)=f\},
 \tag{6.1}
\]

literal depth-\(q\) transport is possible inside that bin if and only if

\[
 \boxed{
 |\Gamma_{j,f,q}(\mathcal Z)\cap A_{j,f}|
       \ge |\mathcal Z|
 \quad\hbox{for every }\mathcal Z\subseteq B_{j,f,q}.}
 \tag{6.2}
\]

This is Hall's theorem applied to the induced subgraph of (1.7). Notice
that (5.12) is only the special case \(\mathcal Z=B_{j,f,q}\) with the
neighbourhood replaced by the entire source bin. It does not imply (6.2).

There is a sharp singleton illustration. If a target \(T\) is assigned to
\((j,f)\) but all

\[
 2^q\binom{f+q}{q}
 \tag{6.3}
\]

of its compatible frame-\(j\) sources were assigned to other frames, then
the cut \(\mathcal Z=\{T\}\) fails although (5.12) may have arbitrarily
large slack. Thus a proof of literal transport must round the owner and
target allocations dependently, preserving (6.2).

Even simultaneous validity of (6.2) at every depth is not enough for one
physical path: the matched targets for a source must obey the nested-prefix
condition (2.7). This is the exact growing-depth transport gate.

## 7. The whole-cycle gate and a congruence obstruction

We finally record an invariant that every cycle rounding must respect.

### Lemma 7.1 (antipodal transition positions)

Let \(C\) be an isometric \(2h\)-cycle in \(Q_h\). Every coordinate occurs
twice in its cyclic transition word, and its two occurrences are exactly
\(h\) positions apart. Equivalently, the transition word is \(\pi\pi\) for
a permutation \(\pi\) of the \(h\) coordinates.

#### Proof

Every coordinate must occur an even positive number of times. An arc of
length at most \(h\) in an isometric cycle is a geodesic, so it cannot
repeat a coordinate. Hence every coordinate occurs exactly twice. If its
two occurrences had cyclic separation smaller than \(h\), the intervening
arc would repeat that coordinate and would not be geodesic. The two cyclic
separations sum to \(2h\), so both equal \(h\). \(\square\)

For a ground coordinate \(a\in[2m]\), put

\[
 \mathcal S_a=\{X\in\mathcal M:a\in X\}.
 \tag{7.1}
\]

### Theorem 7.2 (coordinate-star congruence)

Embed an isometric \(2h\)-cycle in the middle layer using any coordinate
pairing. Then

\[
 |C\cap\mathcal S_a|\in\{0,h,2h\}
 \tag{7.2}
\]

for every ground coordinate \(a\). Consequently, if a disjoint family of
such cycles covers \(\mathcal M\setminus R\), then

\[
 \boxed{
 |R\cap\mathcal S_a|\equiv {W\over2}\pmod h
 \quad\hbox{for every }a.}
 \tag{7.3}
\]

In particular, an exact cycle-only partition requires

\[
                         2h\mid W.
 \tag{7.4}
\]

#### Proof

If the pair containing \(a\) is full, empty, or inactive in the fibre,
the indicator of \(a\in X\) is constant on \(C\), giving \(2h\) or zero.
If that pair is an active cube coordinate, Lemma 7.1 says that its two
toggles are antipodal. Exactly \(h\) consecutive cycle vertices contain
\(a\). This proves (7.2).

Every selected cycle therefore contributes zero modulo \(h\) to every
coordinate star. Since

\[
 |\mathcal S_a|=\binom{2m-1}{m-1}={W\over2},
 \tag{7.5}
\]

subtracting the covered set proves (7.3). An exact partition also has
\(|R|=0\), and its blocks all have size \(2h\), proving (7.4). \(\square\)

For example, Kummer's theorem gives

\[
 v_2\binom{2m}m=s_2(m),
 \tag{7.6}
\]

where \(s_2(m)\) is the number of ones in the binary expansion of \(m\).
If \(m\) is a power of two and \(h\) is even, then \(v_2(W)=1\), so
\(2h\nmid W\). No choice or mixture of coordinate frames can partition all
middle owners into such cycles.

This does not kill the coefficient-one programme: a residual family of
\(o(W/H)\) owners may be compiled separately at \(o(W)\) interface cost.
It does show that Theorem 5.1 cannot be promoted to a cycle theorem by an
unqualified integrality argument. The residual set must satisfy all the
congruences (7.3), and each frame-type count supplied by full \(2h\)-cycles
is itself a multiple of \(2h\).

## 8. Exact successor statement

The fixed-frame capacity obstruction is removed at the strongest marginal
level one could ask for: all sources and all targets are integral, one
common source-frame assignment works at every depth, and every pair-type
bin has the necessary capacity with the sharp reserve beginning at
\(1/(m+1)\).

What is not proved is precisely the following.

> **Mixed-frame coherent cycle theorem.** Choose the owner-frame assignment
> so that (i) every induced graph satisfies the Hall inequalities (6.2),
> (ii) the matchings for successive depths are nested prefixes, and (iii)
> all but \(o(W/H)\) assigned owners form complete isometric cycles within
> their assigned frames, with the residual satisfying (7.3).

Theorem 5.1 proves the projection of this statement onto all pair-type
counts. Therefore no pair-type or Gaussian-capacity obstruction remains.
Any negative result from this point must exhibit either a genuine induced
Hall cut, a failure of simultaneous nested transport, or a cycle-lattice
invariant beyond the explicit congruences above.
