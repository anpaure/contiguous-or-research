# The first-rainbow cycle reduction, an affine-terrace no-go, and the global factor fiber

Date: 2026-07-29

Status: unconditional structural theorems and proof-safe necessary conditions.
This note does **not** prove the decorated-carrier conjecture and does not
change the current bound

\[
6438\leq \nu(15)\leq 6458.
\]

The point is to isolate a smaller exact existence object.  A middle-perfect,
first-lower-rainbow carrier is equivalent to one Hamilton cycle on the lower
middle layer with a second rainbow condition on its edge unions.  All deeper
lower shadows and all upper shadows then become literal intersections and
unions of consecutive vertices of that one cycle.  This gives a proof-safe
global move fiber.  A separate theorem shows why the most obvious affine
run schedule, despite perfect rank, Johnson, residence, and even dual
residence, can never be Hamilton once the Catalan quotient is larger than
the ground set.

Throughout,

\[
 k=2m+1,\qquad r=m+1,\qquad
 W={k\choose r}={k\choose m},\qquad N=W/k.
\]

All sequences in Sections 1--3 are cyclic modulo `W`.

## 1. The exact first-rainbow cycle reduction

Let

\[
 T_i\in { [k]\choose m+1}
\]

be a cyclic Johnson carrier and put

\[
 X_i=T_i\cap T_{i+1}.                              \tag{1.1}
\]

### Theorem 1.1 (one lower Hamilton cycle is the whole `q1` carrier)

The following two descriptions are equivalent.

1. `T` visits every `(m+1)`-set exactly once and the `W` sets `X_i` in
   (1.1) visit every `m`-set exactly once.
2. `X` is a Hamilton cycle of `J(k,m)`, and the `W` edge unions

   \[
       T_{i+1}=X_i\cup X_{i+1}                      \tag{1.2}
   \]

   are pairwise distinct.

In particular, the second condition in (2) says that the edge-union
colouring of the Hamilton cycle `X` is a perfect rainbow over
`binom([k],m+1)`.

If either sequence is a strict unit-voltage spiral, then so is the other,
with the same voltage:

\[
 T_{i+N}=\rho T_i\quad\Longleftrightarrow\quad
 X_{i+N}=\rho X_i.                                  \tag{1.3}
\]

#### Proof

Assume (1).  The two consecutive colours `X_i,X_(i+1)` are distinct
`m`-subsets of `T_(i+1)`.  Hence they are Johnson-adjacent and their union
is `T_(i+1)`, proving (1.2).  The first-rainbow assumption makes `X` a
Hamilton cycle, while middle perfection makes the unions pairwise distinct.

Conversely, assume (2) and define `T` by (1.2).  Each `T_i` has size
`m+1`.  The two sets `T_i,T_(i+1)` both contain `X_i`; they are distinct
because all edge unions are distinct.  Therefore

\[
 T_i\cap T_{i+1}=X_i,
\]

so `T` is a Johnson cycle and its first lower colours are exactly `X`.
There are `W` distinct `(m+1)`-sets and `W` total such sets, so `T` is
middle-perfect.  Equation (1.3) follows by taking intersections or unions,
both of which commute with `rho`.  \(\square\)

### Corollary 1.2 (what is already unconditional)

A Hamilton cycle of the middle-levels graph, projected to its rank-`m`
vertices, supplies an `X` satisfying Theorem 1.1.  Thus simultaneous middle
perfection and exact lower `q1` are not the remaining existence problem.
The strict-equivariant version is supplied by the audited MMM projection.
The missing requirements are residence, deeper lower shadows, upper
shadows, and the compiler interface.

### Corollary 1.3 (the first new condition is a doubly-rainbow cycle)

In the `X` formulation, two separate published theorems give the two first
shadow requirements on two generally different Hamilton cycles:

* the Middle Levels Theorem gives a Hamilton cycle of `J(k,m)` whose edge
  unions enumerate every `(m+1)`-set; and
* the GMM tight-enumeration theorem on levels `{m-1,m}` gives a Hamilton
  cycle of `J(k,m)` whose edge intersections cover every `(m-1)`-set.

By Theorem 2.1 below, a carrier with exact lower `q2` needs one Hamilton
cycle having **both** properties.  Thus the first unresolved shadow gate is
precisely a doubly-rainbow Johnson cycle, followed by residence and the
higher-window conditions.  The two known one-sided cycles certify that
neither palette is individually obstructed.

## 2. Every other carrier shadow is a window of `X`

For `q>=1`, write

\[
 I_i^{(q)}=\bigcap_{a=0}^{q}T_{i+a},\qquad
 U_i^{(q)}=\bigcup_{a=0}^{q}T_{i+a}.
\]

### Theorem 2.1 (exact shadow translation)

Under Theorem 1.1,

\[
 \boxed{I_i^{(q)}=\bigcap_{a=0}^{q-1}X_{i+a}},      \tag{2.1}
\]

and

\[
 \boxed{U_i^{(q)}=\bigcup_{a=-1}^{q}X_{i+a}}.       \tag{2.2}
\]

Consequently:

* lower `q2` coverage is exactly coverage by the edge-intersection colours
  `X_i cap X_(i+1)` of the one cycle `X`;
* upper `q1` coverage is exactly coverage by the three-vertex unions
  `X_(i-1) union X_i union X_(i+1)`; and
* every deeper carrier gate is a consecutive-window condition on the same
  Hamilton cycle `X`, rather than an independent chronology.

#### Proof

For the lower identity,

\[
 \bigcap_{a=0}^{q-1}X_{i+a}
 =\bigcap_{a=0}^{q-1}(T_{i+a}\cap T_{i+a+1})
 =\bigcap_{a=0}^{q}T_{i+a}.
\]

For the upper identity use `T_i=X_(i-1) union X_i` from (1.2) and take the
union over `i,...,i+q`.  \(\square\)

### Corollary 2.2 (residence shifts down one level)

Let `ell` and `g` be the positive-run and zero-gap lengths of a coordinate
trace of `T`.  The corresponding trace of `X_i=T_i cap T_(i+1)` has

\[
 \ell^X=\ell-1,\qquad g^X=g+1.                       \tag{2.3}
\]

Thus carrier residence `ell>=d+1` is equivalent to minimum positive-run
length at least `d` in the lower Hamilton cycle `X`.

#### Proof

The trace of `X` is the one-step forward erosion of the trace of `T`.
Every positive run loses its last point and the following zero gap gains
that point.  A run cannot disappear under the stated first-rainbow carrier
conditions: disappearance would make one of the adjacent intersections
repeat or have the wrong rank.  \(\square\)

Equations (2.1)--(2.3) are the exact form of the proposed “one packet choice
serves many depths” mechanism.  They do not prove that a suitable `X`
exists, but they show that the depths are coupled deterministically rather
than being separate covering instances.

## 3. The global rainbow-`2`-factor fiber

Let `J=J(k,m+1)`.  Every edge `e={A,B}` of `J` has two colours

\[
 \chi(e)=A\cap B\in{[k]\choose m},\qquad
 \psi(e)=A\cup B\in{[k]\choose m+2}.                \tag{3.1}
\]

Introduce one binary variable `x_e` per edge.  Consider the fiber

\[
 \sum_{e:\chi(e)=X}x_e=1
       \quad(X\in{[k]\choose m}),                   \tag{3.2}
\]

\[
 \sum_{e\ni T}x_e=2
       \quad(T\in{[k]\choose m+1}).                 \tag{3.3}
\]

### Theorem 3.1 (exact global state space)

The binary points of (3.2)--(3.3) are exactly the spanning `2`-factors of
`J(k,m+1)` whose edge-intersection colours form a perfect rainbow.  A point
is a single carrier of Theorem 1.1 exactly when the `2`-factor is connected.

Upper `q1` loads are linear on this fiber:

\[
 \mu_A(x)=\sum_{e:\psi(e)=A}x_e.                    \tag{3.4}
\]

Hence upper `q1` coverage is simply `mu_A(x)>=1` for every `(m+2)`-set
`A`.  After orienting each factor component, lower `q2` colours are the
turn colours

\[
 \chi(e_i)\cap\chi(e_{i+1}).                        \tag{3.5}
\]

#### Proof

Equation (3.2) chooses exactly one Johnson edge with each lower colour.
Equation (3.3) gives degree two at every middle vertex, hence a spanning
`2`-factor.  Conversely every first-rainbow spanning `2`-factor satisfies
the equations.  A connected finite `2`-factor is a Hamilton cycle.  Formula
(3.4) is the definition of the upper edge colour, and (3.5) is Theorem 2.1
at `q=2`.  \(\square\)

### Theorem 3.2 (proof-safe complete global moves)

Let `M` be the `0/1` matrix whose rows are the constraints in
(3.2)--(3.3).  A signed integer vector `z` carries one rainbow factor `x`
to another if and only if

\[
 Mz=0,\qquad x+z\in\{0,1\}^{E(J)}.                 \tag{3.6}
\]

In coordinates, this is

\[
 \sum_{e:\chi(e)=X}z_e=0\quad\hbox{for every }X,
 \qquad
 \sum_{e\ni T}z_e=0\quad\hbox{for every }T.        \tag{3.7}
\]

The Graver basis of `M` is a complete Markov basis for this binary fiber:
any two rainbow factors are joined by a sequence of conformal Graver moves,
and every intermediate point remains binary.  No bounded support for these
moves is asserted.

#### Proof

The first assertion is immediate by subtracting the two systems of linear
equations.  For completeness, write the difference of two fiber points as a
conformal sum of Graver elements.  Since the difference has entries only in
`{-1,0,1}`, every conformal partial sum removes only edges present in `x`
and adds only edges absent from `x`; it therefore stays binary.  Each Graver
summand lies in `ker_Z M`, so every intermediate point remains in the fiber.
\(\square\)

This is the proof-safe replacement for bounded endpoint swaps.  It preserves
middle ownership and exact `q1` **by construction**, while its change in the
upper palette is the linear vector

\[
 \Delta\mu_A=\sum_{e:\psi(e)=A}z_e.                 \tag{3.8}
\]

Connectivity, residence, the turn colours (3.5), and the compiler still
have to be audited after a move.  The theorem deliberately does not claim
that primitive moves have small support; the exact `k=15` support-three
closure shows why such a claim would be unsafe.

### Corollary 3.3 (exact strict-equivariant quotient fiber)

Restrict (3.2)--(3.3) to selections invariant under coordinate rotation.
The rotation actions on middle vertices and lower colours are free.  Let
`bar e` run over rotation orbits of Johnson edges and use one binary variable
`y_(bar e)` per edge orbit.  Then the exact quotient equations are

\[
 \sum_{\bar e:\overline\chi(\bar e)=\bar X}y_{\bar e}=1
       \quad\hbox{for every lower-colour orbit }\bar X,       \tag{3.9}
\]

and

\[
 \sum_{\substack{\bar e\text{ nonloop}\\\bar e\ni\bar T}}
       y_{\bar e}
 +2\sum_{\bar e\text{ a loop at }\bar T}y_{\bar e}=2
       \quad\hbox{for every middle-vertex orbit }\bar T.     \tag{3.10}
\]

A quotient loop has coefficient two because its physical lift enters every
vertex of the orbit twice.  Every binary solution lifts to an equivariant
first-rainbow spanning `2`-factor, and every such factor descends to one.
Upper orbit coverage is an ordinary orbit-incidence condition on the chosen
edge orbits; at composite `k` its physical multiplicity must use the actual
upper orbit size.

The integer-kernel and Graver statement of Theorem 3.2 applies verbatim to
this weighted quotient matrix.  At `k=15` it is a genuinely global move
space on the Catalan-size quotient, rather than on all 6,435 physical
middle vertices.

## 4. A structurally perfect affine family that is provably useless

The compact lifetime model makes rank and both residence tails easy.  The
following theorem explains why that alone does not approach Hamiltonicity.

Fix an integer `a` with

\[
 r<a\le k,\qquad \gcd(a,N)=1.                       \tag{4.1}
\]

On the scalar circle `Z_(kN)`, put `N` one-runs

\[
 [ta,ta+r-1],\qquad t=0,1,\ldots,N-1,               \tag{4.2}
\]

and zeros elsewhere.

### Theorem 4.1 (affine terrace and its deck collapse)

The word (4.2) is a legal rank-`r` strict spiral.  Its positive-run lengths
are all `r`; its first `N-1` zero gaps have length `a-r`, and its last zero
gap has length

\[
 (k-a)N+a-r.                                        \tag{4.3}
\]

Thus it has compiler residence with enormous room, and it is dually
resident through every depth below `a-r`.

Nevertheless, among the quotient columns `T_0,...,T_(N-1)` there are at
most `a` distinct literal sets.  In particular, if `N>a`, the carrier is
not Hamilton and cannot have a perfect first lower rainbow.

#### Proof

The start residues are `ta mod N`, a permutation by (4.1), and the end
residues are their translate by `r-1`, also a permutation.  The total
one-mass is `rN`.  Start/end transversality plus the total mass therefore
gives a rank-`r` Johnson spiral.  The displayed run and gap lengths follow
directly from (4.2).

For `0<=j<N` and coordinate `x`, the scalar position defining membership is

\[
 p=(j-xN)_{kN}=j+yN,
 \quad y\equiv-x\pmod k,\quad0\le y<k.
\]

The position `p` lies in a one-run exactly when

\[
 p<aN\quad\hbox{and}\quad p\bmod a<r.               \tag{4.4}
\]

For fixed `x`, the first condition is independent of `j`, and the second
depends on `j` only through `j mod a`.  Hence the entire set `T_j` depends
only on `j mod a`, yielding at most `a` literal columns.  \(\square\)

For `k=9,11,15`, one has respectively `N=14,42,429`, so `N>k>=a` and the
whole affine family is ruled out before any shadow audit.  This includes the
constant-step `k=15` schedule with lifetimes eight, ordinary gaps six, and
one gap enlarged by `N`: it is structurally excellent and deck-degenerate
for a theorem-level reason.  At `k=7`, `N=5` and this numerical obstruction
does not apply, consistent with the exceptional tiny rigidity census.

## 5. Minimum lifetimes are construction resources, not defects

Let a cyclic carrier `T` be cut to a linear carrier of length `W`, and let
`A_0,...,A_(W+d-1)` satisfy `D^d A=T`.  At every two-sided interior source
position

\[
 d+1\le i\le W-2,
\]

the run-boundary argument forces

\[
 \{\alpha_i,\beta_{i-d-1}\}\subseteq A_i.          \tag{5.1}
\]

The two forced coordinates coincide exactly when the run inserted at
transition `i-d-1` has the minimum legal lifetime `d+1`.

### Theorem 5.1 (a minimum-lifetime orbit is necessary for singletons)

If `k>2d+2` and the word `A` covers all singleton targets, then the cyclic
carrier has at least one quotient run of lifetime exactly `d+1`.

#### Proof

If no lifetime is `d+1`, the two coordinates in (5.1) are distinct, so
every interior source letter has size at least two.  There are exactly
`2d+2` remaining boundary source positions.  An interval OR can equal the
singleton `{x}` only if every nonempty source letter in that interval is
itself `{x}`.  Thus each of the `k` distinct singleton targets requires a
distinct singleton source position, impossible using at most `2d+2`
boundary positions.  \(\square\)

In a strict spiral, one quotient minimum run lifts to `k` physical minimum
runs, one for each coordinate.  It therefore creates exactly the right
orbit of singleton-capable forced ports.  The theorem explains why every
known good `k=7,9,11` trace has many minimum lifetimes.  It proves only that
at least one orbit is necessary; the observed abundance is additional Hall
geometry, not a consequence of this count.

## 6. Proof-safe upper-capacity inequalities from the zero gaps

Let the scalar zero gaps be `g_1,...,g_N`, and let

\[
 E_q^+=k\sum_{t=1}^{N}(q-g_t)^+                  \tag{6.1}
\]

be the exact aggregate upper rank deficit.  Put

\[
 M_q={k\choose r+q}.
\]

### Theorem 6.1 (rank-capacity obstruction)

If the depth-`q` upper windows cover every rank-`r+q` target, then

\[
 \boxed{E_q^+\le q(W-M_q).}                          \tag{6.2}
\]

#### Proof

A window with positive rank deficit cannot witness a rank-`r+q` target.
If `B` windows have positive deficit, then `E_q^+<=qB`, so
`B>=E_q^+/q`.  At most `W-B<=W-E_q^+/q` windows can therefore be witnesses.
Coverage requires at least `M_q` witness windows, proving (6.2).  \(\square\)

### Theorem 6.2 (stationary-step obstruction)

Assume `min g_t>=q`, so the depth-`q` upper shadow is rank-exact and lazy
Johnson.  Let `n_q=#{t:g_t=q}`.  If it covers every rank-`r+q` target, then

\[
 \boxed{k n_q\le W-M_q.}                             \tag{6.3}
\]

In particular, because every legal trace has `g_t>=1`, upper `q1` coverage
forces

\[
 \boxed{\#\{t:g_t=1\}
   \le \left\lfloor{W-{k\choose r+1}\over k}\right\rfloor.} \tag{6.4}
\]

#### Proof

The upper depth-`q` chronology has exactly `k n_q` stationary physical
steps.  Contracting them leaves at most `W-k n_q` distinct visited states.
Coverage of `M_q` targets requires `W-k n_q>=M_q`.  \(\square\)

These inequalities are necessary only; nonstationary repetitions can waste
additional capacity.

## 7. Reconciliation with the known strict traces

The following data are direct audits of retained strict traces.  They are
evidence, not additional theorems.

| `k` | `N` | `d+1` | lifetime histogram (abridged) | `#(ell=d+1)` | `#(g=1)` | bound (6.4) |
|---:|---:|---:|---|---:|---:|---:|
| 7 | 5 | 3 | `3^3,4,7` | 3 | 1 | 2 |
| 9 | 14 | 3 | `3^6,4^3,6,7^2,8,12` | 6 | 2 | 4 |
| 11 | 42 | 4 | `4^13,5^17,6^4,7^2,9^2,11,12,15,21` | 13 | 3 | 12 |
| 15 seed | 429 | 4 | minimum `4`, maximum `32` | 112 | 71 | 95 |

Three conclusions are proof-safe.

1. The minimum runs are useful compiler ports, as Theorem 5.1 predicts.
2. Starting at `k=9`, `N>k`, so Theorem 4.1 proves that the attractive
   constant-lifetime affine construction is impossible.  The non-affine
   endpoint permutations and long spines in the actual traces are doing
   real deck-separation work.
3. Every retained trace passes the coarse upper stationary-capacity bound.
   The `k=15` seed is much closer to that bound, but its `95` upper holes are
   not implied by the gap histogram alone.  Orbit collisions remain the
   substantive upper obstruction.

The identities

\[
 \sum_t(\ell_t-(d+1))=(r-d-1)N,
 \qquad
 \sum_t(g_t-1)=(k-r-1)N                            \tag{7.1}
\]

show that every trace distributes the same total positive and zero surplus.
The concentration of that surplus into a few spines is empirical, not
forced by (7.1).

## 8. Exact remaining construction statement

Combining Sections 1--3, the odd-`k` carrier problem can be stated without
raw source words or independent depth variables:

> Find a Hamilton cycle `X` of `J(2m+1,m)` such that its edge unions are a
> perfect rainbow over rank `m+1`, its coordinate runs have minimum length
> `d`, the intersections of every `q` consecutive `X`-vertices cover the
> required lower ranks, and the unions of every `q+2` consecutive vertices
> cover the required upper ranks.  In the strict route, require in addition
> `X_(i+N)=rho X_i`.

Middle Levels/MMM proves the first two clauses in one Hamilton cycle.
Subsequent to the original version of this note, the PBBS two-matching
theorem proved all lower and upper support clauses simultaneously in one
equivariant spanning two-factor.  What remains is their intersection with
one-cycle topology, residence, a safe opening, and the compiler—not raw
shadow support in the ambient factor fiber.

Theorem 3.2 gives a complete global move space in which the first two clauses
are invariant.  Theorem 4.1 says that a local or affine lifetime rule cannot
produce the needed injectivity once `N>k`.  Theorems 5.1 and 6.2 identify the
opposing boundary resources: minimum positive runs are needed by the lower
compiler, while too many minimum zero gaps consume upper-shadow capacity.

### Conjectural direction (not a theorem)

The `k=7,9,11` patterns suggest searching the Graver/circuit fiber of
Theorem 3.2 for factors whose induced scalar schedule concentrates the
forced lifetime surplus into non-affine spines while spreading zero-gap
surplus enough to stay far below (6.4).  There is currently no proof that a
bounded-support circuit family connects the residence-and-shadow-good face,
and the exact `k=15` support-three closure is evidence against assuming one.

## 9. PBBS zero-hole point of the global fiber

For the canonical PBBS odd-graph permutation `f`, define

\[
 M_+(A)=f(A)^c,\qquad M_-(A)=f^{-1}(A)^c,
 \qquad \theta(A)=f^{-1}(A)\cap f(A).                \tag{9.1}
\]

The two `M` maps are edge-disjoint perfect matchings of the middle-levels
incidence graph.  Their union is therefore a binary point of the global
fiber (3.2)--(3.3).  Its upper-`q1` colour at `A` is `theta(A)^c`, and its
lower-`q2` colour at `A^c` is `theta(A)`.  The audited PBBS theorem gives

\[
 1\le |\theta^{-1}(S)|\le3
 \qquad\left(S\in\binom{[2m+1]}{m-1}\right),         \tag{9.2}
\]

so this factor has no holes on either shore.  Rotation equivariance makes it
an exact composite quotient point, with actual stabilizer weights retained.

More generally, every correct PBBS `q`-edge path with intersection `S`
produces a carrier lower-depth-`q+1` window equal to `S` and, on the
complement component, an upper-depth-`q` window equal to `S^c`.  Hence this
single factor has complete correct-window support throughout the Boolean
lattice.

The complete proof, including the exact depth shift, equal complementary
loads, the `Cat_m` component bound, and the `k=15` quotient histogram, is in
`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`.
The PBBS point may contain quotient loops and many components and may fail
residence.  It therefore closes ambient factor feasibility without solving
the Hamilton/resident/compiler intersection posed in Section 8.
