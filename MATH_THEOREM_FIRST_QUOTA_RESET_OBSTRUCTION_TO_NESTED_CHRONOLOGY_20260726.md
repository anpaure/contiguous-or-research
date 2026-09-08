# The first quota reset obstructs a single nested pair-radius chronology

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \rho_q={W\over N_q}.                              \tag{0.1}
\]

At depth \(q\), balanced target loads are

\[
 c_q=\lfloor\rho_q\rfloor
 \quad\hbox{or}\quad c_q+1,                        \tag{0.2}
\]

and the normalized size of the high-quota family is

\[
 \alpha_q=\rho_q-c_q\in[0,1).                     \tag{0.3}
\]

The pair-radius filtration from the preceding note works in the cap-two
interval \(1<\rho_q<2\).  It cannot be continued as one shadow-nested
bonus filtration into any range

\[
                         {H\over\sqrt m}\longrightarrow\infty.            \tag{0.4}
\]

The obstruction is the first integer reset of \(\rho_q\).

Let \(q_*\) be the first depth with \(\rho_{q_*}\ge2\).  Then

\[
 q_*=(\sqrt{\log2}+o(1))\sqrt m,                   \tag{0.5}
\]

and

\[
 \alpha_{q_*-1}=1-O(m^{-1/2}),\qquad
 \alpha_{q_*}=O(m^{-1/2}).                         \tag{0.6}
\]

Normalized lower shadows cannot decrease density.  Consequently any
families \({\cal F}_{q_*-1},{\cal F}_{q_*}\) satisfying

\[
                         \partial{\cal F}_{q_*-1}
                         \subseteq{\cal F}_{q_*}    \tag{0.7}
\]

incur

\[
 \left||{\cal F}_{q_*-1}|-\alpha_{q_*-1}N_{q_*-1}\right|
 +
 \left||{\cal F}_{q_*}|-\alpha_{q_*}N_{q_*}\right|
 \ge\left({1\over2}-o(1)\right)W.                 \tag{0.8}
\]

Thus a single shadow-nested high-quota design has \(\Omega(W)\) target
error at these two depths alone.  In particular it cannot have aggregate
error \(o(W)\).

There is also a local form.  Immediately before the reset, a balanced
high family has density \(1-O(m^{-1/2})\).  On a uniform endpoint flag,
the expected number of rows not belonging to that family is only

\[
                         O(\sqrt m).                \tag{0.9}
\]

Hence the positive linear row slack furnished by the \(O(H^2)\) nested
congestion theorem necessarily disappears before (0.4) is reached.

This is an incompatibility of the proposed **single nested bonus
chronology**, not a no-go for arbitrary \(H\)-safe Johnson cycle factors.
An unrestricted circulation could still work if it carries an explicit
quota-level state and performs a reset whenever \(c_q\) increases.  The
rank-twisted \(Q_r\) owner tiling does not by itself provide such a reset;
its packet and run-vector arithmetic occurs after the obstruction (0.8).

The \(Q_r\) audit does show that its common-run-vector granularity is not
the fatal term.  If a physical \(Q_r\) is factored into isometric
\(C_{2r}\)'s, every active coordinate contributes

\[
                         \kappa_r={2^r\over2r}      \tag{0.10}
\]

runs.  Thus \(R_v\) is quantized in multiples of \(\kappa_r\), but for
\(r=o(m)\) the resulting total point-margin rounding cost is \(o(W)\).
The missing object is therefore a quota-reset-aware target circulation,
not another owner tiling or a correction to the common run vector.

## 1. The first reset lies at Gaussian depth

The exact ratio is

\[
 \rho_q
 ={(m+q)!(m-q)!\over(m!)^2}
 =\prod_{j=1}^q\left(1+{q\over m-q+j}\right).      \tag{1.1}
\]

Uniformly for \(q=O(\sqrt m)\),

\[
                         \log\rho_q={q^2\over m}+O(m^{-1/2}).   \tag{1.2}
\]

Moreover,

\[
 \rho_{q+1}-\rho_q
 =\rho_q{2q+1\over m-q}.                           \tag{1.3}
\]

### Lemma 1.1 (first-reset asymptotics)

Let

\[
                         q_*:=\min\{q:\rho_q\ge2\}.             \tag{1.4}
\]

Then (0.5)--(0.6) hold, and

\[
 N_{q_*-1}=\left({1\over2}+o(1)\right)W,
 \qquad
 N_{q_*}=\left({1\over2}+o(1)\right)W.             \tag{1.5}
\]

#### Proof

Equation (1.2) locates the first crossing of \(2\) at (0.5).  At this
depth, (1.3) is \(O(m^{-1/2})\).  Minimality of \(q_*\) therefore gives

\[
 2-O(m^{-1/2})\le\rho_{q_*-1}<2
 \le\rho_{q_*}\le2+O(m^{-1/2}).                   \tag{1.6}
\]

Taking fractional parts proves (0.6), and
\(N_q=W/\rho_q\) proves (1.5). \(\square\)

Every range satisfying (0.4) contains \(q_*\) for all sufficiently large
\(m\).  Thus the obstruction below cannot be avoided by choosing a slowly
growing super-Gaussian safety factor.

## 2. Normalized shadows and the two-depth contradiction

Let \(n=2m\), let \({\cal A}\subseteq\binom{[n]}k\), with \(k\le n/2\),
and let

\[
                         \partial{\cal A}
 =\{S\in\tbinom{[n]}{k-1}:S\subset A
                       \text{ for some }A\in{\cal A}\}.        \tag{2.1}
\]

### Lemma 2.1 (normalized shadow monotonicity)

\[
 { |\partial{\cal A}|\over\binom n{k-1}}
 \ge { |{\cal A}|\over\binom nk}.                 \tag{2.2}
\]

#### Proof

Count inclusion edges from \({\cal A}\) to its lower shadow.  Every
member of \({\cal A}\) has \(k\) children, while a \((k-1)\)-set has at
most \(n-k+1\) parents.  Hence

\[
 k|{\cal A}|\le(n-k+1)|\partial{\cal A}|.
\]

Use

\[
 \binom n{k-1}=\binom nk{k\over n-k+1}.
\]

This gives (2.2). \(\square\)

### Theorem 2.2 (first-reset nested-family no-go)

Let

\[
 {\cal F}^-\subseteq\binom{[2m]}{m-q_*},
 \qquad
 {\cal F}^+\subseteq\binom{[2m]}{m-q_*+1},         \tag{2.3}
\]

where \({\cal F}^+\) is the depth-\((q_*-1)\) family and
\({\cal F}^-\) the depth-\(q_*\) family.  Assume

\[
                         \partial{\cal F}^+
                         \subseteq{\cal F}^-.       \tag{2.4}
\]

Then (0.8) holds.

#### Proof

Put

\[
 x={|{\cal F}^+|\over N_{q_*-1}},
 \qquad
 y={|{\cal F}^-|\over N_{q_*}}.                   \tag{2.5}
\]

Lemma 2.1 and (2.4) give \(x\le y\).  For any real numbers
\(x\le y\) and \(a>b\),

\[
                         |x-a|+|y-b|\ge a-b.        \tag{2.6}
\]

Take \(a=\alpha_{q_*-1}=1-O(m^{-1/2})\) and
\(b=\alpha_{q_*}=O(m^{-1/2})\).  By (1.5), both layer sizes are
\((1/2+o(1))W\).  Therefore

\[
\begin{aligned}
 &\left||{\cal F}^+|-aN_{q_*-1}\right|
 +\left||{\cal F}^-|-bN_{q_*}\right|\\
 &\hspace{25mm}\ge
 \min\{N_{q_*-1},N_{q_*}\}(|x-a|+|y-b|)\\
 &\hspace{25mm}\ge\left({1\over2}-o(1)\right)W.
\end{aligned}                                      \tag{2.7}
\]

This is (0.8). \(\square\)

The upper-target version follows by complementation.  The theorem applies
to the pair-radius thresholds, to an SCD ideal, and to every other
one-parameter shadow-nested bonus filtration.

## 3. Collapse of the endpoint exchange matrix

The same reset has a direct local consequence even without assuming
nesting at the next depth.

Let \({\cal F}\subseteq\binom{[2m]}k\) have density

\[
                         {|{\cal F}|\over\binom{2m}k}=1-\varepsilon.       \tag{3.1}
\]

For a uniform parent \(I\in\binom{[2m]}{k+1}\), let

\[
                         G(I)=\#\{a\in I:I-a\notin{\cal F}\}.             \tag{3.2}
\]

Double counting gives

\[
                         \mathbb EG(I)=(k+1)\varepsilon.         \tag{3.3}
\]

At depth \(q_*-1\), equation (0.6) has
\(\varepsilon=O(m^{-1/2})\) and \(k+1=m-q_*+2=(1-o(1))m\).
Consequently

\[
                         \mathbb EG(I)=O(\sqrt m).               \tag{3.4}
\]

### Corollary 3.1 (no positive-density row-slack orbit)

For every fixed \(\eta>0\), the proportion of a depth-balanced endpoint
orbit having at least \(\eta m\) rows outside the balanced high family at
depth \(q_*-1\) is \(O(m^{-1/2})\).

#### Proof

Apply Markov's inequality to (3.4).  Restricting from all deletion rows to
the return-free eligible rows can only decrease their number. \(\square\)

Thus the \(O(H^2)\) congestion improvement from the pair-radius
filtration is a genuine cap-two theorem.  It cannot be used as a positive
linear-slack invariant through the first quota reset.

## 4. What the unrestricted circulation would have to add

For a balanced load vector, define its level sets

\[
 {\cal L}_{q,t}=\{T:\mu_q(T)\ge t\},
 \qquad 1\le t\le c_q+1.                            \tag{4.1}
\]

At depth \(q\),

\[
 {\cal L}_{q,t}=\binom{[2m]}{m-q}\quad(1\le t\le c_q),
 \qquad
 |{\cal L}_{q,c_q+1}|=\alpha_qN_q.                \tag{4.2}
\]

When \(c_q\) increases, the old top level must be absorbed into a new
universal base level and a new sparse top level must begin.  A single
nested family has no state variable representing this reset.

Accordingly, a viable integral memory circulation must carry at least:

1. the current quota level \(c_q\);
2. a top-level family which is allowed to reset when \(c_q\) changes;
3. a cross-reset collar rule which prevents the almost-full old top layer
   from blocking the sparse new layer; and
4. one common run vector and memory-flow conservation across every reset.

These are additional states in the safe-path circulation.  Root rows,
ordinary prefix/suffix memory rows, and the pair-radius endpoint potential
do not imply them.

Theorem 2.2 does not exclude such a reset-aware circulation, because its
top family is deliberately nonnested at the reset.  It proves that the
pair-radius construction cannot simply be installed as one all-depth
bonus filtration.

## 5. Audit of the rank-twisted \(Q_r\) owner tiling

The rank-twisted macroblock theorem supplies an owner-disjoint near-factor
by physical \(Q_r\)'s.  Assume a selected packet is factored into
isometric \(C_{2r}\)'s.  Necessarily \(2r\mid2^r\); put

\[
                         \kappa_r={2^r\over2r}.     \tag{5.1}
\]

### Lemma 5.1 (packet contribution to the common run vector)

In one physical \(Q_r\) packet:

1. every active physical coordinate is an endpoint of one packet axis;
2. on each isometric \(C_{2r}\), that coordinate has one cyclic
   membership \(1\)-run; and
3. the complete packet factor contributes exactly \(\kappa_r\) to its
   global run count.

Frozen coordinates contribute zero.

#### Proof

An isometric \(C_{2r}\) uses every cube direction exactly twice, once in
each orientation.  Along the corresponding physical exchange axis, each
endpoint coordinate changes membership twice and therefore has one
cyclic \(1\)-run.  The packet contains \(2^r/(2r)=\kappa_r\) factor
cycles. \(\square\)

Consequently, before the exponentially small owner leave and any seam
correction,

\[
                         R_v=\kappa_r n_v,           \tag{5.2}
\]

where \(n_v\) is the number of selected packets in which \(v\) is active.
Summing over coordinates gives

\[
 \sum_vR_v
 =\kappa_r(2r){W\over2^r}=W.                      \tag{5.3}
\]

Thus the packet factor automatically has the correct total run count.  It
does impose the divisibility lattice (5.2), but this lattice is
asymptotically fine relative to the target problem.  Rounding one desired
coordinate run count changes it by at most \(\kappa_r\), and hence changes
its depth-\(q\) point margin by at most \(q\kappa_r\).  Through all depths
\(q\le H\), the total worst-case point-margin rounding scale is

\[
                         O(mH^2\kappa_r).            \tag{5.4}
\]

If \(r=o(m)\) and \(H=o(r)\), then

\[
                         mH^2\kappa_r=o(W).          \tag{5.5}
\]

Moreover the number of packet cycles is

\[
                         {W\over2r}=o(W/H).          \tag{5.6}
\]

Therefore neither run-count granularity nor component count is the
coefficient-one obstruction in this regime.  What is not supplied by the
packet tiling is the quota reset in Section 4 or the labelled-target
transport needed after each reset.

The conclusion is independent of the dense-cross and macro-support
advantages of the rank-twisted tiling.  Those solve owner packing and
direction support; they do not alter \(\rho_q\), \(c_q\), or the reset
arithmetic (0.6).

## 6. Exact verdict

There is no integral cycle-factor theorem obtained by directly combining
the single nested pair-radius bonus filtration with either:

1. the unrestricted \(H\)-safe Johnson circulation, or
2. the rank-twisted macroblock \(Q_r\) owner tiling,

in a range \(H/\sqrt m\to\infty\).  The combination is already
incompatible at the two target layers \(q_*-1,q_*\): enforcing shadow
nesting costs \((1/2-o(1))W\), while abandoning it destroys the proved
row-union invariant.

This does not disprove an unrestricted integral \(H\)-safe cycle factor
with \(o(W)\) target error.  It identifies the exact stronger object now
required:

> **Quota-reset circulation.**  Construct an integral safe-path
> circulation whose top quota layer may reset at every integer crossing of
> \(W/N_q\), with relative seam collars transporting the old almost-full
> layer into the new universal base layer, while preserving one common run
> vector and incurring total reset error \(o(W)\).

Without this reset mechanism, the \(O(H^2)\) pair-radius congestion theorem
cannot cross even the first Gaussian integer boundary.
