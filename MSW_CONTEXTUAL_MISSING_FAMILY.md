# A Catalan hereditary family of genuine MSW shadow holes

## 1. Outcome

The uniform target from `MSW_SECOND_UPPER_OBSTRUCTION.md` admits a genuine
Catalan context extension.

Put

\[
                         B=11101101.                 \tag{1.1}
\]

For every `m>=4` and every Dyck word `V` of semilength `m-4`, the core mask
whose incidence word is

\[
                         T(V)=B\,V                   \tag{1.2}

has rank `m+2` and is absent from the second-upper MSW map

\[
 \Gamma(x_i)=y_{i-1}\cup y_i,qquad1\le i<m.         \tag{1.3}
\]

Consequently the odd MSW wreath factor has at least

\[
                         \operatorname{Cat}_{m-4}    \tag{1.4}

explicit missing lower depth-one targets (and the same number of
complementary upper targets).

This family is important for the critical ECO programme because it is
*hereditary*, not exceptional.  Its dimension-to-dimension growth ratio is

\[
 {C_{m-3}\over C_{m-4}}
   =4-{6\over m-2}
   <4-{6\over m+2}
   ={C_{m+1}\over C_m}.                              \tag{1.5}

Thus this exact Catalan family can be charged to itself within the critical
Catalan coefficient with no additive residual.  It is the first rigorous
nontrivial example of the kind of targetwise hereditary charge sought in
`CRITICAL_CATALAN_LIFT.md`.

## 2. A suffix-locality lemma for the MSW maps

Regard a balanced word as a path starting at height zero.  Let `P` be any
balanced word and let `V` be Dyck.  Suppose the coordinate selected by the
MSW map `g` on `P` lies in `P`.  Then

\[
                         g(PV)=g(P)V.                \tag{2.1}

If the subsequent coordinate selected by `h` also lies in `P`, then

\[
                         f(PV)=f(P)V.                \tag{2.2}

### Proof

The statistic `d_0` used by `g` counts down-steps starting at height zero.
The Dyck suffix `V` has none, so `d_0(PV)=d_0(P)`.  Every candidate in `P`
precedes every candidate in `V`; hence a `g`-selection already made in `P`
is unchanged, proving (2.1).

After `g` flips a down-step to an up-step, the path height at the beginning
of `V` is two.  All up-steps of `V` therefore start at height at least two.
They cannot enter the list of height-zero/one candidates used by `h`.
Thus an `h`-selection in `P` is unchanged as well, proving (2.2).  \(\square\)

Since `f` is a bijection between consecutive Chung--Feller flaw classes,
(2.2) also preserves the unique predecessor: if `f(P'V)=PV`, then the
predecessor of `PV` is `P'V`.

## 3. The inserted coordinate cannot lie in the suffix

Assume for contradiction that (1.2) equals `Gamma(x_i)`.  By the exact
formula from `MSW_SECOND_UPPER_OBSTRUCTION.md`, there are two up-step
positions `a,b` of `T(V)` such that

\[
 x_i=T(V)\setminus\{a,b\},                           \tag{3.1}

where `a` is the coordinate inserted by `g(x_i)` and `b` is the coordinate
deleted on the preceding Chung--Feller step.

Let `H_T(r)` be the height of `T(V)` immediately before coordinate `r`, and
order `a,b` by their positions when needed.  At coordinate `a`, the word
`x_i` has a down-step which `g` selects, so its starting height is zero or
one:

\[
 H_T(a)-2\mathbf1_{b<a}\in\{0,1\}.                  \tag{3.2}

The prefix `B` ends at height four, and the Dyck suffix never goes below
that height.  Therefore (3.2) rules out `a` in `V`.  If `b` lies in `V`,
then `a<b`, and inspection of the six up-steps of `B` shows that only
`a=1` or `a=2` can satisfy (3.2).

* If `a=1`, then `x_i` begins with a down-step from height zero.  Hence
  `d_0(x_i)>=1`, while coordinate `1` is the first candidate seen by `g`.
  The rule selects candidate number `d_0+1>=2`, not coordinate `1`.

* If `a=2`, coordinate `2` is again the first candidate.  If the suffix
  obtained from `V` by turning position `b` down ever goes below the axis,
  then `d_0(x_i)>0`, so `g` does not select the first candidate.  If it never
  goes below the axis, then the whole balanced word `x_i` is Dyck and lies
  in flaw class zero.  But (1.3) uses only internal states `i>=1`.

Both alternatives are impossible.  Thus

\[
                         a,b\in[8].                  \tag{3.3}

## 4. Reduction to the eight-coordinate obstruction

By (3.3), write

\[
                         x_i=P,V,                   \tag{4.1}

where `P` is the balanced eight-letter word obtained from `B` by turning
the two positions `a,b` down.  The selected `g`-coordinate is in `P`.
After that flip the suffix begins at height two, so the selected
`h`-coordinate is also in `P`.  Lemma 2 and predecessor uniqueness show
that the two upper states adjacent to `x_i` have the form

\[
                         y_{i-1}=Y_-V,qquad
                         y_i=Y_+V.                   \tag{4.2}

Consequently

\[
                  \Gamma(x_i)=(Y_-\cup Y_+)V.        \tag{4.3}

Equation (4.3) says that `B` itself lies in the image of the eight-coordinate
second-upper map.  But `B=T_4` is exactly the base obstruction proved in
`MSW_SECOND_UPPER_OBSTRUCTION.md`.  This contradiction proves (1.2).

For the odd wreath, a core rank-`m+2` target `T` corresponds by
complementation to the lower target

\[
             \{\infty\}\cup([2m]\setminus T),       \tag{4.4}

of rank `m-1`.  Formula (4.4) is injective, establishing (1.4) and its upper
dual.  \(\square\)

## 5. Exact hereditary charge

Deleting the rightmost peak of a nonempty Dyck suffix gives its unique ECO
parent.  Hence the family

\[
             \{BV:V\in\mathcal D_{m-4}\}            \tag{5.1}

maps targetwise into the corresponding family one dimension lower.  Every
member is a genuine hole on both sides, and the total child-to-parent ratio
is the first quantity in (1.5).  Since it is strictly smaller than the
critical allowance, this entire explicit obstruction contributes zero to
the exceptional term `B_(m,H)`.

The lesson is encouraging but limited: the canonical MSW factor has many
more depth-one holes than (5.1).  The unresolved theorem is to decompose all
but `o(C_m)` of them into hereditary context families, or equivalently to
prove the capacitated deletion expansion stated in
`MSW_ECO_TARGET_PROJECTION.md`.
