# Audit of Fable Section 9: interval service, MASTER, and the supply law

## 1. Outcome

The main new assignment-free result survives:

\[
 \int_0^{2a}\min\{M_a,\operatorname{supply}(t)\}\,dt
 \ge4a^3-o(a^3),                                    \tag{1.1}
\]

and consequently, for every fixed `0<c<4/3`,

\[
 s(c):=\frac{\operatorname{supply}(ca)}{a^2}
 \ge\frac{4-3c}{2-c}-o(1).                          \tag{1.2}

The layer-cake argument and the monotonicity deduction are valid once the
`O(a)` boundary starts and the interval `0<=t<1` are handled explicitly.

Theorem L is also valid, but it is a coarse component-free service bound.
`FIRST_DANGEROUS_GLOBAL_SERVICE.md` supplies the refined alternative

\[
 Q\le[3c+2e_c+H_c]a^3+O(a^2),                       \tag{1.3}

whereas Theorem L gives

\[
 Q\le[3c+(4-c)e_c]a^3+O(a^2).                       \tag{1.4}

For `c>1`, the strongest current statement is the minimum of (1.3) and
(1.4).  The first-dangerous bound is stronger when
`H_c<(2-c)e_c`; Theorem L can be numerically stronger for large seam mass.
Thus Section 9 should not say that Theorem L uniquely supersedes all prior
interface accounting—the first-dangerous theorem is the gap-sensitive
refinement of the same component-free idea.

The two-sided theorem and its asymptotic doubly-blocked/pair consequences
are valid after excluding `O(a)` boundary indices from the pairing step.

The following claims need correction or demotion:

1. Theorem L's proof writes `end+1-i<=L+lambda+1<=6a+3`.  This does not
   prove the stated span.  The correct argument is simply
   `end<=i+L`, hence `end+1-i<=L+1=4a+3`.
2. A plateau of effective cost `q_i` need not be the **first** complete
   plateau in word order.  Choose a minimum-effective plateau instead.
3. Theorem M's union identity is exact only for service intervals clipped
   to valid starts `[1,M_a-L]`.  Unclipped intervals differ by only `O(a)`
   starts, so its asymptotic area bound remains true.
4. Boundary indices declared “doubly blocked” have no two windows and do
   not define plateau pairs.  Removing them costs only `O(a)` indices and
   leaves the stated asymptotic pair count unchanged.
5. The recorded negative edge-budget check reverses an inequality:
   `lambda>t` implies `L-lambda<L-t`, not `>=L-t`; an upper bound on the
   number of plateaux cannot establish a lower bound on supplied starts.
6. The static level bound `F(y)<=6(2-y)a+3` is justified only for `y>=1`,
   when two such plateaux cannot share one line.  It is false as stated for
   all `0<y<1` without multiplicity accounting.

## 2. Window dichotomy

Let `L=4a+2` and let

\[
                         W_i=[i+1,i+L]               \tag{2.1}

be a valid forward window in the selected-middle order.

The universal peak theorem supplies a complete internal peak plateau `P`
inside `W_i`.  If its cost is at most `ca`, it is itself a cheap threshold
run.  If it is longer and directed, it is `c`-dangerous.  If it is longer
and nondirected, one cross-coordinate sequence has an interior strict
extremum; a local maximum, or the complementary coordinate at a local
minimum, gives a singleton internal peak.

Thus Lemma 9.1 is correct for every fixed `0<c<2`, forward and backward.
The word “complete” is essential, as the source notes.

## 3. Theorem L

For each valid forward start, use a cheap run when the window is
dangerous-free and otherwise use the first complete dangerous plateau.
Let `n_P` be the number of starts assigned to plateau
`P=[u,u+lambda]`.  Containment in `W_i` is equivalent to

\[
                         u+\lambda-L\le i\le u-1,    \tag{3.1}
\]

so its complete service interval has exactly

\[
                         L-\lambda                  \tag{3.2}

integer starts.  The first-plateau rule only removes starts, hence

\[
                         n_P\le L-\lambda(P).        \tag{3.3}

### 3.1 Correct span

Every assigned dangerous plateau is a subset of `W_i`.  If its final
position is `v`, then

\[
                         v\le i+L,
 \qquad v+1-i\le L+1=4a+3.                          \tag{3.4}

The expression `L+lambda+1` in the source proof is an arithmetic mistake;
it would give only `6a+3`.  Equation (3.4) directly proves the theorem's
claimed span and therefore

\[
                         C_\alpha\le4a+3,
 \qquad C_\beta=0.                                  \tag{3.5}

### 3.2 Cost

There are `M_a-L` valid forward starts.  Count the final `L` starts at cap
`h=3a-1`.  With `delta_P=lambda(P)-ca`,

\[
\begin{aligned}
 Q
 &\le ca(M_a-L)+\sum_P\delta_Pn_P+Lh\\
 &\le caM_a+
       \sum_P(\lambda(P)-ca)(L-\lambda(P))+Lh.       \tag{3.6}
\end{aligned}

Since

\[
 L-\lambda(P)
 =(4-c)a+2-\delta_P,                                \tag{3.7}

and `sum delta_P=e_c a^2=O(a^2)`, this gives

\[
                         Q\le[3c+(4-c)e_c]a^3+O(a^2). \tag{3.8}

The theorem is correct.  Its proof should use `M_a-L`, not the occasional
`N-L`, because all windows are in middle-order index space.

### 3.3 Relation to the first-dangerous theorem

The first-dangerous localization proves, for `1<c<2`,

\[
 Q\le[3c+2e_c+H_c]a^3+O(a^2),                      \tag{3.9}

where

\[
 H_c=\frac1{a^3}\sum_{j\ge2}\delta_j
       \min\{g_{j-1},L-\lambda_j\}.                 \tag{3.10}

Both assignments are component-free.  Equation (3.9) records predecessor
localization and is substantially sharper for one-point or generally small
gaps.  Equation (3.8) is a robust fallback which ignores gaps.  Combining
them gives

\[
 Q\le
 \left[3c+\min\{(4-c)e_c,\,2e_c+H_c\}\right]a^3
 +O(a^2).                                           \tag{3.11}

Theorem L is therefore valid new bookkeeping at thresholds `c<=1`, where
the secant-based first-dangerous theorem was not stated, but for `c>1` it
is best presented alongside—not as replacing—the stronger localized
result.

## 4. The two-sided refinement

For an interior index

\[
                         L<i\le M_a-L,              \tag{4.1}

both forward and backward windows exist.  If at least one is
dangerous-free, Lemma 9.1 supplies a run of cost at most `ca` in that
direction.  Only an index for which both windows contain a dangerous
plateau must pay excess.  At such an index choose the forward plateau
`F(i)`.

The first and last `L` indices contribute at most `2Lh=O(a^2)`.  Therefore

\[
 Q\le caM_a+
       \sum_{i\in DB_{\rm int}}(\lambda(F(i))-ca)+O(a^2). \tag{4.2}

This is the correct form of Theorem L'.  Calling boundary starts “doubly
blocked” is harmless for the cost ledger but false literally; they must be
removed before any plateau-pair argument.

Every run used in (4.2) lies in one of the two `L`-windows, so forward and
backward spans are at most `L+1`; hence

\[
                         C_\alpha,C_\beta\le4a+3.   \tag{4.3}

## 5. Doubly-blocked indices and clustered pairs

Assume `D=o(a^2)`.  The run-spectrum lower bound at `h=3a-1` applied to
(4.2) gives

\[
 \sum_{i\in DB_{\rm int}}(\lambda(F(i))-ca)
 \ge(4-3c)a^3-o(a^3).                               \tag{5.1}

Because every plateau cost is at most `2a`, each summand is at most
`(2-c)a`.  Thus

\[
 |DB_{\rm int}|
 \ge\frac{4-3c}{2-c}a^2-o(a^2).                    \tag{5.2}

This is valid for every fixed `0<c<4/3`.

For every `i` in this set, choose one complete dangerous plateau `B(i)` in
the backward window and pair it with `F(i)` in the forward window.  The two
plateaux occur in left-to-right order and their starts are within `2L`
word positions (indeed a slightly sharper bound follows after subtracting
their lengths).

A fixed ordered pair `(B,F)` can arise for at most

\[
                         L-\lambda(F)
                         <(4-c)a+2                  \tag{5.3}

indices, since every such index belongs to the forward service interval of
`F`.  Therefore the number of distinct clustered ordered pairs is at least

\[
 \frac{4-3c}{(2-c)(4-c)}a-o(a).                    \tag{5.4}

At `c=1`, (5.2)--(5.4) become

\[
                         |DB_{\rm int}|\ge a^2-o(a^2),
 \qquad \#\text{pairs}\ge a/3-o(a).                \tag{5.5}

These source constants are correct.

The auxiliary statement that a fixed plateau sees only `O(1/c)` dangerous
plateau starts in a preceding interval of length `2L` is also true at the
order level, but its proof needs the endpoint extension: every such plateau
has more than `ca` disjoint edges and lies inside an interval of length at
most `2L+2a=O(a)`.  It is not needed for (5.4).

## 6. Corollary S: excess mass and line count

Theorem L combined with the run-spectrum lower bound yields

\[
                         e_c\ge
 \frac{4-3c}{4-c}-o(1),                              \tag{6.1}

for every fixed `0<c<4/3`.  This is correct.

At `c=1`, every dangerous plateau has

\[
                         \delta_P=\lambda(P)-a\le a. \tag{6.2}

Consequently (6.1) forces at least

\[
                         a/3-o(a)                   \tag{6.3}

such plateaux.  Two plateaux of cost greater than `a` cannot lie on the
same coordinate line: their vertex counts would sum to more than `2a+2`,
while a line contains at most `2a+1` points.  They therefore occupy distinct
coordinate lines, and `lambda>a` also implies `|t|<a` from
`lambda<=2a-|t|`.

All these plateau-count consequences are valid.  The same lower count will
also follow from the supply law in Section 9.

The claim that Theorem N “implies” (6.1) needs interpretation.  The
pointwise supply lower bound alone does not force excess mass: many
plateaux just above `ca` can have large total service but arbitrarily small
`e_c`.  The full `q_i` lower law together with the multiplicity upper bound
(3.6)—that is, essentially Theorem L—does imply (6.1).  It should not be
attributed to the supply inequality (1.2) alone.

## 7. Theorem M: assignment-free window costs

For valid forward starts define

\[
 q_i=\min\{\lambda_{\rm eff}(P):
             P\text{ is a complete peak plateau in }W_i\},  \tag{7.1}
\]

where `lambda_eff=lambda` for a directed plateau and `lambda_eff=1` for a
nondirected plateau.  Theorem E makes the set nonempty and `q_i<=2a`.

If a minimum-effective plateau is directed, assign it.  If it is
nondirected, assign the singleton cross-coordinate peak inside it, whose
actual cost is zero and hence at most `q_i=1`.  This gives an actual run
assignment of cost at most `q_i` and span at most `L+1`.

The source phrase “first-complete-plateau assignment realizes `q_i`” is not
correct: the first plateau need not minimize effective cost.  No firstness
is needed for congestion, so choosing a minimizer repairs the proof.

After adding the `L` unassigned tail starts at cap, Theorem I gives

\[
                         \sum_{i=1}^{M_a-L}q_i
                         \ge4a^3-o(a^3).             \tag{7.2}

### 7.1 Exact layer cake

Let

\[
 \operatorname{serv}_0(P)
 =\{i\in[1,M_a-L]:P\subseteq W_i\}                  \tag{7.3}

be the **clipped** service interval.  Then

\[
 \{i:q_i\le t\}
 =\bigcup_{\lambda_{\rm eff}(P)\le t}
     \operatorname{serv}_0(P).                      \tag{7.4}

Since `q_i<=2a`, layer cake gives

\[
\begin{aligned}
 \int_0^{3a}
 \left|\bigcup_{\lambda_{\rm eff}(P)\le t}
       \operatorname{serv}_0(P)\right|dt
 &=\sum_{i=1}^{M_a-L}(3a-q_i)\\
 &\le5a^3+o(a^3).                                   \tag{7.5}
\end{aligned}

This is the correct assignment-free area inequality.  Using the untrimmed
`L-lambda(P)` service intervals changes the union only in the two boundary
start ranges, at most `O(a)` starts for each `t`; after integration the
difference is `O(a^2)`.  Thus the asymptotic source statement survives.

The numerical `5/9` area fraction is correct.  The prose “cheapness must be
clustered” is stronger than (7.5): a small union area may also be spatially
spread but sparse.  What is proved is a joint position-threshold coverage
bound, not clustering by itself.

## 8. Theorem N and MASTER

Put

\[
                         n(t)=\#\{i:q_i>t\}.         \tag{8.1}

For `t>=1`, if `q_i>t`, every complete plateau in `W_i` is directed and has
cost greater than `t`; otherwise a nondirected plateau would have effective
cost one.  In particular `i` belongs to the clipped service interval of at
least one qualifying directed plateau.

Define the untrimmed supply

\[
 \operatorname{supply}(t)
 =\sum_{\substack{P\text{ directed peak}\
                   \lambda(P)>t}}
       (L-\lambda(P)).                               \tag{8.2}

Then, uniformly for `1<=t<=2a`,

\[
                         n(t)
 \le\min\{M_a,\operatorname{supply}(t)\}+O(a).       \tag{8.3}

The `O(a)` absorbs valid-start clipping and the final tail.

For `0<=t<1`, (8.3) need not hold because nondirected plateaux have
effective cost one but are absent from the directed supply.  Use instead
the trivial `n(t)<=M_a`; its integral over an interval of length one is
only `O(a^2)`.

Now

\[
 \sum_iq_i=\int_0^{2a}n(t)\,dt.                    \tag{8.4}

Combining (7.2)--(8.4) proves

\[
 \boxed{
 \int_0^{2a}\min\{M_a,\operatorname{supply}(t)\}\,dt
 \ge4a^3-o(a^3).}                                   \tag{8.5}

This is MASTER.  Its proof is correct after making the harmless
`[0,1)` correction explicit.

## 9. Monotonicity and the supply law

Normalize `t=ca` and write

\[
                         f(c)=\min\{3,s(c)\},
 \qquad s(c)=\frac{\operatorname{supply}(ca)}{a^2}. \tag{9.1}

The function `s`, hence `f`, is nonincreasing: increasing the threshold
only removes plateau summands, whose weights `L-lambda(P)` are fixed.
Equation (8.5) becomes

\[
                         \int_0^2f(u)\,du\ge4-o(1). \tag{9.2}

For a fixed `0<c<4/3`, split the integral:

\[
\begin{aligned}
 \int_0^2f(u)\,du
 &=\int_0^cf(u)\,du+\int_c^2f(u)\,du\\
 &\le3c+(2-c)f(c).                                  \tag{9.3}
\end{aligned}

The first term uses `f<=3`; the second uses monotonicity.  Therefore

\[
 f(c)\ge\frac{4-3c}{2-c}-o(1).                     \tag{9.4}

The right side lies below three in this range, so (9.4) implies

\[
 \boxed{s(c)\ge\frac{4-3c}{2-c}-o(1).}             \tag{9.5}

No differentiation of a cumulative inequality is occurring; this is a
valid one-sided monotonicity argument.

## 10. Plateau-count consequences

Let

\[
 F(c)=\#\{P:P\text{ directed and }\lambda(P)>ca\}. \tag{10.1}

Each qualifying plateau contributes at most

\[
                         L-\lambda(P)
                         <(4-c)a+2                  \tag{10.2}

to supply.  Hence (9.5) gives

\[
 F(c)\ge
 \frac{4-3c}{(2-c)(4-c)}a-o(a).                    \tag{10.3}

At `c=1`,

\[
 \operatorname{supply}(a)\ge a^2-o(a^2),
 \qquad F(1)\ge a/3-o(a).                          \tag{10.4}

As in Section 6, these plateaux occupy distinct coordinate lines.  The
source constants are correct.

For general `c<1`, (10.3) remains a valid plateau **count**, but line
uniqueness does not follow.  The later static assertion

\[
                         F(y)\le6(2-y)a+3            \tag{10.5}

uses “one long plateau per line” and is justified only for `y>=1`.
When `y<1`, several disjoint plateaux of cost greater than `ya` can fit on
one line, so (10.5) requires a multiplicity factor or a different edge
capacity argument.

## 11. False or unsupported side claims

### 11.1 The single-threshold edge-budget check

Section 9.3 says that plateaux of cost `>t` number at most `3a^2/t` and
that each serves `L-t>=2a` starts.  The second assertion has the wrong
direction:

\[
                         \lambda>t
 \quad\Longrightarrow\quad
                         L-\lambda<L-t.             \tag{11.1}

Moreover, an upper bound on the number of plateaux cannot prove that enough
plateaux exist to serve any prescribed number of indices.  Thus this
recorded “negative result” is not a proof that the edge budget never
contradicts a single threshold.  Abstract feasible spectra may establish a
similar conclusion, but (11.1) cannot.

### 11.2 Static satisfiability paragraph

The claimed abstract examples may still be useful exploratory profiles,
but the stated constraint system is not exactly the proved one because its
level-capacity inequality (10.5) is used below `y=1`.  The satisfiability
claim should be rechecked with correct per-line multiplicities before being
entered as a theorem.

### 11.3 Interpretation of Theorem M

The `5/9` area bound constrains the measure of service-interval unions over
threshold.  It does not alone say those intervals form a small number of
spatial clusters.  “Cheapness has limited joint coverage” is proved;
“cheapness must be clustered” requires an additional interval-union
component argument.

## 12. Corrected ledger

### New and valid

* Lemma 9.1.
* Theorem L's coarse component-free bound (3.8), with corrected span proof.
* The two-sided excess ledger (4.2).
* The doubly-blocked lower bound and clustered-pair count after deleting
  boundary starts.
* Theorem M's clipped service-union area law.
* MASTER and the monotone supply law (9.5).
* Plateau-count consequence (10.3), and distinct-line consequence at
  `c=1` (more generally `c>=1`).

### Valid but duplicated or weaker

* Theorem L's elimination of raw component count overlaps the
  first-dangerous theorem.  For `c>1`, use the combined minimum (3.11).
* Corollary S's excess-mass and `c=1` plateau counts follow from the same
  run-spectrum/service framework; Theorem N reproduces the count law but
  not the excess lower bound from pointwise supply alone.

### False as written or overstated

* The `L+lambda+1` span calculation.
* Pairing boundary indices declared doubly blocked.
* “First complete” realizes the minimum `q_i`.
* The single-threshold service-length direction.
* The line-capacity formula for all `y<=1`.
* The claim that the service-union area bound itself proves spatial
  clustering.

The sharpest genuinely new invariant in Section 9 is MASTER/supply, not the
coarse one-threshold excess bound.  It still leaves the static spectrum
feasible and pushes the problem to transition coupling, consistent with
the explicit transparent packets in `THREE_HALVES_TRANSITION_GEOMETRY.md`.
