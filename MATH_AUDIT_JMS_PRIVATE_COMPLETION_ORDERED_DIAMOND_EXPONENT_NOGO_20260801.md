# Private completion copies do not evade the JMS exponent obstruction

Date: 2026-08-01  
Status: exact applicability audit of the proposed ordered Boolean-diamond
factor proof.  The Joos--Mubayi--Smith theorem does not apply.  This does not
disprove existence of an exact ordered four-transversal; it invalidates this
particular black-box proof.

Primary source: F. Joos, D. Mubayi, Z. Smith,
*Conflict-free Hypergraph Matchings and Coverings*, arXiv:2407.18144v2,
Theorem 3.1 and conditions (S2), (H1)--(H4).

## 0. Verdict

Let

\[
 \mathcal L={ [2m]\choose m-1},\quad
 \mathcal U={ [2m]\choose m+1},\quad
 \mathcal M={ [2m]\choose m},
\]

and let one ordered diamond be

\[
 e(L;a,b)=(L,L+a+b,L+a,L+b).                                  \tag{0.1}
\]

The proposed first-stage four-graph `H_1` has degree

\[
                    D=m(m+1)                                   \tag{0.2}
\]

at every `L` and `U`, and degree `m^2` at each tail/head copy of a
middle set.  Giving every ordered diamond three private completion vertices
does make the second-stage degree at every `L` equal to `D` and every
private-vertex degree one.

That modification does **not** alter either the size condition (S2) or the
codegree condition (H2) on `H_1`.  Those two hypotheses require incompatible
values of the same theorem parameter `epsilon`:

\[
                  \epsilon\ge2^{-1/3}-o(1)                      \tag{0.3}
\]

from (S2), but

\[
                  \epsilon\le\tfrac12+o(1)                     \tag{0.4}
\]

from (H2).  Hence Theorem 3.1 cannot certify the proposed exact
four-resource selection.

The statement “all unavoidability sums are `O(1)`, so any sufficiently
small `epsilon<1/4` works” is also in the wrong scale.  The theorem requires
specific negative powers such as `d^{-epsilon}`, while any
`epsilon<1/4` already violates (S2) by an exponential margin.

## 1. The theorem parameter is forced to be `D(1+o(1))`

Write `d_J` for the degree parameter in the JMS theorem, to distinguish it
from the erosion depth used elsewhere in the repository.  Condition (H1)
requires

\[
 (1-d_J^{-\epsilon})d_J\le\delta_P(H_1)=D,qquad
 \Delta(H_1)=D\le d_J.                                         \tag{1.1}
\]

Consequently

\[
                 d_J=D+O(D^{1-\epsilon})=(1+o(1))D.             \tag{1.2}
\]

One cannot choose a much larger `d_J` to relax the host-size condition,
because the lower inequality in (1.1) would then fail.

## 2. The global-size exponent forces `epsilon >= 2^(-1/3)`

Condition (S2) includes

\[
 |P\cup Q|\le\exp(d_J^{\epsilon^3}).                            \tag{2.1}
\]

Here `P` contains `mathcal L`, while `Q` contains `mathcal U` and two
copies of `mathcal M`.  Stirling gives

\[
                  \log|P\cup Q|=\Theta(m).                      \tag{2.2}
\]

By (1.2),

\[
                  d_J^{\epsilon^3}=m^{2\epsilon^3+o(1)}.        \tag{2.3}
\]

For (2.1) to hold asymptotically, one must have

\[
                         2\epsilon^3\ge1-o(1),                  \tag{2.4}
\]

which is (0.3).  In particular every fixed `epsilon<1/4` is impossible.

## 3. A literal pair codegree forces `epsilon <= 1/2`

Fix `L` and a middle tail `T=L+{a}`.  The ordered diamonds containing both
vertices are

\[
                  e(L;a,b),\qquad b\in[2m]-T.                   \tag{3.1}
\]

There are exactly `m` of them.  Hence

\[
                          \Delta_2(H_1)\ge m.                    \tag{3.2}
\]

Condition (H2) requires

\[
                          \Delta_2(H_1)\le d_J^{1-\epsilon}.     \tag{3.3}
\]

Using (1.2), equations (3.2)--(3.3) give

\[
             m\le m^{2(1-\epsilon)+o(1)},                       \tag{3.4}
\]

and therefore (0.4).  Equations (0.3) and (0.4) contradict one
another.  Private vertices in `H_2` do not change this computation.

## 4. The mixed-conflict scale has the same barrier

The physical-collision conflicts also cannot be dismissed merely because a
fixed atom meets `O(D)` conflicting atoms.  The general JMS conditions use
weighted *conditional* unavoidability.

For a concrete row, fix an `H_1` atom `f` with tail `T`, and choose a
different lower set `x subset T` of rank `m-1`.  Among the private `H_2`
alternatives through `x`, exactly `m` remembered diamonds have tail `T` and
therefore conflict with `f`.  Since `d_(H_2)(x)=D`, their normalized weight
is

\[
                              {m\over D}={1\over m+1}
                              =D^{-1/2+o(1)}.                    \tag{4.1}
\]

The relevant mixed condition asks for at most `d_J^{-epsilon}`.  Thus it
again permits only `epsilon<=1/2+o(1)`, independently confirming the
first-stage codegree obstruction.

## 5. Scope of the short-cycle calculation

The estimate that a fixed directed `j`-cycle through one atom has
`O(D^(j-2))` completions is compatible with fixed-length conflict systems.
It becomes relevant only after all base hypotheses of the matching theorem
hold.  It cannot repair the contradiction in Sections 2--3.

Therefore the deductions

```text
exact ordered four-resource factor,
fixed-girth exact factor,
o(N)-cycle exact factor
```

do not follow from the proposed JMS construction.

## 6. What remains plausible

The private completion encoding is conceptually useful: if a matching
theorem with suitable large-host/codegree tolerances were available, its
conflict interpretation would indeed turn a selected private edge back into
one remembered physical diamond.  Three possible repairs remain open:

1. a resource-disjoint decomposition into subexponential/polynomial blocks,
   with exact global palette reconciliation;
2. a stronger perfect conflict-free matching theorem without (2.1), or with
   codegree tolerance reaching the square-root scale simultaneously; or
3. a direct alternating-cycle/absorption proof specialized to the Boolean
   diamond host.

None is supplied by the private-copy trick itself.  The repository's
previous exact common-basis and `P-o(P)` physical-forest theorems therefore
remain the strongest unconditional all-dimensional central results.
