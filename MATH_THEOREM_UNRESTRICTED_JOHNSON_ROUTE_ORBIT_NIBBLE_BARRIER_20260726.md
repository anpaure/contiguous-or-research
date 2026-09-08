# Unrestricted Johnson route orbits: exact quota degrees and the long-edge nibble barrier

Date: 2026-07-26

Method: pure mathematics only.  No finite search, computation, solver, or
web input is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 p_q={N_q\over W}.
\]

An unrestricted cyclic Johnson route of length \(L\) which is geodesic
through depth \(H\) has literal traces

\[
 T^-_{i,q}=X_i\cap X_{i+q},\qquad
 T^+_{i,q}=X_i\cup X_{i+q}.
\]

There is no fractional Hall obstruction.  After accepting a fraction
\(p_q\) of the starts at signed depth \(q\), the full coordinate orbit is
an exactly regular fractional hypergraph on middle owners and on every
typed target rank.  The exact orbit degrees and every pair codegree are
computed below.

The computation nevertheless refutes the standard long-route
nibble/LLL implementation of this fractional point.  In every
quota-balanced route hypergraph, an accepted depth-one target is carried
together with its two physical endpoint owners.  Consequently

\[
 \boxed{\displaystyle {\Delta _2\over D}\ge {2\over m+1}.}       \tag{0.1}
\]

On the other hand the number of resources in one radius-thinned route is

\[
 K=(1+o(1))L\left(1+2\sum_{q\le H}p_q\right)
   =\Theta(L\sqrt m)                                      \tag{0.2}
\]

on every nontrivial Gaussian window.  Cyclic depth-\(H\) geodesicity
forces \(L\ge2H\).  Hence

\[
 \boxed{\displaystyle
 K{\Delta _2\over D}
 \ge (8+o(1)){H\over\sqrt m}
       \int_0^{H/\sqrt m}e^{-x^2}\,dx.}                   \tag{0.3}
\]

It is bounded away from zero when \(H\asymp\sqrt m\), and tends to
infinity when \(H/\sqrt m\to\infty\).  Thus unrestricted coordinate
mixing cannot put the quota hypergraph in the usual growing-uniformity
regime \(K\Delta _2/D=o(1)\).  This is intrinsic, not a fixed-atlas
artifact.

There is a stronger failure of the proposed hereditary nibble invariant.
Even if **all** Johnson routes and all balanced quota marks are allowed,
an independently thinned residual of any polynomial density has
asymptotically empty links.  More precisely, conditional on retaining a
fixed owner and retaining every other resource independently with
probability \(\varepsilon=m^{-\alpha}\), \(\alpha>0\), the expected number
of surviving quota-route columns through that owner is \(o(1)\).  Thus a
product-quasirandom residual cannot be iterated down to the required
\(o(1/H)\) owner leave.

These statements do **not** obstruct an unrestricted Hamilton cycle or
2-factor itself.  Such an object would use strong chronological
correlations which the product nibble discards.  The surviving gate is a
direct correlated quota-rainbow transition/absorption theorem, not a
small-codegree matching theorem.

## 1. Cyclic geodesic routes and quota marks

Let

\[
 \mathcal O=\binom{[2m]}m,qquad
 \mathcal T_q^- =\binom{[2m]}{m-q},\qquad
 \mathcal T_q^+ =\binom{[2m]}{m+q}.
\]

An oriented cyclic route is a sequence of distinct middle sets

\[
 P=(X_i:i\in\mathbb Z_L)
\]

with \(X_iX_{i+1}\in E(J(2m,m))\).  It is an
\(H\)-geodesic route if

\[
 d_J(X_i,X_{i+q})=q
 \qquad(i\in\mathbb Z_L, 1\le q\le H).                  \tag{1.1}
\]

Then the two traces displayed in Section 0 have sizes \(m-q\) and
\(m+q\).  We call a set of accepted starts

\[
 A_q^\epsilon\subseteq\mathbb Z_L
 \qquad(1\le q\le H,\ \epsilon\in\{-,+\})                \tag{1.2}
\]

internally rainbow if \(i\mapsto T_{i,q}^\epsilon\) is injective on
\(A_q^\epsilon\).  A quota-marked route claims all \(L\) owners and the
accepted typed targets.

The correct accepted density is \(p_q=N_q/W\).  Write

\[
 b_q=\lfloor Lp_q\rfloor,qquad
 \theta_q=Lp_q-b_q.                                      \tag{1.3}
\]

For each signed depth, take a uniformly random \(b_q\)-subset of starts
with probability \(1-\theta_q\), and a uniformly random
\((b_q+1)\)-subset with probability \(\theta_q\).  Every start is then
accepted with probability exactly \(p_q\).  All probabilities are
rational, so clearing denominators produces a finite multiset of integral
quota markings.  This is only a device for making the orbit degree
identities integral; it makes no construction choice at separate depths.

Let \(M\) be the total multiplicity after clearing denominators.  For
every \(\pi\in S_{2m}\) and every marking copy, take the coordinate
translate \(\pi P\) with the translated claims.  Indexed duplicates are
retained in the census.  They do not improve an integral matching because
duplicates share all of their resources.

## 2. Exact orbit degrees

### Theorem 2.1 (exact regular quota orbit)

Assume all accepted trace maps are internally rainbow.  In the indexed
orbit multihypergraph above, every owner and every typed target at every
signed depth have the same degree

\[
 \boxed{D=ML(m!)^2.}                                      \tag{2.1}
\]

The mean column size is

\[
 \boxed{\overline K
   =L\left(1+2\sum_{q=1}^Hp_q\right).}                    \tag{2.2}
\]

Every column has size at least

\[
 K_-:=L+2\sum_{q=1}^H\lfloor Lp_q\rfloor.                \tag{2.3}
\]

#### Proof

For a fixed base owner \(X_i\) and a fixed physical owner \(X\), exactly
\((m!)^2\) coordinate permutations send \(X_i\) to \(X\).  There are
\(L\) base owners and \(M\) marking copies, giving (2.1) on the owner
layer.

Across the \(M\) markings, a fixed start is accepted exactly \(Mp_q\)
times.  Hence there are \(MLp_q\) accepted base occurrences at signed
depth \(q\).  For a base target of size \(m-q\), exactly

\[
 (m-q)!(m+q)!
\]

permutations send it to a fixed physical target.  The same formula holds
at size \(m+q\).  Since

\[
 p_q(m-q)!(m+q)!=(m!)^2,                                  \tag{2.4}
\]

the target degree is also (2.1).  Internal rainbowness ensures that this
occurrence count is the support degree of the column hypergraph.  Formula
(2.2) follows by expectation, and (2.3) follows from (1.3). \(\square\)

Thus unrestricted coordinate symmetrization closes the fractional
all-depth Hall equations exactly.  The issue is integral common-route
rounding.

## 3. Exact pair-codegree formula

The orbit permits a complete profile calculation.  Let two typed base
claims have sizes \(k,l\) and intersection size \(a\).  Let
\(I_{k,l,a}\) be the number of ordered pairs of such claims, summed over
the \(M\) marking copies.  For fixed physical claims \(Z,Z'\) of those
types with \(|Z\cap Z'|=a\), their indexed codegree is

\[
 \boxed{
 d(Z,Z')=I_{k,l,a}\,
 a!(k-a)!(l-a)!(2m-k-l+a)!.}                              \tag{3.1}
\]

Indeed, after the four Venn cells of the base pair have been mapped to
the four Venn cells of \((Z,Z')\), the permutation is arbitrary inside
those cells.  Their factorials give (3.1).

For example, let

\[
 A_j(P)=|\{(i,s):i\ne s,\ d_J(X_i,X_s)=j\}|.              \tag{3.2}
\]

For two owners at Johnson distance \(j\), (3.1) gives

\[
 {d(X,Y)\over D}
 ={A_j(P)\over L}\binom mj^{-2}.                         \tag{3.3}
\]

When \(j<H\), the two cyclic offsets \(\pm j\) already give
\(A_j(P)\ge2L\).  Nonlocal Johnson chords can only increase (3.3).
Thus delay alone does not give the upper codegree \(2/m^2\) enjoyed by
special chord-free cube routes.

The decisive codegree is instead forced from below at the owner/target
interface.

### Theorem 3.1 (unavoidable endpoint codegree)

For either sign and every \(q\le H\), the regular quota orbit satisfies

\[
 \boxed{
 {\Delta_2\over D}\ge
 {q+1\over\binom{m+q}{q}}.}                               \tag{3.4}
\]

In particular, at depth one,

\[
 \boxed{{\Delta_2\over D}\ge {2\over m+1}.}              \tag{3.5}
\]

#### Proof

Every lower trace \(T^-_{i,q}\) is contained in all \(q+1\) route owners

\[
 X_i,X_{i+1},\ldots,X_{i+q};                              \tag{3.6}
\]

every upper trace contains the same \(q+1\) owners.  Hence the number of
ordered accepted lower-trace/containing-owner base pairs is at least

\[
 (q+1)MLp_q.                                              \tag{3.7}
\]

The group is transitive on incident pairs \(T\subset X\), so (3.1), or
direct double counting over the \(\binom{m+q}{q}\) middle subsets of one
upper target, gives

\[
 {d(T,X)\over D}
 \ge (q+1)p_q{q!(m-q)!\over m!}
 ={q+1\over\binom{m+q}{q}}.                              \tag{3.8}
\]

The upper sign is identical.  Extra containments by nonlocal route owners
only increase the codegree. \(\square\)

At \(q=1\), (3.5) has a direct interpretation: every accepted edge color
\(S=X_i\cap X_{i+1}\) is claimed together with both of its endpoint
owners, and there are only \(m+1\) middle supersets of \(S\).

## 4. Gaussian quota mass and the small-codegree no-go

For \(q=o(m^{2/3})\),

\[
 \log p_q=-{q^2\over m}
 +O\left({q\over m}+{q^3\over m^2}\right).                \tag{4.1}
\]

This follows by expanding the exact product

\[
 p_q=\prod_{i=0}^{q-1}{m-i\over m+i+1}.                  \tag{4.2}
\]

Consequently, if \(H/\sqrt m\to A\in(0,\infty)\), then

\[
 \sum_{q=1}^Hp_q
 =(1+o(1))\sqrt m\int_0^Ae^{-x^2}\,dx,                  \tag{4.3}
\]

while if \(H/\sqrt m\to\infty\) and \(H=o(m^{2/3})\),

\[
 \sum_{q=1}^Hp_q
 =\left({\sqrt\pi\over2}+o(1)\right)\sqrt m.             \tag{4.4}
\]

These are ordinary Riemann sums; (4.1) supplies uniform domination.

### Lemma 4.1 (cyclic length bound)

Every cyclic \(H\)-geodesic route has \(L\ge2H\).

#### Proof

If \(L<2H\), the two cyclic separations between \(X_i\) and \(X_{i+H}\)
are \(H\) and \(L-H<H\).  Equation (1.1), applied in the two directions,
would make their Johnson distance both \(H\) and \(L-H\), a contradiction.
The equality \(L=2H\) is not excluded. \(\square\)

Since \(\lfloor x\rfloor\ge x-1\), (2.3) and Lemma 4.1 give

\[
 K_-
 \ge L+2L\sum_{q\le H}p_q-2H
 \ge2L\sum_{q\le H}p_q.                                 \tag{4.5}
\]

Combining (3.5) and (4.5),

\[
 K_-{\Delta_2\over D}
 \ge {4L\over m+1}\sum_{q\le H}p_q
 \ge {8H\over m+1}\sum_{q\le H}p_q.                    \tag{4.6}
\]

Equations (4.3)--(4.4) prove (0.3).

The role of this parameter is elementary.  In a \(K\)-uniform regular
hypergraph, estimating the conflict neighborhood of an edge by its \(K\)
vertex stars incurs pair-overlap terms of total possible scale

\[
 \binom K2\Delta_2,
\]

relative to the first-order scale \(KD\).  Their ratio is
\(\Theta(K\Delta_2/D)\).  The condition which makes the usual isolated
bite, degree martingale, and conflict-system estimates asymptotically
linear is therefore unavailable here.  Equation (4.6) does not prove that
a matching is impossible; it proves that low codegree cannot be its
explanation.

## 5. Product selection does not cover the first quota

Take the exactly regular quota orbit of Theorem 2.1 and independently
select every indexed column with probability \(\lambda/D\).  A fixed
typed depth-one target has degree \(D\), and hence

\[
 \Pr(T\text{ is unselected})
 =\left(1-{\lambda\over D}\right)^D
 =e^{-\lambda+o(1)}.                                     \tag{5.1}
\]

The expected load at every owner is \(\lambda\).  Thus the owner-scale
choice \(\lambda=1+o(1)\) leaves

\[
 (e^{-1}+o(1))N_1=\Theta(W)                              \tag{5.2}
\]

expected holes in each signed first target layer.  Deleting intersecting
selected columns can only increase the set of holes.  Therefore the
direct product experiment, and any alteration proof controlled only by
its expected singleton deficit, cannot reach \(o(W)\) holes.  The usual
symmetric local-lemma criterion also cannot start from (5.1), whose bad
event probability is bounded away from zero.

This is a method statement: rare strongly correlated outcomes are not
excluded by the expectation calculation.

## 6. Product residuals lose every long-route link

The failure persists even if the catalogue is enlarged from one orbit to
all unrestricted routes.

Let \(h_2(x)=-x\log x-(1-x)\log(1-x)\).  From (4.1) and the elementary
bound

\[
 h_2(x)\le x(1+\log(1/x))\qquad(0<x\le1/2),               \tag{6.1}
\]

splitting at \(q=C\sqrt m\) gives

\[
 \boxed{\sum_{q\le H}h_2(p_q)=O(\sqrt m)}                \tag{6.2}
\]

uniformly for \(H=o(m^{2/3})\).  Indeed the initial
\(O(\sqrt m)\) terms are bounded, and the tail is dominated after
rescaling by
\((1+x^2)e^{-c x^2}\).

### Theorem 6.1 (independent-residual link death)

Assume

\[
 H\ge a\sqrt m,qquad H=o(m^{2/3}),qquad L\ge2H,          \tag{6.3}
\]

where \(a>0\) is fixed.  Let \(\mathscr C\) be the catalogue of all
distinct cyclic \(H\)-geodesic Johnson routes of length \(L\), with every
signed depth carrying either \(\lfloor Lp_q\rfloor\) or
\(\lceil Lp_q\rceil\) accepted starts.  Internal rainbowness and every
other physical legality condition may be imposed; they only shrink the
catalogue.

Retain every owner and typed target independently with probability
\(\varepsilon=m^{-\alpha}\), where \(\alpha>0\) is fixed.  Conditional on
retaining a fixed owner \(X\), the expected number of columns through
\(X\) all of whose other resources survive is \(o(1)\).

#### Proof

A route through \(X\) is specified by choosing the position of \(X\) and
then at most \(L\) Johnson steps.  Every middle set has \(m^2\) Johnson
neighbors, so the number of underlying route words through \(X\) is at
most

\[
 L(m^2)^L.                                               \tag{6.4}
\]

For each signed depth the number of permitted accepted-start sets is at
most

\[
 \binom L{\lfloor Lp_q\rfloor}
 +\binom L{\lceil Lp_q\rceil}.                            \tag{6.5}
\]

The entropy bound for binomial coefficients, together with changing a
frequency by at most \(1/L\), gives

\[
 \log(6.5)\le Lh_2(p_q)+O(\log L).                        \tag{6.6}
\]

Using (6.2) for the two signs, the logarithm of the number \(D_X\) of
distinct columns through \(X\) is at most

\[
 \log D_X
 \le \log L+2L\log m+O(L\sqrt m+H\log L)
 =O(L\sqrt m).                                           \tag{6.7}
\]

For the last equality, use \(L\ge2H\) and the fact that
\(\log x/x\) decreases for \(x>e\):
\(H\log L/L\le\tfrac12\log(2H)=o(\sqrt m)\).

By (4.3) and (4.5), every column has at least

\[
 K_-\ge c_aL\sqrt m                                      \tag{6.8}
\]

distinct typed resources, for some \(c_a>0\).  Conditional on retaining
\(X\), a fixed incident column survives with probability at most
\(\varepsilon^{K_--1}\).  Therefore

\[
 \begin{aligned}
 \log\mathbb E[d_{\rm res}(X)\mid X\text{ retained}]
 &\le O(L\sqrt m)-(K_--1)\alpha\log m\\
 &\le -\Omega_a(L\sqrt m\log m),
 \end{aligned}                                           \tag{6.9}
\]

which tends to \(-\infty\). \(\square\)

Thus the residual cannot simultaneously resemble independent thinning
and regenerate a positive route degree at the polynomial densities needed
for owner leave \(o(W/H)\).  Indexed copies of one physical column do not
alter this conclusion: they are the same candidate and cannot be selected
together.

## 7. Exact implication boundary

The following statements are proved.

1. The full coordinate orbit of any internally rainbow cyclic route has
   an exact common-owner, all-depth fractional quota resolution after the
   forced density thinning \(p_q=N_q/W\).
2. Formula (3.1) computes every orbit pair codegree.
3. Every quota-balanced route catalogue has the intrinsic endpoint
   codegree (3.4), in particular \(2/(m+1)\) at depth one.
4. The growing-uniformity small-codegree parameter obeys (4.6), so it is
   not small on the Gaussian window.
5. Independent orbit selection at owner load one has a linear expected
   depth-one quota deficit.
6. Even the catalogue of all unrestricted long routes has no hereditary
   product-residual regeneration at any polynomial residual density.

The following statements are not proved.

1. Nonexistence of an \(H\)-delay quota-rainbow Hamilton cycle or
   2-factor.
2. A deterministic Hall cut against all unrestricted Johnson cycles.
3. A correlated absorption theorem preserving chronological route
   blocks.

The minimum surviving construction statement is therefore:

> Build one owner-disjoint family of cyclic \(H\)-geodesic routes whose
> radius counts are \(p_q\) at every depth, whose accepted lower and upper
> traces are globally injective up to \(o(W)\) omissions, and whose owner
> leave is \(o(W/H)\); then splice its route components without changing
> more than \(o(W)\) protected windows.

Such a theorem would evade every obstruction above because its residual
law would be highly correlated rather than product-like.  No such theorem
is established here.
