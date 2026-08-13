# Resident completion of the compound-plus-halo bank is one age-filtered Hall gate

**Date:** 2026-08-13  
**Status:** exact reduction and sharp separation from the existing
uncoloured completion theorem.  The protected compound low-spine path and
all clean source halos admit mutually consistent local signed-age states.
Completing them to a componentwise biresident factor is equivalent to one
perfect-matching Hall system in an age-filtered successor graph.  The
ordinary polynomial protected-factor theorem and the long-arm scheduler do
not prove that Hall system.  A singleton tail can lose all successors under
an otherwise syntactically valid signed-age assignment, so age damage is
not controlled by unfiltered exposure.

## 1. Protected directed bank

Work in the middle-level incidence graph on rank-`(R-1)` and rank-`R`
sets of `[2R-1]`.  Let `P` be the path forest from

* the compound low-spine path; and
* the clean paired source-halo packages for every named crossing casualty.

By the frozen composition corollary, `P` has polynomial size, both
all-occurrence exposures below `R/3`, and maximum protected degree two.
Orient every path component in its prospective scheduled direction; for a
clean halo either orientation is allowed because the reflected halo
identity is available.

Colour the incidences alternately `0,1` along every oriented path.  Let
`F_0,F_1` be the resulting protected matchings.  Any resident completion
must choose a perfect matching `M_0` containing one colour class and then
choose the other perfect matching through a successor permutation.

Put

\[
                         L=d+1.                    \tag{1.1}
\]

Here a positive run or zero gap of `L` owners is the required PBBS
residence aperture.

## 2. Signed capped ages

For an owner `T` and coordinate `z`, a signed capped age is

\[
 \epsilon_T(z)={\bf1}_{z\in T},\qquad
 a_T(z)\in\{1,\ldots,L\},                         \tag{2.1}
\]

where `L` means “at least `L`”.  For a Johnson successor

\[
                         T'=T-x+y,                 \tag{2.2}
\]

the transition is age-legal precisely when

\[
\begin{array}{c|c|c}
 &T&T'\\ \hline
x&(1,L)&(0,1)\\
y&(0,L)&(1,1)\\
z\notin\{x,y\}&(\epsilon,a)&
   (\epsilon,\min\{L,a+1\}).
\end{array}                                       \tag{2.3}
\]

Every protected compound bridge was prospectively scheduled so all
internal runs and gaps are at least `L`; every clean halo is flag-convex
and exports all nonconstant flags to its far ports.  The release/deadline
and two-sided interval-Hall scheduler chooses its arm events so each
protected component has a consistent actual signed-age sequence.  Thus the
union of all protected paths supplies mutually compatible local age states
and clipped age profiles at its free ports.  Because the components are
resource-disjoint, there is no owner at which two local states disagree.

This proves local age legality only.  At every unprotected owner, and on
the exterior side of every free port, the age state is still to be chosen.

## 3. Exact resident completion theorem

Choose a perfect matching `M_0` which contains `F_0`.  Every protected
lower facet of the owner-path forest is incident with one edge of each
colour, so its colour-zero edge already occupies the lower endpoint of its
colour-one edge.  Consequently `M_0` automatically avoids `F_1`.  Such an
`M_0` exists by the polynomial protected matching-extension theorem.

Let

\[
                         X={ [2R-1]\choose R}
\]

be the rank-`R` owner shore, and regard `M_0(T)` as the matched
rank-`(R-1)` facet of owner `T`.  Define the unfiltered successor graph

\[
 T\longrightarrow T'
 \quad\Longleftrightarrow\quad
 M_0(T)\subset T',\qquad T'\ne T.                \tag{3.1}
\]

It is `(R-1)`-regular on the two copies of `X`: the facet `M_0(T)` has
exactly `R` rank-`R` supersets, one of which is `T`.  Choose a global signed-age
assignment `a` extending the protected local states, and retain only the
arcs satisfying `(2.3)`; call the result `D_(M_0,a)`.

The protected colour-`1` incidences determine a forced successor matching
`Q` in this graph.  This uses the declared endpoint and connector
schedules: their event orders must first pass the exact release/deadline
and interval-Hall tests so that every forced transition satisfies `(2.3)`.
Let `Z_Q` and `H_Q` be its tail and head sets.

### Theorem 3.1 (exact compound-halo resident cut)

There is a componentwise `L`-biresident simple spanning two-factor
containing every directed component of `P`, with matching phase `M_0` and
owner age assignment `a`, if and only if

\[
 \boxed{
 |N_{D_{M_0,a}}(S)\setminus H_Q|\ge |S|
 \quad(S\subseteq X\setminus Z_Q).}               \tag{3.2}
\]

If `(3.2)` holds, the completion is integral.  It is one owner cycle if
and only if its selected successor arcs also satisfy

\[
 \sum_{T\in S,\ T'\notin S}z_{TT'}\ge1
 \quad(\varnothing\ne S\subsetneq X).             \tag{3.3}
\]

#### Proof

Delete the forced tails and heads.  Extending `Q` is exactly a perfect
matching of the residual bipartite graph induced by `D_(M_0,a)`.  Hall's
theorem is `(3.2)`.  Adding the corresponding second incidence matching to
`M_0` gives a simple factor, and the deterministic update `(2.3)` makes
every cyclic positive and zero run have length at least `L`.  Conversely,
an oriented resident factor records actual capped ages and its successor
matching lies in `D_(M_0,a)`, so its residual part proves `(3.2)`.
Condition `(3.3)` is the usual subtour criterion for the successor
permutation. \(\square\)

This is the specialization of the general age-filtered completion theorem
to the present compound-plus-halo bank.  After the declared local schedules
have been completed, the local construction verifies

\[
                         Q\subseteq D_{M_0,a}.      \tag{3.4}
\]

It does not verify `(3.2)`.

## 4. The first exact obstruction is already a singleton tail

For a residual tail `T`, write

\[
                         M_0(T)=T\setminus\{x_0\}.  \tag{4.1}
\]

Its unfiltered successors are

\[
                         T_y=T\setminus\{x_0\}\cup\{y\}
                         \qquad(y\notin T).          \tag{4.2}
\]

The transition `T -> T_y` deletes `x_0` and inserts `y`.  Therefore it can
be age-legal only if

\[
                         a_T(x_0)=L,\qquad a_T(y)=L. \tag{4.3}
\]

The complete target age vector must additionally equal the deterministic
update `(2.3)`.  Consequently the following is a proof-safe upper bound
on the age-filtered outdegree:

\[
\deg^+_{D_{M_0,a}}(T)
 \le {\bf1}_{\{a_T(x_0)=L\}}
   |\{y\notin T:a_T(y)=L\}|.                      \tag{4.4}
\]

### Proposition 4.1 (sharp local Hall failure)

If one unforced tail satisfies either

\[
 a_T(x_0)<L
 \quad\text{or}\quad
 a_T(y)<L\quad\text{for every }y\notin T,          \tag{4.5}
\]

then `deg^+(T)=0` and the singleton set `{T}` violates `(3.2)`.

#### Proof

Equation `(4.4)` gives zero legal successors.  Since `T` is an unforced
tail, it remains on the residual tail shore, so the residual neighbourhood
of `{T}` is empty. \(\square\)

This obstruction is compatible with every uncoloured exposure bound.  It
uses no protected owner or lower collision and does not change the size of
the unfiltered successor neighbourhood.  Long arms ensure that the ages of
their own endpoint events are legal; they do not force `(4.3)` at every
unprotected owner of the exponential residual shore.  Notice also that
the converse of `(4.4)` is false for a preassigned global age labelling:
seasoned event labels need not make the target vector equal the required
deterministic update.

More generally, with

\[
 \gamma_Q(S)=|N_{D_{M_0}}(S)\setminus H_Q|-|S|,
\tag{4.6}
\]

and

\[
 \lambda_a(S)=
 |(N_{D_{M_0}}(S)\setminus H_Q)
   \setminus(N_{D_{M_0,a}}(S)\setminus H_Q)|,
\tag{4.7}
\]

the exact residual theorem is

\[
                         \lambda_a(S)\le\gamma_Q(S)
                         \quad\text{for every }S.   \tag{4.8}
\]

The polynomial protected-factor theorem controls ordinary incidence
exposure, not `lambda_a(S)`, and therefore does not imply `(4.8)`.

## 5. What a positive theorem must add

The remaining completion row is precisely:

> Co-select a perfect first matching `M_0` and a global signed-age
> assignment extending all compound/halo endpoint profiles such that
> `(4.8)` holds on every residual Hall shore.

A sufficient quantitative form would prove, for the chosen pair,

\[
 \max_{|S|=t}\lambda_a(S)
 \le
 \min_{|S|=t}\gamma_Q(S)
 \qquad(0\le t\le |X|-|Z_Q|).                    \tag{5.1}
\]

No theorem presently in the bank supplies this domination.  The long-arm
theorem solves clipped ages on polynomially many protected paths; the
ordinary matching/factor theorems solve unfiltered Hall; neither controls
age loss on the exponential unprotected shore.  Resident completion, not
local halo planting, is therefore the next exact carrier gate.
