# Extension expansion and the common-permutation loss

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Fix an exact middle wreath factor on \(n=2m+1\) coordinates.  At depth
\(q\), let \(R\) be a hole of size \(m-q\).  Every middle extension
\(X\supset R\) is owned by one wreath, and its owning length-\(m\)
window contains \(q+1\) length-\((m-q)\) subintervals.  All of those
subintervals are covered targets different from \(R\).

The exact witness count proves

\[
 \boxed{
 |\{S:S\text{ covered},\ d_J(R,S)\le q\}|
 \ge { (q+1)(m+q+1)\over q}.}
 \tag{0.1}
\]

More precisely, a covered target at distance \(d\) absorbs at most

\[
 \boxed{\binom{m+q+1-d}{q-d}}
 \tag{0.2}
\]

extension witnesses.

At depth one this is genuinely useful: every hole has at least
\(2(m+2)\) covered Johnson neighbors.  Hence some coordinate
transposition maps at least

\[
 {2(m+2)h_1\over\binom n2}=\Theta(h_1/m)
 \tag{0.3}
\]

holes to covered targets, improving the earlier spectral opportunity by
removing its factor \(1-h_1/N_1\).

For \(q\ge2\), however, local expansion does not automatically produce
one useful common permutation.  The sharp averaging consequence for
products of at most \(q\) disjoint transpositions is only

\[
 \Theta_q(h_q/m^q)
 \tag{0.4}
\]

for fixed \(q\).  A uniform unrestricted coordinate permutation gives
only \(h_q\cdot\Theta(m/N_q)\) **nearby** images, although of course it
may map many holes to faraway covered targets.

Thus the extension lemma materially strengthens the depth-one soft gate,
but it does not solve the simultaneous Gaussian-depth component problem.
Its loss is exactly the requirement that one permutation work for all
holes and all depths.

## 1. Exact extension witnesses

Put

\[
 r=m-q,\qquad M=n-r=m+q+1.
 \tag{1.1}
\]

There are

\[
 \binom Mq
 \tag{1.2}
\]

middle \(m\)-sets \(X\) containing \(R\).  Each \(X\) occurs in the
unique wreath row which owns it, as one cyclic interval of length \(m\).
Inside that interval, deleting a total of \(q\) elements from its two
ends in all possible left/right splits gives exactly \(q+1\) distinct
consecutive subintervals of length \(r\).

Each is a covered depth-\(q\) target.  None equals \(R\), because \(R\)
is a hole.  Thus the number of pointed extension witnesses is exactly

\[
 \boxed{W_q=(q+1)\binom Mq.}
 \tag{1.3}
\]

Every witnessed target \(S\) is an \(r\)-subset of the same \(m\)-set
\(X\) as \(R\), and therefore

\[
 1\le d:=d_J(R,S)=|R\setminus S|=|S\setminus R|\le q.
 \tag{1.4}
\]

### Theorem 1.1 (distance-sensitive witness capacity)

A fixed covered target \(S\) at distance \(d\) from \(R\) occurs in at
most

\[
 \boxed{c_{q,d}=\binom{M-d}{q-d}}
 \tag{1.5}
\]

of the witnesses in (1.3).

#### Proof

Any witnessing middle extension must contain \(R\cup S\), whose size is

\[
 |R\cup S|=r+d=m-q+d.
 \tag{1.6}
\]

To obtain an \(m\)-set, choose the remaining \(q-d\) elements from the

\[
 n-|R\cup S|=m+q+1-d=M-d
 \tag{1.7}
\]

coordinates outside the union.  This gives the bound (1.5).  For a
fixed extension \(X\), its \(q+1\) consecutive length-\(r\) subintervals
are distinct, so \(S\) contributes at most one witness through that
\(X\). \(\square\)

Let \(C_d(R)\) be the family of covered targets at distance \(d\) from
\(R\).  Theorem 1.1 gives the stronger weighted expansion inequality

\[
 \boxed{
 (q+1)\binom Mq
 \le\sum_{d=1}^q
       \binom{M-d}{q-d}|C_d(R)|.}
 \tag{1.8}
\]

Since

\[
 {c_{q,d+1}\over c_{q,d}}
 ={q-d\over M-d}<1,
 \tag{1.9}
\]

the largest witness capacity is

\[
 c_{q,1}=\binom{M-1}{q-1}.
 \tag{1.10}
\]

Dividing (1.3) by (1.10) proves

\[
 \boxed{
 \sum_{d=1}^q|C_d(R)|
 \ge(q+1){\binom Mq\over\binom{M-1}{q-1}}
 ={(q+1)M\over q}.}
 \tag{1.11}
\]

This proves (0.1).

## 2. The exact depth-one transposition consequence

When \(q=1\), every witnessed target is a Johnson neighbor and its
capacity is one.  Thus every hole has at least

\[
 2(m+2)
 \tag{2.1}
\]

covered neighbors.

Let \({\cal Z}_1\) be the depth-one hole family and \(h_1=|{\cal Z}_1|\).
For a transposition \(\tau\), put

\[
 A_{\tau,1}=|\{R\in{\cal Z}_1:\tau R\notin{\cal Z}_1\}|.
 \tag{2.2}
\]

Every Johnson edge is induced by its unique exchanged coordinate pair,
so

\[
 \sum_\tau A_{\tau,1}=|\partial_J{\cal Z}_1|.
 \tag{2.3}
\]

Equation (2.1) gives the stronger pointwise boundary estimate

\[
 |\partial_J{\cal Z}_1|\ge2(m+2)h_1.
 \tag{2.4}
\]

Therefore some transposition satisfies

\[
 \boxed{
 A_{\tau,1}
 \ge{2(m+2)h_1\over\binom n2}
 ={2(m+2)h_1\over m(2m+1)}.}
 \tag{2.5}
\]

This is asymptotic to \(h_1/m\).  Unlike the generic Johnson spectral
bound, it has no factor \(1-h_1/N_1\).

The conclusion is still only opportunity.  To decrease holes in an
ownership-component cube, the covered occurrences must split across
components and common covered targets must not create larger leakage,
as quantified in
`MATH_THEOREM_SOFT_Q1_COMPONENT_DRIFT_IDENTITY_20260725.md`.

## 3. Common small-support permutations at general depth

The local targets in (1.8) can be mapped by small involutions, but the
number of possible involutions grows rapidly.

Let \({\mathscr M}_d\) be the set of coordinate involutions consisting
of exactly \(d\) disjoint transpositions.  Its cardinality is

\[
 L_{n,d}=|{\mathscr M}_d|
 ={n!\over2^dd!(n-2d)!}.
 \tag{3.1}
\]

For a hole family \({\cal Z}_q\), put

\[
 T_{q,d}=\sum_{R\in{\cal Z}_q}|C_d(R)|.
 \tag{3.2}
\]

A fixed ordered pair \((R,S)\) at Johnson distance \(d\) is mapped by
exactly \(d!\) members of \({\mathscr M}_d\): choose a bijection between
\(R\setminus S\) and \(S\setminus R\), and transpose the paired
coordinates.  Consequently

\[
 \boxed{
 \sum_{\sigma\in{\mathscr M}_d}
 |\{R\in{\cal Z}_q:\sigma R\in C_d(R)\}|
 =d!T_{q,d}.}
 \tag{3.3}
\]

Summing (1.8) over the \(h_q\) holes gives

\[
 (q+1)\binom Mq h_q
 \le\sum_{d=1}^q c_{q,d}T_{q,d}.
 \tag{3.4}
\]

### Theorem 3.1 (best generic small-involution opportunity)

For some \(1\le d\le q\) and some
\(\sigma\in{\mathscr M}_d\),

\[
 \boxed{
 |\{R\in{\cal Z}_q:\sigma R\in C_d(R)\}|
 \ge
 { (q+1)\binom Mq h_q
  \over
  \displaystyle\sum_{j=1}^q
   \binom{M-j}{q-j}{L_{n,j}\over j!}}.}
 \tag{3.5}
\]

#### Proof

Let \(Y\) be the largest left side of (3.3) divided by
\(L_{n,d}\), over all \(d\le q\).  Then

\[
 T_{q,d}\le Y{L_{n,d}\over d!}
 \tag{3.6}
\]

for every \(d\).  Insert this in (3.4) and solve for \(Y\).  Some
involution attains at least the average in (3.3), proving (3.5).
\(\square\)

For fixed \(q\), the \(j=q\) summand dominates the denominator, and
\(M=(1+o(1))m\), \(n=(2+o(1))m\).  Hence (3.5) becomes

\[
 \boxed{
 |\{R\in{\cal Z}_q:\sigma R\text{ is covered}\}|
 \ge
 \left({(q+1)q!\over2^q}+o_q(1)\right){h_q\over m^q}.}
 \tag{3.7}
\]

For \(q=1\), this agrees with (2.5).  For every fixed \(q\ge2\), it is
smaller by additional powers of \(m\).  For growing \(q\), it becomes
far below the coefficient scale.

### The exact weighted minimax consequence across several depths

There is a precise sense in which the preceding loss is the best one
can extract from the extension inequalities alone.  Fix (H), positive
weights (w_q), and abbreviate

\[
 B_q=(q+1)\binom{m+q+1}{q},\qquad
 c_{q,d}=\binom{m+q+1-d}{q-d},\qquad
 a_d={d!\over L_{n,d}}.
 \tag{3.8}
\]

Consider the finite linear program

\[
 \begin{split}
 \Lambda_H(w)=\min\ &Y\\
 \text{subject to }&
 \sum_{d=1}^q c_{q,d}T_{q,d}\ge B_qh_q
                 &&(1\le q\le H),\\
 &Y\ge a_d\sum_{q=d}^H w_qT_{q,d}
                 &&(1\le d\le H),\\
 &T_{q,d}\ge0.
 \end{split}
 \tag{3.9}
\]

Then some (d\le H) and one common
(\sigma\in{\mathscr M}_d) satisfy

\[
 \boxed{
 \sum_{q=d}^H w_q
 |\{R\in{\cal Z}_q:\sigma R\in C_d(R)\}|
 \ge \Lambda_H(w).}
 \tag{3.10}
\]

Indeed, the actual numbers (T_{q,d}) satisfy the first line of
(3.9).  For fixed (d), averaging (3.3) after summing over (q) gives

\[
 \max_{\sigma\in{\mathscr M}_d}
 \sum_{q=d}^H w_q
 |\{R\in{\cal Z}_q:\sigma R\in C_d(R)\}|
 \ge a_d\sum_{q=d}^H w_qT_{q,d}.
 \tag{3.11}
\]

Taking the best (d) proves (3.10).  Conversely, (3.9) is exactly the
worst possible value of the right side of (3.11) if one retains only
the numerical constraints (1.8); thus it is the sharp minimax statement
available from those constraints without additional geometry.

A cruder closed form follows by putting

\[
 c_d^*=\max_{d\le q\le H}c_{q,d}.
 \tag{3.12}
\]

Namely,

\[
 \boxed{
 \Lambda_H(w)\ge
 {\displaystyle\sum_{q=1}^Hw_qB_qh_q
  \over
  \displaystyle\sum_{d=1}^H c_d^*L_{n,d}/d!}.}
 \tag{3.13}
\]

To see this, if every weighted average in (3.11) were at most (Y),
then

\[
 \sum_qw_qB_qh_q
 \le\sum_d c_d^*\sum_{q\ge d}w_qT_{q,d}
 \le Y\sum_d c_d^*{L_{n,d}\over d!}.
 \tag{3.14}
\]

For one depth, (3.9) reduces exactly to (3.5).  Across a Gaussian
window, however, the denominator in (3.13) is dominated by large
support sizes.  The weighted minimax formulation therefore makes the
same obstruction explicit: local expansion does not force substantial
mass onto any one bounded-support permutation.

## 4. One unrestricted permutation across many depths

There is a very simple simultaneous statement if no support restriction
is imposed on the coordinate permutation.  For a uniform
\(\sigma\in S_n\), \(\sigma R\) is uniform on the rank of \(R\).
Therefore

\[
 \Pr(\sigma R\in\cup_{d\le q}C_d(R))
 ={ |\cup_{d\le q}C_d(R)|\over N_q}
 \ge{(q+1)(m+q+1)\over qN_q}.
 \tag{4.1}
\]

For arbitrary weights \(w_q\ge0\), averaging one common permutation
gives:

### Theorem 4.1 (weighted common-permutation local opportunity)

Some \(\sigma\in S_n\) satisfies

\[
 \boxed{
 \sum_qw_q
 |\{R\in{\cal Z}_q:\sigma R\text{ is covered and }
                       d_J(R,\sigma R)\le q\}|
 \ge
 \sum_qw_qh_q{(q+1)(m+q+1)\over qN_q}.}
 \tag{4.2}
\]

#### Proof

Sum (4.1) over all holes and depths, then choose a permutation attaining
at least the expectation. \(\square\)

This is the strongest direct simultaneous conclusion from the local
expansion alone.  If \(h_q=\Theta(N_q)\), its contribution at one depth
is only \(\Theta(m)\), because the covered local neighborhood has only
polynomial size while \(N_q\) is exponential.  Across
\(O(\sqrt m)\) depths it is at most polynomial, still negligible beside
\(W/m\).

An unrestricted random permutation does map a positive fraction of the
holes to **some** covered targets when the covered density is positive:

\[
 \mathbb E|\{R\in{\cal Z}_q:\sigma R\notin{\cal Z}_q\}|
 ={h_q(N_q-h_q)\over N_q}.
 \tag{4.3}
\]

But those images are typically far from \(R\), and the corresponding
factor overlay may be connected.  The extension lemma does not provide
the component fragmentation needed to turn (4.3) into a legal partial
switch.

## 5. Effect on the soft multidepth gate

The extension lemma gives three precise conclusions.

1. **Depth one improves.**  Equation (2.5) is a stronger deterministic
   source of productive transpositions than the generic Johnson spectral
   bound.  It can be inserted directly into the exact biased/fair/local
   drift criteria of the soft-hole note.
2. **Each fixed higher depth has polynomial local expansion.**  Equation
   (3.7) gives a common small involution, but only at scale
   \(h_q/m^q\).  Iterating this for bounded \(q\) is not ruled out, but
   it is not a simultaneous Gaussian-band theorem.
3. **The Gaussian window is unchanged.**  Equation (4.2) loses the
   exponential rank size when one common unrestricted permutation is
   required.  It supplies only polynomial total local opportunity, while
   coefficient one needs control of \(W\)-scale defect across
   \(\Theta(\sqrt m)\) depths.

Thus the strongest useful new gate is depth one:

\[
 \boxed{
 A_{\tau,1}\ge{2(m+2)h_1\over m(2m+1)}
 \quad\text{for some transposition }\tau,}
 \tag{5.1}
\]

followed by the still-open component conversion estimate.  At larger
depth, extension expansion by itself does not bridge local target
richness to one fragmented exact-factor overlay.
