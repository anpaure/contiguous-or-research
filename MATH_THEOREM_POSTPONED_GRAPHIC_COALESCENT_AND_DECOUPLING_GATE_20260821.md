# The postponed graphic gate: exact coalescent structure and the decoupling obstruction

**Status (2026-08-21).**  Every statement below is proved.  The note does
not construct the final common-path selector.  It proves four facts about
the one-central/graphic route.

1. By narrowing the free tail by one position, the common-transformation
   microblock may be made chordless at **every** band rank and
   maximum-distance-pair-free at both middle ranks.  Its uniform-seed law
   then has the desired `O(n^(-2))` same-rank pair kernel simultaneously
   throughout the band.
2. If the real/dummy quotas are assigned after the paths are chosen, every
   postselected-quota Hall deficiency is exactly its **quota-relative global
   union deficit**.  There is no remaining subset-Hall or
   component-susceptibility gate within that postselection model.
3. The postponed forest process nevertheless has an exact rooted-block coalescent
   potential.  The component-square hypothesis is, modulo charged paths,
   precisely bounded second moment of the number of microblocks per
   component.
4. At the no-dummy postponed middle rank, small graphic charge already
   forces almost all observations to be first occurrences.  Independent
   neutral postponed decks instead suffer the usual concentrated linear
   coupon loss; conditional neutrality gives the corresponding expectation.

The first item removes the **annealed** all-band pair-kernel objection.  It
does not make that estimate quenched under a coverage-aware selection.  The
second item shows that such a quenched estimate is not actually needed once
global union coverage is proved and quotas may be chosen after seeing all
decks.  It does **not** modify the previously defined fixed-quota fractional
palette or any of its degree/codegree calculations.

## 1. Narrowed-tail common fibers have an all-band pair bound

Put

\[
 n=2m+1,\qquad H=\lceil\sqrt{n\log n}\rceil,
 \qquad K=\{m-H,\ldots,m+1+H\}.
\]

The original tail floor is `f=m+H+2`.  In the free core use only the
strictly smaller legal generator set

\[
 \{f^\sharp,\ldots,n\},\qquad
 f^\sharp=f+1=m+H+3,\qquad
 d^\sharp=n-f^\sharp+1=m-H-1.                    \tag{1.1}
\]

These moves remain legal for the original palette.  Notice that

\[
 d^\sharp\le q\le f^\sharp-2\qquad(q\in K).       \tag{1.2}
\]

For a legal access word, the rank-`q` observation is the set of its last
`q` access occurrences.  Equal letters in the access word have occurrence
gap at least `f^sharp`.

### Lemma 1.1 (short chords below the narrowed floor)

If `q<=f^sharp-2`, two rank-`q` observations at a time gap
`2<=g<q` cannot be Johnson-adjacent.

#### Proof

The two occurrence windows overlap in `q-g` positions.  Adjacency would
match `g-1` of the `g` exiting occurrences with `g-1` of the `g` entering
occurrences.  Number both groups from `1` to `g`.  If exit `i` matches
entry `j`, its recurrence gap is `q+j-i`, and hence
`j-i>=f^sharp-q`.  If `i_0,j_0` are the unmatched positions, summing over
the matching gives

\[
 (g-1)(f^\sharp-q)
 \le\sum_{\rm matched}(j-i)=i_0-j_0\le g-1.
\]

Thus `f^sharp-q<=1`, contrary to (1.2).  \(\square\)

The history-free endpoint estimate with the narrowed tail is

\[
 \Pr(C_q(\pi_{u+g})=S\mid\mathcal F_u)
 \le \prod_{r=1}^{\min(g,q)}{\min(r,d^\sharp)\over d^\sharp}.
                                                               \tag{1.3}
\]

In particular, if `g>=q>=d^sharp`, the right side is

\[
 B_\sharp={d^\sharp!\over(d^\sharp)^{d^\sharp}}
          =e^{-n/2+o(n)}.                              \tag{1.4}
\]

The proof is the usual last-occurrence exposure: a prescribed endpoint
fixes the set of the last `min(g,q)` distinct selected letters, and when
`r` prescribed letters remain at most `min(r,d^sharp)` of the
`d^sharp` moves are favorable.

### Theorem 1.2 (an all-band chordless common fiber)

Let `ell` satisfy `log ell=o(n)`.  There is a position permutation
`sigma in S_n` and a family `G_ell^sharp` of `ell`-step generator words,
all inducing `sigma`, such that

\[
 |\mathcal G_\ell^\sharp|
 \ge{(1-o(1))(d^\sharp)^\ell\over n!},              \tag{1.5}
\]

and, from every seed, every word in the family has the following
properties.

1. Its deck is simple and chordless at every `q in K`.
2. At `q=m,m+1`, its deck contains no pair at maximum Johnson distance
   `m`.

For fixed `C>1` and `ell=ceil(Cn)`, the right side of (1.5) has logarithm

\[
 (C-1)n\log n-Cn\log2+n-o(n\log n).                \tag{1.6}
\]

#### Proof

Choose each generator independently and uniformly from (1.1).  A return at
a gap below `f^sharp` is impossible.  At a larger gap, (1.3) is at most
`B_sharp`; hence band-simplicity fails with probability at most
`|K| ell^2 B_sharp=o(1)`.

For chords, Lemma 1.1 excludes gaps `2<=g<q`.  At a gap `g>=q`, a fixed
rank-`q` target has `q(n-q)` Johnson neighbours, and (1.3) bounds each
endpoint by `B_sharp`.  A union bound over ranks and time pairs is at most

\[
 |K|\ell^2 n^2B_\sharp=o(1).                         \tag{1.7}
\]

At rank `m`, maximum-distance windows cannot occur at a gap below `m`.
At rank `m+1`, such windows cannot occur below gap `m`, because their
intersection has size at least two.  For every remaining gap, (1.3) is at
most `B_sharp`, and a fixed middle target has only `m+1` targets at maximum
distance.  The additional failure probability is at most
`2 ell^2(m+1)B_sharp=o(1)`.

All three properties depend only on the generator positions, not on seed
labels.  Thus `(1-o(1))(d^sharp)^ell` words are good from every seed.
Partition them by their induced position permutation.  There are at most
`n!` cells, so the largest proves (1.5).  Finally
`log d^sharp=log n-log2-o(1)` and
`log(n!)=n log n-n+o(n)`, which give (1.6).  \(\square\)

### Theorem 1.3 (simultaneous annealed all-band pair kernel)

Retain the first `a=ell-1=Theta(n)` consecutive post-move observations from
a family in Theorem 1.2.  Choose the seed uniformly from `S_n` and use any
branch law independent of the seed.  For every `q in K` and every two
distinct rank-`q` targets `S,T`,

\[
 \Pr(T\in U_q\mid S\in U_q)=O(n^{-2}).               \tag{1.8}
\]

More generally, for any consecutive retained prefix of length `a<=ell` the right side is
`O(n^(-2)+a/n^3)`.

#### Proof

Put `M_q=binom(n,q)`, let `j` be the Johnson distance of `S,T`, and write

\[
 N_{q,j}={q\choose j}{n-q\choose j}.                 \tag{1.9}
\]

Relabeling symmetry gives `Pr(S in U_q)=a/M_q`.  If `c_(q,j)` is the
number of unordered distance-`j` pairs in the branch deck, transitivity on
such pairs gives the exact formula

\[
 \Pr(T\in U_q\mid S\in U_q)
 ={2\,\mathbb E c_{q,j}\over aN_{q,j}}.              \tag{1.10}
\]

For `j=1`, chordlessness makes `c_(q,1)=a-1`, so (1.10) is

\[
 {2(a-1)\over aq(n-q)}=O(n^{-2}).                    \tag{1.11}
\]

For `j>=2`, the trivial bound `c_(q,j)<=binom(a,2)` gives at most
`a/N_(q,j)`.  Uniformly over the central band,

\[
 N_{q,j}=\Omega(n^3),                                \tag{1.12}
\]

except at `(q,j)=(m,m),(m+1,m)`, which Theorem 1.2 excludes.  To verify
(1.12), use the symmetry `q <-> n-q` and write `q=m-t<=m`.
The sequence in (1.9) is unimodal in `j`, so its minimum on an interval is
at an endpoint.  At `j=2` it is `Omega(n^4)`.  At `j=q`, for `t>=1`, it is

\[
 {m+1+t\choose2t+1}\ge {m+2\choose3}=\Omega(n^3),
\]

for all sufficiently large `n`, since `t<=H=o(m)`.  When `t=0`, the
exceptional endpoint `j=m` was deleted and
`N_(m,m-1)=m binom(m+1,2)=Omega(n^3)`.  This proves
(1.12), and (1.8) follows when `a=Theta(n)`.  \(\square\)

Theorem 1.3 is deliberately annealed over the seed.  Conditioning branch
and seed choices on an evolving central residual can concentrate on any
subfamily, so (1.8) is not the quenched estimate required by the custom
nibble.

### Theorem 1.4 (postselected quotas collapse Hall to the global quota deficit)

Fix one rank with an `M`-element real target universe.  Let
`U_1,...,U_b` be arbitrary ordered `a`-element decks and put

\[
 A=ab,\qquad V=\left|\bigcup_{i=1}^bU_i\right|.       \tag{1.13}
\]

Suppose the total required number of real clones is an integer `R` with
`0<=R<=min(A,M)`.  **Only after all decks are known**, choose integers

\[
 r_i+h_i=a,\qquad \sum_i r_i=R,\qquad \sum_i h_i=A-R. \tag{1.14}
\]

Then the quotas can be chosen so that their exact real-target Hall
deficiency is

\[
 \boxed{\delta=(R-V)_+.}                              \tag{1.15}
\]

Here `(R-V)_+` is the **quota-relative global union deficit**.  When
`V<=R`, the actual real-target leave is
`M-V=(M-R)+(R-V)`.  Thus, after postselecting the real/dummy decoration,
all subset Hall cuts disappear: only the quota-relative deficit remains.
No temporal or graphic property of the decks is needed for this assertion.

The order of quantifiers is essential.  This theorem does not allow the
quotas in the earlier fixed-quota fractional palette to be changed after
sampling, and it does not alter that palette's degrees or codegrees.

#### Proof

All `V` union targets admit an assignment to containing blocks with capacity
`a`: for every target family `X`,
`|X|<=a|N(X)|` because
`X subseteq union_(i in N(X))U_i`, so capacitated Hall applies.  Retain
`min(R,V)` of these assignments and let `c_i` be the number assigned to
block `i`.  Then `0<=c_i<=a` and `sum_i c_i=min(R,V)`.

If `R<=V`, set `r_i=c_i`.  These clones have an explicit perfect matching
to the assigned targets, so `delta=0`.

If `R>V`, first assign all `V` union targets as above.  Distribute another
`R-V` clones among the blocks under the capacities `a-c_i`; this is possible
because their total residual capacity is `A-V>=R-V`.  Set `r_i` equal to
the resulting clone count and `h_i=a-r_i`.  The assigned `V` clones match
distinctly, so `delta<=R-V`.  The full-block Hall cut gives
`delta>=R-V`.  This proves (1.15).  \(\square\)

In the fixed-quota one-central specialization, additionally assume
`A<=W` and `M_q<=A` at every outer rank.  Take `R=A` at either middle rank
and `R=M_q` at every outer rank.  Consequently, after the retained rank-`m`
decks have been packed, it is enough to prove

\[
 \sum_{q\in K\setminus\{m\}}
 \left(R_q-\left|\bigcup_iU_{i,q}\right|\right)_+
 =o(W),                                               \tag{1.19}
\]

together with the already established checkpoint charge and the total
two-middle baseline `2(W-A)=o(W)`.  Conversely each summand in (1.19) is a
Hall lower bound for these postselected quotas.  Hence (1.19) exactly
calibrates the postponed-rank Hall deficiency **inside the postselection
model**, with no block-boundary loss.

For postselected decorations this bypasses the earlier component-square
sufficient route.  It does not supersede that route when quotas have been
frozen in advance.  Quenched pair estimates and coalescent balance remain
possible sufficient tools for proving (1.19), but are not additional
postselection requirements after (1.19) is known.

The same observation gives a sufficient formulation that does not assume a
pre-matching even at the first middle rank.

### Corollary 1.5 (all-rank union-cover criterion)

Choose one band-simple common path in each of `b` slots, without any prior
resource matching.  Assume that, after restoring all checkpoints, bridges,
and collars, these paths concatenate into a legal cyclic singleton word
whose equal-letter cyclic gap is at least `f`, and whose physical length
satisfies

\[
 L_{\rm phys}=A+b+L_{\rm bridge/collar}\le W+o(W).   \tag{1.20a}
\]

Here a different normalization may replace the displayed decomposition by
the direct hypothesis `L_phys<=W+o(W)`.  At rank `q` put

\[
 M_q={n\choose q},\qquad R_q=\min(A,M_q),\qquad
 V_q=\left|\bigcup_iU_{i,q}\right|.                  \tag{1.20}
\]

If

\[
 \sum_{q\in K}(R_q-V_q)=o(W),\qquad
 \sum_{q\in K}(M_q-R_q)=o(W),\qquad |K|b=o(W),       \tag{1.21}
\]

then the selected paths admit post hoc real/dummy decorations whose total
claimed-resource collision plus leave is `o(W)`.  More directly, their
retained decks miss only `o(W)` band targets.  Under the physical and cyclic
hypotheses above, the resulting word is a `DCC(n,H,o(1))`; the established
opening and far-rank absorption theorem then proves the coefficient-one
DCC bound.

#### Proof

Apply Theorem 1.4 independently at every rank.  Defect Hall matches
`R_q-delta_q` clones to distinct observed real targets.  Filling each of
the `delta_q` unmatched clones inside its own deck creates at most
`delta_q` collision, while the real-target leave is at most

\[
 M_q-(R_q-\delta_q)=M_q-R_q+\delta_q.
\]

Therefore collision plus leave is at most

\[
 (M_q-R_q)+2(R_q-V_q).                               \tag{1.22}
\]

Sum (1.22), and charge at most one claimed-resource incidence per restored
checkpoint and rank; the last hypothesis in (1.21) absorbs this
`|K|b` term.  This proves the claimed-resource statement.  For the actual DCC
calibration, the number of band targets absent from the retained decks is
the exact identity

\[
 \sum_{q\in K}(M_q-V_q)
 =\sum_{q\in K}(M_q-R_q)+\sum_{q\in K}(R_q-V_q)
 =o(W).                                               \tag{1.22a}
\]

Every retained target is a clean cyclic window by the gap-floor hypothesis,
and ignored physical observations can only add coverage.  Equation (1.20a)
and (1.22a) are precisely the length and missed-band clauses in
`DCC(n,H,o(1))`.  \(\square\)

For the standard maximal linear-checkpoint choice `A=W-O(poly(n))`, every
outer band layer has `M_q<=A` for all sufficiently large `n`; the second
sum in (1.21) is then exactly the two middle baseline leaves `2(W-A)=o(W)`.
More generally it remains an explicit hypothesis of (1.21).  Thus (1.21) is a cleaner sufficient
postselection target than “one central matching plus quenched graphic
completion.”
At a middle rank, where `R_q=A`
and there are no dummies, the identity is even exact:

\[
 \delta_q=A-V_q,                                      \tag{1.23}
\]

because duplicate mass is monotone under adding decks and the full block
set maximizes Hall deficiency.

There is an equivalent process invariant which is much simpler than
component susceptibility.  Order the decks arbitrarily, let `u_(i,q)` be
the number of targets in deck `i` not seen in earlier decks at rank `q`, and
put `x_(i,q)=a-u_(i,q)`.  Then

\[
 \sum_i x_{i,q}=A-V_q,
 \qquad
 R_q-V_q=\sum_i x_{i,q}-(A-R_q).                     \tag{1.24}
\]

Thus `A-R_q` is the repeat allowance represented by ignored/dummy claims,
and every old-target hit beyond it is quota-relative union deficit.  The
quota-relative union-deficit condition in (1.21) is equivalently

\[
 \sum_{q\in K}\left(
   \sum_i x_{i,q}-(A-R_q)
 \right)=o(W).                                       \tag{1.25}
\]

This is a direct first-order martingale target for the postselection route.
Pair probabilities and component-square mass can upper-bound it only
indirectly; they are alternative sufficient tools, not necessary
conditions for an arbitrary DCC construction.

## 2. Exact rooted-block coalescent

Fix one postponed rank and suppose every retained deck has `a` distinct
targets.  Augment deck `i` by its private root `zeta_i`, obtaining an
`a`-edge path `E_i`.  Starting from the empty forest, extend the current
forest maximally with edges of `E_i`.  Let

\[
 \kappa_i=\sum_C(|V(E_i)\cap C|-1)_+               \tag{2.1}
\]

be its exact cycle charge, where `C` ranges over the root-containing
components of the exposed forest immediately before insertion; unused
targets are not inserted as isolated components.  Thus `a-kappa_i` new
edges are retained.

Every omitted edge is spanned by the retained forest.  Consequently all
vertices of `E_i`, including `zeta_i`, lie in one component after step `i`,
and remain together thereafter.  A final component `C` therefore has
well-defined parameters

\[
 p_C=\#\{i:\zeta_i\in C\},\quad
 v_C=\#\{\hbox{real targets in }C\},\quad
 d_C=\sum_{i:\zeta_i\in C}\kappa_i.                \tag{2.2}
\]

### Theorem 2.1 (root-component ledger)

For every final component,

\[
 v_C=(a-1)p_C+1-d_C.                                 \tag{2.3}
\]

In particular, if `b` paths have been added and `g` root-containing
components remain in the exposed augmented union (unused isolated targets
are excluded),

\[
 ab-\left|\bigcup_{i=1}^bU_i\right|
 =b-g+\sum_{i=1}^b\kappa_i.                         \tag{2.4}
\]

#### Proof

The retained subgraph on `C` is a tree.  It has `v_C+p_C` vertices and

\[
 ap_C-d_C
\]

edges, because every path rooted in `C` contributed `a-kappa_i` retained
edges.  Equating the edge count to `v_C+p_C-1` proves (2.3).  Sum (2.3)
over the `g` components to obtain (2.4).  \(\square\)

Thus low graphic charge at a no-dummy rank is already a first-order
near-packing assertion.  If `ab=(1-o(1))M` and `b=o(M)` (equivalently
`a->infinity` in this normalization), then
`sum_i kappa_i=o(M)` implies

\[
 \left|\bigcup_iU_i\right|=(1-o(1))M.               \tag{2.5}
\]

Tree-like overlap is free only up to the `b-g=o(M)` boundary term; it
cannot hide a linear coupon deficit.

There is also an exact dynamic potential.  Before path `i` is inserted,
let `u_i` be its number of previously unseen targets.  Its other
`x_i=a-u_i` targets meet `t_i` old rooted components.  Then

\[
 \kappa_i=x_i-t_i.                                   \tag{2.6}
\]

Give an old component weight equal to its number of private roots, say
`p_1,...,p_(t_i)`, and put `B_i=sum_jp_j`.  Define the rooted-block
susceptibility

\[
 \Psi_i=\sum_Cp_C^2.                                 \tag{2.7}
\]

### Theorem 2.2 (exact coalescent increment)

At step `i`,

\[
 \Psi_i-\Psi_{i-1}
 =(1+B_i)^2-\sum_{j=1}^{t_i}p_j^2
 =1+2B_i+2\sum_{j<k}p_jp_k.                         \tag{2.8}
\]

Consequently

\[
 \sum_{i=1}^b t_i^2\le\Psi_b,\qquad
 \sum_{i=1}^b t_i\le\sqrt{b\Psi_b},                \tag{2.9}
\]

and

\[
 \sum_{i=1}^b(a-u_i)
 =\sum_i(t_i+\kappa_i)
 \le\sqrt{b\Psi_b}+\sum_i\kappa_i.                \tag{2.10}
\]

#### Proof

The new path merges precisely the `t_i` touched rooted components and its
own new root.  Their new root weight is `1+B_i`, which gives (2.8).
Since every `p_j>=1`, its right side is at least
`t_i^2+t_i+1`, proving the first inequality in (2.9); Cauchy--Schwarz gives
the second.  Equations (2.6) and (2.9) give (2.10).  \(\square\)

The target component square mass

\[
 \Phi_b=\sum_Cv_C^2                                  \tag{2.11}
\]

satisfies the deterministic upper bound

\[
 \Phi_b\le a^2\Psi_b.                                \tag{2.12}
\]

Conversely, suppose `a>=2`, `ab=Theta(M)`, `Phi_b=O(Ma)`, and
`sum_i kappa_i=o(ab)`.  Call a component good when
`d_C<=(a-1)p_C/2`.  Then

\[
 \sum_{C\ \mathrm{good}}p_C^2=O(b),\qquad
 \sum_{C\ \mathrm{bad}}p_C=o(b).                   \tag{2.13}
\]

Indeed (2.3) gives `v_C>=(a-1)p_C/2` on good components, while the total
root mass of bad components is at most
`2 sum_i kappa_i/(a-1)=o(b)`.  Hence the component-square hypothesis of the
linear-microblock nibble is, after charging `o(ab)` incidences, exactly a
bounded-second-moment assertion for the number of blocks coalesced into one
component.

One local sufficient balance rule is also immediate.  If every accepted
path obeys `B_i<=L`, then (2.8) gives

\[
 \Psi_b\le b(L+1)^2,\qquad
 \Phi_b\le a^2b(L+1)^2.                              \tag{2.14}
\]

Thus, together with a quenched pair factor `Lambda_n`, the usual
susceptibility calculation still gives total postponed charge `o(W)` when

\[
 |K|\Lambda_n(L+1)^2=o(n).                           \tag{2.15}
\]

This turns “balanced merging” into a precise acceptance statistic: the
quantity to cap is the **total old block mass touched**, not merely the
number of components touched.  The note does not prove that a central-
compatible branch satisfying this cap always exists.

## 3. Neutral decoupling has linear coupon loss

The first-order obstruction can be stated without any geometry.

### Theorem 3.1 (conditionally neutral decks)

Let `U_1,...,U_b` be adapted random `a`-subsets of an `M`-set, and let
`F_(i-1)` contain the complete past.  Suppose that, almost surely, for every
target `x` and every step,

\[
 \Pr(x\in U_i\mid\mathcal F_{i-1})={a\over M}.       \tag{3.1}
\]

Then

\[
 \mathbb E\left|[M]\setminus\bigcup_{i=1}^bU_i\right|
 =M\left(1-{a\over M}\right)^b.                    \tag{3.2}
\]

If `ab/M->1` and `a=o(M)`, the right side is
`(e^(-1)+o(1))M`.

#### Proof

For a fixed `x`, apply the tower property successively on the event that
`x` was avoided in the complete past.  Hypothesis (3.1) makes the next
avoidance probability exactly `1-a/M`, so the total avoidance probability
is `(1-a/M)^b`.  Sum over `x`.  \(\square\)

If the decks are mutually independent and each has the uniform one-target
marginal `a/M` (each deck may still have arbitrary internal dependence),
the loss is concentrated.  Changing one deck changes the union size by at
most `a`, so bounded differences gives

\[
 \Pr\left(\left|X-\mathbb EX\right|>t\right)
 \le2\exp\left(-{2t^2\over ba^2}\right),             \tag{3.3}
\]

where `X` is the number of uncovered targets.  At `b=(1+o(1))M/a`, with
`a->infinity`, `a=o(M)` (hence `b=o(M)`), and in particular for polynomial
`a` with exponential `M`, this yields

\[
 X=(e^{-1}+o(1))M                                    \tag{3.4}
\]

with probability tending to one.

When `ab=(1+o(1))M` and `b=o(M)`, (3.4) is also a linear no-dummy union
deficit and, by (2.4), forces linear graphic charge up to the `b-g` term.
Thus mutually independent neutral decks fail with high probability.
Conditional neutrality alone proves only the expectation (3.2), not that
every realization fails; an existence proof could in principle select an
exceptional correlated outcome.  Annealed pair codegrees, even the
simultaneous bound in Theorem 1.3, do not themselves provide the needed
first-order freshness.

## 4. Remaining postselection target and sufficient routes

Within the postselected-quota model of Theorem 1.4, the exact Hall target is

\[
 \sum_{q\in K}(R_q-V_q)=o(W).                       \tag{4.1}
\]

Together with the two-middle baseline and the physical/cyclic hypotheses of
Corollary 1.5, this is sufficient for `DCC(n,H,o(1))`.  It is not asserted
to be a necessary condition for an arbitrary DCC construction, whose
discarded checkpoints, collars, or other observations may supply additional
coverage.

At the other middle rank `R_(m+1)=A`, so its summand in (4.1) is exactly

\[
 A-V_{m+1}=\sum_i(a-u_i).                            \tag{4.2}
\]

For the sequential graphic strategy, (2.4) shows that
`sum_i kappa_i=o(W)` and `b=o(W)` suffice for (4.2).  The stronger
balanced-coalescent condition `Psi_b=O(b)`, combined with a quenched pair
bound, is one further sufficient way to prove small charge.  Neither that
pair bound nor component-square control is claimed necessary.

The all-band family of Theorem 1.2 supplies the favorable unconditioned
two-point scale.  The still-open constructive problem is to choose common
FIFO-compatible paths satisfying the simultaneous union target (4.1).
One may attack this either after a one-central matching or directly through
Corollary 1.5.  Theorem 3.1 rules out only the mutually independent neutral
experiment with high probability; it does not rule out correlated adaptive
selection.  If the coalescent route is used, controlling only the number
`t_i` of components touched is insufficient because repeated attachment can
build one giant component; the relevant balance statistic is `B_i`, the
total old rooted-block mass touched.
