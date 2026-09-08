# Extension-overlap charging for separated shadow leakage

Date: 2026-07-25

Method: pure mathematics only.

## 0. Setup

Put

\[
 n=2m+1,
 \qquad \Omega=\binom{[n]}m,
\]

and let \(F\) be an exact middle wreath factor.  Thus every
\(X\in\Omega\) has a unique owner row, denoted \(o_F(X)\).

Fix a coordinate permutation \(\sigma\) and a row cut \(A\subseteq F\).
As in the diagonal near-trade ledger, identify a row \(\sigma C\) of
\(\sigma F\) with \(C\in F\).  A middle set \(X\) is then the directed
owner-overlay edge

\[
 o_F(X)\longrightarrow o_F(\sigma^{-1}X).
\tag{0.1}
\]

Let

\[
 \mathcal B_\sigma(A)
 =\{X\in\Omega:
  \mathbf1_A(o_F(X))\ne
  \mathbf1_A(o_F(\sigma^{-1}X))\}.
\tag{0.2}
\]

Then

\[
 |\mathcal B_\sigma(A)|=\partial_\sigma(A).
\tag{0.3}
\]

The two directed parts of the cut both have size
\(\partial_\sigma(A)/2\), because the owner-overlay digraph is balanced.

Fix \(q\ge1\), and write \(r=m-q\).  If an \(r\)-interval \(S\) occurs
in a row \(C\), it is contained in exactly \(q+1\) middle intervals of
that row: extend it by \(t\) coordinates on the left and \(q-t\) on the
right, for \(0\le t\le q\).

Define the **owned middle-extension set**

\[
 E_q^F(S)=\{X\in\Omega:
  S\text{ is an }r\text{-interval in }o_F(X)
  \text{ and }X\text{ is a middle interval of that row containing }S\}.
\tag{0.4}
\]

Exact middle ownership makes the contributions from distinct occurrence
rows disjoint.  Hence

\[
 \boxed{|E_q^F(S)|=(q+1)\mu_q^F(S).}
\tag{0.5}
\]

The corresponding extension set in the relabeled factor is

\[
 E_q^{\sigma F}(S)=\sigma E_q^F(\sigma^{-1}S).
\tag{0.6}
\]

For brevity write \(\widetilde E_q(S)\) for the right side of (0.6).

## 1. Separated targets

Let

\[
 \mathsf O_q(S)=\{C\in F:S\text{ occurs in }C\},
\qquad
 \mathsf N_{\sigma,q}(S)
 =\{C\in F:\sigma^{-1}S\text{ occurs in }C\}.
\tag{1.1}
\]

The damaged targets for the two shore orientations are exactly

\[
 \mathcal D_q(A)
 =\{S:\mathsf O_q(S)\ne\varnothing,
       \mathsf O_q(S)\subseteq A,
       \mathsf N_{\sigma,q}(S)\subseteq A^c\},
\tag{1.2}
\]

\[
 \mathcal D_q(A^c)
 =\{S:\mathsf O_q(S)\ne\varnothing,
       \mathsf O_q(S)\subseteq A^c,
       \mathsf N_{\sigma,q}(S)\subseteq A\}.
\tag{1.3}
\]

They are disjoint.  Put

\[
 \mathcal D_{{\rm sep},q}(A)
 =\mathcal D_q(A)\sqcup\mathcal D_q(A^c),
 \qquad
 D_{{\rm sep},q}(A)=|\mathcal D_{{\rm sep},q}(A)|.
\tag{1.4}
\]

Define the zero-extension-overlap part

\[
 \mathcal Z_q^0(A)=
 \{S\in\mathcal D_{{\rm sep},q}(A):
 E_q^F(S)\cap\widetilde E_q(S)=\varnothing\},
 \qquad Z_q^0(A)=|\mathcal Z_q^0(A)|.
\tag{1.5}
\]

For a middle set \(X\), define its local common-extension multiplicity

\[
 \kappa_q(X)=
 \#\{S\in\tbinom{[n]}{m-q}:
       X\in E_q^F(S)\cap\widetilde E_q(S)\}.
\tag{1.6}
\]

Since the owner row of \(X\) has exactly \(q+1\) rank-\((m-q)\)
subintervals of \(X\),

\[
 0\le\kappa_q(X)\le q+1.
\tag{1.7}
\]

## 2. Exact extension-overlap charging theorem

### Theorem 2.1

For every exact factor \(F\), permutation \(\sigma\), row cut \(A\), and
depth \(q\ge1\),

\[
 \boxed{
 D_{{\rm sep},q}(A)
 \le Z_q^0(A)
     +\sum_{X\in\mathcal B_\sigma(A)}\kappa_q(X)
 \le Z_q^0(A)+(q+1)\partial_\sigma(A).}
\tag{2.1}
\]

More precisely, if \(\mathcal B_\to(A)\) denotes the overlay edges from
\(A\) to \(A^c\), and \(\mathcal B_\leftarrow(A)\) the reverse edges,
then

\[
 \boxed{
 D_q(A)
 \le Z_q^0(A;\to)
    +\sum_{X\in\mathcal B_\to(A)}\kappa_q(X)
 \le Z_q^0(A;\to)+{q+1\over2}\partial_\sigma(A),}
\tag{2.2}
\]

and the analogous reverse inequality holds for \(D_q(A^c)\).

### Proof

Take

\[
 S\in\mathcal D_{{\rm sep},q}(A)\setminus\mathcal Z_q^0(A).
\]

Choose

\[
 X\in E_q^F(S)\cap\widetilde E_q(S).
\]

If \(S\in\mathcal D_q(A)\), then the old owner \(o_F(X)\) belongs to
\(\mathsf O_q(S)\subseteq A\).  Since
\(X\in\widetilde E_q(S)=\sigma E_q^F(\sigma^{-1}S)\), its identified new
owner \(o_F(\sigma^{-1}X)\) belongs to
\(\mathsf N_{\sigma,q}(S)\subseteq A^c\).  Thus \(X\) is a directed cut
edge from \(A\) to \(A^c\).  The reverse conclusion holds when
\(S\in\mathcal D_q(A^c)\).

Instead of choosing one common extension, sum all of them.  Every target
outside \(\mathcal Z_q^0(A)\) contributes at least one incidence, so

\[
 \begin{aligned}
 D_{{\rm sep},q}(A)-Z_q^0(A)
 &\le
 \sum_{S\in\mathcal D_{{\rm sep},q}(A)}
 |E_q^F(S)\cap\widetilde E_q(S)|\\
 &\le
 \sum_{X\in\mathcal B_\sigma(A)}\kappa_q(X).
 \end{aligned}
\tag{2.3}
\]

Now use (1.7) and (0.3).  Restricting the same double count to one
orientation and using
\(|\mathcal B_\to(A)|=|\mathcal B_\leftarrow(A)|
=\partial_\sigma(A)/2\) proves (2.2). \(\square\)

The key point is that this is not an owner-spectrum estimate.  It is a
literal charging of every separated target with a common middle extension
to an actual diagonal boundary middle set.

## 3. Exact depth-one endpoint form

Let \(X\in\Omega\), and write its unique occurrence in its old owner row
as

\[
 X=(x_j,x_{j+1},\ldots,x_{j+m-1}).
\]

Define its unordered old endpoint pair

\[
 p_F(X)=\{x_j,x_{j+m-1}\}.
\tag{3.1}
\]

Likewise define the endpoint pair in its new owner row by

\[
 p_{\sigma F}(X)=\sigma p_F(\sigma^{-1}X).
\tag{3.2}
\]

The two depth-one subintervals of \(X\) in the old owner row are obtained
by deleting one of the two elements of \(p_F(X)\), and similarly on the
new side.  Therefore

\[
 \boxed{
 \kappa_1(X)=|p_F(X)\cap p_{\sigma F}(X)|\in\{0,1,2\}.}
\tag{3.3}
\]

For \(i=0,1,2\), put

\[
 \mathcal B_i(A)=\{X\in\mathcal B_\sigma(A):\kappa_1(X)=i\},
 \qquad b_i(A)=|\mathcal B_i(A)|.
\tag{3.4}
\]

Then the exact endpoint-refined estimate is

\[
 \boxed{
 D_{{\rm sep},1}(A)
 \le Z_1^0(A)+b_1(A)+2b_2(A).}
\tag{3.5}
\]

Since \(b_0+b_1+b_2=\partial_\sigma(A)\), this is equivalently

\[
 \boxed{
 D_{{\rm sep},1}(A)
 \le Z_1^0(A)+\partial_\sigma(A)+b_2(A)-b_0(A)
 \le Z_1^0(A)+2\partial_\sigma(A).}
\tag{3.6}
\]

For one shore orientation the corresponding worst-case bound is

\[
 \boxed{D_1(A)\le Z_1^0(A;\to)+\partial_\sigma(A),}
\tag{3.7}
\]

because its directed boundary contains \(\partial_\sigma(A)/2\) middle
sets and each has at most two common endpoint facets.

Thus the exact universal depth-one coefficient in the two-shore estimate
is \(2\), while the sharper invariant is not the boundary size alone but
the endpoint-alignment score \(b_1+2b_2\).  A coefficient smaller than two
cannot follow from the local extension incidence alone: a boundary middle
set may have the same two unordered endpoint coordinates in its old and
new owner rows, in which case \(\kappa_1(X)=2\).  Any further improvement
must use global restrictions on which such endpoint alignments can belong
to separated support families.

## 4. Consequence for the two-shore gain lemma

The weighted two-shore near-trade lemma gives

\[
 \max_{E\in\{A,A^c\}}\operatorname{Gain}_{w,H}(E,\sigma)
 \ge
 \sum_{q=1}^H w_q
 \bigl(\mathcal O_{\sigma,q}-D_{{\rm sep},q}(A)\bigr)
 -\partial_\sigma(A).
\tag{4.1}
\]

Substituting Theorem 2.1 yields the concrete sufficient estimate

\[
 \boxed{
 \begin{aligned}
 \max_{E\in\{A,A^c\}}\operatorname{Gain}_{w,H}(E,\sigma)
 \ge{}&
 \sum_{q=1}^H w_q
 \bigl(\mathcal O_{\sigma,q}-Z_q^0(A)\bigr)\\
 &-\sum_{X\in\mathcal B_\sigma(A)}
   \sum_{q=1}^H w_q\kappa_q(X)
 -\partial_\sigma(A).
 \end{aligned}}
\tag{4.2}
\]

In particular, at depth one,

\[
 \boxed{
 \max_{E\in\{A,A^c\}}\operatorname{Gain}_1(E,\sigma)
 \ge
 \mathcal O_{\sigma,1}-Z_1^0(A)
 -b_1(A)-2b_2(A)-\partial_\sigma(A).}
\tag{4.3}
\]

Hence low middle conductance does control all separated leakage except the
targets with **no common owned middle extension**.  The remaining positive
theorem can be stated concretely:

> Find a long cycle \(\sigma\) and a balanced low-boundary row cut \(A\)
> for which the global opportunity is large, almost every separated target
> has a common owned middle extension, and the boundary has small endpoint
> alignment score.

At depth one, it is enough that

\[
 Z_1^0(A)=o(W),
 \qquad
 \partial_\sigma(A)=o(W),
\tag{4.4}
\]

because then automatically \(b_1+2b_2\le2\partial=o(W)\).  Thus the truly
new condition beyond low conductance is the zero-overlap estimate
\(Z_1^0=o(W)\), not an unrestricted shadow-support coarea inequality.

## 5. Involutions: exclusive opportunity is automatically zero-overlap

Suppose now that \(\sigma^2=1\).  Consider a two-element target orbit

\[
 \{S,T\},\qquad T=\sigma S,
\]

with

\[
 \mu_q^F(S)=0<\mu_q^F(T).
\tag{5.1}
\]

Then \(E_q^F(S)=\varnothing\), and hence

\[
 \boxed{
 \widetilde E_q(T)
 =\sigma E_q^F(\sigma^{-1}T)
 =\sigma E_q^F(S)
 =\varnothing.}
\tag{5.2}
\]

Thus the covered partner of every hole-to-covered involution orbit has no
common owned middle extension at all.  In particular, for the cut-independent
zero-overlap count used in the coarser version of the extension theorem,

\[
 \boxed{Z^0_{\sigma,q}\ge\mathcal O_{\sigma,q}.}
\tag{5.3}
\]

Consequently the global expression
\(\mathcal O_{\sigma,q}-Z^0_{\sigma,q}\) can never certify positive gain for
an involution.  This applies, without any MSW-specific calculation, to both
the full parallel-pair involution of type \(1\,2^m\) and the truncated one
of type \(1^3\,2^{m-1}\).

The cut-dependent formulation is sharper and recovers the exact productive
condition.  Let

\[
 \mathsf O_q(T)=\{C\in F:T\text{ occurs in }C\}.
\]

For the orbit (5.1), put

\[
 t=|\mathsf O_q(T)|=\mu_q^F(T),
 \qquad a=|\mathsf O_q(T)\cap A|.
\]

The two loads after replacing \(A\) by \(\sigma A\) are

\[
 \boxed{(\mu_A(S),\mu_A(T))=(a,t-a).}
\tag{5.4}
\]

Therefore:

* if \(a=0\) or \(a=t\), one target remains missing; the covered partner
  is separated damage for one shore orientation and belongs to the
  cut-dependent \(\mathcal Z_q^0(A)\);
* if \(1\le a\le t-1\), both targets are covered; neither orientation
  damages the covered partner, so it is absent from the cut-dependent
  separated family.

Hence

\[
 \boxed{
 \text{an exclusive involution orbit is productive exactly when its
 occurrence-owner support is split by the row cut}.}
\tag{5.5}
\]

In particular load one is intrinsically unproductive.  Load at least two
is necessary but still not sufficient: the owner rows must lie on both
shores.  For parallel-pair bridges, endpoint-extension alignment therefore
does not bypass the duplicate-supply theorem.  It reduces exactly to the
duplicate-support splitting problem.
