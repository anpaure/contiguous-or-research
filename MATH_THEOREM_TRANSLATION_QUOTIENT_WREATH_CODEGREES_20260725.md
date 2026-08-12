# Translation-quotient wreath catalogue: exact degrees, codegrees, and the nibble gate

Date: 2026-07-25

Method: exact physical counting followed by cyclic quotienting.  No
computation and no fixed-uniformity matching theorem are used.

## 0. Outcome

Let

\[
 n=2m+1
\]

be prime, identify the ground set with `Z_n`, and let `rho:x->x+1`.
Consider the quotient hypergraph whose vertices are translation necklaces
of middle `m`-sets and whose edges are translation orbits of wreath rows
whose middle windows lie in distinct necklaces.

The catalogue is asymptotically full-degree in the averaged sense, but its
maximum pair codegree is

\[
 \boxed{\overline\Delta _2=\Theta(D/m),
 \qquad D={m!(m+1)!\over2}.}
\tag{0.1}
\]

In particular, cyclic quotienting does **not** improve the relative
codegree to `O(m^-2)`.  A disjoint physical alignment survives the phase
sum and forces the `Theta(1/m)` term.

The numerical parameters do not forbid a long quotient nibble: in an
exogenous residual of density `u`, the expected relative pair link is
`O(1/(mu))`, and the first-moment stall is still only `Theta(1/m)`.
However, one elementary bite or a maximal greedy matching covers only
`Theta(1/n)` of the quotient vertices.  Iteration to an `o(1)` leave needs
the same hereditary residual-flatness and longitudinal anti-clustering
statement as the unquotiented hard-middle nibble.  No such theorem is
proved here.  Thus the quotient supplies no black-box near-perfect
matching theorem; any success must use additional quotient geometry or a
new growing-uniformity nibble argument.

## 1. Physical normalization

Let

\[
 \Omega=\binom{\mathbb Z_n}{m},\qquad
 W=|\Omega|,\qquad T={W\over n}=\operatorname {Cat}_m.
\tag{1.1}
\]

A **row** means a geometric cyclic ordering, modulo rotation and reversal.
Its middle support `E(C)` is the set of its `n` cyclic `m`-windows.  The
number of rows and the degree of a fixed middle set are

\[
 M={(n-1)!\over2}=TD,
 \qquad
 D={m!(m+1)!\over2}.
\tag{1.2}
\]

For distinct `A,B in Omega`, put

\[
 d(A,B)=|A\setminus B|=|B\setminus A|.
\]

The physical common-row count is

\[
 d_{\rm phys}(A,B)
 =d!^2(m-d)!(m+1-d)!,
\tag{1.3}
\]

and hence

\[
 \boxed{
 {d_{\rm phys}(A,B)\over D}
 ={2\over\binom md\binom{m+1}d}.}
\tag{1.4}
\]

To see (1.3), the four regions
`A cap B`, `A\B`, the exterior of `A union B`, and `B\A` must occur as
the four cyclic blocks determined by the two equal-length intervals.
Their internal orders are arbitrary.  The two possible cyclic directions
are identified by reversal, leaving exactly the product in (1.3).

## 2. Transversal rows and the quotient hypergraph

Call a row `C` **transversal** when its `n` middle windows belong to `n`
distinct `rho`-necklaces.  Equivalently,

\[
 E(C)\cap \rho^aE(C)=\varnothing
 \qquad(1\le a<n).
\tag{2.1}
\]

Every transversal row has a free orbit of size `n`.  Its row orbit is a
middle packing, and its projection is a simple `n`-edge on the necklace
set

\[
 \overline\Omega=\Omega/\langle\rho\rangle,
 \qquad |\overline\Omega|=T.
\tag{2.2}
\]

Let `Hbar_tr` denote the resulting `n`-uniform quotient hypergraph.  In
the voltage language, its edges are exactly the simple zero-voltage
`n`-cycles in the quotient odd graph.

Fix a representative `A` of a quotient vertex `[A]`.  Every quotient
edge incident to `[A]` has a unique row representative containing `A`.
Therefore

\[
 \boxed{
 d_{\overline H}([A])
 =\#\{C:A\in E(C),\ C\text{ transversal}\}
 \le D.}
\tag{2.3}
\]

The degree need not be literally identical on all necklace types; the
normalizer of one fixed `n`-cycle is not transitive on all necklaces.
The next section gives the exact averaged loss.

## 3. Nontransversal rows are an exponentially small fraction

For a fixed nonzero `a`, the number of `m`-sets satisfying

\[
 d(A,A+a)=d
\]

is

\[
 N_d={n\over d}
      \binom{m-1}{d-1}\binom m{d-1}.
\tag{3.1}
\]

Indeed, in the cyclic binary word of `A` relative to the step `a`, the
number `d` is the number of one-runs.  Compose the `m` ones and the `m+1`
zeros into `d` positive runs and account for the `n/d` choices of cyclic
origin.

Combining (1.4) and (3.1) gives the useful exact cancellation

\[
\begin{aligned}
 {1\over D}\sum_{A\in\Omega}d_{\rm phys}(A,A+a)
 &=\sum_{d=1}^m
 {n\over d}\binom{m-1}{d-1}\binom m{d-1}
 {2\over\binom md\binom{m+1}d}\\
 &=\sum_{d=1}^m{2nd\over m(m+1)}=n.
\end{aligned}
\tag{3.2}
\]

Let `B_bad` be the number of nontransversal physical rows.  Count triples
`(C,A,a)` with `a nonzero` and `A,A+a in E(C)`.  Every nontransversal row
contributes at least one triple, while (3.2) gives

\[
 \boxed{B_{\rm bad}\le n(n-1)D.}
\tag{3.3}
\]

Consequently

\[
 {B_{\rm bad}\over M}
 \le {n(n-1)\over T}
 ={n^2(n-1)\over W}=e^{-\Theta(m)}.
\tag{3.4}
\]

There is also an exact degree-defect ledger.  Sum one representative
degree over the `T` target necklaces.  A free bad row orbit contributes
exactly its orbit size `n` to this sum, even when its support repeats a
necklace; a fixed AP row contributes one.  Hence

\[
 \boxed{
 \sum_{[A]\in\overline\Omega}
       \bigl(D-d_{\overline H}([A])\bigr)=B_{\rm bad}.}
\tag{3.5}
\]

In particular the average quotient degree is

\[
 \overline d=D-{B_{\rm bad}\over T}
 =D\left(1-O\left({n^2\over T}\right)\right),
\tag{3.6}
\]

and, for every `epsilon>0`, all but

\[
 {n(n-1)\over\epsilon T}\,T
\tag{3.7}
\]

necklace vertices have degree at least `(1-epsilon)D`.  Thus all but an
exponentially small fraction of quotient vertices have essentially full
degree.  This is an averaged trimming statement; it does not by itself
say that deleting the exceptional vertices preserves the links of all
remaining vertices.

## 4. Exact quotient pair-codegree identity

Let `[A]` and `[B]` be distinct necklace vertices.  A transversal row
orbit incident to both has a unique representative containing `A`, and
that representative contains exactly one translate `B+a`.  Therefore

\[
 \boxed{
 d_{\overline H}([A],[B])
 =\sum_{a\in\mathbb Z_n}
   d_{\rm tr}(A,B+a),}
\tag{4.1}
\]

where `d_tr` counts transversal physical rows through the indicated pair.
In particular, with

\[
 d_a=|A\setminus(B+a)|,
\]

one has

\[
 {d_{\overline H}([A],[B])\over D}
 \le
 \sum_{a\in\mathbb Z_n}
 {2\over\binom m{d_a}\binom{m+1}{d_a}}.
\tag{4.2}
\]

This identity is the precise sense in which quotient codegree is a phase
sum of physical codegrees.  It is not, in general, one physical
codegree.

## 5. Uniform upper bound: at most `8D/m`

Because `[A]` and `[B]` are distinct, `d_a` is never zero.  The phases
with `d_a=m` are exactly those with

\[
 A\cap(B+a)=\varnothing.
\]

They are the elements outside the difference set `A-B`.  By
Cauchy--Davenport,

\[
 |A-B|\ge |A|+|B|-1=2m-1=n-2,
\tag{5.1}
\]

so there are at most two disjoint phases.

For `1<=d<=m-1`,

\[
 \binom md\ge m,
 \qquad
 \binom{m+1}d\ge m+1.
\tag{5.2}
\]

Using (4.2), the at most two disjoint phases contribute at most
`4/(m+1)`, and all other phases contribute at most

\[
 {2(n-2)\over m(m+1)}.
\]

Therefore

\[
 \boxed{
 \Delta _2(\overline H_{\rm tr})
 \le {8m-2\over m(m+1)}D
 <{8D\over m}.}
\tag{5.3}
\]

This is already only `Theta(D/m)`, not `O(D/m^2)`.

## 6. Matching lower bound: the `1/m` term is real

The upper bound has the correct order.  There are

\[
 Q={W(m+1)\over2}
\tag{6.1}
\]

unordered disjoint pairs of physical middle sets.  Among them, the pairs
lying in one translation necklace number exactly

\[
 Q_{\rm same}={n(n-1)\over2}.
\tag{6.2}
\]

Indeed, (3.1) at `d=m` gives exactly `n` sets `A` for every nonzero
translation `a`, and every unordered pair is counted in the two
directions.

Every transversal row contains exactly `n` unordered disjoint pairs of
middle windows, and all these pairs join distinct necklaces.  Hence

\[
 \sum_{\substack{\{A,B\}:\ A\cap B=\varnothing\\[A]\ne[B]}}
 d_{\rm tr}(A,B)
 =n(M-B_{\rm bad}).
\tag{6.3}
\]

Dividing by `Q-Q_same`, and using (3.4), shows that some disjoint pair
`A,B` in distinct necklaces satisfies

\[
 d_{\rm tr}(A,B)
 \ge\left(1-o(1)\right){2D\over m+1}.
\tag{6.4}
\]

Its physical alignment is one summand in (4.1), so

\[
 \boxed{
 \Delta _2(\overline H_{\rm tr})
 \ge\left(2-o(1)\right){D\over m+1}.}
\tag{6.5}
\]

Together, (5.3) and (6.5) prove (0.1).  The obstruction is exactly the
disjoint-pair backbone of the physical wreath catalogue.  Passing to
translation necklaces does not average it away.

## 7. What elementary greedy and one nibble bite give

The number of quotient edges is

\[
 |E(\overline H_{\rm tr})|
 ={M-B_{\rm bad}\over n}
 =(1-o(1)){TD\over n}.
\tag{7.1}
\]

A maximal greedy matching has at least

\[
 {|E(\overline H_{\rm tr})|\over nD}
 =(1-o(1)){T\over n^2}
\tag{7.2}
\]

edges, because one chosen edge meets at most `nD` catalogue edges.  This
covers only `(1-o(1))T/n` vertices.  The same scale arises from a single
independent isolated-edge bite: sampling each edge with probability
`theta/(nD)` retains `Theta(T/n^2)` edges and covers `Theta(T/n)`
vertices.

Thus neither maximal greedy nor one bite is a near-perfect quotient
matching theorem.

## 8. Why a long nibble remains plausible but unproved

For comparison, suppose quotient vertices survive independently with
density `u`.  Conditional on one vertex surviving, the expected live
degree has scale

\[
 d(u)=Du^{n-1}.
\tag{8.1}
\]

Conditioned on a pair surviving, (5.3) gives the expected relative pair
link

\[
 {\Delta _2(u)\over d(u)}
 \le {8+o(1)\over mu}.
\tag{8.2}
\]

The expected live catalogue size is

\[
 (1-o(1)){TD\over n}u^n,
\tag{8.3}
\]

whose first-moment stall is

\[
 u_*={e+o(1)\over2m}.
\tag{8.4}
\]

Consequently the product model is still numerically healthy at, for
example, `u=1/log m` or `u=omega(m)/sqrt(m)`: degrees are enormous and
the relative pair link is `o(1)`.  Quotienting by `n` changes none of the
exponential scales.

What is not justified is replacing an exogenous product residual by the
endogenous residual of `Theta(n log(1/u))` preceding bites.  A sufficient
multi-round theorem would have to prove, uniformly along that trajectory,

1. residual degrees `(1+o(1))Du_t^(n-1)` outside an `o(T)` set;
2. edge-neighborhood overlap `o(nd_t)`;
3. a two-time anti-clustering estimate for disjoint original quotient
   edges, strong enough to sum their selection probabilities over all
   rounds.

These are the same longitudinal gates as in the physical hard-middle
nibble.  The quotient estimate `Delta_2/D=Theta(1/m)=Theta(1/n)` does not
close them.  Fixed-uniformity almost-matching theorems also cannot simply
be diagonalized: their small-codegree threshold is allowed to depend on
the uniformity, while here the uniformity tends to infinity and the
available ratio is only `Theta(1/n)`.

Therefore the rigorous verdict is

\[
 \boxed{
 \begin{gathered}
 \text{the direct quotient nibble is not first-moment stalled,}\
 \text{but degree/codegree counting alone does not prove a}\
 \text{near-perfect quotient matching.}
 \end{gathered}}
\tag{8.5}
\]

Any completion of this route needs either a genuinely growing-uniformity
longitudinal nibble theorem or extra expansion/recursive structure of the
zero-voltage cycle catalogue.

## 9. Exact status

Proved here:

* the physical-to-quotient degree identity (2.3);
* the exact nontransversal-row bound (3.3) and averaged degree ledger
  (3.5);
* the exact phase-sum codegree identity (4.1);
* the uniform upper bound `Delta_2<8D/m`;
* the matching lower bound `Delta_2>=(2-o(1))D/(m+1)`;
* the maximal-greedy and one-bite scales;
* the product-residual parameter calculation.

Not proved here:

* uniform pointwise lower degree after deleting every exceptional
  necklace type;
* hereditary flatness of matching-generated residuals;
* a near-perfect matching in the quotient catalogue;
* any multidepth rainbow property of such a matching.
