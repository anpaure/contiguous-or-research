# Endpoint-capacity obstruction to sparse PBBS/product-SCD baseline fusion

Date: 2026-07-26

## 0. Result

Put

\[
 n=2m+1,
 \qquad W=\binom{n}{m},
 \qquad N_r=\binom nr.
\]

Fix a PBBS erosion depth `H<m`.  In the compiled central word there are
exactly `W` owner-aligned erosion positions.  Each such position is an
intersection of at most `H+1` consecutive rank-`(m+1)` Johnson owners and
therefore has cardinality at least

\[
                         m+1-H.                       \tag{0.1}
\]

The first lower rank not reached by that erosion floor is

\[
                         r=m-H.                       \tag{0.2}
\]

The theorem below shows that none of the `W` owner-aligned PBBS positions
can be shared directly with the product-SCD lower tail at rank `r`.

### Theorem A (exact endpoint-capacity inequality)

Let `B` be a literal OR word containing `W` distinguished positions whose
letters all have size greater than `r`.  Let `E` be the number of its
other positions.  Form a word `Q` by

1. retaining all positions of `B`, in any order;
2. changing at most `K` distinguished letters arbitrarily; and
3. inserting `R` further positions.

If `Q` covers every rank-`r` subset of `[n]`, then

\[
 \boxed{
                         K+E+R\ge N_r.}              \tag{0.3}
\]

Consequently:

* if all distinguished PBBS letters are retained unchanged, every fused
  word has length at least

  \[
                         W+N_r;                       \tag{0.4}
  \]

* if the fused length is `W+o(W)` and `E=o(W)`, then

  \[
                         K\ge N_r-o(W).               \tag{0.5}
  \]

Thus fusion at coefficient one cannot be an insertion, splice, seam
replacement, or `o(W)`-support perturbation of the PBBS baseline.  It must
physically rewrite at least one baseline endpoint for essentially every
target in the first missing lower rank.

### Gaussian consequences

For `r=m-H`,

\[
 \frac{N_r}{W}
 =\prod_{i=0}^{H-1}\frac{m-i}{m+2+i}.                \tag{0.6}
\]

Hence, if `H=A sqrt(m)+o(sqrt(m))` for fixed `A>=0`,

\[
 \boxed{
                         \frac{N_r}{W}\longrightarrow e^{-A^2}.}
                                                               \tag{0.7}
\]

In particular, a length-`W+o(W)` fusion at a fixed Gaussian cutoff must
rewrite at least

\[
                         (e^{-A^2}-o(1))W             \tag{0.8}
\]

owner-aligned PBBS positions.  At a sub-Gaussian cutoff
`H=o(sqrt(m))`, it must rewrite

\[
                         W-o(W)                       \tag{0.9}
\]

of them.  Therefore the proved sub-Gaussian PBBS word and the proved
product-SCD exterior word cannot be fused by a sparse interface: any such
fusion is necessarily a wholesale rethreading of the baseline.

This is a statewise obstruction.  It does not use independence, entropy,
randomness, or the particular ordering of the retained PBBS positions.

## 1. Endpoint flags

Let

\[
                         Q=(Q_1,\ldots,Q_L)
\]

be an arbitrary literal OR word.  For a right endpoint `t`, its suffix
unions

\[
 F_t(s)=\bigcup_{i=s}^{t}Q_i,
 \qquad 1\le s\le t,                                 \tag{1.1}
\]

form an inclusion chain as `s` decreases.  Call this the endpoint flag at
`t`.

### Lemma 1.1 (rank-filtered endpoint capacity)

At a fixed endpoint `t`:

1. at most one distinct member of the endpoint flag has any prescribed
   rank `r`;
2. if `|Q_t|>r`, no member of the endpoint flag has rank `r`.

Therefore

\[
 \boxed{
 \#\{\text{rank-}r\text{ sets covered by }Q\}
 \le \#\{t:|Q_t|\le r\}.}                            \tag{1.2}
\]

#### Proof

The sets in (1.1) are nested, so two of equal cardinality are equal.  This
proves the first assertion.  Every interval ending at `t` contains the
letter `Q_t`, so its union has cardinality at least `|Q_t|`; this proves
the second assertion.  Assign every witnessed rank-`r` target to the
right endpoint of one of its witnessing intervals and sum.  \(\square\)

Lemma 1.1 is stronger than the usual one-mask-per-rank-per-endpoint bound:
it identifies exactly which endpoints are even eligible at the rank.

## 2. Proof of Theorem A

After the allowed operations, every unchanged distinguished position has
letter size greater than `r`.  Hence the only rank-`r`-eligible endpoints
are

* the `K` changed distinguished positions;
* the `E` original nondistinguished positions; and
* the `R` inserted positions.

Lemma 1.1 therefore bounds the number of covered rank-`r` targets by
`K+E+R`.  Covering all `N_r` targets gives (0.3).

If `K=0`, then `R>=N_r-E`; since the original word has length `W+E`, the
fused word has length at least

\[
                         W+E+N_r-E=W+N_r,
\]

which is (0.4).  If the fused word has length `W+o(W)`, then `R=o(W)`;
with `E=o(W)`, (0.3) gives (0.5).  \(\square\)

## 3. PBBS specialization

For an owner path

\[
                         X_0,\ldots,X_{v-1},
 \qquad |X_i|=m+1,
\]

the endpoint-capped PBBS erosion letters are

\[
                         D_i=\bigcap_{j=0}^{H}\widetilde X_{i+j}.
                                                               \tag{3.1}
\]

There are at most `H` Johnson transitions in (3.1), and one transition
can delete at most one coordinate.  Therefore

\[
                         |D_i|\ge m+1-H.              \tag{3.2}
\]

Across all PBBS components, there is one owner-aligned `D_i` for each of
the `W` middle owners.  Endpoint extensions, collars, and cut charts are
the nondistinguished positions counted by `E`.  In the proved
sub-Gaussian central compiler,

\[
                         E=o(W).                       \tag{3.3}
\]

Taking `r=m-H`, (3.2) makes all `W` core positions ineligible for the
first missing lower rank.  Theorem A now applies verbatim.

This also explains why the upper tail alone can appear superficially
shareable: large PBBS letters may participate in large unions.  The lower
tail cannot.  Since the product-SCD gadget covers the two tails with one
word, its lower half already forces the obstruction.

## 4. Gaussian asymptotics

Direct cancellation gives (0.6).  Uniformly for `H=O(sqrt(m))`,

\[
\begin{aligned}
 \log\frac{W}{N_{m-H}}
 &=\sum_{i=0}^{H-1}
   \log\frac{m+2+i}{m-i}\\
 &=\sum_{i=0}^{H-1}
   \left(\frac{2i+2}{m}+O\!\left(\frac{(i+1)^2}{m^2}\right)\right)\\
 &=\frac{H(H+1)}m+O\!\left(\frac{H^3}{m^2}\right).
                                                               \tag{4.1}
\end{aligned}
\]

Equation (0.7) follows for `H=A sqrt(m)+o(sqrt(m))`; (0.8)--(0.9) follow
from Theorem A.

As a consistency check, the exact product-SCD fixed-Gaussian cost
`F(A)W` must be at least `N_{m-H}`, because it too is a literal word
covering that rank.  Lemma 1.1 gives the universal inequality

\[
                         F(A)\ge e^{-A^2}.             \tag{4.2}
\]

## 5. The endpoint relaxation is tight, but not physically realizable for free

The obstruction is not a shortage of abstract endpoints.  Fix any
symmetric-chain decomposition of the Boolean lattice.  It has exactly
`W` chains, one through every middle set.  Exactly `N_r` of those chains
reach rank `r`.  If one is allowed to attach an abstract nested flag to
each of `W` endpoints, these SCD chains cover every rank simultaneously
with zero additional endpoints, and inequality (1.2) is attained at every
rank.

What fails for the present PBBS baseline is physical realization.  Its
actual terminal letters satisfy (3.2), so its endpoint flags stop above
the exterior.  Replacing those flags by the SCD flags while retaining one
common contiguous word is precisely an integral SCD--rotor/rethreading
problem.  Theorem A proves that this replacement must affect a positive
fraction of the baseline at every fixed Gaussian cutoff and almost all of
it at a sub-Gaussian cutoff.

The physical realization problem itself has an exact coordinatewise
criterion once the witness intervals have been selected.

### Theorem 5.1 (forbidden-interval realization criterion)

Fix a length `L`, and let

\[
 \{(I_\alpha,S_\alpha):\alpha\in\mathcal A\}          \tag{5.1}
\]

be prescribed data, where every `I_alpha` is a contiguous interval of
`[L]` and every `S_alpha` is a subset of `[n]`.  For `x in [n]`, put

\[
 F_x=\bigcup_{\alpha:x\notin S_\alpha}I_\alpha,
 \qquad A_x=[L]\setminus F_x.                        \tag{5.2}
\]

There exists a word `Q_1,...,Q_L` satisfying

\[
 \bigcup_{i\in I_\alpha}Q_i=S_\alpha
 \quad\hbox{for every }\alpha                         \tag{5.3}
\]

if and only if

\[
 \boxed{
 x\in S_\alpha\quad\Longrightarrow\quad
 I_\alpha\cap A_x\ne\varnothing}
 \quad\hbox{for every }x,\alpha.                     \tag{5.4}
\]

Moreover, there is such a word with every letter nonempty if and only if,
in addition,

\[
 \boxed{\bigcup_{x\in[n]}A_x=[L].}                   \tag{5.5}
\]

When (5.4) holds, the coordinatewise maximal realization is explicit:

\[
 Q_i=\{x:i\in A_x\}.                                 \tag{5.6}
\]

#### Proof

If `x` is absent from `S_alpha`, no letter in `I_alpha` may contain `x`.
Thus every possible occurrence position of `x` lies in `A_x`.  If `x` is
present in `S_alpha`, at least one such position must lie in `I_alpha`;
this proves necessity of (5.4).

Conversely, define (5.6).  For a fixed `alpha`, no coordinate outside
`S_alpha` occurs in `I_alpha` by the definition of `F_x`.  Every
coordinate in `S_alpha` occurs there by (5.4).  Hence (5.3) holds.
Finally (5.6) is the largest possible letter at each position, so a
nonempty realization exists exactly when every position belongs to some
`A_x`, which is (5.5).  \(\square\)

For endpoint flags, the intervals in (5.1) are suffix intervals ending at
their assigned baseline endpoints.  Thus a wholesale fusion proof splits
into two exact tasks:

1. assign each required SCD-chain target to an endpoint and choose nested
   suffix intervals for that endpoint;
2. verify (5.4)--(5.5).

There is no further set-valued compatibility condition: after the
interval schedule is found, (5.6) builds the word.  Conversely, failure of
(5.4) for one coordinate is a literal statewise certificate against that
schedule.

Thus the exact annulus frontier is no longer "can the exterior word be
spliced into the PBBS seams?"  It is:

\[
 \boxed{
 \begin{gathered}
 \text{construct a wholesale }W\text{-position rethreading whose endpoint}\
 \text{flags retain the PBBS central witnesses and simultaneously realize}\
 \text{an SCD-quality lower-tail chain assignment.}
 \end{gathered}}                                      \tag{5.7}
\]

No insertion-only, sparse-edit, local-collar, or seam-only fusion can do
this.

## 6. A positive wholesale rethreading theorem at the middle layer

The edit-distance obstruction is sharp in an important sense.  Wholesale
replacement can make every baseline endpoint eligible for the lower tail
without losing the exact middle targets.

### Theorem 6.1 (sparse morphological preimage)

Let `H=H(m)` satisfy

\[
                         H\longrightarrow\infty,
 \qquad H=o(m).                                      \tag{6.1}
\]

Let `M_t`, over a disjoint union of cyclic components having total length
`W`, be rank-`m` subsets of `[2m+1]` such that

1. consecutive `M_t`'s are equal or Johnson-adjacent;
2. every nonconstant positive coordinate run has length at least `H`;
3. every cyclic component has length at least `H`.

Then, for all sufficiently large `m`, there are nonempty letters `Q_t`
such that

\[
 \boxed{
 M_t=\bigcup_{j=t-H+1}^{t}Q_j
 \quad\hbox{for every }t,}                           \tag{6.2}
\]

with cyclic indices inside each component, and

\[
 \boxed{
                         |Q_t|\le m-H
 \quad\hbox{for every }t.}                           \tag{6.3}
\]

Thus the same `W` physical positions still expose every middle target,
while all `W` positions become eligible endpoints for rank `m-H`.

Every such preimage also preserves the whole upper dilation tower.  For
every `d>=0`,

\[
 \boxed{
 \bigcup_{j=t-H-d+1}^{t}Q_j
 =\bigcup_{s=t-d}^{t}M_s.}                            \tag{6.4}
\]

#### Proof

Work coordinatewise.  For a coordinate `x`, consider a nonconstant
positive run `[a,b]` of its membership word `1_(x in M_t)`, of length
`ell>=H`.  An occurrence of `x` in a letter `Q_j` contributes `x` to
exactly the `H` output positions

\[
                         [j,j+H-1].                   \tag{6.5}
\]

It follows that its allowed letter positions are

\[
                         a\le j\le b-H+1.             \tag{6.6}
\]

Choose a uniform residue `U` modulo `H`, independently for every
coordinate run.  Include the two forced positions `a` and `b-H+1`, and
also the positions congruent to `a+U` modulo `H` strictly between them.
Consecutive selected positions have gap at most `H`; (6.5) therefore
covers `[a,b]` exactly and no point outside it.

If `x` is positive around an entire cyclic component, choose an
approximately equally spaced cyclic set with gaps at most `H`, followed by
a uniform cyclic rotation.  A fixed position is then selected with
probability at most `2/H`.

Let `Q_t^0` be the set of coordinates selected at position `t`.  Because
consecutive `M_t`'s are equal or Johnson-adjacent, at most one coordinate
run starts and at most one coordinate run ends at any transition.  Hence
at a fixed position at most two selected coordinates are forced.  All
remaining indicators are independent over coordinate runs, and each has
probability at most `2/H`.  Therefore

\[
 |Q_t^0|\ \preceq\ 2+\operatorname {Bin}(2m+1,2/H),
 \qquad \mathbb E|Q_t^0|\le2+\frac{4m+2}{H}.          \tag{6.7}
\]

For `r=m-H-1`, the elementary Chernoff bound gives, uniformly in `t`,

\[
 \Pr\bigl(|Q_t^0|>m-H-1\bigr)
 \le
 \left(\frac{e(4m/H+2)}{m-H-1}\right)^{m-H-1}
 =\exp(-m\log H+O(m)).                               \tag{6.8}
\]

There are at most

\[
 W=\binom{2m+1}{m}<2\cdot4^m                         \tag{6.9}
\]

positions.  Since `H->infinity`, the union bound in (6.8)--(6.9) is
`o(1)`.  Hence there is a simultaneous choice for which

\[
                         |Q_t^0|\le m-H-1
 \quad\hbox{for all }t.                               \tag{6.10}
\]

The run-cover construction proves (6.2) with `Q_t^0`, except that some
letters might be empty.  At every position, the intersection

\[
                         D_t=\bigcap_{j=t}^{t+H-1}M_j \tag{6.11}
\]

has size at least `m-H+1`, because `H-1` Johnson transitions delete at
most `H-1` elements from `M_t`.  If `Q_t^0` is empty, add one arbitrary
element of `D_t`.  This is an allowed occurrence: it changes none of the
output masks in (6.2).  It raises the load by at most one, so (6.10) gives
(6.3).

Finally, expanding the right side of (6.4) with (6.2) gives

\[
 \bigcup_{s=t-d}^{t}M_s
 =\bigcup_{s=t-d}^{t}\ \bigcup_{j=s-H+1}^{s}Q_j
 =\bigcup_{j=t-H-d+1}^{t}Q_j.
\]

This proves (6.4).  \(\square\)

### Proposition 6.2 (upper tower is free; canonical lower tower is rigid)

Let `Q` be any word satisfying (6.2).  Then (6.4) shows that every union
of consecutive middle states represented by the maximal PBBS erosion word
is still represented by `Q`, at the same endpoint.

In the other direction, for every `1<=k<=H`,

\[
 \bigcup_{j=t-k+1}^{t}Q_j
 \subseteq
 \bigcap_{s=t}^{t+H-k}M_s.                            \tag{6.12}
\]

At the deepest lower step `k=1`, equality at every endpoint is equivalent
to

\[
 \boxed{
 Q_t=\bigcap_{s=t}^{t+H-1}M_s=D_t
 \quad\hbox{for every }t.}                           \tag{6.13}
\]

Thus the maximal PBBS erosion word is the **unique** sliding preimage
which preserves every canonical deepest-lower witness.  Any rethreading
obeying the low-letter bound (6.3) must abandon and reassign those lower
witnesses.

#### Proof

Every `Q_j` in the left side of (6.12) is contained, by (6.2), in each
`M_s` for `j<=s<=j+H-1`.  The common range over
`t-k+1<=j<=t` is `t<=s<=t+H-k`, which proves (6.12).  For `k=1`, (6.12)
is `Q_t subseteq D_t`; equality is exactly (6.13).  \(\square\)

### PBBS interpretation

For a rank-`(m+1)` PBBS owner trajectory `X_t`, put

\[
                         M_t=X_t\cap X_{t+1}.          \tag{6.14}
\]

Then the maximal preimage (6.11) is literally the PBBS erosion letter:

\[
 \bigcap_{s=t}^{t+H-1}M_s
 =\bigcap_{j=t}^{t+H}X_j=D_t.                         \tag{6.14a}
\]

Then consecutive `M_t`'s are equal or Johnson-adjacent.  A positive owner
run of length at least `H+1` induces a positive `M`-run of length at least
`H`.  Thus Theorem 6.1 applies on every long residence-safe PBBS
component (and on the endpoint-extended paths after the corresponding
linear version of the same proof).  The negligible short-component ledger
may still be patched separately.

The theorem does **not** preserve all of the old erosion--dilation
identities through depth `H`; it preserves the exact middle layer.  Its
importance is narrower and structural:

\[
 \boxed{
 \text{PBBS's high terminal-letter floor is not inherent to its middle}
 \text{ chronology.}}                                \tag{6.15}
\]

A wholesale length-preserving rewrite removes that floor and retains the
upper PBBS tower by (6.4).  Proposition 6.2 shows that it necessarily
destroys the canonical deepest-lower chronology.  The remaining fusion
problem is therefore one-sided and exact: choose the run grids so that
the same letters satisfy the forbidden-interval criterion of Theorem 5.1
for a **new lower** annulus/SCD flag assignment.

## 7. Scope

The theorem rules out a broad natural class of baseline fusions, but it
does **not** rule out coefficient one.  A wholesale change of `W-o(W)`
letters can keep the total length equal to `W`; cyclic-order words are the
basic example of how small terminal letters can accumulate into middle
sets.  The remaining question is global chronology, not endpoint count.

The result should therefore be used as a routing decision:

* stop trying to pay the product-SCD exterior with PBBS collars or a
  sublinear family of local edits;
* retain the SCD endpoint assignment as the correct zero-marginal-cost
  relaxation;
* attack an integral, wholesale PBBS-to-SCD rethreading, or abandon the
  PBBS baseline entirely.
