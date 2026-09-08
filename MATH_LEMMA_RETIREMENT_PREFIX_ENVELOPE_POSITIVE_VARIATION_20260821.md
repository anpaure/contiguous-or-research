# The retirement prefix envelope is controlled by one- and two-step positive variation

**Status (2026-08-21).**  The deterministic theorem below is proved.  It
reduces the affine retirement problem to two explicit weighted positive-
variation ledgers.  It does **not** prove the required asymptotic estimates
for those ledgers.  In particular, exact two-step monotonicity is false; an
exact counterexample is recorded in Section 4.

## 1. Abstract path-capacity data

Let `I` be a finite set of path types.  Type `i` has capacity `a_i>=0` and,
at layer `q=1,...,H`, visits a profile `s_i(q)`.  Let `P_(q,s)>=0` be the
profile quotas and put

\[
 T_{q,s}=\sum_{i:s_i(q)=s}a_i,
 \qquad
 \rho_{q,s}=\min\!\left(1,{P_{q,s}\over T_{q,s}}\right),       \tag{1.1}
\]

with `rho_(q,s)=0` when `T_(q,s)=0`.  Along a path write

\[
 u_i(q)=\rho_{q,s_i(q)}.                                      \tag{1.2}
\]

The independent layer optimum is

\[
 S_q=\sum_s\min(T_{q,s},P_{q,s})=\sum_i a_i u_i(q).            \tag{1.3}
\]

For prescribed layer totals `M_q` define its deficit

\[
 \mathfrak D_{\rm sep}=\sum_{q=1}^H(M_q-S_q).                  \tag{1.4}
\]

The phase-preserving retirement LP is

\[
 0\le x_i(H)\le\cdots\le x_i(1)\le a_i,
 \qquad
 \sum_{i:s_i(q)=s}x_i(q)\le P_{q,s},                          \tag{1.5}
\]

and its deficit is

\[
 \mathfrak D_{\rm ret}
 =\sum_{q=1}^HM_q-max_x\sum_{q=1}^H\sum_i x_i(q).             \tag{1.6}
\]

Finally define the two weighted positive-variation ledgers

\[
 \mathcal A_1=
 \sum_i a_i\sum_{q=2}^H [u_i(q)-u_i(q-1)]_+,                  \tag{1.7}
\]

\[
 \mathcal A_2=
 \sum_i a_i\sum_{q=3}^H [u_i(q)-u_i(q-2)]_+.                  \tag{1.8}
\]

For `q>=2` also define the adjacent minimum and its running envelope,

\[
 m_i(q)=\min(u_i(q),u_i(q-1)),\qquad
 \underline m_i(q)=\min_{2\le j\le q}m_i(j),                  \tag{1.9}
\]

and put

\[
 \mathcal E_m=\sum_i a_i\sum_{q=2}^H
                 [m_i(q)-\underline m_i(q)],\qquad
 \mathcal A_m=\sum_i a_i\sum_{q=3}^H[m_i(q)-m_i(q-1)]_+.
                                                                    \tag{1.10}
\]

No regularity, integrality, or Markov property is assumed.

## 2. Exact prefix-envelope theorem

### Theorem 2.1

For every instance of (1.1)--(1.10),

\[
 \boxed{
 \mathfrak D_{\rm sep}
 \le \mathfrak D_{\rm ret}
 \le \mathfrak D_{\rm sep}+\mathcal A_1+\mathcal E_m
 \le \mathfrak D_{\rm sep}+\mathcal A_1+H\mathcal A_m
 \le \mathfrak D_{\rm sep}+\mathcal A_1+H\mathcal A_2.}      \tag{2.1}
\]

More explicitly, the upper bound is witnessed by

\[
 x_i(q)=a_i\min_{1\le j\le q}u_i(j).                          \tag{2.2}
\]

#### Proof

At any fixed layer `q`, every retirement solution is a feasible solution of
the independent profile-capacity LP.  Its mass is therefore at most `S_q`.
Summing over `q` proves the first inequality in (2.1).

Put

\[
 v_i(q)=\min_{j\le q}u_i(j).
\]

Then (2.2) is nonincreasing in `q`, is at most `a_i`, and obeys

\[
 \sum_{i:s_i(q)=s}x_i(q)
 \le \rho_{q,s}T_{q,s}\le P_{q,s}.                            \tag{2.3}
\]

Thus it is retirement-feasible.  It remains to bound its loss relative to
the independent layer solutions.

For `q>=2`, the running minimum of `u_i(1),...,u_i(q)` is exactly
`underline m_i(q)`: the adjacent pairs in (1.9) cover all entries of the
prefix.  Moreover

\[
 u_i(q)-m_i(q)=[u_i(q)-u_i(q-1)]_+.
\]

Therefore the loss of the explicit witness (2.2) is **exactly**

\[
 \sum_i a_i\sum_{q=1}^H[u_i(q)-v_i(q)]
 =\mathcal A_1+\mathcal E_m.                                  \tag{2.4}
\]

Ordinary positive-variation telescoping applied to the sequence `m_i(q)`
gives

\[
 \mathcal E_m\le H\mathcal A_m.                              \tag{2.5}
\]

Finally,

\[
 [m_i(q)-m_i(q-1)]_+
 \le [u_i(q)-u_i(q-2)]_+,                                    \tag{2.6}
\]

because an increase of the adjacent minimum is impossible if its older
minimum is `u_i(q-1)`, while otherwise it is bounded by
`u_i(q)-u_i(q-2)`.  Thus `A_m<=A_2`, proving every inequality in (2.1).

For completeness, the following parity-envelope argument proves the final
bound directly as well and is sometimes useful when estimating `A_2`.

For one path suppress the subscript `i` and let

\[
 w(q)=\min\{u(j):j\le q,\ j\equiv q\pmod2\},
 \qquad B(q)=u(q)-w(q).                                       \tag{2.7}
\]

Positive-variation telescoping on each parity subsequence gives

\[
 B(q)\le
 \sum_{\substack{3\le k\le q\\k\equiv q\pmod2}}
 [u(k)-u(k-2)]_+.                                             \tag{2.8}
\]

The full running minimum at time `q` is `min(w(q),w(q-1))`, with the
obvious convention at `q=1`.  If it equals `w(q)`, then
`u(q)-v(q)=B(q)`.  If it equals `w(q-1)`, then

\[
 u(q)-v(q)
 \le [u(q)-u(q-1)]_+ + B(q-1).                                \tag{2.9}
\]

Consequently

\[
 u(q)-v(q)
 \le [u(q)-u(q-1)]_+ +B(q)+B(q-1).                            \tag{2.10}
\]

On summing (2.10) over `q`, a fixed two-step positive increment in (2.8)
appears in the later running-parity losses at most `H` times in total.
Therefore

\[
 \sum_{q=1}^H[u(q)-v(q)]
 \le \sum_{q=2}^H[u(q)-u(q-1)]_+
   +H\sum_{q=3}^H[u(q)-u(q-2)]_+.                             \tag{2.11}
\]

Multiply by `a_i`, sum over paths, and combine (1.3), (2.2), and (2.11).
This proves the second inequality in (2.1).  \(\square\)

### Proposition 2.2 (isolated two-step spikes remove the factor `H`)

Suppose every parity subsequence has the local return property

\[
 u_i(q+2)>u_i(q)\quad\Longrightarrow\quad
 u_i(q+4)\le u_i(q)                              \tag{2.12}
\]

whenever all displayed indices are at most `H`.  Then

\[
 \boxed{
 \mathfrak D_{\rm ret}
 \le\mathfrak D_{\rm sep}+\mathcal A_1+2\mathcal A_2.}       \tag{2.13}
\]

Indeed, on either parity subsequence, every non-up-step term is a new
running minimum.  This follows by induction: after an up-step, (2.12) puts
the next term below the pre-spike value, while after a non-up-step the next
non-up-step is smaller still.  Hence the same-parity envelope loss `B(q)`
in (2.7) equals `[u(q)-u(q-2)]_+`.  Sum (2.10); the two `B` terms charge
each two-step positive increment at most twice.  This proves (2.13).

Condition (2.12) is strictly weaker than four-step monotonicity: a negative
two-step move may be followed by a positive one whose endpoint remains
above the value four steps earlier.  It is also an additional hypothesis,
not a consequence of Theorem 2.1.

### Corollary 2.3 (the exact affine analytic target)

Suppose `sum_i a_i=(1+o(1))W_b`,
`H=O(sqrt(b log b))`, and the separate scalar deficit is `o(W_b)`.  The
two estimates

\[
 \mathcal A_1=O\!\left({H\over b}W_b\right),
 \qquad
 \mathcal A_2=O\!\left({H^2\over b^2}W_b\right)               \tag{2.14}
\]

imply

\[
 \mathfrak D_{\rm ret}=o(W_b).                               \tag{2.15}
\]

Indeed, `H/b=o(1)` and
`H^3/b^2=O(log^(3/2)(b)/sqrt(b))=o(1)`.  Notice that (2.14) is an
**aggregate** statement.  It does not require pointwise monotonicity of
`rho` on every affine phase path.  More sharply, the exact middle bound in
(2.1) shows that `A_1+E_m=o(W_b)` is already sufficient.  If (2.12) can be
proved for the affine ratios, Proposition 2.2 reduces the target further to
`A_1+A_2=o(W_b)`.

## 3. Specialization to the half-step affine schedule

Let `b` be an odd prime, `m=(b-1)/2`,

\[
 P_r=\{x\in\mathbb Z_b:mx\bmod b<r\},
 \qquad J=\{\lfloor b/4\rfloor,\ldots,b-\lfloor b/4\rfloor\},
\]

and use

\[
 a_{r,p}={1\over b}{b\choose r}^{\!2},\qquad
 s_{r,p}(q)=r+|P_r\cap\{p+1,\ldots,p+q\}|,                    \tag{3.1}
\]

\[
 P_{q,s}={b\choose s}{b\choose{s-q}},qquad
 M_q={2b\choose{b+q}}.                                       \tag{3.2}
\]

The affine scalar theorem gives `D_sep=o(W_b)` for
`H=O(sqrt(b log b))`.  Thus Corollary 2.3 isolates a sufficient remaining
scalar calculation: prove (2.14) for the explicit finite sums (1.7)--(1.8).
The first ledger measures adjacent parity interleaving.  The second measures
failure of monotonicity within a parity subsequence.

This reduction is strictly stronger than reporting that finite retirement
LPs match their separate-layer optima: (2.2) is one explicit feasible
witness, and (2.1) is valid at every finite `b` without solver duality or
numerical tolerance.

### Lemma 3.1 (exact capacity of two-step defect phases)

Call the two-step transition of `(r,p)` from `q` to `q+2` a **defect** when

\[
 s_{r,p}(q+2)-s_{r,p}(q)\ne1.                              \tag{3.3}
\]

For every fixed payload `r` and every two-step location, exactly
`|2r-b|` phases are defects.  Consequently their total path capacity is at
most

\[
 \boxed{
 {1\over b}\sum_{r=0}^b{b\choose r}^{\!2}|2r-b|
 \le {W_b\over\sqrt{2b-1}}.}                               \tag{3.4}
\]

Indeed the two new affine ranks form one antipodal pair.  Its contribution
is unequal to one on the symmetric difference (for `r<b/2`) or intersection
(for `r>b/2`) of the two threshold arcs, of cardinality `|2r-b|`.
For the bound, the weights `binom(b,r)^2/W_b` form the hypergeometric law
with mean `b/2` and variance `b^2/[4(2b-1)]`; apply Cauchy--Schwarz.

This `O(W_b/sqrt b)` defect capacity is useful, but is not alone enough for
(2.14): a weighted bound on the positive `rho` increments is still needed.
In particular, finite diagnostics do not support a uniform `O(1/b)` bound
on every adjacent positive increment over the entire retained profile
range.  The aggregate ledgers (1.7)--(1.8), rather than a false pointwise
shortcut, are the certified remaining target.

## 4. Exact failure of two-step monotonicity

It is tempting to set `A_2=0`.  That is false.  With the central truncation
in (3.1), take

\[
 b=503,qquad H=55,qquad (r,p)=(265,452).
\]

This path has

\[
 s_{r,p}(47)=300,qquad s_{r,p}(49)=302.
\]

Exact integer evaluation of (1.1) gives

\[
 \rho_{47,300}=0.003016221036951665\ldots,
 \qquad
 \rho_{49,302}=0.003187714893644596\ldots,                     \tag{4.1}
\]

so

\[
 \boxed{\rho_{49,302}-\rho_{47,300}
 =0.000171493856692930\ldots>0.}                              \tag{4.2}
\]

The accompanying checker proves the sign in (4.2) by exact rational cross
multiplication, not floating-point comparison.  Therefore any proof of
(2.15) must retain a positive-variation error, use a more flexible
retirement construction, or prove a direct LP cut theorem.

## 5. H100 diagnostics and scope

The checker `scratch/audit_retirement_prefix_envelope_variation_20260821.py`
does five things.

1. It exhaustively verifies (2.1), (2.4), and the conditional implication
   (2.12)--(2.13) on a finite grid of arbitrary rational sequences,
   including deliberately oscillating examples.
2. It verifies the retirement feasibility and the full sandwich (2.1) for
   exact small affine instances.
3. It verifies the exact defect-phase count and the squared form of (3.4).
4. It certifies (4.2) with exact integers at `b=503`.
5. It prints `A_1/W_b`, `A_2/W_b`, and the actual prefix-envelope loss for
   a finite list of affine instances.  Those rows are diagnostics only and
   are not used as an asymptotic proof.

The theorem concerns only the scalar phase/profile retirement LP.  Even
(2.15) would give a joint fractional retired-chain law, not integral
growing-rank rounding and not coinstantiation of common labelled
tight-factor orders, origins, or physical atoms.
