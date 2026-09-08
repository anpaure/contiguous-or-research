# Exact eligibility for translated partner shores in the ternary eight-cube

2026-09-08. Root's lemma, independently audited and written by
cover-selectors. Pure mathematics; no computation.

Let E=F_2^3 label the eight coordinates, and let tau_v translate
coordinate labels by a nonzero v in E. For an affine hyperplane H
not parallel to v, a full geodesic C in {0,1,2}^H has one member at
each rank 0,...,8. Write C^circ for its members of ranks 1,...,7.
Consider the actual axis-support rectangle

    C^circ x tau_v(C^circ),

with shores H and H+v. No individual complement-translation symmetry
is required of C.

## 1. Exact statement

A target x in {0,1,2}^E belongs to at least one such cropped rectangle
if and only if it has at least two nonzero coordinates and at least
two coordinates whose value is less than two.

Consequently this family covers exactly the cube outside its 34
extremal targets: the 17 targets with at most one nonzero coordinate
and the 17 targets with at most one coordinate below two. These two
sets are disjoint.

If the endpoints of C are retained, the corresponding full rectangles
cover every target in the cube.

## 2. A matching with three useful properties

The four pairs {p,p+v} form the translation-v perfect matching on E.
For a target satisfying the two conditions above, choose v so that
this matching contains:

* a pair P whose two values are positive;
* a pair Q whose two values are below two;
* a pair T whose two values are equal.

The same pair may serve several roles. Existence follows by the number
of coordinates with value one.

If there are at least two ones, take v to be the difference of two
such coordinates. Their pair serves all three roles.

Suppose there is exactly one one. Both the zero class and the two
class are nonempty, and their sizes sum to seven. If the smaller class
has at least two members, choose v between two members of that class.
This gives T and one of P,Q. The larger class together with the one
has at least five members. Some matching pair lies wholly within that
five-or-more-element set, giving the other property. If the smaller
class has one member, pair it with the one. That pair gives Q when the
minority value is zero, or P when it is two. All six remaining points
have the majority value, so their three matching pairs provide T and
the other property.

Finally suppose there are no ones. There are at least two zeros and
at least two twos. Choose v between two members of the smaller class,
which has size at most four. This provides T and one of P,Q. If the
other class has more than four members, it contains a matching pair.
In the remaining 4+4 case, a matching has equally many zero-zero and
two-two pairs: subtract the two equations counting the four members
of each class. Thus the already selected same-class pair forces a
pair in the other class. This provides the missing property.

## 3. Affine interpolation chooses the smaller endpoints

Identify the four matching pairs with E/<v>, an affine plane over F_2.
Fix a linear section sigma of the quotient. Every affine transversal
of the matching has the form

    H = { sigma(q) + epsilon(q)v : q in E/<v> },

where epsilon is an affine Boolean function on the quotient. Such H
is an affine hyperplane, and H and H+v partition E.

For each unequal-valued pair, prescribe epsilon(q) so that H contains
its smaller-valued endpoint. Property T means there are at most three
prescriptions. Any three distinct points of F_2^2 are affinely
independent, so every assignment on at most three points extends to
an affine Boolean function. Choose such an extension.

The two restrictions, written on the common coordinate set H, are

    a_h = x_h,       b_h = x_(h+v).

They satisfy a<=b coordinatewise. Property P gives a positive
coordinate of a; property Q gives a coordinate of b below two.
Therefore

    1 <= rank(a) <= rank(b) <= 7.

There is a full coordinate-increment geodesic from zero through a
and b to the all-two vector: increment coordinates to a, then to b,
then to the top. If a=b it is visited only once. Both a and b survive
cropping to ranks 1,...,7, and their product is precisely x. This
proves sufficiency.

Necessity is immediate: each cropped shore member has a positive
coordinate and a coordinate below two. The two disjoint shores
therefore give at least two of each globally.

## 4. Full rectangles and precise scope

For an arbitrary target, two coordinate values agree by pigeonhole.
Choose v between their positions. This supplies T, hence at most
three forced orientations. The same affine interpolation gives a<=b,
and a full geodesic contains both, including possible endpoints.
Thus the full coupled family covers every target.

An affine H need not contain zero. Translating coordinate labels
moves it to a linear hyperplane and preserves the coupling vector v.
Thus these are members of the translation-developed families used in
the existing catalogues; no new kind of shore is being introduced.

This theorem concerns target eligibility in the full family of
translated partner geodesics. It proves neither a small simultaneous
cover nor compatibility with exact rank-seven and rank-nine budgets.
In particular, it does not ensure that the constructed row's
complement-closed orbit bundle survives the internal critical-collision
filter in Q3_D8_TRANSLATION_COMPLEMENT_CLOSURE_BOUNDED_ATTEMPT_20260908.md.
