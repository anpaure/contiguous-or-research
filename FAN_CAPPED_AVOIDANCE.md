# Fan-capped avoidance for an antichain witness band

## 1. Outcome

Let a word have physical positions `[1,N]`.  Select one witnessing interval

\[
                    I_i=[\ell_i,r_i],\qquad 1\le i\le M,
\]

for each member of an antichain of `M` targets, and order the intervals by
their left endpoints.  Then their right endpoints increase in the same
order.  Put

\[
                         D=N-M,\qquad w_i=r_i-\ell_i.
\]

Let `\mathcal F` be a family of distinct targets, choose one witnessing interval for
each of its members, and suppose every chosen witness avoids containing every
complete `I_i`.  Write
`h=h(\mathcal F)\ge1` for the largest number of distinct members of `\mathcal F`
in one inclusion chain.

For a physical right endpoint `t`, define its **avoidance fan size**

\[
 A_t=\#\{x:1\le x\le t,\ [x,t]\text{ contains no complete }I_i\}.
\]

The fan-capped avoidance theorem is

\[
 \boxed{
 |\mathcal F|
 \le \sum_{t=1}^N\min(A_t,h)
 \le \sum_{i=1}^M\min(w_i,h)+hD.}
 \tag{1.1}
\]

The coefficient of `hD` is exactly one and is best possible.  Thus the
quadratic boundary correction in the uncapped avoidance ledger is not
intrinsic when the targets being counted have bounded chain height.

Combining (1.1) with the audited heterogeneous run-cover lemma gives

\[
\boxed{
|\mathcal F|
\le
 \sum_{i\in J}\min(\lambda_i,h)
 +(C_\alpha+C_\beta)D
 +(M-|J|)h+hD.}
\tag{1.2}
\]

Here `J` is a set of middle indices assigned internal threshold runs not
containing their indices, `\lambda_i` is the assigned run length minus one,
and `C_\alpha,C_\beta` are the two charge congestions from
`THREE_BOX_PHASE_SEPARATION_RESEARCH.md`.

This has a material three-box consequence.  For the perfectly nested phase
order `\mathcal O_a`, any universal realization has

\[
 \boxed{
 D\ge {17\over30}a^2+{4\over5}a+{1\over30}.}
 \tag{1.3}
\]

The previous avoidance calculation only forced `D=\Omega(a^{3/2})` for this
order.  Equation (1.3) rules out the nested phase architecture throughout
the full `D=o(a^2)` regime, including any proposed subquadratic-error use of
this particular local architecture.

## 2. The fan-capped theorem

### Theorem 1 (right-endpoint fan cap)

Under the hypotheses above, (1.1) holds.

### Proof

Write the word entries as `X_1,\ldots,X_N`.  At one fixed right endpoint
`t`, the distinct interval joins

\[
 X_t,\quad X_{t-1}\vee X_t,\quad\ldots,
\]

form an inclusion chain as the left endpoint moves left.
Consequently at most `h` distinct targets from `\mathcal F` can be witnessed
at `t`.  There are only `A_t` avoiding physical intervals ending at `t`, so
at most `\min(A_t,h)` chosen witnesses from `\mathcal F` can end there.
Summing over `t` proves the first inequality.

It remains to evaluate the fans at the selected right endpoints.  If no
selected right endpoint is at most `t`, then `A_t=t`.  Otherwise let `j` be
the largest index with `r_j\le t`.  An interval `[x,t]` contains some
selected interval exactly when `x\le\ell_j`: the monotonicity of both
endpoint sequences makes `I_j` the selected interval with largest left
endpoint among those already ending.  Hence

\[
 A_t=t-\ell_j.                                      \tag{2.1}
\]

In particular,

\[
                         A_{r_i}=r_i-\ell_i=w_i.     \tag{2.2}
\]

The `M` selected right endpoints are distinct.  Exactly `N-M=D` physical
right endpoints are not among them.  Splitting the sum according to these
two classes gives the exact identity

\[
 \sum_{t=1}^N\min(A_t,h)
 =\sum_{i=1}^M\min(w_i,h)
  +\sum_{t\notin\{r_1,\ldots,r_M\}}\min(A_t,h).
 \tag{2.3}
\]

Every summand in the second term is at most `h`, proving the second
inequality in (1.1).  \(\square\)

There is a symmetric left-endpoint version.  At a selected left endpoint
`\ell_i`, the number of avoiding intervals beginning there is again `w_i`,
and there are again exactly `D` unselected left endpoints.  It yields the
same upper bound.

### Sharpness of the correction

The coefficient one in `hD` cannot be reduced uniformly.  Already for
`h=1`, take `N=D+1` word entries to be distinct singleton sets and select
`I_1=[N,N]`.  Let `\mathcal F` be the `D` singleton targets represented by
positions `1,\ldots,D`.  It is an antichain, hence has height one.  Also
`M=1` and `w_1=0`.  At each of the `D` unselected right endpoints `t<N`,
the singleton interval `[t,t]` is avoiding, and the `D` targets are all
represented.  Thus

\[
                         \sum_t\min(A_t,1)=D=hD.
\]

For general fixed `h`, again use distinct singleton word entries and select
only `I_1=[N,N]`.  Among the first `D=N-1` positions, take `\mathcal F` to
be all contiguous singleton sets of lengths at most `h`.  Its chain height
is at most `h`, every displayed interval is avoiding, and for `D\ge h` its
size is

\[
 \sum_{t=1}^D\min(t,h)=hD-{h(h-1)\over2}.
\]

Thus no coefficient below one can uniformly replace the coefficient of
`hD`.

## 3. Capping the heterogeneous run cover

Write the selected intervals in monotone-band form

\[
 \ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,\qquad
 w_i=\beta_i-\alpha_i,
 \tag{3.1}
\]

where both offset sequences are nondecreasing and lie in `[0,D]`.

For every `i\in J`, assign an internal coordinate-threshold run
`R_i=[u_i,v_i]` not containing `i`, and put `\lambda_i=v_i-u_i`.  The audited
run inequality and monotonicity give

\[
 w_i\le
 \begin{cases}
 \lambda_i+\alpha_{v_i+1}-\alpha_i,&i<u_i,\\
 \lambda_i+\beta_i-\beta_{u_i-1},&i>v_i.
 \end{cases}                                         \tag{3.2}
\]

Define `C_\alpha,C_\beta` exactly as in the heterogeneous run-cover lemma:
they are the maximum multiplicities with which an adjacent increment of
`\alpha` or `\beta` occurs in the corresponding differences in (3.2).

### Lemma 2 (fan-capped heterogeneous run cover)

For every positive integer `h`,

\[
 \sum_{i=1}^M\min(w_i,h)
 \le
 \sum_{i\in J}\min(\lambda_i,h)
 +(C_\alpha+C_\beta)D+(M-|J|)h.                     \tag{3.3}
\]

### Proof

For nonnegative `x,y`,

\[
                         \min(x+y,h)\le\min(x,h)+y. \tag{3.4}
\]

Apply (3.4) to (3.2).  On summing, the `\alpha` differences contribute at
most `C_\alpha` times the total variation of `\alpha`, hence at most
`C_\alpha D`; the `\beta` terms contribute at most `C_\beta D`.  Each
unassigned index contributes at most `h`.  This proves (3.3). \(\square\)

Combining Theorem 1 and Lemma 2 proves (1.2).  Compared with the previous
uncapped inequality

\[
 |\mathcal F|\le\sum_iw_i+3D^2+2D,
\]

the new bound makes two independent improvements:

* an assigned run costs only `\min(\lambda_i,h)`, not its full length; and
* all omitted endpoint fans together cost only `hD`, not `O(D^2)`.

The best statement in an application is the minimum of the capped and
uncapped bounds; neither dominates in every parameter range.

## 4. Rank slabs in the three-box lattice

Work in

\[
                         P_a=[0,2a]^3
\]

with componentwise maximum as join and rank
`\rho(x,y,z)=x+y+z`.  Its middle layer has rank `3a` and size

\[
                         M_a=3a^2+3a+1.              \tag{4.1}
\]

For `1\le h\le3a-1`, let

\[
 \mathcal F_h=\{x\in P_a:3a-h\le\rho(x)\le3a-1\}. \tag{4.2}
\]

This family has chain height at most `h`, because rank strictly increases
along every strict inclusion chain.  Every witness of a member of
`\mathcal F_h` avoids every complete selected middle witness: containing a
middle witness would make its join dominate a rank-`3a` point.

Let `L_h(a)=|\mathcal F_h|`.  If `1\le h\le a`, inclusion-exclusion gives

\[
 [x^{3a-q}](1+x+\cdots+x^{2a})^3=M_a-q^2,
 \qquad 0\le q\le a,
\]

and therefore

\[
 L_h(a)=hM_a-{h(h+1)(2h+1)\over6}.                  \tag{4.3}
\]

Two slab sizes used below are

\[
\begin{aligned}
 L_{2a}(a)
   &= {23\over6}a^3+4a^2+{7\over6}a,               \tag{4.4}\\
 L_{3a-1}(a)
   &=4a^3+{9\over2}a^2+{3\over2}a-1=:V_a.          \tag{4.5}
\end{aligned}
\]

For (4.4), remove from the full nonzero lower half the nonzero points of
rank at most `a-1`; their number is `\binom{a+2}{3}-1`.  Equation (4.5) is
the usual full lower-half count.

Theorem 1 now gives, for every selected middle witness band,

\[
 \boxed{
 L_h(a)\le\sum_{i=1}^{M_a}\min(w_i,h)+hD.}
 \tag{4.6}
\]

This rank-slab form is often much stronger than counting every avoiding
physical interval.

## 5. Strengthened anti-mixing inequality

Let `H` be the extreme-run mesh defined in
`THREE_BOX_INTERLEAVING_OBSTRUCTION.md`.  Its audited charging argument gives

\[
 \sum_iw_i\le aM_a+2HD+3(a+1)D.                    \tag{5.1}
\]

Use the full lower family, whose height is `3a-1`, in (4.6), and then use
`\min(w_i,3a-1)\le w_i`.  This yields the exact strengthened inequality

\[
 \boxed{
 V_a\le aM_a+(2H+6a+2)D.}
 \tag{5.2}
\]

Equivalently,

\[
 D\ge
 {a^3+\frac32a^2+\frac12a-1\over 2H+6a+2}.          \tag{5.3}
\]

The earlier ledger had a `3D^2+2D` escape term.  It has disappeared.  Some
immediate consequences are:

* if `H=O(a)`, then `D=\Omega(a^2)`;
* if `H=O(a\log a)`, then `D=\Omega(a^2/\log a)`; and
* more generally, when `H\ge a`, one needs `D=\Omega(a^3/H)`.

Thus, conditional on the selected middle order being uniformly random, the
high-probability random-order consequence strengthens from
`D=\Omega(a^{3/2})` to `D=\Omega(a^2/\log a)`.  The theorem still permits a
near-quadratic run desert; it does not by itself exclude every irregular
order.

## 6. Exact consequence for the nested phase order

Assume `a\ge2`.  For the nested order `\mathcal O_a` in
`THREE_BOX_PHASE_SEPARATION_RESEARCH.md`, the audited run certificate has:

\[
\begin{aligned}
 |J|&=M_a-1,\\
 \sum_{i\in J}\lambda_i&=a^3-a,\\
 C_\alpha&\le2a,\qquad C_\beta\le a,\\
 \lambda_i&\le a-1\quad(i\in J).
\end{aligned}                                        \tag{6.1}
\]

Take the `2a`-rank slab.  Since every assigned run is shorter than the cap,
(1.2), (4.4), and (6.1) give

\[
 {23\over6}a^3+4a^2+{7\over6}a
 \le (a^3-a)+3aD+2a+2aD
 =a^3+a+5aD.                                         \tag{6.2}
\]

Rearranging proves

\[
 D\ge {17\over30}a^2+{4\over5}a+{1\over30},         \tag{6.3}
\]

which is (1.3).  Since `D` is integral, the right side may of course be
rounded up.

The constant `17/30` is not asserted optimal.  Varying a cap
`h=ca+O(1)` and using the exact clipped run sum gives slightly different
constants.  What matters structurally is the quadratic conclusion: this
architecture cannot supply a local three-box word of length
`M_a+o(a^2)`.

## 7. Other certified three-box consequences

### Contiguous complete rings

The run assignment audited in `THREE_BOX_SPIRAL_BAND_OBSTRUCTION_AUDIT.md`
assigns all but `O(a)` middle indices a run with `\lambda_i\le a+O(1)`, has
charge congestion `O(a)`, and has total clipped run cost
`3a^3+O(a^2)`.  Applying (1.2) with `h=3a-1` gives

\[
                         V_a\le3a^3+O(a^2+aD).
\]

Consequently the contiguous-ring architecture requires

\[
                              D=\Omega(a^2),          \tag{7.1}
\]

under the same ring-order and `O(a)` auxiliary-occurrence hypotheses.  This
extends the old width-plus-perimeter obstruction to the entire
subquadratic-error regime.

### Side-batched orders

For a side-batched order with `B` maximal side-homogeneous batches, the
audited nine-block certificate has

\[
 \sum_{i\in J}\lambda_i\le3a^3+O(a^2),\qquad
 C_\alpha+C_\beta\le10a,qquad
 M_a-|J|\le8aB+O(a).                                 \tag{7.2}
\]

Use the full lower family in (1.2).  Equations (4.5) and (7.2) imply

\[
 a^3\le13aD+24a^2B+O(a^2),
\]

or, more transparently,

\[
                         13D+24aB\ge a^2-O(a).        \tag{7.3}
\]

Hence no side-batched family with both `B=o(a)` and `D=o(a^2)` can be
universal.  At surface error this recovers the necessity of linearly many
side changes; the new statement remains informative far beyond surface
error.

### General reusable criterion

Let `h=\Theta(a)`.  If an order admits a heterogeneous run assignment with

\[
 \sum_{i\in J}\min(\lambda_i,h)
 \le(c-o(1))a^3,qquad
 C_\alpha+C_\beta=O(a),qquad
 M_a-|J|=o(a^2),                                     \tag{7.4}
\]

while `L_h(a)\ge(c+\varepsilon)a^3`, then (1.2) forces
`D=\Omega(a^2)`.  This is the appropriate proof-producing test for any new
three-box sweep, needle, or phase schedule.

## 8. Scope and limitations

The new theorem is an endpoint-capacity theorem, not a construction and not
a complete three-box impossibility result.

It proves:

* the exact fan inequality (1.1), with sharp correction `hD`;
* the clipped heterogeneous run-cover inequality (1.2);
* a quadratic-slack obstruction for the nested phase order and contiguous
  complete-ring orders; and
* the stronger side-batch tradeoff (7.3).

It does **not** prove:

* that every ordering of the middle hexagon has a cheap capped run cover;
* that the `\Theta(a)` irregular side-switching regime is impossible;
* alignment of deserts arising from different embedded subcubes; or
* the conjectural exact formula for universal Boolean OR arrays.

For the full Boolean lattice near the conjectural optimum, the lower family
has height `\Theta(k)` while `D=\Theta(\sqrt k)`.  There the old `O(D^2)`
avoidance correction can be smaller than `hD`, so (1.1) does not automatically
strengthen the known rank-slack bound.  Its principal present value is in
fixed-dimensional product lattices, where one must control errors throughout
the much larger range `a\ll D=o(a^2)`.
