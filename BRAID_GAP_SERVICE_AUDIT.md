# Independent audit of `BRAID_GAP_SERVICE.md`

## 1. Verdict

The main braid-plus-gap service inequality is valid, provided the dangerous
plateau overlap convention is made precise:

* take the **vertex union** of all dangerous plateaux;
* define gaps as the connected components of its complement;
* put every vertex shared by two dangerous plateaux in a separate omitted
  set, but do not put it back into a gap; and
* use the original, untruncated peak plateaux as threshold runs.

Under this convention, a genuine gap contains no vertex of any dangerous
plateau and hence no dangerous plateau.  The concern about different
coordinates sharing plateau endpoints does not invalidate Lemma 4.

The following source claims check out:

1. the dangerous-free-window lemma;
2. span `L+1=4a+3` and both congestion bounds;
3. the global cost inequality (1.4) and its leading coefficient
   `3c+2sigma-2cs`;
4. the `r=o(a)` corollary, including its parameter-sensitive hypothesis;
5. the transparent-separator counterexample.

There are three qualifications.

* The word “exact” for (1.4) means an explicit finite upper bound, not an
  equality.  Closing products, omitted overlap vertices, and terminal-block
  estimates introduce slack.
* The exceptional set in one gap has size at most `L`, not merely `2L`.
  This improves the explicit error in (1.3), although the displayed source
  bound remains valid.
* The sub-four conclusion for `r=o(a)` is not automatic from `r=o(a)`
  alone.  It also needs

  \[
  \sigma-cs<(4-3c)/2-\eta.                            \tag{1.1}
  \]

  The “mass-feasibility endpoint” is an additional parameter assumption,
  not a consequence of having few components.

The transparent separator is a real local obstruction: its coordinate sign
ledger is correct, all displayed points are distinct, and every internal
threshold run wholly inside the clean suffix contains one of the long full
line peaks.

## 2. Dangerous plateau overlaps and genuine gaps

Let the dangerous directed peak plateaux be the word intervals

\[
                         P_1,\ldots,P_m,
 \qquad \lambda(P_j)>ca.                              \tag{2.1}
\]

### 2.1 Edge and vertex intersections

Peak-plateau edge sets are pairwise disjoint, even across different
coordinates.  If two coordinate plateaux shared an ordering edge, two
coordinates would be equal at both endpoints; the zero-sum condition would
then make the third coordinate equal as well, contradicting distinctness of
the two middle points.

Two dangerous plateau vertex intervals can nevertheless share one word
position.  Such a shared position must be an endpoint of both intervals.
If it were interior to one plateau, that plateau would use both incident
ordering edges; the other nontrivial plateau would have to share one of
them.

At most two dangerous plateaux share one position.  Three nontrivial
intervals through the same word position would have to reuse one of the
two incident edges.  Consequently the overlap graph is a collection of
linear chains along the word.  If

\[
 \omega:=\sum_j|P_j|-\left|\bigcup_jP_j\right|,       \tag{2.2}
\]

then

\[
                         0\le\omega\le m-1.           \tag{2.3}
\]

This validates the overlap bound in (1.5).

### 2.2 The convention needed by the gap lemma

Define

\[
 \mathcal P:=\bigcup_{j=1}^m P_j                       \tag{2.4}
\]

as a vertex union.  A gap is a nonempty interval component of
`[1,M_a] setminus mathcal P`.  Shared plateau endpoints remain in
`mathcal P`, although they are omitted as assignment starts to avoid
double service.

With this definition,

\[
 |\mathcal P|=\sum_j(\lambda(P_j)+1)-\omega
              =E+m-\omega,                           \tag{2.5}
\]

and hence

\[
 G=M_a-|\mathcal P|=M_a-E-m+\omega.                  \tag{2.6}
\]

Every dangerous plateau is a subset of `mathcal P`; therefore no gap
contains one.  This is the precise justification needed in Lemma 4.

The informal sentence that plateau intervals “may be treated as disjoint”
is safe only for start accounting.  One must not truncate both plateaux at
a shared endpoint and then classify that endpoint as a gap point: the
truncated blocks would no longer be maximal threshold runs, and the
resulting artificial gap would not satisfy the stated complement property.

Resolve all dangerous plateaux into `r` maximal direct rotating components.
A connected component of `mathcal P` may contain more than one direct
component—for example when the rotation rule fails at two adjacent blocks,
or when blocks share an endpoint—but it cannot contain fewer than one.
Thus the number of connected components of `mathcal P` is at most `r`, and
the number of complement gaps is at most

\[
                              r+1.                   \tag{2.7}
\]

So the gap-count step in Section 4 is valid under the vertex-union
convention.

## 3. Dangerous-free windows

### 3.1 Nondirected peaks

On a constant-coordinate plateau, the two cross-coordinate values are
distinct and sum to a constant.  If their order is not monotone, one has an
interior strict local maximum or minimum.  A maximum is a singleton peak
of that coordinate; a minimum is a singleton peak of the complementary
cross-coordinate.  Because this point lies in the interior of the original
plateau, both neighboring word positions lie there too, so the singleton is
an internal peak in the full word.

Lemma 3 is therefore correct.

### 3.2 Lemma 4

Let `W` have `L=4a+2` positions and contain no directed peak plateau of cost
greater than `ca`.  The universal peak-mesh theorem supplies a full-word
internal peak plateau `P` contained in `W`.

* If `lambda(P)<=ca`, use `P` itself.
* If `lambda(P)>ca`, then `P` cannot be directed, and Lemma 3 supplies a
  singleton internal peak inside it.

In either case `W` contains an internal threshold run of cost at most `ca`.
The two boundary comparisons certifying the peak lie inside `W`, so the run
cannot extend outside the window.  Lemma 4 is correct.

For a window contained in a genuine gap from Section 2.2, the hypothesis is
automatic: a directed dangerous plateau contained in the window would be a
subset of `mathcal P`, whereas the window lies in its complement.

## 4. One-dimensional gap service

Let a gap be `I=[u,v]`, of size `g=v-u+1`.  A start `i` is serviced
rightward if `i+L<=v`, and leftward if `i-L>=u`.  Hence the exact number of
positions with neither option is

\[
 |U(I)|=
 \begin{cases}
 g,&0\le g\le L,\\
 2L-g,&L<g<2L,\\
 0,&g\ge2L.
 \end{cases}                                         \tag{4.1}
\]

In particular,

\[
                         |U(I)|\le L,                 \tag{4.2}
\]

which is twice as strong as the source's useful but loose `2L` bound.

Every nonexceptional gap start receives a cost-`ca` run from Lemma 4.
Every exceptional start receives the universal peak-mesh run of cost at
most `2a`.  Therefore

\[
 Q(I)\le ca\,g+(2-c)a|U(I)|.                         \tag{4.3}
\]

For at most `r+1` gaps this yields

\[
 Q_{\rm gap}\le caG+(2-c)aU,
 \qquad U\le L(r+1),                                 \tag{4.4}
\]

improving the source's `2L(r+1)` without changing the leading term.

### 4.1 Span and congestion

A rightward gap window is `[i+1,i+L]`.  If its selected run is `[x,y]`,
then under the audited one-sided-span convention

\[
                         y+1-i\le L+1.                \tag{4.5}
\]

The extra one is real: the run may end at `i+L`.  The symmetric leftward
span is at most `L+1`.  A fixed adjacent `alpha` increment is therefore
charged by at most `L+1` forward starts, and a fixed `beta` increment by at
most `L+1` backward starts.  Thus

\[
 C_\alpha,C_\beta\le L+1=4a+3.                      \tag{4.6}
\]

This part of the source has the off-by-one correct.

The same bound remains valid after mixing gap service, universal fallback,
and braid service: congestion depends only on the maximum one-sided span,
not on the number of gaps or on how the three classes are interleaved.

## 5. Direct-component service

Within one direct component, successive plateaux are disjoint adjacent word
blocks.  Assign every nonomitted start in `P_j`, except starts in the
terminal block, the next plateau `P_(j+1)`.

For the first start of `P_j`, the one-sided span to the end of `P_(j+1)` is

\[
 \lambda_j+\lambda_{j+1}+2\le4a+2=L,                \tag{5.1}
\]

because every coordinate line has at most `2a+1` points.  Thus this part
has no worse congestion than the gap assignment.

Its actual cost before terminal fallback is bounded by

\[
 \sum_{\text{nonterminal }j}(\lambda_j+1)\lambda_{j+1}. \tag{5.2}
\]

For `x,y in [ca,2a]`, writing `x=ca+u`, `y=ca+v` gives

\[
 2uv\le(2-c)a(u+v),
\]

and hence the secant inequality

\[
 xy\le(1+c/2)a(x+y)-2ca^2.                         \tag{5.3}
\]

Add the nonnegative closing product in each component.  Every plateau cost
then appears in two cyclic products, so summing (5.3) gives

\[
 \sum \lambda_j\lambda_{j+1}
 \le(2+c)aE-2ca^2m.                                 \tag{5.4}
\]

The `+1` part of (5.2) contributes at most `2am`.  Therefore

\[
 Q_{\rm braid}\le(2+c)aE-2ca^2m+2am.               \tag{5.5}
\]

This algebra is correct.  It remains an upper bound rather than an exact
cost because of the added closing products and because omitted shared
endpoints may have been counted fictionally in (5.2).

Let `V` be the vertex union of the terminal dangerous blocks.  Since each
has at most `2a+1` positions,

\[
                            V\le(2a+1)r.             \tag{5.6}
\]

Universal fallback on those starts costs at most `2aV`.

## 6. Global finite accounting

The categories

* genuine gap positions;
* nonterminal dangerous-block positions;
* terminal dangerous-block positions; and
* omitted shared endpoints

cover the word, with only the last category unassigned.  There are at most
`m-1` omitted positions.

Adding (4.4), (5.5), and terminal fallback gives the source inequality

\[
 \boxed{
 Q\le(2+c)aE-2ca^2m+2am
       +caG+(2-c)aU+2aV.}                            \tag{6.1}
\]

Using (2.6), `E=sigma*a^2`, and `m=s*a`, its cubic part is

\[
 \bigl(3c+2\sigma-2cs\bigr)a^3.                    \tag{6.2}
\]

Indeed, after removing (6.2), the exact displayed remainder is

\[
 \begin{aligned}
 R={}&3ca^2+ca+(2-c)am+ca\omega\\
    &+(2-c)aU+2aV.                                  \tag{6.3}
 \end{aligned}
\]

This reproduces the source algebra.

Peak edge disjointness gives `E<=M_a-1`.  Since every dangerous block has
`lambda>ca`,

\[
 m<\frac{M_a-1}{ca}<3a+3,
 \qquad m\le3a+2.                                   \tag{6.4}
\]

Using `omega<=m`, `1<c<2`, (5.6), and the source's loose
`U<=2L(r+1)` gives exactly a safe bound of the displayed form

\[
 R\le(12a^2+6a)r+23a^2+15a.                        \tag{6.5}
\]

Thus Theorem 1 as printed is valid.

Using the sharper (4.4) instead gives, still with deliberately simple
coefficient relaxations,

\[
 \boxed{
 R\le(8a^2+4a)r+19a^2+10a.}                        \tag{6.6}
\]

For (6.6), bound successively

\[
 \begin{aligned}
 3ca^2&\le6a^2, & ca&\le2a,\\
 (2-c)am&\le3a^2+2a,
 &ca\omega&\le6a^2+4a,\\
 (2-c)aU&\le(4a^2+2a)(r+1),
 &2aV&\le(4a^2+2a)r.
 \end{aligned}
\]

The constants sum to `19a^2+10a`.  This tightening is optional; it does not
change any asymptotic conclusion.

Omitting the shared endpoints is also harmless for later fan-capped use:
there are only `O(a)` of them, so at a cap `Theta(a)` their unassigned
contribution is `O(a^2)`.

## 7. The few-component corollary

If `r=o(a)`, either finite error (6.5) or (6.6) is `o(a^3)`.  Hence

\[
 Q\le\bigl(3c+2(\sigma-cs)\bigr)a^3+o(a^3).         \tag{7.1}
\]

Put

\[
 e_c:=\sigma-cs
 =\frac1{a^2}\sum_P(\lambda(P)-ca)\ge0.             \tag{7.2}
\]

The exact leading condition for a strict sub-four assignment is

\[
                         3c+2e_c<4.                  \tag{7.3}
\]

Thus the source implication

\[
 e_c<(4-3c)/2-\eta
 \quad\Longrightarrow\quad
 Q\le(4-2\eta)a^3+o(a^3)                            \tag{7.4}
\]

is correct.

If additionally `sigma=cs+o(1)`, then `e_c=o(1)` and the coefficient is
`3c+o(1)`.  At `c=4/3-1/1000`, this is `4-3/1000+o(1)`.

The word “consequently” in Corollary 2 is safe because (1.8) is explicitly
stated.  The surrounding prose should not be shortened to “few components
imply sub-four”: `r=o(a)` removes only the interface error, while (7.3)
controls the potentially cubic excess length of the dangerous blocks.

## 8. Audit of the transparent separators

Let `a=12m`, `1<=j<=m-1`, `t_j=7m+j`, and `r_j=6m+j`.  The full line blocks
have endpoints

\[
 \begin{array}{c|c|c}
 &\text{first}&\text{last}\\ \hline
 X_t&(t,-a,a-t)&(t,a-t,-a)\\
 Y_t&(a-t,t,-a)&(-a,t,a-t)\\
 Z_t&(-a,a-t,t)&(a-t,-a,t).
 \end{array}                                        \tag{8.1}
\]

### 8.1 Distinctness

All selected levels satisfy `t_j>a/2`, so full high lines in different
coordinate directions are disjoint: an `x=t` and `y=u` line could meet in
`H_a` only when `t+u<=a`.  Parallel lines are disjoint.

The separators have one coordinate `-a` and the other two values
`6m+j,6m-j`.  Their positive levels do not equal any selected `t_k`:
`6m+j=7m+k` would require `j-k=m`, impossible for
`1<=j,k<=m-1`.  Different separator types put `-a` in different
coordinates, and indices within one type give different values.  Thus all
displayed points are distinct and no separator belongs to a full block.

### 8.2 Join signs

At `X_(t_j)|R^z_j|Y_(t_j)`, the three points are

\[
 (7m+j,5m-j,-12m),
 (6m+j,6m-j,-12m),
 (5m-j,7m+j,-12m).                                  \tag{8.2}
\]

Thus `x` strictly decreases, `y` strictly increases, and the three-position
`z=-a` plateau is a strict local minimum.  The joins
`Y|R^x|Z` and `Z|R^y|X` are cyclic copies.  At the cross-level join to
`X_(t_(j+1))`,

\[
 5m-j<6m+j<7m+j+1,
 \qquad
 7m+j>6m-j>5m-j-1,                                  \tag{8.3}
\]

so the same monotonicity ledger persists.

Inside `X`, `Y`, and `Z`, one coordinate is constant and the two others are
strictly monotone.  Equations (8.2)--(8.3) therefore show that the only
internal peak plateaux away from the two suffix boundaries are the full
line blocks.  The separator plateaux at `-a` are local minima, not peaks.

Each full block contains `2a-t_j+1` positions and has cost

\[
 \lambda_j=2a-t_j=17m-j\ge16m+1>4a/3.               \tag{8.4}
\]

### 8.3 Threshold runs and local windows

Every internal maximal upper-threshold component in a scalar word contains
an internal maximum plateau: take a plateau attaining the largest value in
the component.  Its neighbours are smaller, including at component
boundaries, which lie below the threshold.

Hence every internal threshold run wholly contained in the clean suffix
contains one of the full blocks from (8.4) and has cost greater than
`4a/3`.

There are `3(m-1)-1=Theta(a)` separator positions.  Since each full block
has `Theta(a)` positions while `L=Theta(a)`, deleting the constant number of
separators within distance `L` of either suffix boundary leaves
`Theta(a)` separators.  At each remaining separator, both adjacent
`L`-position windows lie wholly in the clean suffix, so every internal
avoiding run contained in either window has cost greater than `4a/3`.

Prepending the unused points can alter peak structure only at the one new
prefix/suffix seam.  Retaining separators whose windows avoid that seam
preserves the argument.  Thus the construction is a valid full-permutation
counterexample to pointwise local cheapness.

It does not contradict Theorem 1: the separators split the long blocks into
`Theta(a)` direct components, and the theorem's interface allowance is then
`Theta(a^3)`, not lower order.

## 9. Peak-free gap normal form

The final valley statement is also sound with its intended hypothesis.
Suppose a genuine gap contains no cheap internal peak plateau.  It already
contains no directed dangerous plateau by definition.  A nondirected peak
of cost greater than `ca` would contain a cheap singleton by Lemma 3, while
a directed peak of cost at most `ca` is itself cheap.  Thus it has no
internal peak plateau at all.

Each coordinate word is therefore weakly valley-shaped.  Sorting the three
valley indices gives two exterior constant regions of size at most one and
two middle regions on which every coordinate is monotone.  The standard
potential argument bounds each middle region by `2a+1`, giving gap length at
most `4a+1`.

Finally, constant-coordinate plateau edge sets are globally disjoint across
all coordinates, so

\[
 \sum_{\text{all constant-coordinate plateaux }P}\lambda(P)
 \le M_a-1.                                         \tag{9.1}
\]

This is an edge budget only.  As the source correctly notes, it does not
yet provide the nonlocal assignment needed when `r=Theta(a)`.

## 10. Corrected theorem ledger

**Proved:**

* the dangerous-free-window cheap-run lemma;
* the gap-service inequality, with the sharper `U<=L(r+1)`;
* congestion `C_alpha,C_beta<=4a+3`;
* the direct-component secant bound;
* the global leading cost and both finite error bounds (the source's loose
  one and the refinement (6.6));
* the parameter-sensitive `r=o(a)` corollary; and
* the transparent-separator local counterexample.

**Required convention:** gaps are complements of the dangerous **vertex
union**, and shared endpoints are omitted rather than reclassified as gap
positions.

**Not proved:**

* sub-four service from `r=o(a)` without the excess-mass condition (7.3);
* a uniform sub-four theorem for `r=Theta(a)`;
* cheap average service of the transparent separators; or
* a global charge of all interface starts to the nonpeak plateau-edge
  budget.

The source's central theorem survives the audit.  The next unresolved step
is genuinely the many-component transition-resource problem, not a hidden
failure of the dangerous-free gap decomposition.
