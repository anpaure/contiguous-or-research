# Core-local amortization and boundary-interface coupling

## 1. Verdict

The amortized subcube theorem becomes strictly sharper after the exact
boundary--core decomposition is imposed.  A literal active-rank boundary
entry can represent its own rank-`r` value, but it cannot help represent any
proper subset of that value.  All proper-subcube capacity must be supplied by
the lower core.  Moreover, a length-`d+1` rank-`r` window which is not wholly
inside the core can occur only at one of the two boundary/core interfaces.

This gives an exact nonlinear deficiency budget for the **core support
profile**, rather than another average rank moment.  At the unresolved
`k=11,n=465` checkpoint it strengthens

```text
4 a_28 + 3 a_29 + 2 a_30 + a_31 <= 462
```

to

```text
6 a_28 + 4 a_29 + 2 a_30 + a_31 <= 462
```

in the no-literal-six-set branch.  There is an exact one-cell correction in
the endpoint-six-set branch.

If the peeled core is itself an exact equality word at rank `r-1`, its
literal rank-`r-1` facets give a second refinement.  For `k=11`, every
literal five-set contained in a six-set increases the deep-core capacity
demand for that six-set by one unit.

These statements do not rule out a length-465 word.  They identify the next
missing information precisely: correlations between which subcubes have low
support and which physical long windows supply their credits.

## 2. Exact boundary--core setup

Fix `2<=r<k`, put

\[
 M=\binom kr,
 \qquad
 L=\sum_{s=1}^{r-1}\binom ks,
\]

and let `d>=1` be the least integer for which

\[
 L\le dM+\binom{d+1}{2}.
\]

Assume a universal zero-free word `A` has the exact length `M+d`.
Boundary--core rigidity gives

\[
 A=P\,\Vert\,C\,\Vert\,Q,                              \tag{2.1}
\]

where the `h=|P|+|Q|` boundary entries are distinct rank-`r` sets, every
entry of `C` has rank below `r`, and `C` represents every nonempty mask of
rank below `r`.  In particular `OR(C)=[k]`.

Let `\mathcal B` be the set of the `h` literal boundary values.  Let
`\mathcal E` consist of the boundary value nearest `C` on each nonempty
side.  Thus

\[
 |\mathcal E|\le2,
 \qquad
 \mathcal E\subseteq\mathcal B.                         \tag{2.2}
\]

For `R in binom([k],r)`, define

\[
 P_R^C=\{i\in C:A_i\subseteq R\},
 \qquad p_R^C=|P_R^C|,
\]

and let `q_R^C` be the number of physical length-`d+1` intervals wholly
inside `C` whose OR is `R`.

## 3. Exact support and credit splitting

### Lemma 3.1 (support split)

If `p_R=|{i:A_i subseteq R}|` is the full-word support, then

\[
 p_R=p_R^C+\mathbf1_{\{R\in\mathcal B\}}.                \tag{3.1}
\]

#### Proof

Every boundary value is an `r`-set.  Such a value is contained in the
`r`-set `R` if and only if it equals `R`.  Boundary values are distinct. ∎

### Lemma 3.2 (only interface windows earn boundary credit)

Let `q_R` count all length-`d+1` windows of OR `R`.  There are numbers
`x_R in {0,1}` such that

\[
 q_R=q_R^C+x_R,                                          \tag{3.2}
\]

\[
 x_R=0\quad(R\notin\mathcal E),
 \qquad
 \sum_Rx_R\le2.                                         \tag{3.3}
\]

#### Proof

Consider a length-`d+1` rank-`r` window not wholly in `C`.  It contains a
boundary entry `T`.  Since `T` and the window OR both have rank `r`, the
window OR must equal `T`.  It cannot contain a second boundary entry, since
the boundary values are distinct incomparable `r`-sets.

As `d+1>=2`, a window wholly inside a boundary block contains at least two
boundary entries and is impossible.  A crossing window containing exactly
one boundary entry must use the entry nearest the core and then extend into
the core.  There is only one such length-`d+1` window at either interface.
An interval meeting both boundary blocks contains the coordinate-complete
core and has OR `[k]`, not rank `r`.  This proves (3.2)--(3.3). ∎

The lemma is the exact interaction with the boundary pin rectangles: all
rank-`r` long-window credit outside the core is concentrated at the two
interface cells.  The other `h-2` possible literal boundary values obtain no
long-window credit from their own occurrence.

## 4. The core-local amortization theorem

Put

\[
 N_r=2^r-1,
 \qquad
 c=c_{r,d}=\left\lceil\frac{2N_r}{d+1}\right\rceil.
\]

### Theorem 4.1 (proper-subcube capacity in the core)

For every `R in binom([k],r)`,

\[
 \boxed{
 (d+1)p_R^C+(d-1)q_R^C\ge2(2^r-2).}                     \tag{4.1}
\]

Moreover,

\[
 \boxed{\sum_Rq_R^C\le M-h.}                            \tag{4.2}
\]

#### Proof

Every nonempty proper subset of `R` has rank below `r`; boundary--core
rigidity gives it a witness wholly in `C`.  The global containment cap says
that witness has length at most `d`.

The positions of `P_R^C` form runs of length at most `d+1`.  A core run has
length `d+1` if and only if its OR is `R`, so such runs are counted by
`q_R^C`.  For a run of length `ell`, the number `f_d(ell)` of its internal
intervals of length at most `d` satisfies

\[
 2f_d(\ell)\le(d+1)\ell+(d-1)\mathbf1_{\{\ell=d+1\}}.
\]

The core runs contain distinct witnesses for all `2^r-2` nonempty proper
subsets of `R`.  Summing the displayed run inequality proves (4.1).

The core has length `M+d-h`, and hence contains exactly `M-h` physical
windows of length `d+1`.  Each contributes to at most one `q_R^C`, proving
(4.2). ∎

For `d>1`, define the integer credit demand

\[
 g_{r,d}(p)=
 \max\left\{0,
 \left\lceil
 \frac{2(2^r-2)-(d+1)p}{d-1}
 \right\rceil\right\}.                                  \tag{4.3}
\]

Let

\[
 b_R=\mathbf1_{\{R\in\mathcal B\}}.
\]

The full-word amortized theorem and (3.1)--(3.2) give

\[
 q_R^C\ge(c-p_R^C-b_R-x_R)_+.
\]

Combining this with (4.1) and then using (4.2) proves the exact nonlinear
core-profile cut

\[
 \boxed{
 \sum_R
 \max\left\{
 g_{r,d}(p_R^C),
 (c-p_R^C-b_R-x_R)_+
 \right\}
 \le M-h,}                                               \tag{4.4}
\]

where the latent interface credits satisfy (3.3).  In addition, disjointness
of the long support runs gives the pointwise feasibility condition

\[
 q_R^C\le\left\lfloor\frac{p_R^C}{d+1}\right\rfloor.     \tag{4.5}
\]

When `d=1`, equation (4.1) instead reads simply

\[
 p_R^C\ge2^r-2,                                          \tag{4.6}
\]

and the second term in (4.4) remains valid.

Equation (4.4), not its average over `R`, is the main new consequence.  It
couples the whole lower tail of the core supports to one shared physical
window budget and to at most two interface exceptions.

## 5. Exact `k=11` consequences

Take `k=11,r=6,n=465`.  Then

\[
 M=462,
 \qquad d=3,
 \qquad c=32.
\]

Equation (4.1) becomes

\[
 2p_U^C+q_U^C\ge62.                                     \tag{5.1}
\]

Together with `q_U^C<=floor(p_U^C/4)`, this gives

\[
 p_U^C\ge28                                               \tag{5.2}
\]

for every six-set `U`.

### Case I: no literal six-set

Here `C=A`, `h=0`, and `x_U=0`.  If

\[
 a_j=|\{U:p_U=j\}|,
\]

then (4.4) is exactly

\[
 \boxed{6a_{28}+4a_{29}+2a_{30}+a_{31}\le462.}           \tag{5.3}
\]

Indeed, the core capacity demands respectively `6,4,2,0` credits at support
sizes `28,29,30,31`, while the full-subcube inequality additionally demands
one credit at size `31`.

This strictly strengthens the previous unrestricted lower-tail cut

\[
 4a_{28}+3a_{29}+2a_{30}+a_{31}\le462.
\]

### Case II: one endpoint six-set

After reversal write `A=T || C`, where `T` is a six-set and `|C|=464`.
Let

\[
 a_j^C=|\{U:p_U^C=j\}|.
\]

There are `461` length-four windows wholly in `C`.  The unique possible
interface credit belongs to `T`.  For `p_T^C=28,29,30`, the proper-subcube
demands `6,4,2` credits and already dominates that interface allowance; at
`p_T^C=31` it demands none.  Thus (4.4) specializes to

\[
 \boxed{
 6a_{28}^C+4a_{29}^C+2a_{30}^C+a_{31}^C
 -\mathbf1_{\{p_T^C=31\}}
 \le461.}                                                \tag{5.4}
\]

This is an exact distributional cut for the endpoint branch, not a fixed-row
assumption.

## 6. Moment tightness cannot freely coexist with a boundary

The coupling also clarifies the equality branch of the original amortized
moment theorem.  Put

\[
 \varepsilon=(d+1)c-2(2^r-1),
 \qquad 0\le\varepsilon\le d,
\]

and let

\[
 \Delta=\sum_Rp_R-(c-1)M.
\]

Since `p_R+q_R>=c` and `sum_R q_R<=M`,

\[
 \Delta=(M-\sum_Rq_R)+\sum_R(p_R+q_R-c).                 \tag{6.1}
\]

Both terms are nonnegative.

For a literal boundary value `R`, put

\[
 s_R=p_R+q_R-c.
\]

Substituting `p_R=p_R^C+1` and `q_R=q_R^C+x_R` into (4.1) gives

\[
 \boxed{
 (d+1)s_R
 \ge d-1-\varepsilon+(d+1)x_R+2q_R^C.}                  \tag{6.2}
\]

Consequently:

1. if `epsilon<=d-2`, every literal boundary value contributes at least one
   unit to `Delta`, so `Delta>=h`;
2. if `Delta=0`, every literal boundary value must satisfy

   \[
   x_R=q_R^C=0,
   \qquad \varepsilon\ge d-1.                            \tag{6.3}
   \]

At `k=11,r=6,d=3`, `epsilon=2=d-1`.  The independent tight-branch run
analysis proves `q_U=1` for every six-set.  Equation (6.3) would give
`q_T=0` for a literal boundary value.  Hence the moment-tight branch has

\[
 h=0.                                                     \tag{6.4}
\]

This is a valid structural interaction, but it does not eliminate a real
`k=11` case: cumulative rank-truncation already forces the six-set support
moment strictly above this theorem's equality value.  The significance of
(6.2) is all-dimensional; it prevents one from treating literal boundary
positions as cost-free in a tight amortized profile.

## 7. A consecutive inner peel: facet-incidence refinement

There is a further exact refinement when the outer core `C` itself has an
exact boundary--core decomposition at rank `r-1`:

\[
 C=P_{r-1}\,\Vert\,D\,\Vert\,Q_{r-1}.                    \tag{7.1}
\]

Let `\mathcal F` be its distinct literal rank-`r-1` boundary values.  For an
`r`-set `R`, put

\[
 t_R=|\{S\in\mathcal F:S\subset R\}|.                    \tag{7.2}
\]

Define `p_R^D` as the number of entries of `D` contained in `R`, and define
`q_R^D` as the number of length-`d+1` intervals wholly in `D` having OR
`R`.  Notice that `d` is still the **outer** rank-`r` slack.

### Theorem 7.1 (literal-facet penalty)

For every rank-`r` set `R`,

\[
 p_R^C=p_R^D+t_R,                                        \tag{7.3}
\]

\[
 \boxed{
 (d+1)p_R^D+(d-1)q_R^D
 \ge2(2^r-2-t_R),}                                      \tag{7.4}
\]

or equivalently

\[
 \boxed{
 (d+1)p_R^C+(d-1)q_R^D
 \ge2(2^r-2)+(d-1)t_R.}                                 \tag{7.5}
\]

Furthermore,

\[
 \sum_R t_R=|\mathcal F|(k-r+1),                         \tag{7.6}
\]

\[
 \sum_Rq_R^D\le\max\{|D|-d,0\}.                        \tag{7.7}
\]

#### Proof

A literal inner boundary value has rank `r-1`, so it is contained in `R`
precisely when it is one of the `t_R` facets counted in (7.2).  This proves
(7.3).

Every nonempty proper subset of `R` other than those `t_R` literal facets
has a witness wholly in `D`.  For ranks below `r-1` this is the defining
property of the inner core.  A nonliteral rank-`r-1` target also has its
witness in `D`: an interval containing a literal boundary `(r-1)`-set would
contain a distinct incomparable set of the same rank and could not have the
target OR.  All these proper-target witnesses have length at most `d` by the
outer containment cap.

There are `2^r-2-t_R` such targets.  Applying the same run-capacity argument
inside `D` gives (7.4).  Substitution of (7.3) gives (7.5).

Each literal `(r-1)`-set lies in exactly `k-r+1` rank-`r` sets, proving
(7.6).  Finally `D` contains at most `max{|D|-d,0}` length-`d+1` windows,
which proves (7.7). ∎

### The endpoint-six-set branch at `k=11`

In Case II, `C` is an exact length-464 rank-five equality word.  Let `h_5`
be its literal five-set boundary mass (`0<=h_5<=133`), and let `D` be the
remaining rank-at-most-four core.  For every six-set `U`, let `t_U` be the
number of those literal five-set facets contained in `U`.  Then

\[
 \boxed{2p_U^D+q_U^D\ge62-t_U,}                          \tag{7.8}
\]

equivalently

\[
 \boxed{2p_U^C+q_U^D\ge62+t_U.}                          \tag{7.9}
\]

The global incidence and credit budgets are

\[
 \sum_Ut_U=6h_5,
 \qquad
 \sum_Uq_U^D\le461-h_5.                                 \tag{7.10}
\]

In distributional form,

\[
 \boxed{
 \sum_U(62+t_U-2p_U^C)_+\le461-h_5.}                    \tag{7.11}
\]

Thus inner literal five-sets are not free support: each incident literal
facet raises the deep-core demand for its six-set by one.

## 8. Barrier and scope

The new cuts are feasible in both `k=11` branches.  They do not prove or
disprove `nu(11)=465`.

The reason is quantitative.  The nonlinear constraints become active when a
six-set support is near `28,...,31`, whereas the cumulative entry-rank cuts
force the average six-set support much higher (the minimum total support is
`18866`, an average of about `40.84`).  An abstract profile with all supports
near `40` or `41` easily satisfies (5.3)--(5.4), even though it need not come
from a word.

Accordingly, another scalar average cannot close the gap.  A further advance
must correlate at least two of the following:

* the identities of low-support `r`-sets;
* the physical locations of their length-`d+1` credit runs;
* the facet-incidence degrees `t_R` in an inner peel;
* the coordinate rectangles forced by pin survival.

The present theorem supplies the exact local and global budgets for such a
correlation argument.  It assumes no fixed derivative row, Johnson path,
natural grading, or chosen central order.

## 9. Verification

The independent checker

```text
python3 scratch/check_amortized_pin_coupling.py
```

reconstructs every interval OR in the archived exact words through `k=10`
and at `k=12`.  At every active exact rank it locates the literal boundary
blocks, recomputes `p_R^C,q_R^C,x_R`, and verifies (3.1)--(4.5) target by
target.  It also checks the two `k=11` coefficient tables and the inner-facet
incidence arithmetic.  All checks pass.
