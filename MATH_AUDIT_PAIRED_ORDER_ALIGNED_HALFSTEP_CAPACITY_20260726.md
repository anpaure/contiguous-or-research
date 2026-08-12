# Paired-order traces: exact aligned and half-step capacity cuts

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

## 0. Verdict

Consider the parity complete-mapping lift on

\[
 Q_{2r}=Q_r^p\times Q_r^x,
 \qquad E=\{p:|p|\equiv0\pmod2\},
\]

and suppose every coarse row factor has doubled-permutation direction
words.  For one fixed signed trace map there are

\[
                         A_r=|E|,2^r=2^{2r-1}                 \tag{0.1}
\]

aligned starts.  At completed-pair depth \(d\), their traces lie in an
alphabet of size

\[
                         M_{r,d}=\binom rd4^{r-d}.              \tag{0.2}
\]

Consequently the collision excess is at least

\[
 \boxed{\left(2^{2r-1}-\binom rd4^{r-d}\right)_+.}             \tag{0.3}
\]

This bound is independent of the complete-mapping equations.  In
particular, at \(d=r/2\),

\[
 \frac{M_{r,r/2}}{A_r}
 =\frac{2\binom r{r/2}}{2^r}=O(r^{-1/2}),                       \tag{0.4}
\]

so all but an \(O(r^{-1/2})\) fraction of the aligned starts are collision
excess.  Thus no family of neighbour permutations can have
\(o(2^{2r})\) aligned collision excess simultaneously through \(r/2\),
whether or not it is affine and whether or not every parity complete
mapping is satisfied.

For the nonconstant \(r=4\) affine seed, depth \(d=2\) already has

\[
                         A_4=128,\qquad M_{4,2}=96,              \tag{0.5}
\]

and hence at least 32 aligned collisions for each sign.  This resolves
the proposed half-depth finite-seed gate negatively without inspecting
the seed.

The small-depth boundary is different.  At \(d=1\) the aligned code is
exactly injective whenever the rows have no 2-cycles.  At \(d=2\) and
\(r\ge3\), it is injective inside each fixed context \(p\); every remaining
fibre has size at most two and couples precisely the two even completions
of \(p\) on its two erased coordinates.  Counting alone is silent at
\(d=2\) once \(\binom r2\ge8\).

The half-step alphabets are larger, and their central-depth counts alone
do not obstruct injectivity.  This does not rescue the requested
simultaneous theorem, because its aligned member has the cut (0.3).

## 1. Exact aligned trace alphabet

Write the two directions in local pair \(i\) as \(a_i,b_i\), and encode
an abstract cube state by

\[
                         x_i=a_i,\qquad p_i=a_i\oplus b_i.       \tag{1.1}
\]

At an even-time start, a coarse direction \(i\) expands as the adjacent
physical moves \(b_i,a_i\).  An aligned window of \(2d\) physical moves
therefore completes a set \(J\subseteq[r]\) of \(d\) local pairs.

For either sign, its physical trace is represented exactly by

\[
 \mathcal C_d(p,x)
   =\bigl(J,\ x|_{J^c},\ p|_{J^c}\bigr).                         \tag{1.2}
\]

Indeed, on a completed pair both abstract directions have varied, so the
two corresponding physical exchange pairs are empty in the lower trace
and full in the upper trace.  On every untouched local pair, the two
unchanged choices are recovered from \((x_i,p_i)\).  In particular the
physical trace identifies \(J\); an untouched abstract direction still
contributes one of its two physical points and cannot masquerade as a
completed direction.

For fixed \(J\), there are \(4^{r-d}\) outside assignments.  This proves
(0.2).

### Theorem 1.1 (aligned Hall cut)

Let \(n_c\) denote the number of aligned starts producing trace code
\(c\).  For either sign,

\[
 \sum_c(n_c-1)_+
 =A_r-|\{c:n_c>0\}|
 \ge A_r-M_{r,d}.                                             \tag{1.3}
\]

When the right side is negative it may be replaced by zero.

#### Proof

The identity in (1.3) is fibrewise.  Equation (1.2) places every used
code in a universe of size (0.2).  No ownership or independence
assumption enters.  The same code universe represents the lower and upper
signs, with completed pairs empty or full respectively. \(\square\)

Thus near-injectivity at depth \(d\) has the necessary information
inequality

\[
                         \frac{2\binom rd}{4^d}\ge1-o(1).       \tag{1.4}
\]

This is an exact Hall cut: take as left shore all aligned starts and as
right shore all possible codes (1.2).

## 2. Half depth and the necessary dimension slack

For \(r=2s\),

\[
 \frac{\binom{2s}s}{4^s}
 =\prod_{j=1}^s\left(1-\frac1{2j}\right)
 \le \exp\!\left(-\frac12\sum_{j=1}^s\frac1j\right)
 \le\frac1{\sqrt{s+1}}.                                      \tag{2.1}
\]

Combining (2.1) with (1.3) gives

\[
 \sum_c(n_c-1)_+
 \ge\left(1-\frac2{\sqrt{s+1}}\right)2^{2r-1}                 \tag{2.2}
\]

at \(d=r/2\).  This proves the claimed \(1-O(r^{-1/2})\) excess
without Stirling's formula.

There is also a useful growing-window consequence.  Put

\[
                         r=2H+u.                                \tag{2.3}
\]

The elementary maximum-binomial bound following from (2.1), with the
odd case obtained by adjoining one Bernoulli bit, is

\[
 \binom rH\le
 \frac{2^r}{\sqrt{\lfloor r/2\rfloor+1}}.                      \tag{2.4}
\]

Therefore

\[
 \frac{M_{r,H}}{A_r}
 \le \frac{2^{u+1}}{\sqrt{\lfloor r/2\rfloor+1}}.               \tag{2.5}
\]

In particular, if

\[
 u\le\left(\frac12-\varepsilon\right)\log_2 r,                 \tag{2.6}
\]

then all but \(O(r^{-\varepsilon})\) of the aligned starts are collision
excess.  Merely avoiding this information cut through depth \(H\)
requires

\[
                         r-2H\ge\frac12\log_2 r-O(1).            \tag{2.7}
\]

This is necessary, not sufficient.

If every row is a \(C_{2r}\)-factor, then \(2r\mid2^r\), so \(r\) must
be a power of two.  Hence the relevant nontrivial values of \(r\) are
even, and the half-depth specialization above applies literally.

## 3. The exact small-depth boundary

### Proposition 3.1 (depth one)

Assume \(r\ge2\) and every \(F_p\) has no 2-cycle.  Then the aligned code
\(\mathcal C_1\) is injective.

#### Proof

Suppose two starts have the same code, with completed direction \(i\).
Equality of \(p|_{[r]\setminus\{i\}}\), together with even parity,
determines \(p_i\), so their contexts are equal.  Equality of the outside
\(x\)-bits leaves either the same phase or the two endpoints of the
\(i\)-edge.  In the latter case both endpoints select direction \(i\),
and \(F_p\) has that edge as a directed 2-cycle.  This is excluded.
\(\square\)

In particular every \(C_{2r}\)-row factor with \(r\ge2\) passes the
aligned depth-one code test.  The complete-mapping equations are not
needed for this conclusion.

### Proposition 3.2 (depth-two fibres are cross-context pairs)

Assume \(r\ge3\), and every row is an isometric \(C_{2r}\)-factor with a
doubled-permutation direction word.  Then the depth-two code is injective
after fixing \(p\).  Consequently every full code fibre has size at most
two.  If it has size two and its support is \(J=\{i,j\}\), its contexts
are

\[
                         p,\qquad p\oplus e_i\oplus e_j.         \tag{3.1}
\]

#### Proof

Fix \(p,J\), and the outside phase.  Two starts with this data lie in the
same \(J\)-square.  Each associated two-step path uses three vertices of
that square.  Two such paths cannot lie in different row cycles, because
two three-subsets of a four-set intersect while distinct factor cycles
are vertex-disjoint.  They therefore lie on one isometric cycle.

Their start vertices have Hamming distance at most two, so their cyclic
distance is at most two.  Two distinct length-two intervals of a word
\(\pi\pi\), shifted by one or two positions, cannot have the same
unordered direction set when \(r\ge3\): that would repeat one direction
before its next occurrence, which is exactly \(r\) positions later.
Thus the starts coincide.

For a fixed outside restriction on two erased coordinates, even parity
allows exactly two completions, and they differ by
\(e_i\oplus e_j\).  The last assertion and the fibre bound follow.
\(\square\)

At \(r=4,d=2\), Theorem 1.1 forces at least 32 such paired collisions.
For \(r\ge8\), the alphabet inequality is silent because
\(\binom r2\ge8\); Proposition 3.2 identifies the remaining exact
two-context compatibility problem but does not solve it.

## 4. Exact complete-mapping exclusion

For fixed phase \(x\), write \(D_x(p)=d_p(x)\).  The map

\[
                         T_x(p)=p\oplus e_{D_x(p)}                \tag{4.1}
\]

is a bijection \(E\to O\) if and only if

\[
 D_x(p)=i\quad\Longrightarrow\quad
 D_x(p\oplus e_i\oplus e_j)\ne j
 \quad\text{for every }j\ne i.                                \tag{4.2}
\]

#### Proof

If both displayed labels occurred, the two even contexts would have the
same image:

\[
 p\oplus e_i
 =(p\oplus e_i\oplus e_j)\oplus e_j.
\]

Conversely, equality of two images with selected directions \(i,j\)
forces the contexts either to coincide or to differ by
\(e_i\oplus e_j\), which is precisely the forbidden configuration.
Since the shores have equal size, injectivity is bijectivity. \(\square\)

Equation (4.2) is the exact column-Latin constraint.  It removes the
most immediate depth-two collision in which the two contexts start at
the same phase with swapped directions.  It neither enlarges the trace
alphabet nor changes Theorem 1.1.  Thus no affine, Latin-square, or
nonlinear complete mapping can evade the half-depth Hall cut.

## 5. Half-step code capacities

There are two nonaligned physical window types.

First consider an odd-length window with \(0\le d\le r-1\) completed local pairs and
one partial boundary pair.  For either fixed half-step phase, its code is
specified by

* the completed set \(J\), of size \(d\);
* the boundary local pair outside \(J\);
* the one retained abstract endpoint in that pair; and
* the full states of the other \(r-d-1\) local pairs.

Hence its code universe has size at most

\[
 M^{(1)}_{r,d}
 =2(r-d)\binom rd4^{r-d-1}.                                  \tag{5.1}
\]

For the \(A_r\) starts of one fixed phase,

\[
 \frac{M^{(1)}_{r,d}}{A_r}
 =(r-d)\frac{\binom rd}{4^d}.                                  \tag{5.2}
\]

Second, for \(1\le d\le r-1\), an even-length window beginning between the two moves of a local
pair has \(d-1\) completed pairs and two partial boundary pairs.  Their
roles are ordered, and each retains one abstract endpoint.  Therefore

\[
\begin{aligned}
 M^{(2)}_{r,d}
 &=4\binom r{d-1}(r-d+1)(r-d)4^{r-d-1}\\
 &=\binom r{d-1}(r-d+1)(r-d)4^{r-d},                            \tag{5.3}\\
 \frac{M^{(2)}_{r,d}}{A_r}
 &=2\binom r{d-1}\frac{(r-d+1)(r-d)}{4^d}.                     \tag{5.4}
\end{aligned}
\]

The same fibre identity as in (1.3) gives collision lower bounds
\((A_r-M^{(j)}_{r,d})_+\) for these phase-restricted maps.

At \(d=r/2\), both ratios (5.2) and (5.4) exceed one by polynomial
factors as \(r\to\infty\), so these raw half-step counts do not themselves
furnish an asymptotic central cut.  The simultaneous all-phase theorem is
nevertheless false there because its aligned submap already has collision
excess \((1-o(1))A_r\).

## 6. Precise surviving boundary

The proposed theorem is refuted whenever its protected range contains
\(d=r/2\), and more generally whenever (1.4) fails by a fixed amount.
The first nonconstant \(r=4\) affine seed is refuted at \(d=2\) before
any recursive or outer Hall issue arises.

The result does not refute a genuinely shallow construction with
\(H=o(r)\).  In that regime (0.3) and the half-step counts are silent.
The minimum remaining local task is then to solve simultaneously:

1. the whole-cycle row equations and the column-Latin exclusions (4.2);
2. the paired cross-context condition of Proposition 3.2 and its
   higher-depth analogue; and
3. the two half-step fibre systems (5.1)--(5.4).

Any recursive use of the paired lift must therefore take the coarse
dimension beyond twice its maximum completed-pair depth, with at least the
logarithmic slack in (2.7), before an affine or orthogonal-array design
can even enter the nonvacuous range.
