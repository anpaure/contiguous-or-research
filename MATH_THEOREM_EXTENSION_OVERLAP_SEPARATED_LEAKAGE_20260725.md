# Extension overlap controls separated shadow leakage

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let `F` be an exact middle wreath factor, let `sigma` be a coordinate
permutation, and replace a row family `A subseteq F` by its diagonal image
`sigma A`.  The two orientations `A` and `A^c` have the same middle
boundary.  At depth `q`, the only covered targets which can be lost by one
of these orientations are targets whose old occurrence support and pulled
back new occurrence support lie on opposite shores.

For a target `S`, let `E_q^F(S)` be the set of middle supersets which
literally extend an occurrence of `S` inside its owner wreath.  The main
theorem proves

\[
 D_{{\rm sep},q}(A)
 \le Z^0_{\sigma,q}+(q+1)\,\partial_\sigma(A),
\tag{0.1}
\]

where `Z^0_(sigma,q)` is the number of old covered targets having no
common witnessing middle extension with their pulled-back new support,
including the case in which that new support is empty.  At the first shadow the
coefficient is exactly two.

Combining (0.1) with the two-shore opportunity inequality gives

\[
 \max_{E\in\{A,A^c\}}\operatorname {Gain}_w(E,\sigma)
 \ge
 \sum_{q\le H}w_q
 \bigl(\mathcal O_{\sigma,q}-Z^0_{\sigma,q}\bigr)
 -\left(1+\sum_{q\le H}(q+1)w_q\right)
 \partial_\sigma(A).
\tag{0.2}
\]

Thus low owner conductance is not by itself sufficient.  One additionally
needs extension alignment: most useful covered target pairs must share a
middle extension.  For a generic relative orientation this is a very
strong demand already at `q=1`, because two endpoint pairs inside an
`(m+2)`-element extension star usually do not meet.

## 1. Witnessing middle extensions

Put

\[
 n=2m+1,\qquad \Omega_m=\binom{[n]}m.
\tag{1.1}
\]

For `S in binom([n],m-q)`, define

\[
 E_q^F(S)=\{X\in\Omega_m:
   X\text{ is a middle interval in its unique owner row }C\in F,
   \text{ and }S\text{ is an }(m-q)\text{-interval of }C
   \text{ contained in }X\}.
\tag{1.2}
\]

If one occurrence of `S` lies in a row `C`, exactly `q+1` of the middle
windows of `C` contain that occurrence: one may add `a` symbols at its left
end and `q-a` at its right end, for `0<=a<=q`.  Different occurrences lie
in different owner rows, and exact middle ownership makes their witnessing
middle sets disjoint.  Consequently

\[
 \boxed{|E_q^F(S)|=(q+1)\mu_q^F(S).}
\tag{1.3}
\]

The witnessing set supplied by the new rows `sigma A` is

\[
 E_{q,\sigma}^F(S)
 :=\sigma E_q^F(\sigma^{-1}S).
\tag{1.4}
\]

Define the common-extension multiplicity

\[
 c_{\sigma,q}(S)
 =|E_q^F(S)\cap E_{q,\sigma}^F(S)|.
\tag{1.5}
\]

Finally let

\[
 Z^0_{\sigma,q}
 =\#\{S:
 \mu_q^F(S)>0,\ c_{\sigma,q}(S)=0\}.
\tag{1.6}
\]

This definition is independent of the row cut.  In particular, if
`mu_q^F(sigma^{-1}S)=0`, then `S` is included in `Z^0_(sigma,q)`.

## 2. Diagonal boundary and separated leakage

For `A subseteq F`, let

\[
 U(A)=\bigcup_{C\in A}{\cal W}_m(C),\qquad
 \partial_\sigma(A)=|U(A)\triangle\sigma U(A)|.
\tag{2.1}
\]

Because `F` partitions the middle layer,

\[
 U(A^c)=\Omega_m\setminus U(A),\qquad
 \sigma U(A^c)=\Omega_m\setminus\sigma U(A).
\tag{2.2}
\]

Write `D_q(A)` for the number of previously covered depth-`q` targets
which become holes after replacing `A` by `sigma A`.  Put

\[
 D_{{\rm sep},q}(A)=D_q(A)+D_q(A^c).
\tag{2.3}
\]

The two damage families are disjoint.  A target counted by `D_q(A)` has
all its old occurrence rows in `A` and all the source rows of its pulled
back new occurrences in `A^c`.  Hence

\[
 E_q^F(S)\subseteq U(A),\qquad
 E_{q,\sigma}^F(S)\subseteq\sigma U(A^c).
\tag{2.4}
\]

By (2.2), every common witnessing extension of such a target belongs to

\[
 U(A)\setminus\sigma U(A).
\tag{2.5}
\]

The opposite orientation similarly places every common extension in
`sigma U(A) setminus U(A)`.

## 3. The extension-overlap charging theorem

### Theorem 3.1

For every exact factor `F`, every coordinate permutation `sigma`, every
row cut `A`, and every depth `q`,

\[
 \boxed{
 D_{{\rm sep},q}(A)
 \le Z^0_{\sigma,q}+(q+1)\partial_\sigma(A).}
\tag{3.1}
\]

At `q=1`,

\[
 \boxed{D_{{\rm sep},1}(A)
 \le Z^0_{\sigma,1}+2\partial_\sigma(A).}
\tag{3.2}
\]

#### Proof

Split the separated damaged targets according to whether
`c_(sigma,q)(S)` vanishes.  The zero part has size at most
`Z^0_(sigma,q)` by definition.

For the positive part, count pairs `(S,X)` with `S` separated damaged and

\[
 X\in E_q^F(S)\cap E_{q,\sigma}^F(S).
\tag{3.3}
\]

Every target in the positive part contributes at least one pair.  By
(2.5) and its opposite-shore analogue, every such `X` lies in the middle
boundary `U(A) triangle sigma U(A)`.

Fix a boundary middle set `X`.  In its old owner row there are exactly
`q+1` depth-`q` intervals witnessed through `X`: delete `a` symbols from
the left and `q-a` from the right, `0<=a<=q`.  The new owner row gives
another family of `q+1` such intervals.  Their intersection has size at
most `q+1`.  Hence a fixed boundary `X` occurs in at most `q+1` pairs
(3.3).

There are `partial_sigma(A)` boundary middle sets.  Thus the positive part
has size at most `(q+1)partial_sigma(A)`, which together with the zero part
proves (3.1).  Equation (3.2) is the specialization `q=1`. \(\square\)

The coefficient `q+1` is the sharp local counting constant: if the old
and new induced orders agree on one middle set, all `q+1` witnessed
subintervals through that middle set can agree.

## 4. Combination with the two-shore opportunity theorem

Let `R_q(A)` be the number of old holes repaired by the diagonal
replacement, and let

\[
 \mathcal O_{\sigma,q}
 =\#\{S:\mu_q^F(S)=0,\ \mu_q^F(\sigma^{-1}S)>0\}.
\tag{4.1}
\]

For nonnegative weights `w_q`, define the literal central-band gain

\[
 \operatorname {Gain}_w(A,\sigma)
 =2\sum_{q\le H}w_q\bigl(R_q(A)-D_q(A)\bigr)
  -\partial_\sigma(A).
\tag{4.2}
\]

The middle boundary is charged once because it creates
`partial_sigma(A)/2` missing masks in each of the complementary middle
ranks.  The two orientations obey

\[
 R_q(A)+R_q(A^c)\ge\mathcal O_{\sigma,q}.
\tag{4.3}
\]

Therefore

\[
 \max_{E\in\{A,A^c\}}\operatorname {Gain}_w(E,\sigma)
 \ge
 \sum_{q\le H}w_q
 \bigl(\mathcal O_{\sigma,q}-D_{{\rm sep},q}(A)\bigr)
 -\partial_\sigma(A).
\tag{4.4}
\]

Substitution of Theorem 3.1 gives the advertised inequality

\[
 \boxed{
 \max_{E\in\{A,A^c\}}\operatorname {Gain}_w(E,\sigma)
 \ge
 \sum_{q\le H}w_q
 \bigl(\mathcal O_{\sigma,q}-Z^0_{\sigma,q}\bigr)
 -\left(1+\sum_{q\le H}(q+1)w_q\right)
 \partial_\sigma(A).}
\tag{4.5}
\]

This is a sufficient one-shot bridge theorem stated entirely through
three explicit quantities:

1. global hole-to-covered opportunity;
2. extension-disjoint covered-pair obstruction;
3. diagonal middle boundary.

## 5. First-shadow interpretation

For `q=1`, `E_1^F(R)` consists of the middle supersets of `R` arising as
the two endpoint extensions of every occurrence.  Exact ownership and the
matching property inside the Johnson clique `K_R` give

\[
 |E_1^F(R)|=2\mu_1^F(R).
\tag{5.1}
\]

Thus `Z^0_(sigma,1)` counts old covered targets for which the old endpoint
extension set and the relabelled pulled-back endpoint extension set are
disjoint, including every covered-to-hole target.  If both loads are one,
these are two two-element subsets of the
`m+2` possible middle extensions.  Unstructured relative orientations
typically make them disjoint.  Hence (4.5) does not make a generic bridge
work; it identifies exactly what an algebraically aligned bridge must
provide in addition to target mixing and low owner conductance.

There is a particularly important involutive consequence.  Suppose
`sigma^2=1` and the target orbit `{R,sigma R}` has loads `(0,1)`.  Switching
the unique owner of the covered target repairs one member and destroys the
other; not switching leaves the original hole.  No diagonal cut reduces
the number of holes on this orbit.  A strict improvement is possible only
when the covered member has at least two owner occurrences which the cut
can split between its shores.  Hence selective switching eliminates the
specific fair-coin duplicate ledger, but it does **not** eliminate the
underlying duplicate-supply requirement.

In particular, the surviving coefficient-one bridge is not merely

\[
 \text{fragmentation} + \text{target opportunity}.
\]

It is

\[
 \boxed{
 \text{low middle boundary}
 +\text{hole opportunity}
 +\text{common-extension alignment}.}
\]
