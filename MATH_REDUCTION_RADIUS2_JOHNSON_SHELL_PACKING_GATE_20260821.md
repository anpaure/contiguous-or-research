# Radius-two Walecki slices are an asymptotically perfect Johnson-code gate

**Status (2026-08-21).** The combinatorial reduction, all enumerations, and
the hypergraph parameters below are proved.  Packing the physical rank-two
Walecki slices suggested by the partition route is exactly the problem of
constructing an asymptotically perfect radius-two code in `J(2b,b)`:

\[
 A(2b,10,b)\sim {{2b\choose b}\over {b\choose2}^{2}}.        \tag{0.1}
\]

The shell hypergraph has a perfect fractional matching, but no integral
rounding theorem used in this project proves (0.1).  Its maximum normalized
codegree tends to zero, yet its uniformity grows as `Theta(b^4)`; the
fixed-uniformity Pippenger theorem and the quantitative pseudorandom matching
theorems checked below do not apply.  The recent near-optimal constant-weight
code theorems found in the literature keep the weight fixed, whereas here the
weight is `b=n/2`.

Thus this is a precise possible bypass, but presently an open growing-design
input rather than a proof of `o(W_b)` holes.  Nothing below proves that (0.1)
is impossible.

## 1. Exact shell/code equivalence

Let

\[
 \Omega_b={ [2b]\choose b},\qquad W_b=|\Omega_b|,
 \qquad d_J(X,Y)=b-|X\cap Y|.                               \tag{1.1}
\]

For a center `C in Omega_b`, define its distance-two shell

\[
 \Sigma_2(C)=\{X\in\Omega_b:d_J(X,C)=2\}.                   \tag{1.2}
\]

Writing `A=[2b] setminus C` and `B=C`, this is exactly the
partition slice

\[
 \Sigma_2(C)=\{X:|X\cap A|=2,\ |X\cap B|=b-2\},             \tag{1.3}
\]

so

\[
 S_b:=|\Sigma_2(C)|={b\choose2}^{2}.                        \tag{1.4}
\]

### Proposition 1.1

For `b>=5` and distinct centers `C,D`,

\[
 \Sigma_2(C)\cap\Sigma_2(D)=\varnothing
 \quad\Longleftrightarrow\quad d_J(C,D)\ge5.               \tag{1.5}
\]

#### Proof

If the shells intersect, the triangle inequality gives
`d_J(C,D)<=4`.  Conversely put `d=d_J(C,D)<=4` and partition
the ground set into

\[
 I=C\cap D,\quad U=C\setminus D,\quad V=D\setminus C,
 \quad O=[2b]\setminus(C\cup D),                            \tag{1.6}
\]

of sizes `b-d,d,d,b-d`.  A set `X` at distance two from both
centers may be chosen with

\[
 |X\cap U|=|X\cap V|=t,
 \quad |X\cap I|=b-2-t,
 \quad |X\cap O|=2-t,                                      \tag{1.7}
\]

where `max(0,d-2)<=t<=min(2,d)`.  Such a `t` exists for every
`d<=4`, and all four requested binomial choices are feasible for
`b>=5`.  This constructs an intersection point and proves (1.5).

Consequently a family of pairwise disjoint Walecki shells is exactly a
constant-weight binary code of length `2b`, weight `b`, and minimum Hamming
distance at least `10` (equivalently minimum Johnson distance at least `5`).
If `A(n,d,w)` denotes the largest size of such a code, its maximum shell
coverage is

\[
 {A(2b,10,b)S_b\over W_b}.                                  \tag{1.8}
\]

Therefore asymptotically full shell coverage is exactly (0.1).

## 2. Equivalence with asymptotically perfect radius-two balls

The closed Johnson ball of radius two has size

\[
 V_b=1+b^2+{b\choose2}^{2}=S_b\left(1+O(b^{-2})\right).      \tag{2.1}
\]

Centers of minimum Johnson distance five have disjoint radius-two balls, so
the sphere-packing bound is

\[
 A(2b,10,b)\le {W_b\over V_b}.                              \tag{2.2}
\]

Since `V_b/S_b->1`, (0.1) is equivalent to

\[
 A(2b,10,b)V_b=(1-o(1))W_b.                                 \tag{2.3}
\]

Thus the proposed slice packing does not merely ask for a generic large
constant-weight code.  It asks for an asymptotically perfect two-error code
meeting the Johnson sphere-packing bound to relative error `o(1)`.

## 3. Exact shell-hypergraph parameters

Let `H_b` be the hypergraph with vertex set `Omega_b` and one edge
`Sigma_2(C)` for every center `C`.  By symmetry it is `S_b`-uniform and
`S_b`-regular.  Giving every edge weight `1/S_b` is therefore a perfect
fractional matching of total value `W_b/S_b`.  Equation (0.1) is exactly the
assertion that this fractional matching has an integral matching of
asymptotically equal value.

For two vertices `X,Y` at Johnson distance `d`, their codegree is

\[
 \lambda_d=
 \sum_{t=0}^{2}
 {b-d\choose 2+t-d}{d\choose t}^{2}{b-d\choose 2-t},        \tag{3.1}
\]

where an out-of-range binomial coefficient is zero.  This follows from the
four-part decomposition (1.6), now with the center playing the role of `X`
in (1.7).  In particular,

\[
 \lambda_1=(b-1)^2(b-2),                                   \tag{3.2}
\]
\[
 \lambda_2=(b-2)(5b-11),\qquad
 \lambda_3=18(b-3),\qquad \lambda_4=36,                    \tag{3.3}
\]

and `lambda_d=0` for `d>=5`.  For `b>=5`, (3.2) is the
maximum codegree.  Hence

\[
 {\Delta_2(H_b)\over\Delta(H_b)}
 ={4(b-2)\over b^2}\sim {4\over b},                        \tag{3.4}
\]

but the rank is

\[
 r(H_b)=S_b\sim {b^4\over4},\qquad
 r(H_b){\Delta_2(H_b)\over\Delta(H_b)}
 =\Theta(b^3).                                              \tag{3.5}
\]

The ratio in (3.4) by itself cannot justify a nibble when the rank grows.
Indeed, projective-plane line hypergraphs have growing rank, are regular and
linear, and satisfy `Delta_2/Delta->0`, while every two edges intersect and
their matching number is one.  A rank-free Pippenger inference would
therefore be false.

## 4. Why the checked black boxes do not close the gate

The classical Pippenger--Frankl--Rodl almost-perfect-matching theorem fixes
the uniformity before sending the degree to infinity.  That quantifier does
not cover `r(H_b)=Theta(b^4)`.

The quantitative pseudorandom-matching theorem of Ehard--Glock--Joos
(`arXiv:1907.09946`, Theorem 1.2) also does not apply along this sequence.
In its notation one may take at best a constant `delta<=1/4` from
`Delta^c=Theta(Delta^(3/4))`, while

\[
 \varepsilon={\delta\over50r^2}=O(b^{-8}).                  \tag{4.1}
\]

Its hypothesis

\[
 e(H_b)\le \exp(\Delta^{\varepsilon^2})                    \tag{4.2}
\]

then fails: `e(H_b)=W_b=exp(Theta(b))`, whereas the right side of
(4.2) stays bounded.  The dependence of the degree threshold on the growing
rank is another independent quantifier issue.

Recent asymptotically optimal constant-weight-code results located during
this audit do not have the required parameter regime:

* Liu--Shangguan, `arXiv:2401.00733`, keep the alphabet, weight, and odd
  distance fixed as the length tends to infinity;
* Bennett, `arXiv:2411.16028`, likewise treats fixed weight when completing
  the even-distance case.

Here the weight is `b`, exactly half the length.  Those results therefore do
not imply (0.1).

The exact-perfect-code literature is also not an asymptotic substitute.
Silberstein--Etzion, `arXiv:1004.5195`, gives strong necessary conditions for
perfect codes in Johnson graphs; the related thesis `arXiv:1004.4882`
excludes exact two-perfect codes in `J(2w,w)` through an enormous finite
range.  Exact nonexistence at finite parameters neither proves nor disproves
the relative-error statement (2.3).

## 5. Consequence for the physical program

For odd `b`, the rank-two local factors themselves are available from the
Walecki Hamilton decomposition of `K_b`.  If (0.1) were proved, one could
place the exact rank-two product construction on the corresponding
partitions and obtain `(1-o(1))W_b` pairwise disjoint middle targets; the
number of slices is only `Theta(W_b/b^4)`.  In particular, the already
available `O(b)` connector per slice would cost only `O(W_b/b^3)=o(W_b)`.

The unresolved point is not the rank-two factor or scalar counting.  It is
the integral packing (0.1).  Until a construction or a growing-rank matching
theorem specialized to the Johnson shell hypergraph is supplied, this route
must remain conditional.
