# General-route decision: three boxes are a no-go program; four boxes are the positive target

## 1. What finishing the current three-box seam analysis would prove

The original three-box hope was a uniform construction

\[
 g_3(p,q,r)\le w(p,q,r)+O((1+p+q+r)^{2-\varepsilon}).
\]

Fixed-dimensional aggregation would turn this into

\[
                       \nu(k)=(1+o(1))W(k).
\]

The current seam/run-spectrum program proceeds in the opposite direction:
it assumes a diagonal three-box word of length `M_a+o(a^2)` and tries to
derive a contradiction.  Closing its remaining absorbed/bad branch would
therefore prove a quadratic local obstruction

\[
 g_3(2a,2a,2a)-w(2a,2a,2a)=\Omega(a^2)
\]

(or at least non-`o(a^2)`).  This would kill the three-block aggregation
route.  It would not strengthen the Boolean-cube lower bound: product-box
aggregation is one-way.

The seam program remains worth finishing as a structural no-go theorem, but
it is not the primary positive path to the original problem.

## 2. The shortest credible positive target

For four chain factors, fixed-dimensional aggregation needs only one uniform
local theorem: for some fixed `epsilon>0`,

\[
 \boxed{
 g_4(\ell_1,\ell_2,\ell_3,\ell_4)
 \le w(\ell_1,\ell_2,\ell_3,\ell_4)
      +O((1+\ell_1+\ell_2+\ell_3+\ell_4)^{3-\varepsilon}).}
                                                               \tag{2.1}
\]

Uniformity includes unbalanced and degenerate height vectors.  Equation
(2.1) immediately implies

\[
                       \nu(k)=W(k)+o(W(k)).                    \tag{2.2}
\]

The existing explicit construction already handles the thin sector in
which the product of the two smaller side lengths is subcritical.  The only
remaining regime is the jointly thick sector.

## 3. The thick four-box tail-fusion target

The hook-product middle decomposition already supplies:

* exact central enumeration;
* all but `O(S^2)` first-shadow defects; and
* a family of lower and upper tail demands indexed by hook rectangles.

Independent repair of every block creates the unacceptable deep-tail cost.
The proposed replacement is a global transport braid.

Treat every missing lower tail as negative demand and the complementary
upper tail as positive demand on the hook-index grid.  Pair transposed
rectangle types `(H,K)` and `(K,H)`, orient their central-diagonal words
oppositely, and order blocks along trails of the signed demand flow.  An
interval crossing a consecutive segment of a trail should transport one
tail cell through the intermediate block boundaries; only trail endpoints
and divergence require literal repair.

The sharply testable intermediate theorem is:

> **Factorable hook-tail braid theorem.**  The signed hook-index demand can
> be packed into a single middle row with `O(S^2)` occurrence overload, while
> preserving the central-square intervals; upper demands are joins, lower
> demands are meets, and both are translated by one linked monotone,
> coordinatewise pinnable factor band of `O(S^2)` slack.

An `O(S^2)` abstract trail count alone is not sufficient: it controls neither
total cell reuse nor cross-block contamination, and a lower meet is not an
OR witness.  The factor and pin clauses are essential.  If the strengthened
theorem holds, the resulting max-word has only `O(S^2)` excess, stronger than
required by (2.1).

## 4. Route priority

1. Keep the three-box absorbed-drift analysis as a bounded no-go project.
2. Put the main positive effort into proving or falsifying the hook-tail
   trail theorem.
3. Treat exact `nu(k)=B(k)` as a later stage.  Constant one needs only
   subcubic four-box error; exact `B(k)` additionally requires additive
   `Theta(sqrt(k))` global control, exact endpoints, and pin survival.

This division prevents a negative local program from being mistaken for a
construction of the original arrays.
