# Audit and reduction for integral rounding of the unified rail queues

**Date:** 2026-08-07  
**Files audited:**

* *MATH_THEOREM_BINARY_TOGGLE_VARIABLE_WEIGHT_QUEUE_AND_ROTOR_LIFT_20260807.md*;
* *MATH_THEOREM_UNIFIED_RAIL_QUEUE_FULL_FRACTIONAL_SHADOW_BRAID_20260807.md*;
* *MATH_THEOREM_PURE_RAIL_CAROUSEL_OWNER_HYPERGRAPH_REGULARITY_20260807.md*;
* *MATH_THEOREM_NONMAXIMAL_PURE_RAIL_LATTICE_BREAKERS_20260807.md*;
* *MATH_THEOREM_CAROUSEL_ADJACENT_TRANSPOSITION_COHERENT_BIRAIL_TRADE_20260807.md*; and
* *MATH_THEOREM_POSITIVE_TWO_SIZE_RAIL_UNIT_RESIDUE_ABSORBER_AND_SAFE_ORDER_GATE_20260807.md*.

**Verdict:** The owner-correlated fractional factor, the maximal pure-rail
owner degrees and pair-codegrees, the nonmaximal scalar/first-order lattice
breakers, and the positive two-size coordinate-residue macro are sound.
The authoritative unified rail removes the elementary closed-component
gcd after nonmaximal sizes are admitted.  It does not yet round named
owners and target flags.

There are two important scope corrections.

1. Adjacent transpositions give a signed multiset identity at every width,
   but not two distinct entering and departing **set values** at singleton
   and co-singleton widths.
2. The positive four-carousel macro realizes a unit difference only after
   projection to ground-coordinate incidence.  Its named owner and deck
   symmetric differences have size \(\Theta(k)\); it is not yet a robust
   absorber for an arbitrary named leave.

The exact new codegree calculation shows why owner-first sequential
rounding is preferable: owner-owner normalized codegree is
\(\Theta(k^{-2})\), while a contained owner/lower-target pair has normalized
codegree \(\Theta(k^{-1})\).

## 1. Corollary 3.3 really is owner-correlated

Let

\[
 R=\left\lceil\frac k2\right\rceil,\qquad
 W=\binom{k}{R},
\tag{1.1}
\]

and let a queue type \(\theta\) have endpoint count \(N_\theta\) and
mixture coefficient \(\lambda_\theta\).  Giving it component mass

\[
 \frac{W\lambda_\theta}{N_\theta}
\tag{1.2}
\]

gives endpoint, hence owner, mass \(W\lambda_\theta\).  Summing over types
gives total owner mass \(W\).  Uniform coordinate embedding distributes
this over the \(W\) named rank-\(R\) owners, so every owner has load one.

If the marked rank-\(s\) marginal per endpoint is

\[
 q_s=\frac{\binom{k}{s}-b_s}{W},
\tag{1.3}
\]

the same components carry total marked mass \(Wq_s\).  Symmetry distributes
it uniformly over the rank-\(s\) layer, giving

\[
 \frac{Wq_s}{\binom{k}{s}}
 =1-\frac{b_s}{\binom{k}{s}}.
\tag{1.4}
\]

Thus the owner and lower loads are genuinely correlated through one
component variable; they were not averaged in separate polytopes.
The ambient requirement

\[
 k\ge R+d+1
\tag{1.5}
\]

holds at the optimal deadline for all sufficiently large \(k\).
Corollary 3.3 is therefore correct.  Its displayed (3.3) has only a
typographical missing \(\quad\) before \(1\le s<R\).

The conclusion remains a designated-mark relaxation.  It does not say
that an arbitrary already-chosen owner factor admits the same conditional
distribution of lower decorations.

## 2. Unified owner geometry and maximal sizes

Put

\[
 q=d+1,\qquad c=R-q,\qquad M=k-c=k-R+q.
\tag{2.1}
\]

For every unified rail type, including variable-weight and mixed rotors,
the owner row has the same form

\[
 C\cup\{\text{\(q\) consecutive toggle labels}\},
\qquad |C|=c.
\tag{2.2}
\]

The type affects the lower decoration, not the owner geometry.  If
\(p=d-a+1\), the maximal clock has

\[
\begin{aligned}
 L_p
 &=1+\left\lfloor\frac{k-R+a}{p}\right\rfloor\\
 &=\left\lfloor\frac{M}{p}\right\rfloor,
\end{aligned}
\tag{2.3}
\]

because \(a=q-p\).  Hence its owner count is exactly

\[
 \boxed{N_p=p\left\lfloor\frac Mp\right\rfloor
       =M-(M\bmod p),\qquad1\le p\le q.}
\tag{2.4}
\]

The gcd of the maximal closed sizes is therefore

\[
\boxed{
 g_{\max}
 =\gcd\{N_p:1\le p\le q\}
 =\gcd\bigl(M,M\bmod2,\ldots,M\bmod q\bigr).
}
\tag{2.5}
\]

In particular \(g_{\max}=1\) whenever \(M\) is odd, but maximal clocks
alone do not give a uniform gcd-one theorem for all parameters.

## 3. Audit of the pure-owner hypergraph

For a maximal pure rail, a rooted oriented copy consists of a \(c\)-core
and a cyclic ordering of its \(M\)-element complement.  Fixing an owner
\(T\), choosing its core, the start of its \(q\)-block, the block order,
and the exterior order gives

\[
 \boxed{
 D=\binom Rc\,M\,q!\,(M-q)!.
 }
\tag{3.1}
\]

For two owners with

\[
 |T\cap T'|=c+s,
\qquad0\le s\le q-1,
\tag{3.2}
\]

the audited codegrees are

\[
\lambda_0
=M(M-2q+1)(q!)^2(M-2q)!,
\tag{3.3}
\]

and

\[
\lambda_s
=\binom{c+s}{c}
  2M\,s!\,((q-s)!)^2(M-2q+s)!
\quad(1\le s<q).
\tag{3.4}
\]

The factors have the following exact meanings: choose a common core,
choose the first cyclic start, choose either two overlap orientations or
one of \(M-2q+1\) disjoint starts, and biject the labelled regions.
Thus Theorems 2.1 and 3.1 of the regularity note pass.

Under its displayed monotonicity hypotheses the maximum is
\(s=q-1\), and direct division gives

\[
 \boxed{
 \frac{\Delta_2}{D}
 =\frac{2}{R(M-q)}
 =\frac{2}{R(k-R)}.
 }
\tag{3.5}
\]

The hypotheses hold in the central triangular regime, so the sharp
\(\Theta(k^{-2})\) owner-only codegree claim also passes.

## 4. Exact all-width and owner-target codegrees

The same count has a useful nonmaximal and multi-resource form.
Let \(N\le M\), and parameterize a size-\(N\) pure rail by a \(c\)-core
and an ordered injection of \(\mathbb Z_N\) into the remaining
coordinates.  At width \(w<N/2\), a fixed rank-\((c+w)\) value has degree

\[
 \boxed{
 D_w(N)
 =\binom{c+w}{c}\,N\,w!\,(M-w)_{N-w},
 }
\tag{4.1}
\]

where \((x)_j\) is the falling factorial.

For two distinct width-\(w\) values intersecting in rank \(c+s\),
\(0\le s<w\), their codegree is

\[
\boxed{
\begin{aligned}
 \lambda^{(w)}_0(N)
 &=N(N-2w+1)(w!)^2(M-2w)_{N-2w},\\
 \lambda^{(w)}_s(N)
 &=\binom{c+s}{c}\,
   2N\,s!\,((w-s)!)^2
   (M-2w+s)_{N-2w+s}
   \quad(1\le s<w).
\end{aligned}}
\tag{4.2}
\]

In particular, the adjacent-value ratio is independent of \(N\):

\[
 \boxed{
 \frac{\lambda^{(w)}_{w-1}(N)}{D_w(N)}
 =\frac{2}{(c+w)(M-w)}.
 }
\tag{4.3}
\]

At \(w=q\), this is (3.5).

More generally, take widths \(u\ge v\), with \(u+v\le N\), and values
\(X,Y\) whose toggle residues intersect in \(s\) labels.  Their exact
codegree is

\[
\boxed{
 \lambda_{u,v,s}(N)
 =\binom{c+s}{c}\,
  N\,\eta_{u,v,s}\,
  s!(u-s)!(v-s)!
  (M-u-v+s)_{N-u-v+s},
 }
\tag{4.4}
\]

where

\[
\eta_{u,v,s}=
\begin{cases}
N-u-v+1,&s=0,\\
2,&1\le s<\min(u,v),\\
|u-v|+1,&s=\min(u,v),\ u\ne v.
\end{cases}
\tag{4.5}
\]

These are respectively the numbers of disjoint starts, partial-overlap
orientations, and placements of the shorter interval inside the longer.

The most important case is containment \(Y\subset X\), \(u>v\).  Dividing
(4.4) by the two degrees gives

\[
\boxed{
\frac{\lambda_{u,v,v}(N)}{D_u(N)}
=\frac{u-v+1}{\binom{c+u}{u-v}},
\qquad
\frac{\lambda_{u,v,v}(N)}{D_v(N)}
=\frac{u-v+1}{\binom{M-v}{u-v}}.
}
\tag{4.6}
\]

For an owner and its immediate lower rail value,
\(u=q,v=q-1\), this becomes

\[
\boxed{
\frac{\lambda}{D_{\rm owner}}=\frac2R,
\qquad
\frac{\lambda}{D_{\rm lower}}=\frac2{k-R+1}.
}
\tag{4.7}
\]

Thus the deterministic nesting raises normalized owner-target codegree
from \(\Theta(k^{-2})\) to \(\Theta(k^{-1})\).  The formulas apply
directly to pure-rail lower decks, to the immediate palettes, and to every
unified interval row having the common core \(C\).  Variable-weight
suffixes before all phases are active carry an additional partition
decoration and require a second-stage fibre calculation.

#### Proof of (4.1)--(4.6)

For (4.1), choose the \(c\)-core inside the fixed value, choose the cyclic
start, order its \(w\) labels, and inject the remaining \(N-w\) toggle
positions outside the value.

For a pair, choose the common core.  The two residue intervals have
four labelled regions: intersection, first-only, second-only, and
exterior.  Their sizes give the factorials in (4.4); (4.5) counts their
relative cyclic positions.  Equal widths give (4.2).  In the containment
case, cancelling (4.4) against (4.1) yields (4.6). \(\square\)

This calculation rules out treating the complete owner-plus-flag packet
as if it inherited the owner-only \(\Theta(k^{-2})\) codegree.  A
sequential owner matching followed by a decoration flow is the
proof-compatible architecture.

## 5. Closed nonmaximal rails remove the elementary lattices

A pure rail is legal at every size

\[
 2(q+1)\le N\le M.
\tag{5.1}
\]

Its owners are distinct, its immediate palettes are simple, every proper
interval deck is simple, and its toggle owner run and gap are \(q\) and
\(N-q\).  These assertions follow directly from the cyclic interval
decoder; (5.1) gives the required two-sided residence.

For sufficiently large parameters, \(M-1\) and \(M\) are both available.
Their gcd is one, so the two-generator Frobenius theorem represents every
integer above

\[
 M(M-1)-M-(M-1)
\tag{5.2}
\]

as a nonnegative combination of legal closed sizes.  Since
\(W=\binom{k}{R}\) is exponential and \(M=\Theta(k)\), the owner count
\(W\) is representable.  The scalar closed-component obstruction is
therefore gone once nonmaximal pure rails are admitted.

The first-order role-swap argument also passes.  In a size-\(N\) rail, a
core, toggle, or unused coordinate has owner multiplicity \(N,q,0\).
Swapping a core and unused coordinate gives

\[
 N(\mathbf e_x-\mathbf e_y).
\tag{5.3}
\]

Doing this at the consecutive nonmaximal sizes \(M-1,M-2\), then applying
Bézout, generates every unit difference.  Hence the signed
ground-coordinate incidence lattice contains

\[
 \{z\in\mathbb Z^k:\sum_i z_i=0\}.
\tag{5.4}
\]

This is a first-order projection, not the full named-owner incidence
lattice.

### Marked-target lattice splitting

Under the designated-mark semantics of the fractional theorem, there is
also no named-target congruence.  If a legal component contains a physical
occurrence with value \(S\), compare the same component with that
occurrence marked and unmarked.  Their owner vectors are identical and
their marked-target vectors differ by exactly

\[
 \mathbf e_S.
\tag{5.5}
\]

Every strict-lower rank occurs with positive mass in the fractional
catalogue, and symmetry maps one occurrence to every named target of that
rank.  Therefore all named-target unit vectors lie in the signed
configuration lattice.

Equations (5.2)--(5.5) remove scalar, first-order coordinate, and
designated-target divisibility separators.  They do not give a positive
packing: the marked occurrence \(S\) must still be present in the
eventually selected owner component.

## 6. Open paths also kill scalar divisibility, at a boundary price

Let a legal pure rail of size \(N\) be unrolled.  For any
\(1\le s\le N\), a source segment of length

\[
 s+q-1=s+d
\tag{6.1}
\]

contains exactly \(s\) consecutive owner windows.  They are distinct and
form a Johnson path; all of their proper lower suffixes are literal.
Thus open rail paths realize every owner count \(s\), and their scalar gcd
is automatically one.

This does not make open paths free.  They export two boundary states,
lose the closing owner/palette edge, and use a \(q-1\) source collar.
Using many independent paths would create growing additive overhead unless
their collars are shared during fusion.  Nonmaximal closed rails already
remove scalar divisibility, so open paths are needed only for topology or
boundary-conditioned absorption, not for the elementary gcd.

## 7. Audit of adjacent-transposition trades

The correct all-width statement is the signed multiset identity

\[
 \chi_{\mathcal D_\ell(\sigma)}
-\chi_{\mathcal D_\ell(\sigma')}
=\mathbf e_{L+x}+\mathbf e_{y+R}
 -\mathbf e_{L+y}-\mathbf e_{x+R},
\tag{7.1}
\]

with the common core adjoined.  It is valid for every proper width.

The claim that all four displayed set values are distinct under
\(N\ge2\ell+2\) needs the extra hypothesis \(\ell\ge2\).  At
\(\ell=1\),

\[
 L=R=\varnothing,\qquad
 L+x=x+R,\qquad L+y=y+R,
\tag{7.2}
\]

so both sides cancel and the singleton deck is unchanged as a set family.
The co-singleton deck \(\ell=N-1\) is likewise order-independent.

For \(2\le\ell\le N/2\), \(N\ge2\ell\) already makes the four values
distinct.  Hence the owner and immediate-palette widths

\[
 q-1,\quad q,\quad q+1
\tag{7.3}
\]

have genuine two-in/two-out ports when \(d\ge2\) and
\(N\ge2(q+1)\).  The singleton and co-singleton rows have only the signed
multiset interpretation.

Consequently adjacent transpositions are valid owner alternating-path
moves, but the slogan “two witness ports at every width” is false
set-wise.  Moreover, every order trade preserves the coordinate-incidence
vector

\[
 N\mathbf1_C+\ell\mathbf1_T.
\tag{7.4}
\]

It can route named holes only inside that incidence fibre; it cannot by
itself repair a coordinate residue.

## 8. Audit of the positive two-size unit macro

Let \(N_1=M-1,N_2=M-2\), and use the four core/unused assignments in the
positive absorber note.  Each alternative consists of:

* one component whose sets contain \(x\) and omit \(y\); and
* one component whose sets contain \(y\) and omit \(x\).

Thus the two decks inside either alternative are disjoint at every common
proper width.  The coordinate-incidence formula

\[
 \omega_{N,\ell}=N\mathbf1_C+\ell\mathbf1_T
\tag{8.1}
\]

gives

\[
\begin{aligned}
\omega(Q_1^+)-\omega(Q_1^-)
 &=N_1(\mathbf e_x-\mathbf e_y),\\
\omega(Q_2^+)-\omega(Q_2^-)
 &=-N_2(\mathbf e_x-\mathbf e_y).
\end{aligned}
\tag{8.2}
\]

Since \(N_1-N_2=1\), the positive equal-size alternatives differ by
\(\mathbf e_x-\mathbf e_y\) at every common width.  The four-carousel
trade and its all-common-width incidence claim pass.

The common maximal background argument also passes after adding the
necessary hypothesis

\[
 c\ge2.
\tag{8.3}
\]

Indeed its core must contain both \(x\) and \(y\).  Background owners then
contain both signature coordinates, while absorber owners contain exactly
one.  For a fixed background core, a random cyclic order contains a fixed
\(q\)-set as a block with probability

\[
 \frac{M}{\binom Mq}.
\tag{8.4}
\]

After \(b\) background carousels, at most \(bM\) blocks are forbidden, so
the union bound

\[
 bM^2<\binom Mq
\tag{8.5}
\]

is a valid sufficient condition for another disjoint order.

The all-width avoidance criterion

\[
 \sum_{\ell\in\mathcal W}
 \frac{N|\mathcal F_\ell(C,T)|}{\binom N\ell}<1
\tag{8.6}
\]

also passes: it is the union bound over forbidden cyclic blocks.

What the macro does **not** supply is a unit trade in named resources.
At a given width, the two alternatives each contain \(2M-3\) set values,
and their named deck difference is generally of order \(M\).  Only its
projection to the \(k\)-coordinate incidence vector is the unit
difference (8.2).  Thus it satisfies the elementary divisibility/local
lattice input of an iterative-design theorem, but not the robust
extendability input.

The adjacent-order safe graph may also be disconnected after protected
tickets are forbidden.  Condition (8.6) proves the existence of at least
one safe order; it gives neither many extensions from every partial root
nor paths between safe orders.  This is exactly where a direct invocation
of a Designs-II-style absorption theorem would still need a new proof.

## 9. Exact partial flow result

Ignoring flag compatibility, each lower rank separately has no matching
obstruction.  Let \(G_s\) be the inclusion graph between rank-\(s\)
targets and rank-\(R\) owners.  It is biregular with degrees

\[
 d_L=\binom{k-s}{R-s},
\qquad
 d_R=\binom Rs,
\tag{9.1}
\]

and

\[
 \frac{d_L}{d_R}
=\frac{\binom{k}{R}}{\binom{k}{s}}\ge1.
\tag{9.2}
\]

For every family \(\mathcal A\) of rank-\(s\) targets,

\[
 d_L|\mathcal A|
\le d_R|N(\mathcal A)|,
\tag{9.3}
\]

so Hall gives a matching of the entire rank-\(s\) layer into distinct
owners.  The same holds after deleting any Ferrers-covered targets.

Across all strict-lower ranks, the same edge count gives

\[
 |\mathcal A|
\le
 \frac{\Lambda}{W}|N(\mathcal A)|
 <(d+1)|N(\mathcal A)|
\tag{9.4}
\]

for sufficiently large parameters.  Hence all lower targets admit a
simultaneous owner assignment with capacity \(d+1\).

The literal queue has only \(d\) proper suffix slots per owner.  After the
Ferrers boundary removes its \(h\) targets, total demand is at most \(dW\),
but (9.4) does not automatically improve to the required capacity-\(d\)
Hall inequality for every subfamily.  Even such a \(d\)-capacity matching
would still ignore the stronger condition that the targets assigned to
one endpoint form one nested flag allowed by a common queue decoration.

Thus ordinary per-rank Hall is closed; the surviving lower problem is a
layered flag-flow problem.

## 10. Weakest remaining theorem

All currently proved pieces point to the following sequential statement.

> **Conditioned carousel flag-absorber theorem.**  There is a
> bounded-defect matching of variable-size rail carousels on the owner
> layer, with a sparse nonmaximal absorber, such that the selected frames
> admit legal variable-weight decorations whose marked suffix flags cover
> every Ferrers-residual named lower target once.  The absorber states and
> their safe-order paths remain extendable after reserving the immediate,
> upper, and compiler tickets.

This theorem has three logically distinct parts:

1. an owner matching/absorber beyond the owner-only fractional and
   codegree calculation;
2. a conditioned capacity-\(d\) **flag** flow, not independent rank
   matchings; and
3. robust safe-order expansion for named resources, not merely existence
   under the one-order union bound.

No scalar gcd, first-order coordinate congruence, designated-target
congruence, separate-rank Hall inequality, or local owner codegree remains
as an obstruction.  The unresolved content is positive occurrence-level
extendability and fusion.
